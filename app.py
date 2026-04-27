import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
import json
import time


BLOCKED_EXTENSIONS = {
    ".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a",
    ".mp4", ".mov", ".avi", ".wmv", ".mkv", ".webm",
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".css", ".js", ".json", ".xml", ".txt",
}


def is_external(url, base):
    return urlparse(url).netloc != urlparse(base).netloc


def is_legitimate_web_page(url):
    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"}:
        return False

    path = parsed.path.lower().rstrip("/")

    for ext in BLOCKED_EXTENSIONS:
        if path.endswith(ext):
            return False

    return True


def crawl_site(start_urls, max_links=10, retries=3, delay=3):
    external_links = {}
    internal_links = {}

    def crawl(url, base_url, visited):
        if len(visited) >= max_links:
            return

        url = urldefrag(url).url

        if not is_legitimate_web_page(url):
            print(f"Skipping non-page URL: {url}")
            return

        if url in visited:
            return

        visited.add(url)
        print(f"Crawling: {url}")

        soup = None

        for attempt in range(retries):
            try:
                response = requests.get(
                    url,
                    timeout=5,
                    headers={
                        "User-Agent": "Mozilla/5.0 (compatible; SimpleCrawler/1.0)"
                    }
                )
                response.raise_for_status()

                content_type = response.headers.get("Content-Type", "").lower()

                if "text/html" not in content_type:
                    print(f"Skipping non-HTML content: {url} ({content_type})")
                    return

                soup = BeautifulSoup(response.text, "html.parser")
                break

            except requests.exceptions.RequestException as e:
                print(f"Failed to crawl {url}: {e}")

                if attempt < retries - 1:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    return

        if soup is None:
            return

        for link in soup.find_all("a", href=True):
            href = urljoin(url, link.get("href"))
            href = urldefrag(href).url

            if not is_legitimate_web_page(href):
                continue

            if is_external(href, base_url):
                if href not in external_links:
                    external_links[href] = []
                external_links[href].append(url)
            else:
                if href not in visited:
                    if base_url not in internal_links:
                        internal_links[base_url] = []

                    internal_links[base_url].append(href)
                    crawl(href, base_url, visited)

    for start_url in start_urls:
        visited = set()
        crawl(start_url, start_url, visited)

    return external_links, internal_links


def save_links_as_json(external_links, internal_links, filename="links.json"):
    data = {
        "external_links": external_links,
        "internal_links": internal_links
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


start_urls = ["http://www.example.com"]

external_links, internal_links = crawl_site(start_urls)
save_links_as_json(external_links, internal_links)