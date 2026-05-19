# 002 - ESBE

## 1. Brand identity

- Standard brand name: ESBE
- Official website: https://esbe.eu/group/

- English website: https://esbe.eu/group/products

- Country / region: not_verified_by_browser
- Is this the official brand website: not_verified_by_browser
- Brand / group relationship: 区域选择可能影响可见产品，建议 YAML 使用 group/en 产品入口。
- Notes: not_verified_by_browser; this revision avoids placeholder claims of browser-confirmed evidence. This file is an investigation scaffold / YAML candidate, not a final verified crawl config.

## 2. Website entry decision

- Recommended entry_url: https://esbe.eu/group/products

- Alternative entry URLs: https://esbe.eu/group/
; https://esbe.eu/group/products

- Why this entry URL was selected: mapped from source document fields; not_verified_by_browser in this environment.
- Should the crawler lock to a language path: no_or_needs_review
- Suggested path_prefix: null

## 3. Product scope

- Priority product lines: 混水阀、温控混合阀、旋转阀、执行器和热力控制组件，适合地暖混水与水力控制参考。
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
brand: esbe
brand_name: "ESBE"
website: "https://esbe.eu/group/"
entry_url: "https://esbe.eu/group/products"
seed_urls:
  - "https://esbe.eu/group/products"
max_pages: 250

url_scope:
  path_prefix: null

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
  manual_review: "区域选择可能影响可见产品，建议 YAML 使用 group/en 产品入口。"
  crawl_scope_notes: "爬 Products 下 thermostatic mixing valves、rotary valves、actuators、controllers、loading units；PDF 可从产品页和 media/download 链接收集。
"
  product_line_notes: "混水阀、温控混合阀、旋转阀、执行器和热力控制组件，适合地暖混水与水力控制参考。"
```
