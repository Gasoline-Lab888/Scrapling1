# 006 - JG Speedfit / John Guest

## 1. Brand identity

- Standard brand name: JG Speedfit / John Guest
- Official website: https://www.johnguest.com/
- English website: https://www.johnguest.com/gb/en/
- Country / region: UK
- Is this the official brand website: 是
- Brand / group relationship: Chrome 搜索确认官方 data-sheets；直接打开触发 Cloudflare Just a moment，需爬虫处理防护。
- Notes: 后续需人工/爬虫确认是否可稳定访问，必要时使用 RWC 品牌入口作为备选。

## 2. Website entry decision

- Recommended entry_url: https://www.johnguest.com/gb/en/resources/data-sheets
- Alternative entry URLs: https://www.johnguest.com/gb/en/; https://www.johnguest.com/
- Why this entry URL was selected: 爬 GB/EN products 与 resources/data-sheets，重点 Speedfit plumbing、underfloor heating、manifolds、pipe/fittings、installation guides。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /gb/en/

## 3. Product scope

- Priority product lines: 快接管件、塑料管道、地暖系统和配套阀件，适合 PEX/UFH 系统资料。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.johnguest.com/gb/en/resources/data-sheets
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
  1. https://www.johnguest.com/gb/en/resources/data-sheets
  2. https://www.johnguest.com/gb/en/
  3. https://www.johnguest.com/
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
brand: jg_speedfit_john_guest
brand_name: "JG Speedfit / John Guest"
website: https://www.johnguest.com/
entry_url: https://www.johnguest.com/gb/en/resources/data-sheets
seed_urls:
  - https://www.johnguest.com/gb/en/resources/data-sheets
max_pages: 300

url_scope:
  path_prefix: "/gb/en/"

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
