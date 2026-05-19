# 025 - Giacomini

## 1. Brand identity

- Standard brand name: Giacomini
- Official website: https://www.giacomini.com/
- English website: https://www.giacomini.com/
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 重试确认 International Catalog 页面，初次访问可能有国家/区域选择。
- Notes: 需确认地区选择后的英文产品路径，避免被 change-country 中断。

## 2. Website entry decision

- Recommended entry_url: https://www.giacomini.com/download/international-catalog
- Alternative entry URLs: https://www.giacomini.com/; https://www.giacomini.com/
- Why this entry URL was selected: 爬 International Catalog、download、products，重点 radiant systems、manifolds、thermostatic valves、balancing/control valves、brass components。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /download/international-catalog/

## 3. Product scope

- Priority product lines: 采暖/辐射系统、阀门、分集水器、控制组件和黄铜水暖件，目录价值高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.giacomini.com/download/international-catalog
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
  1. https://www.giacomini.com/download/international-catalog
  2. https://www.giacomini.com/
  3. https://www.giacomini.com/
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
brand: giacomini
brand_name: "Giacomini"
website: https://www.giacomini.com/
entry_url: https://www.giacomini.com/download/international-catalog
seed_urls:
  - https://www.giacomini.com/download/international-catalog
max_pages: 300

url_scope:
  path_prefix: "/download/international-catalog/"

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
