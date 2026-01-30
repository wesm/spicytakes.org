#!/usr/bin/env python3
"""
Medium scraper for Spicy Takes platform.
Scrapes Medium blogs using the RSS feed.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.0


class MediumScraper(BaseScraper):
    """Scraper for Medium blogs via RSS feed."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)
        self.feed_url = self.config["scraper"].get("mediumFeedUrl")
        if not self.feed_url:
            raise ValueError(f"Blog {blog_id} has no mediumFeedUrl in scraper config")

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_posts_from_feed(self) -> list[dict]:
        """Fetch posts from Medium RSS feed."""
        print(f"  Fetching RSS feed: {self.feed_url}")
        try:
            response = requests.get(self.feed_url, timeout=30, headers=self.headers)
            response.raise_for_status()
        except Exception as e:
            print(f"  Error fetching feed: {e}")
            return []

        root = ET.fromstring(response.content)
        ns = {"content": "http://purl.org/rss/1.0/modules/content/"}

        channel = root.find("channel")
        if channel is None:
            print("  No channel found in feed")
            return []

        items = channel.findall("item")
        print(f"  Found {len(items)} items in feed")

        posts = []
        for item in items:
            title_elem = item.find("title")
            link_elem = item.find("link")
            pub_date_elem = item.find("pubDate")
            content_elem = item.find("content:encoded", ns)

            title = title_elem.text if title_elem is not None else "Untitled"
            url = link_elem.text if link_elem is not None else ""

            # Parse date: "Sat, 18 Jan 2025 20:42:07 GMT"
            pub_date = None
            if pub_date_elem is not None and pub_date_elem.text:
                try:
                    dt = parsedate_to_datetime(pub_date_elem.text.strip())
                    pub_date = dt.strftime("%Y-%m-%d")
                except (ValueError, TypeError):
                    pass

            content_html = ""
            if content_elem is not None and content_elem.text:
                content_html = content_elem.text

            posts.append({
                "title": title,
                "url": url,
                "pub_date": pub_date,
                "content_html": content_html,
            })

        return posts

    def make_slug(self, url: str) -> str:
        """Extract slug from Medium URL, keeping the unique ID suffix."""
        # Medium URLs: https://medium.com/@user/title-slug-abc123def456?source=rss-...
        from urllib.parse import urlparse
        path = urlparse(url).path.rstrip("/").split("/")[-1]
        return path

    def make_filename(self, post: dict) -> str:
        """Create markdown filename from post metadata."""
        slug = self.make_slug(post["url"])
        if post.get("pub_date"):
            return f"{post['pub_date']}-{slug}.md"
        return f"{slug}.md"

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post["title"].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if post.get("pub_date"):
            frontmatter.append(f"date: {post['pub_date']}")
        frontmatter.extend([
            f"url: {post['url']}",
            "source: medium",
            f"word_count: {post.get('word_count', 0)}",
            "---",
            "",
        ])
        return "\n".join(frontmatter) + "\n" + post.get("markdown", "")

    def scrape(self) -> list[dict]:
        """Scrape posts from Medium RSS feed."""
        print("Fetching posts from Medium RSS feed...")
        feed_posts = self.fetch_posts_from_feed()
        print(f"Found {len(feed_posts)} posts in feed")

        existing_filenames = self.get_existing_filenames()
        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        posts_to_scrape = []
        for fp in feed_posts:
            filename = self.make_filename(fp)
            if filename not in existing_filenames:
                fp["filename"] = filename
                posts_to_scrape.append(fp)

        if not posts_to_scrape:
            print("All posts already scraped!")
            return posts

        print(f"Scraping {len(posts_to_scrape)} new posts...")

        for i, post in enumerate(posts_to_scrape):
            print(f"[{i+1}/{len(posts_to_scrape)}] {post['title'][:60]}...")

            if post.get("content_html"):
                soup = BeautifulSoup(post["content_html"], "html.parser")
                markdown = self.html_to_markdown(soup)
                post["markdown"] = markdown
                post["word_count"] = len(markdown.split())
            else:
                post["markdown"] = ""
                post["word_count"] = 0

            post["content"] = self.make_post_content(post)

            filepath = self.save_post(post)
            print(f"  Saved: {filepath}")

            index_entry = {
                "filename": post["filename"],
                "title": post["title"],
                "url": post["url"],
                "pub_date": post.get("pub_date"),
                "word_count": post.get("word_count", 0),
                "source": "medium",
            }
            posts.append(index_entry)

            time.sleep(REQUEST_DELAY)

        self.save_index(posts)
        return posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=steveyegge python medium.py")
        sys.exit(1)

    scraper = MediumScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
