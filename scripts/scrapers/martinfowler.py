#!/usr/bin/env python3
"""
Martin Fowler blog scraper for Spicy Takes platform.
Scrapes articles from martinfowler.com using year tag pages for discovery.
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class MartinFowlerScraper(BaseScraper):
    """Scraper for martinfowler.com blog."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        # Validate scraper config
        if self.config["scraper"]["type"] != "martinfowler":
            raise ValueError(f"Blog {blog_id} is not configured as a martinfowler blog")

        self.base_url = self.config["scraper"]["baseUrl"]
        self.start_year = self.config["scraper"].get("startYear", 2003)
        self.end_year = self.config["scraper"].get("endYear", 2026)
        self.urls_file = self.data_dir / "post_urls.json"

    def fetch_page(self, url: str) -> BeautifulSoup | None:
        """Fetch a page and return BeautifulSoup object."""
        try:
            response = requests.get(url, timeout=30, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            })
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def discover_posts_from_year(self, year: int) -> list[dict]:
        """Discover all posts from a year tag page."""
        url = f"{self.base_url}/tags/{year}.html"
        soup = self.fetch_page(url)
        if not soup:
            return []

        posts = []

        # Find article entries - they're typically in divs with class containing 'entry' or similar
        # Look for links to /bliki/ or /articles/
        for link in soup.find_all("a", href=True):
            href = link.get("href", "")

            # Skip non-content links
            if not href or href.startswith("#"):
                continue
            if "/bliki/" not in href and "/articles/" not in href:
                continue
            if href.endswith("/bliki/") or href.endswith("/articles/"):
                continue

            # Make absolute URL
            full_url = urljoin(self.base_url, href)

            # Extract title from link text
            title = link.get_text(strip=True)
            if not title or len(title) < 3:
                continue

            # Try to find the parent container for more metadata
            parent = link.find_parent(["div", "article", "li"])

            # Try to find date
            date_str = None
            if parent:
                # Look for date in text like "22 Dec 2024" or similar
                date_text = parent.get_text()
                date_match = re.search(r'(\d{1,2}\s+\w{3}\s+\d{4})', date_text)
                if date_match:
                    date_str = date_match.group(1)

            # Try to find description/summary
            description = ""
            if parent:
                # Look for paragraph text that's not the title
                for p in parent.find_all("p"):
                    text = p.get_text(strip=True)
                    if text and text != title and len(text) > 20:
                        description = text
                        break

            posts.append({
                "url": full_url,
                "title": title,
                "date_str": date_str,
                "description": description,
                "year": year
            })

        # Deduplicate by URL
        seen = set()
        unique_posts = []
        for post in posts:
            if post["url"] not in seen:
                seen.add(post["url"])
                unique_posts.append(post)

        return unique_posts

    def discover_all_posts(self) -> list[dict]:
        """Discover all posts across all years."""
        all_posts = []

        print(f"Discovering posts from {self.start_year} to {self.end_year}...")

        for year in range(self.end_year, self.start_year - 1, -1):
            print(f"  Year {year}...", end=" ", flush=True)
            posts = self.discover_posts_from_year(year)
            print(f"{len(posts)} posts")
            all_posts.extend(posts)
            time.sleep(REQUEST_DELAY)

        # Deduplicate across years (some posts might appear in multiple year pages)
        seen = set()
        unique_posts = []
        for post in all_posts:
            if post["url"] not in seen:
                seen.add(post["url"])
                unique_posts.append(post)

        print(f"Total unique posts discovered: {len(unique_posts)}")
        return unique_posts

    def update_urls_file(self, posts: list[dict]) -> list[dict]:
        """Update the post URLs file with newly discovered posts."""
        existing = self.load_urls()
        existing_urls = {p["url"] for p in existing}

        new_posts = [p for p in posts if p["url"] not in existing_urls]

        if new_posts:
            print(f"Found {len(new_posts)} new post(s)")

        all_posts = posts  # Use newly discovered list as source of truth

        data = {
            "source": self.base_url,
            "scraped_at": datetime.now().strftime("%Y-%m-%d"),
            "total_posts": len(all_posts),
            "posts": all_posts
        }
        with open(self.urls_file, "w") as f:
            json.dump(data, f, indent=2)

        return new_posts

    def load_urls(self) -> list[dict]:
        """Load post URLs from the JSON file."""
        if not self.urls_file.exists():
            return []
        with open(self.urls_file) as f:
            data = json.load(f)
        return data.get("posts", [])

    def parse_date(self, date_str: str | None, year: int | None = None) -> datetime | None:
        """Parse date string into datetime."""
        if not date_str:
            return None

        # Try various formats
        formats = [
            "%d %b %Y",      # "22 Dec 2024"
            "%d %B %Y",      # "22 December 2024"
            "%B %d, %Y",     # "December 22, 2024"
            "%Y-%m-%d",      # "2024-12-22"
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str.strip(), fmt)
            except ValueError:
                continue

        # If we have a year but couldn't parse, default to Jan 1
        if year:
            return datetime(year, 1, 1)

        return None

    def fetch_post(self, post_info: dict) -> dict | None:
        """Fetch a single post and extract content."""
        url = post_info["url"]
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Extract title - try multiple approaches
        title = post_info.get("title", "")
        title_elem = soup.find("h1")
        if title_elem:
            title = title_elem.get_text(strip=True)

        # Extract date from page - look for date element with class 'date'
        date_str = post_info.get("date_str")
        pub_date = None

        # Look for date in page (martinfowler.com uses <p class='date'>)
        if not date_str:
            date_elem = soup.find("p", class_="date")
            if date_elem:
                date_str = date_elem.get_text(strip=True)

        # Look for date in meta tags
        if not date_str:
            for meta in soup.find_all("meta"):
                if meta.get("property") == "og:article:modified_time":
                    # Format: "2025-08-18 00:00:00 -0400"
                    meta_date = meta.get("content", "")
                    if meta_date:
                        date_str = meta_date.split()[0]  # Just get the date part
                        break

        pub_date = self.parse_date(date_str, post_info.get("year"))

        # Extract tags from tag links
        tags = []
        tags_div = soup.find("div", class_="tags")
        if tags_div:
            for tag_link in tags_div.find_all("a"):
                tag_text = tag_link.get_text(strip=True).lower()
                if tag_text and not tag_text.isdigit():
                    tags.append(tag_text)

        # Extract main content - martinfowler.com uses <div class='paperBody'>
        content_elem = soup.find("div", class_="paperBody")

        # Fallback for articles (they may use different structure)
        if not content_elem:
            content_elem = soup.find("div", class_="paper")

        # Try article tag
        if not content_elem:
            article = soup.find("article")
            if article:
                # Remove frontMatter div to get just content
                front = article.find("div", class_="frontMatter")
                if front:
                    front.decompose()
                content_elem = article

        # Fallback to main tag
        if not content_elem:
            content_elem = soup.find("main")

        if not content_elem:
            print(f"  Warning: Could not find content for {url}")
            return None

        # Convert HTML to markdown
        content = self.html_to_markdown(content_elem, self.base_url)

        # Generate slug from URL
        slug = url.rstrip("/").split("/")[-1]
        if slug.endswith(".html"):
            slug = slug[:-5]

        return {
            "url": url,
            "slug": slug,
            "title": title,
            "date": pub_date.isoformat() if pub_date else None,
            "date_str": date_str,
            "tags": tags,
            "description": post_info.get("description", ""),
            "content": content,
            "word_count": len(content.split())
        }

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post['title'].replace('"', "'").replace("\n", " ")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if post.get("description"):
            escaped_desc = post['description'].replace('"', "'").replace("\n", " ")[:200]
            frontmatter.append(f'description: "{escaped_desc}"')
        if post.get("date"):
            frontmatter.append(f"date: {post['date']}")
        if post.get("tags"):
            frontmatter.append(f"tags: {json.dumps(post['tags'])}")
        frontmatter.extend([
            f"url: {post['url']}",
            f"slug: {post['slug']}",
            f"word_count: {post['word_count']}",
            "---",
            ""
        ])
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all posts from martinfowler.com."""
        # First, discover posts from year pages
        discovered_posts = self.discover_all_posts()
        if discovered_posts:
            self.update_urls_file(discovered_posts)

        post_infos = self.load_urls()
        print(f"Found {len(post_infos)} total posts")

        # Get existing slugs to skip already-scraped posts
        existing_filenames = self.get_existing_filenames()

        # Filter to posts that haven't been scraped
        to_scrape = []
        for post_info in post_infos:
            slug = post_info["url"].rstrip("/").split("/")[-1]
            if slug.endswith(".html"):
                slug = slug[:-5]

            # Check if any existing file matches this slug
            found = False
            for filename in existing_filenames:
                if slug in filename:
                    found = True
                    break
            if not found:
                to_scrape.append(post_info)

        if not to_scrape:
            print("All posts already scraped!")
            existing = self.load_existing_index()
            return existing.get("posts", [])

        print(f"Scraping {len(to_scrape)} new posts...")

        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        for i, post_info in enumerate(to_scrape):
            print(f"[{i+1}/{len(to_scrape)}] {post_info['title'][:50]}...")

            post = self.fetch_post(post_info)
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
        print("Usage: BLOG_ID=fowler python martinfowler.py")
        sys.exit(1)

    scraper = MartinFowlerScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
