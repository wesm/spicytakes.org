#!/usr/bin/env python3
"""
RSS + Next.js scraper for Spicy Takes platform.
Scrapes blogs that have RSS feeds with links (no content) and Next.js-rendered pages.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime

import requests
from bs4 import BeautifulSoup, NavigableString

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class RssNextjsScraper(BaseScraper):
    """Scraper for Next.js blogs with RSS feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "rss_nextjs":
            raise ValueError(f"Blog {blog_id} is not configured as rss_nextjs")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.feed_url = self.config["scraper"]["feedUrl"]
        # CSS selector for the main content
        self.content_selector = self.config["scraper"].get("contentSelector", "div.prose")

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_feed(self) -> list[dict]:
        """Fetch and parse posts from RSS feed."""
        try:
            response = requests.get(self.feed_url, timeout=30, headers=self.headers)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            channel = root.find("channel")
            if channel is None:
                print("  Error: No channel found in RSS feed")
                return []

            posts = []
            for item in channel.findall("item"):
                title_elem = item.find("title")
                link_elem = item.find("link")
                pub_date_elem = item.find("pubDate")

                title = title_elem.text if title_elem is not None else "Untitled"
                url = link_elem.text if link_elem is not None else ""

                # Parse RFC 2822 date format
                pub_date = None
                if pub_date_elem is not None and pub_date_elem.text:
                    try:
                        dt = parsedate_to_datetime(pub_date_elem.text)
                        pub_date = dt.strftime("%Y-%m-%d")
                    except Exception:
                        pass

                if url:
                    posts.append({
                        "title": title,
                        "url": url,
                        "pub_date": pub_date
                    })

            return posts
        except Exception as e:
            print(f"  Error fetching feed: {e}")
            return []

    def fetch_post_content(self, url: str) -> str | None:
        """Fetch a post page and extract the content."""
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Try the configured selector
            content = soup.select_one(self.content_selector)
            if not content:
                # Fallback to article or main
                content = soup.find("article") or soup.find("main")

            if content:
                return self.html_to_markdown(content)
            else:
                print(f"    Warning: Could not find content for {url}")
                return None
        except Exception as e:
            print(f"    Error fetching {url}: {e}")
            return None

    def _inline_to_markdown(self, element) -> str:
        """Convert inline HTML elements to markdown."""
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
                # Make relative URLs absolute
                if href.startswith("/"):
                    href = self.base_url + href
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

        return "".join(self._inline_to_markdown(c) for c in element.children)

    def _get_direct_text(self, element, exclude_tags=None) -> str:
        """Get text content with inline formatting."""
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
                lines.append("")

            elif tag == "pre":
                code_elem = child.find("code")
                if code_elem:
                    # Try to get language from class
                    classes = code_elem.get("class", [])
                    lang = ""
                    for c in classes:
                        if c.startswith("language-"):
                            lang = c.replace("language-", "")
                            break
                    code = code_elem.get_text()
                else:
                    lang = ""
                    code = child.get_text()
                lines.append(f"\n```{lang}\n{code}\n```\n")

            elif tag == "a":
                text = child.get_text(strip=True)
                href = child.get("href", "")
                if text and href and not href.startswith("#"):
                    if href.startswith("/"):
                        href = self.base_url + href
                    lines.append(f"[{text}]({href})")

            elif tag == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                if src:
                    if src.startswith("/"):
                        src = self.base_url + src
                    lines.append(f"\n![{alt}]({src})\n")

            elif tag in ["div", "section", "article", "span", "figure"]:
                nested = self.html_to_markdown(child)
                if nested.strip():
                    lines.append(nested)

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

        return "\n".join(lines)

    def make_slug(self, url: str) -> str:
        """Extract slug from URL."""
        # URLs like https://mitchellh.com/writing/slug or https://mitchellh.com/zig/slug
        path = url.rstrip("/").split("/")[-1]
        return path

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
        """Scrape all posts from the blog."""
        print(f"Fetching posts from RSS feed...")
        feed_posts = self.fetch_feed()
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

            # Fetch content from the post page
            markdown = self.fetch_post_content(post["url"])
            if markdown:
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

            # Add to index
            index_entry = {
                "filename": post["filename"],
                "title": post["title"],
                "url": post["url"],
                "pub_date": post.get("pub_date"),
                "word_count": post.get("word_count", 0)
            }
            posts.append(index_entry)

            # Save index periodically
            if (i + 1) % 10 == 0:
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
        print("Usage: BLOG_ID=mitchellh python rss_nextjs.py")
        sys.exit(1)

    scraper = RssNextjsScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
