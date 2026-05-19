# 010 - Danfoss

## 1. Brand identity

- Standard brand name: Danfoss
- Official website: https://www.danfoss.com/
- English website: https://www.danfoss.com/en/
- Country / region: Denmark
- Is this the official brand website: 是
- Brand / group relationship: Chrome 打开官方 products/dhs/valves 页面，含 hydronic balancing and control 标签。
- Notes: Danfoss 产品庞大，YAML 必须限制到 heating/hydronic valves，避免压缩机、制冷等大类。

## 2. Website entry decision

- Recommended entry_url: https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
- Alternative entry URLs: https://www.danfoss.com/en/; https://www.danfoss.com/
- Why this entry URL was selected: 爬 DHS valves，重点 hydronic balancing/control、thermostatic radiator valves、PICV、district heating valves 和文档链接。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/products/

## 3. Product scope

- Priority product lines: 暖通控制阀、平衡阀、恒温控制和区域供热控制标杆品牌。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
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
  1. https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
  2. https://www.danfoss.com/en/
  3. https://www.danfoss.com/
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
brand: danfoss
brand_name: "Danfoss"
website: https://www.danfoss.com/
entry_url: https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
seed_urls:
  - https://www.danfoss.com/en/products/dhs/valves/#tab-hydronic-balancing-and-control
max_pages: 300

url_scope:
  path_prefix: "/en/products/"

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
