# 024 - Polypipe Underfloor Heating

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:polypipeufh.com filetype:pdf`; `site:polypipeufh.com products`; `Polypipe underfloor heating manifold site:polypipe.com`

## 1. Brand identity

- Standard brand name: Polypipe Underfloor Heating
- Official website: https://www.polypipe.com/
- English website (source doc): https://www.polypipeufh.com/
- English URL confirmed in search index: https://www.polypipeufh.com/underfloor-heating-products/floor-types/
- Country / region: UK (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: polypipe.com 主站范围很大，建议 YAML 先锁定 polypipeufh.com。
- Notes: Chrome 重试确认 Polypipe UFH Downloads 页面含 PDF 和下载链接。

## 2. Website entry decision

- Recommended entry_url: https://www.polypipeufh.com/support-hub/support-hub-downloads/
- Alternative entry URLs: https://www.polypipe.com/; https://www.polypipeufh.com/; https://www.polypipeufh.com/underfloor-heating-products/floor-types/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 英国地暖系统品牌，UFH 产品、控制器、分集水器和安装资料强相关。
- Priority keywords (observed in Google result titles/snippets for this domain): underfloor heating, manifold, mixing valve, autobalancing manifold, valve actuator, wiring centre, overlay, staple system, clip rail, floating floor
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 优先爬 Polypipe UFH 独立站 support downloads、products/systems；重点 underfloor heating packs、manifolds、controls、pipes、installation manuals。
- Manual review needed: polypipe.com 主站范围很大，建议 YAML 先锁定 polypipeufh.com。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.polypipeufh.com/support-hub/support-hub-downloads/
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.polypipeufh.com/wp-content/uploads/2021/01/UFH-Mixing-Valve-Control-Pack-v1.0-DATASHEET-INSTALL-GUIDE-.pdf — Mixing Valve Control Pack Data Sheet (Jan 2021) (datasheet)
  2. https://www.polypipeufh.com/wp-content/uploads/2024/10/GUD-Polypipe-UFH-and-ARDEX-Combined-Installation-Guide.pdf — Polypipe UFH and ARDEX Combined Installation Guide (Oct 2024) (installation guide)
  3. https://www.polypipeufh.com/wp-content/uploads/2022/06/INSTALLATION-GUIDE-Plastic-Plumbing-_-Underfloor-Heating.pdf — Plumbing & Heating Installation Guide (April 2022) (installation guide)
  4. https://www.polypipeufh.com/wp-content/uploads/2021/01/PB0040124-Valve-Actuator-DATASHEET-.pdf — UFCH Valve Actuator Data Sheet (Nov 2018) (datasheet)
  5. https://www.polypipeufh.com/wp-content/uploads/2023/03/DATASHEET-Autobalancing-Manifold-Specification-v0.3-Draft.pdf — Autobalancing Manifold Specification Data Sheet (datasheet)
- Document types observed in samples: datasheet, installation guide
- Notes (search agent): Two related domains: polypipeufh.com (UFH dedicated site, PDFs in /wp-content/uploads/) and polypipe.com (parent group with trade price lists).

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.polypipeufh.com/underfloor-heating-products/floor-types/ — Underfloor Heating Floor Types
  2. https://www.polypipeufh.com/professional/products/staple-system/ — Staple System
  3. https://www.polypipeufh.com/professional/products/clip-rail-system/ — Clip Rail System
  4. https://www.polypipeufh.com/professional/products/red-floor-panel/ — Red Floor Panel
  5. https://www.polypipeufh.com/professional/products_cat/manifolds/ — Manifolds Archives - UFH Professionals
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 重试确认 Polypipe UFH Downloads 页面含 PDF 和下载链接。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: polypipe_underfloor_heating
brand_name: Polypipe Underfloor Heating
website: https://www.polypipe.com/
entry_url: https://www.polypipeufh.com/support-hub/support-hub-downloads/
seed_urls:
- https://www.polypipeufh.com/support-hub/support-hub-downloads/
- https://www.polypipeufh.com/underfloor-heating-products/floor-types/
- https://www.polypipeufh.com/professional/products/staple-system/
max_pages: 250
url_scope:
  path_prefix: null
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
  country_region: UK
  manual_review: polypipe.com 主站范围很大，建议 YAML 先锁定 polypipeufh.com。
  crawl_scope_notes: 优先爬 Polypipe UFH 独立站 support downloads、products/systems；重点 underfloor
    heating packs、manifolds、controls、pipes、installation manuals。
  product_line_notes: 英国地暖系统品牌，UFH 产品、控制器、分集水器和安装资料强相关。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - underfloor heating
  - manifold
  - mixing valve
  - autobalancing manifold
  - valve actuator
  - wiring centre
  - overlay
  - staple system
  - clip rail
  - floating floor
  pdf_examples:
  - url: https://www.polypipeufh.com/wp-content/uploads/2021/01/UFH-Mixing-Valve-Control-Pack-v1.0-DATASHEET-INSTALL-GUIDE-.pdf
    title: Mixing Valve Control Pack Data Sheet (Jan 2021)
    doc_type: datasheet
  - url: https://www.polypipeufh.com/wp-content/uploads/2024/10/GUD-Polypipe-UFH-and-ARDEX-Combined-Installation-Guide.pdf
    title: Polypipe UFH and ARDEX Combined Installation Guide (Oct 2024)
    doc_type: installation_guide
  - url: https://www.polypipeufh.com/wp-content/uploads/2022/06/INSTALLATION-GUIDE-Plastic-Plumbing-_-Underfloor-Heating.pdf
    title: Plumbing & Heating Installation Guide (April 2022)
    doc_type: installation_guide
  - url: https://www.polypipeufh.com/wp-content/uploads/2021/01/PB0040124-Valve-Actuator-DATASHEET-.pdf
    title: UFCH Valve Actuator Data Sheet (Nov 2018)
    doc_type: datasheet
  - url: https://www.polypipeufh.com/wp-content/uploads/2023/03/DATASHEET-Autobalancing-Manifold-Specification-v0.3-Draft.pdf
    title: Autobalancing Manifold Specification Data Sheet
    doc_type: datasheet
  product_page_examples:
  - url: https://www.polypipeufh.com/underfloor-heating-products/floor-types/
    title: Underfloor Heating Floor Types
  - url: https://www.polypipeufh.com/professional/products/staple-system/
    title: Staple System
  - url: https://www.polypipeufh.com/professional/products/clip-rail-system/
    title: Clip Rail System
  - url: https://www.polypipeufh.com/professional/products/red-floor-panel/
    title: Red Floor Panel
  - url: https://www.polypipeufh.com/professional/products_cat/manifolds/
    title: Manifolds Archives - UFH Professionals
  download_center_url: https://www.polypipeufh.com/support-hub/support-hub-downloads/
  search_queries_run:
  - site:polypipeufh.com filetype:pdf
  - site:polypipeufh.com products
  - Polypipe underfloor heating manifold site:polypipe.com
  search_notes: 'Two related domains: polypipeufh.com (UFH dedicated site, PDFs in
    /wp-content/uploads/) and polypipe.com (parent group with trade price lists).'
```
