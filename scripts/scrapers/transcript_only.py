#!/usr/bin/env python3
"""
Transcript-only scraper for Spicy Takes platform.
Reads transcripts from a local transcripts directory (no blog source).
Designed for authors who primarily do talks/podcasts rather than written content.
"""

import json
import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path

from base import BaseScraper, get_blog_dir


def parse_date_robust(date_val, fallback_file: Path = None) -> datetime:
    """Parse a date value robustly, handling various formats."""
    if date_val:
        if hasattr(date_val, 'year'):
            try:
                return datetime(date_val.year, date_val.month, date_val.day)
            except (ValueError, TypeError, AttributeError):
                pass

        if isinstance(date_val, str):
            date_str = date_val.strip().replace('"', '').replace("'", "")
            date_str = date_str.replace('Z', '+00:00')
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                pass

    if fallback_file and fallback_file.exists():
        return datetime.fromtimestamp(fallback_file.stat().st_mtime)

    return datetime(1970, 1, 1)


class TranscriptOnlyScraper(BaseScraper):
    """Scraper for transcript-only blogs (talks, podcasts, no written blog)."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "transcript_only":
            raise ValueError(f"Blog {blog_id} is not configured as transcript_only")

        self.transcripts_path = self.config["scraper"].get("transcriptsPath", "transcripts")
        self.transcripts_dir = get_blog_dir(blog_id) / self.transcripts_path

        # Create transcripts directory if it doesn't exist
        self.transcripts_dir.mkdir(parents=True, exist_ok=True)

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

        # Parse date
        pub_date = parse_date_robust(frontmatter.get("date"), None)
        if pub_date.year == 1970:
            match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', md_file.stem)
            if match:
                pub_date = datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            else:
                pub_date = datetime.fromtimestamp(md_file.stat().st_mtime)

        # Prefer frontmatter slug when present; otherwise use full filename
        # (with date prefix) to avoid collisions between similarly-named transcripts
        slug = frontmatter.get("slug") or md_file.stem

        # Create tags
        tags = []
        if video_type:
            tags.append(video_type.lower())
        tags.append("transcript")

        word_count = len(body.split())

        return {
            "slug": slug,
            "title": title,
            "date": pub_date.isoformat(),
            "tags": tags,
            "summary": f"{video_type} at {event}" if event else video_type,
            "content": body,
            "word_count": word_count,
            "source_file": str(md_file.relative_to(get_blog_dir(self.blog_id))),
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
        frontmatter.append(f"content_type: {post.get('content_type', 'transcript')}")
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
        """Scrape all transcripts from the transcripts directory."""
        existing_filenames = self.get_existing_filenames()
        existing = self.load_existing_index()
        all_posts = existing.get("posts", [])
        existing_source_files = {p.get("source_file") for p in all_posts if p.get("source_file")}

        total_new = 0

        print(f"\n=== Scraping transcripts from {self.transcripts_dir} ===")

        if not self.transcripts_dir.exists():
            print(f"Transcripts directory does not exist: {self.transcripts_dir}")
            print("Create transcripts and place them in this directory.")
            return all_posts

        md_files = sorted(self.transcripts_dir.glob("*.md"))

        if not md_files:
            print("No transcript files found.")
            print(f"Add .md files to: {self.transcripts_dir}")
            return all_posts

        for md_file in md_files:
            # Skip metadata files
            if md_file.name.startswith('_'):
                continue

            post = self.parse_transcript(md_file)
            if not post:
                continue

            # source_file uniquely identifies transcript inputs across slug/filename strategy changes
            if post.get("source_file") in existing_source_files:
                continue

            # Create filename
            date_prefix = post["date"][:10]
            if post["slug"].startswith(f"{date_prefix}-"):
                filename = f"{post['slug']}.md"
            else:
                filename = f"{date_prefix}-{post['slug']}.md"

            if filename in existing_filenames:
                continue

            print(f"[transcript] {post['slug']}")

            # Save post
            post["filename"] = filename
            post["content"] = self.make_post_content(post)
            filepath = self.save_post(post)
            print(f"  Saved: {filepath}")

            # Add to index
            index_entry = {k: v for k, v in post.items() if k != "content"}
            all_posts.append(index_entry)
            existing_source_files.add(post.get("source_file"))
            total_new += 1

        # Validate no duplicate slugs
        seen_slugs = {}
        duplicates = []
        for p in all_posts:
            s = p["slug"]
            if s in seen_slugs:
                duplicates.append(f"Duplicate slug '{s}' in {p.get('filename')} and {seen_slugs[s]}")
            seen_slugs[s] = p.get("filename", "unknown")

        if duplicates:
            for d in duplicates:
                print(f"  ERROR: {d}")
            raise ValueError(f"Found {len(duplicates)} duplicate slug(s) in index. Aborting.")

        # Save index
        self.save_index(all_posts)
        print(f"\nProcessed {total_new} new transcripts. Total in index: {len(all_posts)}")

        return all_posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=hannes python transcript_only.py")
        sys.exit(1)

    scraper = TranscriptOnlyScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
