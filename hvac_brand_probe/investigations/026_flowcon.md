# 026 - FlowCon

## 1. Brand identity

- Standard brand name: FlowCon
- Official website: https://flowcon.com/
- English website: https://flowcon.com/
- Country / region: Denmark
- Is this the official brand website: 是
- Brand / group relationship: Chrome 重试确认 Product Literature 页面，PDF/下载链接丰富。
- Notes: FlowCon 原 Excel URL 为空，已通过 Chrome 搜索补全。

## 2. Website entry decision

- Recommended entry_url: https://flowcon.com/view-and-download/product-literature
- Alternative entry URLs: https://flowcon.com/; https://flowcon.com/
- Why this entry URL was selected: 爬 Product Literature 和 product pages，重点 PICV、dynamic balancing valves、actuators、cartridges、commissioning documents。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /view-and-download/product-literature/

## 3. Product scope

- Priority product lines: 压差无关控制阀和动态水力平衡阀专业品牌，商用 HVAC 控制阀参考价值高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://flowcon.com/view-and-download/product-literature
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
  1. https://flowcon.com/view-and-download/product-literature
  2. https://flowcon.com/
  3. https://flowcon.com/
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
brand: flowcon
brand_name: "FlowCon"
website: https://flowcon.com/
entry_url: https://flowcon.com/view-and-download/product-literature
seed_urls:
  - https://flowcon.com/view-and-download/product-literature
max_pages: 300

url_scope:
  path_prefix: "/view-and-download/product-literature/"

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
