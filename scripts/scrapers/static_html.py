#!/usr/bin/env python3
"""
Static HTML blog scraper for Spicy Takes platform.
Scrapes blogs served as plain HTML pages (like danluu.com).
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

# Rate limiting
REQUEST_DELAY = 1.5  # seconds between requests


class StaticHtmlScraper(BaseScraper):
    """Scraper for static HTML blogs like danluu.com."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "static_html":
            raise ValueError(f"Blog {blog_id} is not configured as static_html")

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.index_url = self.config["scraper"].get("indexUrl", self.base_url)

        # Headers to appear as a regular browser
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

    def get_post_urls_danluu(self, soup: BeautifulSoup) -> list[dict]:
        """
        Extract public post URLs from danluu.com index page.
        Stops at the Patreon divider (hr#pt element or text marker).
        Returns list of {url, date_str, title} dicts.
        """
        posts = []

        # Find all list items, stopping when we hit the Patreon section
        # The structure is: <li>...</li>... ↑ Public posts <hr id=pt> ↓Patreon posts
        for li in soup.find_all("li"):
            # DOM-aware check: if this li has hr#pt as a previous sibling, we're in Patreon section
            if li.find_previous("hr", id="pt") is not None:
                if len(posts) > 0:
                    print(f"  Found Patreon section (hr#pt), stopping. Got {len(posts)} public posts.")
                break

            # Fallback: check for exact marker text if hr#pt is missing
            # Only match marker-only items, not posts with "Patreon" in the title
            li_text = li.get_text(strip=True)
            link = li.find("a")

            # Navigation link to Patreon section - skip but continue
            if link and link.get("href") == "#pt":
                continue

            # Exact marker patterns that indicate start of Patreon section
            # These should be short marker-only lines, not full post titles
            is_patreon_marker = (
                li_text == "↓Patreon posts" or
                li_text.startswith("↓Patreon") or
                (link and link.get("href", "").startswith("https://www.patreon.com/"))
            )
            if is_patreon_marker:
                if len(posts) > 0:
                    print(f"  Found Patreon section (text marker), stopping. Got {len(posts)} public posts.")
                break

            # Skip if no valid link
            if not link or not link.get("href"):
                continue

            href = link.get("href")
            title = link.get_text(strip=True)

            # Skip external links (Patreon links)
            if href.startswith("http") and "danluu.com" not in href:
                continue

            # Skip non-post links
            if href in ["/", "#", ""] or href.startswith("mailto:"):
                continue

            # Normalize URL
            if href.startswith("/"):
                url = f"{self.base_url}{href}"
            elif not href.startswith("http"):
                url = f"{self.base_url}/{href}"
            else:
                url = href

            # Extract date (MM/YY format) from the li text
            text = li.get_text()
            date_match = re.search(r"(\d{1,2})/(\d{2})", text)
            date_str = None
            if date_match:
                month = int(date_match.group(1))
                year = int(date_match.group(2))
                # Convert YY to YYYY (assume 20xx for years < 50, 19xx otherwise)
                full_year = 2000 + year if year < 50 else 1900 + year
                date_str = f"{full_year}-{month:02d}-01"

            posts.append({
                "url": url.rstrip("/") + "/",
                "title": title,
                "date_str": date_str
            })

        return posts

    def fetch_post(self, url: str, date_str: str | None) -> dict | None:
        """Fetch and parse a single blog post."""
        soup = self.fetch_page(url)
        if not soup:
            return None

        # Extract title - usually the first h1 or a specific pattern
        title_elem = soup.find("h1")
        if not title_elem:
            # Try finding title in a header-like element
            title_elem = soup.find("title")
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # Clean up title (remove site name suffix if present)
        title = re.sub(r"\s*[-|]\s*Dan Luu\s*$", "", title, flags=re.IGNORECASE)

        # Find main content - Dan Luu's posts use minimal HTML
        # Try <main> first, then <body>, then the whole document
        content_elem = soup.find("main")
        if not content_elem:
            content_elem = soup.find("body")
        if not content_elem:
            # Use the html element or the soup itself for minimal HTML pages
            content_elem = soup.find("html") or soup

        # Convert to markdown, skipping nav elements
        content = self.html_to_markdown(content_elem, skip_nav=True)

        # Extract slug from URL
        slug = url.rstrip("/").split("/")[-1]

        return {
            "url": url,
            "slug": slug,
            "title": title,
            "date": date_str,
            "content": content,
            "word_count": len(content.split())
        }

    def html_to_markdown(self, element, skip_nav: bool = False, depth: int = 0) -> str:
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

            # Skip navigation, header, footer elements
            if skip_nav and tag in ["nav", "header", "footer"]:
                continue

            # Skip elements with nav-like classes
            if skip_nav and child.get("class"):
                classes = " ".join(child.get("class", []))
                if any(x in classes.lower() for x in ["nav", "menu", "footer", "header"]):
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

            elif tag == "code" and child.parent and child.parent.name != "pre":
                text = child.get_text(strip=True)
                if text:
                    lines.append(f"`{text}`")

            elif tag == "a":
                text = child.get_text(strip=True)
                href = child.get("href", "")
                if text and href and not href.startswith("#"):
                    # Don't linkify if it's just the URL text
                    if text == href:
                        lines.append(href)
                    else:
                        lines.append(f"[{text}]({href})")
                elif text:
                    lines.append(text)

            elif tag == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                if src:
                    lines.append(f"\n![{alt}]({src})\n")

            elif tag in ["div", "section", "article", "main"]:
                nested = self.html_to_markdown(child, skip_nav=skip_nav, depth=depth+1)
                if nested.strip():
                    lines.append(nested)

            elif tag == "table":
                # Simple table handling
                lines.append("\n[Table]\n")
                for row in child.find_all("tr"):
                    cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                    if cells:
                        lines.append("| " + " | ".join(cells) + " |")
                lines.append("")

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
        """Scrape all public posts."""
        print(f"Fetching index from {self.index_url}...")
        soup = self.fetch_page(self.index_url)
        if not soup:
            print("Failed to fetch index page")
            return []

        # Get post URLs (danluu-specific logic)
        post_infos = self.get_post_urls_danluu(soup)
        print(f"Found {len(post_infos)} public posts")

        # Filter out already-scraped posts
        existing_filenames = self.get_existing_filenames()
        existing_slugs = {f.split("-")[-1].replace(".md", "") for f in existing_filenames}

        to_scrape = [p for p in post_infos if p["url"].rstrip("/").split("/")[-1] not in existing_slugs]

        if not to_scrape:
            print("All posts already scraped!")
            existing = self.load_existing_index()
            return existing.get("posts", [])

        print(f"Scraping {len(to_scrape)} new posts...")

        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        for i, info in enumerate(to_scrape):
            url = info["url"]
            print(f"[{i+1}/{len(to_scrape)}] {url}")

            post = self.fetch_post(url, info.get("date_str"))
            if post:
                # Use the title from index if we got one
                if info.get("title") and post["title"] == "Untitled":
                    post["title"] = info["title"]

                # Create filename
                slug = post["slug"]
                if post.get("date"):
                    filename = f"{post['date'][:10]}-{slug}.md"
                else:
                    filename = f"{slug}.md"

                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                # Add to index
                index_entry = {k: v for k, v in post.items() if k != "content"}
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
        print("Usage: BLOG_ID=danluu python static_html.py")
        sys.exit(1)

    scraper = StaticHtmlScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
