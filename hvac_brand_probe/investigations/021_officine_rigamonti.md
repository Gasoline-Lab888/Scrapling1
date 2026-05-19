# 021 - Officine Rigamonti / OR

## 1. Brand identity

- Standard brand name: Officine Rigamonti / OR
- Official website: https://www.officinerigamonti.it/
- English website: https://www.officinerigamonti.it/en/
- Country / region: Italy
- Is this the official brand website: 是
- Brand / group relationship: Chrome 搜索确认官方英文站；搜索结果出现 2025 catalog PDF，但来自第三方域，需谨慎。
- Notes: 官网内下载页/PDF 入口需人工复核，避免混入代理商目录。

## 2. Website entry decision

- Recommended entry_url: https://www.officinerigamonti.it/en/
- Alternative entry URLs: https://www.officinerigamonti.it/en/; https://www.officinerigamonti.it/
- Why this entry URL was selected: 爬英文 products，重点 valves、pressure reducing/safety、brass plumbing components；PDF 可能通过 catalogue 或产品页链接。
- Should the crawler lock to a language path: yes
- Suggested path_prefix: /en/

## 3. Product scope

- Priority product lines: 黄铜阀门、水暖控制和通用阀件，适合作为阀门结构与目录参考。
- Priority keywords: hydronic, underfloor heating, manifold, balancing valve, control valve, thermostatic valve, actuator, datasheet
- Product lines / pages to exclude: news, blog, career, investor, generic corporate pages
- Should this brand be split into sub-brands or sub-sites: no

## 4. Downloads / PDF evidence

- Has download center: 可能有
- Download center URL: https://www.officinerigamonti.it/en/
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
  1. https://www.officinerigamonti.it/en/
  2. https://www.officinerigamonti.it/en/
  3. https://www.officinerigamonti.it/
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
brand: officine_rigamonti_or
brand_name: "Officine Rigamonti / OR"
website: https://www.officinerigamonti.it/
entry_url: https://www.officinerigamonti.it/en/
seed_urls:
  - https://www.officinerigamonti.it/en/
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
