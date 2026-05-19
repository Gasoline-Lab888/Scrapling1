# 028 - LK Systems

## 1. Brand identity

- Standard brand name: LK Systems
- Official website: https://www.lksystems.se/
- English website: https://www.lksystems.se/en/
- Country / region: Sweden
- Is this the official brand website: 是
- Brand / group relationship: Chrome 重试确认 English Floor Heating 页面，有 PDF/下载链接信号。
- Notes: 站点瑞典本地化强，需确认英文资料覆盖是否完整。

## 2. Website entry decision

- Recommended entry_url: https://www.lksystems.se/en/products/floor-heating/
- Alternative entry URLs: https://www.lksystems.se/en/; https://www.lksystems.se/
- Why this entry URL was selected: 爬 English floor heating/system solutions/products，重点 floor heating pipes、manifolds、shunts/mixing groups、controls、installation docs。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/products/

## 3. Product scope

- Priority product lines: 瑞典地暖系统、管道、分集水器和控制组件，UFH 相关度高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.lksystems.se/en/products/floor-heating/
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
  1. https://www.lksystems.se/en/products/floor-heating/
  2. https://www.lksystems.se/en/
  3. https://www.lksystems.se/
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
brand: lk_systems
brand_name: "LK Systems"
website: https://www.lksystems.se/
entry_url: https://www.lksystems.se/en/products/floor-heating/
seed_urls:
  - https://www.lksystems.se/en/products/floor-heating/
max_pages: 300

url_scope:
  path_prefix: "/en/products/"

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
