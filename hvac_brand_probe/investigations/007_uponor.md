# 007 - Uponor

## 1. Brand identity

- Standard brand name: Uponor
- Official website: https://www.uponor.com/
- English website: https://www.uponor.com/en-en
- Country / region: Finland
- Is this the official brand website: 是
- Brand / group relationship: Chrome 确认 en-en download-centre 页面含 PDF 和下载筛选。
- Notes: Uponor 有多区域站，建议优先 en-en 或目标市场 EN 页面。

## 2. Website entry decision

- Recommended entry_url: https://www.uponor.com/en-en/download-centre
- Alternative entry URLs: https://www.uponor.com/en-en; https://www.uponor.com/
- Why this entry URL was selected: 爬 Products 和 Download centre，重点 underfloor heating/cooling、PEX/MLCP pipes、manifolds、controls、installation manuals。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en-en/download-centre/

## 3. Product scope

- Priority product lines: 地暖/辐射供冷供热、PEX/多层管、分集水器和控制系统，是系统型品牌标杆。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 是
- Download center URL: https://www.uponor.com/en-en/download-centre
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
  1. https://www.uponor.com/en-en/download-centre
  2. https://www.uponor.com/en-en
  3. https://www.uponor.com/
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
brand: uponor
brand_name: "Uponor"
website: https://www.uponor.com/
entry_url: https://www.uponor.com/en-en/download-centre
seed_urls:
  - https://www.uponor.com/en-en/download-centre
max_pages: 300

url_scope:
  path_prefix: "/en-en/download-centre/"

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
