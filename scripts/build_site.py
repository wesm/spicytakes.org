#!/usr/bin/env python3
"""
Static site generator for Benn Stancil's intellectual footprint.
Creates an HTML website showcasing themes, quotes, and evolution of ideas.
"""

import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
POSTS_DIR = BASE_DIR / "posts"
WEBSITE_DIR = BASE_DIR / "website"

QUOTES_FILE = DATA_DIR / "quotes.json"
THEMES_FILE = DATA_DIR / "themes.json"
INDEX_FILE = DATA_DIR / "posts_index.json"


def load_data():
    """Load analysis data."""
    quotes = {}
    themes = {}
    posts_index = {}

    if QUOTES_FILE.exists():
        with open(QUOTES_FILE) as f:
            quotes = json.load(f)

    if THEMES_FILE.exists():
        with open(THEMES_FILE) as f:
            themes = json.load(f)

    if INDEX_FILE.exists():
        with open(INDEX_FILE) as f:
            posts_index = json.load(f)

    return quotes, themes, posts_index


def generate_css():
    """Generate CSS styles."""
    return """
:root {
    --bg-color: #fafafa;
    --text-color: #1a1a1a;
    --accent-color: #6366f1;
    --card-bg: #ffffff;
    --border-color: #e5e7eb;
    --quote-bg: #f3f4f6;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background: var(--bg-color);
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

header {
    text-align: center;
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border-color);
}

h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
}

.subtitle {
    color: #666;
    font-size: 1.1rem;
}

.stats {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
}

.stat {
    text-align: center;
}

.stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: var(--accent-color);
}

.stat-label {
    font-size: 0.875rem;
    color: #666;
}

nav {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

nav a {
    padding: 0.5rem 1rem;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    text-decoration: none;
    color: var(--text-color);
    transition: all 0.2s;
}

nav a:hover, nav a.active {
    background: var(--accent-color);
    color: white;
    border-color: var(--accent-color);
}

section {
    margin-bottom: 3rem;
}

h2 {
    font-size: 1.75rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--accent-color);
}

.theme-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
}

.theme-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 0.75rem;
    padding: 1.5rem;
    transition: transform 0.2s, box-shadow 0.2s;
}

.theme-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.theme-name {
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    text-transform: capitalize;
}

.theme-count {
    color: var(--accent-color);
    font-size: 0.875rem;
}

.quote-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.quote-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 0.75rem;
    padding: 1.5rem;
    border-left: 4px solid var(--accent-color);
}

.quote-text {
    font-size: 1.1rem;
    font-style: italic;
    margin-bottom: 1rem;
    line-height: 1.7;
}

.quote-text::before {
    content: '"';
    color: var(--accent-color);
    font-size: 1.5rem;
}

.quote-text::after {
    content: '"';
    color: var(--accent-color);
    font-size: 1.5rem;
}

.quote-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.quote-source {
    font-size: 0.875rem;
}

.quote-source a {
    color: var(--accent-color);
    text-decoration: none;
}

.quote-source a:hover {
    text-decoration: underline;
}

.quote-date {
    font-size: 0.875rem;
    color: #666;
}

.quote-themes {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 0.75rem;
}

.theme-tag {
    background: var(--quote-bg);
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    font-size: 0.75rem;
    color: #666;
}

.timeline {
    position: relative;
    padding-left: 2rem;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--border-color);
}

.timeline-year {
    margin-bottom: 2rem;
}

.timeline-year h3 {
    font-size: 1.25rem;
    color: var(--accent-color);
    margin-bottom: 1rem;
    position: relative;
}

.timeline-year h3::before {
    content: '';
    position: absolute;
    left: -2rem;
    top: 50%;
    transform: translateY(-50%);
    width: 12px;
    height: 12px;
    background: var(--accent-color);
    border-radius: 50%;
}

.timeline-posts {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.timeline-post {
    font-size: 0.9rem;
}

.timeline-post a {
    color: var(--text-color);
    text-decoration: none;
}

.timeline-post a:hover {
    color: var(--accent-color);
}

.timeline-post .date {
    color: #666;
    font-size: 0.8rem;
}

footer {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid var(--border-color);
    color: #666;
    font-size: 0.875rem;
}

footer a {
    color: var(--accent-color);
}

@media (max-width: 768px) {
    body {
        padding: 1rem;
    }

    h1 {
        font-size: 1.75rem;
    }

    .stats {
        gap: 1rem;
    }

    .stat-value {
        font-size: 1.5rem;
    }
}
"""


def generate_html(quotes, themes, posts_index):
    """Generate the main HTML page."""
    total_posts = posts_index.get("total_posts", 0)
    total_quotes = quotes.get("total_quotes", 0)
    theme_count = len(themes.get("themes", {}))

    # Get date range
    posts = posts_index.get("posts", [])
    if posts:
        dates = [p.get("date", "")[:10] for p in posts if p.get("date")]
        if dates:
            earliest = min(dates)
            latest = max(dates)
            date_range = f"{earliest[:4]} - {latest[:4]}"
        else:
            date_range = "N/A"
    else:
        date_range = "N/A"

    # Build theme cards
    theme_cards = []
    for theme_name, theme_data in sorted(
        themes.get("themes", {}).items(),
        key=lambda x: -x[1]["total_posts"]
    ):
        display_name = theme_name.replace("_", " ").title()
        theme_cards.append(f"""
        <div class="theme-card">
            <div class="theme-name">{display_name}</div>
            <div class="theme-count">{theme_data['total_posts']} posts</div>
        </div>
        """)

    # Build quote cards (top 50 by score)
    quote_cards = []
    sorted_quotes = sorted(
        quotes.get("quotes", []),
        key=lambda x: -x.get("score", 0)
    )[:50]

    for q in sorted_quotes:
        themes_html = "".join(
            f'<span class="theme-tag">{t.replace("_", " ")}</span>'
            for t in q.get("themes", [])[:3]
        )
        quote_cards.append(f"""
        <div class="quote-card">
            <div class="quote-text">{q['quote']}</div>
            <div class="quote-meta">
                <span class="quote-source">
                    <a href="{q.get('url', '#')}" target="_blank">{q['title']}</a>
                </span>
                <span class="quote-date">{q['date']}</span>
            </div>
            <div class="quote-themes">{themes_html}</div>
        </div>
        """)

    # Build timeline by year
    posts_by_year = {}
    for p in sorted(posts, key=lambda x: x.get("date", ""), reverse=True):
        date = p.get("date", "")
        if date:
            year = date[:4]
            if year not in posts_by_year:
                posts_by_year[year] = []
            posts_by_year[year].append(p)

    timeline_html = []
    for year in sorted(posts_by_year.keys(), reverse=True):
        year_posts = posts_by_year[year][:10]  # Show up to 10 per year
        posts_html = "".join(
            f"""<div class="timeline-post">
                <span class="date">{p['date'][:10]}</span>
                <a href="{p.get('url', '#')}" target="_blank">{p['title']}</a>
            </div>"""
            for p in year_posts
        )
        if len(posts_by_year[year]) > 10:
            posts_html += f'<div class="timeline-post">...and {len(posts_by_year[year]) - 10} more</div>'

        timeline_html.append(f"""
        <div class="timeline-year">
            <h3>{year}</h3>
            <div class="timeline-posts">{posts_html}</div>
        </div>
        """)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Benn Stancil's Intellectual Footprint</title>
    <style>{generate_css()}</style>
</head>
<body>
    <header>
        <h1>Benn Stancil's Intellectual Footprint</h1>
        <p class="subtitle">An archive and analysis of writings from <a href="https://benn.substack.com">benn.substack.com</a></p>
        <div class="stats">
            <div class="stat">
                <div class="stat-value">{total_posts}</div>
                <div class="stat-label">Posts</div>
            </div>
            <div class="stat">
                <div class="stat-value">{total_quotes}</div>
                <div class="stat-label">Quotes Extracted</div>
            </div>
            <div class="stat">
                <div class="stat-value">{theme_count}</div>
                <div class="stat-label">Themes</div>
            </div>
            <div class="stat">
                <div class="stat-value">{date_range}</div>
                <div class="stat-label">Time Span</div>
            </div>
        </div>
    </header>

    <nav>
        <a href="#themes">Themes</a>
        <a href="#quotes">Money Quotes</a>
        <a href="#timeline">Timeline</a>
    </nav>

    <section id="themes">
        <h2>Key Themes</h2>
        <div class="theme-grid">
            {''.join(theme_cards)}
        </div>
    </section>

    <section id="quotes">
        <h2>Money Quotes</h2>
        <div class="quote-list">
            {''.join(quote_cards)}
        </div>
    </section>

    <section id="timeline">
        <h2>Timeline</h2>
        <div class="timeline">
            {''.join(timeline_html)}
        </div>
    </section>

    <footer>
        <p>Generated on {datetime.now().strftime('%Y-%m-%d')} |
        Original content at <a href="https://benn.substack.com">benn.substack.com</a></p>
        <p>This is a personal research project archiving and analyzing Benn Stancil's public writings.</p>
    </footer>
</body>
</html>
"""


def build_site():
    """Build the static website."""
    print("Building website...")

    # Create website directory
    WEBSITE_DIR.mkdir(parents=True, exist_ok=True)

    # Load data
    quotes, themes, posts_index = load_data()

    if not posts_index.get("posts"):
        print("No posts found in index. Run scrape.py and analyze.py first.")
        return

    # Generate HTML
    html = generate_html(quotes, themes, posts_index)

    # Write index.html
    index_path = WEBSITE_DIR / "index.html"
    with open(index_path, "w") as f:
        f.write(html)

    print(f"Website built: {index_path}")
    print(f"Open in browser: file://{index_path.absolute()}")


if __name__ == "__main__":
    build_site()
