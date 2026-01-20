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
        index = {
            "total_posts": len(posts),
            "last_updated": datetime.now().isoformat(),
            "posts": posts
        }
        with open(index_file, "w") as f:
            json.dump(index, f, indent=2)

    def get_existing_slugs(self) -> set[str]:
        """Get set of already-scraped post slugs."""
        existing = self.load_existing_index()
        return {p.get("slug", "") for p in existing.get("posts", [])}

    def run(self):
        """Main entry point - scrape and save all posts."""
        print(f"Scraper for {self.config['name']}")
        print("=" * 40)
        posts = self.scrape()
        print(f"\nDone! Processed {len(posts)} posts.")
