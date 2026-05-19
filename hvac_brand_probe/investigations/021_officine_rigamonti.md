# 021 - Officine Rigamonti / OR

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:officinerigamonti.it filetype:pdf`; `site:officinerigamonti.it english products`

## 1. Brand identity

- Standard brand name: Officine Rigamonti / OR
- Official website: https://www.officinerigamonti.it/
- English website (source doc): https://www.officinerigamonti.it/en/
- English URL confirmed in search index: https://www.officinerigamonti.it/en/products/
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 官网内下载页/PDF 入口需人工复核，避免混入代理商目录。
- Notes: Chrome 搜索确认官方英文站；搜索结果出现 2025 catalog PDF，但来自第三方域，需谨慎。

## 2. Website entry decision

- Recommended entry_url: https://www.officinerigamonti.it/en/
- Alternative entry URLs: https://www.officinerigamonti.it/; https://www.officinerigamonti.it/en/products/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 黄铜阀门、水暖控制和通用阀件，适合作为阀门结构与目录参考。
- Priority keywords (observed in Google result titles/snippets for this domain): pressure reducing valves, thermostatic mixing valves, water supply, preset safety valves, water hammer damper, PED certifications, solar systems, heating
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬英文 products，重点 valves、pressure reducing/safety、brass plumbing components；PDF 可能通过 catalogue 或产品页链接。
- Manual review needed: 官网内下载页/PDF 入口需人工复核，避免混入代理商目录。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.officinerigamonti.it/en/products/
- PDF links found via Google site:search: 1 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.officinerigamonti.it/schede-prodotto/EN/acquedottistica/0198%20-%20EN.pdf — 0198 1/2 Water Hammer Damper Hammer Stop (datasheet)
  2. (no further sample from Google site:search)
  3. (no further sample from Google site:search)
  4. (no further sample from Google site:search)
  5. (no further sample from Google site:search)
- Document types observed in samples: datasheet
- Notes (search agent): Only one PDF result indexed (under /schede-prodotto/EN/). Product pages well categorized under /en/products/. Vortex dirt separator featured.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.officinerigamonti.it/en/products/ — Products
  2. https://www.officinerigamonti.it/en/products/components-for-water-supply/ — Components for Water Supply
  3. https://www.officinerigamonti.it/en/products/connections/ — Connections
  4. https://www.officinerigamonti.it/en/products/pressure-reducing-valves-with-diaphragm/ — Pressure Reducing Valves with Diaphragm
  5. https://www.officinerigamonti.it/en/products/adjustable-thermostatic-mixing-valves/ — Adjustable Thermostatic Mixing Valves
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 搜索确认官方英文站；搜索结果出现 2025 catalog PDF，但来自第三方域，需谨慎。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: officine_rigamonti_or
brand_name: Officine Rigamonti / OR
website: https://www.officinerigamonti.it/
entry_url: https://www.officinerigamonti.it/en/
seed_urls:
- https://www.officinerigamonti.it/en/
- https://www.officinerigamonti.it/en/products/
- https://www.officinerigamonti.it/en/products/components-for-water-supply/
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
  suggested_category: D-黄铜阀门/管件/分集水器/通用水暖
  suggested_priority: P1
  country_region: Italy
  manual_review: 官网内下载页/PDF 入口需人工复核，避免混入代理商目录。
  crawl_scope_notes: 爬英文 products，重点 valves、pressure reducing/safety、brass plumbing
    components；PDF 可能通过 catalogue 或产品页链接。
  product_line_notes: 黄铜阀门、水暖控制和通用阀件，适合作为阀门结构与目录参考。
  blocked_reason_hint: ''
  pdf_sample_count: 1
  product_page_sample_count: 5
  evidence_keywords:
  - pressure reducing valves
  - thermostatic mixing valves
  - water supply
  - preset safety valves
  - water hammer damper
  - PED certifications
  - solar systems
  - heating
  pdf_examples:
  - url: https://www.officinerigamonti.it/schede-prodotto/EN/acquedottistica/0198%20-%20EN.pdf
    title: 0198 1/2 Water Hammer Damper Hammer Stop
    doc_type: datasheet
  product_page_examples:
  - url: https://www.officinerigamonti.it/en/products/
    title: Products
  - url: https://www.officinerigamonti.it/en/products/components-for-water-supply/
    title: Components for Water Supply
  - url: https://www.officinerigamonti.it/en/products/connections/
    title: Connections
  - url: https://www.officinerigamonti.it/en/products/pressure-reducing-valves-with-diaphragm/
    title: Pressure Reducing Valves with Diaphragm
  - url: https://www.officinerigamonti.it/en/products/adjustable-thermostatic-mixing-valves/
    title: Adjustable Thermostatic Mixing Valves
  download_center_url: https://www.officinerigamonti.it/en/products/
  search_queries_run:
  - site:officinerigamonti.it filetype:pdf
  - site:officinerigamonti.it english products
  search_notes: Only one PDF result indexed (under /schede-prodotto/EN/). Product
    pages well categorized under /en/products/. Vortex dirt separator featured.
```
