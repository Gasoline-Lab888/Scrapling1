# 017 - Caleffi

## 1. Brand identity

- Standard brand name: Caleffi
- Official website: https://www.caleffi.com/
- English website: https://www.caleffi.com/en-int
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 搜索确认官方产品搜索和目录 PDF；页面有产品检索入口。
- Notes: Caleffi 区域站很多，建议优先 en-int，必要时补 North America catalog。

## 2. Website entry decision

- Recommended entry_url: https://www.caleffi.com/en-int/products/search
- Alternative entry URLs: https://www.caleffi.com/en-int; https://www.caleffi.com/
- Why this entry URL was selected: 爬 en-int products/search 和 technical brochures，重点 balancing valves、mixing valves、manifolds、heat interface、safety/control devices。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en-int/products/

## 3. Product scope

- Priority product lines: 暖通水力控制、混水、平衡、分集水器和系统组件标杆，PDF 资料质量高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.caleffi.com/en-int/products/search
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
  1. https://www.caleffi.com/en-int/products/search
  2. https://www.caleffi.com/en-int
  3. https://www.caleffi.com/
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
brand: caleffi
brand_name: "Caleffi"
website: https://www.caleffi.com/
entry_url: https://www.caleffi.com/en-int/products/search
seed_urls:
  - https://www.caleffi.com/en-int/products/search
max_pages: 300

url_scope:
  path_prefix: "/en-int/products/"

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
