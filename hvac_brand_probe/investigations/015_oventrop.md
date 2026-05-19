# 015 - Oventrop

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:oventrop.com filetype:pdf`; `site:oventrop.com products english`

## 1. Brand identity

- Standard brand name: Oventrop
- Official website: https://www.oventrop.com/
- English website (source doc): https://www.oventrop.com/en
- English URL confirmed in search index: https://www.oventrop.com/en-GB/products/itemsearch
- Country / region: Germany (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: Google 搜索结果出现多区域 en-XX 文件链接，需选择稳定全球/英文入口。
- Notes: Chrome 打开 /en 官方页，搜索结果显示 Oventrop 文件/PDF URL。

## 2. Website entry decision

- Recommended entry_url: https://www.oventrop.com/en
- Alternative entry URLs: https://www.oventrop.com/; https://www.oventrop.com/en-GB/products/itemsearch
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 暖通阀门、平衡阀、恒温阀、地暖控制与系统组件标杆。
- Priority keywords (observed in Google result titles/snippets for this domain): hydronic balancing, thermostat, actuator, valves, fittings, Regumaq, Regudis, HydroControl, potable water, oil heating, climate control, radiator
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 English 产品目录、文件/文档链接，重点 hydronic balancing、thermostatic valves、floor heating controls、manifolds、stations。
- Manual review needed: Google 搜索结果出现多区域 en-XX 文件链接，需选择稳定全球/英文入口。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.oventrop.com/en-GB/products/technicalinformationoperatinginstructions
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.oventrop.com/Pools/Files/manual/en/L_115096180_EN_b2f61bd0-9595-41a2-bad4-3b88c95bba22.pdf — Valves, controls + systems Manual EN (technical manual)
  2. https://www.oventrop.com/Pools/Files/manual/en/10227810%20001%2002_Regumaq-X25_BA_EN_15_8538a89e-151a-4f38-871d-33983742425d.pdf — Regumaq X-25 Operating Instructions EN (installation guide)
  3. https://www.oventrop.com/Pools/Files/hbtd/en/db_1077103_en_45c0b3ea-220d-4a36-b0bc-265728b1ec0f.pdf — Oventrop Datasheet (hbtd) EN (datasheet)
  4. https://www.oventrop.com/Pools/Files/file/en/Katalog_EN_2015_web_386b3592-3d08-4947-a10a-c4ab12579240.pdf — Thermostats, actuators, valves and fittings Catalogue 2015 EN (catalogue)
  5. https://www.oventrop.com/Pools/Files/file/en/Katalog_2018_EN_web_74043f3b-3ee9-4794-9272-e018855f8765.pdf — Room temperature and climate control / Hydronic balancing at the radiator Catalogue 2018 EN (catalogue)
- Document types observed in samples: catalogue, datasheet, installation guide, technical manual
- Notes (search agent): PDFs at /Pools/Files/ path with hash IDs and language-prefixed folders (manual/en, file/en). Many locale variants (en-GB, en-AU, en-DK, en-GR).

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.oventrop.com/en-GB/products/technicalinformationoperatinginstructions — Technical information / Operating instructions | Oventrop GB
  2. https://www.oventrop.com/en-GB/products/itemsearch — Item search | Oventrop GB
  3. https://www.oventrop.com/en-GB/productssystems/catalogue/potable-water/shutoff-valves-and-other-products-for-potable-water/system-components-for-the-potable-water-installation/drain-valves/2226 — Drain valves potable water
  4. https://www.oventrop.com/en-GB/productssystems/catalogue/oil/products-for-heating-oil-installations/pipeline-valves-and-components-for-oil-heating-technology/76 — Pipeline valves and components for oil heating technology
  5. https://www.oventrop.com/en-GR/productssystems/catalogue/oil/products-for-heating-oil-installations/deaerators-and-filters-for-oil-heating-technology/39 — Deaerators and filters for oil heating technology
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 打开 /en 官方页，搜索结果显示 Oventrop 文件/PDF URL。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: oventrop
brand_name: Oventrop
website: https://www.oventrop.com/
entry_url: https://www.oventrop.com/en
seed_urls:
- https://www.oventrop.com/en
- https://www.oventrop.com/en-GB/products/technicalinformationoperatinginstructions
- https://www.oventrop.com/en-GB/products/itemsearch
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
  suggested_category: A-核心暖通水力控制/地暖阀门
  suggested_priority: P0
  country_region: Germany
  manual_review: Google 搜索结果出现多区域 en-XX 文件链接，需选择稳定全球/英文入口。
  crawl_scope_notes: 爬 English 产品目录、文件/文档链接，重点 hydronic balancing、thermostatic valves、floor
    heating controls、manifolds、stations。
  product_line_notes: 暖通阀门、平衡阀、恒温阀、地暖控制与系统组件标杆。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - hydronic balancing
  - thermostat
  - actuator
  - valves
  - fittings
  - Regumaq
  - Regudis
  - HydroControl
  - potable water
  - oil heating
  - climate control
  - radiator
  pdf_examples:
  - url: https://www.oventrop.com/Pools/Files/manual/en/L_115096180_EN_b2f61bd0-9595-41a2-bad4-3b88c95bba22.pdf
    title: Valves, controls + systems Manual EN
    doc_type: manual
  - url: https://www.oventrop.com/Pools/Files/manual/en/10227810%20001%2002_Regumaq-X25_BA_EN_15_8538a89e-151a-4f38-871d-33983742425d.pdf
    title: Regumaq X-25 Operating Instructions EN
    doc_type: installation_guide
  - url: https://www.oventrop.com/Pools/Files/hbtd/en/db_1077103_en_45c0b3ea-220d-4a36-b0bc-265728b1ec0f.pdf
    title: Oventrop Datasheet (hbtd) EN
    doc_type: datasheet
  - url: https://www.oventrop.com/Pools/Files/file/en/Katalog_EN_2015_web_386b3592-3d08-4947-a10a-c4ab12579240.pdf
    title: Thermostats, actuators, valves and fittings Catalogue 2015 EN
    doc_type: catalogue
  - url: https://www.oventrop.com/Pools/Files/file/en/Katalog_2018_EN_web_74043f3b-3ee9-4794-9272-e018855f8765.pdf
    title: Room temperature and climate control / Hydronic balancing at the radiator
      Catalogue 2018 EN
    doc_type: catalogue
  product_page_examples:
  - url: https://www.oventrop.com/en-GB/products/technicalinformationoperatinginstructions
    title: Technical information / Operating instructions | Oventrop GB
  - url: https://www.oventrop.com/en-GB/products/itemsearch
    title: Item search | Oventrop GB
  - url: https://www.oventrop.com/en-GB/productssystems/catalogue/potable-water/shutoff-valves-and-other-products-for-potable-water/system-components-for-the-potable-water-installation/drain-valves/2226
    title: Drain valves potable water
  - url: https://www.oventrop.com/en-GB/productssystems/catalogue/oil/products-for-heating-oil-installations/pipeline-valves-and-components-for-oil-heating-technology/76
    title: Pipeline valves and components for oil heating technology
  - url: https://www.oventrop.com/en-GR/productssystems/catalogue/oil/products-for-heating-oil-installations/deaerators-and-filters-for-oil-heating-technology/39
    title: Deaerators and filters for oil heating technology
  download_center_url: https://www.oventrop.com/en-GB/products/technicalinformationoperatinginstructions
  search_queries_run:
  - site:oventrop.com filetype:pdf
  - site:oventrop.com products english
  search_notes: PDFs at /Pools/Files/ path with hash IDs and language-prefixed folders
    (manual/en, file/en). Many locale variants (en-GB, en-AU, en-DK, en-GR).
```
