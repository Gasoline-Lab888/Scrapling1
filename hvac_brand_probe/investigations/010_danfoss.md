# 010 - Danfoss

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:danfoss.com filetype:pdf valves`; `site:danfoss.com products valves heating`

## 1. Brand identity

- Standard brand name: Danfoss
- Official website: https://www.danfoss.com/
- English website (source doc): https://www.danfoss.com/en/
- English URL confirmed in search index: https://www.danfoss.com/en-us/products/dhs/valves/
- Country / region: Denmark (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: Danfoss 产品庞大，YAML 必须限制到 heating/hydronic valves，避免压缩机、制冷等大类。
- Notes: Chrome 打开官方 products/dhs/valves 页面，含 hydronic balancing and control 标签。

## 2. Website entry decision

- Recommended entry_url: https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
- Alternative entry URLs: https://www.danfoss.com/; https://www.danfoss.com/en/; https://www.danfoss.com/en-us/products/dhs/valves/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 暖通控制阀、平衡阀、恒温控制和区域供热控制标杆品牌。
- Priority keywords (observed in Google result titles/snippets for this domain): thermostatic radiator valves, TRV, hydronic balancing, PICV, RA-C valves, cartridge valves, pressure relief, thermostatic expansion valve, refrigeration valves, directional control
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 DHS valves，重点 hydronic balancing/control、thermostatic radiator valves、PICV、district heating valves 和文档链接。
- Manual review needed: Danfoss 产品庞大，YAML 必须限制到 heating/hydronic valves，避免压缩机、制冷等大类。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://assets.danfoss.com/documents/latest/
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://assets.danfoss.com/documents/latest/361747/BC475984423737en-000101.pdf — Industrial Valves Directional Control Valves (datasheet)
  2. https://assets.danfoss.com/documents/latest/366111/AF479742383899en-000101.pdf — Danfoss Cartridge valves Market leading portfolio (brochure)
  3. https://assets.danfoss.com/documents/latest/238593/BC442682790300en-000101.pdf — Pressure Relief Valves (datasheet)
  4. https://assets.danfoss.com/documents/latest/100443/AF251686497779en-001003.pdf — Shut-off and regulating valves for Industrial Refrigeration (datasheet)
  5. https://assets.danfoss.com/documents/latest/103392/AI000086414526en-000101.pdf — Thermostatic expansion valve Type TGE (datasheet)
- Document types observed in samples: brochure, datasheet
- Notes (search agent): PDFs hosted on assets.danfoss.com (DAM system) with hash IDs. Product pages on /en-us/ locale; also designcenter.danfoss.com subdomain.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.danfoss.com/en-us/products/dhs/valves/ — Valves - For heating | Danfoss
  2. https://www.danfoss.com/en-us/products/dhs/valves/hydronic-balancing-and-control/ra-c-heating-and-cooling-valves/ — RA-C heating and cooling valves | Danfoss
  3. https://www.danfoss.com/en-us/products/dhs/radiator-and-room-thermostats/radiator-thermostats/radiator-valves/ — Thermostatic radiator valves | Danfoss
  4. https://www.danfoss.com/en-us/about-danfoss/our-businesses/heating/hydronic-comfort-controls/ — Hydronic comfort controls | Danfoss
  5. https://www.danfoss.com/en-us/markets/buildings-residential/dhs/solutions-for-hydronic-distributors/ — Solutions for hydronic distributors and wholesalers | Danfoss
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 打开官方 products/dhs/valves 页面，含 hydronic balancing and control 标签。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: danfoss
brand_name: Danfoss
website: https://www.danfoss.com/
entry_url: https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
seed_urls:
- https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
- https://assets.danfoss.com/documents/latest/
- https://www.danfoss.com/en-us/products/dhs/valves/
- https://www.danfoss.com/en-us/products/dhs/valves/hydronic-balancing-and-control/ra-c-heating-and-cooling-valves/
max_pages: 250
url_scope:
  path_prefix: /en
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
  suggested_category: C-商用 HVAC/水力平衡/控制阀
  suggested_priority: P0
  country_region: Denmark
  manual_review: Danfoss 产品庞大，YAML 必须限制到 heating/hydronic valves，避免压缩机、制冷等大类。
  crawl_scope_notes: 爬 DHS valves，重点 hydronic balancing/control、thermostatic radiator
    valves、PICV、district heating valves 和文档链接。
  product_line_notes: 暖通控制阀、平衡阀、恒温控制和区域供热控制标杆品牌。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - thermostatic radiator valves
  - TRV
  - hydronic balancing
  - PICV
  - RA-C valves
  - cartridge valves
  - pressure relief
  - thermostatic expansion valve
  - refrigeration valves
  - directional control
  pdf_examples:
  - url: https://assets.danfoss.com/documents/latest/361747/BC475984423737en-000101.pdf
    title: Industrial Valves Directional Control Valves
    doc_type: datasheet
  - url: https://assets.danfoss.com/documents/latest/366111/AF479742383899en-000101.pdf
    title: Danfoss Cartridge valves Market leading portfolio
    doc_type: brochure
  - url: https://assets.danfoss.com/documents/latest/238593/BC442682790300en-000101.pdf
    title: Pressure Relief Valves
    doc_type: datasheet
  - url: https://assets.danfoss.com/documents/latest/100443/AF251686497779en-001003.pdf
    title: Shut-off and regulating valves for Industrial Refrigeration
    doc_type: datasheet
  - url: https://assets.danfoss.com/documents/latest/103392/AI000086414526en-000101.pdf
    title: Thermostatic expansion valve Type TGE
    doc_type: datasheet
  product_page_examples:
  - url: https://www.danfoss.com/en-us/products/dhs/valves/
    title: Valves - For heating | Danfoss
  - url: https://www.danfoss.com/en-us/products/dhs/valves/hydronic-balancing-and-control/ra-c-heating-and-cooling-valves/
    title: RA-C heating and cooling valves | Danfoss
  - url: https://www.danfoss.com/en-us/products/dhs/radiator-and-room-thermostats/radiator-thermostats/radiator-valves/
    title: Thermostatic radiator valves | Danfoss
  - url: https://www.danfoss.com/en-us/about-danfoss/our-businesses/heating/hydronic-comfort-controls/
    title: Hydronic comfort controls | Danfoss
  - url: https://www.danfoss.com/en-us/markets/buildings-residential/dhs/solutions-for-hydronic-distributors/
    title: Solutions for hydronic distributors and wholesalers | Danfoss
  download_center_url: https://assets.danfoss.com/documents/latest/
  search_queries_run:
  - site:danfoss.com filetype:pdf valves
  - site:danfoss.com products valves heating
  search_notes: PDFs hosted on assets.danfoss.com (DAM system) with hash IDs. Product
    pages on /en-us/ locale; also designcenter.danfoss.com subdomain.
```
