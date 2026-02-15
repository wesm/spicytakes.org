#!/usr/bin/env python3
"""
Blog statistics utilities for Spicy Takes.

Reusable functions for reading blog stats and updating landing.json.
Also provides a CLI for use from shell scripts.

CLI usage:
    python3 scripts/update_stats.py config <blog_id> <dotted.key>
    python3 scripts/update_stats.py stats <blog_id>
    python3 scripts/update_stats.py update-landing <blog_id> [blog_id ...]
    python3 scripts/update_stats.py update-landing --all
"""

import json
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent


def load_config(blog_id: str) -> dict:
    """Load a blog's config JSON."""
    path = PROJECT_DIR / "config" / f"{blog_id}.json"
    return json.loads(path.read_text())


def config_value(blog_id: str, dotted_key: str) -> str:
    """Read a dotted key from a blog config. e.g. 'scraper.type'"""
    obj = load_config(blog_id)
    for part in dotted_key.split("."):
        obj = obj[part]
    return str(obj)


def blog_stats(blog_id: str) -> dict:
    """Return post and quote counts for a blog.

    Returns dict with 'posts' and 'quotes' keys (int or None).
    'posts' uses the successful analysis count (no errors),
    not the raw scrape count.
    """
    blog_dir = PROJECT_DIR / "blogs" / blog_id / "data"

    posts = None
    llm_path = blog_dir / "llm_quotes.json"
    if llm_path.exists():
        data = json.loads(llm_path.read_text())
        posts = sum(
            1 for p in data.get("posts", [])
            if "error" not in p
        )

    quotes = None
    spicy_path = blog_dir / "spicy_quotes.json"
    if spicy_path.exists():
        data = json.loads(spicy_path.read_text())
        quotes = data.get("total", 0)

    return {"posts": posts, "quotes": quotes}


def raw_post_count(blog_id: str) -> int:
    """Return the raw scrape count from posts_index.json."""
    path = PROJECT_DIR / "blogs" / blog_id / "data" / "posts_index.json"
    if path.exists():
        return json.loads(path.read_text()).get("total_posts", 0)
    return 0


def load_landing() -> dict:
    """Load config/landing.json."""
    path = PROJECT_DIR / "config" / "landing.json"
    return json.loads(path.read_text())


def save_landing(data: dict) -> None:
    """Write config/landing.json."""
    path = PROJECT_DIR / "config" / "landing.json"
    path.write_text(json.dumps(data, indent=2) + "\n")


def update_landing(blog_ids: list[str] | None = None) -> bool:
    """Update landing.json stats for given blogs (or all if None).

    Returns True if landing.json was modified.
    """
    landing = load_landing()
    changed = False

    for entry in landing.get("blogs", []):
        bid = entry["id"]
        if blog_ids is not None and bid not in blog_ids:
            continue

        stats = blog_stats(bid)
        old = entry.get("stats", {})

        if stats["posts"] is not None and old.get("posts") != stats["posts"]:
            entry.setdefault("stats", {})["posts"] = stats["posts"]
            changed = True
        if stats["quotes"] is not None and old.get("quotes") != stats["quotes"]:
            entry.setdefault("stats", {})["quotes"] = stats["quotes"]
            changed = True

    if changed:
        save_landing(landing)

    return changed


def cli_config(args: list[str]) -> None:
    """CLI: print a config value."""
    if len(args) != 2:
        print("Usage: update_stats.py config <blog_id> <dotted.key>", file=sys.stderr)
        sys.exit(1)
    print(config_value(args[0], args[1]))


def cli_stats(args: list[str]) -> None:
    """CLI: print blog stats."""
    if len(args) != 1:
        print("Usage: update_stats.py stats <blog_id>", file=sys.stderr)
        sys.exit(1)
    s = blog_stats(args[0])
    print(f"{s['posts'] or 0}\t{s['quotes'] or 0}")


def cli_update_landing(args: list[str]) -> None:
    """CLI: update landing.json stats."""
    if not args:
        print("Usage: update_stats.py update-landing [--all | blog_id ...]", file=sys.stderr)
        sys.exit(1)

    if args == ["--all"]:
        ids = None
    else:
        ids = args

    changed = update_landing(ids)

    # Print what we set
    landing = load_landing()
    targets = ids or [e["id"] for e in landing.get("blogs", [])]
    for entry in landing.get("blogs", []):
        if entry["id"] in targets:
            s = entry.get("stats", {})
            print(f"  {entry['id']}: {s.get('posts', 0)} posts, {s.get('quotes', 0)} quotes")

    if changed:
        print("landing.json updated")
    else:
        print("landing.json already up to date")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__.strip(), file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "config": cli_config,
        "stats": cli_stats,
        "update-landing": cli_update_landing,
    }

    if command not in commands:
        print(f"Unknown command: {command}", file=sys.stderr)
        print(f"Available: {', '.join(commands)}", file=sys.stderr)
        sys.exit(1)

    commands[command](args)


if __name__ == "__main__":
    main()
