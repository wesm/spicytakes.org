#!/usr/bin/env python3
"""
Quarto blog scraper for Spicy Takes platform.
Reads blog posts and talk transcripts from a local Quarto blog repository.
Designed for blogs like wesmckinney.com that use Quarto with transcripts.
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


def parse_date_robust(date_val, fallback_file: Path = None) -> datetime:
    """Parse a date value robustly, handling various formats.

    Args:
        date_val: Date value from frontmatter (string, date object, or None)
        fallback_file: File to use for mtime fallback if date parsing fails

    Returns:
        datetime object
    """
    if date_val:
        # If it's already a date/datetime object from YAML
        if hasattr(date_val, 'year'):
            try:
                return datetime(date_val.year, date_val.month, date_val.day)
            except (ValueError, TypeError, AttributeError):
                pass

        # If it's a string, try parsing
        if isinstance(date_val, str):
            date_str = date_val.strip().replace('"', '').replace("'", "")
            # Handle Z suffix (UTC indicator) - replace with +00:00
            date_str = date_str.replace('Z', '+00:00')
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                pass

    # Stable fallback: use file modification time if available
    if fallback_file and fallback_file.exists():
        return datetime.fromtimestamp(fallback_file.stat().st_mtime)

    # Last resort: use epoch (1970-01-01) to make it obvious something is wrong
    return datetime(1970, 1, 1)


class QuartoBlogScraper(BaseScraper):
    """Scraper for Quarto-based blogs with transcripts."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        # Validate scraper config
        if self.config["scraper"]["type"] != "quarto_blog":
            raise ValueError(f"Blog {blog_id} is not configured as a quarto_blog")

        # Allow env var override for localPath
        env_var = f"{blog_id.upper()}_LOCAL_PATH"
        local_path_str = os.environ.get(env_var) or self.config["scraper"].get("localPath")
        if not local_path_str:
            raise ValueError(f"localPath not set in config and {env_var} not set")

        self.local_path = Path(local_path_str).expanduser()
        self.blog_path = self.config["scraper"].get("blogPath", "blog")
        self.transcripts_path = self.config["scraper"].get("transcriptsPath", "transcripts")
        self.repo_url = self.config["scraper"].get("repoUrl")

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

        if not self.local_path.exists():
            raise FileNotFoundError(
                f"Source directory not found: {self.local_path}"
            )

    def parse_frontmatter(self, content: str) -> tuple[dict, str]:
        """Extract YAML frontmatter and body from content."""
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

        return frontmatter, body

    def parse_blog_post(self, post_dir: Path) -> dict | None:
        """Parse a Quarto blog post directory containing index.qmd."""
        qmd_file = post_dir / "index.qmd"
        if not qmd_file.exists():
            return None

        try:
            content = qmd_file.read_text()
        except Exception as e:
            print(f"  Error reading {qmd_file}: {e}")
            return None

        frontmatter, body = self.parse_frontmatter(content)

        # Extract title
        title = frontmatter.get("title", post_dir.name)

        # Parse date with robust handling
        pub_date = parse_date_robust(frontmatter.get("date"), qmd_file)

        # Get categories as tags
        tags = frontmatter.get("categories", [])

        # Create slug from directory name
        slug = post_dir.name

        # Word count
        word_count = len(body.split())

        return {
            "slug": slug,
            "title": title,
            "date": pub_date.isoformat() if isinstance(pub_date, datetime) else str(pub_date),
            "tags": tags,
            "summary": "",
            "content": body,
            "word_count": word_count,
            "source_file": str(qmd_file.relative_to(self.local_path)),
            "content_type": "blog"
        }

    def parse_transcript(self, md_file: Path) -> dict | None:
        """Parse a transcript markdown file."""
        try:
            content = md_file.read_text()
        except Exception as e:
            print(f"  Error reading {md_file}: {e}")
            return None

        frontmatter, body = self.parse_frontmatter(content)

        # Extract metadata
        title = frontmatter.get("title", md_file.stem)
        event = frontmatter.get("event", "")
        location = frontmatter.get("location", "")
        video_url = frontmatter.get("video_url", "")
        video_type = frontmatter.get("video_type", "talk")

        # Parse date from frontmatter, filename, or file mtime
        pub_date = parse_date_robust(frontmatter.get("date"), None)
        # If frontmatter date failed (returns epoch), try filename
        if pub_date.year == 1970:
            match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', md_file.stem)
            if match:
                pub_date = datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            else:
                # Last fallback: file mtime
                pub_date = datetime.fromtimestamp(md_file.stat().st_mtime)

        # Create slug from filename (without date prefix)
        filename = md_file.stem
        slug_match = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)$', filename)
        slug = slug_match.group(1) if slug_match else filename

        # Create tags from event type and video type
        tags = []
        if video_type:
            tags.append(video_type.lower())
        if event:
            tags.append("transcript")

        # Word count
        word_count = len(body.split())

        return {
            "slug": slug,
            "title": title,
            "date": pub_date.isoformat(),
            "tags": tags,
            "summary": f"{video_type} at {event}" if event else "",
            "content": body,
            "word_count": word_count,
            "source_file": str(md_file.relative_to(self.local_path)),
            "content_type": "transcript",
            "event": event,
            "location": location,
            "video_url": video_url
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
        frontmatter.append(f"slug: {post['slug']}")
        frontmatter.append(f"word_count: {post['word_count']}")
        frontmatter.append(f"source_file: {post['source_file']}")
        frontmatter.append(f"content_type: {post.get('content_type', 'blog')}")
        if post.get("event"):
            frontmatter.append(f'event: "{post["event"]}"')
        if post.get("video_url"):
            frontmatter.append(f'video_url: "{post["video_url"]}"')
        frontmatter.extend([
            "---",
            ""
        ])
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all posts and transcripts from the local repository."""
        existing_filenames = self.get_existing_filenames()
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])

        total_new = 0

        # Scrape blog posts
        blog_dir = self.local_path / self.blog_path
        if blog_dir.exists():
            print(f"\n=== Scraping blog posts from {blog_dir} ===")
            post_dirs = sorted([
                d for d in blog_dir.iterdir()
                if d.is_dir() and not d.name.startswith('.')
            ])

            for post_dir in post_dirs:
                post = self.parse_blog_post(post_dir)
                if not post:
                    continue

                # Create filename from date and slug
                date_prefix = post["date"][:10]
                filename = f"{date_prefix}-{post['slug']}.md"

                if filename in existing_filenames:
                    continue

                print(f"[blog] {post['slug']}")

                # Save post
                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                # Add to index (without full content)
                index_entry = {k: v for k, v in post.items() if k != "content"}
                all_posts.append(index_entry)
                total_new += 1

        # Scrape transcripts
        transcripts_dir = self.local_path / self.transcripts_path
        if transcripts_dir.exists():
            print(f"\n=== Scraping transcripts from {transcripts_dir} ===")
            md_files = sorted(transcripts_dir.glob("*.md"))

            for md_file in md_files:
                # Skip metadata files
                if md_file.name.startswith('_'):
                    continue

                post = self.parse_transcript(md_file)
                if not post:
                    continue

                # Use original filename or create from date and slug
                date_prefix = post["date"][:10]
                filename = f"{date_prefix}-{post['slug']}.md"

                if filename in existing_filenames:
                    continue

                print(f"[transcript] {post['slug']}")

                # Save post
                post["filename"] = filename
                original_content = post["content"]
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                # Add to index (without full content)
                index_entry = {k: v for k, v in post.items() if k != "content"}
                all_posts.append(index_entry)
                total_new += 1

        # Save index
        self.save_index(all_posts)
        print(f"\nProcessed {total_new} new items. Total in index: {len(all_posts)}")

        return all_posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=wesm python quarto_blog.py")
        sys.exit(1)

    scraper = QuartoBlogScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
