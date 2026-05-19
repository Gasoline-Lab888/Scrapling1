# 009 - Watts

## 1. Brand identity

- Standard brand name: Watts
- Official website: https://www.watts.com/
- English website: https://www.watts.eu/en/
- Country / region: USA / Europe
- Is this the official brand website: 是
- Brand / group relationship: 原 Excel Watts 行 URL 错填为 FAR；Chrome 核查应改用 watts.com / watts.eu 官方站。
- Notes: 需决定爬 watts.com 全球站还是 watts.eu 欧洲站；欧洲站更适合 EN 技术资料。

## 2. Website entry decision

- Recommended entry_url: https://www.watts.eu/en/technical-support
- Alternative entry URLs: https://www.watts.eu/en/; https://www.watts.com/
- Why this entry URL was selected: 优先 Watts Europe EN 技术支持和 HVAC/plumbing 产品；重点 balancing valves、mixing valves、backflow/safety、manifolds、radiant/controls。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/technical-support/

## 3. Product scope

- Priority product lines: 大型水暖/HVAC 控制阀与安全阀品牌，产品线和技术文档丰富。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.watts.eu/en/technical-support
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
  1. https://www.watts.eu/en/technical-support
  2. https://www.watts.eu/en/
  3. https://www.watts.com/
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
brand: watts
brand_name: "Watts"
website: https://www.watts.com/
entry_url: https://www.watts.eu/en/technical-support
seed_urls:
  - https://www.watts.eu/en/technical-support
max_pages: 300

url_scope:
  path_prefix: "/en/technical-support/"

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
