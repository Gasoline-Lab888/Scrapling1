# 019 - ICMA S.p.A.

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:icmaspa.it filetype:pdf`; `site:icmaspa.it products english`

## 1. Brand identity

- Standard brand name: ICMA S.p.A.
- Official website: https://www.icmaspa.it/
- English website (source doc): https://www.icmaspa.it/?lang=en
- English URL confirmed in search index: https://www.icmaspa.it/products/?lang=en
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 站点使用 lang=en 参数，需在爬虫中保留语言参数。
- Notes: Chrome 确认英文 products catalogue 与 downloads 页面。

## 2. Website entry decision

- Recommended entry_url: https://www.icmaspa.it/products-catalogue/?lang=en
- Alternative entry URLs: https://www.icmaspa.it/; https://www.icmaspa.it/?lang=en; https://www.icmaspa.it/products/?lang=en
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 采暖技术阀件、分集水器、管件、混水和系统组件。
- Priority keywords (observed in Google result titles/snippets for this domain): manifold, ball valves, thermal drain valve, filling group, three-way mixing valve, safety valve, press fittings, underfloor heating, thermoplastic manifold
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 products-catalogue 和 downloads，重点 heating components、manifolds、mixing units、thermostatic valves、fittings。
- Manual review needed: 站点使用 lang=en 参数，需在爬虫中保留语言参数。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.icmaspa.it/products/?lang=en
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.icmaspa.it/wp-content/uploads/2020/ST-EN/ST-P207-ENG.pdf — Polypropylene micro fiber P207 Technical Data Sheet (datasheet)
  2. https://www.icmaspa.it/wp-content/uploads/2020/ST-EN/ST-P226-ENG.pdf — Macro synthetic fibers P226 Technical Data Sheet (datasheet)
  3. https://www.icmaspa.it/wp-content/uploads/2025/FI-ML/FI.K071.EN.D.pdf — Art. K069-K071-K072-K073-K074-K075-K077-K079-K081-K086-K088 (datasheet)
  4. https://www.icmaspa.it/wp-content/uploads/2023/ST-IT/ST.400.06.23.IT.pdf — Raccordi a pressare (Press fittings) (datasheet)
  5. https://www.icmaspa.it/wp-content/uploads/2023/FI-ML/FI.S00X.ML.C.pdf — Art. S002 S004 Gruppi Solari (Solar Groups) (datasheet)
- Document types observed in samples: datasheet
- Notes (search agent): English content reached via ?lang=en parameter. PDFs hosted in /wp-content/uploads/ with ST-EN, FI-ML language subfolders.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.icmaspa.it/catalogo-prodotti/manifolds-and-circulation-modules/single-and-coplanar-joinable-manifolds-for-heating-and-sanitary-systems/1102-collettore-semplice-di-distribuzione-con-uscite-laterali-da-1-2-femmina/?lang=en — 1102 Single distribution manifold
  2. https://www.icmaspa.it/catalogo-prodotti/water-and-gas-network/ball-valves-mini-ball-valves/347-ball-valve-with-lever/?lang=en — 347 Full bore straight ball valve with pipe tail
  3. https://www.icmaspa.it/catalogo-prodotti/central-heating-systems-gas-gas-oil-and-bio-fuel/automatic-fillings-groups/249-gruppo-di-riempimento-serie-pesante-con-rubinetto-intercettazione-e-filtro-con-manometro/?lang=en — 249 Heavy model filling group with stop cock and filter
  4. https://www.icmaspa.it/catalogo-prodotti/manifolds-and-circulation-modules/zone-valves/324-valvola-miscelatrice-a-tre-vie-con-sensore-termostatico-a-capillare-campo-di-regolazione-60-90c/?lang=en — 324 Three-way mixing valve with thermostatic capillary remote sensor
  5. https://www.icmaspa.it/catalogo-prodotti/central-heating-systems-gas-gas-oil-and-bio-fuel/pressure-safety-systems/242-valvola-di-sicurezza-a-membrana-m-f/?lang=en — 242 Male/Female membrane safety valve
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认英文 products catalogue 与 downloads 页面。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: icma
brand_name: ICMA S.p.A.
website: https://www.icmaspa.it/
entry_url: https://www.icmaspa.it/products-catalogue/?lang=en
seed_urls:
- https://www.icmaspa.it/products-catalogue/?lang=en
- https://www.icmaspa.it/products/?lang=en
- https://www.icmaspa.it/catalogo-prodotti/manifolds-and-circulation-modules/single-and-coplanar-joinable-manifolds-for-heating-and-sanitary-systems/1102-collettore-semplice-di-distribuzione-con-uscite-laterali-da-1-2-femmina/?lang=en
- https://www.icmaspa.it/catalogo-prodotti/water-and-gas-network/ball-valves-mini-ball-valves/347-ball-valve-with-lever/?lang=en
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
  suggested_category: D-黄铜阀门/管件/分集水器/通用水暖
  suggested_priority: P1
  country_region: Italy
  manual_review: 站点使用 lang=en 参数，需在爬虫中保留语言参数。
  crawl_scope_notes: 爬 products-catalogue 和 downloads，重点 heating components、manifolds、mixing
    units、thermostatic valves、fittings。
  product_line_notes: 采暖技术阀件、分集水器、管件、混水和系统组件。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - manifold
  - ball valves
  - thermal drain valve
  - filling group
  - three-way mixing valve
  - safety valve
  - press fittings
  - underfloor heating
  - thermoplastic manifold
  pdf_examples:
  - url: https://www.icmaspa.it/wp-content/uploads/2020/ST-EN/ST-P207-ENG.pdf
    title: Polypropylene micro fiber P207 Technical Data Sheet
    doc_type: datasheet
  - url: https://www.icmaspa.it/wp-content/uploads/2020/ST-EN/ST-P226-ENG.pdf
    title: Macro synthetic fibers P226 Technical Data Sheet
    doc_type: datasheet
  - url: https://www.icmaspa.it/wp-content/uploads/2025/FI-ML/FI.K071.EN.D.pdf
    title: Art. K069-K071-K072-K073-K074-K075-K077-K079-K081-K086-K088
    doc_type: datasheet
  - url: https://www.icmaspa.it/wp-content/uploads/2023/ST-IT/ST.400.06.23.IT.pdf
    title: Raccordi a pressare (Press fittings)
    doc_type: datasheet
  - url: https://www.icmaspa.it/wp-content/uploads/2023/FI-ML/FI.S00X.ML.C.pdf
    title: Art. S002 S004 Gruppi Solari (Solar Groups)
    doc_type: datasheet
  product_page_examples:
  - url: https://www.icmaspa.it/catalogo-prodotti/manifolds-and-circulation-modules/single-and-coplanar-joinable-manifolds-for-heating-and-sanitary-systems/1102-collettore-semplice-di-distribuzione-con-uscite-laterali-da-1-2-femmina/?lang=en
    title: 1102 Single distribution manifold
  - url: https://www.icmaspa.it/catalogo-prodotti/water-and-gas-network/ball-valves-mini-ball-valves/347-ball-valve-with-lever/?lang=en
    title: 347 Full bore straight ball valve with pipe tail
  - url: https://www.icmaspa.it/catalogo-prodotti/central-heating-systems-gas-gas-oil-and-bio-fuel/automatic-fillings-groups/249-gruppo-di-riempimento-serie-pesante-con-rubinetto-intercettazione-e-filtro-con-manometro/?lang=en
    title: 249 Heavy model filling group with stop cock and filter
  - url: https://www.icmaspa.it/catalogo-prodotti/manifolds-and-circulation-modules/zone-valves/324-valvola-miscelatrice-a-tre-vie-con-sensore-termostatico-a-capillare-campo-di-regolazione-60-90c/?lang=en
    title: 324 Three-way mixing valve with thermostatic capillary remote sensor
  - url: https://www.icmaspa.it/catalogo-prodotti/central-heating-systems-gas-gas-oil-and-bio-fuel/pressure-safety-systems/242-valvola-di-sicurezza-a-membrana-m-f/?lang=en
    title: 242 Male/Female membrane safety valve
  download_center_url: https://www.icmaspa.it/products/?lang=en
  search_queries_run:
  - site:icmaspa.it filetype:pdf
  - site:icmaspa.it products english
  search_notes: English content reached via ?lang=en parameter. PDFs hosted in /wp-content/uploads/
    with ST-EN, FI-ML language subfolders.
```
