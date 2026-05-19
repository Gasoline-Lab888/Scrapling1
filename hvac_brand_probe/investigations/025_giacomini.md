# 025 - Giacomini

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:giacomini.com filetype:pdf`; `site:giacomini.com products english`

## 1. Brand identity

- Standard brand name: Giacomini
- Official website: https://www.giacomini.com/
- English website (source doc): https://www.giacomini.com/
- English URL confirmed in search index: https://www.giacomini.com/business-area/radiant-systems
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需确认地区选择后的英文产品路径，避免被 change-country 中断。
- Notes: Chrome 重试确认 International Catalog 页面，初次访问可能有国家/区域选择。

## 2. Website entry decision

- Recommended entry_url: https://www.giacomini.com/download/international-catalog
- Alternative entry URLs: https://www.giacomini.com/; https://www.giacomini.com/business-area/radiant-systems
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 采暖/辐射系统、阀门、分集水器、控制组件和黄铜水暖件，目录价值高。
- Priority keywords (observed in Google result titles/snippets for this domain): radiant systems, boiler room components, balancing valves, electric actuators, magnetic Y filter, filling unit, heating and cooling, thermal central, expansion system
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 International Catalog、download、products，重点 radiant systems、manifolds、thermostatic valves、balancing/control valves、brass components。
- Manual review needed: 需确认地区选择后的英文产品路径，避免被 change-country 中断。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.giacomini.com/find-us
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://dam.giacomini.com/fr.giacomini.com/product_documentations/datasheets/R553DK.pdf — R553DK Datasheet (datasheet)
  2. https://dam.giacomini.com/pt.giacomini.com/product_documentations/instructions/R586HPI.pdf — R586HPI Instructions (installation guide)
  3. https://dam.giacomini.com/es.giacomini.com/product_documentations/datasheets/R146M.pdf — R146M Components for thermal central (datasheet)
  4. https://dam.giacomini.com/giacomini.com/product_documentations/datasheets/A111.pdf — A111 Fire protection (July 2019) (datasheet)
  5. https://pl.giacomini.com/dam/jcr:cdec1925-05d3-4757-811e-0c6f60c529d9/radiant_systems_er0002_folder.pdf — ER0002 Radiant Systems Heating and cooling (brochure)
- Document types observed in samples: brochure, datasheet, installation guide
- Notes (search agent): PDFs hosted on dam.giacomini.com DAM with regional subpaths (fr/pt/es/etc.). Products served from www.giacomini.com/product/{code} structure.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.giacomini.com/products/boiler-room-components-and-balancing-valves/electric-actuators — Electric actuators
  2. https://www.giacomini.com/business-area/radiant-systems — Radiant Systems
  3. https://www.giacomini.com/product/A75 — A75 Female to Male reducer
  4. https://www.giacomini.com/product/R74M — R74M Magnetic Y filter
  5. https://www.giacomini.com/product/R150M — R150M Automatic filling unit
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 重试确认 International Catalog 页面，初次访问可能有国家/区域选择。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: giacomini
brand_name: Giacomini
website: https://www.giacomini.com/
entry_url: https://www.giacomini.com/download/international-catalog
seed_urls:
- https://www.giacomini.com/download/international-catalog
- https://www.giacomini.com/find-us
- https://www.giacomini.com/products/boiler-room-components-and-balancing-valves/electric-actuators
- https://www.giacomini.com/business-area/radiant-systems
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
  suggested_priority: P0
  country_region: Italy
  manual_review: 需确认地区选择后的英文产品路径，避免被 change-country 中断。
  crawl_scope_notes: 爬 International Catalog、download、products，重点 radiant systems、manifolds、thermostatic
    valves、balancing/control valves、brass components。
  product_line_notes: 采暖/辐射系统、阀门、分集水器、控制组件和黄铜水暖件，目录价值高。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - radiant systems
  - boiler room components
  - balancing valves
  - electric actuators
  - magnetic Y filter
  - filling unit
  - heating and cooling
  - thermal central
  - expansion system
  pdf_examples:
  - url: https://dam.giacomini.com/fr.giacomini.com/product_documentations/datasheets/R553DK.pdf
    title: R553DK Datasheet
    doc_type: datasheet
  - url: https://dam.giacomini.com/pt.giacomini.com/product_documentations/instructions/R586HPI.pdf
    title: R586HPI Instructions
    doc_type: installation_guide
  - url: https://dam.giacomini.com/es.giacomini.com/product_documentations/datasheets/R146M.pdf
    title: R146M Components for thermal central
    doc_type: datasheet
  - url: https://dam.giacomini.com/giacomini.com/product_documentations/datasheets/A111.pdf
    title: A111 Fire protection (July 2019)
    doc_type: datasheet
  - url: https://pl.giacomini.com/dam/jcr:cdec1925-05d3-4757-811e-0c6f60c529d9/radiant_systems_er0002_folder.pdf
    title: ER0002 Radiant Systems Heating and cooling
    doc_type: brochure
  product_page_examples:
  - url: https://www.giacomini.com/products/boiler-room-components-and-balancing-valves/electric-actuators
    title: Electric actuators
  - url: https://www.giacomini.com/business-area/radiant-systems
    title: Radiant Systems
  - url: https://www.giacomini.com/product/A75
    title: A75 Female to Male reducer
  - url: https://www.giacomini.com/product/R74M
    title: R74M Magnetic Y filter
  - url: https://www.giacomini.com/product/R150M
    title: R150M Automatic filling unit
  download_center_url: https://www.giacomini.com/find-us
  search_queries_run:
  - site:giacomini.com filetype:pdf
  - site:giacomini.com products english
  search_notes: PDFs hosted on dam.giacomini.com DAM with regional subpaths (fr/pt/es/etc.).
    Products served from www.giacomini.com/product/{code} structure.
```
