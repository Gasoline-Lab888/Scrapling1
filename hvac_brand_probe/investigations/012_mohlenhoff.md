# 012 - Möhlenhoff / Mohlenhoff

## 1. Brand identity

- Standard brand name: Möhlenhoff / Mohlenhoff
- Official website: https://www.moehlenhoff.de/

- English website: https://www.moehlenhoff.de/en/

- Country / region: not_verified_by_browser
- Is this the official brand website: not_verified_by_browser
- Brand / group relationship: 品牌德文字符 Möhlenhoff 与 Mohlenhoff URL 拼写需统一。
- Notes: not_verified_by_browser; this revision avoids placeholder claims of browser-confirmed evidence. This file is an investigation scaffold / YAML candidate, not a final verified crawl config.

## 2. Website entry decision

- Recommended entry_url: https://www.moehlenhoff.de/en/download

- Alternative entry URLs: https://www.moehlenhoff.de/
; https://www.moehlenhoff.de/en/

- Why this entry URL was selected: mapped from source document fields; not_verified_by_browser in this environment.
- Should the crawler lock to a language path: yes
- Suggested path_prefix: "/en/"

## 3. Product scope

- Priority product lines: 地暖温控、执行器、接线中心和室温控制系统，控制类参考价值高。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, mixing valve, thermostatic valve
- Product lines / pages to exclude: news, blog, events, careers, privacy, cookie, about, contact
- Should this brand be split into sub-brands or sub-sites: review_needed

## 4. Downloads / PDF evidence

- Has download center: not_verified_by_browser
- Download center URL: not_verified_by_browser
- PDF links found: 0 (not_verified_by_browser)
- PDF samples, maximum 5:
  1. not_verified_by_browser
  2. not_verified_by_browser
  3. not_verified_by_browser
  4. not_verified_by_browser
  5. not_verified_by_browser
- Document types found:
  - catalogue (not_verified_by_browser)
  - brochure (not_verified_by_browser)
  - datasheet (not_verified_by_browser)
  - technical manual (not_verified_by_browser)
  - installation guide (not_verified_by_browser)
  - certificate (not_verified_by_browser)
- Notes: Browser/search verification was not performed for this brand in the current update.

## 5. Product page evidence

- Product pages found: not_verified_by_browser
- Product page samples, maximum 5:
  1. not_verified_by_browser
  2. not_verified_by_browser
  3. not_verified_by_browser
  4. not_verified_by_browser
  5. not_verified_by_browser
- Product page structure assessment: not_verified_by_browser
- May require JS rendering: not_verified_by_browser

## 6. Crawl risk / blocking

- HTTP 403 / 429 encountered: not_verified_by_browser
- Cloudflare / captcha encountered: not_verified_by_browser
- Login required: not_verified_by_browser
- Cookie / session required: not_verified_by_browser
- blocked_reason: not_verified_by_browser
- Browser investigation conclusion: not_verified_by_browser

## 7. Suggested hvac-ai-crawler YAML

```yaml
brand: moehlenhoff
brand_name: "Möhlenhoff / Mohlenhoff"
website: "https://www.moehlenhoff.de/"
entry_url: "https://www.moehlenhoff.de/en/download"
seed_urls:
  - "https://www.moehlenhoff.de/en/download"
max_pages: 250

url_scope:
  path_prefix: "/en/"

page_role_classification:
  category:
    indicators:
      - "/product"
    recurse: true
  product:
    indicators:
      - "/product/"
    recurse: false
  navigation:
    indicators:
      - "/download"
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

probe_notes:
  verification_status: "not_verified_by_browser"
  suggested_category: "A-核心暖通水力控制/地暖阀门"
  suggested_priority: "P0"
  manual_review: "品牌德文字符 Möhlenhoff 与 Mohlenhoff URL 拼写需统一。"
  crawl_scope_notes: "爬 English products/download，重点 thermal actuators、room thermostats、UFH controls、connection strips、wireless control manuals。
"
  product_line_notes: "地暖温控、执行器、接线中心和室温控制系统，控制类参考价值高。"
```
