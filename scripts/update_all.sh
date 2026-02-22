#!/bin/bash
# Update all (or specific) blogs: scrape, analyze, grade, and optionally build
#
# Usage:
#   ./scripts/update_all.sh                    # Update all blogs
#   ./scripts/update_all.sh benn armin mempko  # Update specific blogs only

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
UTILS="$SCRIPT_DIR/update_stats.py"

cd "$PROJECT_DIR"

# Extract ALL_BLOGS from deploy.sh (no eval — parse the value safely)
ALL_BLOGS=$(grep '^ALL_BLOGS=' scripts/deploy.sh | sed 's/^ALL_BLOGS="//' | sed 's/"$//')

# Remove "landing" from the list
ALL_BLOGS=$(echo "$ALL_BLOGS" | tr ' ' '\n' | grep -v '^landing$' | tr '\n' ' ')

if [[ $# -gt 0 ]]; then
    BLOGS="$*"
else
    BLOGS="$ALL_BLOGS"
fi

echo "=== Spicy Takes: Update All Blogs ==="
echo "Blogs: $BLOGS"
echo ""

FAILED_BLOGS=""

for blog in $BLOGS; do
    echo "========================================"
    echo "Updating: $blog"
    echo "========================================"

    if BLOG_ID="$blog" bash scripts/update.sh; then
        echo ""
    else
        echo "WARNING: update.sh failed for $blog"
        FAILED_BLOGS="$FAILED_BLOGS $blog"
        echo ""
    fi
done

# Final landing.json reconciliation (in case any individual updates were skipped)
echo "========================================"
echo "Reconciling landing.json stats..."
echo "========================================"
python3 "$UTILS" update-landing --all

if [[ -n "$FAILED_BLOGS" ]]; then
    echo ""
    echo "FAILED blogs:$FAILED_BLOGS"
fi

echo ""
echo "=== All Done ==="
