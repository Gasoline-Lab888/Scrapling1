# 028 - LK Systems

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:lksystems.se filetype:pdf`; `site:lksystems.se floor heating english`

## 1. Brand identity

- Standard brand name: LK Systems
- Official website: https://www.lksystems.se/
- English website (source doc): https://www.lksystems.se/en/
- English URL confirmed in search index: https://www.lksystems.se/en/products/floor-heating/
- Country / region: Sweden (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 站点瑞典本地化强，需确认英文资料覆盖是否完整。
- Notes: Chrome 重试确认 English Floor Heating 页面，有 PDF/下载链接信号。

## 2. Website entry decision

- Recommended entry_url: https://www.lksystems.se/en/products/floor-heating/
- Alternative entry URLs: https://www.lksystems.se/; https://www.lksystems.se/en/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 瑞典地暖系统、管道、分集水器和控制组件，UFH 相关度高。
- Priority keywords (observed in Google result titles/snippets for this domain): floor heating, underfloor heating, heat circuit distributor, room thermostats, shunt valve, manifold, HeatFloor, CombiBoard EPS, wireless
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 English floor heating/system solutions/products，重点 floor heating pipes、manifolds、shunts/mixing groups、controls、installation docs。
- Manual review needed: 站点瑞典本地化强，需确认英文资料覆盖是否完整。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.lksystems.se/en/products/floor-heating/
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.lksystems.se/download/69715/se.33.c.180_lk-rumsreglering-ics.2_anvandarmanual-for-daglig-drift.pdf — LK Rumsreglering ICS.2 User Manual (technical manual)
  2. https://www.lksystems.se/download/72959/se.33.c.146_lk-varmekretsfordelare-rf.pdf — LK Varmekretsfordelare RF (heat circuit distributor) (datasheet)
  3. https://www.lksystems.se/globalassets/lk-systems-se/dokument-pdf-mm/lk-arc/lk-arc---installationsguide-archub---2024-10-24-v1.pdf — LK ARC Installation Guide ArcHub (installation guide)
  4. https://www.lksystems.se/download/64904/se.33.c.93_lk-fordelarshunt-vs-2-25-2.pdf — LK Fordelarshunt VS 2-2,5 (datasheet)
  5. https://www.lksystems.se/download/71033/SE.33.B.1_Projekteringsanvisning_2025.pdf — LK Projekteringsanvisning 2025 (Design Guide) (technical manual)
- Document types observed in samples: datasheet, installation guide, technical manual
- Notes (search agent): PDF datasheets are Swedish-only (under /download/{id}/ and /globalassets/). English content lives at /en/ for product/system pages.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.lksystems.se/en/products/floor-heating/ — Floor Heating
  2. https://www.lksystems.se/en/system-solutions/underfloor-heating/ — Underfloor heating
  3. https://www.lksystems.se/en/system-solutions/underfloor-heating/our-floor-heating-systems/ — Our floor heating systems
  4. https://www.lksystems.se/en/system-solutions/underfloor-heating/our-floor-heating-systems/on-floor-joists/ — On floor joists
  5. https://www.lksystems.se/en/system-solutions/underfloor-heating/room-control-for-underfloor-heating2/ — Room control for underfloor heating
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 重试确认 English Floor Heating 页面，有 PDF/下载链接信号。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: lk_systems
brand_name: LK Systems
website: https://www.lksystems.se/
entry_url: https://www.lksystems.se/en/products/floor-heating/
seed_urls:
- https://www.lksystems.se/en/products/floor-heating/
- https://www.lksystems.se/en/system-solutions/underfloor-heating/
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
  suggested_category: B-地暖系统/PEX/管道系统
  suggested_priority: P1
  country_region: Sweden
  manual_review: 站点瑞典本地化强，需确认英文资料覆盖是否完整。
  crawl_scope_notes: 爬 English floor heating/system solutions/products，重点 floor heating
    pipes、manifolds、shunts/mixing groups、controls、installation docs。
  product_line_notes: 瑞典地暖系统、管道、分集水器和控制组件，UFH 相关度高。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - floor heating
  - underfloor heating
  - heat circuit distributor
  - room thermostats
  - shunt valve
  - manifold
  - HeatFloor
  - CombiBoard EPS
  - wireless
  pdf_examples:
  - url: https://www.lksystems.se/download/69715/se.33.c.180_lk-rumsreglering-ics.2_anvandarmanual-for-daglig-drift.pdf
    title: LK Rumsreglering ICS.2 User Manual
    doc_type: manual
  - url: https://www.lksystems.se/download/72959/se.33.c.146_lk-varmekretsfordelare-rf.pdf
    title: LK Varmekretsfordelare RF (heat circuit distributor)
    doc_type: datasheet
  - url: https://www.lksystems.se/globalassets/lk-systems-se/dokument-pdf-mm/lk-arc/lk-arc---installationsguide-archub---2024-10-24-v1.pdf
    title: LK ARC Installation Guide ArcHub
    doc_type: installation_guide
  - url: https://www.lksystems.se/download/64904/se.33.c.93_lk-fordelarshunt-vs-2-25-2.pdf
    title: LK Fordelarshunt VS 2-2,5
    doc_type: datasheet
  - url: https://www.lksystems.se/download/71033/SE.33.B.1_Projekteringsanvisning_2025.pdf
    title: LK Projekteringsanvisning 2025 (Design Guide)
    doc_type: manual
  product_page_examples:
  - url: https://www.lksystems.se/en/products/floor-heating/
    title: Floor Heating
  - url: https://www.lksystems.se/en/system-solutions/underfloor-heating/
    title: Underfloor heating
  - url: https://www.lksystems.se/en/system-solutions/underfloor-heating/our-floor-heating-systems/
    title: Our floor heating systems
  - url: https://www.lksystems.se/en/system-solutions/underfloor-heating/our-floor-heating-systems/on-floor-joists/
    title: On floor joists
  - url: https://www.lksystems.se/en/system-solutions/underfloor-heating/room-control-for-underfloor-heating2/
    title: Room control for underfloor heating
  download_center_url: https://www.lksystems.se/en/products/floor-heating/
  search_queries_run:
  - site:lksystems.se filetype:pdf
  - site:lksystems.se floor heating english
  search_notes: PDF datasheets are Swedish-only (under /download/{id}/ and /globalassets/).
    English content lives at /en/ for product/system pages.
```
