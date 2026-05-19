# 015 - Oventrop

## 1. Brand identity

- Standard brand name: Oventrop
- Official website: https://www.oventrop.com/
- English website: https://www.oventrop.com/en
- Country / region: Germany
- Is this the official brand website: 是
- Brand / group relationship: Chrome 打开 /en 官方页，搜索结果显示 Oventrop 文件/PDF URL。
- Notes: Google 搜索结果出现多区域 en-XX 文件链接，需选择稳定全球/英文入口。

## 2. Website entry decision

- Recommended entry_url: https://www.oventrop.com/en
- Alternative entry URLs: https://www.oventrop.com/en; https://www.oventrop.com/
- Why this entry URL was selected: 爬 English 产品目录、文件/文档链接，重点 hydronic balancing、thermostatic valves、floor heating controls、manifolds、stations。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en

## 3. Product scope

- Priority product lines: 暖通阀门、平衡阀、恒温阀、地暖控制与系统组件标杆。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.oventrop.com/en
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
  1. https://www.oventrop.com/en
  2. https://www.oventrop.com/en
  3. https://www.oventrop.com/
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
brand: oventrop
brand_name: "Oventrop"
website: https://www.oventrop.com/
entry_url: https://www.oventrop.com/en
seed_urls:
  - https://www.oventrop.com/en
max_pages: 300

url_scope:
  path_prefix: "/en"

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
