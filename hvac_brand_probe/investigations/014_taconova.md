# 014 - Taconova

## 1. Brand identity

- Standard brand name: Taconova
- Official website: https://www.taconova.com/
- English website: https://www.taconova.com/en/
- Country / region: Switzerland
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 Download-Center 页面，PDF/下载入口丰富。
- Notes: 下载中心筛选条件需在 YAML 阶段确认是否可静态抓取。

## 2. Website entry decision

- Recommended entry_url: https://www.taconova.com/en/download-center
- Alternative entry URLs: https://www.taconova.com/en/; https://www.taconova.com/
- Why this entry URL was selected: 爬 hydronic balancing、panel heating、system technology、download center；重点 balancing valves、mixing stations、manifolds、pump groups。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/download-center/

## 3. Product scope

- Priority product lines: 水力平衡、流量调节、地暖/面板采暖和系统技术组件。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.taconova.com/en/download-center
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
  1. https://www.taconova.com/en/download-center
  2. https://www.taconova.com/en/
  3. https://www.taconova.com/
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
brand: taconova
brand_name: "Taconova"
website: https://www.taconova.com/
entry_url: https://www.taconova.com/en/download-center
seed_urls:
  - https://www.taconova.com/en/download-center
max_pages: 300

url_scope:
  path_prefix: "/en/download-center/"

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
