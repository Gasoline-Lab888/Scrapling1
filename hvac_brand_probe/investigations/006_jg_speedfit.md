# 006 - JG Speedfit / John Guest

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:johnguest.com filetype:pdf`; `site:johnguest.com products data sheets`

## 1. Brand identity

- Standard brand name: JG Speedfit / John Guest
- Official website: https://www.johnguest.com/
- English website (source doc): https://www.johnguest.com/gb/en/
- English URL confirmed in search index: https://www.johnguest.com/gb/en/resources/data-sheets
- Country / region: UK (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 后续需人工/爬虫确认是否可稳定访问，必要时使用 RWC 品牌入口作为备选。
- Notes: Chrome 搜索确认官方 data-sheets；直接打开触发 Cloudflare Just a moment，需爬虫处理防护。

## 2. Website entry decision

- Recommended entry_url: https://www.johnguest.com/gb/en/resources/data-sheets
- Alternative entry URLs: https://www.johnguest.com/; https://www.johnguest.com/gb/en/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/gb` (derived from entry URL locale segment)
- Suggested path_prefix: /gb

## 3. Product scope

- Priority product lines: 快接管件、塑料管道、地暖系统和配套阀件，适合 PEX/UFH 系统资料。
- Priority keywords (observed in Google result titles/snippets for this domain): underfloor heating, Speedfit, push-fit, manifold, data sheet, fittings, reducing tee, equal tee, EPDM, plumbing heating
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 GB/EN products 与 resources/data-sheets，重点 Speedfit plumbing、underfloor heating、manifolds、pipe/fittings、installation guides。
- Manual review needed: 后续需人工/爬虫确认是否可稳定访问，必要时使用 RWC 品牌入口作为备选。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.johnguest.com/gb/en/resources/data-sheets
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.johnguest.com/sites/jg/files/2025-11/UFH-eguide.pdf — An Installer's Guide to Underfloor Heating (installation guide)
  2. https://www.johnguest.com/sites/jg/files/2025-05/JG%20Underfloor%20Heating%20Brochure%20June%202025.pdf — JG Underfloor Heating Brochure June 2025 (brochure)
  3. https://www.johnguest.com/sites/jg/files/2022-02/JG%20Speedfit%20Equal%20Tee%20Data%20Sheet.pdf — JG Speedfit Equal Tee Data Sheet (datasheet)
  4. https://www.johnguest.com/sites/jg/files/2022-02/JG%20Speedfit%20Cold%20Water%20Reducing%20Tee%20Data%20Sheet.pdf — JG Speedfit Cold Water Reducing Tee Data Sheet (datasheet)
  5. https://www.johnguest.com/sites/jg/files/2022-02/JG%20Speedfit%20EPDM%20O-Ring%20Data%20Sheet.pdf — JG Speedfit EPDM O-Ring Data Sheet (datasheet)
- Document types observed in samples: brochure, datasheet, installation guide
- Notes (search agent): Strong English/GB indexed coverage. PDFs hosted at /sites/jg/files/ path. UFH and manifold pages present.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.johnguest.com/gb/en/resources/data-sheets — Data sheets | John Guest
  2. https://www.johnguest.com/gb/en/products/jg-speedfit?lang=en-GB — JG Speedfit | John Guest
  3. https://www.johnguest.com/gb/en/products/jg-underfloor — JG Underfloor | John Guest
  4. https://www.johnguest.com/gb/en/products/jg-speedfit/fittings/push-fit-plastic-fittings/reducing-tee — JG Speedfit Push-fit Reducing Tee
  5. https://www.johnguest.com/gb/en/products/jg-speedfit/fittings/push-fit-plumbing-manifolds/plastic-plumbing-manifold — JG Speedfit Plastic Push-fit Manifold
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: cloudflare_jschallenge (per source doc); please re-verify with a live browser before crawl
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: cloudflare_jschallenge (per source doc)
- Browser investigation conclusion (carried from source doc): "Chrome 搜索确认官方 data-sheets；直接打开触发 Cloudflare Just a moment，需爬虫处理防护。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: jg_speedfit
brand_name: JG Speedfit / John Guest
website: https://www.johnguest.com/
entry_url: https://www.johnguest.com/gb/en/resources/data-sheets
seed_urls:
- https://www.johnguest.com/gb/en/resources/data-sheets
- https://www.johnguest.com/gb/en/products/jg-speedfit?lang=en-GB
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
  suggested_priority: P1
  country_region: UK
  manual_review: 后续需人工/爬虫确认是否可稳定访问，必要时使用 RWC 品牌入口作为备选。
  crawl_scope_notes: 爬 GB/EN products 与 resources/data-sheets，重点 Speedfit plumbing、underfloor
    heating、manifolds、pipe/fittings、installation guides。
  product_line_notes: 快接管件、塑料管道、地暖系统和配套阀件，适合 PEX/UFH 系统资料。
  blocked_reason_hint: cloudflare_jschallenge (per source doc)
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - underfloor heating
  - Speedfit
  - push-fit
  - manifold
  - data sheet
  - fittings
  - reducing tee
  - equal tee
  - EPDM
  - plumbing heating
  pdf_examples:
  - url: https://www.johnguest.com/sites/jg/files/2025-11/UFH-eguide.pdf
    title: An Installer's Guide to Underfloor Heating
    doc_type: installation_guide
  - url: https://www.johnguest.com/sites/jg/files/2025-05/JG%20Underfloor%20Heating%20Brochure%20June%202025.pdf
    title: JG Underfloor Heating Brochure June 2025
    doc_type: brochure
  - url: https://www.johnguest.com/sites/jg/files/2022-02/JG%20Speedfit%20Equal%20Tee%20Data%20Sheet.pdf
    title: JG Speedfit Equal Tee Data Sheet
    doc_type: datasheet
  - url: https://www.johnguest.com/sites/jg/files/2022-02/JG%20Speedfit%20Cold%20Water%20Reducing%20Tee%20Data%20Sheet.pdf
    title: JG Speedfit Cold Water Reducing Tee Data Sheet
    doc_type: datasheet
  - url: https://www.johnguest.com/sites/jg/files/2022-02/JG%20Speedfit%20EPDM%20O-Ring%20Data%20Sheet.pdf
    title: JG Speedfit EPDM O-Ring Data Sheet
    doc_type: datasheet
  product_page_examples:
  - url: https://www.johnguest.com/gb/en/resources/data-sheets
    title: Data sheets | John Guest
  - url: https://www.johnguest.com/gb/en/products/jg-speedfit?lang=en-GB
    title: JG Speedfit | John Guest
  - url: https://www.johnguest.com/gb/en/products/jg-underfloor
    title: JG Underfloor | John Guest
  - url: https://www.johnguest.com/gb/en/products/jg-speedfit/fittings/push-fit-plastic-fittings/reducing-tee
    title: JG Speedfit Push-fit Reducing Tee
  - url: https://www.johnguest.com/gb/en/products/jg-speedfit/fittings/push-fit-plumbing-manifolds/plastic-plumbing-manifold
    title: JG Speedfit Plastic Push-fit Manifold
  download_center_url: https://www.johnguest.com/gb/en/resources/data-sheets
  search_queries_run:
  - site:johnguest.com filetype:pdf
  - site:johnguest.com products data sheets
  search_notes: Strong English/GB indexed coverage. PDFs hosted at /sites/jg/files/
    path. UFH and manifold pages present.
```
