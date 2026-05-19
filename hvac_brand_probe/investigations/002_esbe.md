# 002 - ESBE

## 1. Brand identity

- Standard brand name: ESBE
- Official website: https://esbe.eu/group/
- English website: https://esbe.eu/group/products
- Country / region: Sweden
- Is this the official brand website: 是
- Brand / group relationship: Chrome 搜索和官网页面均显示 English products 与产品 PDF 入口。
- Notes: 区域选择可能影响可见产品，建议 YAML 使用 group/en 产品入口。

## 2. Website entry decision

- Recommended entry_url: https://esbe.eu/group/products
- Alternative entry URLs: https://esbe.eu/group/products; https://esbe.eu/group/
- Why this entry URL was selected: 爬 Products 下 thermostatic mixing valves、rotary valves、actuators、controllers、loading units；PDF 可从产品页和 media/download 链接收集。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /group/products/

## 3. Product scope

- Priority product lines: 混水阀、温控混合阀、旋转阀、执行器和热力控制组件，适合地暖混水与水力控制参考。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://esbe.eu/group/products
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
  1. https://esbe.eu/group/products
  2. https://esbe.eu/group/products
  3. https://esbe.eu/group/
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
brand: esbe
brand_name: "ESBE"
website: https://esbe.eu/group/
entry_url: https://esbe.eu/group/products
seed_urls:
  - https://esbe.eu/group/products
max_pages: 300

url_scope:
  path_prefix: "/group/products/"

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
