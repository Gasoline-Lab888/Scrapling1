# 007 - Uponor

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:uponor.com filetype:pdf`; `site:uponor.com products download centre`

## 1. Brand identity

- Standard brand name: Uponor
- Official website: https://www.uponor.com/
- English website (source doc): https://www.uponor.com/en-en
- English URL confirmed in search index: https://www.uponor.com/en-en/download-centre
- Country / region: Finland (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: Uponor 有多区域站，建议优先 en-en 或目标市场 EN 页面。
- Notes: Chrome 确认 en-en download-centre 页面含 PDF 和下载筛选。

## 2. Website entry decision

- Recommended entry_url: https://www.uponor.com/en-en/download-centre
- Alternative entry URLs: https://www.uponor.com/; https://www.uponor.com/en-en
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en-en` (derived from entry URL locale segment)
- Suggested path_prefix: /en-en

## 3. Product scope

- Priority product lines: 地暖/辐射供冷供热、PEX/多层管、分集水器和控制系统，是系统型品牌标杆。
- Priority keywords (observed in Google result titles/snippets for this domain): PEX, piping systems, S-Press, Tecto, Smatrix, Ecoflex, ChlorFIT, thermostat, installation manual, product brochure
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 Products 和 Download centre，重点 underfloor heating/cooling、PEX/MLCP pipes、manifolds、controls、installation manuals。
- Manual review needed: Uponor 有多区域站，建议优先 en-en 或目标市场 EN 页面。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.uponor.com/en-en/download-centre
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.uponor.com/getmedia/cf49967c-55ec-4787-b050-ffb197ab1431/ChlorFIT-Manual-0925.pdf?sitename=USA — Uponor ChlorFIT Schedule 80 Corzan CPVC Piping Systems (technical manual)
  2. https://brandportal.uponor.com/m/10c6b001fb2a8ca0/original/IM-Tecto-INT-1187744-v2.pdf — Uponor Tecto Installation Manual (installation guide)
  3. https://www.uponor.com/getmedia/14f105c8-7016-4204-a9a7-7139ca5af1ec/Uponor-Tignum-17-technical-information-INT-1118597-202006.pdf?sitename=UponorInternational — Uponor Tignum 17 Technical Information (datasheet)
  4. https://brandportal.uponor.com/m/598d0e5afb0b305/original/TI-Ecoflex-pipe-systems-UK-1142161.pdf — Ecoflex Solutions Technical Information UK (datasheet)
  5. https://brandportal.uponor.com/m/40b38e79540d873b/original/PB_S_Press_Plus_EN_09-2025_1094180.pdf — Uponor S-Press PLUS Product Brochure (brochure)
- Document types observed in samples: brochure, datasheet, installation guide, technical manual
- Notes (search agent): PDFs split between www.uponor.com/getmedia and brandportal.uponor.com subdomain. Strong en-en locale coverage with formal Download Centre.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.uponor.com/en-en/download-centre — Download centre | Uponor
  2. https://www.uponor.com/en-en/services/services-for-designers — Services for designers, specifiers and planners | Uponor
  3. https://www.uponor.com/en-en/products/room-temperature-controls/uponor-smatrix-app-and-software/downloads — Uponor Smatrix App - downloads
  4. https://www.uponor.com/en-us/customer-support/order-catalog — Product catalog | Uponor
  5. https://www.uponor.com/en-en/solutions/uponor-infra-solutions/tanks — Polyethylene tanks | Uponor
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 en-en download-centre 页面含 PDF 和下载筛选。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: uponor
brand_name: Uponor
website: https://www.uponor.com/
entry_url: https://www.uponor.com/en-en/download-centre
seed_urls:
- https://www.uponor.com/en-en/download-centre
- https://www.uponor.com/en-en/services/services-for-designers
max_pages: 250
url_scope:
  path_prefix: /en-en
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
  country_region: Finland
  manual_review: Uponor 有多区域站，建议优先 en-en 或目标市场 EN 页面。
  crawl_scope_notes: 爬 Products 和 Download centre，重点 underfloor heating/cooling、PEX/MLCP
    pipes、manifolds、controls、installation manuals。
  product_line_notes: 地暖/辐射供冷供热、PEX/多层管、分集水器和控制系统，是系统型品牌标杆。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - PEX
  - piping systems
  - S-Press
  - Tecto
  - Smatrix
  - Ecoflex
  - ChlorFIT
  - thermostat
  - installation manual
  - product brochure
  pdf_examples:
  - url: https://www.uponor.com/getmedia/cf49967c-55ec-4787-b050-ffb197ab1431/ChlorFIT-Manual-0925.pdf?sitename=USA
    title: Uponor ChlorFIT Schedule 80 Corzan CPVC Piping Systems
    doc_type: manual
  - url: https://brandportal.uponor.com/m/10c6b001fb2a8ca0/original/IM-Tecto-INT-1187744-v2.pdf
    title: Uponor Tecto Installation Manual
    doc_type: installation_guide
  - url: https://www.uponor.com/getmedia/14f105c8-7016-4204-a9a7-7139ca5af1ec/Uponor-Tignum-17-technical-information-INT-1118597-202006.pdf?sitename=UponorInternational
    title: Uponor Tignum 17 Technical Information
    doc_type: datasheet
  - url: https://brandportal.uponor.com/m/598d0e5afb0b305/original/TI-Ecoflex-pipe-systems-UK-1142161.pdf
    title: Ecoflex Solutions Technical Information UK
    doc_type: datasheet
  - url: https://brandportal.uponor.com/m/40b38e79540d873b/original/PB_S_Press_Plus_EN_09-2025_1094180.pdf
    title: Uponor S-Press PLUS Product Brochure
    doc_type: brochure
  product_page_examples:
  - url: https://www.uponor.com/en-en/download-centre
    title: Download centre | Uponor
  - url: https://www.uponor.com/en-en/services/services-for-designers
    title: Services for designers, specifiers and planners | Uponor
  - url: https://www.uponor.com/en-en/products/room-temperature-controls/uponor-smatrix-app-and-software/downloads
    title: Uponor Smatrix App - downloads
  - url: https://www.uponor.com/en-us/customer-support/order-catalog
    title: Product catalog | Uponor
  - url: https://www.uponor.com/en-en/solutions/uponor-infra-solutions/tanks
    title: Polyethylene tanks | Uponor
  download_center_url: https://www.uponor.com/en-en/download-centre
  search_queries_run:
  - site:uponor.com filetype:pdf
  - site:uponor.com products download centre
  search_notes: PDFs split between www.uponor.com/getmedia and brandportal.uponor.com
    subdomain. Strong en-en locale coverage with formal Download Centre.
```
