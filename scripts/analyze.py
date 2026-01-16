#!/usr/bin/env python3
"""
Analysis script for Benn Stancil's Substack posts.
Extracts themes, key quotes, and tracks evolution of ideas over time.
"""

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / "posts"
DATA_DIR = BASE_DIR / "data"
INDEX_FILE = DATA_DIR / "posts_index.json"
QUOTES_FILE = DATA_DIR / "quotes.json"
THEMES_FILE = DATA_DIR / "themes.json"


# Key themes to track in Benn's writing
THEME_KEYWORDS = {
    "modern_data_stack": [
        "modern data stack", "mds", "data stack", "data infrastructure",
        "data pipeline", "etl", "elt"
    ],
    "analytics_practice": [
        "analyst", "analytics team", "data team", "self-serve", "self serve",
        "dashboard", "bi ", "business intelligence", "reporting"
    ],
    "specific_tools": [
        "dbt", "snowflake", "fivetran", "looker", "tableau", "databricks",
        "bigquery", "redshift", "postgres", "metabase", "mode"
    ],
    "ai_and_llms": [
        "ai ", "llm", "chatgpt", "gpt", "large language", "artificial intelligence",
        "machine learning", "ml ", "automation"
    ],
    "startups_and_vc": [
        "startup", "venture", "funding", "valuation", "yc", "y combinator",
        "founder", "investor", "vc ", "series "
    ],
    "career_and_work": [
        "career", "job", "hire", "hiring", "promotion", "salary", "compensation",
        "engineer", "manager", "leadership"
    ],
    "data_quality": [
        "data quality", "data governance", "data contract", "data catalog",
        "metadata", "lineage", "observability"
    ],
    "metrics_and_measurement": [
        "metric", "kpi", "measure", "measurement", "semantic layer",
        "metrics layer", "definition"
    ],
    "industry_criticism": [
        "hype", "overhyped", "bubble", "collapse", "fail", "failure",
        "problem", "broken", "criticism"
    ],
    "sql_and_technical": [
        "sql", "query", "database", "table", "join", "aggregate",
        "window function", "cte"
    ]
}


def load_posts():
    """Load all post markdown files."""
    posts = []
    for filepath in sorted(POSTS_DIR.glob("*.md")):
        with open(filepath) as f:
            content = f.read()

        # Parse frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1].strip()
                body = parts[2].strip()

                # Parse YAML-like frontmatter
                meta = {}
                for line in frontmatter.split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        meta[key.strip()] = value.strip().strip('"')

                posts.append({
                    "filename": filepath.name,
                    "meta": meta,
                    "content": body,
                    "full_text": content
                })

    return posts


def identify_themes(post):
    """Identify which themes are present in a post."""
    content_lower = post["content"].lower()
    title_lower = post["meta"].get("title", "").lower()

    themes = []
    for theme, keywords in THEME_KEYWORDS.items():
        for keyword in keywords:
            if keyword in content_lower or keyword in title_lower:
                themes.append(theme)
                break

    return list(set(themes))


def extract_potential_quotes(content, max_quotes=10):
    """
    Extract sentences that could be good "money quotes".
    Looks for:
    - Strong declarative statements
    - Sentences with opinion markers
    - Metaphors and analogies
    - Short punchy sentences after longer ones
    """
    # Split into sentences (rough)
    sentences = re.split(r'(?<=[.!?])\s+', content)

    potential_quotes = []

    for i, sentence in enumerate(sentences):
        score = 0

        # Skip very short or very long sentences
        word_count = len(sentence.split())
        if word_count < 5 or word_count > 50:
            continue

        # Opinion/assertion markers
        opinion_markers = [
            "the problem is", "the truth is", "the reality is",
            "what this means", "here's the thing", "the point is",
            "we need to", "we should", "we must",
            "isn't about", "is really about", "it's actually",
            "the fundamental", "the real question",
            "most people", "nobody", "everyone", "few people",
            "the best", "the worst", "the only",
            "never", "always", "rarely"
        ]
        for marker in opinion_markers:
            if marker in sentence.lower():
                score += 2

        # Contrast/pivot words (often introduce key points)
        contrast_words = ["but", "however", "instead", "yet", "still", "though"]
        for word in contrast_words:
            if f" {word} " in sentence.lower():
                score += 1

        # Metaphor indicators
        metaphor_markers = ["like a", "is a", "isn't a", "as if", "imagine"]
        for marker in metaphor_markers:
            if marker in sentence.lower():
                score += 1

        # Question sentences (rhetorical questions can be punchy)
        if sentence.strip().endswith("?"):
            score += 1

        # Shorter sentences after long ones (often conclusions)
        if i > 0 and word_count < 15 and len(sentences[i-1].split()) > 25:
            score += 2

        if score > 0:
            potential_quotes.append({
                "text": sentence.strip(),
                "score": score,
                "word_count": word_count
            })

    # Sort by score and return top quotes
    potential_quotes.sort(key=lambda x: x["score"], reverse=True)
    return potential_quotes[:max_quotes]


def analyze_all_posts():
    """Run analysis on all posts."""
    print("Loading posts...")
    posts = load_posts()
    print(f"Loaded {len(posts)} posts")

    if not posts:
        print("No posts found. Run scrape.py first.")
        return

    # Analyze each post
    analysis_results = []
    theme_timeline = defaultdict(list)
    all_quotes = []

    for post in posts:
        date = post["meta"].get("date", "")[:10] if post["meta"].get("date") else "unknown"
        title = post["meta"].get("title", "Untitled")
        slug = post["meta"].get("slug", "")
        url = post["meta"].get("url", "")

        # Identify themes
        themes = identify_themes(post)

        # Extract potential quotes
        quotes = extract_potential_quotes(post["content"])

        # Track themes over time
        for theme in themes:
            theme_timeline[theme].append({
                "date": date,
                "title": title,
                "slug": slug
            })

        # Collect quotes
        for q in quotes[:5]:  # Top 5 quotes per post
            all_quotes.append({
                "date": date,
                "title": title,
                "slug": slug,
                "url": url,
                "quote": q["text"],
                "score": q["score"],
                "themes": themes
            })

        analysis_results.append({
            "date": date,
            "title": title,
            "slug": slug,
            "url": url,
            "themes": themes,
            "word_count": post["meta"].get("word_count", 0),
            "top_quotes": [q["text"] for q in quotes[:3]]
        })

    # Sort by date
    analysis_results.sort(key=lambda x: x["date"])
    all_quotes.sort(key=lambda x: (x["date"], -x["score"]))

    # Save results
    print("\nSaving analysis results...")

    with open(QUOTES_FILE, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_quotes": len(all_quotes),
            "quotes": all_quotes
        }, f, indent=2)
    print(f"  Saved {len(all_quotes)} quotes to {QUOTES_FILE}")

    # Convert theme_timeline to serializable format
    theme_data = {
        theme: {
            "total_posts": len(posts_list),
            "posts": posts_list
        }
        for theme, posts_list in theme_timeline.items()
    }

    with open(THEMES_FILE, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "themes": theme_data
        }, f, indent=2)
    print(f"  Saved theme analysis to {THEMES_FILE}")

    # Print summary
    print("\n" + "=" * 50)
    print("ANALYSIS SUMMARY")
    print("=" * 50)
    print(f"\nTotal posts analyzed: {len(posts)}")

    print("\nTheme distribution:")
    for theme, data in sorted(theme_data.items(), key=lambda x: -x[1]["total_posts"]):
        print(f"  {theme}: {data['total_posts']} posts")

    print("\nSample high-scoring quotes:")
    top_quotes = sorted(all_quotes, key=lambda x: -x["score"])[:10]
    for q in top_quotes:
        print(f"\n  [{q['date']}] {q['title']}")
        print(f"  \"{q['quote'][:100]}...\"" if len(q['quote']) > 100 else f"  \"{q['quote']}\"")


if __name__ == "__main__":
    analyze_all_posts()
