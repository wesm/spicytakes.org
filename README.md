# Spicy Takes - Multi-Blog Archive Platform

A platform for archiving and analyzing blog content with LLM-powered summaries, "money quotes," and spiciness scoring. Currently supports multiple blogs including Benn Stancil's Substack, Armin Ronacher's lucumr, and Wes McKinney's blog.

## Quick Start

```bash
npm install
VITE_BLOG_ID=benn npm run dev  # or armin, wesm
```

Then open http://localhost:5173

## Project Structure

```
spicy-takes/
├── src/                        # SvelteKit website source
├── config/
│   ├── benn.json               # Benn Stancil config (Substack)
│   ├── armin.json              # Armin Ronacher config (GitHub markdown)
│   └── wesm.json               # Wes McKinney config (Quarto blog)
├── blogs/
│   ├── benn/
│   │   ├── posts/              # Markdown posts with YAML frontmatter
│   │   └── data/               # LLM analysis and spiciness data
│   ├── armin/
│   │   ├── posts/
│   │   └── data/
│   └── wesm/
│       ├── posts/
│       └── data/
└── scripts/
    ├── scrapers/
    │   ├── base.py             # Shared scraper interface
    │   ├── substack.py         # Substack scraper
    │   ├── github_markdown.py  # GitHub markdown scraper
    │   └── quarto_blog.py      # Quarto blog scraper
    ├── llm_analyze.sh          # Run LLM analysis with codex
    ├── grade_spiciness.sh      # Grade quotes on spiciness
    └── update.sh               # Full pipeline orchestrator
```

## Features

### Website Views

- **Timeline** - Posts organized by year, searchable
- **Quotes** - Money quotes in single-column layout
  - Sort by date or spiciness
  - Filter by year or minimum spice level
  - "Spiciest First" shows top 5 per year
- **Themes** - Topic areas with avg spiciness scores

### Data

Each post has:
- **Summary** - 2-6 sentence overview (configurable per blog)
- **Key Insight** - Core takeaway
- **Money Quotes** - 3-8 memorable, quotable sentences
- **Themes** - Topics configured per blog
- **Tone** - e.g., "sardonic, analytical, critical"
- **Spiciness** (1-10) - How provocative/biting the take is

## Running the Data Pipeline

All scripts require `BLOG_ID` environment variable.

### Full Update (Recommended)

```bash
BLOG_ID=benn ./scripts/update.sh
```

This runs all steps: scrape, analyze, grade, and build.

### Individual Steps

#### 1. Scrape Posts

```bash
# Substack blog
BLOG_ID=benn python scripts/scrapers/substack.py

# GitHub markdown blog (e.g., lucumr)
BLOG_ID=armin python scripts/scrapers/github_markdown.py

# Quarto blog with transcripts
BLOG_ID=wesm python scripts/scrapers/quarto_blog.py
```

#### 2. LLM Analysis (requires codex CLI)

```bash
BLOG_ID=benn ./scripts/llm_analyze.sh

# Single post mode for testing
BLOG_ID=benn POST_FILE=blogs/benn/posts/2024-01-15-some-post.md ./scripts/llm_analyze.sh

# Force re-analysis
BLOG_ID=benn FORCE=1 ./scripts/llm_analyze.sh
```

#### 3. Spiciness Grading (requires codex CLI)

```bash
BLOG_ID=benn ./scripts/grade_spiciness.sh
```

## Development

```bash
VITE_BLOG_ID=benn npm run dev      # Dev server at localhost:5173
VITE_BLOG_ID=benn npm run build    # Production build
VITE_BLOG_ID=benn npm run preview  # Preview production build
```

## Adding a New Blog

1. Create `config/<blog_id>.json` with themes, prompts, and scraper config
2. Add scraper support if needed (or use existing type)
3. Update `src/lib/config.ts` to import the new config
4. Update `src/lib/data.ts` to import the new blog's data
5. Run `BLOG_ID=<blog_id> ./scripts/update.sh`

## Tech Stack

- **Scraping**: Python, BeautifulSoup, requests, PyYAML
- **Analysis**: OpenAI Codex CLI
- **Website**: SvelteKit, Svelte 5, Tailwind CSS v4
- **Typography**: Inter (UI), Newsreader (quotes)

## Supported Blogs

| Blog | Type | Posts |
|------|------|-------|
| Benn Stancil | Substack | ~240 |
| Armin Ronacher | GitHub Markdown | ~200 |
| Wes McKinney | Quarto + Transcripts | ~81 |
