# 018 - Fratelli Pettinaroli / Jomar

## 1. Brand identity

- Standard brand name: Fratelli Pettinaroli / Jomar
- Official website: https://www.pettinaroli.com/
- English website: https://www.pettinaroli.com/en/
- Country / region: Italy / USA
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 Pettinaroli 英文官网；搜索 Pettinaroli/Jomar 时也出现 Jomar 下载库。
- Notes: 需人工确认 018 是否只代表 Pettinaroli，还是要并入 Jomar 资料。

## 2. Website entry decision

- Recommended entry_url: https://www.pettinaroli.com/en/
- Alternative entry URLs: https://www.pettinaroli.com/en/; https://www.pettinaroli.com/
- Why this entry URL was selected: 先爬 Pettinaroli English products，重点 manifolds、valves、HVAC components；Jomar 美国站作为单独品牌在 027 处理。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/

## 3. Product scope

- Priority product lines: 黄铜阀门、分集水器、HVAC/水暖组件；与 Jomar/Jomar Valve 有品牌关联但站点应分开。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: yes

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.pettinaroli.com/en/
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
  1. https://www.pettinaroli.com/en/
  2. https://www.pettinaroli.com/en/
  3. https://www.pettinaroli.com/
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
brand: fratelli_pettinaroli_jomar
brand_name: "Fratelli Pettinaroli / Jomar"
website: https://www.pettinaroli.com/
entry_url: https://www.pettinaroli.com/en/
seed_urls:
  - https://www.pettinaroli.com/en/
max_pages: 300

url_scope:
  path_prefix: "/en/"

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
