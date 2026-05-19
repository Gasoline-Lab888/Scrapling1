# 008 - Barberi Rubinetterie

## 1. Brand identity

- Standard brand name: Barberi Rubinetterie
- Official website: https://www.barberi.it/
- English website: https://www.barberi.it/ww/en/
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 /ww/en/products 英文产品列表，页面含下载/资料入口。
- Notes: 需确认产品页 PDF 是否动态加载。

## 2. Website entry decision

- Recommended entry_url: https://www.barberi.it/ww/en/products
- Alternative entry URLs: https://www.barberi.it/ww/en/; https://www.barberi.it/
- Why this entry URL was selected: 爬英文产品列表，重点 mixing units、manifolds、safety valves、balancing/shut-off valves、pump groups，PDF 从产品页收集。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /ww/en/

## 3. Product scope

- Priority product lines: 黄铜阀门、采暖机组、混水组件、分集水器与水暖控制组件。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.barberi.it/ww/en/products
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
  1. https://www.barberi.it/ww/en/products
  2. https://www.barberi.it/ww/en/
  3. https://www.barberi.it/
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
brand: barberi_rubinetterie
brand_name: "Barberi Rubinetterie"
website: https://www.barberi.it/
entry_url: https://www.barberi.it/ww/en/products
seed_urls:
  - https://www.barberi.it/ww/en/products
max_pages: 300

url_scope:
  path_prefix: "/ww/en/"

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
