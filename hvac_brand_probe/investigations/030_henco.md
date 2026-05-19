# 030 - Henco

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:henco.be filetype:pdf`; `site:henco.be english products downloads`

## 1. Brand identity

- Standard brand name: Henco
- Official website: https://www.henco.be/
- English website (source doc): https://www.henco.be/en/home
- English URL confirmed in search index: https://www.henco.be/en/downloads
- Country / region: Belgium (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需关注 Aalberts 收购后的品牌/集团归属，不影响官网爬取。
- Notes: Chrome 确认 Henco Downloads 页面，技术数据表、brochures、manuals 信号明确。

## 2. Website entry decision

- Recommended entry_url: https://www.henco.be/en/downloads
- Alternative entry URLs: https://www.henco.be/; https://www.henco.be/en/home
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 多层管、管件、地暖、分集水器和系统安装资料；Aalberts 旗下品牌。
- Priority keywords (observed in Google result titles/snippets for this domain): multilayer pipe system, underfloor heating, fittings, Henco Logic, Henco Floor, thermostat, pre-insulated pipe, sprinkler, gas pipes, PK/PKW Leak Before Press
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 products 和 downloads，重点 multilayer pipe、press fittings、underfloor heating、manifolds、technical data sheets、manuals。
- Manual review needed: 需关注 Aalberts 收购后的品牌/集团归属，不影响官网爬取。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.henco.be/en/downloads
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.henco.be/sites/default/files/images/2023-12/HencoLogic%20handleiding%20DTHERM_1.pdf — HENCO LOGIC Wired digital room thermostat (technical manual)
  2. https://www.henco.be/sites/default/files/images/2020-02/Technical_manual_ENG_2019_chapter7.pdf — Henco Assembly Instructions Technical Manual chapter 7 (technical manual)
  3. https://www.henco.be/sites/default/files/images/2023-12/TH_Henco_2023_EN_LR.pdf — Henco Technical Manual 2023 EN (technical manual)
  4. https://www.henco.be/sites/default/files/images/2024-01/HENCO%20FLOOR_Technisch%20handboek_CMYK.pdf — Henco Floor Technical Handbook (technical manual)
  5. https://www.henco.be/sites/default/files/images/2024-01/Henco_Voorgeisoleerde-Buis_EN_LR.pdf — Henco Pre-insulated Pipe (EN) (brochure)
- Document types observed in samples: brochure, technical manual
- Notes (search agent): PDFs hosted at /sites/default/files/images/{YYYY-MM}/. English content split between /en/ (downloads/home) and /en-US/ (product pages).

## 5. Product page evidence

- Product pages found via Google site:search: 6 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.henco.be/en/home — Henco Home - The Perfect Fit
  2. https://www.henco.be/en-US/product/product-catalogus — Henco Product Catalogue - Pipes, fittings & systems
  3. https://www.henco.be/en-US/product/pipes — Henco Pipes
  4. https://www.henco.be/en-US/product/fittings — Henco Fittings - water, gas, compressed air & sprinklers
  5. https://www.henco.be/en-US/product/underfloorheating-our-systems — Underfloor heating systems wet & dry construction RENO12 XPS
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 Henco Downloads 页面，技术数据表、brochures、manuals 信号明确。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: henco
brand_name: Henco
website: https://www.henco.be/
entry_url: https://www.henco.be/en/downloads
seed_urls:
- https://www.henco.be/en/downloads
- https://www.henco.be/en/home
- https://www.henco.be/en-US/product/product-catalogus
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
  country_region: Belgium
  manual_review: 需关注 Aalberts 收购后的品牌/集团归属，不影响官网爬取。
  crawl_scope_notes: 爬 products 和 downloads，重点 multilayer pipe、press fittings、underfloor
    heating、manifolds、technical data sheets、manuals。
  product_line_notes: 多层管、管件、地暖、分集水器和系统安装资料；Aalberts 旗下品牌。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 6
  evidence_keywords:
  - multilayer pipe system
  - underfloor heating
  - fittings
  - Henco Logic
  - Henco Floor
  - thermostat
  - pre-insulated pipe
  - sprinkler
  - gas pipes
  - PK/PKW Leak Before Press
  pdf_examples:
  - url: https://www.henco.be/sites/default/files/images/2023-12/HencoLogic%20handleiding%20DTHERM_1.pdf
    title: HENCO LOGIC Wired digital room thermostat
    doc_type: manual
  - url: https://www.henco.be/sites/default/files/images/2020-02/Technical_manual_ENG_2019_chapter7.pdf
    title: Henco Assembly Instructions Technical Manual chapter 7
    doc_type: manual
  - url: https://www.henco.be/sites/default/files/images/2023-12/TH_Henco_2023_EN_LR.pdf
    title: Henco Technical Manual 2023 EN
    doc_type: manual
  - url: https://www.henco.be/sites/default/files/images/2024-01/HENCO%20FLOOR_Technisch%20handboek_CMYK.pdf
    title: Henco Floor Technical Handbook
    doc_type: manual
  - url: https://www.henco.be/sites/default/files/images/2024-01/Henco_Voorgeisoleerde-Buis_EN_LR.pdf
    title: Henco Pre-insulated Pipe (EN)
    doc_type: brochure
  product_page_examples:
  - url: https://www.henco.be/en/home
    title: Henco Home - The Perfect Fit
  - url: https://www.henco.be/en-US/product/product-catalogus
    title: Henco Product Catalogue - Pipes, fittings & systems
  - url: https://www.henco.be/en-US/product/pipes
    title: Henco Pipes
  - url: https://www.henco.be/en-US/product/fittings
    title: Henco Fittings - water, gas, compressed air & sprinklers
  - url: https://www.henco.be/en-US/product/underfloorheating-our-systems
    title: Underfloor heating systems wet & dry construction RENO12 XPS
  - url: https://www.henco.be/en-US/product/henco-logic
    title: Henco Logic - smart zone control for underfloor heating
  download_center_url: https://www.henco.be/en/downloads
  search_queries_run:
  - site:henco.be filetype:pdf
  - site:henco.be english products downloads
  search_notes: PDFs hosted at /sites/default/files/images/{YYYY-MM}/. English content
    split between /en/ (downloads/home) and /en-US/ (product pages).
```
