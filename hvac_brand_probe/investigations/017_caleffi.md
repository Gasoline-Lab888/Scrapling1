# 017 - Caleffi

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:caleffi.com filetype:pdf`; `site:caleffi.com products`

## 1. Brand identity

- Standard brand name: Caleffi
- Official website: https://www.caleffi.com/
- English website (source doc): https://www.caleffi.com/en-int
- English URL confirmed in search index: https://www.caleffi.com/en-us/products
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: Caleffi 区域站很多，建议优先 en-int，必要时补 North America catalog。
- Notes: Chrome 搜索确认官方产品搜索和目录 PDF；页面有产品检索入口。

## 2. Website entry decision

- Recommended entry_url: https://www.caleffi.com/en-int/products/search
- Alternative entry URLs: https://www.caleffi.com/; https://www.caleffi.com/en-int; https://www.caleffi.com/en-us/products
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en-int` (derived from entry URL locale segment)
- Suggested path_prefix: /en-int

## 3. Product scope

- Priority product lines: 暖通水力控制、混水、平衡、分集水器和系统组件标杆，PDF 资料质量高。
- Priority keywords (observed in Google result titles/snippets for this domain): hydronic, manifolds, mixing stations, pressure reducing valves, hydraulic separators, DISCAL air separators, zone valve, tempering valve, balancing
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 en-int products/search 和 technical brochures，重点 balancing valves、mixing valves、manifolds、heat interface、safety/control devices。
- Manual review needed: Caleffi 区域站很多，建议优先 en-int，必要时补 North America catalog。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.caleffi.com/en-us/products/search
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.caleffi.com/sites/default/files/media/external-file/03533_EN.pdf — LEGIOFLOW Domestic Water Distribution Units 6005 series (datasheet)
  2. https://www.caleffi.com/sites/default/files/media/external-file/01115_EN.pdf — Z-one motorised zone valve 642-643 series (datasheet)
  3. https://www.caleffi.com/sites/default/files/media/external-file/H0013594.pdf — Electronic mixing valve digital regulator 6003 series Quick Start Guide (technical manual)
  4. https://www.caleffi.com/sites/default/files/media/external-file/01392_EN.pdf — Motorised diverting ball valve for heat (datasheet)
  5. https://www.caleffi.com/sites/default/files/media/external-file/01194_EN_14.pdf — Tempering adjustable valve with knob 5219 series (datasheet)
- Document types observed in samples: datasheet, technical manual
- Notes (search agent): PDF datasheets hosted at /sites/default/files/media/external-file/ with _EN suffix. Strong hydronic product coverage on en-us subpath.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.caleffi.com/en-us/products/distribution-manifolds-and-mixing-stations — Distribution Manifolds and Mixing Stations
  2. https://www.caleffi.com/en-us/products/pressure-reducing-valves — Pressure Reducing Valves
  3. https://www.caleffi.com/en-us/products/hydraulic-separators — Hydraulic Separators
  4. https://www.caleffi.com/en-us/products/hydraulic-separators/hydro-separators — Hydro Separators
  5. https://www.caleffi.com/en-us/products/air-and-dirt-separators-and-air-vents/discalr-air-separators — DISCAL Air Separators
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 搜索确认官方产品搜索和目录 PDF；页面有产品检索入口。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: caleffi
brand_name: Caleffi
website: https://www.caleffi.com/
entry_url: https://www.caleffi.com/en-int/products/search
seed_urls:
- https://www.caleffi.com/en-int/products/search
- https://www.caleffi.com/en-us/products/search
- https://www.caleffi.com/en-us/products/distribution-manifolds-and-mixing-stations
- https://www.caleffi.com/en-us/products/pressure-reducing-valves
max_pages: 250
url_scope:
  path_prefix: /en-int
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
  suggested_category: A-核心暖通水力控制/地暖阀门
  suggested_priority: P0
  country_region: Italy
  manual_review: Caleffi 区域站很多，建议优先 en-int，必要时补 North America catalog。
  crawl_scope_notes: 爬 en-int products/search 和 technical brochures，重点 balancing valves、mixing
    valves、manifolds、heat interface、safety/control devices。
  product_line_notes: 暖通水力控制、混水、平衡、分集水器和系统组件标杆，PDF 资料质量高。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - hydronic
  - manifolds
  - mixing stations
  - pressure reducing valves
  - hydraulic separators
  - DISCAL air separators
  - zone valve
  - tempering valve
  - balancing
  pdf_examples:
  - url: https://www.caleffi.com/sites/default/files/media/external-file/03533_EN.pdf
    title: LEGIOFLOW Domestic Water Distribution Units 6005 series
    doc_type: datasheet
  - url: https://www.caleffi.com/sites/default/files/media/external-file/01115_EN.pdf
    title: Z-one motorised zone valve 642-643 series
    doc_type: datasheet
  - url: https://www.caleffi.com/sites/default/files/media/external-file/H0013594.pdf
    title: Electronic mixing valve digital regulator 6003 series Quick Start Guide
    doc_type: manual
  - url: https://www.caleffi.com/sites/default/files/media/external-file/01392_EN.pdf
    title: Motorised diverting ball valve for heat
    doc_type: datasheet
  - url: https://www.caleffi.com/sites/default/files/media/external-file/01194_EN_14.pdf
    title: Tempering adjustable valve with knob 5219 series
    doc_type: datasheet
  product_page_examples:
  - url: https://www.caleffi.com/en-us/products/distribution-manifolds-and-mixing-stations
    title: Distribution Manifolds and Mixing Stations
  - url: https://www.caleffi.com/en-us/products/pressure-reducing-valves
    title: Pressure Reducing Valves
  - url: https://www.caleffi.com/en-us/products/hydraulic-separators
    title: Hydraulic Separators
  - url: https://www.caleffi.com/en-us/products/hydraulic-separators/hydro-separators
    title: Hydro Separators
  - url: https://www.caleffi.com/en-us/products/air-and-dirt-separators-and-air-vents/discalr-air-separators
    title: DISCAL Air Separators
  download_center_url: https://www.caleffi.com/en-us/products/search
  search_queries_run:
  - site:caleffi.com filetype:pdf
  - site:caleffi.com products
  search_notes: PDF datasheets hosted at /sites/default/files/media/external-file/
    with _EN suffix. Strong hydronic product coverage on en-us subpath.
```
