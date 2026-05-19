# 016 - Altecnic

## 1. Brand identity

- Standard brand name: Altecnic
- Official website: https://www.altecnic.co.uk/
- English website: https://www.altecnic.co.uk/
- Country / region: UK
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 downloads 页面，PDF 和 technical data sheet 分类明显。
- Notes: 需确认与 Caleffi 产品重复边界。

## 2. Website entry decision

- Recommended entry_url: https://www.altecnic.co.uk/downloads/
- Alternative entry URLs: https://www.altecnic.co.uk/; https://www.altecnic.co.uk/
- Why this entry URL was selected: 爬 Products 和 Downloads，重点 heating、hydronic solutions、mixing valves、PICV/balancing、manifolds、technical data sheets。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /downloads/

## 3. Product scope

- Priority product lines: 英国 HVAC/水暖阀门与 Caleffi 相关产品，技术数据表完整。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.altecnic.co.uk/downloads/
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
  1. https://www.altecnic.co.uk/downloads/
  2. https://www.altecnic.co.uk/
  3. https://www.altecnic.co.uk/
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
brand: altecnic
brand_name: "Altecnic"
website: https://www.altecnic.co.uk/
entry_url: https://www.altecnic.co.uk/downloads/
seed_urls:
  - https://www.altecnic.co.uk/downloads/
max_pages: 300

url_scope:
  path_prefix: "/downloads/"

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
