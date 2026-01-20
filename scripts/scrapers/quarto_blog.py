#!/usr/bin/env python3
"""
Quarto blog scraper for Spicy Takes platform.
Reads blog posts and talk transcripts from a local Quarto blog repository.
Designed for blogs like wesmckinney.com that use Quarto with transcripts.
"""

import json
import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path

from base import BaseScraper, get_blog_dir


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

        # Validate local path exists
        if not self.local_path.exists():
            raise FileNotFoundError(f"Source directory not found: {self.local_path}")

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

        # Parse date
        date_str = frontmatter.get("date", "")
        if date_str:
            try:
                if isinstance(date_str, str):
                    pub_date = datetime.fromisoformat(date_str.replace('"', ''))
                else:
                    pub_date = date_str
            except (ValueError, TypeError):
                pub_date = datetime.now()
        else:
            pub_date = datetime.now()

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

        # Parse date from frontmatter or filename
        date_str = frontmatter.get("date", "")
        if date_str:
            try:
                if isinstance(date_str, str):
                    pub_date = datetime.fromisoformat(date_str)
                else:
                    pub_date = datetime(date_str.year, date_str.month, date_str.day)
            except (ValueError, TypeError, AttributeError):
                # Try parsing from filename: YYYY-MM-DD-slug.md
                match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', md_file.stem)
                if match:
                    pub_date = datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
                else:
                    pub_date = datetime.now()
        else:
            # Try parsing from filename
            match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', md_file.stem)
            if match:
                pub_date = datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            else:
                pub_date = datetime.now()

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
