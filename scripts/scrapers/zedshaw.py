#!/usr/bin/env python3
"""
Zed Shaw blog scraper for Spicy Takes platform.
Scrapes blog posts from zedshaw.com.
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.5


class ZedShawScraper(BaseScraper):
    """Scraper for zedshaw.com blog posts."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "zedshaw":
            raise ValueError(
                f"Blog {blog_id} is not configured as zedshaw type"
            )

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.blog_url = self.config["scraper"]["blogUrl"]

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
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def get_post_urls(self, soup: BeautifulSoup) -> list[dict]:
        """
        Extract blog post URLs from the blog index page.
        Returns list of {url, slug, date} dicts.
        """
        posts = []
        seen_slugs = set()

        for link in soup.find_all("a", href=True):
            href = link.get("href", "")

            # Match /blog/YYYY-MM-DD-slug/ pattern
            match = re.match(
                r"^/blog/(\d{4}-\d{2}-\d{2})-(.+?)/?$", href
            )
            if not match:
                continue

            date_str = match.group(1)
            slug = match.group(2)

            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)

            url = f"{self.base_url}{href}"
            posts.append({
                "url": url,
                "slug": slug,
                "date": date_str,
            })

        return posts

    def fetch_post(self, url: str, date: str) -> dict | None:
        """Fetch and parse a single blog post."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Extract title from h1 inside <content> tag
        content_tag = soup.find("content")
        if not content_tag:
            print(f"  No <content> tag found: {url}")
            return None

        h1 = content_tag.find("h1")
        title = h1.get_text(strip=True) if h1 else "Untitled"

        # Remove <info> tag (author byline) before conversion
        info_tag = content_tag.find("info")
        if info_tag:
            info_tag.decompose()

        # Convert content to markdown
        content = self.html_to_markdown(
            content_tag, self.base_url
        )

        # Strip Svelte rendering artifacts
        content = content.replace("HTML_TAG_START", "")
        content = content.replace("HTML_TAG_END", "")

        word_count = len(content.split())

        if word_count < 50:
            print(f"  Skipping (only {word_count} words): {title}")
            return None

        slug = url.rstrip("/").split("/")[-1]
        # Strip date prefix from slug if present
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)

        return {
            "url": url,
            "slug": slug,
            "title": title,
            "date": date,
            "content": content,
            "word_count": word_count,
        }

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post["title"].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if post.get("date"):
            frontmatter.append(f"date: {post['date']}")
        frontmatter.extend([
            f"url: {post['url']}",
            f"slug: {post['slug']}",
            f"word_count: {post['word_count']}",
            "---",
            "",
        ])
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all blog posts."""
        print(f"Fetching blog index from {self.blog_url}...")
        soup = self.fetch_page(self.blog_url)
        if not soup:
            print("Failed to fetch blog index")
            return []

        post_infos = self.get_post_urls(soup)
        print(f"Found {len(post_infos)} posts")

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
            url = info["url"]
            print(f"[{i+1}/{len(to_scrape)}] {url.split('/')[-2][:50]}...")

            post = self.fetch_post(url, info["date"])
            if post:
                slug = post["slug"]
                filename = f"{post['date']}-{slug}.md"

                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath} ({post['title'][:40]})")

                index_entry = {
                    k: v for k, v in post.items() if k != "content"
                }
                posts.append(index_entry)

                if (i + 1) % 10 == 0:
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
        print("Usage: BLOG_ID=zedshaw python zedshaw.py")
        sys.exit(1)

    scraper = ZedShawScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
