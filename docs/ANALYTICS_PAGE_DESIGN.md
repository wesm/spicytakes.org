# Spicy Takes Analytics Page - Design Document

**Status:** Draft v1
**Authors:** Wes McKinney, with input from Benn Stancil
**Date:** 2026-01-27

## Overview

Create an analytics dashboard at `spicytakes.org/analytics` that provides fun, insightful visualizations and curated content across all archived blog data. The goal is to surface interesting patterns, crown the spiciest takes, and let users explore the data in new ways.

## Data Available

We have rich data across **22 blogs**:
- **Quotes:** 10,000+ with spiciness scores (1-10 scale)
- **Posts:** 2,000+ with summaries, themes, tone analysis
- **Themes:** 6-9 per blog (data infrastructure, AI/LLMs, career, industry criticism, etc.)
- **Time Range:** 2006-2026 (varies by author)

---

## Proposed Sections

### 1. Spiciness Over Time (Hero Visualization)

**The main attraction** - a time series chart showing spiciness trends.

**Visualization:**
- X-axis: Time (monthly or quarterly buckets)
- Y-axis: Spiciness score (1-10)
- Line: Rolling average (e.g., 6-month or 12-month window)
- Shaded band: ± 1 standard deviation
- Optional: Scatter plot of individual quotes behind the trend line

**Interactions:**
- Toggle between individual blogs or "All Authors" aggregate
- Hover to see specific quotes that contributed to peaks
- Click peaks to see the spiciest quotes from that period

**Fun Insights:**
- "The Great Spicening of 2023" - label notable peaks
- Correlate with industry events (GPT-4 launch, tech layoffs, etc.)

---

### 2. Spiciest Takes Hall of Fame

**Curated showcase of the hottest takes ever recorded.**

**Display:**
- Top 10 (or 25) spiciest quotes across all blogs
- Beautiful quote cards with:
  - The quote itself
  - Spiciness score (with fire emojis scale)
  - Author + post title + date
  - Theme badges
  - Link to original

**Variations:**
- "All Time Greatest" - overall top quotes
- "Spiciest Per Author" - each author's hottest take
- "Spiciest Per Theme" - hottest take in each category
- "Spiciest Per Year" - annual champions

---

### 3. Author Leaderboard

**Who brings the heat?**

**Metrics per author:**
- Average spiciness score
- Total "10/10" quotes (perfect spice)
- Spiciness consistency (low std dev = consistently spicy)
- Total quotes analyzed
- Most common themes

**Display:**
- Ranked cards or table
- Sparkline showing spiciness trend over time
- "Spice Style" badge: "Consistently Warm", "Occasional Inferno", "Slow Burn", etc.

---

### 4. Theme Analytics

**Which topics bring the most heat?**

**Visualizations:**

**A) Theme Heatmap:**
| Theme | Avg Spiciness | Quote Count | Spiciest Quote |
|-------|---------------|-------------|----------------|
| Industry Criticism | 7.2 | 342 | "VCs are..." |
| AI/LLMs | 6.8 | 521 | "ChatGPT is..." |

**B) Theme Radar Chart:**
- Spider/radar chart showing each author's spiciness per theme
- Compare authors: "Benn is spiciest on startups, Armin on Rust tooling"

**C) Theme Evolution:**
- Stacked area chart showing theme popularity over time
- "AI/LLMs" theme explodes in 2023, etc.

---

### 5. Distribution Deep Dive

**Understanding the spiciness landscape.**

**Visualizations:**

**A) Histogram:**
- Distribution of all spiciness scores
- "Most quotes are 5-6, but there's a long tail of 9-10s"

**B) Box Plots:**
- Per-author or per-theme distributions
- Show median, quartiles, outliers

**C) Cumulative Distribution:**
- "90% of quotes are below spiciness 7"
- "Only 2% of quotes reach 10/10"

---

### 6. Fun Stats & Records

**Quick hits of interesting data.**

**Examples:**
- **Longest 10/10 quote:** [quote] - X words
- **Most prolific spicy author:** [name] - X quotes scored 8+
- **Spiciest month ever:** March 2023 (avg 7.4 spiciness)
- **Most controversial theme:** Industry Criticism (highest variance)
- **Quote of the Day:** Random high-spiciness quote (refreshes daily)

---

### 7. Spicy Streaks & Events

**When did authors go on hot streaks?**

**Display:**
- Timeline markers for notable periods
- "Benn's 2023 AI Rant Series" - 5 posts in 2 months, avg spiciness 8.2
- "Armin's Rust Tooling Crusade" - 8 posts on Rust in Q2 2024

**Correlation Opportunities:**
- Map spicy periods to industry events
- GPT-4 launch, Twitter/X changes, tech layoffs, etc.

---

### 8. Search & Filter (Unified)

**Let users explore freely.**

- Filter by: Author, Theme, Year range, Min spiciness
- Sort by: Spiciness, Date, Quote length
- Search within quotes

---

## Technical Approach

### Data Architecture: DuckDB + Parquet

**Why this stack:**
- **Parquet:** Columnar format, excellent compression, fast analytical reads
- **DuckDB:** Blazing fast OLAP queries, zero external dependencies
- **duckdb-wasm:** Run DuckDB in the browser - no server needed for queries
- **Mosaic:** Declarative visualization grammar backed by DuckDB queries

This gives us:
- Sub-millisecond query latency in the browser
- Rich SQL for ad-hoc exploration
- Linked, interactive visualizations via Mosaic
- Single source of truth (Parquet file)

### Data Pipeline

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  JSON Data      │────▶│  ETL Script     │────▶│  quotes.parquet │
│  (per blog)     │     │  (Python/DuckDB)│     │  (unified)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                        ┌───────────────────────────────┘
                        ▼
              ┌─────────────────┐
              │  duckdb-wasm    │
              │  (browser)      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │    Mosaic       │
              │  (visualizations)│
              └─────────────────┘
```

### Parquet Schema

```sql
-- Main quotes table
CREATE TABLE quotes (
  quote_id        INTEGER PRIMARY KEY,
  quote_text      VARCHAR,
  spiciness       TINYINT,         -- 1-10

  -- Post info
  post_filename   VARCHAR,
  post_title      VARCHAR,
  post_date       DATE,
  post_year       SMALLINT,
  post_month      TINYINT,
  post_url        VARCHAR,

  -- Author info
  author_id       VARCHAR,         -- 'benn', 'armin', etc.
  author_name     VARCHAR,         -- 'Benn Stancil', etc.

  -- Analysis
  themes          VARCHAR[],       -- array of theme IDs
  tone            VARCHAR,
  summary         VARCHAR,
  key_insight     VARCHAR,

  -- Derived
  quote_length    INTEGER,         -- char count
  word_count      INTEGER
);

-- Materialized aggregations (for fast initial load)
CREATE TABLE author_stats AS
SELECT
  author_id,
  author_name,
  COUNT(*) as quote_count,
  AVG(spiciness) as avg_spiciness,
  STDDEV(spiciness) as std_spiciness,
  COUNT(*) FILTER (WHERE spiciness = 10) as perfect_10s,
  MIN(post_date) as first_post,
  MAX(post_date) as last_post
FROM quotes
GROUP BY author_id, author_name;

CREATE TABLE monthly_stats AS
SELECT
  DATE_TRUNC('month', post_date) as month,
  author_id,
  COUNT(*) as quote_count,
  AVG(spiciness) as avg_spiciness,
  STDDEV(spiciness) as std_spiciness
FROM quotes
WHERE post_date IS NOT NULL
GROUP BY 1, 2;

CREATE TABLE theme_stats AS
SELECT
  UNNEST(themes) as theme,
  author_id,
  COUNT(*) as quote_count,
  AVG(spiciness) as avg_spiciness
FROM quotes
GROUP BY 1, 2;
```

### ETL Script

```python
# scripts/build_analytics_parquet.py
import duckdb
import json
from pathlib import Path

def build_parquet():
    con = duckdb.connect()

    # Load all blog data
    quotes = []
    for config_file in Path('config').glob('*.json'):
        blog_id = config_file.stem
        config = json.load(open(config_file))

        # Load spicy quotes
        spicy_path = Path(f'blogs/{blog_id}/data/spicy_quotes.json')
        if spicy_path.exists():
            spicy = json.load(open(spicy_path))
            for q in spicy:
                quotes.append({
                    'quote_text': q['quote'],
                    'spiciness': q['spiciness'],
                    'post_filename': q['filename'],
                    'author_id': blog_id,
                    'author_name': config['name'],
                    'themes': q.get('themes', []),
                    # ... etc
                })

    # Create table from list of dicts
    con.execute("CREATE TABLE quotes AS SELECT * FROM quotes_df")

    # Export to parquet
    con.execute("COPY quotes TO 'static/data/quotes.parquet' (FORMAT PARQUET)")

    # Also export pre-aggregated stats for fast initial render
    con.execute("COPY (SELECT ...) TO 'static/data/stats.parquet'")
```

### Mosaic Integration

[Mosaic](https://github.com/uwdata/mosaic) provides:
- **vgplot:** Declarative visualization specs (Vega-Lite style)
- **Coordinator:** Manages DuckDB connection and query routing
- **Linked selections:** Brush one chart, filter all others
- **Optimized queries:** Automatic query planning and caching

```javascript
// Example: Linked spiciness dashboard
import { coordinator, vgplot } from '@uwdata/mosaic';
import * as duckdb from '@duckdb/duckdb-wasm';

// Initialize DuckDB-WASM
const db = await duckdb.createDuckDB();
await coordinator().databaseConnector(db);

// Load parquet directly in browser
await coordinator().exec(`
  CREATE TABLE quotes AS
  SELECT * FROM 'quotes.parquet'
`);

// Create linked visualizations
const spicyOverTime = vgplot.plot({
  marks: [
    vgplot.lineY(
      vgplot.from('monthly_stats'),
      { x: 'month', y: 'avg_spiciness', stroke: 'author_id' }
    ),
    vgplot.areaY(
      vgplot.from('monthly_stats'),
      {
        x: 'month',
        y1: sql`avg_spiciness - std_spiciness`,
        y2: sql`avg_spiciness + std_spiciness`,
        fill: 'author_id',
        opacity: 0.2
      }
    )
  ],
  // Brush selection links to other charts
  interactors: [vgplot.brushX({ as: 'timeRange' })]
});

const spicyDistribution = vgplot.plot({
  marks: [
    vgplot.rectY(
      vgplot.from('quotes', { filterBy: 'timeRange' }),  // Linked!
      vgplot.binX({ y: 'count' }, { x: 'spiciness' })
    )
  ]
});
```

### Why Mosaic?

[Mosaic](https://uwdata.github.io/mosaic/) from UW Data is uniquely suited here:

**Key Features:**
- **DuckDB-native:** Visualizations are backed by SQL queries, not JSON data blobs
- **Linked views:** Brush one chart → all others update automatically
- **Scalable:** Handles millions of rows via query pushdown
- **Declarative:** Vega-Lite-like grammar, but with live SQL
- **Cross-filtering:** Click on "Benn" → all charts filter to Benn's data

**Example Interactions:**
```
┌─────────────────────────────────────────────────────────────┐
│  [Brush time range on timeline]                              │
│       ↓ linked                                               │
│  [Distribution updates to show only selected period]         │
│       ↓ linked                                               │
│  [Quote list filters to selected period]                     │
└─────────────────────────────────────────────────────────────┘
```

**Mosaic Inputs (interactive widgets):**
- `menu`: Dropdown for author/theme selection
- `search`: Text search over quote text
- `slider`: Spiciness threshold
- `brush`: Time range selection on charts

All inputs automatically update all visualizations that reference them.

### Route Structure

```
/analytics                    # Main dashboard
/analytics/author/[id]        # Deep dive per author
/analytics/theme/[theme]      # Theme-specific view
/analytics/hall-of-fame       # Top quotes showcase
/analytics/explore            # Free-form SQL explorer (fun!)
```

### Performance Considerations

**Initial Load:**
- Parquet file size: ~1-5MB compressed (efficient!)
- Pre-aggregated stats for instant first paint
- Progressive loading: show stats first, load full data async

**Query Performance:**
- DuckDB-WASM handles 100K+ rows easily
- Complex aggregations in <100ms
- Mosaic caches query results automatically

**Build Time:**
- ETL runs at build time (npm run build)
- Parquet regenerated when source data changes
- Can also run incrementally for new posts only

---

## Visual Design Ideas

### Color Palette (Spiciness Scale)
```
1-2:  Cool blue     #3B82F6
3-4:  Mild green    #22C55E
5-6:  Warm yellow   #EAB308
7-8:  Hot orange    #F97316
9-10: Fire red      #EF4444
```

### Spiciness Indicators
- **Numeric badge:** Simple "7.2" with colored background
- **Fire emojis:** 🔥🔥🔥 (1-3 fires based on score)
- **Pepper scale:** 🌶️🌶️🌶️🌶️🌶️ (1-5 peppers)
- **Temperature gauge:** Visual thermometer

### Dashboard Layout
```
┌─────────────────────────────────────────────────────────┐
│  SPICY TAKES ANALYTICS                    [Filter] [Search] │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐ │
│  │     SPICINESS OVER TIME (Hero Chart)                │ │
│  │     [Rolling avg line with ±1 STD band]             │ │
│  └─────────────────────────────────────────────────────┘ │
├──────────────────────────┬──────────────────────────────┤
│  HALL OF FAME            │  AUTHOR LEADERBOARD          │
│  ┌────────────────────┐  │  ┌────────────────────────┐  │
│  │ Top 5 Spiciest     │  │  │ 1. Benn      7.2 avg   │  │
│  │ Quotes All Time    │  │  │ 2. Armin     6.8 avg   │  │
│  │ [Quote cards...]   │  │  │ 3. Wes       6.5 avg   │  │
│  └────────────────────┘  │  └────────────────────────┘  │
├──────────────────────────┴──────────────────────────────┤
│  THEME BREAKDOWN                                         │
│  [Heatmap or cards showing spiciness by theme]          │
├─────────────────────────────────────────────────────────┤
│  FUN STATS                                               │
│  [Grid of interesting metrics and records]               │
└─────────────────────────────────────────────────────────┘
```

---

## MVP Scope (Phase 1)

Build these first:
1. **Spiciness Over Time chart** - The hero visualization
2. **Hall of Fame** - Top 25 spiciest quotes all-time
3. **Author Leaderboard** - Rankings with key stats
4. **Basic Stats Grid** - Quick interesting numbers

## Phase 2 Enhancements

- Theme analytics and heatmap
- Author deep-dive pages
- Distribution charts
- Spicy streaks timeline
- "Quote of the Day" feature

## Phase 3 Ideas (Future)

- Compare any two authors side-by-side
- User voting on spiciness (wisdom of crowds vs LLM)
- "Spiciness prediction" - guess the score before reveal
- RSS feed of new spicy quotes
- Social sharing cards for quotes

---

## Open Questions

1. **Mosaic vs custom D3:** Mosaic is powerful but adds complexity. Worth it for linked brushing?
2. **Mobile experience:** How do Mosaic charts adapt? May need responsive fallbacks.
3. **Cross-blog vs single-blog:** Default to unified view with author filter? Or separate pages?
4. **Parquet hosting:** Serve from static/ or use a CDN for faster global access?
5. **Spiciness calibration:** Are LLM scores comparable across blogs? May need normalization.
6. **SQL Explorer:** Expose a "playground" for users to write custom queries? Fun but risky.

---

## Next Steps

1. [ ] Review and refine this design doc
2. [ ] Build ETL script (`scripts/build_analytics_parquet.py`)
3. [ ] Prototype DuckDB-WASM + Mosaic integration in Svelte
4. [ ] Create `/analytics` route with hero time series chart
5. [ ] Add Hall of Fame and Author Leaderboard sections
6. [ ] Iterate on interactions and linked filtering

---

*Let's make data deliciously spicy.* 🌶️
