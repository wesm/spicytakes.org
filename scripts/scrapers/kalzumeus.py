#!/usr/bin/env python3
"""
Kalzumeus (Patrick McKenzie / patio11) scraper for Spicy Takes.
Scrapes blog posts from www.kalzumeus.com/archive/.
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.0

MONTHS = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "may": "05", "jun": "06", "jul": "07", "aug": "08",
    "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}


class KalzumeusScraper(BaseScraper):
    """Scraper for kalzumeus.com blog posts."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "kalzumeus":
            raise ValueError(
                f"Blog {blog_id} is not configured as "
                "kalzumeus type"
            )

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.archive_url = self.config["scraper"]["archiveUrl"]

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36"
            )
        }

    def fetch_page(self, url: str) -> BeautifulSoup | None:
        """Fetch a page and return parsed BeautifulSoup."""
        try:
            response = requests.get(
                url, timeout=30, headers=self.headers
            )
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def parse_archive_date(self, text: str) -> str | None:
        """Parse 'DD Mon YYYY' date to YYYY-MM-DD."""
        text = text.strip()
        match = re.match(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", text)
        if not match:
            return None
        day, month_abbr, year = match.groups()
        month = MONTHS.get(month_abbr.lower())
        if not month:
            return None
        return f"{year}-{month}-{int(day):02d}"

    def extract_slug(self, href: str) -> str:
        """Extract slug from URL path."""
        path = href.rstrip("/")
        slug_match = re.search(r"/([^/]+)$", path)
        return slug_match.group(1) if slug_match else "unknown"

    def extract_date_from_url(self, href: str) -> str | None:
        """Extract date from URL like /YYYY/MM/DD/slug/."""
        match = re.match(
            r"/(\d{4})/(\d{1,2})/(\d{1,2})/", href
        )
        if match:
            year, month, day = match.groups()
            return (
                f"{year}-{int(month):02d}-{int(day):02d}"
            )
        return None

    def get_post_urls(self, soup: BeautifulSoup) -> list[dict]:
        """
        Parse all post entries from the archive page.
        Returns list of {url, slug, date, title, href}.
        """
        archive = soup.find("div", class_="page-archive")
        if not archive:
            print("  No page-archive div found")
            return []

        posts = []
        seen_slugs = set()

        for p_tag in archive.find_all("p"):
            a_tag = p_tag.find("a", class_="post-title-archive")
            if not a_tag:
                continue

            href = a_tag.get("href", "")
            title = a_tag.get_text(strip=True)
            if not href or not title:
                continue

            slug = self.extract_slug(href)
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)

            # Parse date from <small> tag or URL
            small_tag = p_tag.find("small")
            date_str = None
            if small_tag:
                date_str = self.parse_archive_date(
                    small_tag.get_text(strip=True)
                )
            if not date_str:
                date_str = self.extract_date_from_url(href)

            # Build full URL
            if href.startswith("/"):
                full_url = self.base_url + href
            else:
                full_url = href

            posts.append({
                "url": full_url,
                "href": href,
                "slug": slug,
                "date": date_str,
                "title": title,
            })

        return posts

    def fetch_post(self, post_info: dict) -> dict | None:
        """Fetch and parse a single blog post."""
        url = post_info["url"]
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Content is in <div class="post-content">
        content_div = soup.find("div", class_="post-content")
        if not content_div:
            print(f"  No post-content div: {url}")
            return None

        content = self.html_to_markdown(
            content_div, self.base_url
        )
        word_count = len(content.split())

        if word_count < 50:
            print(
                f"  Skipping (only {word_count} words): "
                f"{post_info['title']}"
            )
            return None

        # Try to get date from page if not from archive
        date_str = post_info.get("date")
        if not date_str:
            header = soup.find("div", class_="post-header")
            if header:
                muted = header.find("p", class_="text-muted")
                if muted:
                    text = muted.get_text(strip=True)
                    # Format: "February 10, 2025"
                    date_str = self.parse_long_date(text)

        return {
            "url": url,
            "slug": post_info["slug"],
            "title": post_info["title"],
            "date": date_str,
            "content": content,
            "word_count": word_count,
        }

    def parse_long_date(self, text: str) -> str | None:
        """Parse 'Month DD, YYYY' to YYYY-MM-DD."""
        long_months = {
            "january": "01", "february": "02",
            "march": "03", "april": "04",
            "may": "05", "june": "06",
            "july": "07", "august": "08",
            "september": "09", "october": "10",
            "november": "11", "december": "12",
        }
        match = re.match(
            r"(\w+)\s+(\d{1,2}),?\s+(\d{4})", text
        )
        if not match:
            return None
        month_name, day, year = match.groups()
        month = long_months.get(month_name.lower())
        if not month:
            return None
        return f"{year}-{month}-{int(day):02d}"

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post["title"].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
            f"date: {post['date']}",
            f"url: {post['url']}",
            f"slug: {post['slug']}",
            f"word_count: {post['word_count']}",
            "---",
            "",
        ]
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all blog posts."""
        print(f"Fetching archive from {self.archive_url}...")
        soup = self.fetch_page(self.archive_url)
        if not soup:
            print("Failed to fetch archive page")
            return []

        post_infos = self.get_post_urls(soup)
        print(f"Found {len(post_infos)} posts in archive")

        existing_slugs = self.get_existing_slugs()
        to_scrape = [
            p for p in post_infos
            if p["slug"] not in existing_slugs
        ]

        if not to_scrape:
            print("All posts already scraped!")
            existing = self.load_existing_index()
            return existing.get("posts", [])

        print(f"Scraping {len(to_scrape)} new posts...")

        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        for i, info in enumerate(to_scrape):
            title_preview = info["title"][:60]
            print(f"[{i+1}/{len(to_scrape)}] {title_preview}...")

            post = self.fetch_post(info)
            if post:
                date_str = post.get("date")
                if date_str:
                    filename = f"{date_str}-{post['slug']}.md"
                else:
                    filename = f"{post['slug']}.md"

                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                index_entry = {
                    k: v for k, v in post.items()
                    if k != "content"
                }
                posts.append(index_entry)

                if (i + 1) % 25 == 0:
                    self.save_index(posts)
                    print(f"  Index saved ({len(posts)} posts)")

            time.sleep(REQUEST_DELAY)

        self.save_index(posts)
        return posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=patio11 python kalzumeus.py")
        sys.exit(1)

    scraper = KalzumeusScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
