#!/bin/bash
# Update all (or specific) blogs: scrape, analyze, grade, and optionally build
#
# Usage:
#   ./scripts/update_all.sh                    # Update all blogs
#   ./scripts/update_all.sh benn armin mempko  # Update specific blogs only
#   NO_BUILD=1 ./scripts/update_all.sh         # Skip the build step (faster)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Source ALL_BLOGS from deploy.sh
ALL_BLOGS_LINE=$(grep '^ALL_BLOGS=' scripts/deploy.sh)
eval "$ALL_BLOGS_LINE"

# Remove "landing" from the list — it's not a blog
ALL_BLOGS=$(echo "$ALL_BLOGS" | tr ' ' '\n' | grep -v '^landing$' | tr '\n' ' ')

# If specific blogs passed as args, use those instead
if [[ $# -gt 0 ]]; then
    BLOGS="$*"
else
    BLOGS="$ALL_BLOGS"
fi

echo "=== Spicy Takes: Update All Blogs ==="
echo "Blogs: $BLOGS"
echo ""

# Track results per blog
declare -A POSTS_BEFORE
declare -A POSTS_AFTER
declare -A QUOTES_AFTER
FAILED_BLOGS=""

# Count posts before updating
for blog in $BLOGS; do
    index_file="blogs/$blog/data/posts_index.json"
    if [[ -f "$index_file" ]]; then
        POSTS_BEFORE[$blog]=$(python3 -c "import json; print(json.load(open('$index_file')).get('total_posts', 0))")
    else
        POSTS_BEFORE[$blog]=0
    fi
done

# Run update.sh for each blog
for blog in $BLOGS; do
    echo "========================================"
    echo "Updating: $blog"
    echo "========================================"

    if BLOG_ID="$blog" NO_BUILD="${NO_BUILD:-}" bash scripts/update.sh; then
        echo ""
    else
        echo "WARNING: update.sh failed for $blog"
        FAILED_BLOGS="$FAILED_BLOGS $blog"
        echo ""
    fi
done

# Collect post/quote counts after updating
for blog in $BLOGS; do
    index_file="blogs/$blog/data/posts_index.json"
    quotes_file="blogs/$blog/data/spicy_quotes.json"

    if [[ -f "$index_file" ]]; then
        POSTS_AFTER[$blog]=$(python3 -c "import json; print(json.load(open('$index_file')).get('total_posts', 0))")
    else
        POSTS_AFTER[$blog]=0
    fi

    if [[ -f "$quotes_file" ]]; then
        QUOTES_AFTER[$blog]=$(python3 -c "import json; print(json.load(open('$quotes_file')).get('total', 0))")
    else
        QUOTES_AFTER[$blog]=0
    fi
done

# Update landing.json stats from actual data files
echo "========================================"
echo "Updating landing.json stats..."
echo "========================================"

python3 -c "
import json, os

landing_path = 'config/landing.json'
with open(landing_path) as f:
    landing = json.load(f)

changed = False
for blog_entry in landing['blogs']:
    bid = blog_entry['id']
    index_file = f'blogs/{bid}/data/posts_index.json'
    quotes_file = f'blogs/{bid}/data/spicy_quotes.json'

    new_posts = None
    new_quotes = None

    if os.path.exists(index_file):
        with open(index_file) as f:
            new_posts = json.load(f).get('total_posts', 0)
    if os.path.exists(quotes_file):
        with open(quotes_file) as f:
            new_quotes = json.load(f).get('total', 0)

    old = blog_entry.get('stats', {})
    if new_posts is not None and old.get('posts') != new_posts:
        blog_entry.setdefault('stats', {})['posts'] = new_posts
        changed = True
    if new_quotes is not None and old.get('quotes') != new_quotes:
        blog_entry.setdefault('stats', {})['quotes'] = new_quotes
        changed = True

if changed:
    with open(landing_path, 'w') as f:
        json.dump(landing, f, indent=2)
        f.write('\n')
    print('landing.json updated')
else:
    print('landing.json already up to date')
"

# Print summary
echo ""
echo "========================================"
echo "Summary"
echo "========================================"
printf "%-15s %10s %10s %10s\n" "Blog" "New Posts" "Total" "Quotes"
printf "%-15s %10s %10s %10s\n" "----" "---------" "-----" "------"
for blog in $BLOGS; do
    before=${POSTS_BEFORE[$blog]:-0}
    after=${POSTS_AFTER[$blog]:-0}
    new=$((after - before))
    quotes=${QUOTES_AFTER[$blog]:-0}
    printf "%-15s %10d %10d %10d\n" "$blog" "$new" "$after" "$quotes"
done

if [[ -n "$FAILED_BLOGS" ]]; then
    echo ""
    echo "FAILED blogs:$FAILED_BLOGS"
fi

echo ""
echo "=== All Done ==="
