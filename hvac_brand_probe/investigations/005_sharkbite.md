# 005 - SharkBite

## 1. Brand identity

- Standard brand name: SharkBite
- Official website: https://www.sharkbite.com/
- English website: https://www.sharkbite.com/us/en/
- Country / region: USA
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 technical-downloads 页面，PDF/下载链接明显。
- Notes: 产品偏 plumbing，需在 YAML 中过滤零售/DIY 内容，保留技术资料和产品页。

## 2. Website entry decision

- Recommended entry_url: https://www.sharkbite.com/us/en/technical-downloads
- Alternative entry URLs: https://www.sharkbite.com/us/en/; https://www.sharkbite.com/
- Why this entry URL was selected: 爬 Products、Resources/Technical Downloads，重点 push-to-connect fittings、PEX pipe、valves、manifolds、installation guides。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /us/en/

## 3. Product scope

- Priority product lines: PEX 与快接管件品牌，强于水暖安装、管件、阀门和系统手册。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.sharkbite.com/us/en/technical-downloads
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
  1. https://www.sharkbite.com/us/en/technical-downloads
  2. https://www.sharkbite.com/us/en/
  3. https://www.sharkbite.com/
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
brand: sharkbite
brand_name: "SharkBite"
website: https://www.sharkbite.com/
entry_url: https://www.sharkbite.com/us/en/technical-downloads
seed_urls:
  - https://www.sharkbite.com/us/en/technical-downloads
max_pages: 300

url_scope:
  path_prefix: "/us/en/"

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
