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

## Notes

- Posts are archived for personal research purposes
- Always attribute quotes with links to original posts
- The `BLOG_ID` env var selects which blog to process/build
