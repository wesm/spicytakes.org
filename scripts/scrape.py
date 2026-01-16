#!/usr/bin/env python3
"""
Scraper for Benn Stancil's Substack posts.
Downloads all posts and saves them as markdown files with metadata.
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# Configuration
BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / "posts"
DATA_DIR = BASE_DIR / "data"
URLS_FILE = DATA_DIR / "post_urls.json"
INDEX_FILE = DATA_DIR / "posts_index.json"

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests

def load_urls():
    """Load post URLs from the JSON file."""
    with open(URLS_FILE) as f:
        data = json.load(f)
    return data["posts"]


def fetch_post(url: str) -> dict | None:
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
            # Handle ISO format with timezone
            if "T" in date_str:
                # Remove timezone for simpler parsing
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
    content = html_to_markdown(content_div)

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


def html_to_markdown(element) -> str:
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
            # Recursively process nested containers
            nested = html_to_markdown(child)
            if nested.strip():
                lines.append(nested)

        elif tag == "figure":
            # Handle figures (usually images with captions)
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


def save_post(post: dict) -> str:
    """Save a post as a markdown file with YAML frontmatter."""
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    # Create filename from date and slug
    if post["date"]:
        date_prefix = post["date"][:10]
        filename = f"{date_prefix}-{post['slug']}.md"
    else:
        filename = f"{post['slug']}.md"

    filepath = POSTS_DIR / filename

    # Create frontmatter - escape quotes for YAML
    escaped_title = post['title'].replace('"', "'")
    frontmatter = [
        "---",
        f'title: "{escaped_title}"',
    ]
    if post["subtitle"]:
        escaped_subtitle = post['subtitle'].replace('"', "'")
        frontmatter.append(f'subtitle: "{escaped_subtitle}"')
    if post["date"]:
        frontmatter.append(f"date: {post['date']}")
    frontmatter.extend([
        f"url: {post['url']}",
        f"slug: {post['slug']}",
        f"word_count: {post['word_count']}",
        "---",
        ""
    ])

    content = "\n".join(frontmatter) + "\n" + post["content"]

    with open(filepath, "w") as f:
        f.write(content)

    return str(filepath)


def load_existing_index() -> dict:
    """Load existing index if it exists."""
    if INDEX_FILE.exists():
        with open(INDEX_FILE) as f:
            return json.load(f)
    return {"posts": [], "last_updated": None}


def save_index(posts: list):
    """Save the post index."""
    index = {
        "total_posts": len(posts),
        "last_updated": datetime.now().isoformat(),
        "posts": posts
    }
    with open(INDEX_FILE, "w") as f:
        json.dump(index, f, indent=2)


def main():
    """Main scraping function."""
    print("Benn Stancil Substack Scraper")
    print("=" * 40)

    # Load URLs
    urls = load_urls()
    print(f"Found {len(urls)} posts to scrape")

    # Load existing index to skip already scraped posts
    existing = load_existing_index()
    existing_slugs = {p["slug"] for p in existing.get("posts", [])}

    # Filter to only new posts
    urls_to_scrape = [u for u in urls if u.split("/p/")[-1].rstrip("/") not in existing_slugs]

    if not urls_to_scrape:
        print("All posts already scraped!")
        return

    print(f"Scraping {len(urls_to_scrape)} new posts...")

    posts = existing.get("posts", [])

    for i, url in enumerate(urls_to_scrape):
        print(f"[{i+1}/{len(urls_to_scrape)}] {url}")

        post = fetch_post(url)
        if post:
            filepath = save_post(post)
            print(f"  Saved: {filepath}")

            # Add to index (without full content)
            index_entry = {k: v for k, v in post.items() if k != "content"}
            posts.append(index_entry)

            # Save index periodically
            if (i + 1) % 10 == 0:
                save_index(posts)
                print(f"  Index saved ({len(posts)} posts)")

        # Rate limiting
        time.sleep(REQUEST_DELAY)

    # Final save
    save_index(posts)
    print(f"\nDone! Scraped {len(urls_to_scrape)} posts.")
    print(f"Total posts in index: {len(posts)}")


if __name__ == "__main__":
    main()
