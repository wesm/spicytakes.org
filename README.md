# Spicy Takes

A multi-blog archive platform that uses LLM-powered analysis to generate summaries, extract memorable quotes, and score "spiciness" of blog posts.

## Supported Blogs

| Blog | Author | Topics | Posts |
|------|--------|--------|-------|
| [benn.spicytakes.org](https://benn.spicytakes.org) | Benn Stancil | Data, analytics, startups | 240 |
| [mitsuhiko.spicytakes.org](https://mitsuhiko.spicytakes.org) | Armin Ronacher | Rust, Python, developer tools | 200 |
| [wesm.spicytakes.org](https://wesm.spicytakes.org) | Wes McKinney | Data infrastructure, Apache Arrow | 81 |
| [danluu.spicytakes.org](https://danluu.spicytakes.org) | Dan Luu | Performance, systems, industry myths | 111 |
| [bcantrill.spicytakes.org](https://bcantrill.spicytakes.org) | Bryan Cantrill | Systems software, startups | 174 |
| [jessfraz.spicytakes.org](https://jessfraz.spicytakes.org) | Jess Frazelle | Containers, security, hardware | 75 |
| [geohot.spicytakes.org](https://geohot.spicytakes.org) | George Hotz | AI, tinygrad, contrarian takes | 98 |
| [mrocklin.spicytakes.org](https://mrocklin.spicytakes.org) | Matt Rocklin | Dask, open source, startups | 199 |

## Project Structure

```
spicytakes.org/
├── config/
│   ├── <blog_id>.json      # Blog-specific config (themes, prompts, scraper settings)
│   └── landing.json        # Landing page configuration
├── blogs/
│   └── <blog_id>/
│       ├── posts/          # Markdown posts with YAML frontmatter
│       └── data/
│           ├── llm_quotes.json    # Combined LLM analysis
│           ├── spicy_quotes.json  # Spiciness scores
│           └── llm_analysis/      # Per-post analysis files
├── scripts/
│   ├── scrapers/           # Blog scrapers (Python)
│   ├── llm_analyze.sh      # LLM analysis pipeline
│   ├── grade_spiciness.sh  # Spiciness grading
│   ├── update.sh           # Full pipeline orchestrator
│   └── deploy.sh           # Vercel deployment script
├── src/                    # SvelteKit website
└── static/                 # Static assets (photos, etc.)
```

## Development

### Prerequisites

- Node.js 20+
- Python 3.10+
- Vercel CLI (for deployment)

### Setup

```bash
npm install
pip install requests beautifulsoup4
```

### Local Development

```bash
# Run dev server for a specific blog
npm run dev:benn
npm run dev:geohot
npm run dev:mrocklin
npm run dev:landing

# Or use the env variable directly
VITE_BLOG_ID=geohot npm run dev
```

## Content Pipeline

### 1. Scraping Posts

Each blog has a scraper configured in `config/<blog_id>.json`. Run with:

```bash
# Scrape a specific blog
BLOG_ID=geohot python scripts/scrapers/jekyll_feed.py
BLOG_ID=benn python scripts/scrapers/substack.py
BLOG_ID=mrocklin python scripts/scrapers/jekyll_feed.py

# Available scraper types:
# - substack.py         Substack blogs
# - github_markdown.py  GitHub-hosted markdown blogs
# - quarto_blog.py      Quarto blogs with transcripts
# - static_html.py      Static HTML blogs (danluu)
# - hugo_rss.py         Hugo blogs with RSS
# - hugo_homepage.py    Hugo blogs scraped from homepage
# - jekyll_feed.py      Jekyll/Atom feed blogs (geohot, mrocklin)
```

### 2. LLM Analysis

Generate summaries and extract quotes:

```bash
BLOG_ID=geohot ./scripts/llm_analyze.sh

# Single post (for testing)
BLOG_ID=geohot POST_FILE=blogs/geohot/posts/2025-12-29-five-years-of-tinygrad.md ./scripts/llm_analyze.sh
```

### 3. Spiciness Grading

Score quotes for "spiciness":

```bash
BLOG_ID=geohot ./scripts/grade_spiciness.sh
```

### 4. Full Pipeline

Run scrape + analyze + grade:

```bash
BLOG_ID=geohot ./scripts/update.sh
```

## Deployment

The site is deployed to Vercel with separate projects for each subdomain.

### Setup (One-time)

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   vercel login
   ```

2. Disable automatic Git deployments in Vercel dashboard for each project:
   - Go to Project → Settings → Git → Ignored Build Step
   - Enter: `exit 0`
   - Save

3. Set environment variables in each Vercel project:
   - Go to Project → Settings → Environment Variables
   - Add: `VITE_BLOG_ID` = `<blog_id>` (e.g., `geohot`, `landing`)

### Deploy

```bash
# Deploy a single site to production
./scripts/deploy.sh landing --prod
./scripts/deploy.sh geohot --prod
./scripts/deploy.sh mrocklin --prod

# Preview deploy (not production)
./scripts/deploy.sh geohot

# Deploy all sites
./scripts/deploy.sh --all --prod

# List available blogs
./scripts/deploy.sh --list
```

### Vercel Project Names

| Blog ID | Vercel Project |
|---------|----------------|
| landing | spicytakes.org |
| benn | spicy-takes-benn |
| armin | spicy-takes-armin |
| wesm | spicy-takes-wesm |
| danluu | spicy-takes-danluu |
| bcantrill | spicy-takes-bcantrill |
| jessfraz | spicy-takes-jessfraz |
| geohot | spicy-takes-geohot |
| mrocklin | spicy-takes-mrocklin |

## Adding a New Blog

1. Create config file: `config/<blog_id>.json`
   ```json
   {
     "id": "newblog",
     "name": "Author Name",
     "tagline": "Short description",
     "description": "Longer description",
     "sourceUrl": "https://example.com/blog",
     "sourceLabel": "example.com/blog",
     "scraper": {
       "type": "jekyll_feed",
       "baseUrl": "https://example.com",
       "feedUrl": "https://example.com/feed.xml"
     },
     "themes": { ... },
     "llmAnalysis": { ... },
     "spiciness": { ... }
   }
   ```

2. Add to `src/lib/config.ts`:
   ```typescript
   import newblogConfig from '../../config/newblog.json';
   // ...
   const configs = {
     // ...
     newblog: newblogConfig as BlogConfig,
   };
   ```

3. Add to `config/landing.json` (with `"hidden": true` initially)

4. Add npm scripts to `package.json`:
   ```json
   "dev:newblog": "VITE_BLOG_ID=newblog vite dev",
   "build:newblog": "VITE_BLOG_ID=newblog vite build"
   ```

5. Add to `scripts/deploy.sh` in `get_project_name()` and `ALL_BLOGS`

6. Run the pipeline:
   ```bash
   BLOG_ID=newblog python scripts/scrapers/<scraper>.py
   BLOG_ID=newblog ./scripts/llm_analyze.sh
   BLOG_ID=newblog ./scripts/grade_spiciness.sh
   ```

7. Create Vercel project, set `VITE_BLOG_ID` env var, deploy

8. Remove `"hidden": true` from landing.json when ready

## License

Content is archived for personal research purposes. All quotes link back to original posts.
