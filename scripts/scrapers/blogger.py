#!/usr/bin/env python3
"""
Blogger scraper for Spicy Takes platform.
Scrapes Blogger blogs using the Atom feed with pagination.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests
from bs4 import BeautifulSoup, NavigableString

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class BloggerScraper(BaseScraper):
    """Scraper for Blogger blogs with Atom feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "blogger":
            raise ValueError(f"Blog {blog_id} is not configured as blogger")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.feed_url = self.config["scraper"].get("feedUrl", f"{self.base_url}/feeds/posts/default")

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_all_posts_from_feed(self) -> list[dict]:
        """Fetch all posts from Atom feed with pagination."""
        all_posts = []
        start_index = 1
        max_results = 150  # Blogger allows up to 150 per request

        while True:
            url = f"{self.feed_url}?max-results={max_results}&start-index={start_index}"
            print(f"  Fetching posts {start_index} to {start_index + max_results - 1}...")

            try:
                response = requests.get(url, timeout=30, headers=self.headers)
                response.raise_for_status()

                # Parse Atom feed
                root = ET.fromstring(response.content)

                # Handle Atom namespace
                ns = {"atom": "http://www.w3.org/2005/Atom"}

                entries = root.findall("atom:entry", ns)
                if not entries:
                    break

                for entry in entries:
                    title_elem = entry.find("atom:title", ns)
                    published_elem = entry.find("atom:published", ns)
                    content_elem = entry.find("atom:content", ns)

                    # Get URL from alternate link
                    url = ""
                    for link in entry.findall("atom:link", ns):
                        if link.get("rel") == "alternate":
                            url = link.get("href", "")
                            break

                    title = title_elem.text if title_elem is not None else "Untitled"

                    # Parse published date
                    pub_date = None
                    if published_elem is not None and published_elem.text:
                        pub_date = published_elem.text[:10]  # Get YYYY-MM-DD

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

                print(f"    Got {len(entries)} posts")

                # Check if there are more posts
                if len(entries) < max_results:
                    break

                start_index += max_results
                time.sleep(REQUEST_DELAY)

            except Exception as e:
                print(f"  Error fetching feed: {e}")
                break

        return all_posts

    def _inline_to_markdown(self, element) -> str:
        """Convert inline HTML elements to markdown, preserving links and formatting."""
        if isinstance(element, str):
            return element

        if isinstance(element, NavigableString):
            return str(element)

        if not hasattr(element, 'name'):
            return str(element)

        tag = element.name

        if tag == "a":
            href = element.get("href", "")
            text = "".join(self._inline_to_markdown(c) for c in element.children)
            if href and text and not href.startswith("#"):
                return f"[{text}]({href})"
            return text

        if tag == "code":
            return f"`{element.get_text()}`"

        if tag in ["strong", "b"]:
            text = "".join(self._inline_to_markdown(c) for c in element.children)
            return f"**{text}**"

        if tag in ["em", "i"]:
            text = "".join(self._inline_to_markdown(c) for c in element.children)
            return f"*{text}*"

        if tag == "br":
            return "\n"

        # For other elements, recurse into children
        return "".join(self._inline_to_markdown(c) for c in element.children)

    def _get_direct_text(self, element, exclude_tags=None) -> str:
        """Get text content with inline formatting, excluding certain child tags."""
        if exclude_tags is None:
            exclude_tags = set()

        parts = []
        for child in element.children:
            if isinstance(child, NavigableString):
                parts.append(str(child))
            elif hasattr(child, 'name'):
                if child.name in exclude_tags:
                    continue
                parts.append(self._inline_to_markdown(child))
        return "".join(parts).strip()

    def html_to_markdown(self, element) -> str:
        """Convert HTML content to markdown."""
        lines = []

        for child in element.children:
            if isinstance(child, str):
                text = child.strip()
                if text:
                    lines.append(text)
                continue

            if isinstance(child, NavigableString):
                text = str(child).strip()
                if text:
                    lines.append(text)
                continue

            if not hasattr(child, 'name'):
                continue

            tag = child.name

            if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                level = int(tag[1])
                text = self._get_direct_text(child)
                if text:
                    lines.append(f"\n{'#' * level} {text}\n")

            elif tag == "p":
                text = self._get_direct_text(child)
                if text:
                    lines.append(f"\n{text}\n")

            elif tag == "blockquote":
                text = self._get_direct_text(child)
                if text:
                    quoted = "\n".join(f"> {line}" for line in text.split("\n") if line.strip())
                    lines.append(f"\n{quoted}\n")

            elif tag in ["ul", "ol"]:
                for i, li in enumerate(child.find_all("li", recursive=False)):
                    prefix = "-" if tag == "ul" else f"{i+1}."
                    text = self._get_direct_text(li, exclude_tags={"ul", "ol"})
                    if text:
                        lines.append(f"{prefix} {text}")
                    # Handle nested lists
                    for nested_list in li.find_all(["ul", "ol"], recursive=False):
                        nested_md = self.html_to_markdown(nested_list)
                        if nested_md.strip():
                            indented = "\n".join("  " + line for line in nested_md.split("\n") if line.strip())
                            lines.append(indented)
                lines.append("")

            elif tag == "pre":
                code = child.get_text()
                lines.append(f"\n```\n{code}\n```\n")

            elif tag == "a":
                text = child.get_text(strip=True)
                href = child.get("href", "")
                if text and href and not href.startswith("#"):
                    lines.append(f"[{text}]({href})")

            elif tag == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                if src:
                    lines.append(f"\n![{alt}]({src})\n")

            elif tag in ["div", "section", "article", "span"]:
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
                text = self._get_direct_text(child)
                if text:
                    lines.append(f"*{text}*")

            elif tag in ["strong", "b"]:
                text = self._get_direct_text(child)
                if text:
                    lines.append(f"**{text}**")

            elif tag == "table":
                # Basic table support
                lines.append("\n")
                for row in child.find_all("tr"):
                    cells = row.find_all(["td", "th"])
                    row_text = " | ".join(self._get_direct_text(c) for c in cells)
                    lines.append(f"| {row_text} |")
                lines.append("\n")

        return "\n".join(lines)

    def make_slug(self, url: str) -> str:
        """Extract slug from Blogger URL."""
        # Blogger URLs are like: https://www.elidedbranches.com/2025/11/revisiting-manager-readmes.html
        match = re.search(r'/(\d{4})/(\d{2})/([^/]+)\.html$', url)
        if match:
            return match.group(3)
        # Fallback: use last part of URL
        return url.rstrip("/").split("/")[-1].replace(".html", "")

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
        """Scrape all posts from the Blogger blog."""
        print(f"Fetching posts from feed...")
        feed_posts = self.fetch_all_posts_from_feed()
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
        print("Usage: BLOG_ID=skamille python blogger.py")
        sys.exit(1)

    scraper = BloggerScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
