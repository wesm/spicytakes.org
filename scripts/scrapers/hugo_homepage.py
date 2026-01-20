#!/usr/bin/env python3
"""
Hugo homepage blog scraper for Spicy Takes platform.
Scrapes blogs that list all posts on homepage (like blog.jessfraz.com).
"""

import os
import re
import sys
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class HugoHomepageScraper(BaseScraper):
    """Scraper for Hugo blogs that list all posts on homepage."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "hugo_homepage":
            raise ValueError(f"Blog {blog_id} is not configured as hugo_homepage")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.post_prefix = self.config["scraper"].get("postPrefix", "/post/")

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
            # Posts are in <h3><a href="...">Title</a></h3>
            # Links can be relative (/post/slug/) or absolute (https://site/post/slug/)
            for h3 in soup.find_all("h3"):
                link = h3.find("a")
                if not link:
                    continue

                href = link.get("href", "")
                title = link.get_text(strip=True)

                # Check if it's a post link (handles both relative and absolute URLs)
                if self.post_prefix in href:
                    # Make URL absolute if relative
                    if href.startswith("/"):
                        url = self.base_url + href
                    else:
                        url = href

                    posts.append({
                        "title": title,
                        "url": url,
                        "pub_date": None,  # Will extract from post page
                    })

            return posts
        except Exception as e:
            print(f"  Error fetching homepage: {e}")
            return []

    def parse_date_from_page(self, soup: BeautifulSoup) -> str | None:
        """Extract date from post page. Returns YYYY-MM-DD string."""
        # First, try <time> elements with datetime attribute (most reliable)
        time_elem = soup.find("time", datetime=True)
        if time_elem:
            dt = time_elem.get("datetime", "")
            # Handle ISO format: 2021-01-22 or 2021-01-22T...
            match = re.match(r"(\d{4})-(\d{2})-(\d{2})", dt)
            if match:
                return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

        # Second, try meta tags
        for meta in soup.find_all("meta", property=True):
            if "date" in meta.get("property", "").lower():
                content = meta.get("content", "")
                match = re.match(r"(\d{4})-(\d{2})-(\d{2})", content)
                if match:
                    return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"

        # Fall back to text parsing in header area only
        header = soup.find("header") or soup.find("article") or soup.find("main")
        if header:
            text = header.get_text()
        else:
            # Last resort: first 500 chars of page to avoid content dates
            text = soup.get_text()[:500]

        months = {
            "january": 1, "february": 2, "march": 3, "april": 4,
            "may": 5, "june": 6, "july": 7, "august": 8,
            "september": 9, "october": 10, "november": 11, "december": 12
        }

        # Try various date patterns
        patterns = [
            # "Friday, January 22, 2021"
            (r"(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+(\w+)\s+(\d{1,2}),\s+(\d{4})", "mdy"),
            # "January 22, 2021"
            (r"(\w+)\s+(\d{1,2}),\s+(\d{4})", "mdy"),
            # "22 January 2021"
            (r"(\d{1,2})\s+(\w+)\s+(\d{4})", "dmy"),
        ]

        for pattern, fmt in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                groups = match.groups()
                try:
                    if fmt == "mdy":
                        month_name, day, year = groups[0], groups[1], groups[2]
                    else:
                        day, month_name, year = groups[0], groups[1], groups[2]
                    month = months.get(month_name.lower())
                    if month:
                        return f"{year}-{month:02d}-{int(day):02d}"
                except (ValueError, KeyError):
                    continue

        return None

    def fetch_post(self, url: str, title: str) -> dict | None:
        """Fetch a single post and return structured data."""
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

        # Extract date from page
        date_str = self.parse_date_from_page(soup)

        # Find main content - look for article or main content area
        content_elem = soup.find("article") or soup.find("main") or soup.find("div", class_="content")
        if not content_elem:
            content_elem = soup.find("body") or soup

        # Convert to markdown
        content = self.html_to_markdown(content_elem)

        if not content or len(content.strip()) < 100:
            print(f"  Warning: Very short content for {url}")

        # Extract slug from URL
        slug_match = re.search(r"/post/([^/]+)/?$", url.rstrip("/"))
        if not slug_match:
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

        # Fetch from homepage
        print("\nFetching homepage posts...")
        all_posts = self.fetch_homepage_posts()
        print(f"  Found {len(all_posts)} posts on homepage")

        if not all_posts:
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
        for i, post_meta in enumerate(all_posts):
            url = post_meta["url"]
            title = post_meta["title"]

            # Extract slug
            slug_match = re.search(r"/post/([^/]+)/?$", url.rstrip("/"))
            if not slug_match:
                slug_match = re.search(r"/([^/]+)/?$", url.rstrip("/"))
            slug = slug_match.group(1) if slug_match else None

            if slug in existing_slugs:
                print(f"  Skipping {slug} (already scraped)")
                continue

            print(f"\n[{i+1}/{len(all_posts)}] Fetching: {title}")
            time.sleep(REQUEST_DELAY)

            post = self.fetch_post(url, title)

            if post:
                # Save post
                date_str = post.get("date")
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
        print("Usage: BLOG_ID=jessfraz python scripts/scrapers/hugo_homepage.py")
        sys.exit(1)

    scraper = HugoHomepageScraper(blog_id)
    scraper.scrape()
