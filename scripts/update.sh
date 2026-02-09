#!/bin/bash
# Incremental update script for Spicy Takes
# Fetches new posts, analyzes them, grades spiciness, and rebuilds the site
#
# Usage: BLOG_ID=benn ./scripts/update.sh
#
# Requirements:
# - Python 3 with requests, beautifulsoup4
# - Node.js with npm
# - codex CLI (for LLM analysis)

set -e

# Require BLOG_ID
if [[ -z "$BLOG_ID" ]]; then
    echo "Error: BLOG_ID environment variable required"
    echo "Usage: BLOG_ID=benn ./scripts/update.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_DIR/config/${BLOG_ID}.json"

# Validate config exists
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found: $CONFIG_FILE"
    exit 1
fi

cd "$PROJECT_DIR"

echo "=== Spicy Takes Incremental Update ==="
echo "Blog: $BLOG_ID"
echo ""

# Read scraper type from config
SCRAPER_TYPE=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['scraper']['type'])")

# Step 1: Scrape new posts (based on scraper type)
echo "Step 1/4: Checking for new posts..."
case "$SCRAPER_TYPE" in
    substack)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/substack.py
        ;;
    github_markdown)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/github_markdown.py
        ;;
    quarto_blog)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/quarto_blog.py
        ;;
    static_html)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/static_html.py
        ;;
    hugo_rss)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/hugo_rss.py
        ;;
    hugo_homepage)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/hugo_homepage.py
        ;;
    jekyll_feed)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/jekyll_feed.py
        ;;
    jekyll_static)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/jekyll_static.py
        ;;
    blogger)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/blogger.py
        ;;
    ghost)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/ghost.py
        ;;
    medium)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/medium.py
        ;;
    rss_nextjs)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/rss_nextjs.py
        ;;
    wordpress)
        BLOG_ID="$BLOG_ID" python3 scripts/scrapers/wordpress.py
        ;;
    *)
        echo "Unknown scraper type: $SCRAPER_TYPE"
        exit 1
        ;;
esac
echo ""

# Step 2: Run LLM analysis on new posts
echo "Step 2/4: Running LLM analysis on new posts..."
BLOG_ID="$BLOG_ID" bash scripts/llm_analyze.sh
echo ""

# Step 3: Grade spiciness on new quotes
echo "Step 3/4: Grading spiciness on new quotes..."
BLOG_ID="$BLOG_ID" bash scripts/grade_spiciness.sh
echo ""

# Step 4: Rebuild the site
echo "Step 4/4: Rebuilding site..."
VITE_BLOG_ID="$BLOG_ID" npm run build
echo ""

echo "=== Update Complete ==="
echo ""
echo "To preview locally: VITE_BLOG_ID=$BLOG_ID npm run preview"
echo "To deploy: git add -A && git commit -m 'Update $BLOG_ID posts' && git push"
