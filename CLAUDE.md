# Spicy Takes - Multi-Blog Archive Platform

## Project Overview

This project archives and analyzes blog content from multiple authors with LLM-powered summaries, money quotes, and spiciness scoring. Currently supports:

- **Benn Stancil** (Substack) - Data, analytics, startups, tech industry
- **Armin Ronacher** (lucumr) - Rust, Python, open source, tooling
- **Wes McKinney** (wesmckinney.com) - Data infrastructure, Apache Arrow, Python

## Project Structure

```
spicy-takes/
├── config/
│   ├── benn.json               # Blog-specific themes, prompts, scraper config
│   ├── armin.json
│   └── wesm.json
├── blogs/
│   ├── benn/
│   │   ├── posts/              # Markdown posts with YAML frontmatter
│   │   └── data/
│   │       ├── llm_quotes.json     # Combined LLM analysis
│   │       ├── spicy_quotes.json   # Spiciness scores
│   │       └── llm_analysis/       # Per-post analysis files
│   ├── armin/
│   │   └── ...
│   └── wesm/
│       └── ...
├── scripts/
│   ├── scrapers/
│   │   ├── base.py             # Shared scraper interface
│   │   ├── substack.py         # Substack scraper
│   │   ├── github_markdown.py  # GitHub markdown scraper (lucumr-style)
│   │   └── quarto_blog.py      # Quarto blog + transcripts scraper
│   ├── llm_analyze.sh          # LLM analysis with codex
│   ├── grade_spiciness.sh      # Spiciness grading
│   └── update.sh               # Full pipeline orchestrator
└── src/                        # SvelteKit website
```

## Running the Scripts

All scripts require `BLOG_ID` environment variable.

```bash
# Full update pipeline (scrape + analyze + grade + build)
BLOG_ID=benn ./scripts/update.sh

# Individual scrapers
BLOG_ID=benn python scripts/scrapers/substack.py
BLOG_ID=armin python scripts/scrapers/github_markdown.py
BLOG_ID=wesm python scripts/scrapers/quarto_blog.py

# LLM analysis
BLOG_ID=benn ./scripts/llm_analyze.sh

# Single post analysis (for testing)
BLOG_ID=benn POST_FILE=blogs/benn/posts/2024-01-15-post.md ./scripts/llm_analyze.sh

# Spiciness grading
BLOG_ID=benn ./scripts/grade_spiciness.sh
```

## Development

```bash
npm install
VITE_BLOG_ID=benn npm run dev      # Dev server
VITE_BLOG_ID=benn npm run build    # Production build
```

## Key Configuration

Each blog config (`config/<blog_id>.json`) contains:

- `id`, `name`, `tagline`, `description` - Blog identity
- `sourceUrl`, `sourceLabel` - Original source link
- `scraper` - Type and paths for the scraper
- `themes` - Topic categories with labels and icons
- `llmAnalysis` - Prompts and settings for LLM analysis
- `spiciness` - Context prompt for spiciness grading

## Adding a New Blog

Every new blog requires updates in ALL of these places (do not skip any):

1. `config/<blog_id>.json` - Create blog config (scraper, themes, LLM prompts, spiciness)
2. `src/lib/config.ts` - Add import AND add to the `configs` map (both are required)
3. `package.json` - Add `dev:<blog_id>` and `build:<blog_id>` scripts
4. `scripts/deploy.sh` - Add to `ALL_BLOGS` list AND add case in `get_project_name()`
5. `config/landing.json` - Add entry to the `blogs` array with initial stats `{ "posts": 0, "quotes": 0 }`

After all registration is done, run the full pipeline:

```bash
BLOG_ID=<id> python3 scripts/scrapers/<scraper_type>.py   # Scrape posts
BLOG_ID=<id> ./scripts/llm_analyze.sh                     # LLM analysis
BLOG_ID=<id> ./scripts/grade_spiciness.sh                 # Spiciness grading
```

Then update `config/landing.json` stats with the correct counts (see below).

Verify with `npm run dev:<blog_id>` before deploying.

## Post and Quote Counts

There are three different post counts — do not confuse them:

- `posts_index.json` `total_posts`: Raw scrape count (all posts fetched from the blog)
- `llm_quotes.json` posts without `"error"`: Posts with successful LLM analysis
- The website only shows posts with successful analysis

**The `config/landing.json` stats `posts` field must use the successful analysis count** (posts without errors from `llm_quotes.json`), NOT the raw scrape count. The quote count comes from `spicy_quotes.json` `total`.

To get the correct counts for landing.json:

```bash
# Successful posts (what the site actually shows)
python3 -c "import json; d=json.load(open('blogs/<id>/data/llm_quotes.json')); print(sum(1 for p in d['posts'] if 'error' not in p))"

# Total graded quotes
python3 -c "import json; d=json.load(open('blogs/<id>/data/spicy_quotes.json')); print(d['total'])"
```

Note: `scripts/update_all.sh` currently uses `posts_index.json` `total_posts` (the raw count), which overstates the number. This is a known bug.

## Notes

- Posts are archived for personal research purposes
- Always attribute quotes with links to original posts
- The `BLOG_ID` env var selects which blog to process/build
