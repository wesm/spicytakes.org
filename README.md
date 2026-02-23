# Spicy Takes

Spicy Takes is a multi-blog archive and analysis platform.

It pulls posts from selected authors, stores normalized markdown, and runs an LLM pipeline to produce:
- summaries
- key quotes
- theme tags
- a "spiciness" score for memorable takes

Live site: `https://spicytakes.org`

## What This Repo Contains

- A SvelteKit frontend for landing pages and per-author sites
- Config-driven scrapers for many blog platforms (RSS, Substack, Hugo, Quarto, static HTML, and more)
- A CLI-driven content pipeline for scrape -> analyze -> score -> deploy
- Generated datasets under `blogs/<blog_id>/data`

## Quick Start

### Prerequisites

- Node.js `24.x` (see `package.json` engines)
- Python `3.10+`
- `pip` and `venv`

### Install

```bash
npm install
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

### Run Locally

```bash
# Landing site
npm run dev:landing

# Any specific blog site
npm run dev:benn
npm run dev:wesm

# Generic form
VITE_BLOG_ID=benn npm run dev
```

## Content Pipeline

### One-command update for a blog

```bash
BLOG_ID=benn ./scripts/update.sh
```

This runs:
1. scrape new posts
2. LLM analysis
3. spiciness grading
4. landing-page stats update

### Orchestration CLI

```bash
# Show status for all configured blogs
./scripts/spicy status

# Update one blog
./scripts/spicy update benn

# Update all blogs
./scripts/spicy update --all

# Rebuild landing stats from stored data
./scripts/spicy sync-stats
```

### LLM backend requirements

The LLM steps use `scripts/llm_call.sh`, which supports:
- `LLM_BACKEND=claude` (default, requires `claude` CLI)
- `LLM_BACKEND=codex` (requires `codex` CLI)

Example:

```bash
LLM_BACKEND=codex BLOG_ID=benn ./scripts/llm_analyze.sh
LLM_BACKEND=codex BLOG_ID=benn ./scripts/grade_spiciness.sh
```

## Deployment

Deployments are handled with `scripts/deploy.sh` (Vercel-targeted).

```bash
# List configured deploy targets
./scripts/deploy.sh --list

# Deploy one site
./scripts/deploy.sh benn --prod

# Deploy everything
./scripts/deploy.sh --all --prod
```

## Repository Layout

```text
config/                    Blog configs + landing config
blogs/<blog_id>/posts/     Normalized post markdown
blogs/<blog_id>/data/      Derived analysis + indexes + quote datasets
scripts/scrapers/          Source-specific scrapers
scripts/*.sh               Analysis/grading/update/deploy scripts
src/                       SvelteKit app
static/                    Static assets
```

## Content Ownership and Attribution

Important: source content ownership is retained by original authors/publishers.

- All scraped posts, transcribed text, and quoted source content committed under `blogs/<blog_id>/` belong to the original author or rights holder for that blog.
- This repository does not claim ownership of third-party source material.
- Generated metadata in this repo (summaries, scores, indexes, tags) is supplemental analysis and does not replace the original source.
- Every blog entry should preserve clear attribution and source links.

If you are a rights holder and want content corrected or removed, open an issue with the relevant paths.

## Code License

The code in this repository is licensed under the MIT License. See [LICENSE](LICENSE).

For clarity, third-party source content under `blogs/<blog_id>/` (including scraped posts and transcribed text) is not re-licensed by MIT and remains owned by the original author or rights holder.
