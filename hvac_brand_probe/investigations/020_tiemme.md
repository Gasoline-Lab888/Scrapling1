# 020 - Tiemme

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:tiemme.com filetype:pdf`; `site:tiemme.com english products`

## 1. Brand identity

- Standard brand name: Tiemme
- Official website: https://www.tiemme.com/
- English website (source doc): https://www.tiemme.com/
- English URL confirmed in search index: https://www.tiemme.com/eng/index.php
- Country / region: Italy (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需人工确认稳定英文入口，可能是移动英文站或语言切换后的路径。
- Notes: Chrome 打开主站标题为意大利语；Google 结果显示 m.tiemme.com/eng 英文产品页和 PDF/目录信号。

## 2. Website entry decision

- Recommended entry_url: https://www.tiemme.com/
- Alternative entry URLs: https://www.tiemme.com/eng/index.php
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 管件、阀门、分集水器、采暖系统和多层管系统。
- Priority keywords (observed in Google result titles/snippets for this domain): manifolds, heat pumps, central heating, metering, ball valves, press fittings, thermostatic, radiant systems, motorized ball valves
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬产品目录中 manifolds、valves、fittings、PEX/multilayer、heating components；Chrome 搜索可补 m.tiemme.com/eng 产品页。
- Manual review needed: 需人工确认稳定英文入口，可能是移动英文站或语言切换后的路径。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.tiemme.com/eng/index.php
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://m.tiemme.com/eng/brochure_ceiling_home_smart_26_ceiling_home_plus_brochure_d2604.pdf — Ceiling Home Smart & Ceiling Home Plus (brochure)
  2. https://m.tiemme.com/eng/brochure_components_for_heat_pumps_brochure_d2443.pdf — Components for Heat Pumps (brochure)
  3. https://m.tiemme.com/eng/central_heating_and_metering_systems_h2_b20_0_catalogo_d2198.pdf — Central Heating and Metering Systems (catalogue)
  4. https://m.tiemme.com/eng/brochure_tiemme_next_brochure_d1823.pdf — Home Comfort Management System (Tiemme Next) (brochure)
  5. https://m.tiemme.com/eng/brochure_tiemme_gate_brochure_d2321.pdf — Temperature Control System & Wi-Fi (Tiemme Gate) (brochure)
- Document types observed in samples: brochure, catalogue
- Notes (search agent): English content split between www.tiemme.com/eng (product list pages) and m.tiemme.com/eng (PDF brochures/catalogues).

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://m.tiemme.com/eng/manifolds_and_equipment_prodotti-list2_32296.php?site=master — Manifolds and Equipment
  2. https://www.tiemme.com/eng/ball_valves_for_water_prodotti-list_25175.php — Ball Valves MISTRAL for water
  3. https://www.tiemme.com/eng/valves_with_thermostatic_option_prodotti-list_33472.php — Valves with Thermostatic option
  4. https://m.tiemme.com/eng/press_fittings_prodotti-list2_123174.php?site=master — Press fittings
  5. https://www.tiemme.com/eng/prodotti-list_26127_p2_r5.php — Motorized ball valves
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 打开主站标题为意大利语；Google 结果显示 m.tiemme.com/eng 英文产品页和 PDF/目录信号。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: tiemme
brand_name: Tiemme
website: https://www.tiemme.com/
entry_url: https://www.tiemme.com/
seed_urls:
- https://www.tiemme.com/
- https://www.tiemme.com/eng/index.php
- https://m.tiemme.com/eng/manifolds_and_equipment_prodotti-list2_32296.php?site=master
- https://www.tiemme.com/eng/ball_valves_for_water_prodotti-list_25175.php
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
  country_region: Italy
  manual_review: 需人工确认稳定英文入口，可能是移动英文站或语言切换后的路径。
  crawl_scope_notes: 爬产品目录中 manifolds、valves、fittings、PEX/multilayer、heating components；Chrome
    搜索可补 m.tiemme.com/eng 产品页。
  product_line_notes: 管件、阀门、分集水器、采暖系统和多层管系统。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - manifolds
  - heat pumps
  - central heating
  - metering
  - ball valves
  - press fittings
  - thermostatic
  - radiant systems
  - motorized ball valves
  pdf_examples:
  - url: https://m.tiemme.com/eng/brochure_ceiling_home_smart_26_ceiling_home_plus_brochure_d2604.pdf
    title: Ceiling Home Smart & Ceiling Home Plus
    doc_type: brochure
  - url: https://m.tiemme.com/eng/brochure_components_for_heat_pumps_brochure_d2443.pdf
    title: Components for Heat Pumps
    doc_type: brochure
  - url: https://m.tiemme.com/eng/central_heating_and_metering_systems_h2_b20_0_catalogo_d2198.pdf
    title: Central Heating and Metering Systems
    doc_type: catalogue
  - url: https://m.tiemme.com/eng/brochure_tiemme_next_brochure_d1823.pdf
    title: Home Comfort Management System (Tiemme Next)
    doc_type: brochure
  - url: https://m.tiemme.com/eng/brochure_tiemme_gate_brochure_d2321.pdf
    title: Temperature Control System & Wi-Fi (Tiemme Gate)
    doc_type: brochure
  product_page_examples:
  - url: https://m.tiemme.com/eng/manifolds_and_equipment_prodotti-list2_32296.php?site=master
    title: Manifolds and Equipment
  - url: https://www.tiemme.com/eng/ball_valves_for_water_prodotti-list_25175.php
    title: Ball Valves MISTRAL for water
  - url: https://www.tiemme.com/eng/valves_with_thermostatic_option_prodotti-list_33472.php
    title: Valves with Thermostatic option
  - url: https://m.tiemme.com/eng/press_fittings_prodotti-list2_123174.php?site=master
    title: Press fittings
  - url: https://www.tiemme.com/eng/prodotti-list_26127_p2_r5.php
    title: Motorized ball valves
  download_center_url: https://www.tiemme.com/eng/index.php
  search_queries_run:
  - site:tiemme.com filetype:pdf
  - site:tiemme.com english products
  search_notes: English content split between www.tiemme.com/eng (product list pages)
    and m.tiemme.com/eng (PDF brochures/catalogues).
```
