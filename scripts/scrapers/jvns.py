#!/usr/bin/env python3
"""
Julia Evans (jvns.ca) blog scraper for Spicy Takes platform.
Hugo blog with all posts listed on homepage.
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.0


class JvnsScraper(BaseScraper):
    """Scraper for jvns.ca blog posts."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "jvns":
            raise ValueError(
                f"Blog {blog_id} is not configured as jvns type"
            )

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")

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
        Extract blog post URLs from the homepage.
        All 590+ posts are listed on the single homepage.
        Returns list of {url, slug, date, title} dicts.
        """
        posts = []
        seen_slugs = set()

        for link in soup.find_all("a", href=True):
            href = link.get("href", "")
            title = link.get_text(strip=True)

            # Match /blog/YYYY/MM/DD/slug/ pattern
            match = re.match(
                r"^/blog/(\d{4})/(\d{2})/(\d{2})/(.+?)/?$",
                href,
            )
            if not match:
                continue
            if not title:
                continue

            year, month, day, slug = match.groups()
            date_str = f"{year}-{month}-{day}"

            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)

            url = f"{self.base_url}{href}"
            posts.append({
                "url": url,
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

        # Find content in <article> > <main>
        article = soup.find("article")
        if not article:
            print(f"  No <article> tag found: {url}")
            return None

        main_tag = article.find("main")
        content_elem = main_tag if main_tag else article

        content = self.html_to_markdown(
            content_elem, self.base_url
        )

        word_count = len(content.split())

        if word_count < 50:
            print(
                f"  Skipping (only {word_count} words): "
                f"{post_info['title']}"
            )
            return None

        return {
            "url": url,
            "slug": post_info["slug"],
            "title": post_info["title"],
            "date": post_info["date"],
            "content": content,
            "word_count": word_count,
        }

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
        print(f"Fetching homepage from {self.base_url}...")
        soup = self.fetch_page(self.base_url)
        if not soup:
            print("Failed to fetch homepage")
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
            title_preview = info["title"][:50]
            print(f"[{i+1}/{len(to_scrape)}] {title_preview}...")

            post = self.fetch_post(info)
            if post:
                filename = f"{post['date']}-{post['slug']}.md"

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
        print("Usage: BLOG_ID=jvns python jvns.py")
        sys.exit(1)

    scraper = JvnsScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
