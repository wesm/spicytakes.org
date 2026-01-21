#!/usr/bin/env python3
"""
Jekyll Atom feed scraper for Spicy Takes platform.
Scrapes Jekyll blogs that provide Atom feeds (like geohot.github.io/blog).
Also fetches older posts from the homepage that aren't in the feed.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


class JekyllFeedScraper(BaseScraper):
    """Scraper for Jekyll blogs with Atom feeds."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "jekyll_feed":
            raise ValueError(f"Blog {blog_id} is not configured as jekyll_feed")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.feed_url = self.config["scraper"]["feedUrl"]
        self.homepage_url = self.config["scraper"].get("homepageUrl", self.base_url + "/blog/")
        # URL pattern to identify blog posts (regex pattern)
        self.url_pattern = self.config["scraper"].get("urlPattern", r"/\d{4}/\d{2}/\d{2}/")
        # Whether posts are in <li><h3><a> (True) or just <li><a> (False)
        self.posts_in_h3 = self.config["scraper"].get("postsInH3", True)
        # Optional: additional articles page (e.g., MkDocs Material site)
        self.articles_url = self.config["scraper"].get("articlesUrl")
        self.articles_base_url = self.config["scraper"].get("articlesBaseUrl", "")

        # Headers to appear as a regular browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_feed(self) -> list[dict]:
        """Fetch and parse posts from Atom feed. Returns list of post metadata."""
        try:
            response = requests.get(self.feed_url, timeout=30, headers=self.headers)
            response.raise_for_status()

            # Parse Atom feed
            root = ET.fromstring(response.content)

            # Handle Atom namespace
            ns = {"atom": "http://www.w3.org/2005/Atom"}

            posts = []
            for entry in root.findall("atom:entry", ns):
                title_elem = entry.find("atom:title", ns)
                link_elem = entry.find("atom:link", ns)
                published_elem = entry.find("atom:published", ns)
                content_elem = entry.find("atom:content", ns)

                title = title_elem.text if title_elem is not None else "Untitled"

                # Get URL from link element
                url = ""
                if link_elem is not None:
                    url = link_elem.get("href", "")

                # Make URL absolute if needed
                if url.startswith("/"):
                    url = self.base_url + url

                # Parse published date (ISO format: 2025-12-29T00:00:00+00:00)
                pub_date = None
                if published_elem is not None and published_elem.text:
                    pub_date = published_elem.text[:10]  # Get YYYY-MM-DD

                # Get content (HTML in CDATA)
                content_html = ""
                if content_elem is not None and content_elem.text:
                    content_html = content_elem.text

                posts.append({
                    "title": title,
                    "url": url,
                    "pub_date": pub_date,
                    "content_html": content_html
                })

            return posts
        except Exception as e:
            print(f"  Error fetching feed: {e}")
            return []

    def fetch_homepage_posts(self) -> list[dict]:
        """Fetch and parse posts from homepage. Returns list of post metadata."""
        try:
            response = requests.get(self.homepage_url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            posts = []
            # Posts are in <li> elements, possibly with <h3><a> or just <a>
            for li in soup.find_all("li"):
                if self.posts_in_h3:
                    h3 = li.find("h3")
                    if not h3:
                        continue
                    link = h3.find("a")
                else:
                    # Direct <a> inside <li>
                    link = li.find("a")

                if not link:
                    continue

                href = link.get("href", "")
                title = link.get_text(strip=True)

                # Only include posts matching the URL pattern
                if not re.search(self.url_pattern, href):
                    continue

                # Make URL absolute
                if href.startswith("/"):
                    url = self.base_url + href
                else:
                    url = href

                posts.append({
                    "title": title,
                    "url": url,
                    "pub_date": self.parse_date_from_url(url),
                    "content_html": None  # Will fetch from individual page
                })

            return posts
        except Exception as e:
            print(f"  Error fetching homepage: {e}")
            return []

    def fetch_articles_page(self) -> list[dict]:
        """Fetch articles from a separate articles page (e.g., MkDocs Material site)."""
        if not self.articles_url:
            return []

        try:
            response = requests.get(self.articles_url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            posts = []
            # MkDocs Material articles: look for links with dates in text
            # Format: "Title YYYY-MM-DD description..."
            for link in soup.find_all("a", href=True):
                href = link.get("href", "")
                text = link.get_text(strip=True)

                # Skip navigation/non-article links
                if not href.startswith("../") and not href.startswith("/"):
                    continue
                if href in ["../", "/", "../articles/", "#"]:
                    continue

                # Look for date pattern in text (YYYY-MM-DD)
                date_match = re.search(r"(\d{4}-\d{2}-\d{2})", text)
                if not date_match:
                    continue

                pub_date = date_match.group(1)

                # Extract title (text before the date)
                title = text[:date_match.start()].strip()
                if not title:
                    continue

                # Build absolute URL
                if href.startswith("../"):
                    url = self.articles_base_url + "/" + href[3:].rstrip("/") + "/"
                elif href.startswith("/"):
                    url = self.articles_base_url + href
                else:
                    url = href

                # Normalize URL
                url = url.rstrip("/") + "/"

                posts.append({
                    "title": title,
                    "url": url,
                    "pub_date": pub_date,
                    "content_html": None
                })

            return posts
        except Exception as e:
            print(f"  Error fetching articles page: {e}")
            return []

    def fetch_post_page(self, url: str) -> str | None:
        """Fetch a single post page and extract HTML content."""
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Find main content - try various selectors
            content_elem = None

            # MkDocs Material uses md-content__inner
            content_elem = soup.find("div", class_="md-content__inner")
            if not content_elem:
                # Jekyll blogs typically use <article> or <main>
                content_elem = soup.find("article") or soup.find("main")
            if not content_elem:
                # Try finding post-content div
                content_elem = soup.find("div", class_="post-content")
            if not content_elem:
                print(f"  Warning: Falling back to <body> for {url} - may include nav/footer")
                content_elem = soup.find("body")

            if content_elem:
                return str(content_elem)
            return None
        except Exception as e:
            print(f"  Error fetching post page {url}: {e}")
            return None

    def parse_date_from_url(self, url: str) -> str | None:
        """Extract date from Jekyll URL pattern /YYYY/MM/DD/slug.html"""
        match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        return None

    def extract_slug_from_url(self, url: str) -> str:
        """Extract slug from URL like /blog/jekyll/update/2025/12/29/five-years-of-tinygrad.html"""
        # Remove .html extension and get the last path segment
        slug_match = re.search(r"/([^/]+?)(?:\.html)?$", url.rstrip("/"))
        return slug_match.group(1) if slug_match else "unknown"

    def _inline_to_markdown(self, element) -> str:
        """Convert inline HTML elements to markdown, preserving links and formatting."""
        if isinstance(element, str):
            return element

        if not hasattr(element, 'name'):
            return str(element) if element else ""

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

        # For other inline elements, recurse into children
        if hasattr(element, 'children'):
            return "".join(self._inline_to_markdown(c) for c in element.children)

        return element.get_text() if hasattr(element, 'get_text') else str(element)

    def _get_direct_text(self, element, exclude_tags: list[str] | None = None) -> str:
        """Get text from element, excluding specified nested tags, preserving inline formatting."""
        exclude_tags = exclude_tags or []
        parts = []

        for child in element.children:
            if isinstance(child, str):
                parts.append(child)
            elif hasattr(child, 'name'):
                if child.name in exclude_tags:
                    continue
                parts.append(self._inline_to_markdown(child))

        return " ".join(parts).strip()

    def html_to_markdown(self, html_content: str) -> str:
        """Convert HTML content to markdown."""
        soup = BeautifulSoup(html_content, "html.parser")
        lines = []

        def process_element(elem, depth=0):
            """Recursively process an element and its children."""
            if isinstance(elem, str):
                return

            if not hasattr(elem, 'name'):
                return

            tag = elem.name

            if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                level = int(tag[1])
                text = self._get_direct_text(elem)
                if text:
                    lines.append(f"{'#' * level} {text}")
                    lines.append("")

            elif tag == "p":
                text = self._get_direct_text(elem)
                if text:
                    lines.append(text)
                    lines.append("")

            elif tag == "blockquote":
                text = self._get_direct_text(elem)
                if text:
                    quoted = "\n".join(f"> {line}" for line in text.split("\n") if line.strip())
                    lines.append(quoted)
                    lines.append("")

            elif tag == "pre":
                # Preserve whitespace in code blocks
                code_elem = elem.find("code")
                if code_elem:
                    code = code_elem.get_text()
                else:
                    code = elem.get_text()
                # Strip only leading/trailing newlines, preserve internal indentation
                code = code.strip("\n")
                lines.append("```")
                lines.append(code)
                lines.append("```")
                lines.append("")

            elif tag in ["ul", "ol"]:
                for i, li in enumerate(elem.find_all("li", recursive=False)):
                    prefix = "*" if tag == "ul" else f"{i+1}."
                    # Get only direct text, exclude nested ul/ol
                    text = self._get_direct_text(li, exclude_tags=["ul", "ol"])
                    if text:
                        lines.append(f"{prefix} {text}")
                    # Process nested lists with indentation (simplified - just recurse)
                    for nested_list in li.find_all(["ul", "ol"], recursive=False):
                        for nested_li in nested_list.find_all("li", recursive=False):
                            nested_text = self._get_direct_text(nested_li, exclude_tags=["ul", "ol"])
                            if nested_text:
                                lines.append(f"  * {nested_text}")
                lines.append("")

            elif tag in ["div", "article", "section", "main"]:
                for child in elem.children:
                    process_element(child, depth + 1)

        for child in soup.children:
            process_element(child)

        # If no block elements found, just extract all text
        if not lines:
            text = soup.get_text(separator="\n", strip=True)
            lines = [text]

        # Join with newlines, collapse multiple blank lines
        result = "\n".join(lines)
        result = re.sub(r"\n{3,}", "\n\n", result)
        return result.strip()

    def process_post(self, post_meta: dict) -> dict | None:
        """Process a post from feed data into structured format."""
        url = post_meta["url"]
        title = post_meta["title"]
        date_str = post_meta.get("pub_date") or self.parse_date_from_url(url)
        content_html = post_meta.get("content_html", "")

        # Convert HTML to markdown
        content = self.html_to_markdown(content_html)

        if not content or len(content.strip()) < 50:
            print(f"  Warning: Very short content for {url}")

        slug = self.extract_slug_from_url(url)

        return {
            "title": title,
            "date": date_str,
            "url": url,
            "slug": slug,
            "content": content,
            "word_count": len(content.split())
        }

    def scrape(self):
        """Main scrape method."""
        print(f"Scraping {self.config['name']}...")
        print(f"Feed URL: {self.feed_url}")

        # Fetch from Atom feed (has full content for recent posts)
        print("\nFetching feed posts...")
        feed_posts = self.fetch_feed()
        print(f"  Found {len(feed_posts)} posts in feed")

        # Build dict of feed posts by URL for quick lookup
        feed_posts_by_url = {p["url"]: p for p in feed_posts}

        # Fetch from homepage (has all posts but no content)
        print("\nFetching homepage posts...")
        homepage_posts = self.fetch_homepage_posts()
        print(f"  Found {len(homepage_posts)} posts on homepage")

        # Fetch from articles page if configured (e.g., MkDocs Material site)
        articles_posts = []
        if self.articles_url:
            print("\nFetching articles page...")
            articles_posts = self.fetch_articles_page()
            print(f"  Found {len(articles_posts)} posts on articles page")

        # Merge: use feed content when available, otherwise fetch from page
        all_post_metas = []
        seen_urls = set()

        # First add all feed posts (they have content)
        for post in feed_posts:
            all_post_metas.append(post)
            seen_urls.add(post["url"])

        # Then add homepage posts not in feed
        for post in homepage_posts:
            if post["url"] not in seen_urls:
                all_post_metas.append(post)
                seen_urls.add(post["url"])

        # Then add articles posts not already seen
        for post in articles_posts:
            if post["url"] not in seen_urls:
                all_post_metas.append(post)
                seen_urls.add(post["url"])

        print(f"\nTotal unique posts: {len(all_post_metas)}")

        # Load existing index to avoid re-scraping
        existing_slugs = self.get_existing_slugs()

        # Process each post
        new_posts = []

        for i, post_meta in enumerate(all_post_metas):
            url = post_meta["url"]
            title = post_meta["title"]
            slug = self.extract_slug_from_url(url)

            if slug in existing_slugs:
                print(f"  Skipping {slug} (already scraped)")
                continue

            print(f"\n[{i+1}/{len(all_post_metas)}] Processing: {title}")

            # If no content_html, fetch from page
            if not post_meta.get("content_html"):
                time.sleep(REQUEST_DELAY)
                content_html = self.fetch_post_page(url)
                if content_html:
                    post_meta["content_html"] = content_html
                else:
                    print(f"  Warning: Could not fetch content for {url}")
                    continue

            post = self.process_post(post_meta)

            if post:
                # Create filename
                date_str = post.get("date")
                if date_str:
                    filename = f"{date_str}-{slug}.md"
                else:
                    filename = f"{slug}.md"

                post["filename"] = filename

                # Create frontmatter content
                escaped_title = post['title'].replace('"', '\\"')
                frontmatter = f"""---
title: "{escaped_title}"
date: {post['date'] or 'unknown'}
url: {post['url']}
slug: {post['slug']}
word_count: {post['word_count']}
---

{post['content']}
"""
                post["content"] = frontmatter

                self.save_post(post)
                new_posts.append(post)
                print(f"  Saved: {filename} ({post['word_count']} words)")

        # Update index with new posts
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])

        for post in new_posts:
            all_posts.append({
                "slug": post["slug"],
                "title": post["title"],
                "date": post["date"],
                "url": post["url"],
                "word_count": post["word_count"],
                "filename": post["filename"]
            })

        # Sort by date descending
        all_posts.sort(key=lambda p: p.get("date") or "", reverse=True)

        self.save_index(all_posts)
        print(f"\nDone! Scraped {len(new_posts)} new posts.")
        return all_posts


if __name__ == "__main__":
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=geohot python scripts/scrapers/jekyll_feed.py")
        sys.exit(1)

    scraper = JekyllFeedScraper(blog_id)
    scraper.scrape()
