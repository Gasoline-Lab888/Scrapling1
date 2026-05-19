# 012 - Möhlenhoff / Mohlenhoff

## 1. Brand identity

- Standard brand name: Möhlenhoff / Mohlenhoff
- Official website: https://www.moehlenhoff.de/
- English website: https://www.moehlenhoff.de/en/
- Country / region: Germany
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 /en/download 页面，PDF 下载链接明显。
- Notes: 品牌德文字符 Möhlenhoff 与 Mohlenhoff URL 拼写需统一。

## 2. Website entry decision

- Recommended entry_url: https://www.moehlenhoff.de/en/download
- Alternative entry URLs: https://www.moehlenhoff.de/en/; https://www.moehlenhoff.de/
- Why this entry URL was selected: 爬 English products/download，重点 thermal actuators、room thermostats、UFH controls、connection strips、wireless control manuals。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/download/

## 3. Product scope

- Priority product lines: 地暖温控、执行器、接线中心和室温控制系统，控制类参考价值高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.moehlenhoff.de/en/download
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
  1. https://www.moehlenhoff.de/en/download
  2. https://www.moehlenhoff.de/en/
  3. https://www.moehlenhoff.de/
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
brand: m_hlenhoff_mohlenhoff
brand_name: "Möhlenhoff / Mohlenhoff"
website: https://www.moehlenhoff.de/
entry_url: https://www.moehlenhoff.de/en/download
seed_urls:
  - https://www.moehlenhoff.de/en/download
max_pages: 300

url_scope:
  path_prefix: "/en/download/"

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
