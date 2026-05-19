# 029 - Wavin

## 1. Brand identity

- Standard brand name: Wavin
- Official website: https://wavin.com/
- English website: https://wavin.com/gb
- Country / region: Netherlands / UK
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 wavin.com/gb/downloads 页面含多个 PDF 下载。
- Notes: Wavin 产品范围过宽，YAML 需限制到 heating/underfloor/pipe systems。

## 2. Website entry decision

- Recommended entry_url: https://wavin.com/gb/downloads
- Alternative entry URLs: https://wavin.com/gb; https://wavin.com/
- Why this entry URL was selected: 爬 GB downloads 和 product categories，重点 underfloor heating、heating/cooling、MLCP/PEX pipes、manifolds、controls。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /gb/downloads/

## 3. Product scope

- Priority product lines: 大型管道系统品牌，包含地暖、冷热水、排水和建筑系统；需限定暖通/UFH。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://wavin.com/gb/downloads
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
  1. https://wavin.com/gb/downloads
  2. https://wavin.com/gb
  3. https://wavin.com/
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
brand: wavin
brand_name: "Wavin"
website: https://wavin.com/
entry_url: https://wavin.com/gb/downloads
seed_urls:
  - https://wavin.com/gb/downloads
max_pages: 300

url_scope:
  path_prefix: "/gb/downloads/"

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
