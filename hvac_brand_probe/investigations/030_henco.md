# 030 - Henco

## 1. Brand identity

- Standard brand name: Henco
- Official website: https://www.henco.be/
- English website: https://www.henco.be/en/home
- Country / region: Belgium
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 Henco Downloads 页面，技术数据表、brochures、manuals 信号明确。
- Notes: 需关注 Aalberts 收购后的品牌/集团归属，不影响官网爬取。

## 2. Website entry decision

- Recommended entry_url: https://www.henco.be/en/downloads
- Alternative entry URLs: https://www.henco.be/en/home; https://www.henco.be/
- Why this entry URL was selected: 爬 products 和 downloads，重点 multilayer pipe、press fittings、underfloor heating、manifolds、technical data sheets、manuals。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/downloads/

## 3. Product scope

- Priority product lines: 多层管、管件、地暖、分集水器和系统安装资料；Aalberts 旗下品牌。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.henco.be/en/downloads
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
  1. https://www.henco.be/en/downloads
  2. https://www.henco.be/en/home
  3. https://www.henco.be/
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
brand: henco
brand_name: "Henco"
website: https://www.henco.be/
entry_url: https://www.henco.be/en/downloads
seed_urls:
  - https://www.henco.be/en/downloads
max_pages: 300

url_scope:
  path_prefix: "/en/downloads/"

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
