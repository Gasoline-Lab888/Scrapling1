# HVAC Brand Probe

This directory turns `Scrapling-main` into a **HVAC brand-website investigation
lab**. It does *not* turn Scrapling into a production PDF crawler — that role
belongs to `hvac-ai-crawler`. Here we only **survey** brand sites so we can
decide which ones are worth promoting to the real crawler.

The probe is intentionally light-touch. It will:

- visit a brand homepage
- try to find the English version (hreflang + URL hints + `<html lang>`)
- scan the English landing page for product / download / catalogue / brochure /
  datasheet / manual / certificate links
- record a few PDF samples (no bulk download)
- record any blockers (`403`, `429`, Cloudflare, Turnstile, captcha, DNS,
  SSL, timeout, login wall, JS-required, …)
- write a `hvac-ai-crawler`-style YAML candidate for every brand

It will **not**:

- bypass Cloudflare / Turnstile / captcha
- enable residential proxies, fingerprint spoofing, or undetectable mode by
  default
- download PDFs in bulk
- crawl beyond a small set of suspected download pages
- continue crashing the run if a single brand fails — failures are logged

---

## Why mirror `hvac-ai-crawler` here, but stay separate?

`hvac-ai-crawler` is the production system. It already has the conventions
that matter:

| `hvac-ai-crawler` concept            | Mirrored here as                          |
| ------------------------------------ | ----------------------------------------- |
| `brand` / `brand_name` / `website`   | same keys in the probe + candidate YAML   |
| `entry_url`, `seed_urls`             | drafted from probe findings               |
| `url_scope.path_prefix`              | inferred from English entry path          |
| `page_role_classification`           | regex sets for homepage / product / dl    |
| `fields`                             | minimal `title` / `description` skeleton  |
| `filters` (size, lang)               | starter `min_pdf_size_kb`, `language: en` |
| `reject_url_patterns`                | non-EN locale paths, blog/news/legal/etc. |
| `download_link_selector`             | `a[href$=.pdf], a[href*=/download], …`    |
| `global_download_threshold`          | starter cap (review before promoting)     |
| JSONL + Markdown + CSV outputs       | same triple-output report format          |
| `blocked_reason`                     | recorded verbatim per brand               |

We *borrow the design*, but we keep the probe out of `hvac-ai-crawler`. That
way the production repo stays untouched, and Scrapling-main becomes the cheap
playground where we triage candidate brands before promoting them.

---

## Layout

```
hvac_brand_probe/
  README.md                        # this file
  selected_brands_30.yml           # 30 representative brand seeds
  probe_brand_sites.py             # the probe script
  outputs/
    brand_probe_results.jsonl      # one JSON record per brand (machine-read)
    brand_probe_summary.csv        # flat overview (spreadsheet-friendly)
    brand_probe_report.md          # human-friendly triage report
    hvac_yaml_candidates/          # one candidate YAML per brand
      daikin.yml
      viessmann.yml
      ...
```

The `outputs/` artefacts are regenerated on every run; nothing here is meant
to be hand-edited. To promote a brand to `hvac-ai-crawler`, **copy the
candidate YAML into `hvac-ai-crawler`'s brand config directory and review it
manually**. The probe drafts conservative defaults; a human should always
review `seed_urls`, `url_scope`, `reject_url_patterns`, and
`global_download_threshold` before going live.

---

## Running the probe

The probe will use `scrapling.fetchers.Fetcher` if it is installed (it ships
with this repo's `[fetchers]` extra). If those deps are not available it
falls back to the Python stdlib (`urllib`) automatically.

```bash
# From the repo root:
python hvac_brand_probe/probe_brand_sites.py

# Limit to a few brands:
python hvac_brand_probe/probe_brand_sites.py --brands daikin viessmann grundfos

# Probe only the first 5 brands:
python hvac_brand_probe/probe_brand_sites.py --limit 5

# Force the urllib fallback (useful in restricted environments):
python hvac_brand_probe/probe_brand_sites.py --force-stdlib

# Escalate to StealthyFetcher only when a page is detected as blocked:
python hvac_brand_probe/probe_brand_sites.py --use-stealth
```

`--use-stealth` is off by default. It only kicks in when the plain fetch is
detected as blocked, and it still **does not solve captchas, render
Turnstile, or fake fingerprints** — it just gives a JS-capable browser a
single attempt. If that attempt also fails, the probe records
`blocked_reason` and moves on.

---

## What "worth_promoting" means

A brand is marked `worth_promoting: true` only if **all** of the following
hold:

1. The homepage responded with a 2xx/3xx status and was not detected as
   blocked.
2. An English version was located (via hreflang, URL hint, or `<html lang>`).
3. At least one download-centre link or at least one PDF sample was found.

If a brand fails any of these, `worth_promoting_reason` records the specific
reasons (e.g. `no_english_version,no_download_or_pdf_links`,
`blocked:cloudflare_challenge`). Those brands need human follow-up before
they belong in `hvac-ai-crawler`.

---

## `blocked_reason` taxonomy

When a fetch fails, the probe writes one of these reason strings:

| Reason                       | What it means                                       |
| ---------------------------- | --------------------------------------------------- |
| `dns_error`                  | DNS lookup failed                                   |
| `ssl_error`                  | SSL/TLS handshake failed                            |
| `timeout`                    | Network timed out                                   |
| `connection_refused`         | Host rejected the connection                        |
| `connection_reset`           | Peer reset the TCP connection                       |
| `forbidden_403`              | HTTP 403                                            |
| `rate_limited_429`           | HTTP 429                                            |
| `legal_block_451`            | HTTP 451                                            |
| `service_unavailable_503`    | HTTP 503 (non-Cloudflare)                           |
| `cloudflare_challenge`       | Cloudflare interstitial detected                    |
| `cloudflare_jschallenge`     | "Checking your browser" page                        |
| `cloudflare_turnstile`       | Turnstile widget detected                           |
| `cloudflare_block`           | Cloudflare 1020/1015-style block page               |
| `akamai_block` / `imperva_block` | Other WAF block pages                           |
| `captcha`                    | Captcha keyword present                             |
| `access_denied` / `forbidden`| Generic block phrases                               |
| `js_required`                | Body explicitly says JS is required                 |
| `login_required`             | HTTP 401                                            |

`hvac-ai-crawler` should use this to decide policy: e.g. only enable
Playwright rendering for `js_required` or `cloudflare_jschallenge`; skip
`captcha` and `cloudflare_turnstile` entirely until a human supervises.

---

## Brand → YAML candidate workflow

```
selected_brands_30.yml
        │
        ▼
probe_brand_sites.py
        │
        ├─► outputs/brand_probe_results.jsonl   (machine record)
        ├─► outputs/brand_probe_summary.csv     (Excel triage)
        ├─► outputs/brand_probe_report.md       (human review)
        └─► outputs/hvac_yaml_candidates/*.yml  (hvac-ai-crawler drafts)
                       │
                       │   (human review)
                       ▼
        copied / merged into hvac-ai-crawler's brand config
```

Nothing in this directory ever writes into `hvac-ai-crawler`. The hand-off
is a manual review step on purpose — the probe's drafts are starting points,
not production configs.
