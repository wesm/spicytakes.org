#!/usr/bin/env python3
"""
Substack scraper for Spicy Takes platform.
Downloads posts from Substack blogs and saves them as markdown files.
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from base import BaseScraper, get_blog_dir

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class SubstackScraper(BaseScraper):
    """Scraper for Substack blogs."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        # Validate scraper config
        if self.config["scraper"]["type"] != "substack":
            raise ValueError(f"Blog {blog_id} is not configured as a Substack blog")

        self.substack_url = self.config["scraper"]["substackUrl"]
        self.urls_file = self.data_dir / "post_urls.json"

    def discover_post_urls(self) -> list[str]:
        """Discover all post URLs from the Substack archive API."""
        all_urls = []
        offset = 0
        limit = 50  # Substack API limit

        print(f"Discovering posts from {self.substack_url}...")

        while True:
            api_url = f"{self.substack_url}/api/v1/archive?sort=new&offset={offset}&limit={limit}"
            try:
                response = requests.get(api_url, timeout=30, headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
                })
                response.raise_for_status()
                posts = response.json()

                if not posts:
                    break

                for post in posts:
                    if "canonical_url" in post:
                        all_urls.append(post["canonical_url"])
                    elif "slug" in post:
                        all_urls.append(f"{self.substack_url}/p/{post['slug']}")

                print(f"  Found {len(all_urls)} posts so far...")
                offset += limit
                time.sleep(REQUEST_DELAY)

            except requests.RequestException as e:
                print(f"  Error fetching archive at offset {offset}: {e}")
                break

        return all_urls

    def update_urls_file(self, urls: list[str]):
        """Update the post URLs file with newly discovered URLs."""
        existing_urls = self.load_urls()
        existing_set = set(existing_urls)
        new_urls = [u for u in urls if u not in existing_set]

        if new_urls:
            print(f"Found {len(new_urls)} new post(s)")

        # Merge: new discovered URLs + existing URLs not in discovered (preserves old posts)
        discovered_set = set(urls)
        old_only = [u for u in existing_urls if u not in discovered_set]
        all_urls = urls + old_only  # New first, then any old posts not in API

        data = {
            "source": self.substack_url,
            "scraped_at": datetime.now().strftime("%Y-%m-%d"),
            "total_posts": len(all_urls),
            "posts": all_urls
        }
        with open(self.urls_file, "w") as f:
            json.dump(data, f, indent=2)

        return new_urls

    def load_urls(self) -> list[str]:
        """Load post URLs from the JSON file."""
        if not self.urls_file.exists():
            print(f"Warning: {self.urls_file} not found")
            return []
        with open(self.urls_file) as f:
            data = json.load(f)
        return data.get("posts", [])

    def fetch_post(self, url: str) -> dict | None:
        """Fetch a single post and extract metadata + content."""
        try:
            response = requests.get(url, timeout=30, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            })
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title
        title_elem = soup.find("h1", class_="post-title")
        if not title_elem:
            title_elem = soup.find("h1")
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # Extract subtitle
        subtitle_elem = soup.find("h3", class_="subtitle")
        subtitle = subtitle_elem.get_text(strip=True) if subtitle_elem else ""

        # Extract date from JSON-LD (most reliable)
        pub_date = None
        date_str = ""
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                ld_data = json.loads(script.string)
                if "datePublished" in ld_data:
                    date_str = ld_data["datePublished"]
                    break
            except (json.JSONDecodeError, TypeError):
                continue

        # Fallback to time element
        if not date_str:
            date_elem = soup.find("time")
            if date_elem and date_elem.get("datetime"):
                date_str = date_elem["datetime"]

        # Parse date
        if date_str:
            try:
                if "T" in date_str:
                    pub_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            except Exception:
                pass

        # Extract main content
        content_div = soup.find("div", class_="body")
        if not content_div:
            content_div = soup.find("div", class_="post-content")
        if not content_div:
            content_div = soup.find("article")

        if not content_div:
            print(f"  Warning: Could not find content div for {url}")
            return None

        # Convert HTML to markdown-like text
        content = self.html_to_markdown(content_div)

        # Generate slug from URL
        slug = url.split("/p/")[-1].rstrip("/")

        return {
            "url": url,
            "slug": slug,
            "title": title,
            "subtitle": subtitle,
            "date": pub_date.isoformat() if pub_date else None,
            "date_str": date_str,
            "content": content,
            "word_count": len(content.split())
        }

    def html_to_markdown(self, element) -> str:
        """Convert HTML content to markdown-like text."""
        lines = []

        for child in element.children:
            if isinstance(child, str):
                text = child.strip()
                if text:
                    lines.append(text)
                continue

            tag = child.name

            if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                level = int(tag[1])
                text = child.get_text(strip=True)
                lines.append(f"\n{'#' * level} {text}\n")

            elif tag == "p":
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"\n{text}\n")

            elif tag == "blockquote":
                text = child.get_text(strip=True)
                if text:
                    quoted = "\n".join(f"> {line}" for line in text.split("\n"))
                    lines.append(f"\n{quoted}\n")

            elif tag in ["ul", "ol"]:
                for i, li in enumerate(child.find_all("li", recursive=False)):
                    prefix = "-" if tag == "ul" else f"{i+1}."
                    text = li.get_text(strip=True)
                    lines.append(f"{prefix} {text}")
                lines.append("")

            elif tag == "pre":
                code = child.get_text()
                lines.append(f"\n```\n{code}\n```\n")

            elif tag == "a":
                text = child.get_text(strip=True)
                href = child.get("href", "")
                if text and href:
                    lines.append(f"[{text}]({href})")

            elif tag == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                if src:
                    lines.append(f"\n![{alt}]({src})\n")

            elif tag in ["div", "section", "article"]:
                nested = self.html_to_markdown(child)
                if nested.strip():
                    lines.append(nested)

            elif tag == "figure":
                img = child.find("img")
                if img:
                    alt = img.get("alt", "")
                    src = img.get("src", "")
                    lines.append(f"\n![{alt}]({src})\n")
                figcaption = child.find("figcaption")
                if figcaption:
                    lines.append(f"*{figcaption.get_text(strip=True)}*\n")

            elif tag == "hr":
                lines.append("\n---\n")

            elif tag in ["em", "i"]:
                text = child.get_text(strip=True)
                lines.append(f"*{text}*")

            elif tag in ["strong", "b"]:
                text = child.get_text(strip=True)
                lines.append(f"**{text}**")

        return "\n".join(lines)

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post['title'].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if post.get("subtitle"):
            escaped_subtitle = post['subtitle'].replace('"', "'")
            frontmatter.append(f'subtitle: "{escaped_subtitle}"')
        if post.get("date"):
            frontmatter.append(f"date: {post['date']}")
        frontmatter.extend([
            f"url: {post['url']}",
            f"slug: {post['slug']}",
            f"word_count: {post['word_count']}",
            "---",
            ""
        ])
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all posts from the Substack."""
        # First, discover any new posts from the Substack API
        discovered_urls = self.discover_post_urls()
        if discovered_urls:
            self.update_urls_file(discovered_urls)

        urls = self.load_urls()
        print(f"Found {len(urls)} total posts")

        existing_slugs = self.get_existing_slugs()
        urls_to_scrape = [u for u in urls if u.split("/p/")[-1].rstrip("/") not in existing_slugs]

        if not urls_to_scrape:
            print("All posts already scraped!")
            existing = self.load_existing_index()
            return existing.get("posts", [])

        print(f"Scraping {len(urls_to_scrape)} new posts...")

        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        for i, url in enumerate(urls_to_scrape):
            print(f"[{i+1}/{len(urls_to_scrape)}] {url}")

            post = self.fetch_post(url)
            if post:
                # Create filename from date and slug
                if post["date"]:
                    date_prefix = post["date"][:10]
                    filename = f"{date_prefix}-{post['slug']}.md"
                else:
                    filename = f"{post['slug']}.md"

                # Save post
                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                # Add to index (without full content)
                index_entry = {k: v for k, v in post.items() if k != "content"}
                posts.append(index_entry)

                # Save index periodically
                if (i + 1) % 10 == 0:
                    self.save_index(posts)
                    print(f"  Index saved ({len(posts)} posts)")

            # Rate limiting
            time.sleep(REQUEST_DELAY)

        # Final save
        self.save_index(posts)
        return posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=benn python substack.py")
        sys.exit(1)

    scraper = SubstackScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
