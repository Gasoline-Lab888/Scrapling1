from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

from scrapling.fetchers import Fetcher


BASE_URL = "https://esbe.eu"
OUTPUT_ROOT = Path("data/esbe")
RAW_ROOT = OUTPUT_ROOT / "raw"
IMAGES_ROOT = OUTPUT_ROOT / "images"
DOCS_ROOT = OUTPUT_ROOT / "docs"


@dataclass
class Product:
    title: str
    product_url: str
    image_url: str | None
    image_file: str | None
    manuals: list[str]
    manuals_files: list[str]


def slugify(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", text).strip("-").lower()
    return value or "product"


def _request(url: str):
    return Fetcher.fetch(url, timeout=30)


def discover_product_urls() -> set[str]:
    """Find product pages from sitemap-like pages and product links."""
    candidates = [
        f"{BASE_URL}/sitemap.xml",
        f"{BASE_URL}/products",
        BASE_URL,
    ]
    product_urls: set[str] = set()

    for url in candidates:
        try:
            page = _request(url)
        except Exception:
            continue

        for link in page.css("a::attr(href)").getall():
            absolute = urljoin(url, link)
            parsed = urlparse(absolute)
            if not parsed.netloc.endswith("esbe.eu"):
                continue
            if "/products/" in parsed.path.lower() or "product" in parsed.path.lower():
                product_urls.add(absolute.split("#")[0])

    return product_urls


def find_manual_links(page, product_url: str) -> list[str]:
    links: list[str] = []
    for link in page.css("a::attr(href)").getall():
        absolute = urljoin(product_url, link)
        if absolute.lower().endswith(".pdf"):
            links.append(absolute)
    return sorted(set(links))


def download_binary(url: str, output_file: Path) -> bool:
    try:
        response = _request(url)
        body = response.body
    except Exception:
        return False

    if not body:
        return False

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_bytes(body)
    return True


def scrape_products(product_urls: Iterable[str]) -> list[Product]:
    products: list[Product] = []

    for idx, product_url in enumerate(sorted(product_urls), start=1):
        try:
            page = _request(product_url)
        except Exception:
            continue

        title = (
            page.css("h1::text").first(default="").strip()
            or page.css("title::text").first(default="").strip()
            or product_url.rstrip("/").split("/")[-1]
        )
        slug = slugify(title)

        image_url = page.css("meta[property='og:image']::attr(content)").first(default=None)
        if not image_url:
            image_url = page.css("img::attr(src)").first(default=None)
        image_file = None
        if image_url:
            image_url = urljoin(product_url, image_url)
            suffix = Path(urlparse(image_url).path).suffix or ".jpg"
            local_image = IMAGES_ROOT / f"{slug}{suffix}"
            if download_binary(image_url, local_image):
                image_file = str(local_image)

        manuals = find_manual_links(page, product_url)
        manual_files: list[str] = []
        for manual_url in manuals:
            file_name = Path(urlparse(manual_url).path).name or f"{slug}.pdf"
            local_pdf = DOCS_ROOT / slug / file_name
            if download_binary(manual_url, local_pdf):
                manual_files.append(str(local_pdf))
            time.sleep(0.2)

        products.append(
            Product(
                title=title,
                product_url=product_url,
                image_url=image_url,
                image_file=image_file,
                manuals=manuals,
                manuals_files=manual_files,
            )
        )
        print(f"[{idx}] {title} | manuals={len(manual_files)}")
        time.sleep(0.2)

    return products


def write_outputs(products: list[Product]) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    RAW_ROOT.mkdir(parents=True, exist_ok=True)

    tree_data = [asdict(item) for item in products]
    (OUTPUT_ROOT / "products_tree.json").write_text(
        json.dumps(tree_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md_lines = ["# ESBE Product Tree", ""]
    for product in products:
        md_lines.append(f"- **{product.title}**")
        md_lines.append(f"  - URL: {product.product_url}")
        if product.image_file:
            md_lines.append(f"  - Image: `{product.image_file}`")
        if product.manuals_files:
            md_lines.append("  - Manuals:")
            for file in product.manuals_files:
                md_lines.append(f"    - `{file}`")
        else:
            md_lines.append("  - Manuals: none found")
        md_lines.append("")

    (OUTPUT_ROOT / "products_tree.md").write_text("\n".join(md_lines), encoding="utf-8")


def maybe_upload_to_drive() -> None:
    drive_folder = os.getenv("GDRIVE_FOLDER_ID")
    service_account = os.getenv("GDRIVE_SERVICE_ACCOUNT_JSON")
    if not drive_folder or not service_account:
        print("Skip Google Drive upload (missing secrets).")
        return

    from pydrive2.auth import GoogleAuth
    from pydrive2.drive import GoogleDrive

    creds_file = OUTPUT_ROOT / "gdrive_service_account.json"
    creds_file.write_text(service_account, encoding="utf-8")

    gauth = GoogleAuth(settings={
        "client_config_backend": "service",
        "service_config": {
            "client_json_file_path": str(creds_file),
        },
    })
    gauth.ServiceAuth()
    drive = GoogleDrive(gauth)

    for file in OUTPUT_ROOT.rglob("*"):
        if not file.is_file():
            continue
        drive_file = drive.CreateFile({
            "title": file.name,
            "parents": [{"id": drive_folder}],
        })
        drive_file.SetContentFile(str(file))
        drive_file.Upload()
    print("Uploaded output files to Google Drive.")


def main() -> None:
    product_urls = discover_product_urls()
    print(f"Discovered {len(product_urls)} product links")
    products = scrape_products(product_urls)
    write_outputs(products)
    maybe_upload_to_drive()


if __name__ == "__main__":
    main()
