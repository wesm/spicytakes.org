#!/usr/bin/env python3
"""
Build blogs/feed_index.json from all blogs' data.

Precomputes the cross-blog feed and per-blog spiciness so the
landing deployment only needs this single file (~2 MB) instead
of every blog's raw JSON (~113 MB).

Usage:
    python3 scripts/build_feed_index.py
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_DIR / "config"
BLOGS_DIR = PROJECT_DIR / "blogs"
OUTPUT_PATH = BLOGS_DIR / "feed_index.json"

MAX_FEED_POSTS = 1000


def parse_date(filename: str) -> str | None:
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}T12:00:00Z"
    return None


def format_title(filename: str) -> str:
    title_part = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", filename)
    acronyms = {
        "bi", "sql", "ai", "yc", "vc", "llm", "llms",
        "mds", "obp", "svb", "tam", "mvp",
    }

    words = []
    for word in title_part.split("-"):
        lower = word.lower()
        if lower in acronyms:
            words.append(lower.upper())
        elif lower == "dbt":
            words.append("dbt")
        else:
            words.append(word[0:1].upper() + word[1:])
    return " ".join(words)


def build_source_url(
    filename: str,
    cfg: dict,
    post_meta: dict | None = None,
) -> str:
    """Port of buildSourceUrl from src/lib/config.ts."""
    meta = post_meta or {}
    scraper = cfg.get("scraper", {})
    scraper_type = scraper.get("type", "")
    source_url = cfg.get("sourceUrl", "")

    if meta.get("content_type") == "transcript":
        return meta.get("video_url", "")

    if meta.get("source_url"):
        return meta["source_url"]

    stem = re.sub(r"\.md$", "", filename)
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)
    date_match = re.match(
        r"^(\d{4})-(\d{2})-(\d{2})-(.+?)(?:\.md)?$", filename
    )

    if scraper_type == "substack":
        return f"{source_url}/p/{slug}"

    if scraper_type == "github_markdown" and date_match:
        y, m_str, d_str, s = date_match.groups()
        return (
            f"{source_url}/{y}/{int(m_str)}/{int(d_str)}/{s}/"
        )

    if scraper_type == "quarto_blog":
        return f"{source_url}/blog/{slug}/"

    if scraper_type == "static_html":
        return f"{source_url}/{slug}/"

    if scraper_type == "hugo_rss" and date_match:
        y, mo, d, s = date_match.groups()
        return f"{source_url}/{y}/{mo}/{d}/{s}/"

    if scraper_type == "hugo_homepage":
        return f"{source_url}/post/{slug}/"

    if scraper_type == "jekyll_feed" and date_match:
        y, mo, d, s = date_match.groups()
        post_path = scraper.get(
            "sourcePostPath",
            "/blog/jekyll/update/{year}/{month}/{day}/{slug}.html",
        )
        path = (
            post_path.replace("{year}", y)
            .replace("{month}", mo)
            .replace("{day}", d)
            .replace("{slug}", s)
        )
        return f"{source_url}{path}"

    if scraper_type == "wordpress" and date_match:
        y, mo, d, s = date_match.groups()
        return f"{source_url}/{y}/{mo}/{d}/{s}/"

    if scraper_type == "jekyll_static":
        return f"{source_url}/{slug}"

    if scraper_type == "rss_generic":
        post_path = scraper.get(
            "sourcePostPath", "/blog/{slug}/"
        )
        return f"{source_url}{post_path.replace('{slug}', slug)}"

    if scraper_type == "paulgraham":
        return f"{source_url}/{slug}.html"

    if scraper_type == "caseymuratori":
        return f"{source_url}/{slug}"

    if scraper_type == "jvns" and date_match:
        y, mo, d, s = date_match.groups()
        return f"{source_url}/blog/{y}/{mo}/{d}/{s}/"

    if scraper_type == "kalzumeus" and date_match:
        y, mo, d, s = date_match.groups()
        return f"{source_url}/{y}/{mo}/{d}/{s}/"

    if scraper_type == "daringfireball":
        m2 = re.match(
            r"^(\d{4})-(\d{2})-\d{2}-(.+?)\.md$", filename
        )
        if m2:
            y, mo, s = m2.groups()
            return f"{source_url}/{y}/{mo}/{s}"

    if scraper_type == "zedshaw":
        return f"{source_url}/blog/{stem}/"

    if scraper_type == "hey_world":
        return f"{source_url}/{slug}"

    if scraper_type == "blogger":
        m3 = re.match(
            r"^(\d{4})-(\d{2})-\d{2}-(.+?)(?:\.md)?$",
            filename,
        )
        if m3:
            y, mo, s = m3.groups()
            return f"{source_url}/{y}/{mo}/{s}.html"

    if scraper_type == "martinfowler":
        return f"{source_url}/bliki/{slug}.html"

    return source_url


def load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def build_feed_index() -> dict:
    landing = load_json(CONFIG_DIR / "landing.json")
    if not landing:
        print("Error: config/landing.json not found", file=sys.stderr)
        sys.exit(1)

    blogs = [b for b in landing["blogs"] if not b.get("hidden")]
    feed_posts: list[dict] = []
    blog_spiciness: dict[str, float | None] = {}

    for blog in blogs:
        bid = blog["id"]
        blog_dir = BLOGS_DIR / bid / "data"
        cfg_path = CONFIG_DIR / f"{bid}.json"

        blog_cfg = load_json(cfg_path)
        if not blog_cfg:
            continue

        llm_data = load_json(blog_dir / "llm_quotes.json") or {
            "posts": []
        }
        spicy_data = load_json(
            blog_dir / "spicy_quotes.json"
        ) or {"quotes": []}
        posts_index_data = load_json(
            blog_dir / "posts_index.json"
        ) or {"posts": []}

        # Build lookups from posts_index
        title_lookup: dict[str, str] = {}
        url_lookup: dict[str, str] = {}
        video_url_lookup: dict[str, str] = {}
        content_type_lookup: dict[str, str] = {}

        for p in posts_index_data.get("posts", []):
            fn = p.get("filename")
            if not fn:
                continue
            keys = [fn, re.sub(r"\.md$", "", fn)]
            if p.get("title"):
                for k in keys:
                    title_lookup[k] = p["title"]
            if p.get("url"):
                for k in keys:
                    url_lookup[k] = p["url"]
            if p.get("video_url"):
                for k in keys:
                    video_url_lookup[k] = p["video_url"]
            if p.get("content_type"):
                for k in keys:
                    content_type_lookup[k] = p["content_type"]
            slug = p.get("slug")
            if slug:
                if p.get("title"):
                    title_lookup[slug] = p["title"]
                if p.get("url"):
                    url_lookup[slug] = p["url"]

        # Build spiciness lookup
        spicy_lookup: dict[str, float] = {}
        for q in spicy_data.get("quotes", []):
            key = json.dumps(
                [q["quote"], q["filename"]], ensure_ascii=False
            )
            spicy_lookup[key] = q.get("spiciness", 5)

        # Compute per-blog average spiciness
        all_scores = [
            q.get("spiciness", 5)
            for q in spicy_data.get("quotes", [])
        ]
        if all_scores:
            avg = sum(all_scores) / len(all_scores)
            blog_spiciness[bid] = round(avg, 1)
        else:
            blog_spiciness[bid] = None

        # Build feed posts
        for post in llm_data.get("posts", []):
            if post.get("error"):
                continue
            fn = post["filename"]
            date_str = parse_date(fn)
            if not date_str:
                continue  # Feed requires dates

            slug = re.sub(
                r"\.md$",
                "",
                re.sub(r"^\d{4}-\d{2}-\d{2}-", "", fn),
            )
            title = (
                title_lookup.get(fn)
                or title_lookup.get(slug)
                or format_title(fn)
            )

            video_url = video_url_lookup.get(
                fn
            ) or video_url_lookup.get(slug)
            content_type = content_type_lookup.get(
                fn
            ) or content_type_lookup.get(slug)
            src_url = url_lookup.get(fn) or url_lookup.get(slug)

            source_url = build_source_url(
                fn,
                blog_cfg,
                {
                    "video_url": video_url,
                    "content_type": content_type,
                    "source_url": src_url,
                },
            )

            # Per-quote spiciness + top 3
            quotes_with_spiciness = []
            for q_text in post.get("money_quotes", []):
                key = json.dumps(
                    [q_text, fn], ensure_ascii=False
                )
                quotes_with_spiciness.append(
                    {
                        "quote": q_text,
                        "spiciness": spicy_lookup.get(key, 5),
                    }
                )

            top_quotes = sorted(
                quotes_with_spiciness,
                key=lambda x: x["spiciness"],
                reverse=True,
            )[:3]

            spiciness: float | None = None
            if quotes_with_spiciness:
                avg_s = sum(
                    q["spiciness"] for q in quotes_with_spiciness
                ) / len(quotes_with_spiciness)
                spiciness = round(avg_s, 1)

            filename_stem = re.sub(r"\.md$", "", fn)

            feed_posts.append(
                {
                    "filename": fn,
                    "title": title,
                    "dateStr": date_str,
                    "blogId": bid,
                    "authorName": blog["name"],
                    "authorPhoto": blog["photo"],
                    "subdomain": blog["subdomain"],
                    "summary": post.get("summary", ""),
                    "key_insight": post.get("key_insight", ""),
                    "topQuotes": top_quotes,
                    "spiciness": spiciness,
                    "sourceUrl": source_url,
                    "spicytakesUrl": (
                        f"https://{blog['subdomain']}"
                        f"/post/{filename_stem}"
                    ),
                }
            )

    # Sort by date descending, take top MAX_FEED_POSTS
    feed_posts.sort(
        key=lambda p: p["dateStr"] or "", reverse=True
    )
    posts = feed_posts[:MAX_FEED_POSTS]

    # Collect unique blog authors for filter options
    author_set = {p["blogId"] for p in posts}
    authors = [
        {"id": b["id"], "name": b["name"]}
        for b in blogs
        if b["id"] in author_set
    ]

    return {
        "generated": datetime.now(timezone.utc).isoformat(),
        "posts": posts,
        "authors": authors,
        "blogSpiciness": blog_spiciness,
    }


def main() -> None:
    feed_index = build_feed_index()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(feed_index, ensure_ascii=False) + "\n"
    )

    post_count = len(feed_index["posts"])
    author_count = len(feed_index["authors"])
    size_mb = OUTPUT_PATH.stat().st_size / (1024 * 1024)
    print(
        f"feed_index.json: {post_count} posts, "
        f"{author_count} authors, {size_mb:.1f} MB"
    )


if __name__ == "__main__":
    main()
