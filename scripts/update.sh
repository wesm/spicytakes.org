#!/bin/bash
# Incremental update script for Spicy Takes
# Fetches new posts, analyzes them, grades spiciness, and rebuilds the site
#
# Usage: ./scripts/update.sh
#
# Requirements:
# - Python 3 with requests, beautifulsoup4
# - Node.js with npm
# - codex CLI (for LLM analysis)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "=== Spicy Takes Incremental Update ==="
echo ""

# Step 1: Scrape new posts
echo "Step 1/4: Checking for new posts..."
python3 scripts/scrape.py
echo ""

# Step 2: Run LLM analysis on new posts
echo "Step 2/4: Running LLM analysis on new posts..."
bash scripts/llm_analyze.sh
echo ""

# Step 3: Grade spiciness on new quotes
echo "Step 3/4: Grading spiciness on new quotes..."
bash scripts/grade_spiciness.sh
echo ""

# Step 4: Rebuild the site
echo "Step 4/4: Rebuilding site..."
npm run build
echo ""

echo "=== Update Complete ==="
echo ""
echo "To preview locally: npm run preview"
echo "To deploy: git add -A && git commit -m 'Update posts' && git push"
