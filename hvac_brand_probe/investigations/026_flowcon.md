# 026 - FlowCon

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:flowcon.com filetype:pdf`; `site:flowcon.com products`

## 1. Brand identity

- Standard brand name: FlowCon
- Official website: https://flowcon.com/
- English website (source doc): https://flowcon.com/
- English URL confirmed in search index: https://flowcon.com/product-groups
- Country / region: Denmark (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: FlowCon 原 Excel URL 为空，已通过 Chrome 搜索补全。
- Notes: Chrome 重试确认 Product Literature 页面，PDF/下载链接丰富。

## 2. Website entry decision

- Recommended entry_url: https://flowcon.com/view-and-download/product-literature
- Alternative entry URLs: https://flowcon.com/; https://flowcon.com/product-groups
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 压差无关控制阀和动态水力平衡阀专业品牌，商用 HVAC 控制阀参考价值高。
- Priority keywords (observed in Google result titles/snippets for this domain): PICV, pressure independent control valve, dynamic balancing valves, valve authority, automatic balancing valves, ABV, PITCV, CRAC units, calorifiers, actuators
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 Product Literature 和 product pages，重点 PICV、dynamic balancing valves、actuators、cartridges、commissioning documents。
- Manual review needed: FlowCon 原 Excel URL 为空，已通过 Chrome 搜索补全。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://flowcon.com/view-and-download/product-literature/
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://flowcon.com/fileadmin/user_upload/Pdf/Articles/FlowCon-Topic-Letter-Valve-Authority.pdf — FlowCon Topic Letter - Valve Authority (other)
  2. https://flowcon.com/fileadmin/user_upload/Pdf/Applications/FlowCon-Application-Calorifiers-ABV.pdf — FlowCon Application Calorifiers ABV (technical manual)
  3. https://flowcon.com/fileadmin/user_upload/Pdf/Assembly_Drawings/FlowCon-Green-Assembly.pdf — FlowCon Green Assembly Drawing (datasheet)
  4. https://flowcon.com/fileadmin/user_upload/Pdf/Applications/FlowCon-Application-CRAC-Units-PITCV.pdf — FlowCon Application CRAC Units PITCV (technical manual)
  5. https://flowcon.com/fileadmin/user_upload/Pdf/Certificates_Stainless_Steel/PED/FlowCon-Unimizer-SSL-PED-Declaration-of-Conformity.pdf — FlowCon Unimizer SSL PED Declaration of Conformity (certificate)
- Document types observed in samples: certificate, datasheet, technical manual, other
- Notes (search agent): PDFs hosted at /fileadmin/user_upload/Pdf/ with category subfolders (Applications, Certificates, Assembly_Drawings). Product groups page is the main catalogue.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://flowcon.com/product-groups — FlowCon Product Range
  2. https://flowcon.com/product-groups/flowcon-sm-stainless-steel — FlowCon SM in Stainless Steel - PICV PN40
  3. https://flowcon.com/product-groups/flowcon-fn-actuators — FlowCon FN Actuator - electrical actuator
  4. https://flowcon.com/product-groups/flowcon-e-just — FlowCon E-JUST - adjustable dynamic balancing valves
  5. https://flowcon.com/product-groups/flowcon-pure — FlowCon Pure - pre-set dynamic balancing valves
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 重试确认 Product Literature 页面，PDF/下载链接丰富。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: flowcon
brand_name: FlowCon
website: https://flowcon.com/
entry_url: https://flowcon.com/view-and-download/product-literature
seed_urls:
- https://flowcon.com/view-and-download/product-literature
- https://flowcon.com/view-and-download/product-literature/
- https://flowcon.com/product-groups
- https://flowcon.com/product-groups/flowcon-sm-stainless-steel
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
  suggested_category: C-商用 HVAC/水力平衡/控制阀
  suggested_priority: P0
  country_region: Denmark
  manual_review: FlowCon 原 Excel URL 为空，已通过 Chrome 搜索补全。
  crawl_scope_notes: 爬 Product Literature 和 product pages，重点 PICV、dynamic balancing
    valves、actuators、cartridges、commissioning documents。
  product_line_notes: 压差无关控制阀和动态水力平衡阀专业品牌，商用 HVAC 控制阀参考价值高。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - PICV
  - pressure independent control valve
  - dynamic balancing valves
  - valve authority
  - automatic balancing valves
  - ABV
  - PITCV
  - CRAC units
  - calorifiers
  - actuators
  pdf_examples:
  - url: https://flowcon.com/fileadmin/user_upload/Pdf/Articles/FlowCon-Topic-Letter-Valve-Authority.pdf
    title: FlowCon Topic Letter - Valve Authority
    doc_type: other
  - url: https://flowcon.com/fileadmin/user_upload/Pdf/Applications/FlowCon-Application-Calorifiers-ABV.pdf
    title: FlowCon Application Calorifiers ABV
    doc_type: manual
  - url: https://flowcon.com/fileadmin/user_upload/Pdf/Assembly_Drawings/FlowCon-Green-Assembly.pdf
    title: FlowCon Green Assembly Drawing
    doc_type: datasheet
  - url: https://flowcon.com/fileadmin/user_upload/Pdf/Applications/FlowCon-Application-CRAC-Units-PITCV.pdf
    title: FlowCon Application CRAC Units PITCV
    doc_type: manual
  - url: https://flowcon.com/fileadmin/user_upload/Pdf/Certificates_Stainless_Steel/PED/FlowCon-Unimizer-SSL-PED-Declaration-of-Conformity.pdf
    title: FlowCon Unimizer SSL PED Declaration of Conformity
    doc_type: certificate
  product_page_examples:
  - url: https://flowcon.com/product-groups
    title: FlowCon Product Range
  - url: https://flowcon.com/product-groups/flowcon-sm-stainless-steel
    title: FlowCon SM in Stainless Steel - PICV PN40
  - url: https://flowcon.com/product-groups/flowcon-fn-actuators
    title: FlowCon FN Actuator - electrical actuator
  - url: https://flowcon.com/product-groups/flowcon-e-just
    title: FlowCon E-JUST - adjustable dynamic balancing valves
  - url: https://flowcon.com/product-groups/flowcon-pure
    title: FlowCon Pure - pre-set dynamic balancing valves
  download_center_url: https://flowcon.com/view-and-download/product-literature/
  search_queries_run:
  - site:flowcon.com filetype:pdf
  - site:flowcon.com products
  search_notes: PDFs hosted at /fileadmin/user_upload/Pdf/ with category subfolders
    (Applications, Certificates, Assembly_Drawings). Product groups page is the main
    catalogue.
```
