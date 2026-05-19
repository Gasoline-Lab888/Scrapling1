# 027 - Jomar Hydronics / Jomar Valve

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:jomarvalve.com filetype:pdf`; `site:jomarvalve.com products`

## 1. Brand identity

- Standard brand name: Jomar Hydronics / Jomar Valve
- Official website: https://www.jomarvalve.com/
- English website (source doc): https://www.jomarvalve.com/
- English URL confirmed in search index: https://www.jomarvalve.com/products/
- Country / region: USA (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需决定 jomarvalve.com 与 jomarhydronics.com 是否分别生成 YAML 或合并为一个品牌。
- Notes: Chrome 确认 Download Library 含多个 PDF；搜索结果也确认 jomarhydronics.com 产品页。

## 2. Website entry decision

- Recommended entry_url: https://www.jomarvalve.com/download-library/
- Alternative entry URLs: https://www.jomarvalve.com/; https://www.jomarvalve.com/products/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 阀门与 hydronics 产品，含 Jomar Hydronics 平衡阀/水力产品线。
- Priority keywords (observed in Google result titles/snippets for this domain): ball valves, lead free brass, filter ball, stainless steel ball valve, thread sealant, lockwings, basket strainers, actuator accessories, commercial catalog
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 Jomar Valve Download Library 与 Jomar Hydronics products，重点 balancing valves、ball valves、hydronic components、technical submittals。
- Manual review needed: 需决定 jomarvalve.com 与 jomarhydronics.com 是否分别生成 YAML 或合并为一个品牌。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.jomarvalve.com/download-library/
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.jomarvalve.com/docs/LIT-SF-FB.pdf — Lead Free Filter Ball LIT-SF-FB (2024) (brochure)
  2. https://www.jomarvalve.com/specsheets/F-351.pdf — F-351 Spec Sheet (datasheet)
  3. https://www.jomarvalve.com/docs/lit-jv-pc.pdf — Product Catalog (catalogue)
  4. https://www.jomarvalve.com/specsheets/T-150G.pdf — T-150G Lead Free Brass Ball Valves 2-Piece Full Port (datasheet)
  5. https://www.jomarvalve.com/docs/lit-jv-com.pdf — Commercial Catalog (catalogue)
- Document types observed in samples: brochure, catalogue, datasheet
- Notes (search agent): PDFs split between /docs/ (literature/catalogs) and /specsheets/ (individual product spec sheets). US-focused, no PICV/HVAC balancing line visible.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.jomarvalve.com/products/ — Products
  2. https://www.jomarvalve.com/products/ball-valves/lead-free-brass/t-413g/ — T-413G Ball Valve
  3. https://www.jomarvalve.com/products/basket-strainers/designer-series/twist-loc-ds/ — Twist-N-Loc Basket Strainer
  4. https://www.jomarvalve.com/products/lockwings/175-lwibp/ — 175-LWIBP Lockwing
  5. https://www.jomarvalve.com/products/cpvcpvc/s-701/ — S-701 CPVC/PVC Valve
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 Download Library 含多个 PDF；搜索结果也确认 jomarhydronics.com 产品页。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: jomar
brand_name: Jomar Hydronics / Jomar Valve
website: https://www.jomarvalve.com/
entry_url: https://www.jomarvalve.com/download-library/
seed_urls:
- https://www.jomarvalve.com/download-library/
- https://www.jomarvalve.com/products/
- https://www.jomarvalve.com/products/ball-valves/lead-free-brass/t-413g/
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
  country_region: USA
  manual_review: 需决定 jomarvalve.com 与 jomarhydronics.com 是否分别生成 YAML 或合并为一个品牌。
  crawl_scope_notes: 爬 Jomar Valve Download Library 与 Jomar Hydronics products，重点
    balancing valves、ball valves、hydronic components、technical submittals。
  product_line_notes: 阀门与 hydronics 产品，含 Jomar Hydronics 平衡阀/水力产品线。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - ball valves
  - lead free brass
  - filter ball
  - stainless steel ball valve
  - thread sealant
  - lockwings
  - basket strainers
  - actuator accessories
  - commercial catalog
  pdf_examples:
  - url: https://www.jomarvalve.com/docs/LIT-SF-FB.pdf
    title: Lead Free Filter Ball LIT-SF-FB (2024)
    doc_type: brochure
  - url: https://www.jomarvalve.com/specsheets/F-351.pdf
    title: F-351 Spec Sheet
    doc_type: datasheet
  - url: https://www.jomarvalve.com/docs/lit-jv-pc.pdf
    title: Product Catalog
    doc_type: catalogue
  - url: https://www.jomarvalve.com/specsheets/T-150G.pdf
    title: T-150G Lead Free Brass Ball Valves 2-Piece Full Port
    doc_type: datasheet
  - url: https://www.jomarvalve.com/docs/lit-jv-com.pdf
    title: Commercial Catalog
    doc_type: catalogue
  product_page_examples:
  - url: https://www.jomarvalve.com/products/
    title: Products
  - url: https://www.jomarvalve.com/products/ball-valves/lead-free-brass/t-413g/
    title: T-413G Ball Valve
  - url: https://www.jomarvalve.com/products/basket-strainers/designer-series/twist-loc-ds/
    title: Twist-N-Loc Basket Strainer
  - url: https://www.jomarvalve.com/products/lockwings/175-lwibp/
    title: 175-LWIBP Lockwing
  - url: https://www.jomarvalve.com/products/cpvcpvc/s-701/
    title: S-701 CPVC/PVC Valve
  download_center_url: https://www.jomarvalve.com/download-library/
  search_queries_run:
  - site:jomarvalve.com filetype:pdf
  - site:jomarvalve.com products
  search_notes: PDFs split between /docs/ (literature/catalogs) and /specsheets/ (individual
    product spec sheets). US-focused, no PICV/HVAC balancing line visible.
```
