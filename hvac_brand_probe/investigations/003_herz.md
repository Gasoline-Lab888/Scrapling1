# 003 - HERZ Armaturen

## 1. Brand identity

- Standard brand name: HERZ Armaturen
- Official website: https://www.herz.eu/
- English website: https://www.herz.eu/index_eng.html
- Country / region: Austria
- Is this the official brand website: 是
- Brand / group relationship: Chrome 搜索结果显示 herz.eu 英文站和多个 HERZ catalogue PDF。
- Notes: HERZ 存在国家站/媒体服务器，需确认主爬使用 herz.eu 而不是区域经销商 PDF。

## 2. Website entry decision

- Recommended entry_url: https://www.herz.eu/index_eng.html
- Alternative entry URLs: https://www.herz.eu/index_eng.html; https://www.herz.eu/
- Why this entry URL was selected: 从 English 首页进入 Products/Catalogues，重点 radiator valves、thermostatic valves、balancing valves、manifolds、floor heating 相关资料。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /index_eng.html

## 3. Product scope

- Priority product lines: 阀门、恒温控制、水力平衡、分集水器与采暖控制，产品面广且技术 PDF 价值高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.herz.eu/index_eng.html
- PDF links found: indicated in source document / manual browser check required per run
- PDF samples, maximum 5:
  1. TBD from official site crawl
  2. TBD
  3. TBD
  4. TBD
  5. TBD
- Document types found:
  - catalogue
  - brochure
  - datasheet
  - technical manual
  - installation guide
  - certificate
- Notes: Prioritize official domain and official download center PDF links.

## 5. Product page evidence

- Product pages found: yes (per source document notes)
- Product page samples, maximum 5:
  1. https://www.herz.eu/index_eng.html
  2. https://www.herz.eu/index_eng.html
  3. https://www.herz.eu/
  4. TBD
  5. TBD
- Product page structure assessment: mixed modern and legacy structures; include static HTML/PHP if present
- May require JS rendering: possible for filtered product/download pages

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: unknown (requires runtime probing)
- Cloudflare / captcha encountered: possible for some brands (e.g., JG Speedfit per source note)
- Login required: generally no
- Cookie / session required: possible for localized selectors
- blocked_reason: none confirmed from source document
- Browser investigation conclusion: start from recommended English entry URL and pivot to products/download sections.

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: herz_armaturen
brand_name: "HERZ Armaturen"
website: https://www.herz.eu/
entry_url: https://www.herz.eu/index_eng.html
seed_urls:
  - https://www.herz.eu/index_eng.html
max_pages: 300

url_scope:
  path_prefix: "/index_eng.html"

page_role_classification:
  category:
    indicators:
      - "products"
    recurse: true
  product:
    indicators:
      - "datasheet"
    recurse: false
  navigation:
    indicators:
      - "download"
    recurse: true

fields:
  product_name: "h1"
  downloads: "a[href$='.pdf']"

filters:
  download_link_selector: "a[href$='.pdf']"
  reject_url_patterns:
    - "/news/"
    - "/blog/"
    - "/events/"
    - "/careers/"
    - "/privacy/"
    - "/terms/"
    - "/cookie/"
    - "/contact/"
    - "/about/"
  global_download_threshold: 10
```
