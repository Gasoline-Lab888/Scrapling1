# 009 - Watts

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:watts.eu filetype:pdf`; `site:watts.eu products english`

## 1. Brand identity

- Standard brand name: Watts
- Official website: https://www.watts.com/
- English website (source doc): https://www.watts.eu/en/
- English URL confirmed in search index: https://www.watts.eu/en/products/eu/antipollution-devices
- Country / region: USA / Europe (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需决定爬 watts.com 全球站还是 watts.eu 欧洲站；欧洲站更适合 EN 技术资料。
- Notes: 原 Excel Watts 行 URL 错填为 FAR；Chrome 核查应改用 watts.com / watts.eu 官方站。

## 2. Website entry decision

- Recommended entry_url: https://www.watts.eu/en/technical-support
- Alternative entry URLs: https://www.watts.com/; https://www.watts.eu/en/; https://www.watts.eu/en/products/eu/antipollution-devices
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 大型水暖/HVAC 控制阀与安全阀品牌，产品线和技术文档丰富。
- Priority keywords (observed in Google result titles/snippets for this domain): antipollution devices, pressure reducing valve, hydraulic separator, water meter, climatic control, heat pump, BT-DP, pressure gauges, gas pressure regulator, sanitary devices
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 优先 Watts Europe EN 技术支持和 HVAC/plumbing 产品；重点 balancing valves、mixing valves、backflow/safety、manifolds、radiant/controls。
- Manual review needed: 需决定爬 watts.com 全球站还是 watts.eu 欧洲站；欧洲站更适合 EN 技术资料。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.watts.eu/en/technical-support/download-catalogue
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639442-source/638417188140000000/OF110_manual.pdf — Model OF110-1 Installation Operation and Maintenance Manual (technical manual)
  2. https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639305-source/638484263910000000/manual-22c-22cx-22cx5.pdf — Series 22C 22CX 22CX5 Installation Manual (installation guide)
  3. https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639074-source/638412639980000000/10083117_HW_Q20_IM_DE_W_DE_08_19_Rev0.pdf — Hydraulic separator HW-Q20 Installation Manual (installation guide)
  4. https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/638674-source/638424942760000000/WPMM_TS_IT_W_UK_01_18_Rev2web.pdf — WPMM Series Woltman Turbine Water Meters (datasheet)
  5. https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639882-source/638574971580000000/WPAT_BR_DE_W_UK_09_19_Rev1.pdf — Connecting Heat Pumps with Watts Connection Technology (brochure)
- Document types observed in samples: brochure, datasheet, installation guide, technical manual
- Notes (search agent): PDFs hosted at watts.eu/dfsmedia/ path (DAM system). Strong English product catalog under /en/products/eu/.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.watts.eu/en/products/eu/antipollution-devices — Antipollution devices | Watts Europe
  2. https://www.watts.eu/en/products/eu/sanitary-devices-systems/pressure-reducing-valves/pressure-reducing-valve-drv — Diaphragm pressure reducing valve DRV
  3. https://www.watts.eu/en/products/eu/sanitary-devices-systems/automatic-control-devices — Automatic Control Devices | Watts Europe
  4. https://www.watts.eu/en/products/eu/Smart-Home-and-Controls/Weather-dependent-and-remote-heating-control/controller-climatic-control-for-heating-and-cooling-systems-new — Controller CLIMATIC CONTROL for heating and cooling systems
  5. https://www.watts.eu/en/products/eu/Components-for-oil-and-gas-systems/Gas-pressure-regulators — Gas pressure regulators
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "原 Excel Watts 行 URL 错填为 FAR；Chrome 核查应改用 watts.com / watts.eu 官方站。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: watts
brand_name: Watts
website: https://www.watts.com/
entry_url: https://www.watts.eu/en/technical-support
seed_urls:
- https://www.watts.eu/en/technical-support
- https://www.watts.eu/en/technical-support/download-catalogue
- https://www.watts.eu/en/products/eu/antipollution-devices
- https://www.watts.eu/en/products/eu/sanitary-devices-systems/pressure-reducing-valves/pressure-reducing-valve-drv
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
  suggested_category: C-商用 HVAC/水力平衡/控制阀
  suggested_priority: P0
  country_region: USA / Europe
  manual_review: 需决定爬 watts.com 全球站还是 watts.eu 欧洲站；欧洲站更适合 EN 技术资料。
  crawl_scope_notes: 优先 Watts Europe EN 技术支持和 HVAC/plumbing 产品；重点 balancing valves、mixing
    valves、backflow/safety、manifolds、radiant/controls。
  product_line_notes: 大型水暖/HVAC 控制阀与安全阀品牌，产品线和技术文档丰富。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - antipollution devices
  - pressure reducing valve
  - hydraulic separator
  - water meter
  - climatic control
  - heat pump
  - BT-DP
  - pressure gauges
  - gas pressure regulator
  - sanitary devices
  pdf_examples:
  - url: https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639442-source/638417188140000000/OF110_manual.pdf
    title: Model OF110-1 Installation Operation and Maintenance Manual
    doc_type: manual
  - url: https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639305-source/638484263910000000/manual-22c-22cx-22cx5.pdf
    title: Series 22C 22CX 22CX5 Installation Manual
    doc_type: installation_guide
  - url: https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639074-source/638412639980000000/10083117_HW_Q20_IM_DE_W_DE_08_19_Rev0.pdf
    title: Hydraulic separator HW-Q20 Installation Manual
    doc_type: installation_guide
  - url: https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/638674-source/638424942760000000/WPMM_TS_IT_W_UK_01_18_Rev2web.pdf
    title: WPMM Series Woltman Turbine Water Meters
    doc_type: datasheet
  - url: https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639882-source/638574971580000000/WPAT_BR_DE_W_UK_09_19_Rev1.pdf
    title: Connecting Heat Pumps with Watts Connection Technology
    doc_type: brochure
  product_page_examples:
  - url: https://www.watts.eu/en/products/eu/antipollution-devices
    title: Antipollution devices | Watts Europe
  - url: https://www.watts.eu/en/products/eu/sanitary-devices-systems/pressure-reducing-valves/pressure-reducing-valve-drv
    title: Diaphragm pressure reducing valve DRV
  - url: https://www.watts.eu/en/products/eu/sanitary-devices-systems/automatic-control-devices
    title: Automatic Control Devices | Watts Europe
  - url: https://www.watts.eu/en/products/eu/Smart-Home-and-Controls/Weather-dependent-and-remote-heating-control/controller-climatic-control-for-heating-and-cooling-systems-new
    title: Controller CLIMATIC CONTROL for heating and cooling systems
  - url: https://www.watts.eu/en/products/eu/Components-for-oil-and-gas-systems/Gas-pressure-regulators
    title: Gas pressure regulators
  download_center_url: https://www.watts.eu/en/technical-support/download-catalogue
  search_queries_run:
  - site:watts.eu filetype:pdf
  - site:watts.eu products english
  search_notes: PDFs hosted at watts.eu/dfsmedia/ path (DAM system). Strong English
    product catalog under /en/products/eu/.
```
