# 008 - Barberi Rubinetterie

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:barberi.it filetype:pdf`; `site:barberi.it products english`

## 1. Brand identity

- Standard brand name: Barberi Rubinetterie
- Official website: https://www.barberi.it/
- English website (source doc): https://www.barberi.it/ww/en/
- English URL confirmed in search index: https://www.barberi.it/ww/en/products
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需确认产品页 PDF 是否动态加载。
- Notes: Chrome 确认 /ww/en/products 英文产品列表，页面含下载/资料入口。

## 2. Website entry decision

- Recommended entry_url: https://www.barberi.it/ww/en/products
- Alternative entry URLs: https://www.barberi.it/; https://www.barberi.it/ww/en/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/ww/en` (derived from entry URL locale segment)
- Suggested path_prefix: /ww/en

## 3. Product scope

- Priority product lines: 黄铜阀门、采暖机组、混水组件、分集水器与水暖控制组件。
- Priority keywords (observed in Google result titles/snippets for this domain): thermostatic mixing valves, regulating groups, manifold, safety relief valve, air vents, filters, ball valves, water hammer arrestor, Y-filter, hydraulic separator
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬英文产品列表，重点 mixing units、manifolds、safety valves、balancing/shut-off valves、pump groups，PDF 从产品页收集。
- Manual review needed: 需确认产品页 PDF 是否动态加载。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.barberi.it/ww/en/documentations
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.barberi.it/downloads/5799/787/ST00279_en.pdf — 54D Water Hammer Arrestor EN Datasheet (datasheet)
  2. https://www.barberi.it/downloads/5748/736/LB00166.pdf?act=download — V83.W.ARPM-V82.W.ARPM Documentation (datasheet)
  3. https://www.barberi.it/downloads/2192/68/CA2526r0-IT_web.pdf?act=download — Catalogo (General Product Catalogue) (catalogue)
  4. https://www.barberi.it/downloads/5658/646/ST00108_it.pdf?act=download — 050 049 Filtri a Y Scheda Tecnica ST00108 (datasheet)
  5. https://www.barberi.it/downloads/4127/288/BPP00010r0_IT.pdf?act=download — Product Preview (brochure)
- Document types observed in samples: brochure, catalogue, datasheet
- Notes (search agent): Strong PDF coverage via /downloads/ path, multilingual versioning (EN/IT/ES/FR/RU). Full product taxonomy B1-B13 under /ww/en/.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.barberi.it/ww/en/products — Full product list | Barberi Rubinetterie
  2. https://www.barberi.it/ww/en/products/b3-regulating-groups-and-heating-components/system-components/safety-relief-valve — Safety relief valve
  3. https://www.barberi.it/ww/en/products/b3-regulating-groups-and-heating-components/system-components — System components
  4. https://www.barberi.it/ww/en/products/b1-thermostatic-mixing-valves/temperature-safety-relief-valve — Temperature safety relief valve
  5. https://www.barberi.it/ww/en/products/b6-air-vents-and-deaerators/air-vents — Air vents
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 /ww/en/products 英文产品列表，页面含下载/资料入口。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: barberi_rubinetterie
brand_name: Barberi Rubinetterie
website: https://www.barberi.it/
entry_url: https://www.barberi.it/ww/en/products
seed_urls:
- https://www.barberi.it/ww/en/products
- https://www.barberi.it/ww/en/documentations
- https://www.barberi.it/ww/en/products/b3-regulating-groups-and-heating-components/system-components/safety-relief-valve
max_pages: 250
url_scope:
  path_prefix: /ww/en
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
  manual_review: 需确认产品页 PDF 是否动态加载。
  crawl_scope_notes: 爬英文产品列表，重点 mixing units、manifolds、safety valves、balancing/shut-off
    valves、pump groups，PDF 从产品页收集。
  product_line_notes: 黄铜阀门、采暖机组、混水组件、分集水器与水暖控制组件。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - thermostatic mixing valves
  - regulating groups
  - manifold
  - safety relief valve
  - air vents
  - filters
  - ball valves
  - water hammer arrestor
  - Y-filter
  - hydraulic separator
  pdf_examples:
  - url: https://www.barberi.it/downloads/5799/787/ST00279_en.pdf
    title: 54D Water Hammer Arrestor EN Datasheet
    doc_type: datasheet
  - url: https://www.barberi.it/downloads/5748/736/LB00166.pdf?act=download
    title: V83.W.ARPM-V82.W.ARPM Documentation
    doc_type: datasheet
  - url: https://www.barberi.it/downloads/2192/68/CA2526r0-IT_web.pdf?act=download
    title: Catalogo (General Product Catalogue)
    doc_type: catalogue
  - url: https://www.barberi.it/downloads/5658/646/ST00108_it.pdf?act=download
    title: 050 049 Filtri a Y Scheda Tecnica ST00108
    doc_type: datasheet
  - url: https://www.barberi.it/downloads/4127/288/BPP00010r0_IT.pdf?act=download
    title: Product Preview
    doc_type: brochure
  product_page_examples:
  - url: https://www.barberi.it/ww/en/products
    title: Full product list | Barberi Rubinetterie
  - url: https://www.barberi.it/ww/en/products/b3-regulating-groups-and-heating-components/system-components/safety-relief-valve
    title: Safety relief valve
  - url: https://www.barberi.it/ww/en/products/b3-regulating-groups-and-heating-components/system-components
    title: System components
  - url: https://www.barberi.it/ww/en/products/b1-thermostatic-mixing-valves/temperature-safety-relief-valve
    title: Temperature safety relief valve
  - url: https://www.barberi.it/ww/en/products/b6-air-vents-and-deaerators/air-vents
    title: Air vents
  download_center_url: https://www.barberi.it/ww/en/documentations
  search_queries_run:
  - site:barberi.it filetype:pdf
  - site:barberi.it products english
  search_notes: Strong PDF coverage via /downloads/ path, multilingual versioning
    (EN/IT/ES/FR/RU). Full product taxonomy B1-B13 under /ww/en/.
```
