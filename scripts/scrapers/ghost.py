#!/usr/bin/env python3
"""
Ghost blog scraper for Spicy Takes platform.
Uses the Ghost Content API to fetch all posts.
"""

import os
import re
import sys

import requests
from bs4 import BeautifulSoup

from base import BaseScraper


class GhostScraper(BaseScraper):
    """Scraper for Ghost blogs using the Content API."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "ghost":
            raise ValueError(f"Blog {blog_id} is not configured as ghost")

        self.ghost_url = self.config["scraper"]["ghostUrl"].rstrip("/")
        self.content_api_key = self.config["scraper"]["contentApiKey"]

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def fetch_all_posts(self) -> list[dict]:
        """Fetch all posts from the Ghost Content API."""
        url = f"{self.ghost_url}/ghost/api/content/posts/"
        params = {
            "key": self.content_api_key,
            "limit": "all",
            "include": "tags",
        }

        print(f"  Fetching posts from Ghost API...")
        response = requests.get(url, params=params, timeout=30, headers=self.headers)
        response.raise_for_status()

        data = response.json()
        posts = data.get("posts", [])
        print(f"    Got {len(posts)} posts")
        return posts

    def make_slug(self, post: dict) -> str:
        """Get slug from Ghost post."""
        return post.get("slug", "untitled")

    def make_filename(self, post: dict) -> str:
        """Create markdown filename from post metadata."""
        slug = self.make_slug(post)
        pub_date = post.get("published_at", "")[:10]  # YYYY-MM-DD
        if pub_date:
            return f"{pub_date}-{slug}.md"
        return f"{slug}.md"

    def make_post_content(self, post: dict, markdown: str) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post.get("title", "Untitled").replace('"', "'")
        pub_date = post.get("published_at", "")[:10]
        url = post.get("url", "")
        word_count = len(markdown.split())

        # Extract tag names
        tags = [t["name"] for t in post.get("tags", []) if t.get("name")]

        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if pub_date:
            frontmatter.append(f"date: {pub_date}")
        frontmatter.append(f"url: {url}")
        frontmatter.append(f"slug: {post.get('slug', '')}")
        frontmatter.append(f"word_count: {word_count}")
        if tags:
            frontmatter.append(f"tags: {tags}")
        frontmatter.extend(["---", ""])

        return "\n".join(frontmatter) + "\n" + markdown

    def scrape(self) -> list[dict]:
        """Scrape all posts from the Ghost blog."""
        api_posts = self.fetch_all_posts()

        existing_filenames = self.get_existing_filenames()
        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        posts_to_scrape = []
        for ap in api_posts:
            filename = self.make_filename(ap)
            if filename not in existing_filenames:
                posts_to_scrape.append((filename, ap))

        if not posts_to_scrape:
            print("All posts already scraped!")
            return posts

        print(f"Scraping {len(posts_to_scrape)} new posts...")

        for i, (filename, api_post) in enumerate(posts_to_scrape):
            title = api_post.get("title", "Untitled")
            print(f"[{i+1}/{len(posts_to_scrape)}] {title[:60]}...")

            # Convert HTML content to markdown
            html = api_post.get("html", "")
            if html:
                soup = BeautifulSoup(html, "html.parser")
                markdown = self.html_to_markdown(soup, self.ghost_url)
                # Strip Ghost card markers (kg-card-begin/end)
                markdown = re.sub(r'\n?kg-card-(begin|end): \w+\n?', '\n', markdown)
            else:
                markdown = ""

            word_count = len(markdown.split())

            # Create full content with frontmatter
            content = self.make_post_content(api_post, markdown)

            # Save post
            post = {"filename": filename, "content": content}
            filepath = self.save_post(post)
            print(f"  Saved: {filepath}")

            # Extract tag names for index
            tags = [t["name"] for t in api_post.get("tags", []) if t.get("name")]

            # Add to index
            index_entry = {
                "filename": filename,
                "title": title,
                "url": api_post.get("url", ""),
                "pub_date": api_post.get("published_at", "")[:10],
                "word_count": word_count,
                "tags": tags,
            }
            posts.append(index_entry)

            # Save index periodically
            if (i + 1) % 20 == 0:
                self.save_index(posts)
                print(f"  Index saved ({len(posts)} posts)")

        # Final save
        self.save_index(posts)
        return posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=mempko python ghost.py")
        sys.exit(1)

    scraper = GhostScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
