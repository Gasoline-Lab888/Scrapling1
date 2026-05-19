# 029 - Wavin

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:wavin.com filetype:pdf`; `site:wavin.com gb downloads`; `Wavin underfloor heating manifold site:wavin.com`

## 1. Brand identity

- Standard brand name: Wavin
- Official website: https://wavin.com/
- English website (source doc): https://wavin.com/gb
- English URL confirmed in search index: https://wavin.com/gb/downloads
- Country / region: Netherlands / UK (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: Wavin 产品范围过宽，YAML 需限制到 heating/underfloor/pipe systems。
- Notes: Chrome 确认 wavin.com/gb/downloads 页面含多个 PDF 下载。

## 2. Website entry decision

- Recommended entry_url: https://wavin.com/gb/downloads
- Alternative entry URLs: https://wavin.com/; https://wavin.com/gb
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/gb` (derived from entry URL locale segment)
- Suggested path_prefix: /gb

## 3. Product scope

- Priority product lines: 大型管道系统品牌，包含地暖、冷热水、排水和建筑系统；需限定暖通/UFH。
- Priority keywords (observed in Google result titles/snippets for this domain): underfloor heating manifolds, Comfia, composite manifold, UFH pipes, HDPE soil waste, drainage, Tigris crimp fittings, Hepworth, balancing, Sentio
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 GB downloads 和 product categories，重点 underfloor heating、heating/cooling、MLCP/PEX pipes、manifolds、controls。
- Manual review needed: Wavin 产品范围过宽，YAML 需限制到 heating/underfloor/pipe systems。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://wavin.com/gb/downloads
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://mediahub.wavin.com/asset/66409c15-4734-4deb-918c-9d8f61774217/Wavin-HDPE-Welded-Soil-Waste-and-Vent-System-Product-Guide.pdf — Wavin HDPE Soil Waste and Vent System Product Guide (technical manual)
  2. https://mediahub.wavin.com/m/484053c8388eef67/original/HDPE-Data-Sheet-MEA.pdf — Wavin HDPE Soil and Waste System Welded MEA Data Sheet (datasheet)
  3. https://mediahub.wavin.com/asset/dc0af3c6-9876-47ef-ba81-40ada822feb1/Wavin-Hepworth-Drainage-Sewage.pdf — Wavin Hepworth Drainage & Sewage (brochure)
  4. https://mediahub.wavin.com/asset/de4b7b3f-4004-4da2-9d85-1c0f0108da55/Wavin-Solvent-Soil-Product-and-Installation-Manual.pdf — Wavin Solvent Weld Soil Plumbing System Product Manual (technical manual)
  5. https://mediahub.wavin.com/m/2fc798149b0410d6/original/Guide-Technique-Wavin-Hydrodistribution.pdf — WAVIN TIGRIS Manuel technique - crimp fittings (technical manual)
- Document types observed in samples: brochure, datasheet, technical manual
- Notes (search agent): PDFs hosted on mediahub.wavin.com. Country site uses /gb/ for UK; /ie/ for Ireland. Product pages use code-based slugs (e.g., C05_F018_S122).

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://wavin.com/gb/s/C05_F018_S122/Comfia-Underfloor-Heating-Manifolds — Comfia Underfloor Heating Manifolds - System Features
  2. https://wavin.com/gb/p/741ccb9c-c195-49ae-b8df-d9194edfddbe/ufh-3-port-composite-manifold — UFH 3 Port Composite Manifold
  3. https://wavin.com/gb/p/91c280c5-46f6-44c4-923b-bb44df159cf1/ufh-5-port-composite-manifold — UFH 5 Port Composite Manifold
  4. https://wavin.com/gb/c?category=C05 — Heating & Cooling
  5. https://wavin.com/ie/s/C05_F018_S175/Wavin-UFH-Pipes-and-Flooring-Systems — Wavin UFH Pipes and Flooring Systems
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 wavin.com/gb/downloads 页面含多个 PDF 下载。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: wavin
brand_name: Wavin
website: https://wavin.com/
entry_url: https://wavin.com/gb/downloads
seed_urls:
- https://wavin.com/gb/downloads
- https://wavin.com/gb/s/C05_F018_S122/Comfia-Underfloor-Heating-Manifolds
- https://wavin.com/gb/p/741ccb9c-c195-49ae-b8df-d9194edfddbe/ufh-3-port-composite-manifold
max_pages: 250
url_scope:
  path_prefix: /gb
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
  suggested_priority: P0
  country_region: Netherlands / UK
  manual_review: Wavin 产品范围过宽，YAML 需限制到 heating/underfloor/pipe systems。
  crawl_scope_notes: 爬 GB downloads 和 product categories，重点 underfloor heating、heating/cooling、MLCP/PEX
    pipes、manifolds、controls。
  product_line_notes: 大型管道系统品牌，包含地暖、冷热水、排水和建筑系统；需限定暖通/UFH。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - underfloor heating manifolds
  - Comfia
  - composite manifold
  - UFH pipes
  - HDPE soil waste
  - drainage
  - Tigris crimp fittings
  - Hepworth
  - balancing
  - Sentio
  pdf_examples:
  - url: https://mediahub.wavin.com/asset/66409c15-4734-4deb-918c-9d8f61774217/Wavin-HDPE-Welded-Soil-Waste-and-Vent-System-Product-Guide.pdf
    title: Wavin HDPE Soil Waste and Vent System Product Guide
    doc_type: manual
  - url: https://mediahub.wavin.com/m/484053c8388eef67/original/HDPE-Data-Sheet-MEA.pdf
    title: Wavin HDPE Soil and Waste System Welded MEA Data Sheet
    doc_type: datasheet
  - url: https://mediahub.wavin.com/asset/dc0af3c6-9876-47ef-ba81-40ada822feb1/Wavin-Hepworth-Drainage-Sewage.pdf
    title: Wavin Hepworth Drainage & Sewage
    doc_type: brochure
  - url: https://mediahub.wavin.com/asset/de4b7b3f-4004-4da2-9d85-1c0f0108da55/Wavin-Solvent-Soil-Product-and-Installation-Manual.pdf
    title: Wavin Solvent Weld Soil Plumbing System Product Manual
    doc_type: manual
  - url: https://mediahub.wavin.com/m/2fc798149b0410d6/original/Guide-Technique-Wavin-Hydrodistribution.pdf
    title: WAVIN TIGRIS Manuel technique - crimp fittings
    doc_type: manual
  product_page_examples:
  - url: https://wavin.com/gb/s/C05_F018_S122/Comfia-Underfloor-Heating-Manifolds
    title: Comfia Underfloor Heating Manifolds - System Features
  - url: https://wavin.com/gb/p/741ccb9c-c195-49ae-b8df-d9194edfddbe/ufh-3-port-composite-manifold
    title: UFH 3 Port Composite Manifold
  - url: https://wavin.com/gb/p/91c280c5-46f6-44c4-923b-bb44df159cf1/ufh-5-port-composite-manifold
    title: UFH 5 Port Composite Manifold
  - url: https://wavin.com/gb/c?category=C05
    title: Heating & Cooling
  - url: https://wavin.com/ie/s/C05_F018_S175/Wavin-UFH-Pipes-and-Flooring-Systems
    title: Wavin UFH Pipes and Flooring Systems
  download_center_url: https://wavin.com/gb/downloads
  search_queries_run:
  - site:wavin.com filetype:pdf
  - site:wavin.com gb downloads
  - Wavin underfloor heating manifold site:wavin.com
  search_notes: PDFs hosted on mediahub.wavin.com. Country site uses /gb/ for UK;
    /ie/ for Ireland. Product pages use code-based slugs (e.g., C05_F018_S122).
```
