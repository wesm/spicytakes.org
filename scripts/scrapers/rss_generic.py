#!/usr/bin/env python3
"""
Generic RSS feed scraper for Spicy Takes platform.
Scrapes blogs that provide standard RSS feeds (like Hugo-powered blogs).
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class RssGenericScraper(BaseScraper):
    """Scraper for blogs with standard RSS feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "rss_generic":
            raise ValueError(f"Blog {blog_id} is not configured as rss_generic")

        self.feed_url = self.config["scraper"]["feedUrl"]
        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        # Optional URL filter to include only certain paths (e.g., "/blog/")
        self.url_filter = self.config["scraper"].get("urlFilter", "")
        # Optional archive page pattern for fetching older posts (e.g., "/posts/page/{page}/")
        self.archive_pattern = self.config["scraper"].get("archivePattern", "")
        # Starting page number for archive (some sites start at 2)
        self.archive_start_page = self.config["scraper"].get("archiveStartPage", 1)
        # Maximum archive pages to fetch
        self.max_archive_pages = self.config["scraper"].get("maxArchivePages", 10)

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def normalize_title(self, title: str, date_str: str | None = None) -> str:
        """Clean up titles that accidentally include trailing date suffixes."""
        if not title:
            return title

        normalized = " ".join(title.split())

        if not date_str:
            return normalized

        match = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", date_str)
        if not match:
            return normalized

        month = match.group(2)
        day = match.group(3)
        month_i = str(int(month))
        day_i = str(int(day))
        candidates = {
            f"{month}-{day}",
            f"{month_i}-{day_i}",
            f"{month_i}-{day}",
            f"{month}-{day_i}",
        }

        for suffix in sorted(candidates, key=len, reverse=True):
            if not normalized.endswith(suffix):
                continue
            suffix_start = len(normalized) - len(suffix)
            if suffix_start <= 0:
                continue
            # Only strip if the date is glued onto the end of the title text.
            # If there's whitespace or a separator before it, keep it.
            boundary_char = normalized[suffix_start - 1]
            if boundary_char.isspace() or boundary_char in "-–—|:/":
                continue
            prefix = normalized[:-len(suffix)].rstrip(" \t-–—|:/")
            # Keep a conservative floor so legitimate short titles that happen
            # to end in digits are unlikely to be truncated.
            if len(prefix) >= 8:
                return prefix

        return normalized

    def fetch_feed(self) -> list[dict]:
        """Fetch and parse posts from RSS feed. Returns list of post metadata."""
        try:
            response = requests.get(self.feed_url, timeout=30, headers=self.headers)
            response.raise_for_status()

            # Parse RSS feed
            root = ET.fromstring(response.content)

            posts = []
            # RSS items are in channel/item
            channel = root.find("channel")
            if channel is None:
                print("  Warning: No channel element found in RSS")
                return []

            for item in channel.findall("item"):
                title_elem = item.find("title")
                link_elem = item.find("link")
                pub_date_elem = item.find("pubDate")
                description_elem = item.find("description")

                raw_title = title_elem.text if title_elem is not None else "Untitled"
                url = link_elem.text if link_elem is not None else ""

                # Skip if URL doesn't match filter
                if self.url_filter and self.url_filter not in url:
                    continue

                # Make URL absolute if needed
                if url.startswith("/"):
                    url = self.base_url + url

                # Parse pubDate (RFC 2822 format: "Mon, 13 Jan 2026 00:00:00 +0000")
                pub_date = None
                if pub_date_elem is not None and pub_date_elem.text:
                    pub_date = self.parse_rfc2822_date(pub_date_elem.text)

                title = self.normalize_title(raw_title, pub_date)

                # Description is usually a summary, not full content
                description = ""
                if description_elem is not None and description_elem.text:
                    description = description_elem.text

                posts.append({
                    "title": title,
                    "url": url,
                    "pub_date": pub_date,
                    "description": description
                })

            return posts
        except Exception as e:
            print(f"  Error fetching feed: {e}")
            return []

    def fetch_archive_pages(self) -> list[dict]:
        """Fetch posts from paginated archive pages."""
        if not self.archive_pattern:
            return []

        all_posts = []
        page = self.archive_start_page
        max_page = self.archive_start_page + self.max_archive_pages - 1

        while page <= max_page:
            url = self.base_url + self.archive_pattern.format(page=page)
            print(f"  Fetching archive page {page}...")

            try:
                response = requests.get(url, timeout=30, headers=self.headers)
                if response.status_code == 404:
                    # No more pages
                    break
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")

                # Find all article links - look for links containing the url_filter
                page_posts = []
                for link in soup.find_all("a", href=True):
                    href = link.get("href", "")
                    title = link.get_text(strip=True)
                    title_lower = title.lower()

                    # Skip non-blog links
                    if self.url_filter and self.url_filter not in href:
                        continue
                    # Skip archive/pagination navigation links
                    if title_lower in {"previous page", "next page"}:
                        continue
                    if re.search(r"/page/\d+/?$", href.rstrip("/")):
                        continue
                    # Skip short titles (likely navigation)
                    if len(title) < 10:
                        continue
                    # Skip duplicate entries (some themes have multiple links)
                    if href.startswith("/"):
                        full_url = self.base_url + href
                    else:
                        full_url = href

                    # Check if we already have this post
                    if any(p["url"] == full_url for p in all_posts + page_posts):
                        continue

                    page_posts.append({
                        "title": title,
                        "url": full_url,
                        "pub_date": None,  # Will extract from page
                        "description": ""
                    })

                if not page_posts:
                    # No posts found on this page, stop
                    break

                all_posts.extend(page_posts)
                page += 1
                time.sleep(REQUEST_DELAY)

            except Exception as e:
                print(f"  Error fetching archive page {page}: {e}")
                break

        return all_posts

    def parse_rfc2822_date(self, date_str: str) -> str | None:
        """Parse RFC 2822 date to YYYY-MM-DD format."""
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(date_str)
            return dt.strftime("%Y-%m-%d")
        except Exception:
            # Try simpler parsing
            match = re.search(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", date_str)
            if match:
                day, month_abbr, year = match.groups()
                months = {
                    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
                    "may": "05", "jun": "06", "jul": "07", "aug": "08",
                    "sep": "09", "oct": "10", "nov": "11", "dec": "12"
                }
                month = months.get(month_abbr.lower(), "01")
                return f"{year}-{month}-{int(day):02d}"
            return None

    def extract_slug_from_url(self, url: str) -> str:
        """Extract slug from URL like https://ssp.sh/blog/some-post/"""
        # Remove trailing slash and get last path segment
        path = url.rstrip("/")
        slug_match = re.search(r"/([^/]+)$", path)
        return slug_match.group(1) if slug_match else "unknown"

    def fetch_post_page(self, url: str) -> tuple[str | None, str | None]:
        """Fetch a single post page and extract HTML content and date.

        Returns tuple of (content_html, date_str).
        """
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            # Use response.content (bytes) to let BeautifulSoup
            # handle encoding detection and avoid double-encoding
            soup = BeautifulSoup(response.content, "html.parser")

            # Try to extract date from page
            date_str = None
            # Look for time element with datetime attribute
            time_elem = soup.find("time", datetime=True)
            if time_elem:
                dt = time_elem.get("datetime", "")
                match = re.match(r"(\d{4})-(\d{2})-(\d{2})", dt)
                if match:
                    date_str = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

            # Find main content - try various selectors
            content_elem = None

            # Try article first (common in Hugo themes)
            content_elem = soup.find("article")
            if not content_elem:
                content_elem = soup.find("main")
            if not content_elem:
                content_elem = soup.find("div", class_="content")
            if not content_elem:
                content_elem = soup.find("div", class_="post-content")
            if not content_elem:
                content_elem = soup.find("div", class_="article-content")
            if not content_elem:
                # Last resort
                content_elem = soup.find("body")

            if content_elem:
                return str(content_elem), date_str
            return None, date_str
        except Exception as e:
            print(f"  Error fetching post page {url}: {e}")
            return None, None

    def process_post(self, post_meta: dict, content_html: str) -> dict | None:
        """Process a post into structured format."""
        url = post_meta["url"]
        date_str = post_meta.get("pub_date")
        title = self.normalize_title(post_meta["title"], date_str)

        # Parse HTML and convert to markdown
        soup = BeautifulSoup(content_html, "html.parser")
        content = self.html_to_markdown(soup, self.base_url)

        if not content or len(content.strip()) < 50:
            print(f"  Warning: Very short content for {url}")

        slug = self.extract_slug_from_url(url)

        return {
            "title": title,
            "date": date_str,
            "url": url,
            "slug": slug,
            "content": content.strip(),
            "word_count": len(content.split())
        }

    def scrape(self) -> list[dict]:
        """Main scrape method."""
        print(f"Scraping {self.config['name']}...")
        print(f"Feed URL: {self.feed_url}")

        # Fetch from RSS feed
        print("\nFetching feed posts...")
        feed_posts = self.fetch_feed()
        print(f"  Found {len(feed_posts)} posts in feed")

        # Also fetch from archive pages if configured
        archive_posts = []
        if self.archive_pattern:
            print("\nFetching archive pages...")
            archive_posts = self.fetch_archive_pages()
            print(f"  Found {len(archive_posts)} posts in archive")

        # Merge posts, preferring feed data (has dates)
        all_post_metas = []
        seen_urls = set()

        # First add feed posts (they have dates from RSS)
        for post in feed_posts:
            all_post_metas.append(post)
            seen_urls.add(post["url"])

        # Then add archive posts not in feed
        for post in archive_posts:
            if post["url"] not in seen_urls:
                all_post_metas.append(post)
                seen_urls.add(post["url"])

        if not all_post_metas:
            print("No posts found")
            return []

        print(f"\nTotal unique posts: {len(all_post_metas)}")

        # Load existing index to avoid re-scraping
        existing_slugs = self.get_existing_slugs()

        # Process each post
        new_posts = []

        for i, post_meta in enumerate(all_post_metas):
            url = post_meta["url"]
            title = post_meta["title"]
            slug = self.extract_slug_from_url(url)

            if slug in existing_slugs:
                print(f"  Skipping {slug} (already scraped)")
                continue

            print(f"\n[{i+1}/{len(all_post_metas)}] Fetching: {title}")
            time.sleep(REQUEST_DELAY)

            content_html, page_date = self.fetch_post_page(url)
            if not content_html:
                print(f"  Warning: Could not fetch content for {url}")
                continue

            # Use date from RSS if available, otherwise from page
            if not post_meta.get("pub_date") and page_date:
                post_meta["pub_date"] = page_date

            post = self.process_post(post_meta, content_html)

            if post:
                # Create filename
                date_str = post.get("date")
                if date_str:
                    filename = f"{date_str}-{slug}.md"
                else:
                    filename = f"{slug}.md"

                post["filename"] = filename

                # Create frontmatter content
                escaped_title = post['title'].replace('"', '\\"')
                frontmatter = f"""---
title: "{escaped_title}"
date: {post['date'] or 'unknown'}
url: {post['url']}
slug: {post['slug']}
word_count: {post['word_count']}
---

{post['content']}
"""
                post["content"] = frontmatter

                self.save_post(post)
                new_posts.append(post)
                print(f"  Saved: {filename} ({post['word_count']} words)")

        # Update index with new posts
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])

        for post in new_posts:
            all_posts.append({
                "slug": post["slug"],
                "title": post["title"],
                "date": post["date"],
                "url": post["url"],
                "word_count": post["word_count"],
                "filename": post["filename"]
            })

        # Sort by date descending
        all_posts.sort(key=lambda p: p.get("date") or "", reverse=True)

        self.save_index(all_posts)
        print(f"\nDone! Scraped {len(new_posts)} new posts.")
        return all_posts


if __name__ == "__main__":
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=<blog_id> python scripts/scrapers/rss_generic.py")
        sys.exit(1)

    scraper = RssGenericScraper(blog_id)
    scraper.scrape()
