"""Unit tests for hvac_brand_probe.probe_brand_sites helpers.

These cover the pure-Python helpers that don't need network access:
classification, body coercion, English-URL detection, link classification,
and YAML candidate shaping.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
PROBE_DIR = HERE.parent
if str(PROBE_DIR) not in sys.path:
    sys.path.insert(0, str(PROBE_DIR))

import probe_brand_sites as probe  # noqa: E402


# ---------------------------------------------------------------------------
# _classify_block
# ---------------------------------------------------------------------------

class TestClassifyBlock:
    def test_sandbox_egress_block_via_body_takes_priority_over_403(self):
        # The sandbox/CI proxy returns 403 with a fixed short body. We must
        # NOT classify this as a brand WAF 403, otherwise the report would
        # mislead reviewers into thinking the brand site itself is the
        # blocker.
        assert (
            probe._classify_block(403, "Host not in allowlist")
            == "sandbox_egress_block"
        )

    def test_sandbox_egress_block_detected_in_header_text(self):
        body = "<html>x-deny-reason: host_not_allowed</html>"
        assert probe._classify_block(403, body) == "sandbox_egress_block"

    def test_cloudflare_challenge_body_wins_over_status_200(self):
        assert (
            probe._classify_block(200, "Just a moment...")
            == "cloudflare_jschallenge"
        )

    def test_turnstile_in_body(self):
        body = "<div class='cf-turnstile' data-sitekey='x'></div>"
        assert probe._classify_block(200, body) == "cloudflare_turnstile"

    def test_status_403_with_no_body_falls_back_to_forbidden_403(self):
        assert probe._classify_block(403, "") == "forbidden_403"

    def test_status_401(self):
        assert probe._classify_block(401, "") == "login_required"

    def test_status_429(self):
        assert probe._classify_block(429, "") == "rate_limited_429"

    def test_status_451(self):
        assert probe._classify_block(451, "") == "legal_block_451"

    def test_status_503_plain(self):
        assert probe._classify_block(503, "Service Unavailable") == "service_unavailable_503"

    def test_status_503_with_cloudflare_body_is_challenge(self):
        body = "<html>cloudflare error</html>"
        assert probe._classify_block(503, body) == "cloudflare_challenge"

    def test_status_200_clean_body_is_not_blocked(self):
        assert probe._classify_block(200, "<html><body>Hello</body></html>") == ""

    def test_status_none_with_empty_body_is_not_blocked(self):
        assert probe._classify_block(None, "") == ""


# ---------------------------------------------------------------------------
# _coerce_body_to_text
# ---------------------------------------------------------------------------

class _PageWithBody:
    def __init__(self, body):
        self.body = body


class _PageNoBody:
    def __str__(self):
        return "<html>from-str</html>"


class TestCoerceBodyToText:
    def test_bytes_body_decoded_utf8(self):
        page = _PageWithBody(b"<html>caf\xc3\xa9</html>")
        out = probe._coerce_body_to_text(page)
        assert isinstance(out, str)
        assert "café" in out

    def test_bytes_body_invalid_utf8_replaces(self):
        page = _PageWithBody(b"\xff\xfe<html>x</html>")
        out = probe._coerce_body_to_text(page)
        assert isinstance(out, str)
        assert "<html>x</html>" in out

    def test_str_body_passthrough(self):
        page = _PageWithBody("<html>plain</html>")
        assert probe._coerce_body_to_text(page) == "<html>plain</html>"

    def test_none_body_falls_back_to_str_page(self):
        page = _PageNoBody()
        out = probe._coerce_body_to_text(page)
        assert "<html>from-str</html>" in out

    def test_unknown_body_type_is_stringified(self):
        page = _PageWithBody(12345)
        assert probe._coerce_body_to_text(page) == "12345"


# ---------------------------------------------------------------------------
# Link classification + extraction
# ---------------------------------------------------------------------------

class TestClassifyLink:
    def test_pdf_extension(self):
        is_p, is_d, is_pdf = probe._classify_link("https://x.com/manuals/foo.pdf")
        assert is_pdf is True

    def test_pdf_extension_with_query(self):
        is_p, is_d, is_pdf = probe._classify_link("https://x.com/file.pdf?v=2")
        assert is_pdf is True

    def test_download_keyword(self):
        is_p, is_d, _ = probe._classify_link("https://x.com/en/downloads/index")
        assert is_d is True

    def test_product_keyword(self):
        is_p, _, _ = probe._classify_link("https://x.com/en/products/heat-pump")
        assert is_p is True

    def test_unrelated_link(self):
        assert probe._classify_link("https://x.com/about/company") == (False, False, False)


def test_extract_hrefs_picks_up_both_quote_styles():
    html = """
        <a href="/en/products">Products</a>
        <a href='/downloads/manual.pdf'>Manual</a>
        <a HREF="https://x.com/en/datasheet">Sheet</a>
    """
    hrefs = probe._extract_hrefs(html)
    assert "/en/products" in hrefs
    assert "/downloads/manual.pdf" in hrefs
    assert "https://x.com/en/datasheet" in hrefs


def test_extract_hrefs_empty():
    assert probe._extract_hrefs("") == []


# ---------------------------------------------------------------------------
# English-URL detection helpers
# ---------------------------------------------------------------------------

class TestLooksLikeEnglishUrl:
    @pytest.mark.parametrize(
        "url",
        [
            "https://x.com/en/",
            "https://x.com/en-us/products",
            "https://x.com/global/",
            "https://x.com/international/about",
        ],
    )
    def test_positive_hints(self, url):
        assert probe._looks_like_english_url(url) is True

    @pytest.mark.parametrize(
        "url",
        [
            "https://x.com/de/",
            "https://x.com/fr/produits",
            "https://x.com/",
        ],
    )
    def test_negative_hints(self, url):
        assert probe._looks_like_english_url(url) is False


def test_same_registered_domain_handles_www_and_subdomain():
    assert probe._same_registered_domain("https://www.x.com/", "https://x.com/") is True
    assert probe._same_registered_domain("https://a.x.com/", "https://b.x.com/") is True
    assert probe._same_registered_domain("https://x.com/", "https://y.com/") is False


def test_find_english_url_via_hreflang():
    html = """
        <html lang="ja">
        <head>
          <link rel="alternate" hreflang="en" href="https://x.com/en/" />
          <link rel="alternate" hreflang="de" href="https://x.com/de/" />
        </head>
        </html>
    """
    url, method = probe._find_english_url("https://x.com/", html)
    assert url == "https://x.com/en/"
    assert "hreflang" in method


def test_find_english_url_via_url_hint():
    html = """
        <html lang="ja">
        <a href="/en/products">English</a>
        </html>
    """
    url, method = probe._find_english_url("https://x.com/", html)
    assert url.endswith("/en/products")
    # Detection method must be one of the documented heuristics.
    assert any(t in method for t in ("hreflang", "path_hint", "url_hint", "html_lang"))


def test_find_english_url_when_homepage_already_english():
    html = '<html lang="en-US"><body>Hi</body></html>'
    url, method = probe._find_english_url("https://x.com/", html)
    assert url == "https://x.com/"
    assert method.startswith("html_lang:")


def test_find_english_url_none_found():
    html = '<html lang="ja"><body>こんにちは</body></html>'
    url, method = probe._find_english_url("https://x.com/", html)
    assert url == ""
    assert method == ""


# ---------------------------------------------------------------------------
# YAML candidate shaping
# ---------------------------------------------------------------------------

def _make_result(**overrides):
    base = dict(
        brand="acme",
        brand_name="Acme",
        website="https://www.acme.com/",
        homepage_status=200,
        homepage_ok=True,
        homepage_final_url="https://www.acme.com/",
        has_english_version=True,
        english_url="https://www.acme.com/en/",
        english_detection="hreflang:en",
        has_product_pages=True,
        product_page_examples=["https://www.acme.com/en/products/x"],
        has_download_center=True,
        download_page_examples=["https://www.acme.com/en/downloads"],
        pdf_examples=["https://www.acme.com/en/downloads/manual.pdf"],
        needs_js_render=False,
        blocked_reason="",
        fetcher_used="scrapling.Fetcher",
        worth_promoting=True,
        worth_promoting_reason="",
    )
    base.update(overrides)
    return probe.BrandProbeResult(**base)


def test_build_yaml_candidate_basic_keys():
    res = _make_result()
    cand = probe.build_yaml_candidate(res)
    for key in (
        "brand", "brand_name", "website", "entry_url", "seed_urls",
        "max_pages", "url_scope", "page_role_classification", "fields",
        "filters", "reject_url_patterns", "download_link_selector",
        "global_download_threshold", "probe_metadata",
    ):
        assert key in cand, f"missing key: {key}"


def test_build_yaml_candidate_uses_english_url_as_entry():
    res = _make_result()
    cand = probe.build_yaml_candidate(res)
    assert cand["entry_url"] == "https://www.acme.com/en/"
    assert cand["url_scope"]["path_prefix"] == "/en/"


def test_build_yaml_candidate_seeds_include_downloads_and_products():
    res = _make_result()
    cand = probe.build_yaml_candidate(res)
    seeds = cand["seed_urls"]
    assert "https://www.acme.com/en/" in seeds
    assert "https://www.acme.com/en/downloads" in seeds
    assert "https://www.acme.com/en/products/x" in seeds


def test_build_yaml_candidate_records_block_status():
    res = _make_result(
        homepage_status=403,
        homepage_ok=False,
        blocked_reason="sandbox_egress_block",
        worth_promoting=False,
        worth_promoting_reason="blocked:sandbox_egress_block",
    )
    cand = probe.build_yaml_candidate(res)
    meta = cand["probe_metadata"]
    assert meta["homepage_status"] == 403
    assert meta["homepage_ok"] is False
    assert meta["blocked_reason"] == "sandbox_egress_block"
    assert meta["worth_promoting"] is False


def test_build_yaml_candidate_adds_render_hint_when_js_detected():
    res = _make_result(needs_js_render=True)
    cand = probe.build_yaml_candidate(res)
    assert "render" in cand
    assert cand["render"]["engine"] == "playwright"
