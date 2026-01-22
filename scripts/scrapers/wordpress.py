#!/usr/bin/env python3
"""
WordPress scraper for Spicy Takes platform.
Scrapes WordPress blogs using the RSS feed with pagination.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class WordPressScraper(BaseScraper):
    """Scraper for WordPress blogs with RSS feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "wordpress":
            raise ValueError(f"Blog {blog_id} is not configured as wordpress")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.feed_url = self.config["scraper"].get("feedUrl", f"{self.base_url}/feed/")

        # Optional filters for excluding posts
        self.exclude_title_patterns = self.config["scraper"].get("excludeTitlePatterns", [])

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def should_exclude_post(self, title: str) -> bool:
        """Check if post should be excluded based on title patterns."""
        title_lower = title.lower()
        for pattern in self.exclude_title_patterns:
            if pattern.lower() in title_lower:
                return True
        return False

    def fetch_all_posts_from_feed(self) -> list[dict]:
        """Fetch all posts from RSS feed with pagination."""
        all_posts = []
        page = 1
        max_pages = 200  # Safety limit

        while page <= max_pages:
            url = f"{self.feed_url}?paged={page}"
            print(f"  Fetching page {page}...")

            try:
                response = requests.get(url, timeout=30, headers=self.headers)

                # WordPress returns 404 when there are no more pages
                if response.status_code == 404:
                    break

                response.raise_for_status()

                # Parse RSS feed
                root = ET.fromstring(response.content)

                # Find all items in the channel
                channel = root.find("channel")
                if channel is None:
                    break

                items = channel.findall("item")
                if not items:
                    break

                excluded_count = 0
                for item in items:
                    title_elem = item.find("title")
                    link_elem = item.find("link")
                    pub_date_elem = item.find("pubDate")

                    # content:encoded namespace
                    content_elem = item.find("{http://purl.org/rss/1.0/modules/content/}encoded")

                    title = title_elem.text if title_elem is not None else "Untitled"
                    url = link_elem.text if link_elem is not None else ""

                    # Check exclusion patterns
                    if self.should_exclude_post(title):
                        excluded_count += 1
                        continue

                    # Parse published date (format: "Tue, 02 Sep 2025 16:24:56 +0000")
                    pub_date = None
                    if pub_date_elem is not None and pub_date_elem.text:
                        try:
                            dt = datetime.strptime(pub_date_elem.text, "%a, %d %b %Y %H:%M:%S %z")
                            pub_date = dt.strftime("%Y-%m-%d")
                        except ValueError:
                            # Try alternate format
                            try:
                                dt = datetime.strptime(pub_date_elem.text[:25], "%a, %d %b %Y %H:%M:%S")
                                pub_date = dt.strftime("%Y-%m-%d")
                            except ValueError:
                                pass

                    # Get content (HTML)
                    content_html = ""
                    if content_elem is not None and content_elem.text:
                        content_html = content_elem.text

                    all_posts.append({
                        "title": title,
                        "url": url,
                        "pub_date": pub_date,
                        "content_html": content_html
                    })

                print(f"    Got {len(items)} items ({excluded_count} excluded)")

                # Check if there are more pages
                if len(items) < 10:  # WordPress default is 10 per page
                    break

                page += 1
                time.sleep(REQUEST_DELAY)

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    break
                print(f"  Error fetching feed page {page}: {e}")
                break
            except Exception as e:
                print(f"  Error fetching feed page {page}: {e}")
                break

        return all_posts

    def make_slug(self, url: str) -> str:
        """Extract slug from WordPress URL."""
        # WordPress URLs are like: https://mathbabe.org/2025/09/02/post-title/
        match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/([^/]+)/?$', url)
        if match:
            return match.group(4)
        # Fallback: use last part of URL
        return url.rstrip("/").split("/")[-1]

    def make_filename(self, post: dict) -> str:
        """Create markdown filename from post metadata."""
        slug = self.make_slug(post["url"])
        if post.get("pub_date"):
            return f"{post['pub_date']}-{slug}.md"
        return f"{slug}.md"

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post['title'].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if post.get("pub_date"):
            frontmatter.append(f"date: {post['pub_date']}")
        frontmatter.extend([
            f"url: {post['url']}",
            f"word_count: {post.get('word_count', 0)}",
            "---",
            ""
        ])
        return "\n".join(frontmatter) + "\n" + post.get("markdown", "")

    def scrape(self) -> list[dict]:
        """Scrape all posts from the WordPress blog."""
        print(f"Fetching posts from feed...")
        feed_posts = self.fetch_all_posts_from_feed()
        print(f"Found {len(feed_posts)} posts in feed (after exclusions)")

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

            # Convert HTML content to markdown
            if post.get("content_html"):
                soup = BeautifulSoup(post["content_html"], "html.parser")
                markdown = self.html_to_markdown(soup)
                post["markdown"] = markdown
                post["word_count"] = len(markdown.split())
            else:
                post["markdown"] = ""
                post["word_count"] = 0

            # Create full content with frontmatter
            post["content"] = self.make_post_content(post)

            # Save post
            filepath = self.save_post(post)
            print(f"  Saved: {filepath}")

            # Add to index (without full content)
            index_entry = {
                "filename": post["filename"],
                "title": post["title"],
                "url": post["url"],
                "pub_date": post.get("pub_date"),
                "word_count": post.get("word_count", 0)
            }
            posts.append(index_entry)

            # Save index periodically
            if (i + 1) % 20 == 0:
                self.save_index(posts)
                print(f"  Index saved ({len(posts)} posts)")

            time.sleep(REQUEST_DELAY)

        # Final save
        self.save_index(posts)
        return posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=mathbabe python wordpress.py")
        sys.exit(1)

    scraper = WordPressScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
