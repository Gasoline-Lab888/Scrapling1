# 024 - Polypipe Underfloor Heating

## 1. Brand identity

- Standard brand name: Polypipe Underfloor Heating
- Official website: https://www.polypipe.com/
- English website: https://www.polypipeufh.com/
- Country / region: UK
- Is this the official brand website: 是
- Brand / group relationship: Chrome 重试确认 Polypipe UFH Downloads 页面含 PDF 和下载链接。
- Notes: polypipe.com 主站范围很大，建议 YAML 先锁定 polypipeufh.com。

## 2. Website entry decision

- Recommended entry_url: https://www.polypipeufh.com/support-hub/support-hub-downloads/
- Alternative entry URLs: https://www.polypipeufh.com/; https://www.polypipe.com/
- Why this entry URL was selected: 优先爬 Polypipe UFH 独立站 support downloads、products/systems；重点 underfloor heating packs、manifolds、controls、pipes、installation manuals。
- Should the crawler lock to a language path: no
- Suggested path_prefix: /support-hub/support-hub-downloads/

## 3. Product scope

- Priority product lines: 英国地暖系统品牌，UFH 产品、控制器、分集水器和安装资料强相关。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.polypipeufh.com/support-hub/support-hub-downloads/
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
  1. https://www.polypipeufh.com/support-hub/support-hub-downloads/
  2. https://www.polypipeufh.com/
  3. https://www.polypipe.com/
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
brand: polypipe_underfloor_heating
brand_name: "Polypipe Underfloor Heating"
website: https://www.polypipe.com/
entry_url: https://www.polypipeufh.com/support-hub/support-hub-downloads/
seed_urls:
  - https://www.polypipeufh.com/support-hub/support-hub-downloads/
max_pages: 300

url_scope:
  path_prefix: "/support-hub/support-hub-downloads/"

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
