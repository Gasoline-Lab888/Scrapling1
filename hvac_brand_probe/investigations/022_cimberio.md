# 022 - Cimberio

## 1. Brand identity

- Standard brand name: Cimberio
- Official website: https://www.cimberio.com/
- English website: https://www.cimberio.com/en/
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 cimberio.com/en 官方英文站；搜索结果显示产品指南 PDF 但可能在 CDN 或第三方。
- Notes: 需确认官网 PDF 链接是否可从站内导航发现。

## 2. Website entry decision

- Recommended entry_url: https://www.cimberio.com/en/
- Alternative entry URLs: https://www.cimberio.com/en/; https://www.cimberio.com/
- Why this entry URL was selected: 爬英文 products/catalogue，重点 valves、balancing valves、actuated/control valves、brass/industrial valves。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/

## 3. Product scope

- Priority product lines: 阀门制造品牌，覆盖黄铜阀、平衡阀、控制阀及工业/建筑阀门。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 可能有
- Download center URL: https://www.cimberio.com/en/
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
  1. https://www.cimberio.com/en/
  2. https://www.cimberio.com/en/
  3. https://www.cimberio.com/
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
brand: cimberio
brand_name: "Cimberio"
website: https://www.cimberio.com/
entry_url: https://www.cimberio.com/en/
seed_urls:
  - https://www.cimberio.com/en/
max_pages: 300

url_scope:
  path_prefix: "/en/"

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
