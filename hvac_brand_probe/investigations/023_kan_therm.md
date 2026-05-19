# 023 - KAN-therm

## 1. Brand identity

- Standard brand name: KAN-therm
- Official website: https://en.kan-therm.com/
- English website: https://en.kan-therm.com/
- Country / region: Poland
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 en.kan-therm.com 官方英文站，搜索和页面均显示 PDF/guidebook 信号。
- Notes: 不同国家子域较多，建议锁定 en.kan-therm.com。

## 2. Website entry decision

- Recommended entry_url: https://en.kan-therm.com/
- Alternative entry URLs: https://en.kan-therm.com/; https://en.kan-therm.com/
- Why this entry URL was selected: 爬 systems/products/downloads，重点 surface heating/cooling、KAN-therm pipes、manifolds、controls、system guidebooks。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /

## 3. Product scope

- Priority product lines: 水暖/采暖系统、地暖/面板采暖、管道系统和分集水器，系统资料价值高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://en.kan-therm.com/
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
  1. https://en.kan-therm.com/
  2. https://en.kan-therm.com/
  3. https://en.kan-therm.com/
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
brand: kan_therm
brand_name: "KAN-therm"
website: https://en.kan-therm.com/
entry_url: https://en.kan-therm.com/
seed_urls:
  - https://en.kan-therm.com/
max_pages: 300

url_scope:
  path_prefix: "/"

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
