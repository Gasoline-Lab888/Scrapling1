"""HVAC brand website probe.

Investigates ~30 HVAC / hydronics / underfloor heating / valve brand sites
and emits a triage report plus hvac-ai-crawler-style YAML candidates.

This is a *survey* tool, not a crawler. For each brand it:

  1. Fetches the homepage (HEAD-like behaviour for blockers, then GET)
  2. Tries to locate an English version (path heuristics + hreflang)
  3. Scans the English landing page for links pointing at product / download /
     catalog / brochure / datasheet pages
  4. Records up to a small number of sample PDF URLs (no download)
  5. Records blocked_reason instead of attempting bypass
  6. Writes a hvac-ai-crawler-style YAML candidate per brand

Outputs (all under ./outputs):
  - brand_probe_results.jsonl   - per-brand machine record
  - brand_probe_summary.csv     - flat overview for spreadsheets
  - brand_probe_report.md       - human-readable triage report
  - hvac_yaml_candidates/*.yml  - candidate brand configs

Run:
  python probe_brand_sites.py
  python probe_brand_sites.py --brands daikin viessmann
  python probe_brand_sites.py --use-stealth   # only if you really need it

This script intentionally does *not*:
  - solve captchas
  - bypass Cloudflare / Turnstile
  - use residential proxies or fingerprint spoofing
  - download PDFs in bulk
  - crawl deeply
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import socket
import ssl
import sys
import time
import traceback
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional, Sequence
from urllib.parse import urljoin, urlparse, urlunparse

HERE = Path(__file__).resolve().parent
DEFAULT_BRANDS_YAML = HERE / "selected_brands_30.yml"
OUT_DIR = HERE / "outputs"
YAML_OUT_DIR = OUT_DIR / "hvac_yaml_candidates"

# How long to spend on a single network call.
HTTP_TIMEOUT = 20

# Per-brand polite delay (seconds) between requests.
PER_REQUEST_DELAY = 1.5

# Cap on links/pdfs we record per brand.
MAX_PRODUCT_LINKS = 25
MAX_DOWNLOAD_LINKS = 25
MAX_PDF_LINKS = 15
MAX_CANDIDATE_PAGES_PROBED = 4  # homepage + a few suspects

DOWNLOAD_KEYWORDS = [
    "download", "downloads", "document", "documents", "documentation",
    "catalogue", "catalog", "brochure", "brochures", "datasheet", "data-sheet",
    "data sheets", "technical-documents", "technical documents",
    "tech-docs", "manual", "manuals", "installation-guide", "installation guide",
    "product-documentation", "literature", "media-center", "media center",
    "resources", "support/downloads", "certificate", "certificates",
    "spec-sheet", "spec sheet", "leaflet", "service-manual", "service manual",
]

PRODUCT_KEYWORDS = [
    "product", "products", "produkte", "produits", "produkty",
    "solution", "solutions", "range", "lineup",
    "boiler", "boilers", "heat-pump", "heat pump", "heatpump",
    "air-conditioner", "air conditioner", "ac-units", "vrf",
    "underfloor", "radiant", "valve", "valves", "manifold", "pump",
    "chiller", "indoor-unit", "outdoor-unit",
]

ENGLISH_HINTS = [
    "/en/", "/en-us/", "/en-gb/", "/en_gb/", "/en_us/", "/en-eu/",
    "/en-int/", "/international/", "/global/", "/en/products",
    "/en-ww/", "/en-row/", "/com/en/", "/com/en-",
]

PDF_HREF_RE = re.compile(r"\.pdf(?:[?#]|$)", re.IGNORECASE)
HREF_RE = re.compile(r'href\s*=\s*"([^"]+)"|href\s*=\s*\'([^\']+)\'', re.IGNORECASE)
HREFLANG_RE = re.compile(
    r'<link[^>]+rel=["\']alternate["\'][^>]+hreflang=["\']([^"\']+)["\'][^>]+href=["\']([^"\']+)["\']',
    re.IGNORECASE,
)
HREFLANG_RE_2 = re.compile(
    r'<link[^>]+hreflang=["\']([^"\']+)["\'][^>]+href=["\']([^"\']+)["\']',
    re.IGNORECASE,
)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
LANG_ATTR_RE = re.compile(r'<html[^>]+lang=["\']([^"\']+)["\']', re.IGNORECASE)
META_REFRESH_RE = re.compile(
    r'<meta[^>]+http-equiv=["\']refresh["\'][^>]+content=["\'][^"\']*url=([^"\'\s>]+)',
    re.IGNORECASE,
)

# Patterns suggesting an anti-bot wall.
BLOCKED_BODY_HINTS = [
    ("cloudflare", "cloudflare_challenge"),
    ("attention required! | cloudflare", "cloudflare_block"),
    ("cf-chl", "cloudflare_challenge"),
    ("just a moment", "cloudflare_jschallenge"),
    ("checking your browser", "cloudflare_jschallenge"),
    ("captcha", "captcha"),
    ("turnstile", "cloudflare_turnstile"),
    ("akamai", "akamai_block"),
    ("imperva", "imperva_block"),
    ("incapsula", "imperva_block"),
    ("access denied", "access_denied"),
    ("forbidden", "forbidden"),
    ("please enable javascript", "js_required"),
    ("you need to enable javascript", "js_required"),
]

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


# ---------------------------------------------------------------------------
# Optional dependency: Scrapling fetcher. Fallback to stdlib urllib if missing.
# ---------------------------------------------------------------------------

def _try_import_scrapling():
    try:
        from scrapling.fetchers import Fetcher, StealthyFetcher  # type: ignore
        return Fetcher, StealthyFetcher
    except Exception:
        return None, None


# ---------------------------------------------------------------------------
# YAML helpers - keep it dependency-light.
# ---------------------------------------------------------------------------

def _load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except ImportError:
        return _load_yaml_minimal(path)


def _load_yaml_minimal(path: Path) -> dict:
    """Tiny YAML reader for our specific selected_brands_30.yml shape.

    Supports only what we wrote ourselves: top-level `brands:` list of mappings
    whose values are scalars or flow-style sequences. Not a general parser.
    """
    brands: list[dict] = []
    current: Optional[dict] = None
    with path.open("r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            if stripped.startswith("- "):
                if current is not None:
                    brands.append(current)
                current = {}
                stripped = stripped[2:]
                if ":" in stripped:
                    key, _, val = stripped.partition(":")
                    current[key.strip()] = _coerce(val.strip())
                continue
            if indent >= 4 and current is not None and ":" in stripped:
                key, _, val = stripped.partition(":")
                current[key.strip()] = _coerce(val.strip())
    if current is not None:
        brands.append(current)
    return {"brands": brands}


def _coerce(val: str):
    if not val:
        return ""
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if not inner:
            return []
        return [p.strip().strip('"').strip("'") for p in inner.split(",") if p.strip()]
    if val in {"true", "True"}:
        return True
    if val in {"false", "False"}:
        return False
    return val.strip('"').strip("'")


def _dump_yaml(obj, path: Path) -> None:
    try:
        import yaml  # type: ignore
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(obj, f, sort_keys=False, allow_unicode=True)
    except ImportError:
        with path.open("w", encoding="utf-8") as f:
            _dump_yaml_minimal(obj, f, 0)


def _dump_yaml_minimal(obj, f, indent: int):
    pad = "  " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                f.write(f"{pad}{k}:\n")
                _dump_yaml_minimal(v, f, indent + 1)
            else:
                f.write(f"{pad}{k}: {_yaml_scalar(v)}\n")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                f.write(f"{pad}-\n")
                _dump_yaml_minimal(item, f, indent + 1)
            else:
                f.write(f"{pad}- {_yaml_scalar(item)}\n")
    else:
        f.write(f"{pad}{_yaml_scalar(obj)}\n")


def _yaml_scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if any(ch in s for ch in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", "<", ">", "=", "!", "%", "@", "`", "\n", '"', "'"]) or s.strip() != s:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


# ---------------------------------------------------------------------------
# Result records.
# ---------------------------------------------------------------------------

@dataclass
class FetchResult:
    url: str
    final_url: str = ""
    status: Optional[int] = None
    ok: bool = False
    blocked_reason: str = ""
    error: str = ""
    body: str = ""
    elapsed_ms: int = 0
    fetcher_used: str = ""
    notes: list = field(default_factory=list)


@dataclass
class BrandProbeResult:
    brand: str
    brand_name: str
    website: str
    categories: list = field(default_factory=list)
    country_origin: str = ""
    homepage_status: Optional[int] = None
    homepage_ok: bool = False
    homepage_final_url: str = ""
    has_english_version: bool = False
    english_url: str = ""
    english_detection: str = ""  # how we found it
    has_product_pages: bool = False
    product_page_examples: list = field(default_factory=list)
    has_download_center: bool = False
    download_page_examples: list = field(default_factory=list)
    pdf_examples: list = field(default_factory=list)
    needs_js_render: bool = False
    js_render_evidence: str = ""
    needs_login: bool = False
    blocked_reason: str = ""
    errors: list = field(default_factory=list)
    fetcher_used: str = ""
    worth_promoting: bool = False
    worth_promoting_reason: str = ""
    notes: str = ""
    elapsed_total_ms: int = 0


# ---------------------------------------------------------------------------
# Fetcher abstraction.
# ---------------------------------------------------------------------------

class Probe:
    def __init__(self, use_stealth: bool = False, force_stdlib: bool = False):
        self.use_stealth = use_stealth
        self.force_stdlib = force_stdlib
        self._Fetcher, self._StealthyFetcher = (None, None)
        if not force_stdlib:
            self._Fetcher, self._StealthyFetcher = _try_import_scrapling()

    def fetch(self, url: str) -> FetchResult:
        start = time.monotonic()
        # 1) Prefer Scrapling Fetcher when available.
        if self._Fetcher is not None:
            res = self._fetch_scrapling(url)
            if res is not None:
                res.elapsed_ms = int((time.monotonic() - start) * 1000)
                # If page looks blocked and stealth is enabled, escalate.
                if self.use_stealth and self._StealthyFetcher is not None and res.blocked_reason and not res.ok:
                    stealth_res = self._fetch_stealth(url)
                    if stealth_res is not None:
                        stealth_res.elapsed_ms = int((time.monotonic() - start) * 1000)
                        # Prefer stealth only when it actually got further than the
                        # plain Fetcher (real status / non-blocked body). Otherwise
                        # the stealth failure (e.g. missing Playwright browser)
                        # would clobber the legitimate blocked_reason from Fetcher.
                        stealth_is_better = stealth_res.ok or (
                            stealth_res.status is not None
                            and not stealth_res.error
                        )
                        if stealth_is_better:
                            return stealth_res
                        # Keep the Fetcher result; annotate that stealth was tried.
                        if stealth_res.error:
                            res.notes.append(stealth_res.error)
                        res.notes.append(
                            f"stealth_fallback_no_improvement(blocked={stealth_res.blocked_reason or '-'},status={stealth_res.status})"
                        )
                return res
        # 2) Stdlib fallback.
        res = self._fetch_stdlib(url)
        res.elapsed_ms = int((time.monotonic() - start) * 1000)
        return res

    def _fetch_scrapling(self, url: str) -> Optional[FetchResult]:
        try:
            page = self._Fetcher.get(
                url,
                timeout=HTTP_TIMEOUT,
                stealthy_headers=True,
                follow_redirects=True,
            )
        except Exception as exc:
            return FetchResult(
                url=url,
                error=f"scrapling_fetcher_exception: {type(exc).__name__}: {exc}",
                fetcher_used="scrapling.Fetcher",
                blocked_reason=_classify_network_exc(exc),
            )
        status = getattr(page, "status", None)
        body = _coerce_body_to_text(page)
        final_url = getattr(page, "url", url) or url
        ok = bool(status and 200 <= int(status) < 400)
        blocked = _classify_block(status, body)
        return FetchResult(
            url=url,
            final_url=final_url,
            status=int(status) if status else None,
            ok=ok and not blocked,
            blocked_reason=blocked,
            body=body or "",
            fetcher_used="scrapling.Fetcher",
        )

    def _fetch_stealth(self, url: str) -> Optional[FetchResult]:
        try:
            page = self._StealthyFetcher.fetch(
                url,
                timeout=HTTP_TIMEOUT * 1000,
                headless=True,
                network_idle=False,
            )
        except Exception as exc:
            return FetchResult(
                url=url,
                error=f"stealthy_fetcher_exception: {type(exc).__name__}: {exc}",
                fetcher_used="scrapling.StealthyFetcher",
                blocked_reason=_classify_network_exc(exc),
            )
        status = getattr(page, "status", None)
        body = _coerce_body_to_text(page)
        final_url = getattr(page, "url", url) or url
        ok = bool(status and 200 <= int(status) < 400)
        blocked = _classify_block(status, body)
        return FetchResult(
            url=url,
            final_url=final_url,
            status=int(status) if status else None,
            ok=ok and not blocked,
            blocked_reason=blocked,
            body=body or "",
            fetcher_used="scrapling.StealthyFetcher",
        )

    def _fetch_stdlib(self, url: str) -> FetchResult:
        import urllib.request
        import urllib.error
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
            },
        )
        try:
            ctx = ssl.create_default_context()
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT, context=ctx) as resp:
                status = resp.status
                final_url = resp.geturl()
                raw = resp.read(800_000)  # cap body size
                encoding = resp.headers.get_content_charset() or "utf-8"
                try:
                    body = raw.decode(encoding, errors="replace")
                except LookupError:
                    body = raw.decode("utf-8", errors="replace")
                blocked = _classify_block(status, body)
                return FetchResult(
                    url=url,
                    final_url=final_url,
                    status=status,
                    ok=(200 <= status < 400) and not blocked,
                    blocked_reason=blocked,
                    body=body,
                    fetcher_used="stdlib.urllib",
                )
        except urllib.error.HTTPError as exc:
            try:
                raw = exc.read(400_000) if exc.fp else b""
                body = raw.decode("utf-8", errors="replace")
            except Exception:
                body = ""
            blocked = _classify_block(exc.code, body)
            return FetchResult(
                url=url,
                final_url=url,
                status=exc.code,
                ok=False,
                blocked_reason=blocked or f"http_{exc.code}",
                body=body,
                fetcher_used="stdlib.urllib",
            )
        except urllib.error.URLError as exc:
            return FetchResult(
                url=url,
                final_url=url,
                status=None,
                ok=False,
                blocked_reason=_classify_network_exc(exc),
                error=f"urlerror: {exc.reason}",
                fetcher_used="stdlib.urllib",
            )
        except (socket.timeout, TimeoutError) as exc:
            return FetchResult(
                url=url,
                final_url=url,
                status=None,
                ok=False,
                blocked_reason="timeout",
                error=str(exc),
                fetcher_used="stdlib.urllib",
            )
        except ssl.SSLError as exc:
            return FetchResult(
                url=url,
                final_url=url,
                status=None,
                ok=False,
                blocked_reason="ssl_error",
                error=str(exc),
                fetcher_used="stdlib.urllib",
            )
        except Exception as exc:
            return FetchResult(
                url=url,
                final_url=url,
                status=None,
                ok=False,
                blocked_reason=_classify_network_exc(exc),
                error=f"{type(exc).__name__}: {exc}",
                fetcher_used="stdlib.urllib",
            )


def _classify_network_exc(exc: BaseException) -> str:
    name = type(exc).__name__.lower()
    msg = str(exc).lower()
    if "timeout" in name or "timed out" in msg:
        return "timeout"
    if "ssl" in name or "certificate" in msg:
        return "ssl_error"
    if "nodename" in msg or "name or service not known" in msg or "name resolution" in msg or "dns" in msg:
        return "dns_error"
    if "connection refused" in msg:
        return "connection_refused"
    if "connection reset" in msg:
        return "connection_reset"
    if "unreachable" in msg:
        return "network_unreachable"
    return ""


def _coerce_body_to_text(page: object) -> str:
    """Return page body as a `str`, decoding bytes if needed.

    Scrapling's Fetcher / StealthyFetcher may expose `body` as bytes, str,
    or a None-ish value depending on backend. The probe's downstream regex
    helpers all assume str, so normalize here.
    """
    raw = getattr(page, "body", None)
    if raw is None:
        try:
            raw = str(page)
        except Exception:
            return ""
    if isinstance(raw, bytes):
        try:
            return raw.decode("utf-8", errors="replace")
        except Exception:
            try:
                return raw.decode("latin-1", errors="replace")
            except Exception:
                return ""
    if isinstance(raw, str):
        return raw
    try:
        return str(raw)
    except Exception:
        return ""


def _classify_block(status: Optional[int], body: str) -> str:
    if status in (401,):
        return "login_required"
    if status in (403,):
        return "forbidden_403"
    if status in (429,):
        return "rate_limited_429"
    if status in (451,):
        return "legal_block_451"
    if status in (503,):
        # 503 + cloudflare body = challenge.
        if "cloudflare" in (body or "").lower():
            return "cloudflare_challenge"
        return "service_unavailable_503"
    lower = (body or "").lower()
    for needle, reason in BLOCKED_BODY_HINTS:
        if needle in lower:
            return reason
    return ""


# ---------------------------------------------------------------------------
# Page analysis helpers.
# ---------------------------------------------------------------------------

def _extract_hrefs(html: str) -> list[str]:
    out = []
    for m in HREF_RE.finditer(html or ""):
        h = m.group(1) or m.group(2)
        if h:
            out.append(h.strip())
    return out


def _extract_title(html: str) -> str:
    m = TITLE_RE.search(html or "")
    if not m:
        return ""
    title = re.sub(r"\s+", " ", m.group(1)).strip()
    return title[:200]


def _detect_html_lang(html: str) -> str:
    m = LANG_ATTR_RE.search(html or "")
    return (m.group(1) if m else "").strip().lower()


def _hreflang_alternates(html: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for rx in (HREFLANG_RE, HREFLANG_RE_2):
        for m in rx.finditer(html or ""):
            lang = m.group(1).strip().lower()
            href = m.group(2).strip()
            if lang and href and lang not in out:
                out[lang] = href
    return out


def _meta_refresh_target(html: str, base_url: str) -> str:
    m = META_REFRESH_RE.search(html or "")
    if not m:
        return ""
    return urljoin(base_url, m.group(1).strip().strip('"').strip("'"))


def _looks_like_english_url(url: str) -> bool:
    u = url.lower()
    return any(h in u for h in ENGLISH_HINTS)


def _same_registered_domain(a: str, b: str) -> bool:
    pa, pb = urlparse(a).netloc.lower(), urlparse(b).netloc.lower()
    if not pa or not pb:
        return False
    pa = pa.split(":")[0].lstrip("www.")
    pb = pb.split(":")[0].lstrip("www.")
    if pa == pb:
        return True
    # crude registered-domain compare on last 2 labels
    return pa.split(".")[-2:] == pb.split(".")[-2:]


def _absolutize(href: str, base: str) -> str:
    if not href:
        return ""
    if href.startswith("javascript:") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#"):
        return ""
    return urljoin(base, href)


def _classify_link(url: str) -> tuple[bool, bool, bool]:
    """Return (is_product, is_download, is_pdf) hints."""
    u = url.lower()
    is_pdf = bool(PDF_HREF_RE.search(u))
    is_download = any(kw in u for kw in DOWNLOAD_KEYWORDS)
    is_product = any(kw in u for kw in PRODUCT_KEYWORDS)
    return is_product, is_download, is_pdf


def _js_render_evidence(html: str) -> str:
    """Heuristic: does this page rely on client-side rendering?"""
    if not html:
        return ""
    lower = html.lower()
    visible = re.sub(r"<script[\s\S]*?</script>", " ", lower)
    visible = re.sub(r"<style[\s\S]*?</style>", " ", visible)
    visible = re.sub(r"<[^>]+>", " ", visible)
    visible_text_len = len(re.sub(r"\s+", " ", visible).strip())
    script_count = lower.count("<script")
    indicators = []
    if visible_text_len < 400 and script_count >= 3:
        indicators.append(f"thin_body(text={visible_text_len},scripts={script_count})")
    for needle in ("ng-app", "data-reactroot", '"react"', "window.__nuxt__", "window.__next_data__",
                   "vue.js", "ng-version", "spa-shell"):
        if needle in lower:
            indicators.append(needle)
    return ",".join(indicators)


def _detect_login_wall(html: str) -> bool:
    lower = (html or "").lower()
    if "sign in to continue" in lower:
        return True
    if "members only" in lower:
        return True
    if "please log in" in lower:
        return True
    return False


# ---------------------------------------------------------------------------
# English-version detection.
# ---------------------------------------------------------------------------

def _find_english_url(homepage_url: str, html: str) -> tuple[str, str]:
    """Return (english_url, detection_method) or ('', '')."""
    if not html:
        return "", ""
    base = homepage_url

    # 1) hreflang alternates.
    alternates = _hreflang_alternates(html)
    if alternates:
        for key in ("en", "en-us", "en-gb", "en-int", "en-eu", "en-ww", "x-default"):
            if key in alternates:
                cand = _absolutize(alternates[key], base)
                if cand:
                    return cand, f"hreflang:{key}"
        # Any "en*" hreflang.
        for k, v in alternates.items():
            if k.startswith("en"):
                cand = _absolutize(v, base)
                if cand:
                    return cand, f"hreflang:{k}"

    # 2) Same-domain links matching English path hints.
    candidates: list[tuple[str, str]] = []
    for href in _extract_hrefs(html):
        absu = _absolutize(href, base)
        if not absu:
            continue
        if not _same_registered_domain(absu, base):
            continue
        if _looks_like_english_url(absu):
            candidates.append((absu, "path_hint"))

    if candidates:
        # Prefer "/en/" and "/en-us/" style exact segments.
        def score(u: str) -> int:
            ul = u.lower()
            s = 0
            if "/en/" in ul:
                s += 10
            if "/en-us/" in ul or "/en-gb/" in ul:
                s += 8
            if "/global/" in ul:
                s += 5
            if "/international/" in ul:
                s += 4
            return s
        candidates.sort(key=lambda x: score(x[0]), reverse=True)
        return candidates[0]

    # 3) If page lang is already English, return homepage.
    lang = _detect_html_lang(html)
    if lang.startswith("en"):
        return base, f"html_lang:{lang}"

    return "", ""


# ---------------------------------------------------------------------------
# Brand probe core.
# ---------------------------------------------------------------------------

def probe_brand(brand: dict, prober: Probe) -> BrandProbeResult:
    result = BrandProbeResult(
        brand=brand.get("brand", ""),
        brand_name=brand.get("brand_name", ""),
        website=brand.get("website", ""),
        categories=brand.get("categories") or [],
        country_origin=brand.get("country_origin", ""),
        notes=brand.get("notes", ""),
    )
    if not result.website:
        result.errors.append("missing_website")
        return result

    t_start = time.monotonic()
    homepage = prober.fetch(result.website)
    result.fetcher_used = homepage.fetcher_used
    result.homepage_status = homepage.status
    result.homepage_ok = homepage.ok
    result.homepage_final_url = homepage.final_url or result.website

    if homepage.blocked_reason and not homepage.ok:
        result.blocked_reason = homepage.blocked_reason
    if homepage.error:
        result.errors.append(homepage.error)
    for note in homepage.notes:
        if note and note not in result.errors:
            result.errors.append(note)

    body = homepage.body or ""

    # JS-rendering hint.
    js_evidence = _js_render_evidence(body)
    if js_evidence:
        result.needs_js_render = True
        result.js_render_evidence = js_evidence

    # Login wall hint.
    if _detect_login_wall(body):
        result.needs_login = True

    # English detection.
    english_url, detection = ("", "")
    if homepage.ok and body:
        english_url, detection = _find_english_url(homepage.final_url or result.website, body)
    if english_url:
        result.has_english_version = True
        result.english_url = english_url
        result.english_detection = detection

    # Fetch English page if it differs from homepage.
    english_body = body
    english_final = result.homepage_final_url
    if english_url and english_url != (homepage.final_url or result.website):
        time.sleep(PER_REQUEST_DELAY)
        en_fetch = prober.fetch(english_url)
        if en_fetch.error:
            result.errors.append(en_fetch.error)
        if en_fetch.blocked_reason and not result.blocked_reason:
            result.blocked_reason = en_fetch.blocked_reason
        if en_fetch.ok and en_fetch.body:
            english_body = en_fetch.body
            english_final = en_fetch.final_url or english_url
            if _js_render_evidence(en_fetch.body):
                result.needs_js_render = True
            if _detect_login_wall(en_fetch.body):
                result.needs_login = True

    # Link scan on English page.
    product_links: list[str] = []
    download_links: list[str] = []
    pdf_links: list[str] = []

    seen = set()
    for href in _extract_hrefs(english_body):
        absu = _absolutize(href, english_final)
        if not absu or absu in seen:
            continue
        seen.add(absu)
        if not _same_registered_domain(absu, english_final):
            continue
        is_product, is_download, is_pdf = _classify_link(absu)
        if is_pdf and len(pdf_links) < MAX_PDF_LINKS:
            pdf_links.append(absu)
        if is_download and len(download_links) < MAX_DOWNLOAD_LINKS:
            download_links.append(absu)
        if is_product and len(product_links) < MAX_PRODUCT_LINKS:
            product_links.append(absu)

    # If no PDFs on landing, peek at top download candidate (small probe budget).
    extra_pages_probed = 0
    if not pdf_links and download_links and not result.blocked_reason:
        for cand in download_links[:MAX_CANDIDATE_PAGES_PROBED]:
            if extra_pages_probed >= MAX_CANDIDATE_PAGES_PROBED:
                break
            extra_pages_probed += 1
            time.sleep(PER_REQUEST_DELAY)
            sub = prober.fetch(cand)
            if sub.error:
                result.errors.append(f"download_probe_error[{cand}]: {sub.error}")
            if sub.blocked_reason and not result.blocked_reason:
                result.blocked_reason = sub.blocked_reason
            if not sub.ok:
                continue
            if not result.needs_js_render and _js_render_evidence(sub.body):
                result.needs_js_render = True
            for h in _extract_hrefs(sub.body):
                absu = _absolutize(h, sub.final_url or cand)
                if not absu or absu in seen:
                    continue
                seen.add(absu)
                if not _same_registered_domain(absu, sub.final_url or cand):
                    continue
                _, _, is_pdf = _classify_link(absu)
                if is_pdf and len(pdf_links) < MAX_PDF_LINKS:
                    pdf_links.append(absu)
            if pdf_links:
                break

    result.product_page_examples = product_links
    result.has_product_pages = bool(product_links)
    result.download_page_examples = download_links
    result.has_download_center = bool(download_links)
    result.pdf_examples = pdf_links

    # worth-promoting heuristic.
    worth = result.homepage_ok and result.has_english_version and (result.has_download_center or result.pdf_examples)
    if worth and result.blocked_reason:
        worth = False
    result.worth_promoting = bool(worth)
    if not result.worth_promoting:
        reasons = []
        if not result.homepage_ok:
            reasons.append(f"homepage_not_ok(status={result.homepage_status})")
        if not result.has_english_version:
            reasons.append("no_english_version")
        if not (result.has_download_center or result.pdf_examples):
            reasons.append("no_download_or_pdf_links")
        if result.blocked_reason:
            reasons.append(f"blocked:{result.blocked_reason}")
        result.worth_promoting_reason = ",".join(reasons) or "unknown"
    else:
        bits = []
        if result.pdf_examples:
            bits.append(f"pdf_seen({len(result.pdf_examples)})")
        if result.has_download_center:
            bits.append(f"download_pages({len(result.download_page_examples)})")
        if result.has_product_pages:
            bits.append(f"product_pages({len(result.product_page_examples)})")
        result.worth_promoting_reason = ",".join(bits)

    result.elapsed_total_ms = int((time.monotonic() - t_start) * 1000)
    return result


# ---------------------------------------------------------------------------
# YAML candidate generation (hvac-ai-crawler-style).
# ---------------------------------------------------------------------------

def build_yaml_candidate(res: BrandProbeResult) -> dict:
    """Produce a hvac-ai-crawler-compatible draft config.

    The shape mirrors the conventions described in the task brief:
      brand, brand_name, website, entry_url, seed_urls, max_pages,
      url_scope.path_prefix, page_role_classification, fields, filters,
      reject_url_patterns, download_link_selector, global_download_threshold.

    Values are best-effort drafts; a human is expected to review.
    """
    entry_url = res.english_url or res.homepage_final_url or res.website
    parsed_entry = urlparse(entry_url)
    path_prefix = ""
    if parsed_entry.path:
        first_seg = parsed_entry.path.lstrip("/").split("/", 1)[0]
        if first_seg and len(first_seg) <= 12:
            path_prefix = f"/{first_seg}/"

    seed_urls = []
    if entry_url:
        seed_urls.append(entry_url)
    # Use download centers as natural seeds.
    for u in res.download_page_examples[:5]:
        if u not in seed_urls:
            seed_urls.append(u)
    # And a couple of product pages.
    for u in res.product_page_examples[:5]:
        if u not in seed_urls:
            seed_urls.append(u)

    candidate = {
        "brand": res.brand,
        "brand_name": res.brand_name,
        "website": res.website,
        "entry_url": entry_url,
        "seed_urls": seed_urls,
        "max_pages": 200,
        "url_scope": {
            "path_prefix": path_prefix,
            "same_registered_domain": True,
        },
        "page_role_classification": {
            "homepage": [r"^/?$", r"^/(en|en-us|en-gb)/?$"],
            "product": [r"/product", r"/products", r"/range", r"/solutions"],
            "download": [
                r"/download", r"/downloads",
                r"/document", r"/documents", r"/documentation",
                r"/catalog", r"/catalogue", r"/brochure",
                r"/datasheet", r"/manual", r"/literature",
                r"/technical-document", r"/product-documentation",
                r"/certificate",
            ],
        },
        "fields": {
            "title": {"selector": "h1", "type": "text"},
            "description": {"selector": "meta[name=description]", "type": "attr", "attr": "content"},
        },
        "filters": {
            "language": "en",
            "min_pdf_size_kb": 30,
            "max_pdf_size_mb": 60,
        },
        "reject_url_patterns": [
            r"/(de|fr|it|es|pt|nl|pl|ru|zh|jp|ja|ko|tr|ar)(/|$)",
            r"/news/", r"/blog/", r"/press/", r"/career", r"/jobs",
            r"/legal/", r"/privacy", r"/cookie", r"/contact",
            r"\?lang=(?!en)",
        ],
        "download_link_selector": "a[href$='.pdf'], a[href*='/download'], a[href*='/documents/'], a[href*='/datasheet']",
        "global_download_threshold": 500,
        "probe_metadata": {
            "homepage_status": res.homepage_status,
            "homepage_ok": res.homepage_ok,
            "needs_js_render": res.needs_js_render,
            "js_render_evidence": res.js_render_evidence,
            "needs_login": res.needs_login,
            "blocked_reason": res.blocked_reason,
            "english_detection": res.english_detection,
            "fetcher_used": res.fetcher_used,
            "worth_promoting": res.worth_promoting,
            "worth_promoting_reason": res.worth_promoting_reason,
            "pdf_example_count": len(res.pdf_examples),
            "download_link_count": len(res.download_page_examples),
            "product_link_count": len(res.product_page_examples),
        },
        "pdf_examples": res.pdf_examples,
    }

    # If JS rendering is detected, surface a hint.
    if res.needs_js_render:
        candidate["render"] = {
            "engine": "playwright",
            "reason": "probe_detected_spa_or_thin_html",
        }

    return candidate


# ---------------------------------------------------------------------------
# Output writers.
# ---------------------------------------------------------------------------

def write_jsonl(results: Sequence[BrandProbeResult], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(asdict(r), ensure_ascii=False) + "\n")


def write_csv(results: Sequence[BrandProbeResult], path: Path) -> None:
    cols = [
        "brand", "brand_name", "website", "homepage_status", "homepage_ok",
        "has_english_version", "english_url", "has_product_pages",
        "has_download_center", "pdf_count", "needs_js_render", "needs_login",
        "blocked_reason", "worth_promoting", "worth_promoting_reason",
        "fetcher_used", "elapsed_total_ms",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in results:
            w.writerow([
                r.brand, r.brand_name, r.website, r.homepage_status, r.homepage_ok,
                r.has_english_version, r.english_url, r.has_product_pages,
                r.has_download_center, len(r.pdf_examples), r.needs_js_render,
                r.needs_login, r.blocked_reason, r.worth_promoting,
                r.worth_promoting_reason, r.fetcher_used, r.elapsed_total_ms,
            ])


def write_markdown_report(results: Sequence[BrandProbeResult], path: Path) -> None:
    total = len(results)
    promotable = [r for r in results if r.worth_promoting]
    blocked = [r for r in results if r.blocked_reason]
    js_heavy = [r for r in results if r.needs_js_render]

    lines: list[str] = []
    lines.append("# HVAC Brand Site Probe Report")
    lines.append("")
    lines.append(f"- Brands probed: **{total}**")
    lines.append(f"- Worth promoting to hvac-ai-crawler: **{len(promotable)}**")
    lines.append(f"- Blocked / requires special handling: **{len(blocked)}**")
    lines.append(f"- Likely JS-rendered: **{len(js_heavy)}**")
    lines.append("")
    lines.append("## Summary table")
    lines.append("")
    lines.append("| Brand | EN? | Product | Download | PDFs | JS | Blocked | Promote |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in results:
        lines.append(
            f"| {r.brand_name} | {'Y' if r.has_english_version else '-'} | "
            f"{'Y' if r.has_product_pages else '-'} | "
            f"{'Y' if r.has_download_center else '-'} | "
            f"{len(r.pdf_examples)} | "
            f"{'Y' if r.needs_js_render else '-'} | "
            f"{r.blocked_reason or '-'} | "
            f"{'Y' if r.worth_promoting else '-'} |"
        )
    lines.append("")

    lines.append("## Per-brand detail")
    lines.append("")
    for r in results:
        lines.append(f"### {r.brand_name} (`{r.brand}`)")
        lines.append("")
        lines.append(f"- Website: {r.website}")
        lines.append(f"- Final homepage URL: {r.homepage_final_url or '-'}")
        lines.append(f"- Homepage status: {r.homepage_status} (ok={r.homepage_ok})")
        lines.append(f"- English URL: {r.english_url or '-'} ({r.english_detection or 'n/a'})")
        lines.append(f"- Needs JS render: {r.needs_js_render} ({r.js_render_evidence or 'n/a'})")
        lines.append(f"- Needs login: {r.needs_login}")
        lines.append(f"- Blocked reason: {r.blocked_reason or '-'}")
        lines.append(f"- Fetcher used: {r.fetcher_used}")
        lines.append(f"- Worth promoting: {r.worth_promoting} — {r.worth_promoting_reason}")
        if r.product_page_examples:
            lines.append("- Product page samples:")
            for u in r.product_page_examples[:8]:
                lines.append(f"  - {u}")
        if r.download_page_examples:
            lines.append("- Download page samples:")
            for u in r.download_page_examples[:8]:
                lines.append(f"  - {u}")
        if r.pdf_examples:
            lines.append("- PDF samples:")
            for u in r.pdf_examples[:8]:
                lines.append(f"  - {u}")
        if r.errors:
            lines.append("- Errors:")
            for e in r.errors[:6]:
                lines.append(f"  - `{e}`")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_yaml_candidates(results: Sequence[BrandProbeResult], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for r in results:
        if not r.brand:
            continue
        candidate = build_yaml_candidate(r)
        path = out_dir / f"{r.brand}.yml"
        _dump_yaml(candidate, path)


# ---------------------------------------------------------------------------
# CLI.
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--brands-file", default=str(DEFAULT_BRANDS_YAML), help="Path to selected_brands_30.yml")
    ap.add_argument("--brands", nargs="*", default=None, help="Only probe these brand IDs")
    ap.add_argument("--out-dir", default=str(OUT_DIR), help="Output directory")
    ap.add_argument("--use-stealth", action="store_true",
                    help="Allow StealthyFetcher escalation when blocked. Off by default.")
    ap.add_argument("--force-stdlib", action="store_true",
                    help="Force urllib fallback even if scrapling.Fetcher is importable.")
    ap.add_argument("--limit", type=int, default=0, help="Max number of brands to probe (0=all)")
    args = ap.parse_args(argv)

    brands_yaml = Path(args.brands_file)
    if not brands_yaml.exists():
        print(f"[fatal] brands file not found: {brands_yaml}", file=sys.stderr)
        return 2

    out_dir = Path(args.out_dir)
    yaml_out_dir = out_dir / "hvac_yaml_candidates"
    out_dir.mkdir(parents=True, exist_ok=True)
    yaml_out_dir.mkdir(parents=True, exist_ok=True)

    data = _load_yaml(brands_yaml)
    brands_all = data.get("brands") or []
    if args.brands:
        wanted = set(args.brands)
        brands = [b for b in brands_all if b.get("brand") in wanted]
        missing = wanted - {b.get("brand") for b in brands}
        if missing:
            print(f"[warn] unknown brand ids: {sorted(missing)}", file=sys.stderr)
    else:
        brands = brands_all
    if args.limit:
        brands = brands[: args.limit]

    print(f"[info] probing {len(brands)} brands. use_stealth={args.use_stealth} force_stdlib={args.force_stdlib}")
    prober = Probe(use_stealth=args.use_stealth, force_stdlib=args.force_stdlib)

    results: list[BrandProbeResult] = []
    for i, brand in enumerate(brands, 1):
        bid = brand.get("brand", "?")
        print(f"[{i:>2}/{len(brands)}] probing {bid} ({brand.get('website')})")
        try:
            res = probe_brand(brand, prober)
        except Exception as exc:
            print(f"  [error] {bid} crashed: {exc}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            res = BrandProbeResult(
                brand=bid,
                brand_name=brand.get("brand_name", ""),
                website=brand.get("website", ""),
                categories=brand.get("categories") or [],
                country_origin=brand.get("country_origin", ""),
                notes=brand.get("notes", ""),
                errors=[f"probe_crashed: {type(exc).__name__}: {exc}"],
            )
        bits = []
        if res.homepage_ok:
            bits.append(f"home_ok({res.homepage_status})")
        else:
            bits.append(f"home_FAIL({res.homepage_status})")
        if res.has_english_version:
            bits.append("en")
        if res.has_download_center:
            bits.append(f"dl({len(res.download_page_examples)})")
        if res.pdf_examples:
            bits.append(f"pdf({len(res.pdf_examples)})")
        if res.blocked_reason:
            bits.append(f"blocked:{res.blocked_reason}")
        if res.worth_promoting:
            bits.append("PROMOTE")
        print(f"    -> {' '.join(bits)}")
        results.append(res)
        time.sleep(PER_REQUEST_DELAY)

    write_jsonl(results, out_dir / "brand_probe_results.jsonl")
    write_csv(results, out_dir / "brand_probe_summary.csv")
    write_markdown_report(results, out_dir / "brand_probe_report.md")
    write_yaml_candidates(results, yaml_out_dir)

    promote_n = sum(1 for r in results if r.worth_promoting)
    blocked_n = sum(1 for r in results if r.blocked_reason)
    print(
        f"[done] {len(results)} probed | promotable={promote_n} | blocked={blocked_n} | "
        f"outputs in {out_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
