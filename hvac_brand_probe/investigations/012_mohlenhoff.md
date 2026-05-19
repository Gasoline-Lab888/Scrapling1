# 012 - Möhlenhoff / Mohlenhoff

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:moehlenhoff.de filetype:pdf`; `site:moehlenhoff.de products english download`

## 1. Brand identity

- Standard brand name: Möhlenhoff / Mohlenhoff
- Official website: https://www.moehlenhoff.de/
- English website (source doc): https://www.moehlenhoff.de/en/
- English URL confirmed in search index: https://www.moehlenhoff.de/en/products
- Country / region: Germany (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 品牌德文字符 Möhlenhoff 与 Mohlenhoff URL 拼写需统一。
- Notes: Chrome 确认 /en/download 页面，PDF 下载链接明显。

## 2. Website entry decision

- Recommended entry_url: https://www.moehlenhoff.de/en/download
- Alternative entry URLs: https://www.moehlenhoff.de/; https://www.moehlenhoff.de/en/; https://www.moehlenhoff.de/en/products
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 地暖温控、执行器、接线中心和室温控制系统，控制类参考价值高。
- Priority keywords (observed in Google result titles/snippets for this domain): thermal actuator, valve adapter, OEM, Alpha Smart, Alpha direct, room-by-room control, Modbus RTU, DDC actuator, underfloor heating, drive technology
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 English products/download，重点 thermal actuators、room thermostats、UFH controls、connection strips、wireless control manuals。
- Manual review needed: 品牌德文字符 Möhlenhoff 与 Mohlenhoff URL 拼写需统一。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.moehlenhoff.de/en/download
- PDF links found via Google site:search: 4 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.moehlenhoff.de/fileadmin/user_upload/Download/Broschueren/120554_2405_Brosch_OEM_Produkte_DEU_web.pdf — OEM Produktprogramm Stellantriebe und Einzelraumregelung (brochure)
  2. https://www.moehlenhoff.de/fileadmin/user_upload/Download/Datenblaetter/126559_2139_VA-Liste_Kunde_ENG.pdf — VA-Liste Kunde ENG (Valve Adapter List) (datasheet)
  3. https://www.moehlenhoff.de/fileadmin/user_upload/Download/Broschueren/136432_2051_Flyer_OEM_Modbus_Konverter_ENG.pdf — OEM Modbus RTU Converter Valve drive technology (brochure)
  4. https://www.moehlenhoff.de/fileadmin/user_upload/Download/Datenblaetter/126559_2411_VA-Liste_Kunde_ENG.pdf — VA-Liste Kunde ENG (Valve Adapter List rev) (datasheet)
  5. (no further sample from Google site:search)
- Document types observed in samples: brochure, datasheet
- Notes (search agent): PDFs at /fileadmin/user_upload/Download/ path. Both German and English filenames present. Multiple ENG-suffixed datasheets indexed.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.moehlenhoff.de/en/oem-alpha-smart-system — OEM Alpha Smart System
  2. https://www.moehlenhoff.de/en/products — OEM Product overview | Möhlenhoff GmbH
  3. https://www.moehlenhoff.de/en/products/actuator-technology-2-1 — OEM Actuator 5: DDC
  4. https://www.moehlenhoff.de/en/products/room-by-room-control/oem-alpha-direct-system — OEM Alpha direct: System
  5. https://www.moehlenhoff.de/en/products/actuator-technology — Möhlenhoff Number 1 in Drive Technology
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 /en/download 页面，PDF 下载链接明显。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: moehlenhoff
brand_name: Möhlenhoff / Mohlenhoff
website: https://www.moehlenhoff.de/
entry_url: https://www.moehlenhoff.de/en/download
seed_urls:
- https://www.moehlenhoff.de/en/download
- https://www.moehlenhoff.de/en/oem-alpha-smart-system
- https://www.moehlenhoff.de/en/products
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
  manual_review: 品牌德文字符 Möhlenhoff 与 Mohlenhoff URL 拼写需统一。
  crawl_scope_notes: 爬 English products/download，重点 thermal actuators、room thermostats、UFH
    controls、connection strips、wireless control manuals。
  product_line_notes: 地暖温控、执行器、接线中心和室温控制系统，控制类参考价值高。
  blocked_reason_hint: ''
  pdf_sample_count: 4
  product_page_sample_count: 5
  evidence_keywords:
  - thermal actuator
  - valve adapter
  - OEM
  - Alpha Smart
  - Alpha direct
  - room-by-room control
  - Modbus RTU
  - DDC actuator
  - underfloor heating
  - drive technology
  pdf_examples:
  - url: https://www.moehlenhoff.de/fileadmin/user_upload/Download/Broschueren/120554_2405_Brosch_OEM_Produkte_DEU_web.pdf
    title: OEM Produktprogramm Stellantriebe und Einzelraumregelung
    doc_type: brochure
  - url: https://www.moehlenhoff.de/fileadmin/user_upload/Download/Datenblaetter/126559_2139_VA-Liste_Kunde_ENG.pdf
    title: VA-Liste Kunde ENG (Valve Adapter List)
    doc_type: datasheet
  - url: https://www.moehlenhoff.de/fileadmin/user_upload/Download/Broschueren/136432_2051_Flyer_OEM_Modbus_Konverter_ENG.pdf
    title: OEM Modbus RTU Converter Valve drive technology
    doc_type: brochure
  - url: https://www.moehlenhoff.de/fileadmin/user_upload/Download/Datenblaetter/126559_2411_VA-Liste_Kunde_ENG.pdf
    title: VA-Liste Kunde ENG (Valve Adapter List rev)
    doc_type: datasheet
  product_page_examples:
  - url: https://www.moehlenhoff.de/en/oem-alpha-smart-system
    title: OEM Alpha Smart System
  - url: https://www.moehlenhoff.de/en/products
    title: OEM Product overview | Möhlenhoff GmbH
  - url: https://www.moehlenhoff.de/en/products/actuator-technology-2-1
    title: 'OEM Actuator 5: DDC'
  - url: https://www.moehlenhoff.de/en/products/room-by-room-control/oem-alpha-direct-system
    title: 'OEM Alpha direct: System'
  - url: https://www.moehlenhoff.de/en/products/actuator-technology
    title: Möhlenhoff Number 1 in Drive Technology
  download_center_url: https://www.moehlenhoff.de/en/download
  search_queries_run:
  - site:moehlenhoff.de filetype:pdf
  - site:moehlenhoff.de products english download
  search_notes: PDFs at /fileadmin/user_upload/Download/ path. Both German and English
    filenames present. Multiple ENG-suffixed datasheets indexed.
```
