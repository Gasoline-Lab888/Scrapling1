# 018 - Fratelli Pettinaroli / Jomar

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:pettinaroli.com filetype:pdf`; `site:pettinaroli.com english products`; `site:pettinaroli.com balancing manifold PICV catalog`

## 1. Brand identity

- Standard brand name: Fratelli Pettinaroli / Jomar
- Official website: https://www.pettinaroli.com/
- English website (source doc): https://www.pettinaroli.com/en/
- English URL confirmed in search index: https://www.pettinaroli.com/hvac-solutions/
- Country / region: Italy / USA (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需人工确认 018 是否只代表 Pettinaroli，还是要并入 Jomar 资料。
- Notes: Chrome 确认 Pettinaroli 英文官网；搜索 Pettinaroli/Jomar 时也出现 Jomar 下载库。

## 2. Website entry decision

- Recommended entry_url: https://www.pettinaroli.com/en/
- Alternative entry URLs: https://www.pettinaroli.com/; https://www.pettinaroli.com/hvac-solutions/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 黄铜阀门、分集水器、HVAC/水暖组件；与 Jomar/Jomar Valve 有品牌关联但站点应分开。
- Priority keywords (observed in Google result titles/snippets for this domain): PICV, EvoPICV, dynamic balancing valves, industrial valves, HVAC, balancing, FilterBall, Dynasty, Diversiflow manifold
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 先爬 Pettinaroli English products，重点 manifolds、valves、HVAC components；Jomar 美国站作为单独品牌在 027 处理。
- Manual review needed: 需人工确认 018 是否只代表 Pettinaroli，还是要并入 Jomar 资料。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.pettinaroli.com/fileadmin/Pettinaroli_UK/Commercial_Documents_UK/Catalogue_UK/Catalogue_UK_2025_r.pdf
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.pettinaroli.com/fileadmin/Pettinaroli_Worldwide/Commercial_Documents_Worldwide/Technical_Manuals/Definitive_Guide_to_PICVs_ENG.pdf — The Definitive Guide to PICVs (technical manual)
  2. https://www.pettinaroli.com/fileadmin/Pettinaroli_Worldwide/Commercial_Documents_Worldwide/Technical_Manuals/EvoPICV_Technical_manual_ENG.pdf — EvoPICV Pressure Independent Control Valve Technical Manual (technical manual)
  3. https://www.pettinaroli.com/fileadmin/Pettinaroli_Worldwide/Commercial_Documents_Worldwide/Leaflets_PDF/Industrial_valves_ENG.pdf — Industrial Valves Flanged series for HVAC applications (brochure)
  4. https://www.pettinaroli.com/fileadmin/Technical_sheets/STE0145_7002K-2_rev00_17-07-2015.pdf — Technical Specification 7002K/1 & 7002K/2 (datasheet)
  5. https://www.pettinaroli.com/fileadmin/Pettinaroli_UK/Commercial_Documents_UK/Catalogue_UK/Catalogue_UK_2025_r.pdf — 2025 HVAC Catalogue UK (catalogue)
- Document types observed in samples: brochure, catalogue, datasheet, technical manual
- Notes (search agent): PDFs hosted at /fileadmin/ with regional subfolders (Worldwide, UK). HVAC catalog area is well structured with dedicated PICV product pages.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/ — Dynamic Balancing Valves (PICV)
  2. https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/83/ — PICV 83 Series
  3. https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/94f/ — PICV 94F
  4. https://www.pettinaroli.com/hvac-solutions/ — HVAC Solutions
  5. https://www.pettinaroli.com/catalog/heating/heating-accessories/ — Heating Accessories
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 Pettinaroli 英文官网；搜索 Pettinaroli/Jomar 时也出现 Jomar 下载库。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: pettinaroli
brand_name: Fratelli Pettinaroli / Jomar
website: https://www.pettinaroli.com/
entry_url: https://www.pettinaroli.com/en/
seed_urls:
- https://www.pettinaroli.com/en/
- https://www.pettinaroli.com/fileadmin/Pettinaroli_UK/Commercial_Documents_UK/Catalogue_UK/Catalogue_UK_2025_r.pdf
- https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/
- https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/83/
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
  country_region: Italy / USA
  manual_review: 需人工确认 018 是否只代表 Pettinaroli，还是要并入 Jomar 资料。
  crawl_scope_notes: 先爬 Pettinaroli English products，重点 manifolds、valves、HVAC components；Jomar
    美国站作为单独品牌在 027 处理。
  product_line_notes: 黄铜阀门、分集水器、HVAC/水暖组件；与 Jomar/Jomar Valve 有品牌关联但站点应分开。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - PICV
  - EvoPICV
  - dynamic balancing valves
  - industrial valves
  - HVAC
  - balancing
  - FilterBall
  - Dynasty
  - Diversiflow manifold
  pdf_examples:
  - url: https://www.pettinaroli.com/fileadmin/Pettinaroli_Worldwide/Commercial_Documents_Worldwide/Technical_Manuals/Definitive_Guide_to_PICVs_ENG.pdf
    title: The Definitive Guide to PICVs
    doc_type: manual
  - url: https://www.pettinaroli.com/fileadmin/Pettinaroli_Worldwide/Commercial_Documents_Worldwide/Technical_Manuals/EvoPICV_Technical_manual_ENG.pdf
    title: EvoPICV Pressure Independent Control Valve Technical Manual
    doc_type: manual
  - url: https://www.pettinaroli.com/fileadmin/Pettinaroli_Worldwide/Commercial_Documents_Worldwide/Leaflets_PDF/Industrial_valves_ENG.pdf
    title: Industrial Valves Flanged series for HVAC applications
    doc_type: brochure
  - url: https://www.pettinaroli.com/fileadmin/Technical_sheets/STE0145_7002K-2_rev00_17-07-2015.pdf
    title: Technical Specification 7002K/1 & 7002K/2
    doc_type: datasheet
  - url: https://www.pettinaroli.com/fileadmin/Pettinaroli_UK/Commercial_Documents_UK/Catalogue_UK/Catalogue_UK_2025_r.pdf
    title: 2025 HVAC Catalogue UK
    doc_type: catalogue
  product_page_examples:
  - url: https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/
    title: Dynamic Balancing Valves (PICV)
  - url: https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/83/
    title: PICV 83 Series
  - url: https://www.pettinaroli.com/catalog/hvac/dynamic-balancing-valves-picv/94f/
    title: PICV 94F
  - url: https://www.pettinaroli.com/hvac-solutions/
    title: HVAC Solutions
  - url: https://www.pettinaroli.com/catalog/heating/heating-accessories/
    title: Heating Accessories
  download_center_url: https://www.pettinaroli.com/fileadmin/Pettinaroli_UK/Commercial_Documents_UK/Catalogue_UK/Catalogue_UK_2025_r.pdf
  search_queries_run:
  - site:pettinaroli.com filetype:pdf
  - site:pettinaroli.com english products
  - site:pettinaroli.com balancing manifold PICV catalog
  search_notes: PDFs hosted at /fileadmin/ with regional subfolders (Worldwide, UK).
    HVAC catalog area is well structured with dedicated PICV product pages.
```
