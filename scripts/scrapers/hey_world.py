#!/usr/bin/env python3
"""
HEY World Atom feed scraper for Spicy Takes platform.
Scrapes blogs hosted on world.hey.com that provide paginated Atom feeds.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.0


class HeyWorldScraper(BaseScraper):
    """Scraper for HEY World blogs with paginated Atom feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "hey_world":
            raise ValueError(
                f"Blog {blog_id} is not configured as hey_world"
            )

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.feed_url = self.config["scraper"]["feedUrl"]
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36"
            ),
        }

    def fetch_all_feed_pages(self) -> list[dict]:
        """Fetch all pages of the Atom feed, following next links."""
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        all_entries = []
        url = self.feed_url
        page = 0

        while url:
            page += 1
            print(f"  Fetching feed page {page}: {url}")

            response = requests.get(
                url, timeout=30, headers=self.headers
            )
            response.raise_for_status()
            root = ET.fromstring(response.content)

            for entry in root.findall("atom:entry", ns):
                parsed = self._parse_entry(entry, ns)
                if parsed:
                    all_entries.append(parsed)

            # Follow <link rel="next"> for pagination
            url = None
            for link in root.findall("atom:link", ns):
                if link.get("rel") == "next":
                    url = link.get("href", "")
                    break

            if url:
                time.sleep(REQUEST_DELAY)

        return all_entries

    def _parse_entry(self, entry, ns: dict) -> dict | None:
        """Parse a single Atom entry into post metadata."""
        title_elem = entry.find("atom:title", ns)
        published_elem = entry.find("atom:published", ns)
        content_elem = entry.find("atom:content", ns)

        title = "Untitled"
        if title_elem is not None and title_elem.text:
            title = title_elem.text

        # Get URL from link elements (prefer alternate)
        url = ""
        for link in entry.findall("atom:link", ns):
            rel = link.get("rel", "alternate")
            if rel == "alternate":
                url = link.get("href", "")
                break
        if not url:
            first_link = entry.find("atom:link", ns)
            if first_link is not None:
                url = first_link.get("href", "")

        if not url:
            return None

        pub_date = None
        if published_elem is not None and published_elem.text:
            pub_date = published_elem.text[:10]

        content_html = ""
        if content_elem is not None and content_elem.text:
            content_html = content_elem.text

        return {
            "title": title,
            "url": url,
            "pub_date": pub_date,
            "content_html": content_html,
        }

    def extract_slug(self, url: str) -> str:
        """Extract slug from HEY World URL.

        e.g. https://world.hey.com/dhh/clankers-with-claws-9f86fa71
        -> clankers-with-claws-9f86fa71
        """
        path = url.rstrip("/").split("/")[-1]
        return path if path else "unknown"

    def scrape(self) -> list[dict]:
        """Main scrape method."""
        print(f"Scraping {self.config['name']}...")
        print(f"Feed URL: {self.feed_url}")

        print("\nFetching all feed pages...")
        feed_entries = self.fetch_all_feed_pages()
        print(f"  Found {len(feed_entries)} total entries")

        existing_filenames = self.get_existing_filenames()
        new_posts = []

        for i, entry in enumerate(feed_entries):
            url = entry["url"]
            title = entry["title"]
            date_str = entry.get("pub_date")
            slug = self.extract_slug(url)

            if date_str:
                filename = f"{date_str}-{slug}.md"
            else:
                filename = f"{slug}.md"

            if filename in existing_filenames:
                continue

            print(f"\n[{i+1}/{len(feed_entries)}] Processing: {title}")

            content_html = entry.get("content_html", "")
            if not content_html:
                print(f"  Warning: No content for {url}, skipping")
                continue

            soup = BeautifulSoup(content_html, "html.parser")
            content = self.html_to_markdown(soup, self.base_url)

            if not content or len(content.strip()) < 50:
                print(f"  Warning: Very short content for {url}")

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

            post = {
                "filename": filename,
                "content": frontmatter,
                "title": title,
                "date": date_str,
                "url": url,
                "slug": slug,
                "word_count": word_count,
            }

            self.save_post(post)
            new_posts.append(post)
            print(f"  Saved: {filename} ({word_count} words)")

        # Update index
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])

        for post in new_posts:
            all_posts.append({
                "slug": post["slug"],
                "title": post["title"],
                "date": post["date"],
                "url": post["url"],
                "word_count": post["word_count"],
                "filename": post["filename"],
            })

        all_posts.sort(
            key=lambda p: p.get("date") or "", reverse=True
        )
        self.save_index(all_posts)

        print(f"\nDone! Scraped {len(new_posts)} new posts.")
        return all_posts


if __name__ == "__main__":
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print(
            "Usage: BLOG_ID=dhh python scripts/scrapers/hey_world.py"
        )
        sys.exit(1)

    scraper = HeyWorldScraper(blog_id)
    scraper.scrape()
