#!/bin/bash
# Incremental update script for Spicy Takes
# Fetches new posts, analyzes them, grades spiciness, and updates stats
#
# Usage: BLOG_ID=benn ./scripts/update.sh
#
# Requirements:
# - Python 3 with requests, beautifulsoup4
# - Node.js with npm
# - codex CLI (for LLM analysis)

set -euo pipefail

if [[ -z "${BLOG_ID:-}" ]]; then
    echo "Error: BLOG_ID environment variable required"
    echo "Usage: BLOG_ID=benn ./scripts/update.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_DIR/config/${BLOG_ID}.json"
UTILS="$SCRIPT_DIR/update_stats.py"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found: $CONFIG_FILE"
    exit 1
fi

cd "$PROJECT_DIR"

echo "=== Spicy Takes Incremental Update ==="
echo "Blog: $BLOG_ID"
echo ""

SCRAPER_TYPE=$(python3 "$UTILS" config "$BLOG_ID" scraper.type)
POSTS_BEFORE=$(python3 "$UTILS" raw-post-count "$BLOG_ID")

# Step 1: Scrape new posts
echo "Step 1/4: Checking for new posts..."

# For github_markdown blogs, pull the local repo first (best-effort)
if [[ "$SCRAPER_TYPE" == "github_markdown" ]]; then
    LOCAL_PATH=$(python3 "$UTILS" config "$BLOG_ID" scraper.localPath --default "")
    if [[ -n "$LOCAL_PATH" ]]; then
        EXPANDED_PATH="${LOCAL_PATH/#\~/$HOME}"
        if [[ -d "$EXPANDED_PATH/.git" ]]; then
            echo "  Pulling latest from $EXPANDED_PATH..."
            git -C "$EXPANDED_PATH" pull || echo "  Warning: git pull failed, continuing with local state"
        fi
    fi
fi

# Validate scraper type is safe (alphanumeric + underscore only)
if [[ ! "$SCRAPER_TYPE" =~ ^[a-z0-9_]+$ ]]; then
    echo "Error: Invalid scraper type: $SCRAPER_TYPE"
    exit 1
fi
SCRAPER_SCRIPT="scripts/scrapers/${SCRAPER_TYPE}.py"
if [[ ! -f "$SCRAPER_SCRIPT" ]]; then
    echo "Error: No scraper found at $SCRAPER_SCRIPT"
    exit 1
fi
BLOG_ID="$BLOG_ID" python3 "$SCRAPER_SCRIPT"
echo ""

POSTS_AFTER=$(python3 "$UTILS" raw-post-count "$BLOG_ID")
NEW_POSTS=$((POSTS_AFTER - POSTS_BEFORE))

if [[ "$NEW_POSTS" -lt 0 ]]; then
    echo "Warning: Post count decreased ($POSTS_BEFORE -> $POSTS_AFTER). Possible data issue."
    echo ""
    echo "=== Update Aborted ==="
    exit 1
fi

BLOG_DIR="$PROJECT_DIR/blogs/$BLOG_ID"
ANALYSIS_DIR="$BLOG_DIR/data/llm_analysis"

# Check for failed analyses that need retrying
FAILED_ANALYSES=0
if [[ -d "$ANALYSIS_DIR" ]]; then
    FAILED_ANALYSES=$(python3 -c "
import json, glob, sys
count = 0
for f in glob.glob('$ANALYSIS_DIR/*.json'):
    try:
        with open(f) as fp:
            if 'error' in json.load(fp):
                count += 1
    except Exception:
        count += 1
print(count)
")
fi

if [[ "$NEW_POSTS" -eq 0 && "$FAILED_ANALYSES" -eq 0 ]]; then
    echo "No new posts found. Skipping analysis, grading, and build."
    echo ""
    echo "=== Update Complete (no changes) ==="
    exit 0
fi

if [[ "$NEW_POSTS" -gt 0 ]]; then
    echo "Found $NEW_POSTS new post(s)."
fi
if [[ "$FAILED_ANALYSES" -gt 0 ]]; then
    echo "Found $FAILED_ANALYSES failed analysis(es) to retry."
fi
echo ""

# Step 2: Run LLM analysis
echo "Step 2/4: Running LLM analysis..."
BLOG_ID="$BLOG_ID" bash scripts/llm_analyze.sh
echo ""

# Step 3: Grade spiciness
echo "Step 3/4: Grading spiciness..."
BLOG_ID="$BLOG_ID" bash scripts/grade_spiciness.sh
echo ""

# Step 4: Update landing.json post/quote counts
echo "Step 4/4: Updating landing page stats..."
python3 "$UTILS" update-landing "$BLOG_ID"
echo ""

echo "=== Update Complete ==="
echo ""
echo "To deploy: ./scripts/deploy.sh $BLOG_ID --prod"
