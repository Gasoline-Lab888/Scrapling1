# 002 - ESBE

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:esbe.eu filetype:pdf`; `site:esbe.eu products english`

## 1. Brand identity

- Standard brand name: ESBE
- Official website: https://esbe.eu/group/
- English website (source doc): https://esbe.eu/group/products
- English URL confirmed in search index: https://www.esbe.eu/group/products
- Country / region: Sweden (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 区域选择可能影响可见产品，建议 YAML 使用 group/en 产品入口。
- Notes: Chrome 搜索和官网页面均显示 English products 与产品 PDF 入口。

## 2. Website entry decision

- Recommended entry_url: https://esbe.eu/group/products
- Alternative entry URLs: https://esbe.eu/group/; https://www.esbe.eu/group/products
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 混水阀、温控混合阀、旋转阀、执行器和热力控制组件，适合地暖混水与水力控制参考。
- Priority keywords (observed in Google result titles/snippets for this domain): rotary valves, mixing valves, actuators, circulation units, thermostatic mixing, linear motorized valves, filling valve, check valve, fresh hydro, hydronic
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 Products 下 thermostatic mixing valves、rotary valves、actuators、controllers、loading units；PDF 可从产品页和 media/download 链接收集。
- Manual review needed: 区域选择可能影响可见产品，建议 YAML 使用 group/en 产品入口。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.esbe.eu/group/support/esbe-catalogue-online
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.esbe.eu/storage/D091963ECA85AFB2FAE6D8F1189389DD51AED9B8B8F714273118810EDCC568DC/e4bf9ef0f7084be09d4661009f22fc16/pdf/media/3b40dae352ee42e7a031ec518378e02b/ALFxx1_en_C_LR.pdf — ALF131 ALF261 ALF361 ALF461 Linear Motorized Valves Actuator Series ALFxx1 (datasheet)
  2. https://www.esbe.eu/storage/2984E8C3EC851472A8D5B841770DD437F28E190EC4A6D8788C76FF8300488F31/d80c0aab2347435794c842456e25a4cb/pdf/media/345a4aab1f964a6b8b0292854939534a/VFA200_en_C_LR.pdf — VFA200 Filling Valve Series Complementary Products (datasheet)
  3. https://www.esbe.eu/storage/3AD3F39EBD725BAD64A2DC19EFDA33D065DBB871ABF542108C9FD95374684736/7b0601b9a0444bc6b11aff3945c644ec/pdf/media/06ed729f4b1e4ca991d765de3a0dfcb4/ARA600%203p_pl_K4_LR.pdf — ARA600 3p Extended Technical Data (datasheet)
  4. https://esbe.eu/storage/AA052E449EA83240A1D752F896683CC2D128334D7889AAE4B4B7F9302E58CBAE/0c95308f4dba4395b3c7e2b9bb05cb5f/pdf/media/3c358c7c7703442cb038ea42711d6007/ESBE%20ARA600%20Prop_VIESSMANN_en_C_LR.pdf — ESBE Rotary Actuators ARA600 Viessmann Assortment (datasheet)
  5. https://www.esbe.eu/storage/44649959C9931FCF86E6DA7CD0D5FCCA554D2221A93B85541C01EC6E6B4509B5/88865af578464ff7bb7ae1b89060d69f/pdf/media/da05b86b23804ed48358802a354777a8/DoC_CRA100_D.pdf — Declaration of Conformity CRA100 (certificate)
- Document types observed in samples: certificate, datasheet
- Notes (search agent): PDFs hosted on storage subpaths with hash IDs. Clear product taxonomy with English product pages available.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.esbe.eu/group/products — Products
  2. https://esbe.eu/group/products/circulation-units — ESBE Circulation Units
  3. https://esbe.eu/group/products/rotary-actuators — ESBE Rotary actuator
  4. https://esbe.eu/group/products/thermostatic-mixing-valves — ESBE Thermostatic mixing valves
  5. https://esbe.eu/group/products/rotary-valves — ESBE Rotary Valves
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 搜索和官网页面均显示 English products 与产品 PDF 入口。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: esbe
brand_name: ESBE
website: https://esbe.eu/group/
entry_url: https://esbe.eu/group/products
seed_urls:
- https://esbe.eu/group/products
- https://www.esbe.eu/group/support/esbe-catalogue-online
- https://www.esbe.eu/group/products
- https://esbe.eu/group/products/circulation-units
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
  country_region: Sweden
  manual_review: 区域选择可能影响可见产品，建议 YAML 使用 group/en 产品入口。
  crawl_scope_notes: 爬 Products 下 thermostatic mixing valves、rotary valves、actuators、controllers、loading
    units；PDF 可从产品页和 media/download 链接收集。
  product_line_notes: 混水阀、温控混合阀、旋转阀、执行器和热力控制组件，适合地暖混水与水力控制参考。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - rotary valves
  - mixing valves
  - actuators
  - circulation units
  - thermostatic mixing
  - linear motorized valves
  - filling valve
  - check valve
  - fresh hydro
  - hydronic
  pdf_examples:
  - url: https://www.esbe.eu/storage/D091963ECA85AFB2FAE6D8F1189389DD51AED9B8B8F714273118810EDCC568DC/e4bf9ef0f7084be09d4661009f22fc16/pdf/media/3b40dae352ee42e7a031ec518378e02b/ALFxx1_en_C_LR.pdf
    title: ALF131 ALF261 ALF361 ALF461 Linear Motorized Valves Actuator Series ALFxx1
    doc_type: datasheet
  - url: https://www.esbe.eu/storage/2984E8C3EC851472A8D5B841770DD437F28E190EC4A6D8788C76FF8300488F31/d80c0aab2347435794c842456e25a4cb/pdf/media/345a4aab1f964a6b8b0292854939534a/VFA200_en_C_LR.pdf
    title: VFA200 Filling Valve Series Complementary Products
    doc_type: datasheet
  - url: https://www.esbe.eu/storage/3AD3F39EBD725BAD64A2DC19EFDA33D065DBB871ABF542108C9FD95374684736/7b0601b9a0444bc6b11aff3945c644ec/pdf/media/06ed729f4b1e4ca991d765de3a0dfcb4/ARA600%203p_pl_K4_LR.pdf
    title: ARA600 3p Extended Technical Data
    doc_type: datasheet
  - url: https://esbe.eu/storage/AA052E449EA83240A1D752F896683CC2D128334D7889AAE4B4B7F9302E58CBAE/0c95308f4dba4395b3c7e2b9bb05cb5f/pdf/media/3c358c7c7703442cb038ea42711d6007/ESBE%20ARA600%20Prop_VIESSMANN_en_C_LR.pdf
    title: ESBE Rotary Actuators ARA600 Viessmann Assortment
    doc_type: datasheet
  - url: https://www.esbe.eu/storage/44649959C9931FCF86E6DA7CD0D5FCCA554D2221A93B85541C01EC6E6B4509B5/88865af578464ff7bb7ae1b89060d69f/pdf/media/da05b86b23804ed48358802a354777a8/DoC_CRA100_D.pdf
    title: Declaration of Conformity CRA100
    doc_type: certificate
  product_page_examples:
  - url: https://www.esbe.eu/group/products
    title: Products
  - url: https://esbe.eu/group/products/circulation-units
    title: ESBE Circulation Units
  - url: https://esbe.eu/group/products/rotary-actuators
    title: ESBE Rotary actuator
  - url: https://esbe.eu/group/products/thermostatic-mixing-valves
    title: ESBE Thermostatic mixing valves
  - url: https://esbe.eu/group/products/rotary-valves
    title: ESBE Rotary Valves
  download_center_url: https://www.esbe.eu/group/support/esbe-catalogue-online
  search_queries_run:
  - site:esbe.eu filetype:pdf
  - site:esbe.eu products english
  search_notes: PDFs hosted on storage subpaths with hash IDs. Clear product taxonomy
    with English product pages available.
```
