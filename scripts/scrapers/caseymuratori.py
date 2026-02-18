#!/usr/bin/env python3
"""
Casey Muratori blog scraper for Spicy Takes platform.
Scrapes blog posts from caseymuratori.com.
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.5


class CaseyMuratoriScraper(BaseScraper):
    """Scraper for caseymuratori.com blog posts."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "caseymuratori":
            raise ValueError(
                f"Blog {blog_id} is not configured as caseymuratori type"
            )

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.contents_url = self.config["scraper"]["contentsUrl"]

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
        Extract blog post URLs from the contents page.
        Returns list of {url, title, slug} dicts.
        """
        posts = []
        seen_slugs = set()

        for link in soup.find_all("a", href=True):
            href = link.get("href", "")
            title = link.get_text(strip=True)

            if not re.match(r"^blog_\d{4}$", href):
                continue
            if not title:
                continue

            slug = href
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)

            url = f"{self.base_url}/{href}"
            posts.append({
                "url": url,
                "title": title,
                "slug": slug,
            })

        return posts

    def fetch_post(self, url: str, index_title: str) -> dict | None:
        """Fetch and parse a single blog post."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Extract title from <title> tag (clean, no suffix)
        title = index_title
        title_tag = soup.find("title")
        if title_tag:
            raw_title = title_tag.get_text(strip=True)
            if raw_title:
                title = raw_title

        # Extract date — look for YYYY-MM-DD pattern in page text
        date_str = None
        page_text = soup.get_text()
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", page_text)
        if date_match:
            date_str = date_match.group(1)

        # Find main content container: largest div child of body
        # CSS class names are obfuscated and vary per page
        body = soup.find("body")
        if not body:
            return None
        div_children = [
            c for c in body.children
            if hasattr(c, "name") and c.name == "div"
        ]
        if div_children:
            content_div = max(
                div_children, key=lambda d: len(d.get_text())
            )
        else:
            content_div = body

        content = self.html_to_markdown(content_div, self.base_url)

        # Strip navigation/header cruft from start of content
        # Remove lines that are just nav links like "< Prev | Contents | Next >"
        lines = content.split("\n")
        cleaned_lines = []
        in_body = False
        for line in lines:
            stripped = line.strip()
            # Skip nav-like lines at the top
            if not in_body:
                if re.match(
                    r"^[\[<]?\s*(Prev|Next|Contents)", stripped
                ):
                    continue
                if stripped and not re.match(r"^[|\-\s<>]+$", stripped):
                    in_body = True
            if in_body:
                cleaned_lines.append(line)
        content = "\n".join(cleaned_lines)

        word_count = len(content.split())

        # Skip posts with very little text (likely video-only)
        if word_count < 50:
            print(f"  Skipping (only {word_count} words): {title}")
            return None

        slug = url.rstrip("/").split("/")[-1]

        return {
            "url": url,
            "slug": slug,
            "title": title,
            "date": date_str,
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
        print(f"Fetching contents from {self.contents_url}...")
        soup = self.fetch_page(self.contents_url)
        if not soup:
            print("Failed to fetch contents page")
            return []

        post_infos = self.get_post_urls(soup)
        print(f"Found {len(post_infos)} posts")

        existing_slugs = self.get_existing_slugs()
        to_scrape = [
            p for p in post_infos if p["slug"] not in existing_slugs
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
            print(f"[{i+1}/{len(to_scrape)}] {info['title'][:60]}...")

            post = self.fetch_post(url, info["title"])
            if post:
                slug = post["slug"]
                if post.get("date"):
                    filename = f"{post['date'][:10]}-{slug}.md"
                else:
                    filename = f"{slug}.md"

                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

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
        print("Usage: BLOG_ID=cmuratori python caseymuratori.py")
        sys.exit(1)

    scraper = CaseyMuratoriScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
