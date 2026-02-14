#!/usr/bin/env python3
"""
Historical scraper for DHH's pre-HEY-World content.

Collects posts from three sources:
1. Medium @dhh (Nov 2018 - Feb 2019, ~10 posts)
2. Signal v. Noise WordPress era (Sep 2015 - Feb 2021, ~170 posts)
3. dhh.dk personal blog (Jul 2001 - 2014, ~800 posts)

Posts are saved to blogs/dhh/posts/ alongside the HEY World posts.
The source_url field in posts_index.json enables correct linking
regardless of which source a post came from.

Usage: BLOG_ID=dhh python3 scripts/scrapers/dhh_historical.py
       BLOG_ID=dhh SOURCE=medium python3 scripts/scrapers/dhh_historical.py
       BLOG_ID=dhh SOURCE=svn python3 scripts/scrapers/dhh_historical.py
       BLOG_ID=dhh SOURCE=dhhdk python3 scripts/scrapers/dhh_historical.py
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests
from bs4 import BeautifulSoup, NavigableString

from base import BaseScraper

REQUEST_DELAY = 1.0
MAX_RETRIES = 3
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36"
    ),
}


def slugify(text: str) -> str:
    """Convert text to a URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def fetch_with_retry(url: str, retries: int = MAX_RETRIES) -> requests.Response | None:
    """Fetch URL with retry logic for intermittent failures."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, timeout=30, headers=HEADERS)
            if resp.status_code == 404 and attempt < retries - 1:
                wait = 2 ** attempt
                print(f"    Got 404, retrying in {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            if attempt < retries - 1:
                wait = 2 ** attempt
                print(f"    Error: {e}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"    Failed after {retries} attempts: {e}")
                return None
    return None


class DhhHistoricalScraper(BaseScraper):
    """Collects DHH's historical posts from multiple sources."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)
        self.new_posts = []

    def save_historical_post(
        self, title: str, date_str: str, url: str,
        slug: str, content: str
    ) -> bool:
        """Save a post if not already scraped. Returns True if saved."""
        if date_str:
            filename = f"{date_str}-{slug}.md"
        else:
            filename = f"{slug}.md"

        existing = self.get_existing_filenames()
        if filename in existing:
            return False

        word_count = len(content.split())
        escaped_title = title.replace('"', '\\"')
        frontmatter = (
            f'---\n'
            f'title: "{escaped_title}"\n'
            f'date: {date_str or "unknown"}\n'
            f'url: {url}\n'
            f'slug: {slug}\n'
            f'word_count: {word_count}\n'
            f'---\n\n'
            f'{content}\n'
        )

        post = {"filename": filename, "content": frontmatter}
        self.save_post(post)

        self.new_posts.append({
            "slug": slug,
            "title": title,
            "date": date_str,
            "url": url,
            "word_count": word_count,
            "filename": filename,
            "source_url": url,
        })
        print(f"  Saved: {filename} ({word_count} words)")
        return True

    def update_index(self):
        """Merge new posts into the existing index."""
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])
        existing_filenames = {p["filename"] for p in all_posts}

        for post in self.new_posts:
            if post["filename"] not in existing_filenames:
                all_posts.append(post)

        all_posts.sort(
            key=lambda p: p.get("date") or "", reverse=True
        )
        self.save_index(all_posts)

    # ── Medium (@dhh) ──────────────────────────────────────────

    def scrape_medium(self):
        """Scrape DHH's Medium posts via RSS feed."""
        print("\n" + "=" * 50)
        print("Source: Medium (@dhh)")
        print("=" * 50)

        feed_url = "https://medium.com/feed/@dhh"
        print(f"Fetching {feed_url}")
        resp = fetch_with_retry(feed_url)
        if not resp:
            print("Failed to fetch Medium feed")
            return

        root = ET.fromstring(resp.content)
        channel = root.find("channel")
        if channel is None:
            print("No channel in feed")
            return

        items = channel.findall("item")
        print(f"Found {len(items)} posts")

        count = 0
        for item in items:
            title = item.findtext("title", "Untitled")
            link = item.findtext("link", "")
            pub_date_raw = item.findtext("pubDate", "")

            # Parse RSS date: "Mon, 11 Feb 2019 15:51:56 GMT"
            date_str = None
            if pub_date_raw:
                try:
                    dt = datetime.strptime(
                        pub_date_raw, "%a, %d %b %Y %H:%M:%S %Z"
                    )
                    date_str = dt.strftime("%Y-%m-%d")
                except ValueError:
                    pass

            # Full HTML in content:encoded
            content_html = ""
            for child in item:
                if child.tag.endswith("}encoded") or child.tag == "content:encoded":
                    content_html = child.text or ""
                    break

            if not content_html:
                print(f"  No content for: {title}")
                continue

            # Extract slug from Medium URL
            slug_match = re.search(r"/([a-z0-9-]+)-([a-f0-9]+)(?:\?|$)", link)
            if slug_match:
                slug = slug_match.group(1)
            else:
                slug = slugify(title)

            soup = BeautifulSoup(content_html, "html.parser")
            content = self.html_to_markdown(soup)

            if self.save_historical_post(
                title, date_str, link, slug, content
            ):
                count += 1

        print(f"\nMedium: saved {count} new posts")

    # ── Signal v. Noise (WordPress era) ────────────────────────

    def scrape_svn(self):
        """Scrape DHH's posts from Signal v. Noise WordPress."""
        print("\n" + "=" * 50)
        print("Source: Signal v. Noise (WordPress, 2015-2021)")
        print("=" * 50)

        base = "https://signalvnoise.com"
        post_metas = []

        # Fetch author listing pages (1-17)
        for page_num in range(1, 25):
            if page_num == 1:
                url = f"{base}/svn3/author/dhh/"
            else:
                url = f"{base}/svn3/author/dhh/page/{page_num}/"

            print(f"  Fetching listing page {page_num}: {url}")
            resp = fetch_with_retry(url)
            if not resp:
                print(f"    Page {page_num} failed, stopping")
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            entries = self._parse_svn_listing(soup, base)
            if not entries:
                print(f"    No entries on page {page_num}, stopping")
                break

            post_metas.extend(entries)
            print(f"    Found {len(entries)} posts")
            time.sleep(REQUEST_DELAY)

        print(f"\nFound {len(post_metas)} total SvN posts")

        # Dedup by URL
        seen = set()
        unique_metas = []
        for m in post_metas:
            if m["url"] not in seen:
                seen.add(m["url"])
                unique_metas.append(m)
        post_metas = unique_metas

        # Fetch each post for full content
        existing = self.get_existing_filenames()
        count = 0
        for i, meta in enumerate(post_metas):
            slug = meta["url"].rstrip("/").split("/")[-1]
            date_str = meta.get("date")
            if date_str:
                filename = f"{date_str}-{slug}.md"
            else:
                filename = f"{slug}.md"

            if filename in existing:
                continue

            print(f"\n[{i+1}/{len(post_metas)}] {meta['title']}")
            time.sleep(REQUEST_DELAY)

            resp = fetch_with_retry(meta["url"])
            if not resp:
                continue

            soup = BeautifulSoup(resp.text, "html.parser")
            content_elem = (
                soup.find("div", class_="entry-content")
                or soup.find("article")
                or soup.find("main")
            )
            if not content_elem:
                print("    No content found")
                continue

            content = self.html_to_markdown(
                content_elem, base
            )

            if self.save_historical_post(
                meta["title"], date_str, meta["url"],
                slug, content
            ):
                count += 1
                # Re-read existing filenames after save
                existing.add(filename)

        print(f"\nSvN: saved {count} new posts")

    def _parse_svn_listing(
        self, soup: BeautifulSoup, base: str
    ) -> list[dict]:
        """Parse a SvN author listing page for post metadata."""
        entries = []
        # Posts are in article or h2 elements with links
        for heading in soup.find_all("h2"):
            link = heading.find("a")
            if not link:
                continue
            href = link.get("href", "")
            if "/svn3/" not in href:
                continue

            title = link.get_text(strip=True)
            url = href if href.startswith("http") else base + href

            # Find date near this heading
            date_str = None
            parent = heading.parent
            if parent:
                date_text = parent.get_text()
                date_match = re.search(
                    r"posted on\s+(\w+ \d+, \d{4})", date_text
                )
                if date_match:
                    try:
                        dt = datetime.strptime(
                            date_match.group(1), "%B %d, %Y"
                        )
                        date_str = dt.strftime("%Y-%m-%d")
                    except ValueError:
                        pass

            entries.append({
                "title": title,
                "url": url,
                "date": date_str,
            })
        return entries

    # ── dhh.dk personal blog ───────────────────────────────────

    def scrape_dhhdk(self):
        """Scrape all dhh.dk content across all archive systems."""
        print("\n" + "=" * 50)
        print("Source: dhh.dk (Loud Thinking, 2001-2014)")
        print("=" * 50)

        self._scrape_dhhdk_legacy_archives()
        self._scrape_dhhdk_arc_archives()
        self._scrape_dhhdk_posts()
        self._scrape_dhhdk_essays()

    def _scrape_dhhdk_legacy_archives(self):
        """Scrape /archives/ monthly pages (Jul 2001 - Jul 2002)."""
        print("\n--- dhh.dk /archives/ (2001-2002) ---")

        months = [
            "072001", "082001", "092001", "102001",
            "112001", "122001", "012002", "022002",
            "032002", "042002", "052002", "062002",
            "072002",
        ]

        count = 0
        for month_code in months:
            url = f"https://dhh.dk/archives/archive-{month_code}.html"
            # Parse year from code: MMYYYY
            mm = month_code[:2]
            yyyy = month_code[2:]
            print(f"  Fetching {yyyy}-{mm}: {url}")

            resp = fetch_with_retry(url)
            if not resp:
                continue

            soup = BeautifulSoup(resp.text, "html.parser")
            posts = self._parse_legacy_archive_page(
                soup, int(yyyy), int(mm)
            )
            for post in posts:
                if self.save_historical_post(**post):
                    count += 1

            time.sleep(REQUEST_DELAY)

        print(f"\n  /archives/: saved {count} new posts")

    def _parse_legacy_archive_page(
        self, soup: BeautifulSoup, year: int, month: int
    ) -> list[dict]:
        """Parse a /archives/ monthly page into posts.

        Structure: <h2><a href="...">Title</a></h2>
        followed by date line and content, until next <h2>.
        """
        posts = []
        headings = soup.find_all("h2")

        for h2 in headings:
            link = h2.find("a")
            if not link:
                continue
            href = link.get("href", "")
            if "/archives/" not in href:
                continue

            title = link.get_text(strip=True)
            post_url = f"https://dhh.dk{href}" if href.startswith("/") else href

            # Collect content between this h2 and the next
            content_parts = []
            date_str = None
            sibling = h2.next_sibling

            while sibling:
                if hasattr(sibling, "name") and sibling.name == "h2":
                    break
                if isinstance(sibling, NavigableString):
                    text = str(sibling).strip()
                    if text:
                        # Check for date pattern
                        dm = re.search(
                            r"(\w+day),?\s+(\w+)\s+(\d+),?\s+(\d{4})\s*@?\s*(\d+:\d+)?",
                            text
                        )
                        if dm and not date_str:
                            month_name = dm.group(2)
                            day = dm.group(3)
                            yr = dm.group(4)
                            try:
                                dt = datetime.strptime(
                                    f"{month_name} {day} {yr}",
                                    "%B %d %Y"
                                )
                                date_str = dt.strftime("%Y-%m-%d")
                            except ValueError:
                                pass
                        elif text and not text.startswith("challenges") and "comments" not in text.lower():
                            content_parts.append(text)
                elif hasattr(sibling, "name"):
                    tag = sibling.name
                    if tag in ("p", "blockquote", "pre", "ul", "ol"):
                        md = self.html_to_markdown(sibling, "https://dhh.dk")
                        if md.strip():
                            content_parts.append(md.strip())
                    elif tag == "a" and "comments" in sibling.get_text(strip=True).lower():
                        pass  # Skip comments link
                    elif tag not in ("br", "hr", "script", "style"):
                        text = sibling.get_text(strip=True)
                        # Check for date in element text too
                        if text and not date_str:
                            dm = re.search(
                                r"(\w+day),?\s+(\w+)\s+(\d+),?\s+(\d{4})",
                                text
                            )
                            if dm:
                                try:
                                    dt = datetime.strptime(
                                        f"{dm.group(2)} {dm.group(3)} {dm.group(4)}",
                                        "%B %d %Y"
                                    )
                                    date_str = dt.strftime("%Y-%m-%d")
                                except ValueError:
                                    pass

                sibling = sibling.next_sibling

            if not date_str:
                date_str = f"{year:04d}-{month:02d}-01"

            content = "\n\n".join(content_parts)
            slug_match = re.search(r"/(\d+)\.html", href)
            slug = slugify(title) if not slug_match else f"loud-thinking-{slug_match.group(1)}"

            if title and (content or len(title) > 10):
                posts.append({
                    "title": title,
                    "date_str": date_str,
                    "url": post_url,
                    "slug": slug,
                    "content": content if content else title,
                })

        return posts

    def _scrape_dhhdk_arc_archives(self):
        """Scrape /arc/ monthly pages (Aug 2002 - Nov 2006)."""
        print("\n--- dhh.dk /arc/ (2002-2006) ---")

        # Build list of all YYYY_MM archive pages
        arc_months = []
        # 2002: Aug-Dec
        for m in range(8, 13):
            arc_months.append((2002, m))
        # 2003-2005: all months
        for y in range(2003, 2006):
            for m in range(1, 13):
                arc_months.append((y, m))
        # 2006: Jan-Jun, Aug-Nov (missing Jul, Dec)
        for m in [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]:
            arc_months.append((2006, m))

        count = 0
        for year, month in arc_months:
            url = f"https://dhh.dk/arc/{year}_{month:02d}.html"
            print(f"  Fetching {year}-{month:02d}: {url}")

            resp = fetch_with_retry(url)
            if not resp:
                continue

            soup = BeautifulSoup(resp.text, "html.parser")
            posts = self._parse_arc_archive_page(
                soup, year, month
            )
            for post in posts:
                if self.save_historical_post(**post):
                    count += 1

            time.sleep(REQUEST_DELAY)

        print(f"\n  /arc/: saved {count} new posts")

    def _parse_arc_archive_page(
        self, soup: BeautifulSoup, year: int, month: int
    ) -> list[dict]:
        """Parse a /arc/ monthly page into posts.

        Dates on these pages lack year, so we use the archive page's year.
        """
        posts = []
        headings = soup.find_all("h2")

        for h2 in headings:
            link = h2.find("a")
            if not link:
                continue
            href = link.get("href", "")
            if "/arc/" not in href:
                continue

            title = link.get_text(strip=True)
            post_url = f"https://dhh.dk{href}" if href.startswith("/") else href

            content_parts = []
            date_str = None
            day_num = 1
            sibling = h2.next_sibling

            while sibling:
                if hasattr(sibling, "name") and sibling.name == "h2":
                    break
                if isinstance(sibling, NavigableString):
                    text = str(sibling).strip()
                    if text:
                        # Date pattern: "January 30, 22:27" (no year)
                        dm = re.search(
                            r"(\w+)\s+(\d+),?\s+\d+:\d+", text
                        )
                        if dm and not date_str:
                            month_name = dm.group(1)
                            day = dm.group(2)
                            try:
                                dt = datetime.strptime(
                                    f"{month_name} {day} {year}",
                                    "%B %d %Y"
                                )
                                date_str = dt.strftime("%Y-%m-%d")
                                day_num = int(day)
                            except ValueError:
                                pass
                        elif (
                            text
                            and "comments" not in text.lower()
                            and "challenge" not in text.lower()
                        ):
                            content_parts.append(text)
                elif hasattr(sibling, "name"):
                    tag = sibling.name
                    if tag in ("p", "blockquote", "pre", "ul", "ol", "div"):
                        md = self.html_to_markdown(
                            sibling, "https://dhh.dk"
                        )
                        if md.strip():
                            content_parts.append(md.strip())
                    elif tag == "a" and "comment" in sibling.get_text(strip=True).lower():
                        pass

                sibling = sibling.next_sibling

            if not date_str:
                date_str = f"{year:04d}-{month:02d}-{day_num:02d}"

            content = "\n\n".join(content_parts)
            slug_match = re.search(r"/(\d+)\.html", href)
            slug = slugify(title) if not slug_match else f"loud-thinking-{slug_match.group(1)}"

            if title and (content or len(title) > 10):
                posts.append({
                    "title": title,
                    "date_str": date_str,
                    "url": post_url,
                    "slug": slug,
                    "content": content if content else title,
                })

        return posts

    def _scrape_dhhdk_posts(self):
        """Scrape /posts/ pages (2007-2012, 44 posts)."""
        print("\n--- dhh.dk /posts/ (2007-2012) ---")

        # Get post list from archives page
        url = "https://dhh.dk/posts/archives"
        print(f"  Fetching archive index: {url}")
        resp = fetch_with_retry(url)
        if not resp:
            print("  Failed to fetch archives page")
            return

        soup = BeautifulSoup(resp.text, "html.parser")
        post_links = []

        for link in soup.find_all("a", href=True):
            href = link.get("href", "")
            if "/posts/" in href and href != "/posts/archives":
                title = link.get_text(strip=True)
                if title:
                    full_url = (
                        f"https://dhh.dk{href}"
                        if href.startswith("/")
                        else href
                    )
                    post_links.append({
                        "title": title,
                        "url": full_url,
                    })

        # Dedup
        seen = set()
        unique_links = []
        for pl in post_links:
            if pl["url"] not in seen:
                seen.add(pl["url"])
                unique_links.append(pl)
        post_links = unique_links

        print(f"  Found {len(post_links)} post links")

        count = 0
        existing = self.get_existing_filenames()
        for i, meta in enumerate(post_links):
            # Extract slug from URL
            slug_match = re.search(r"/posts/\d+-(.+)$", meta["url"])
            slug = slug_match.group(1) if slug_match else slugify(meta["title"])

            # Check if already exists (approximate check)
            skip = False
            for fn in existing:
                if slug in fn:
                    skip = True
                    break
            if skip:
                continue

            print(f"\n  [{i+1}/{len(post_links)}] {meta['title']}")
            time.sleep(REQUEST_DELAY)

            resp = fetch_with_retry(meta["url"])
            if not resp:
                continue

            page_soup = BeautifulSoup(resp.text, "html.parser")

            # Extract date from byline
            date_str = None
            text = page_soup.get_text()
            date_match = re.search(
                r"on\s+(\w+\s+\d+,?\s+\d{4})", text
            )
            if date_match:
                try:
                    dt = datetime.strptime(
                        date_match.group(1).replace(",", ""),
                        "%B %d %Y"
                    )
                    date_str = dt.strftime("%Y-%m-%d")
                except ValueError:
                    pass

            # Extract content - find main content area
            content_elem = (
                page_soup.find("div", class_="entry-content")
                or page_soup.find("article")
                or page_soup.find("div", id="content")
                or page_soup.find("body")
            )

            if content_elem:
                content = self.html_to_markdown(
                    content_elem, "https://dhh.dk"
                )
            else:
                content = ""

            if not content or len(content.strip()) < 20:
                print("    Skipping (no content)")
                continue

            if self.save_historical_post(
                meta["title"], date_str, meta["url"],
                slug, content
            ):
                count += 1
                existing.add(f"{date_str}-{slug}.md" if date_str else f"{slug}.md")

        print(f"\n  /posts/: saved {count} new posts")

    def _scrape_dhhdk_essays(self):
        """Scrape technical essays from /archive.html (2012-2014)."""
        print("\n--- dhh.dk essays (2012-2014) ---")

        url = "https://dhh.dk/archive.html"
        print(f"  Fetching essay index: {url}")
        resp = fetch_with_retry(url)
        if not resp:
            print("  Failed to fetch archive page")
            return

        soup = BeautifulSoup(resp.text, "html.parser")
        essay_links = []

        for link in soup.find_all("a", href=True):
            href = link.get("href", "")
            # Essays are at /YYYY/slug.html
            if re.match(r"/?20\d{2}/", href):
                title = link.get_text(strip=True)
                if title:
                    full_url = (
                        f"https://dhh.dk{href}"
                        if href.startswith("/")
                        else f"https://dhh.dk/{href}"
                    )
                    essay_links.append({
                        "title": title,
                        "url": full_url,
                    })

        # Dedup
        seen = set()
        unique_links = []
        for el in essay_links:
            if el["url"] not in seen:
                seen.add(el["url"])
                unique_links.append(el)
        essay_links = unique_links

        print(f"  Found {len(essay_links)} essays")

        count = 0
        existing = self.get_existing_filenames()
        for i, meta in enumerate(essay_links):
            # Extract slug and year from URL
            match = re.search(r"/(\d{4})/(.+?)\.html", meta["url"])
            if match:
                year = match.group(1)
                slug = match.group(2)
            else:
                slug = slugify(meta["title"])
                year = None

            # Check if already exists
            skip = False
            for fn in existing:
                if slug in fn:
                    skip = True
                    break
            if skip:
                continue

            print(f"\n  [{i+1}/{len(essay_links)}] {meta['title']}")
            time.sleep(REQUEST_DELAY)

            resp = fetch_with_retry(meta["url"])
            if not resp:
                continue

            page_soup = BeautifulSoup(resp.text, "html.parser")

            # Extract date
            date_str = None
            text = page_soup.get_text()
            date_match = re.search(
                r"on\s+(\w+\s+\d+,?\s+\d{4})", text
            )
            if date_match:
                try:
                    dt = datetime.strptime(
                        date_match.group(1).replace(",", ""),
                        "%B %d %Y"
                    )
                    date_str = dt.strftime("%Y-%m-%d")
                except ValueError:
                    pass

            if not date_str and year:
                date_str = f"{year}-01-01"

            content_elem = (
                page_soup.find("div", class_="entry-content")
                or page_soup.find("article")
                or page_soup.find("div", id="content")
                or page_soup.find("body")
            )

            if content_elem:
                content = self.html_to_markdown(
                    content_elem, "https://dhh.dk"
                )
            else:
                content = ""

            if not content or len(content.strip()) < 20:
                print("    Skipping (no content)")
                continue

            if self.save_historical_post(
                meta["title"], date_str, meta["url"],
                slug, content
            ):
                count += 1
                fn = f"{date_str}-{slug}.md" if date_str else f"{slug}.md"
                existing.add(fn)

        print(f"\n  Essays: saved {count} new posts")

    # ── Main entry ─────────────────────────────────────────────

    def scrape(self) -> list[dict]:
        """Run all historical scrapers."""
        source = os.environ.get("SOURCE", "all").lower()

        if source in ("all", "medium"):
            self.scrape_medium()
        if source in ("all", "svn"):
            self.scrape_svn()
        if source in ("all", "dhhdk"):
            self.scrape_dhhdk()

        self.update_index()

        total = len(self.new_posts)
        print(f"\n{'=' * 50}")
        print(f"Total: saved {total} new historical posts")
        print(f"{'=' * 50}")

        existing = self.load_existing_index()
        return existing.get("posts", [])


if __name__ == "__main__":
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=dhh python3 scripts/scrapers/dhh_historical.py")
        sys.exit(1)

    scraper = DhhHistoricalScraper(blog_id)
    scraper.run()
