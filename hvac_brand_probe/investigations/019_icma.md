# 019 - ICMA S.p.A.

## 1. Brand identity

- Standard brand name: ICMA S.p.A.
- Official website: https://www.icmaspa.it/
- English website: https://www.icmaspa.it/?lang=en
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认英文 products catalogue 与 downloads 页面。
- Notes: 站点使用 lang=en 参数，需在爬虫中保留语言参数。

## 2. Website entry decision

- Recommended entry_url: https://www.icmaspa.it/products-catalogue/?lang=en
- Alternative entry URLs: https://www.icmaspa.it/?lang=en; https://www.icmaspa.it/
- Why this entry URL was selected: 爬 products-catalogue 和 downloads，重点 heating components、manifolds、mixing units、thermostatic valves、fittings。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: parameter:lang=en

## 3. Product scope

- Priority product lines: 采暖技术阀件、分集水器、管件、混水和系统组件。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.icmaspa.it/products-catalogue/?lang=en
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
  1. https://www.icmaspa.it/products-catalogue/?lang=en
  2. https://www.icmaspa.it/?lang=en
  3. https://www.icmaspa.it/
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
brand: icma_s_p_a
brand_name: "ICMA S.p.A."
website: https://www.icmaspa.it/
entry_url: https://www.icmaspa.it/products-catalogue/?lang=en
seed_urls:
  - https://www.icmaspa.it/products-catalogue/?lang=en
max_pages: 300

url_scope:
  path_prefix: "parameter:lang=en"

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
