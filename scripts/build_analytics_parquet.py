#!/usr/bin/env python3
"""
Build analytics Parquet file from all blog data.

Combines spicy_quotes.json, posts_index.json, and config.json from all blogs
into a single unified Parquet file for DuckDB-WASM analytics.

Usage:
    python scripts/build_analytics_parquet.py
"""

import json
import re
from pathlib import Path
from datetime import datetime

try:
    import duckdb
except ImportError:
    print("DuckDB not installed. Run: pip install duckdb")
    exit(1)

try:
    import pyarrow  # noqa: F401 - required by duckdb for parquet export
except ImportError:
    print("PyArrow not installed. Run: pip install pyarrow")
    exit(1)


def parse_date_from_filename(filename: str) -> tuple[int | None, int | None, str | None]:
    """Extract year, month, and date string from filename like '2024-01-15-post-slug'."""
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})', filename)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        return year, month, f"{year}-{month:02d}-{day:02d}"
    return None, None, None


def load_blog_data(blog_id: str, config_path: Path, blogs_dir: Path) -> list[dict]:
    """Load and process data for a single blog."""
    quotes = []

    # Load config
    with open(config_path) as f:
        config = json.load(f)

    author_name = config.get('name', blog_id)
    source_url = config.get('sourceUrl', '')
    themes_config = config.get('themes', {})

    # Load spicy quotes
    spicy_path = blogs_dir / blog_id / 'data' / 'spicy_quotes.json'
    if not spicy_path.exists():
        print(f"  No spicy_quotes.json for {blog_id}")
        return quotes

    with open(spicy_path) as f:
        spicy_data = json.load(f)

    # Load posts index for titles and URLs
    posts_index_path = blogs_dir / blog_id / 'data' / 'posts_index.json'
    posts_lookup = {}
    if posts_index_path.exists():
        with open(posts_index_path) as f:
            posts_data = json.load(f)
        for post in posts_data.get('posts', []):
            # Key by slug or filename
            slug = post.get('slug', '')
            filename = post.get('filename', '').replace('.md', '')
            if slug:
                posts_lookup[slug] = post
            if filename:
                posts_lookup[filename] = post

    # Process quotes
    quote_list = spicy_data.get('quotes', [])
    for i, q in enumerate(quote_list):
        filename = q.get('filename', '').replace('.md', '')
        year, month, date_str = parse_date_from_filename(filename)

        # Try to find post info
        post_info = posts_lookup.get(filename, {})

        # If no date from filename, try posts_index
        if not year and post_info.get('date'):
            try:
                dt = datetime.fromisoformat(post_info['date'].replace('Z', '+00:00'))
                year = dt.year
                month = dt.month
                date_str = dt.strftime('%Y-%m-%d')
            except:
                pass

        # Build post URL
        post_url = post_info.get('url', '')
        if not post_url and source_url:
            post_url = f"{source_url.rstrip('/')}/{filename}"

        # Get theme labels
        theme_ids = q.get('themes', [])
        theme_labels = [themes_config.get(t, {}).get('label', t) for t in theme_ids]

        quotes.append({
            'quote_id': f"{blog_id}_{i}",
            'quote_text': q.get('quote', ''),
            'spiciness': q.get('spiciness', 5),
            'post_filename': filename,
            'post_title': post_info.get('title', filename.split('-', 3)[-1].replace('-', ' ').title() if '-' in filename else filename),
            'post_date': date_str,
            'post_year': year,
            'post_month': month,
            'post_url': post_url,
            'author_id': blog_id,
            'author_name': author_name,
            'themes': theme_ids,
            'theme_labels': theme_labels,
            'tone': q.get('tone', ''),
            'summary': q.get('summary', ''),
            'key_insight': q.get('key_insight', ''),
            'quote_length': len(q.get('quote', '')),
            'word_count': len(q.get('quote', '').split()),
        })

    return quotes


def main():
    root = Path(__file__).parent.parent
    config_dir = root / 'config'
    blogs_dir = root / 'blogs'
    output_dir = root / 'static' / 'data'
    output_dir.mkdir(parents=True, exist_ok=True)

    all_quotes = []

    # Process each blog
    for config_path in sorted(config_dir.glob('*.json')):
        blog_id = config_path.stem
        if blog_id == 'landing':
            continue

        print(f"Processing {blog_id}...")
        quotes = load_blog_data(blog_id, config_path, blogs_dir)
        print(f"  Found {len(quotes)} quotes")
        all_quotes.extend(quotes)

    print(f"\nTotal quotes: {len(all_quotes)}")

    # Create DuckDB and export to Parquet
    con = duckdb.connect()

    # Convert to PyArrow table for DuckDB ingestion
    import pyarrow as pa

    # Define schema
    schema = pa.schema([
        ('quote_id', pa.string()),
        ('quote_text', pa.string()),
        ('spiciness', pa.int8()),
        ('post_filename', pa.string()),
        ('post_title', pa.string()),
        ('post_date', pa.string()),
        ('post_year', pa.int16()),
        ('post_month', pa.int8()),
        ('post_url', pa.string()),
        ('author_id', pa.string()),
        ('author_name', pa.string()),
        ('themes', pa.list_(pa.string())),
        ('theme_labels', pa.list_(pa.string())),
        ('tone', pa.string()),
        ('summary', pa.string()),
        ('key_insight', pa.string()),
        ('quote_length', pa.int32()),
        ('word_count', pa.int32()),
    ])

    # Build arrays
    arrays = [
        pa.array([q['quote_id'] for q in all_quotes]),
        pa.array([q['quote_text'] for q in all_quotes]),
        pa.array([q['spiciness'] for q in all_quotes], type=pa.int8()),
        pa.array([q['post_filename'] for q in all_quotes]),
        pa.array([q['post_title'] for q in all_quotes]),
        pa.array([q['post_date'] for q in all_quotes]),
        pa.array([q['post_year'] for q in all_quotes], type=pa.int16()),
        pa.array([q['post_month'] for q in all_quotes], type=pa.int8()),
        pa.array([q['post_url'] for q in all_quotes]),
        pa.array([q['author_id'] for q in all_quotes]),
        pa.array([q['author_name'] for q in all_quotes]),
        pa.array([q['themes'] for q in all_quotes]),
        pa.array([q['theme_labels'] for q in all_quotes]),
        pa.array([q['tone'] for q in all_quotes]),
        pa.array([q['summary'] for q in all_quotes]),
        pa.array([q['key_insight'] for q in all_quotes]),
        pa.array([q['quote_length'] for q in all_quotes], type=pa.int32()),
        pa.array([q['word_count'] for q in all_quotes], type=pa.int32()),
    ]

    table = pa.Table.from_arrays(arrays, schema=schema)

    # Register with DuckDB
    con.register('quotes_arrow', table)
    con.execute("CREATE TABLE quotes AS SELECT * FROM quotes_arrow")

    # Export main quotes table
    output_path = output_dir / 'analytics_quotes.parquet'
    con.execute(f"COPY quotes TO '{output_path}' (FORMAT PARQUET, COMPRESSION ZSTD)")
    print(f"\nWrote {output_path}")

    # Show some stats
    result = con.execute("""
        SELECT
            COUNT(*) as total_quotes,
            COUNT(DISTINCT author_id) as num_authors,
            MIN(post_year) as min_year,
            MAX(post_year) as max_year,
            ROUND(AVG(spiciness), 2) as avg_spiciness
        FROM quotes
        WHERE post_year IS NOT NULL
    """).fetchone()

    print(f"\nStats:")
    print(f"  Total quotes: {result[0]}")
    print(f"  Authors: {result[1]}")
    print(f"  Year range: {result[2]}-{result[3]}")
    print(f"  Avg spiciness: {result[4]}")

    # Show file size
    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"  File size: {size_mb:.2f} MB")


if __name__ == '__main__':
    main()
