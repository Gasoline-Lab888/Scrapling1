# 023 - KAN-therm

> **Evidence provenance**
> - Brand metadata (country, category, priority, URLs, scope, product line, manual_review) is mapped from `代表性30个品牌_官网调查与爬取优先级.md`, the author's Chrome-verified baseline source document.
> - URLs in §4 PDF samples / §5 Product pages are taken from Google `site:` search results retrieved on 2026-05-19 via WebSearch.
> - Live HTTP probing (Cloudflare/captcha/login/JS-render detection) was NOT performed in this run because the sandbox blocked outbound HTTP; items marked `not_verified_in_this_run` need a future live-browser pass.
> - Search queries used: `site:en.kan-therm.com filetype:pdf`; `site:en.kan-therm.com products`

## 1. Brand identity

- Standard brand name: KAN-therm
- Official website: https://en.kan-therm.com/
- English website (source doc): https://en.kan-therm.com/
- English URL confirmed in search index: https://en.kan-therm.com/download/catalogs
- Country / region: Poland (per source doc)
- Is this the official brand website: yes (per source doc)
- Brand / group relationship: 不同国家子域较多，建议锁定 en.kan-therm.com。
- Notes: Chrome 确认 en.kan-therm.com 官方英文站，搜索和页面均显示 PDF/guidebook 信号。

## 2. Website entry decision

- Recommended entry_url: https://en.kan-therm.com/
- Alternative entry URLs: https://en.kan-therm.com/download/catalogs
- Why this entry URL was selected: chosen by the source-doc author as the canonical English product/download hub; Google site:search shows this hostname is indexed and serves real product/PDF URLs (see §4 and §5).
- Should the crawler lock to a language path: no_or_needs_review (no obvious locale segment in entry URL)
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 水暖/采暖系统、地暖/面板采暖、管道系统和分集水器，系统资料价值高。
- Priority keywords (observed in Google result titles/snippets for this domain): water installation, heating and cooling, surface heating, underfloor heating, PE-Xa pipes, multisystem, copper, inox, manifold, smart control
- Product lines / pages to exclude: news, blog, press, events, careers, privacy, terms, cookie, about, contact
- Crawl scope notes: 爬 systems/products/downloads，重点 surface heating/cooling、KAN-therm pipes、manifolds、controls、system guidebooks。
- Manual review needed: 不同国家子域较多，建议锁定 en.kan-therm.com。

## 4. Downloads / PDF evidence

- Has download center: yes (per source doc hint + search-observed downloads URL)
- Download center URL: https://en.kan-therm.com/download/catalogs
- PDF links found via Google site:search: 5 (sample; not exhaustive)
- PDF samples, maximum 5 (from Google site:search):
  1. https://en.kan-therm.com/resfile/open/2278/kan-therm-main-catalogue-en-25-04-25.pdf — KAN-therm Main Catalogue Water Installation Heating and Cooling (catalogue)
  2. https://en.kan-therm.com/resfile/open/1259/kan-therm-guidebook-designer&contractor-en-22-09-15-v1.1.pdf — KAN-therm MULTISYSTEM Guidebook Designer and Contractor (technical manual)
  3. https://en.kan-therm.com/resfile/open/1249/kan-therm-guidebook-surface-heating-en-22-09-15.pdf — Surface Heating/Cooling Guidebook (technical manual)
  4. https://en.kan-therm.com/resfile/open/2284/kan-therm-catalogue-surface-heating&cooling-en-25-12-02.pdf — Surface heating and cooling catalogue (catalogue)
  5. https://en.kan-therm.com/resfile/open/1419/36.KAN-DWU%2021EN%20-%20PE-Xa%20%20pipes%20.pdf — System KAN-therm Push PE-Xa Pipes Declaration (certificate)
- Document types observed in samples: catalogue, certificate, technical manual
- Notes (search agent): PDFs hosted at /resfile/open/{ID}/. Systems documented in /system/system-kan-therm-{type} paths. Main catalogue updated 25-04-25 and 25-12-02.

## 5. Product page evidence

- Product pages found via Google site:search: 5 (sample; not exhaustive)
- Product page samples, maximum 5 (from Google site:search):
  1. https://en.kan-therm.com/system/system-kan-therm-inoxflow — System KAN-therm InoxFlow
  2. https://en.kan-therm.com/system/system-kan-therm-copper/tools — Tools - System KAN-therm Copper
  3. https://en.kan-therm.com/download/catalogs — Downloads - Catalogs
  4. https://en.kan-therm.com/p/kan-group — KAN Group
  5. http://en.kan-therm.com/landing/solutions_for_large_area_and_agriculture.html — Solutions for large-area and agriculture
- Product page structure assessment: not_verified_in_this_run (requires live HTTP fetch to inspect DOM/listings)
- May require JS rendering: not_verified_in_this_run (no HTTP fetch performed in this run)

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_in_this_run (sandbox blocked outbound HTTP; previous PR #2 probe under the same sandbox returned sandbox_egress_block 403 for every host, which is a sandbox artefact, not a brand WAF)
- Cloudflare / captcha: not_verified_in_this_run (no live HTTP fetch performed)
- Login required: not_verified_in_this_run
- Cookie / session required: not_verified_in_this_run
- blocked_reason: not_verified_in_this_run
- Browser investigation conclusion (carried from source doc): "Chrome 确认 en.kan-therm.com 官方英文站，搜索和页面均显示 PDF/guidebook 信号。"

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: kan_therm
brand_name: KAN-therm
website: https://en.kan-therm.com/
entry_url: https://en.kan-therm.com/
seed_urls:
- https://en.kan-therm.com/
- https://en.kan-therm.com/download/catalogs
- https://en.kan-therm.com/system/system-kan-therm-inoxflow
- https://en.kan-therm.com/system/system-kan-therm-copper/tools
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
  suggested_category: B-地暖系统/PEX/管道系统
  suggested_priority: P0
  country_region: Poland
  manual_review: 不同国家子域较多，建议锁定 en.kan-therm.com。
  crawl_scope_notes: 爬 systems/products/downloads，重点 surface heating/cooling、KAN-therm
    pipes、manifolds、controls、system guidebooks。
  product_line_notes: 水暖/采暖系统、地暖/面板采暖、管道系统和分集水器，系统资料价值高。
  blocked_reason_hint: ''
  pdf_sample_count: 5
  product_page_sample_count: 5
  evidence_keywords:
  - water installation
  - heating and cooling
  - surface heating
  - underfloor heating
  - PE-Xa pipes
  - multisystem
  - copper
  - inox
  - manifold
  - smart control
  pdf_examples:
  - url: https://en.kan-therm.com/resfile/open/2278/kan-therm-main-catalogue-en-25-04-25.pdf
    title: KAN-therm Main Catalogue Water Installation Heating and Cooling
    doc_type: catalogue
  - url: https://en.kan-therm.com/resfile/open/1259/kan-therm-guidebook-designer&contractor-en-22-09-15-v1.1.pdf
    title: KAN-therm MULTISYSTEM Guidebook Designer and Contractor
    doc_type: manual
  - url: https://en.kan-therm.com/resfile/open/1249/kan-therm-guidebook-surface-heating-en-22-09-15.pdf
    title: Surface Heating/Cooling Guidebook
    doc_type: manual
  - url: https://en.kan-therm.com/resfile/open/2284/kan-therm-catalogue-surface-heating&cooling-en-25-12-02.pdf
    title: Surface heating and cooling catalogue
    doc_type: catalogue
  - url: https://en.kan-therm.com/resfile/open/1419/36.KAN-DWU%2021EN%20-%20PE-Xa%20%20pipes%20.pdf
    title: System KAN-therm Push PE-Xa Pipes Declaration
    doc_type: certificate
  product_page_examples:
  - url: https://en.kan-therm.com/system/system-kan-therm-inoxflow
    title: System KAN-therm InoxFlow
  - url: https://en.kan-therm.com/system/system-kan-therm-copper/tools
    title: Tools - System KAN-therm Copper
  - url: https://en.kan-therm.com/download/catalogs
    title: Downloads - Catalogs
  - url: https://en.kan-therm.com/p/kan-group
    title: KAN Group
  - url: http://en.kan-therm.com/landing/solutions_for_large_area_and_agriculture.html
    title: Solutions for large-area and agriculture
  download_center_url: https://en.kan-therm.com/download/catalogs
  search_queries_run:
  - site:en.kan-therm.com filetype:pdf
  - site:en.kan-therm.com products
  search_notes: PDFs hosted at /resfile/open/{ID}/. Systems documented in /system/system-kan-therm-{type}
    paths. Main catalogue updated 25-04-25 and 25-12-02.
```
