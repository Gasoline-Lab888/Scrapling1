# 003 - HERZ Armaturen

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:herz.eu filetype:pdf`; `site:herz.eu products english`; `site:herz.eu products valves armaturen`

## 1. Brand identity

- Standard brand name: HERZ Armaturen
- Official website: https://www.herz.eu/
- English website (source doc): https://www.herz.eu/index_eng.html
- English URL confirmed in search index: same as source-doc URL
- Country / region: Austria (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: HERZ 存在国家站/媒体服务器，需确认主爬使用 herz.eu 而不是区域经销商 PDF。
- Notes: Chrome 搜索结果显示 herz.eu 英文站和多个 HERZ catalogue PDF。

## 2. Website entry decision

- Recommended entry_url: https://www.herz.eu/index_eng.html
- Alternative entry URLs: https://www.herz.eu/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 阀门、恒温控制、水力平衡、分集水器与采暖控制，产品面广且技术 PDF 价值高。
- Priority keywords (observed in Google result titles/snippets for this domain): pressure independent control valves, balancing valves, actuators, mixing valves, thermostatic valve, ball valves, SMARTCONTROL, valves, PICV
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 从 English 首页进入 Products/Catalogues，重点 radiator valves、thermostatic valves、balancing valves、manifolds、floor heating 相关资料。
- Manual review needed: HERZ 存在国家站/媒体服务器，需确认主爬使用 herz.eu 而不是区域经销商 PDF。

## 4. Downloads / PDF evidence

- Has download center: no obvious dedicated hub in this run's search
- Download center URL: (none observed)
- PDF links found via Google site:search: 3 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://herzmediaserver.com/data/01_product_data/06_broschure/eng/4002-4006_eng.pdf — HERZ Pressure Independent Control Valves (brochure)
  2. https://herzmediaserver.com/data/01_product_data/06_broschure/eng/4218_balancing_valve_cast_iron-eng.pdf — HERZ Balancing Valves Cast Iron (brochure)
  3. https://herzmediaserver.com/data/01_product_data/06_broschure/eng/kugelhahne_en.pdf — HERZ Ball Valves (brochure)
  4. (no further sample from Google site:search)
  5. (no further sample from Google site:search)
- Document types observed in samples: brochure
- Notes (search agent): PDFs hosted on separate subdomain herzmediaserver.com, not herz.eu itself. Main herz.eu site is minimal English landing page.

## 5. Product page evidence

- Product pages found via Google site:search: 1 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.herz.eu/index_eng.html — HERZ Armaturen English
  2. (no further sample from Google site:search)
  3. (no further sample from Google site:search)
  4. (no further sample from Google site:search)
  5. (no further sample from Google site:search)
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 搜索结果显示 herz.eu 英文站和多个 HERZ catalogue PDF。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: herz_armaturen
brand_name: HERZ Armaturen
website: https://www.herz.eu/
entry_url: https://www.herz.eu/index_eng.html
seed_urls:
- https://www.herz.eu/index_eng.html
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
  suggested_category: A-核心暖通水力控制/地暖阀门
  suggested_priority: P0
  country_region: Austria
  manual_review: HERZ 存在国家站/媒体服务器，需确认主爬使用 herz.eu 而不是区域经销商 PDF。
  crawl_scope_notes: 从 English 首页进入 Products/Catalogues，重点 radiator valves、thermostatic
    valves、balancing valves、manifolds、floor heating 相关资料。
  product_line_notes: 阀门、恒温控制、水力平衡、分集水器与采暖控制，产品面广且技术 PDF 价值高。
  blocked_reason_hint: ''
  pdf_sample_count: 3
  product_page_sample_count: 1
  evidence_keywords:
  - pressure independent control valves
  - balancing valves
  - actuators
  - mixing valves
  - thermostatic valve
  - ball valves
  - SMARTCONTROL
  - valves
  - PICV
  pdf_examples:
  - url: https://herzmediaserver.com/data/01_product_data/06_broschure/eng/4002-4006_eng.pdf
    title: HERZ Pressure Independent Control Valves
    doc_type: brochure
  - url: https://herzmediaserver.com/data/01_product_data/06_broschure/eng/4218_balancing_valve_cast_iron-eng.pdf
    title: HERZ Balancing Valves Cast Iron
    doc_type: brochure
  - url: https://herzmediaserver.com/data/01_product_data/06_broschure/eng/kugelhahne_en.pdf
    title: HERZ Ball Valves
    doc_type: brochure
  product_page_examples:
  - url: https://www.herz.eu/index_eng.html
    title: HERZ Armaturen English
  download_center_url: ''
  search_queries_run:
  - site:herz.eu filetype:pdf
  - site:herz.eu products english
  - site:herz.eu products valves armaturen
  search_notes: PDFs hosted on separate subdomain herzmediaserver.com, not herz.eu
    itself. Main herz.eu site is minimal English landing page.
```
