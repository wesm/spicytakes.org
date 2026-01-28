#!/usr/bin/env python3
"""
Jekyll static site scraper for Spicy Takes platform.
Scrapes Jekyll blogs by fetching post list page and individual posts.
Used for sites without full RSS feeds (e.g., nadia.xyz).
"""

import json
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


class JekyllStaticScraper(BaseScraper):
    """Scraper for static Jekyll blogs without full RSS feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "jekyll_static":
            raise ValueError(f"Blog {blog_id} is not configured as jekyll_static")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.posts_list_url = self.config["scraper"].get("postsListUrl", f"{self.base_url}/posts/")
        self.content_selector = self.config["scraper"].get("contentSelector", "article")

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_post_urls(self) -> list[str]:
        """Fetch all post URLs from the posts list page."""
        print(f"  Fetching post list from {self.posts_list_url}...")

        try:
            response = requests.get(self.posts_list_url, timeout=30, headers=self.headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Find all links that look like blog posts
            urls = []
            for link in soup.find_all("a", href=True):
                href = link["href"]
                # Skip navigation links, external links, etc.
                if href.startswith("/") and not href.startswith("//"):
                    # Skip common non-post paths
                    if href in ["/", "/posts/", "/about/", "/projects/", "/notes/"]:
                        continue
                    if any(href.startswith(p) for p in ["/assets/", "/images/", "/css/", "/js/"]):
                        continue
                    # This looks like a post URL
                    full_url = self.base_url + href
                    if full_url not in urls:
                        urls.append(full_url)

            return urls

        except Exception as e:
            print(f"  Error fetching post list: {e}")
            return []

    def extract_date_from_page(self, soup: BeautifulSoup) -> str | None:
        """Extract publication date from page."""
        # Try JSON-LD first
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string)
                if isinstance(data, dict):
                    date_str = data.get("datePublished") or data.get("dateCreated")
                    if date_str:
                        # Parse ISO date
                        return date_str[:10]
            except (json.JSONDecodeError, TypeError):
                continue

        # Try meta tags
        for meta in soup.find_all("meta"):
            prop = meta.get("property", "") or meta.get("name", "")
            if prop in ["article:published_time", "date", "publish_date"]:
                content = meta.get("content", "")
                if content:
                    return content[:10]

        # Try to find date in page text (common patterns)
        # Look for text like "August 23, 2022" near the title
        h1 = soup.find("h1")
        if h1:
            # Check siblings or nearby text
            next_elem = h1.find_next_sibling()
            if next_elem:
                text = next_elem.get_text(strip=True)
                # Try to parse common date formats
                date_patterns = [
                    (r"(\w+ \d{1,2}, \d{4})", "%B %d, %Y"),  # August 23, 2022
                    (r"(\d{4}-\d{2}-\d{2})", "%Y-%m-%d"),    # 2022-08-23
                    (r"(\d{1,2}/\d{1,2}/\d{4})", "%m/%d/%Y"), # 08/23/2022
                ]
                for pattern, fmt in date_patterns:
                    match = re.search(pattern, text)
                    if match:
                        try:
                            dt = datetime.strptime(match.group(1), fmt)
                            return dt.strftime("%Y-%m-%d")
                        except ValueError:
                            continue

        return None

    def fetch_post(self, url: str) -> dict | None:
        """Fetch and parse a single post."""
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract date (before content manipulation)
            pub_date = self.extract_date_from_page(soup)

            # Extract content element first so we can find the title within it
            content_elem = None
            if self.content_selector:
                content_elem = soup.select_one(self.content_selector)
            if not content_elem:
                for selector in ["article", "main", ".post-content", ".content", ".entry-content"]:
                    content_elem = soup.select_one(selector)
                    if content_elem:
                        break
            if not content_elem:
                content_elem = soup.find("body")

            # Extract h1 from content BEFORE decomposing (it may be inside a <header>)
            content_h1 = content_elem.find("h1")

            # Remove header/footer/nav from content
            for tag in content_elem.find_all(["header", "footer", "nav", "script", "style"]):
                tag.decompose()

            # Extract title: prefer h1 inside content element, then fall
            # back to og:title, <title> tag, or page-level h1
            title = "Untitled"
            if content_h1:
                title = content_h1.get_text(strip=True)
            else:
                og_title = soup.find("meta", property="og:title")
                if og_title and og_title.get("content"):
                    title = og_title["content"]
                elif soup.title and soup.title.string:
                    # Strip common site name suffixes from <title>
                    # Use rsplit to only remove the last segment (the site name)
                    raw = soup.title.string.strip()
                    for sep in [" | ", " - ", " — ", " · "]:
                        if sep in raw:
                            title = raw.rsplit(sep, 1)[0].strip()
                            break
                    else:
                        title = raw
                else:
                    page_h1 = soup.find("h1")
                    if page_h1:
                        title = page_h1.get_text(strip=True)

            markdown = self.html_to_markdown(content_elem, self.base_url)

            return {
                "title": title,
                "url": url,
                "pub_date": pub_date,
                "markdown": markdown,
                "word_count": len(markdown.split())
            }

        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def make_slug(self, url: str) -> str:
        """Extract slug from URL."""
        # URL like https://nadia.xyz/agency -> agency
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
        """Scrape all posts from the Jekyll blog."""
        print(f"Fetching post URLs...")
        post_urls = self.fetch_post_urls()
        print(f"Found {len(post_urls)} posts")

        existing_filenames = self.get_existing_filenames()
        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        # Filter to new posts only
        posts_to_scrape = []
        for url in post_urls:
            # We need to fetch to get the date for filename, so check by slug
            slug = self.make_slug(url)
            # Check if any existing filename ends with this slug
            if not any(f.endswith(f"-{slug}.md") or f == f"{slug}.md" for f in existing_filenames):
                posts_to_scrape.append(url)

        if not posts_to_scrape:
            print("All posts already scraped!")
            return posts

        print(f"Scraping {len(posts_to_scrape)} new posts...")

        for i, url in enumerate(posts_to_scrape):
            print(f"[{i+1}/{len(posts_to_scrape)}] {url}...")

            post = self.fetch_post(url)
            if not post:
                continue

            post["filename"] = self.make_filename(post)
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
        print("Usage: BLOG_ID=nayafia python jekyll_static.py")
        sys.exit(1)

    scraper = JekyllStaticScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
