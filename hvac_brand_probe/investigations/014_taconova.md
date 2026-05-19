# 014 - Taconova

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:taconova.com filetype:pdf`; `site:taconova.com products english download center`

## 1. Brand identity

- Standard brand name: Taconova
- Official website: https://www.taconova.com/
- English website (source doc): https://www.taconova.com/en/
- English URL confirmed in search index: https://www.taconova.com/en/download-center
- Country / region: Switzerland (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 下载中心筛选条件需在 YAML 阶段确认是否可静态抓取。
- Notes: Chrome 确认 Download-Center 页面，PDF/下载入口丰富。

## 2. Website entry decision

- Recommended entry_url: https://www.taconova.com/en/download-center
- Alternative entry URLs: https://www.taconova.com/; https://www.taconova.com/en/
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: yes — recommended lock to `/en` (derived from entry URL locale segment)
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 水力平衡、流量调节、地暖/面板采暖和系统技术组件。
- Priority keywords (observed in Google result titles/snippets for this domain): TacoFlow, TacoDrive, NovaMix, TacoTherm, datasheet catalog, circulation pump, manifold, underfloor heating, balancing valve, metering
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 hydronic balancing、panel heating、system technology、download center；重点 balancing valves、mixing stations、manifolds、pump groups。
- Manual review needed: 下载中心筛选条件需在 YAML 阶段确认是否可静态抓取。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.taconova.com/en/download-center
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.taconova.com/fileadmin/downloads/Drucksachen/Datenblattkatalog/Datenblattkatalog_e.pdf — Datasheet Catalog (English) (catalogue)
  2. https://www.taconova.com/fileadmin/downloads/DB/PT/anleitungen/Einbau-%20und%20Betriebsanleitung%20TacoFlow2%20Pure%20plus_e.pdf — TacoFlow2 Pure plus Installation and Operating Manual (installation guide)
  3. https://www.taconova.com/fileadmin/downloads/EA/EA_TacoDrive.pdf — TacoDrive (datasheet)
  4. https://www.taconova.com/fileadmin/downloads/EA/EA_NovaMix_Standard_HC.pdf — NovaMix Standard High Capacity (datasheet)
  5. https://www.taconova.com/fileadmin/downloads/DB/ST/TacoTherm_Circ_Mega_Peta_e.pdf — TacoTherm Circ Mega/Peta System Schematic Diagram (datasheet)
- Document types observed in samples: catalogue, datasheet, installation guide
- Notes (search agent): PDFs at /fileadmin/downloads/ path with _e (English) or _d (German) suffix. Clear English download-center entry.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.taconova.com/en/download-center?category=151&cHash=5bab4eb380e096ff2a6e6449f8b702d2 — Download-Center: Taconova
  2. https://taconova.com/en/?amp=&cHash=e03a8a4c6afaef5790441887780eaa79&x182=OlU2 — Home: Taconova
  3. https://www.taconova.com/en/tacoflow3 — TacoFlow3: Taconova
  4. https://www.taconova.com/en/oem — OEM: Taconova
  5. https://www.taconova.com/en/metering-hardware — Metering & Billing (Metering hardware): Taconova
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 Download-Center 页面，PDF/下载入口丰富。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: taconova
brand_name: Taconova
website: https://www.taconova.com/
entry_url: https://www.taconova.com/en/download-center
seed_urls:
- https://www.taconova.com/en/download-center
- https://www.taconova.com/en/download-center?category=151&cHash=5bab4eb380e096ff2a6e6449f8b702d2
- https://taconova.com/en/?amp=&cHash=e03a8a4c6afaef5790441887780eaa79&x182=OlU2
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
  country_region: Switzerland
  manual_review: 下载中心筛选条件需在 YAML 阶段确认是否可静态抓取。
  crawl_scope_notes: 爬 hydronic balancing、panel heating、system technology、download
    center；重点 balancing valves、mixing stations、manifolds、pump groups。
  product_line_notes: 水力平衡、流量调节、地暖/面板采暖和系统技术组件。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - TacoFlow
  - TacoDrive
  - NovaMix
  - TacoTherm
  - datasheet catalog
  - circulation pump
  - manifold
  - underfloor heating
  - balancing valve
  - metering
  pdf_examples:
  - url: https://www.taconova.com/fileadmin/downloads/Drucksachen/Datenblattkatalog/Datenblattkatalog_e.pdf
    title: Datasheet Catalog (English)
    doc_type: catalogue
  - url: https://www.taconova.com/fileadmin/downloads/DB/PT/anleitungen/Einbau-%20und%20Betriebsanleitung%20TacoFlow2%20Pure%20plus_e.pdf
    title: TacoFlow2 Pure plus Installation and Operating Manual
    doc_type: installation_guide
  - url: https://www.taconova.com/fileadmin/downloads/EA/EA_TacoDrive.pdf
    title: TacoDrive
    doc_type: datasheet
  - url: https://www.taconova.com/fileadmin/downloads/EA/EA_NovaMix_Standard_HC.pdf
    title: NovaMix Standard High Capacity
    doc_type: datasheet
  - url: https://www.taconova.com/fileadmin/downloads/DB/ST/TacoTherm_Circ_Mega_Peta_e.pdf
    title: TacoTherm Circ Mega/Peta System Schematic Diagram
    doc_type: datasheet
  product_page_examples:
  - url: https://www.taconova.com/en/download-center?category=151&cHash=5bab4eb380e096ff2a6e6449f8b702d2
    title: 'Download-Center: Taconova'
  - url: https://taconova.com/en/?amp=&cHash=e03a8a4c6afaef5790441887780eaa79&x182=OlU2
    title: 'Home: Taconova'
  - url: https://www.taconova.com/en/tacoflow3
    title: 'TacoFlow3: Taconova'
  - url: https://www.taconova.com/en/oem
    title: 'OEM: Taconova'
  - url: https://www.taconova.com/en/metering-hardware
    title: 'Metering & Billing (Metering hardware): Taconova'
  download_center_url: https://www.taconova.com/en/download-center
  search_queries_run:
  - site:taconova.com filetype:pdf
  - site:taconova.com products english download center
  search_notes: PDFs at /fileadmin/downloads/ path with _e (English) or _d (German)
    suffix. Clear English download-center entry.
```
