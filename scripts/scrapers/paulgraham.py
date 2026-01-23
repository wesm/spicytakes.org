#!/usr/bin/env python3
"""
Paul Graham essays scraper for Spicy Takes platform.
Scrapes essays from paulgraham.com.
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
REQUEST_DELAY = 1.5  # seconds between requests


class PaulGrahamScraper(BaseScraper):
    """Scraper for paulgraham.com essays."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "paulgraham":
            raise ValueError(f"Blog {blog_id} is not configured as paulgraham type")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.index_url = self.config["scraper"]["indexUrl"]

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_page(self, url: str) -> BeautifulSoup | None:
        """Fetch a page and return parsed BeautifulSoup."""
        try:
            response = requests.get(url, timeout=30, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def get_essay_urls(self, soup: BeautifulSoup) -> list[dict]:
        """
        Extract essay URLs from the articles index page.
        Returns list of {url, title} dicts.
        """
        essays = []
        seen_urls = set()

        # Find all links on the page
        for link in soup.find_all("a"):
            href = link.get("href", "")
            title = link.get_text(strip=True)

            # Skip empty or external links
            if not href or not title:
                continue
            if href.startswith("http") and "paulgraham.com" not in href:
                continue
            if href.startswith("#") or href.startswith("mailto:"):
                continue

            # Only include .html files (essays)
            if not href.endswith(".html"):
                continue

            # Skip the articles index itself and other non-essay pages
            skip_pages = ["articles.html", "index.html", "rss.html", "arc.html",
                         "hierarchies.html", "hierarchiesalisp.html", "hierarchiesalisp2.html"]
            if href in skip_pages:
                continue

            # Build full URL
            if href.startswith("/"):
                url = f"{self.base_url}{href}"
            elif not href.startswith("http"):
                url = f"{self.base_url}/{href}"
            else:
                url = href

            # Deduplicate
            if url in seen_urls:
                continue
            seen_urls.add(url)

            essays.append({
                "url": url,
                "title": title,
                "slug": href.replace(".html", "")
            })

        return essays

    def extract_date(self, soup: BeautifulSoup, text_content: str) -> str | None:
        """Extract publication date from essay page."""
        # Paul Graham's essays often have dates like "January 2023" or "March 2004"
        # Usually near the top of the page

        # Common date patterns
        month_pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})"

        # First try to find it in the first 500 chars of content
        match = re.search(month_pattern, text_content[:1000])
        if match:
            month_name = match.group(1)
            year = int(match.group(2))

            # Convert month name to number
            months = {
                "January": 1, "February": 2, "March": 3, "April": 4,
                "May": 5, "June": 6, "July": 7, "August": 8,
                "September": 9, "October": 10, "November": 11, "December": 12
            }
            month = months.get(month_name, 1)

            return f"{year}-{month:02d}-01"

        return None

    def extract_title(self, soup: BeautifulSoup, fallback_title: str) -> str:
        """Extract essay title from the page."""
        # Try <title> tag first
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)
            # Clean up common suffixes
            title = re.sub(r"\s*[-|]\s*Paul Graham\s*$", "", title, flags=re.IGNORECASE)
            if title and title.lower() not in ["paul graham", ""]:
                return title

        # Try finding title in an image alt text (PG uses image titles)
        for img in soup.find_all("img"):
            alt = img.get("alt", "")
            src = img.get("src", "")
            # Title images are usually from turbifycdn
            if "turbifycdn" in src and alt and len(alt) > 3:
                return alt

        # Try first h1
        h1 = soup.find("h1")
        if h1:
            return h1.get_text(strip=True)

        # Fall back to the title from the index page
        return fallback_title

    def fetch_essay(self, url: str, index_title: str) -> dict | None:
        """Fetch and parse a single essay."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Get the raw text for date extraction
        body = soup.find("body")
        if not body:
            body = soup
        raw_text = body.get_text()

        # Extract metadata
        title = self.extract_title(soup, index_title)
        date_str = self.extract_date(soup, raw_text)

        # Extract content
        content = self.html_to_markdown(body)

        # Extract slug from URL
        slug = url.rstrip("/").split("/")[-1].replace(".html", "")

        return {
            "url": url,
            "slug": slug,
            "title": title,
            "date": date_str,
            "content": content,
            "word_count": len(content.split())
        }

    def html_to_markdown(self, element) -> str:
        """Convert HTML content to markdown."""
        lines = []

        for child in element.children:
            if isinstance(child, str):
                text = child.strip()
                if text:
                    lines.append(text)
                continue

            if not hasattr(child, 'name'):
                continue

            tag = child.name

            # Skip scripts, styles, etc
            if tag in ["script", "style", "noscript", "iframe"]:
                continue

            if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                level = int(tag[1])
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"\n{'#' * level} {text}\n")

            elif tag == "p":
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"\n{text}\n")

            elif tag == "blockquote":
                text = child.get_text(strip=True)
                if text:
                    quoted = "\n".join(f"> {line}" for line in text.split("\n") if line.strip())
                    lines.append(f"\n{quoted}\n")

            elif tag in ["ul", "ol"]:
                for i, li in enumerate(child.find_all("li", recursive=False)):
                    prefix = "-" if tag == "ul" else f"{i+1}."
                    text = li.get_text(strip=True)
                    if text:
                        lines.append(f"{prefix} {text}")
                lines.append("")

            elif tag == "pre":
                code = child.get_text()
                lines.append(f"\n```\n{code}\n```\n")

            elif tag == "a":
                text = child.get_text(strip=True)
                href = child.get("href", "")
                if text and href and not href.startswith("#"):
                    lines.append(f"[{text}]({href})")
                elif text:
                    lines.append(text)

            elif tag == "img":
                # Skip decorative images (spacers, etc)
                src = child.get("src", "")
                alt = child.get("alt", "")
                if "spacer" in src.lower() or not alt:
                    continue
                if src:
                    lines.append(f"\n![{alt}]({src})\n")

            elif tag in ["div", "section", "article", "main", "td", "tr", "table", "font", "center"]:
                nested = self.html_to_markdown(child)
                if nested.strip():
                    lines.append(nested)

            elif tag == "hr":
                lines.append("\n---\n")

            elif tag in ["em", "i"]:
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"*{text}*")

            elif tag in ["strong", "b"]:
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"**{text}**")

            elif tag == "br":
                lines.append("\n")

            elif tag in ["span", "small"]:
                text = child.get_text(strip=True)
                if text:
                    lines.append(text)

        result = "\n".join(lines)
        # Clean up excessive newlines
        result = re.sub(r"\n{3,}", "\n\n", result)
        return result

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post['title'].replace('"', "'")
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
            ""
        ])
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all essays."""
        print(f"Fetching index from {self.index_url}...")
        soup = self.fetch_page(self.index_url)
        if not soup:
            print("Failed to fetch index page")
            return []

        # Get essay URLs
        essay_infos = self.get_essay_urls(soup)
        print(f"Found {len(essay_infos)} essays")

        # Filter out already-scraped posts
        existing_slugs = self.get_existing_slugs()
        to_scrape = [e for e in essay_infos if e["slug"] not in existing_slugs]

        if not to_scrape:
            print("All essays already scraped!")
            existing = self.load_existing_index()
            return existing.get("posts", [])

        print(f"Scraping {len(to_scrape)} new essays...")

        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        for i, info in enumerate(to_scrape):
            url = info["url"]
            print(f"[{i+1}/{len(to_scrape)}] {info['title'][:50]}...")

            essay = self.fetch_essay(url, info["title"])
            if essay:
                # Create filename
                slug = essay["slug"]
                if essay.get("date"):
                    filename = f"{essay['date'][:10]}-{slug}.md"
                else:
                    filename = f"{slug}.md"

                essay["filename"] = filename
                essay["content"] = self.make_post_content(essay)
                filepath = self.save_post(essay)
                print(f"  Saved: {filepath}")

                # Add to index
                index_entry = {k: v for k, v in essay.items() if k != "content"}
                posts.append(index_entry)

                # Save periodically
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
        print("Usage: BLOG_ID=paulg python paulgraham.py")
        sys.exit(1)

    scraper = PaulGrahamScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
