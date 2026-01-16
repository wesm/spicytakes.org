#!/bin/bash
# LLM-powered analysis of Benn Stancil posts using codex exec
# Processes posts in parallel to extract summaries and money quotes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
POSTS_DIR="$PROJECT_DIR/posts"
OUTPUT_DIR="$PROJECT_DIR/data/llm_analysis"
PARALLEL_JOBS="${PARALLEL_JOBS:-5}"

mkdir -p "$OUTPUT_DIR"

analyze_post() {
    local post_file="$1"
    local filename=$(basename "$post_file" .md)
    local output_file="$OUTPUT_DIR/${filename}.json"

    # Skip if already analyzed
    if [[ -f "$output_file" ]]; then
        echo "Skipping $filename (already analyzed)"
        return 0
    fi

    echo "Analyzing: $filename"

    local content=$(cat "$post_file")
    local tmpfile=$(mktemp)

    codex exec --skip-git-repo-check --sandbox read-only -c reasoning_effort=medium \
        -o "$tmpfile" - >/dev/null 2>&1 <<EOF
You are analyzing a blog post by Benn Stancil, a prominent writer on data, analytics, startups, and tech industry trends.

Your task is to extract:
1. A 2-3 sentence summary of the post's main argument
2. The 3-5 best "money quotes" - memorable, quotable sentences that capture key insights
3. Key themes (from: data_infrastructure, analytics_practice, ai_llms, startups_vc, career, industry_criticism, tools_products)
4. The post's overall tone (e.g., critical, optimistic, reflective, satirical, analytical)

Output as JSON with this structure:
{
  "summary": "...",
  "money_quotes": ["quote1", "quote2", ...],
  "themes": ["theme1", "theme2"],
  "tone": "...",
  "key_insight": "One sentence capturing the core insight"
}

POST CONTENT:
$content
EOF

    if [[ -f "$tmpfile" && -s "$tmpfile" ]]; then
        # Extract just the JSON from the response
        python3 -c "
import sys
import json
import re

content = open('$tmpfile').read()

# Try to find JSON in the response
json_match = re.search(r'\{[^{}]*\"summary\"[^{}]*\}', content, re.DOTALL)
if json_match:
    try:
        data = json.loads(json_match.group())
        data['filename'] = '$filename'
        print(json.dumps(data, indent=2))
    except:
        # If JSON parsing fails, create a minimal record
        print(json.dumps({'filename': '$filename', 'error': 'parse_failed', 'raw': content[:500]}))
else:
    print(json.dumps({'filename': '$filename', 'error': 'no_json', 'raw': content[:500]}))
" > "$output_file" 2>/dev/null || echo "{\"filename\": \"$filename\", \"error\": \"processing_failed\"}" > "$output_file"
        rm -f "$tmpfile"
        echo "  Done: $filename"
    else
        echo "{\"filename\": \"$filename\", \"error\": \"codex_failed\"}" > "$output_file"
        rm -f "$tmpfile"
        echo "  Failed: $filename"
    fi
}

export -f analyze_post
export OUTPUT_DIR

echo "=== Benn Stancil Post Analysis with Codex ==="
echo "Posts directory: $POSTS_DIR"
echo "Output directory: $OUTPUT_DIR"
echo "Parallel jobs: $PARALLEL_JOBS"
echo ""

# Count total posts
total=$(ls "$POSTS_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "Total posts to analyze: $total"
echo ""

# Process in parallel
if command -v parallel &> /dev/null; then
    echo "Using GNU parallel..."
    ls "$POSTS_DIR"/*.md | parallel -j "$PARALLEL_JOBS" analyze_post {}
else
    echo "Using xargs (install GNU parallel for better progress)..."
    ls "$POSTS_DIR"/*.md | xargs -P "$PARALLEL_JOBS" -I {} bash -c 'analyze_post "$@"' _ {}
fi

echo ""
echo "=== Combining Results ==="

# Combine all JSON files into one
python3 <<PYEOF
import json
import glob
import os

output_dir = "$OUTPUT_DIR"
results = []

for f in sorted(glob.glob(os.path.join(output_dir, "*.json"))):
    try:
        with open(f) as fp:
            data = json.load(fp)
            results.append(data)
    except Exception as e:
        print(f"Error reading {f}: {e}")

# Save combined results
combined_file = os.path.join(os.path.dirname(output_dir), "llm_quotes.json")
with open(combined_file, "w") as fp:
    json.dump({
        "total_posts": len(results),
        "successful": len([r for r in results if "error" not in r]),
        "posts": results
    }, fp, indent=2)

print(f"Combined {len(results)} analyses into {combined_file}")

# Extract all money quotes
all_quotes = []
for r in results:
    if "money_quotes" in r:
        for q in r["money_quotes"]:
            all_quotes.append({
                "quote": q,
                "filename": r.get("filename", "unknown"),
                "themes": r.get("themes", [])
            })

quotes_file = os.path.join(os.path.dirname(output_dir), "best_quotes.json")
with open(quotes_file, "w") as fp:
    json.dump({"total": len(all_quotes), "quotes": all_quotes}, fp, indent=2)

print(f"Extracted {len(all_quotes)} money quotes into {quotes_file}")
PYEOF

echo ""
echo "Done!"
