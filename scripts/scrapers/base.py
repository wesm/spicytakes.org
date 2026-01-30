#!/usr/bin/env python3
"""
Base scraper interface for Spicy Takes platform.
All blog scrapers should inherit from BaseScraper.
"""

import json
import os
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Optional

from bs4 import NavigableString


def get_project_dir() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent


def get_blog_dir(blog_id: str) -> Path:
    """Get the directory for a specific blog."""
    return get_project_dir() / "blogs" / blog_id


def load_config(blog_id: str) -> dict:
    """Load configuration for a blog from config/{blog_id}.json."""
    config_path = get_project_dir() / "config" / f"{blog_id}.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    with open(config_path) as f:
        return json.load(f)


class BaseScraper(ABC):
    """Abstract base class for blog scrapers."""

    def __init__(self, blog_id: str):
        self.blog_id = blog_id
        self.config = load_config(blog_id)
        self.blog_dir = get_blog_dir(blog_id)
        self.posts_dir = self.blog_dir / "posts"
        self.data_dir = self.blog_dir / "data"

        # Create directories if they don't exist
        self.posts_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def scrape(self) -> list[dict]:
        """
        Scrape posts and return a list of post dicts.
        Each post should have at minimum:
        - filename: str (e.g., '2024-01-15-slug.md')
        - content: str (markdown content)
        """
        pass

    def save_post(self, post: dict) -> str:
        """Save a post as a markdown file. Returns the filepath."""
        filename = post.get("filename")
        if not filename:
            raise ValueError("Post must have a 'filename' field")

        filepath = self.posts_dir / filename
        content = post.get("content", "")

        with open(filepath, "w") as f:
            f.write(content)

        return str(filepath)

    def load_existing_index(self) -> dict:
        """Load existing posts index if it exists."""
        index_file = self.data_dir / "posts_index.json"
        if index_file.exists():
            with open(index_file) as f:
                return json.load(f)
        return {"posts": [], "last_updated": None}

    def save_index(self, posts: list):
        """Save the posts index."""
        index_file = self.data_dir / "posts_index.json"
        sorted_posts = sorted(posts, key=lambda p: p.get("pub_date", ""), reverse=True)
        index = {
            "total_posts": len(sorted_posts),
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "posts": sorted_posts
        }
        with open(index_file, "w") as f:
            json.dump(index, f, indent=2)
            f.write("\n")

    def get_existing_slugs(self) -> set[str]:
        """Get set of already-scraped post slugs."""
        existing = self.load_existing_index()
        return {p.get("slug", "") for p in existing.get("posts", [])}

    def get_existing_filenames(self) -> set[str]:
        """Get set of already-scraped post filenames (more reliable than slugs)."""
        existing = self.load_existing_index()
        return {p.get("filename", "") for p in existing.get("posts", [])}

    def _inline_to_markdown(self, element, base_url: str = "") -> str:
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
            text = "".join(self._inline_to_markdown(c, base_url) for c in element.children)
            if href and text and not href.startswith("#"):
                # Make relative URLs absolute
                if href.startswith("/") and base_url:
                    href = base_url + href
                return f"[{text}]({href})"
            return text

        if tag == "code":
            return f"`{element.get_text()}`"

        if tag in ["strong", "b"]:
            text = "".join(self._inline_to_markdown(c, base_url) for c in element.children)
            return f"**{text}**"

        if tag in ["em", "i"]:
            text = "".join(self._inline_to_markdown(c, base_url) for c in element.children)
            return f"*{text}*"

        if tag == "br":
            return "\n"

        # For other elements, recurse into children
        return "".join(self._inline_to_markdown(c, base_url) for c in element.children)

    def _get_direct_text(self, element, base_url: str = "", exclude_tags=None) -> str:
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
                parts.append(self._inline_to_markdown(child, base_url))
        return "".join(parts).strip()

    def html_to_markdown(self, element, base_url: str = "") -> str:
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
                text = self._get_direct_text(child, base_url)
                if text:
                    lines.append(f"\n{'#' * level} {text}\n")

            elif tag == "p":
                text = self._get_direct_text(child, base_url)
                if text:
                    lines.append(f"\n{text}\n")

            elif tag == "blockquote":
                text = self._get_direct_text(child, base_url)
                if text:
                    quoted = "\n".join(f"> {line}" for line in text.split("\n") if line.strip())
                    lines.append(f"\n{quoted}\n")

            elif tag in ["ul", "ol"]:
                for i, li in enumerate(child.find_all("li", recursive=False)):
                    prefix = "-" if tag == "ul" else f"{i+1}."
                    text = self._get_direct_text(li, base_url, exclude_tags={"ul", "ol"})
                    if text:
                        lines.append(f"{prefix} {text}")
                    # Handle nested lists
                    for nested_list in li.find_all(["ul", "ol"], recursive=False):
                        nested_md = self.html_to_markdown(nested_list, base_url)
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
                    if href.startswith("/") and base_url:
                        href = base_url + href
                    lines.append(f"[{text}]({href})")

            elif tag == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                if src:
                    if src.startswith("/") and base_url:
                        src = base_url + src
                    lines.append(f"\n![{alt}]({src})\n")

            elif tag in ["div", "section", "article", "span", "main"]:
                nested = self.html_to_markdown(child, base_url)
                if nested.strip():
                    lines.append(nested)

            elif tag == "figure":
                img = child.find("img")
                if img:
                    alt = img.get("alt", "")
                    src = img.get("src", "")
                    if src.startswith("/") and base_url:
                        src = base_url + src
                    lines.append(f"\n![{alt}]({src})\n")
                figcaption = child.find("figcaption")
                if figcaption:
                    lines.append(f"*{figcaption.get_text(strip=True)}*\n")

            elif tag == "hr":
                lines.append("\n---\n")

            elif tag in ["em", "i"]:
                text = self._get_direct_text(child, base_url)
                if text:
                    lines.append(f"*{text}*")

            elif tag in ["strong", "b"]:
                text = self._get_direct_text(child, base_url)
                if text:
                    lines.append(f"**{text}**")

            elif tag == "table":
                lines.append("\n")
                for row in child.find_all("tr"):
                    cells = row.find_all(["td", "th"])
                    row_text = " | ".join(self._get_direct_text(c, base_url) for c in cells)
                    lines.append(f"| {row_text} |")
                lines.append("\n")

            # Skip script, style, nav, header, footer, etc.
            elif tag in ["script", "style", "nav", "header", "footer", "aside", "noscript", "iframe"]:
                continue

        return "\n".join(lines)

    def run(self):
        """Main entry point - scrape and save all posts."""
        print(f"Scraper for {self.config['name']}")
        print("=" * 40)
        posts = self.scrape()
        print(f"\nDone! Processed {len(posts)} posts.")
