#!/usr/bin/env python3
"""Validate posts_index.json files for all blogs. Checks for duplicate slugs and filenames."""

import json
import sys
from pathlib import Path

def validate_blog(blog_dir: Path) -> list[str]:
    """Validate a single blog's posts_index.json. Returns list of errors."""
    index_file = blog_dir / "data" / "posts_index.json"
    if not index_file.exists():
        return []

    data = json.loads(index_file.read_text())
    posts = data if isinstance(data, list) else data.get("posts", [])

    errors = []
    seen_slugs = {}
    seen_filenames = {}

    for i, post in enumerate(posts):
        slug = post.get("slug", "")
        filename = post.get("filename", "")

        if slug and slug in seen_slugs:
            errors.append(f"{blog_dir.name}: Duplicate slug '{slug}' at index {i} and {seen_slugs[slug]}")
        if slug:
            seen_slugs[slug] = i

        if filename and filename in seen_filenames:
            errors.append(f"{blog_dir.name}: Duplicate filename '{filename}' at index {i} and {seen_filenames[filename]}")
        if filename:
            seen_filenames[filename] = i

    return errors


def main():
    blogs_dir = Path(__file__).resolve().parent.parent / "blogs"
    all_errors = []

    for blog_dir in sorted(blogs_dir.iterdir()):
        if blog_dir.is_dir():
            errors = validate_blog(blog_dir)
            if errors:
                all_errors.extend(errors)
            else:
                print(f"  {blog_dir.name}: OK")

    if all_errors:
        print("\nErrors found:")
        for e in all_errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    else:
        print("\nAll blogs valid.")


if __name__ == "__main__":
    main()
