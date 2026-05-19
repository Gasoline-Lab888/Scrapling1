# 016 - Altecnic

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:altecnic.co.uk filetype:pdf`; `site:altecnic.co.uk products`

## 1. Brand identity

- Standard brand name: Altecnic
- Official website: https://www.altecnic.co.uk/
- English website (source doc): https://www.altecnic.co.uk/
- English URL confirmed in search index: https://www.altecnic.co.uk/all-products
- Country / region: UK (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 需确认与 Caleffi 产品重复边界。
- Notes: Chrome 确认 downloads 页面，PDF 和 technical data sheet 分类明显。

## 2. Website entry decision

- Recommended entry_url: https://www.altecnic.co.uk/downloads/
- Alternative entry URLs: https://www.altecnic.co.uk/; https://www.altecnic.co.uk/all-products
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 英国 HVAC/水暖阀门与 Caleffi 相关产品，技术数据表完整。
- Priority keywords (observed in Google result titles/snippets for this domain): dynamic balancing valve, heat interface unit, safety relief valve, discal dirtmag, expansion vessel, PRV, radiator valves, fan coil kits, heat pumps
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 Products 和 Downloads，重点 heating、hydronic solutions、mixing valves、PICV/balancing、manifolds、technical data sheets。
- Manual review needed: 需确认与 Caleffi 产品重复边界。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://www.altecnic.co.uk/all-products
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://www.altecnic.co.uk/wp/wp-content/uploads/downloads/Robokit%20Sealed%20System%20Guide%20IOM.pdf — Robokit Sealed System Guide IOM (installation guide)
  2. https://www.altecnic.co.uk/wp/wp-content/uploads/downloads/5460%20Discal%20Dirtmag%20IOM.pdf — 5460 Discal Dirtmag IOM (DN 50) (installation guide)
  3. https://www.altecnic.co.uk/wp/wp-content/uploads/resource-files/Altecnic_Commercial_Product_Guide_LINKED.pdf — Altecnic Commercial Product Guide (catalogue)
  4. https://www.altecnic.co.uk/wp/wp-content/uploads/2024/10/Autoflow-Balancing-Valve-Application-Guide.pdf — AutoFlow Dynamic Balancing Valve Application Guide (technical manual)
  5. https://www.altecnic.co.uk/wp/wp-content/uploads/downloads/311-312%20Safety%20Relief%20Valve%20Data%20Sheet.pdf — 311 & 312 Safety Relief Valve Data Sheet (datasheet)
- Document types observed in samples: catalogue, datasheet, installation guide, technical manual
- Notes (search agent): PDFs hosted in /wp/wp-content/uploads/. Strong hydronic coverage: AutoFlow balancing, HIU design, Discal, safety valves, expansion vessels.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://www.altecnic.co.uk/domestic/plumbing-heating/radiator-valves — Radiator Valves
  2. https://www.altecnic.co.uk/domestic/plumbing-heating/ball-valves — Ball Valves
  3. https://www.altecnic.co.uk/domestic/plumbing-heating/sealed-systems — Domestic Sealed Systems
  4. https://www.altecnic.co.uk/domestic/plumbing-heating/fan-coil-kits — Fan Coil Kits
  5. https://www.altecnic.co.uk/domestic/renewables/heat-pumps — Heat Pumps Parts - Renewables
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 downloads 页面，PDF 和 technical data sheet 分类明显。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: altecnic
brand_name: Altecnic
website: https://www.altecnic.co.uk/
entry_url: https://www.altecnic.co.uk/downloads/
seed_urls:
- https://www.altecnic.co.uk/downloads/
- https://www.altecnic.co.uk/all-products
- https://www.altecnic.co.uk/domestic/plumbing-heating/radiator-valves
- https://www.altecnic.co.uk/domestic/plumbing-heating/ball-valves
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
  country_region: UK
  manual_review: 需确认与 Caleffi 产品重复边界。
  crawl_scope_notes: 爬 Products 和 Downloads，重点 heating、hydronic solutions、mixing valves、PICV/balancing、manifolds、technical
    data sheets。
  product_line_notes: 英国 HVAC/水暖阀门与 Caleffi 相关产品，技术数据表完整。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - dynamic balancing valve
  - heat interface unit
  - safety relief valve
  - discal dirtmag
  - expansion vessel
  - PRV
  - radiator valves
  - fan coil kits
  - heat pumps
  pdf_examples:
  - url: https://www.altecnic.co.uk/wp/wp-content/uploads/downloads/Robokit%20Sealed%20System%20Guide%20IOM.pdf
    title: Robokit Sealed System Guide IOM
    doc_type: installation_guide
  - url: https://www.altecnic.co.uk/wp/wp-content/uploads/downloads/5460%20Discal%20Dirtmag%20IOM.pdf
    title: 5460 Discal Dirtmag IOM (DN 50)
    doc_type: installation_guide
  - url: https://www.altecnic.co.uk/wp/wp-content/uploads/resource-files/Altecnic_Commercial_Product_Guide_LINKED.pdf
    title: Altecnic Commercial Product Guide
    doc_type: catalogue
  - url: https://www.altecnic.co.uk/wp/wp-content/uploads/2024/10/Autoflow-Balancing-Valve-Application-Guide.pdf
    title: AutoFlow Dynamic Balancing Valve Application Guide
    doc_type: manual
  - url: https://www.altecnic.co.uk/wp/wp-content/uploads/downloads/311-312%20Safety%20Relief%20Valve%20Data%20Sheet.pdf
    title: 311 & 312 Safety Relief Valve Data Sheet
    doc_type: datasheet
  product_page_examples:
  - url: https://www.altecnic.co.uk/domestic/plumbing-heating/radiator-valves
    title: Radiator Valves
  - url: https://www.altecnic.co.uk/domestic/plumbing-heating/ball-valves
    title: Ball Valves
  - url: https://www.altecnic.co.uk/domestic/plumbing-heating/sealed-systems
    title: Domestic Sealed Systems
  - url: https://www.altecnic.co.uk/domestic/plumbing-heating/fan-coil-kits
    title: Fan Coil Kits
  - url: https://www.altecnic.co.uk/domestic/renewables/heat-pumps
    title: Heat Pumps Parts - Renewables
  download_center_url: https://www.altecnic.co.uk/all-products
  search_queries_run:
  - site:altecnic.co.uk filetype:pdf
  - site:altecnic.co.uk products
  search_notes: 'PDFs hosted in /wp/wp-content/uploads/. Strong hydronic coverage:
    AutoFlow balancing, HIU design, Discal, safety valves, expansion vessels.'
```
