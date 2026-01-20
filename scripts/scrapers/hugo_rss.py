#!/usr/bin/env python3
"""
Hugo RSS blog scraper for Spicy Takes platform.
Scrapes blogs that provide RSS feeds (like Hugo-powered blogs).
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class HugoRssScraper(BaseScraper):
    """Scraper for Hugo/RSS-based blogs like bcantrill.dtrace.org."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "hugo_rss":
            raise ValueError(f"Blog {blog_id} is not configured as hugo_rss")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_homepage_posts(self) -> list[dict]:
        """Fetch and parse posts from homepage. Returns list of post metadata."""
        try:
            response = requests.get(self.base_url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            posts = []
            # Posts are in <h4><a href="/YYYY/MM/DD/slug/">Title</a></h4>
            for h4 in soup.find_all("h4"):
                link = h4.find("a")
                if not link:
                    continue

                href = link.get("href", "")
                title = link.get_text(strip=True)

                # Only include posts with date-based URLs
                if not re.match(r"^/\d{4}/\d{2}/\d{2}/", href):
                    continue

                # Make URL absolute
                url = self.base_url + href if href.startswith("/") else href

                posts.append({
                    "title": title,
                    "url": url,
                    "pub_date": None,  # Will extract from URL
                    "description": None
                })

            return posts
        except Exception as e:
            print(f"  Error fetching homepage: {e}")
            return []

    def parse_date(self, pub_date: str | None, url: str) -> str | None:
        """Parse date from pubDate or URL. Returns YYYY-MM-DD string."""
        # Try to extract from URL first (more reliable format)
        # URL format: /YYYY/MM/DD/slug/
        match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

        # Fall back to parsing pubDate
        if pub_date:
            # RFC 2822 format: "Wed, 31 Dec 2025 00:00:00 +0000"
            try:
                from email.utils import parsedate_to_datetime
                dt = parsedate_to_datetime(pub_date)
                return dt.strftime("%Y-%m-%d")
            except Exception:
                pass

        return None

    def fetch_post(self, url: str, title: str, date_str: str | None) -> dict | None:
        """Fetch a single post and return structured data."""
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

        # Find main content - Hugo blogs typically use <article> or <main>
        content_elem = soup.find("article") or soup.find("main") or soup.find("div", class_="content")
        if not content_elem:
            content_elem = soup.find("body") or soup

        # Convert to markdown
        content = self.html_to_markdown(content_elem)

        if not content or len(content.strip()) < 100:
            print(f"  Warning: Very short content for {url}")

        # Extract slug from URL
        slug_match = re.search(r"/([^/]+)/?$", url.rstrip("/"))
        slug = slug_match.group(1) if slug_match else "unknown"

        return {
            "title": title,
            "date": date_str,
            "url": url,
            "slug": slug,
            "content": content.strip(),
            "word_count": len(content.split())
        }

    def html_to_markdown(self, element) -> str:
        """Convert HTML element to markdown.

        Only processes block-level elements to avoid text duplication.
        Inline elements are handled within their parent blocks via get_text().
        """
        lines = []

        # Block-level elements to process
        block_tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre", "ul", "ol", "li"]

        for child in element.find_all(block_tags, recursive=True):
            # Skip nested blocks (e.g., li inside ul) - they'll be processed separately
            if child.find_parent(block_tags[:-1]):  # Exclude li from parent check
                if child.name != "li":
                    continue

            if child.name == "p":
                text = child.get_text(separator=" ", strip=True)
                if text:
                    lines.append(text)
                    lines.append("")
            elif child.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                level = int(child.name[1])
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"{'#' * level} {text}")
                    lines.append("")
            elif child.name == "blockquote":
                text = child.get_text(separator=" ", strip=True)
                if text:
                    lines.append(f"> {text}")
                    lines.append("")
            elif child.name == "pre":
                code = child.get_text()
                lines.append("```")
                lines.append(code.strip())
                lines.append("```")
                lines.append("")
            elif child.name == "li":
                text = child.get_text(separator=" ", strip=True)
                if text:
                    lines.append(f"* {text}")

        # Join with newlines, collapse multiple blank lines
        result = "\n".join(lines)
        result = re.sub(r"\n{3,}", "\n\n", result)
        return result.strip()

    def scrape(self):
        """Main scrape method."""
        print(f"Scraping {self.config['name']}...")
        print(f"Base URL: {self.base_url}")

        # Fetch from homepage (has all posts, not just recent 20)
        print("\nFetching homepage posts...")
        rss_posts = self.fetch_homepage_posts()
        print(f"  Found {len(rss_posts)} posts on homepage")

        if not rss_posts:
            print("No posts found on homepage")
            return

        # Load existing index to avoid re-scraping
        existing_slugs = set()
        index_file = self.data_dir / "posts_index.json"
        if index_file.exists():
            import json
            with open(index_file) as f:
                index = json.load(f)
                existing_slugs = {p.get("slug") for p in index.get("posts", [])}

        # Process each post
        new_posts = []
        for i, post_meta in enumerate(rss_posts):
            url = post_meta["url"]
            title = post_meta["title"]

            # Extract slug
            slug_match = re.search(r"/([^/]+)/?$", url.rstrip("/"))
            slug = slug_match.group(1) if slug_match else None

            if slug in existing_slugs:
                print(f"  Skipping {slug} (already scraped)")
                continue

            print(f"\n[{i+1}/{len(rss_posts)}] Fetching: {title}")
            time.sleep(REQUEST_DELAY)

            date_str = self.parse_date(post_meta["pub_date"], url)
            post = self.fetch_post(url, title, date_str)

            if post:
                # Save post
                if date_str:
                    filename = f"{date_str}-{slug}.md"
                else:
                    filename = f"{slug}.md"

                self.save_post(post, filename)
                new_posts.append(post)
                print(f"  Saved: {filename} ({post['word_count']} words)")

        # Update index
        self.update_index(new_posts)
        print(f"\nDone! Scraped {len(new_posts)} new posts.")

    def save_post(self, post: dict, filename: str):
        """Save a post as markdown with frontmatter."""
        filepath = os.path.join(self.posts_dir, filename)

        frontmatter = f"""---
title: "{post['title'].replace('"', '\\"')}"
date: {post['date'] or 'unknown'}
url: {post['url']}
slug: {post['slug']}
word_count: {post['word_count']}
---

{post['content']}
"""
        with open(filepath, "w") as f:
            f.write(frontmatter)

    def update_index(self, new_posts: list[dict]):
        """Update the posts index file."""
        import json
        from datetime import datetime

        index_file = self.data_dir / "posts_index.json"

        # Load existing index
        existing_posts = []
        if index_file.exists():
            with open(index_file) as f:
                data = json.load(f)
                existing_posts = data.get("posts", [])

        # Add new posts
        for post in new_posts:
            existing_posts.append({
                "slug": post["slug"],
                "title": post["title"],
                "date": post["date"],
                "url": post["url"],
                "word_count": post["word_count"],
                "filename": f"{post['date']}-{post['slug']}.md" if post["date"] else f"{post['slug']}.md"
            })

        # Sort by date descending
        existing_posts.sort(key=lambda p: p.get("date") or "", reverse=True)

        # Save index
        with open(index_file, "w") as f:
            json.dump({
                "last_updated": datetime.now().isoformat(),
                "total_posts": len(existing_posts),
                "posts": existing_posts
            }, f, indent=2)


if __name__ == "__main__":
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=bcantrill python scripts/scrapers/hugo_rss.py")
        sys.exit(1)

    scraper = HugoRssScraper(blog_id)
    scraper.scrape()
