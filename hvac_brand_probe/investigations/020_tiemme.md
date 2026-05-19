# 020 - Tiemme

## 1. Brand identity

- Standard brand name: Tiemme
- Official website: https://www.tiemme.com/
- English website: https://www.tiemme.com/
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 打开主站标题为意大利语；Google 结果显示 m.tiemme.com/eng 英文产品页和 PDF/目录信号。
- Notes: 需人工确认稳定英文入口，可能是移动英文站或语言切换后的路径。

## 2. Website entry decision

- Recommended entry_url: https://www.tiemme.com/
- Alternative entry URLs: https://www.tiemme.com/; https://www.tiemme.com/
- Why this entry URL was selected: 爬产品目录中 manifolds、valves、fittings、PEX/multilayer、heating components；Chrome 搜索可补 m.tiemme.com/eng 产品页。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /

## 3. Product scope

- Priority product lines: 管件、阀门、分集水器、采暖系统和多层管系统。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.tiemme.com/
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
  1. https://www.tiemme.com/
  2. https://www.tiemme.com/
  3. https://www.tiemme.com/
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
brand: tiemme
brand_name: "Tiemme"
website: https://www.tiemme.com/
entry_url: https://www.tiemme.com/
seed_urls:
  - https://www.tiemme.com/
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
