# 022 - Cimberio

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:cimberio.com filetype:pdf`; `site:cimberio.com english products`; `site:cimberio.com catalogs balancing valves`

## 1. Brand identity

- Standard brand name: Cimberio
- Official website: https://www.cimberio.com/
- English website (source doc): https://www.cimberio.com/en/
- English URL confirmed in search index: https://www.cimberio.com/en/products/
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需确认官网 PDF 链接是否可从站内导航发现。
- Notes: Chrome 确认 cimberio.com/en 官方英文站；搜索结果显示产品指南 PDF 但可能在 CDN 或第三方。

## 2. Website entry decision

- Recommended entry_url: https://www.cimberio.com/en/
- Alternative entry URLs: https://www.cimberio.com/; https://www.cimberio.com/en/products/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 阀门制造品牌，覆盖黄铜阀、平衡阀、控制阀及工业/建筑阀门。
- Priority keywords (observed in Google result titles/snippets for this domain): balancing valves, thermostatic balancing valve, TBV, CIM778, hydraulic systems, thermohydraulic, PN16, PN25, valves and components
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬英文 products/catalogue，重点 valves、balancing valves、actuated/control valves、brass/industrial valves。
- Manual review needed: 需确认官网 PDF 链接是否可从站内导航发现。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.cimberio.com/en/catalogs/
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://web.cimberio.com/index.php/figura/pdf/578?_lang=en — Cimberio Technical PDF Figure 578 (PN rated) (datasheet)
  2. https://www.cimberio.com/wp-content/uploads/2024/11/FM-01820-en.pdf — Certificate of Registration QMS ISO 9001:2015 (certificate)
  3. https://web.cimberio.com/index.php/figura/pdf/526?_lang=en — Cimberio Technical PDF Figure 526 (PN16) (datasheet)
  4. https://web.cimberio.com/index.php/figura/pdf/693?_lang=en — Cimberio Technical PDF Figure 693 (PN16) (datasheet)
  5. https://web.cimberio.com/index.php/figura/pdf/72?_lang=en — Cimberio Technical PDF Figure 72 (datasheet)
- Document types observed in samples: certificate, datasheet
- Notes (search agent): Technical PDFs are served dynamically through web.cimberio.com/index.php/figura/pdf/{ID}?_lang=en. Catalogs hub at /en/catalogs/.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.cimberio.com/en/products/ — Plumbing and Heating Components - Cimberio Products
  2. https://www.cimberio.com/en/catalogs/ — Catalogs - Cimberio
  3. https://www.cimberio.com/en/ — Cimberio Manufacturing innovative and reliable valves
  4. https://www.cimberio.com/eng/leggi_news.asp?id=239 — Cimberio Balancing Valves: solution for more comfortable environments
  5. https://www.cimberio.com/en/company/ — Manufacturers of valves and components for hydraulic systems
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 cimberio.com/en 官方英文站；搜索结果显示产品指南 PDF 但可能在 CDN 或第三方。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: cimberio
brand_name: Cimberio
website: https://www.cimberio.com/
entry_url: https://www.cimberio.com/en/
seed_urls:
- https://www.cimberio.com/en/
- https://www.cimberio.com/en/catalogs/
- https://www.cimberio.com/en/products/
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
  country_region: Italy
  manual_review: 需确认官网 PDF 链接是否可从站内导航发现。
  crawl_scope_notes: 爬英文 products/catalogue，重点 valves、balancing valves、actuated/control
    valves、brass/industrial valves。
  product_line_notes: 阀门制造品牌，覆盖黄铜阀、平衡阀、控制阀及工业/建筑阀门。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - balancing valves
  - thermostatic balancing valve
  - TBV
  - CIM778
  - hydraulic systems
  - thermohydraulic
  - PN16
  - PN25
  - valves and components
  pdf_examples:
  - url: https://web.cimberio.com/index.php/figura/pdf/578?_lang=en
    title: Cimberio Technical PDF Figure 578 (PN rated)
    doc_type: datasheet
  - url: https://www.cimberio.com/wp-content/uploads/2024/11/FM-01820-en.pdf
    title: Certificate of Registration QMS ISO 9001:2015
    doc_type: certificate
  - url: https://web.cimberio.com/index.php/figura/pdf/526?_lang=en
    title: Cimberio Technical PDF Figure 526 (PN16)
    doc_type: datasheet
  - url: https://web.cimberio.com/index.php/figura/pdf/693?_lang=en
    title: Cimberio Technical PDF Figure 693 (PN16)
    doc_type: datasheet
  - url: https://web.cimberio.com/index.php/figura/pdf/72?_lang=en
    title: Cimberio Technical PDF Figure 72
    doc_type: datasheet
  product_page_examples:
  - url: https://www.cimberio.com/en/products/
    title: Plumbing and Heating Components - Cimberio Products
  - url: https://www.cimberio.com/en/catalogs/
    title: Catalogs - Cimberio
  - url: https://www.cimberio.com/en/
    title: Cimberio Manufacturing innovative and reliable valves
  - url: https://www.cimberio.com/eng/leggi_news.asp?id=239
    title: 'Cimberio Balancing Valves: solution for more comfortable environments'
  - url: https://www.cimberio.com/en/company/
    title: Manufacturers of valves and components for hydraulic systems
  download_center_url: https://www.cimberio.com/en/catalogs/
  search_queries_run:
  - site:cimberio.com filetype:pdf
  - site:cimberio.com english products
  - site:cimberio.com catalogs balancing valves
  search_notes: Technical PDFs are served dynamically through web.cimberio.com/index.php/figura/pdf/{ID}?_lang=en.
    Catalogs hub at /en/catalogs/.
```
