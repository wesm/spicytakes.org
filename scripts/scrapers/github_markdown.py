#!/usr/bin/env python3
"""
GitHub Markdown scraper for Spicy Takes platform.
Reads posts from a local repository with markdown files organized by year.
Designed for blogs like lucumr.pocoo.org that store posts in git.
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import yaml
from datetime import datetime
from pathlib import Path

from base import BaseScraper, get_blog_dir


class GitHubMarkdownScraper(BaseScraper):
    """Scraper for GitHub-hosted markdown blogs."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        # Validate scraper config
        if self.config["scraper"]["type"] != "github_markdown":
            raise ValueError(f"Blog {blog_id} is not configured as a github_markdown blog")

        # Allow env var override for localPath (e.g., ARMIN_LOCAL_PATH for armin blog)
        env_var = f"{blog_id.upper()}_LOCAL_PATH"
        local_path_str = os.environ.get(env_var) or self.config["scraper"].get("localPath")
        if not local_path_str:
            raise ValueError(f"localPath not set in config and {env_var} not set")

        self.local_path = Path(local_path_str).expanduser()
        self.posts_path = self.config["scraper"].get("postsPath", "posts")
        self.repo_url = self.config["scraper"].get("repoUrl")
        self._tmp_dir = None

        # If local path doesn't exist, clone from repoUrl
        if not self.local_path.exists() and self.repo_url:
            self._tmp_dir = tempfile.mkdtemp(
                prefix=f"spicytakes-{blog_id}-"
            )
            clone_path = Path(self._tmp_dir) / "repo"
            print(f"Local path not found, cloning {self.repo_url}...")
            subprocess.run(
                ["git", "clone", "--depth=1", self.repo_url,
                 str(clone_path)],
                check=True,
            )
            self.local_path = clone_path

        self.source_dir = self.local_path / self.posts_path
        if not self.source_dir.exists():
            raise FileNotFoundError(
                f"Source directory not found: {self.source_dir}"
            )

    def parse_post_file(self, file_path: Path, year: int) -> dict | None:
        """Parse a markdown post file and extract metadata + content."""
        try:
            content = file_path.read_text()
        except Exception as e:
            print(f"  Error reading {file_path}: {e}")
            return None

        # Extract frontmatter if present
        frontmatter = {}
        body = content

        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                    body = parts[2].strip()
                except yaml.YAMLError:
                    pass

        # Extract title from first H1 heading in body
        title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else file_path.stem

        # Parse date from filename: MM-DD-slug.md
        filename = file_path.stem
        date_match = re.match(r'^(\d{2})-(\d{2})-(.+)$', filename)
        if date_match:
            month, day, slug = date_match.groups()
            try:
                pub_date = datetime(year, int(month), int(day))
            except ValueError:
                pub_date = datetime(year, 1, 1)
        else:
            slug = filename
            pub_date = datetime(year, 1, 1)

        # Get tags and summary from frontmatter
        tags = frontmatter.get("tags", [])
        summary = frontmatter.get("summary", "")

        # Word count
        word_count = len(body.split())

        return {
            "slug": slug,
            "title": title,
            "date": pub_date.isoformat(),
            "tags": tags,
            "summary": summary,
            "content": body,
            "word_count": word_count,
            "source_file": str(file_path.relative_to(self.local_path))
        }

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post['title'].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
        ]
        if post.get("summary"):
            escaped_summary = post['summary'].replace('"', "'")
            frontmatter.append(f'summary: "{escaped_summary}"')
        if post.get("date"):
            frontmatter.append(f"date: {post['date']}")
        if post.get("tags"):
            frontmatter.append(f"tags: {json.dumps(post['tags'])}")
        frontmatter.extend([
            f"slug: {post['slug']}",
            f"word_count: {post['word_count']}",
            f"source_file: {post['source_file']}",
            "---",
            ""
        ])
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all posts from the local repository."""
        # Find all year directories
        year_dirs = sorted([
            d for d in self.source_dir.iterdir()
            if d.is_dir() and d.name.isdigit()
        ], key=lambda d: int(d.name))

        print(f"Found {len(year_dirs)} year directories")
        print(f"Source: {self.source_dir}")

        existing_filenames = self.get_existing_filenames()
        posts = []
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])

        total_new = 0
        for year_dir in year_dirs:
            year = int(year_dir.name)
            md_files = sorted(year_dir.glob("*.md"))

            for md_file in md_files:
                post = self.parse_post_file(md_file, year)
                if not post:
                    continue

                # Create filename from date and slug (includes year, so unique)
                date_prefix = post["date"][:10]
                filename = f"{date_prefix}-{post['slug']}.md"

                # Check if already scraped using filename (not slug) to handle same slug in different years
                if filename in existing_filenames:
                    continue

                print(f"[{year}] {post['slug']}")

                # Save post
                post["filename"] = filename
                original_content = post["content"]
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                # Add to index (without full content)
                index_entry = {k: v for k, v in post.items() if k != "content"}
                all_posts.append(index_entry)
                posts.append(index_entry)
                total_new += 1

        # Save index
        self.save_index(all_posts)
        print(f"\nProcessed {total_new} new posts. Total in index: {len(all_posts)}")

        return all_posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=armin python github_markdown.py")
        sys.exit(1)

    scraper = GitHubMarkdownScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
