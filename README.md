# Benn Stancil - Intellectual Footprint

An archive and analysis of [Benn Stancil's Substack](https://benn.substack.com), featuring 240 posts from 2021-2026 with LLM-powered summaries, "money quotes," and spiciness scoring.

## Quick Start

```bash
# Run the website
cd web
npm install
npm run dev
```

Then open http://localhost:5173

## Project Structure

```
benn-stancil/
├── posts/                  # 240 markdown posts with YAML frontmatter
├── data/
│   ├── llm_quotes.json     # LLM analysis (summaries, quotes, themes)
│   ├── spicy_quotes.json   # Spiciness scores (1-10) for all quotes
│   └── llm_analysis/       # Individual post analysis files
├── scripts/
│   ├── scrape.py           # Download posts from Substack
│   ├── llm_analyze.sh      # Run LLM analysis with codex
│   └── grade_spiciness.sh  # Grade quotes on spiciness
└── web/                    # SvelteKit website
```

## Features

### Website Views

- **Timeline** - Posts organized by year, searchable
- **Quotes** - 1,185 money quotes in single-column layout
  - Sort by date or spiciness
  - Filter by year or minimum spice level
  - "Spiciest First" shows top 5 per year
- **Themes** - 7 topic areas with avg spiciness scores

### Data

Each post has:
- **Summary** - 2-3 sentence overview
- **Key Insight** - Core takeaway
- **Money Quotes** - 3-5 memorable, quotable sentences
- **Themes** - Topics like `ai_llms`, `startups_vc`, `industry_criticism`
- **Tone** - e.g., "sardonic, analytical, critical"
- **Spiciness** (1-10) - How provocative/biting the take is

## Running the Data Pipeline

### 1. Scrape Posts (already done)

```bash
python scripts/scrape.py
```

Downloads all posts as markdown to `posts/`.

### 2. LLM Analysis (requires codex CLI)

```bash
bash scripts/llm_analyze.sh
```

Uses GPT-5 via codex to extract summaries and quotes. Requires a [Codex](https://openai.com/codex) subscription.

### 3. Spiciness Grading (requires codex CLI)

```bash
bash scripts/grade_spiciness.sh
```

Grades each quote 1-10 on "spiciness" - how sardonic, biting, or contrarian.

## Development

```bash
cd web
npm run dev      # Dev server at localhost:5173
npm run build    # Production build to web/build/
npm run preview  # Preview production build
```

## Tech Stack

- **Scraping**: Python, BeautifulSoup, requests
- **Analysis**: OpenAI Codex CLI (GPT-5)
- **Website**: SvelteKit, Svelte 5, Tailwind CSS v4
- **Typography**: Inter (UI), Newsreader (quotes)

## Stats

- **240** posts (Feb 2021 - Jan 2026)
- **1,185** money quotes extracted
- **7** themes identified
- **4.4** average spiciness score
- Top spiciness: **9** (several quotes)

## Sample Spicy Quotes

> "Databricks is a $38 billion dollar mistake." (Spiciness: 9)

> "Every LLM vendor is eighteen months from dead." (Spiciness: 9)

> "They turn systemic racism into systematic racism, encoded and executed at scale." (Spiciness: 9)
