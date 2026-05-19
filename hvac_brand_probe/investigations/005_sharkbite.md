# 005 - SharkBite

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:sharkbite.com filetype:pdf`; `site:sharkbite.com products technical`

## 1. Brand identity

- Standard brand name: SharkBite
- Official website: https://www.sharkbite.com/
- English website (source doc): https://www.sharkbite.com/us/en/
- English URL confirmed in search index: https://www.sharkbite.com/us/en/technical-downloads
- Country / region: USA (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 产品偏 plumbing，需在 YAML 中过滤零售/DIY 内容，保留技术资料和产品页。
- Notes: Chrome 确认 technical-downloads 页面，PDF/下载链接明显。

## 2. Website entry decision

- Recommended entry_url: https://www.sharkbite.com/us/en/technical-downloads
- Alternative entry URLs: https://www.sharkbite.com/; https://www.sharkbite.com/us/en/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/us/en` (derived from entry URL locale segment)
- Suggested path_prefix: /us/en

## 3. Product scope

- Priority product lines: PEX 与快接管件品牌，强于水暖安装、管件、阀门和系统手册。
- Priority keywords (observed in Google result titles/snippets for this domain): push-to-connect, push-fit, PEX, fittings, check valve, DZR brass, plumbing heating, spec sheet, fire fittings, elbow
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 Products、Resources/Technical Downloads，重点 push-to-connect fittings、PEX pipe、valves、manifolds、installation guides。
- Manual review needed: 产品偏 plumbing，需在 YAML 中过滤零售/DIY 内容，保留技术资料和产品页。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.sharkbite.com/us/en/technical-downloads
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.sharkbite.com/sites/default/files/files/sharkbite-max-install-instructions-2024-07.pdf — SharkBite Max Install Instructions 2024-07 (installation guide)
  2. https://www.sharkbite.com/sites/default/files/files/SB-US-Product-Catalog-2024.pdf — SharkBite US Product Catalog 2024 (catalogue)
  3. https://www.sharkbite.com/sites/default/files/resources/SharkBite-PEX-b-Spec-Sheet.pdf — SharkBite PEX-b Spec Sheet (datasheet)
  4. https://www.sharkbite.com/sites/default/files/resources/SharkBite-Max-Check-Valve-Spec-Sheet.pdf — SharkBite Max Check Valve Spec Sheet (datasheet)
  5. https://www.sharkbite.com/sites/default/files/files/SB-PTC-Installer-Pocket-Guide-2024.pdf — Push-to-Connect Installer Pocket Guide 2024 (installation guide)
- Document types observed in samples: catalogue, datasheet, installation guide
- Notes (search agent): Strong PDF index with clear catalog/spec sheet pattern. UK/US locale split (us/en, gb/en).

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.sharkbite.com/us/en/technical-downloads — Technical Downloads | SharkBite
  2. https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/slip-tee-connectors — Brass Push-fit Slip Tee Connectors
  3. https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/equal-tees — Brass Push-fit Equal Tees
  4. https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-valves/double-check-valves — DZR Brass Push-fit Double Check Valves
  5. https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/equal-straight-connectors — Brass Push-fit Equal Straight Connectors
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 technical-downloads 页面，PDF/下载链接明显。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: sharkbite
brand_name: SharkBite
website: https://www.sharkbite.com/
entry_url: https://www.sharkbite.com/us/en/technical-downloads
seed_urls:
- https://www.sharkbite.com/us/en/technical-downloads
- https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/slip-tee-connectors
max_pages: 250
url_scope:
  path_prefix: /us/en
page_role_classification:
  category:
    indicators:
    - /product
    - /products
    - /catalog
    - /catalogue
    recurse: true
  product:
    indicators:
    - /product/
    recurse: false
  navigation:
    indicators:
    - /download
    - /downloads
    - /literature
    - /resources
    recurse: true
fields:
  product_name: h1
  downloads: a[href$='.pdf']
filters:
  download_link_selector: a[href$='.pdf']
  reject_url_patterns:
  - /news/
  - /blog/
  - /press/
  - /events/
  - /careers/
  - /jobs/
  - /privacy/
  - /terms/
  - /cookie/
  - /contact/
  - /about/
  global_download_threshold: 10
probe_notes:
  verification_status: google_indexed_2026-05-19; http_not_verified
  verification_method: google_site_search via WebSearch; no live HTTP fetch (sandbox
    blocked egress)
  verification_date: '2026-05-19'
  suggested_category: B-地暖系统/PEX/管道系统
  suggested_priority: P1
  country_region: USA
  manual_review: 产品偏 plumbing，需在 YAML 中过滤零售/DIY 内容，保留技术资料和产品页。
  crawl_scope_notes: 爬 Products、Resources/Technical Downloads，重点 push-to-connect fittings、PEX
    pipe、valves、manifolds、installation guides。
  product_line_notes: PEX 与快接管件品牌，强于水暖安装、管件、阀门和系统手册。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - push-to-connect
  - push-fit
  - PEX
  - fittings
  - check valve
  - DZR brass
  - plumbing heating
  - spec sheet
  - fire fittings
  - elbow
  pdf_examples:
  - url: https://www.sharkbite.com/sites/default/files/files/sharkbite-max-install-instructions-2024-07.pdf
    title: SharkBite Max Install Instructions 2024-07
    doc_type: installation_guide
  - url: https://www.sharkbite.com/sites/default/files/files/SB-US-Product-Catalog-2024.pdf
    title: SharkBite US Product Catalog 2024
    doc_type: catalogue
  - url: https://www.sharkbite.com/sites/default/files/resources/SharkBite-PEX-b-Spec-Sheet.pdf
    title: SharkBite PEX-b Spec Sheet
    doc_type: datasheet
  - url: https://www.sharkbite.com/sites/default/files/resources/SharkBite-Max-Check-Valve-Spec-Sheet.pdf
    title: SharkBite Max Check Valve Spec Sheet
    doc_type: datasheet
  - url: https://www.sharkbite.com/sites/default/files/files/SB-PTC-Installer-Pocket-Guide-2024.pdf
    title: Push-to-Connect Installer Pocket Guide 2024
    doc_type: installation_guide
  product_page_examples:
  - url: https://www.sharkbite.com/us/en/technical-downloads
    title: Technical Downloads | SharkBite
  - url: https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/slip-tee-connectors
    title: Brass Push-fit Slip Tee Connectors
  - url: https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/equal-tees
    title: Brass Push-fit Equal Tees
  - url: https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-valves/double-check-valves
    title: DZR Brass Push-fit Double Check Valves
  - url: https://www.sharkbite.com/gb/en/products/plumbing-heating/dzr-brass-fittings/equal-straight-connectors
    title: Brass Push-fit Equal Straight Connectors
  download_center_url: https://www.sharkbite.com/us/en/technical-downloads
  search_queries_run:
  - site:sharkbite.com filetype:pdf
  - site:sharkbite.com products technical
  search_notes: Strong PDF index with clear catalog/spec sheet pattern. UK/US locale
    split (us/en, gb/en).
```
