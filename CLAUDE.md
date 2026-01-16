# Benn Stancil Substack Archive & Analysis

## Project Overview

This project archives and analyzes Benn Stancil's Substack (https://benn.substack.com), a prolific writer on data, analytics, startups, and the tech industry. The goal is to:

1. Download all posts as markdown files
2. Extract key quotes ("money quotes") from each post
3. Analyze themes and evolution of thinking over time
4. Build a website showcasing his intellectual arc

## Corpus

- **Source**: https://benn.substack.com
- **Posts**: 244 articles (as of January 2026)
- **Date Range**: February 2021 - January 2026
- **Frequency**: Approximately weekly

## Project Structure

```
benn-stancil/
├── CLAUDE.md              # This file
├── scripts/               # Scraping and analysis scripts
│   ├── scrape.py         # Download posts to markdown
│   ├── analyze.py        # Extract themes and quotes
│   └── build_site.py     # Generate static website
├── posts/                 # Raw markdown files (one per post)
├── data/
│   ├── posts.json        # Post metadata index
│   ├── quotes.json       # Extracted money quotes
│   └── themes.json       # Identified themes over time
└── website/              # Static site output
```

## Key Themes to Track

Based on initial review, Benn frequently writes about:

- **Data Infrastructure**: Modern data stack, dbt, Snowflake, Fivetran, data warehouses
- **Analytics Practice**: Role of analysts, data teams, self-serve analytics, BI tools
- **Startup/VC Dynamics**: Fundraising, valuations, startup culture, YC
- **AI/LLMs**: Impact on data work, SQL chatbots, automation of analysis
- **Industry Criticism**: Contrarian takes on trends, hype cycles, tech culture

## Running the Scripts

```bash
# Install dependencies
pip install -r requirements.txt

# Scrape all posts
python scripts/scrape.py

# Run analysis
python scripts/analyze.py

# Build website
python scripts/build_site.py
```

## Notes

- Respect rate limits when scraping
- Posts are archived for personal research purposes
- Always attribute quotes to Benn Stancil with links to original posts
