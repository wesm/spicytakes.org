#!/bin/bash
# LLM-powered analysis of blog posts
# Processes posts in parallel to extract summaries and money quotes
#
# Usage: BLOG_ID=benn ./scripts/llm_analyze.sh
# Single post: BLOG_ID=armin POST_FILE=blogs/armin/posts/2024-02-04-rye-a-vision.md ./scripts/llm_analyze.sh
#
# Environment variables:
#   BLOG_ID: required - which blog to process
#   LLM_BACKEND: "codex" (default) or "claude"
#   POST_FILE: optional - process single post only
#   FORCE: set to 1 to reprocess already-analyzed posts
#   PARALLEL_JOBS: number of parallel jobs (default 5)

set -e

# Require BLOG_ID
if [[ -z "$BLOG_ID" ]]; then
    echo "Error: BLOG_ID environment variable required"
    echo "Usage: BLOG_ID=benn ./scripts/llm_analyze.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_DIR/config/${BLOG_ID}.json"
BLOG_DIR="$PROJECT_DIR/blogs/$BLOG_ID"
POSTS_DIR="$BLOG_DIR/posts"
OUTPUT_DIR="$BLOG_DIR/data/llm_analysis"
PARALLEL_JOBS="${PARALLEL_JOBS:-5}"

# Validate config exists
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found: $CONFIG_FILE"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Read config values using Python
read_config() {
    python3 -c "import json; c=json.load(open('$CONFIG_FILE')); print($1)"
}

read_config_default() {
    python3 -c "import json; c=json.load(open('$CONFIG_FILE')); print($1)" 2>/dev/null || echo "$2"
}

AUTHOR_NAME=$(read_config "c['name']")
CONTEXT_PROMPT=$(read_config "c['llmAnalysis']['contextPrompt']")
THEMES_LIST=$(read_config "', '.join(c['themes'].keys())")
SUMMARY_LENGTH=$(read_config_default "c['llmAnalysis'].get('summaryLength', '2-3 sentences')" "2-3 sentences")
DETAILED_BREAKDOWN=$(read_config_default "str(c['llmAnalysis'].get('detailedBreakdown', False)).lower()" "false")
MAX_WORDS=$(read_config_default "c['llmAnalysis'].get('maxWords', 150)" "150")
NUM_QUOTES=$(read_config_default "c['llmAnalysis'].get('numQuotes', '3-5')" "3-5")

# Build the prompt based on config
# Schema is consistent: always includes key_points (empty array if not detailed)
build_prompt() {
    local content="$1"

    if [[ "$DETAILED_BREAKDOWN" == "true" ]]; then
        cat <<PROMPT
$CONTEXT_PROMPT

Analyze this blog post in depth (up to $MAX_WORDS words total). Extract:

1. **Summary** ($SUMMARY_LENGTH): The post's main argument and conclusion
2. **Key Points** (3-5 bullets): The distinct arguments, insights, or observations made
3. **Money Quotes** ($NUM_QUOTES): The most memorable, quotable sentences that capture key insights. Choose lines that are self-contained and impactful out of context.
4. **Themes**: Which of these themes apply? $THEMES_LIST
5. **Tone**: The post's overall tone (e.g., critical, optimistic, reflective, satirical, technical, opinionated)
6. **Key Insight**: One sentence capturing the core takeaway

Output as JSON (no markdown fences):
{
  "summary": "...",
  "key_points": ["point1", "point2", ...],
  "money_quotes": ["quote1", "quote2", ...],
  "themes": ["theme1", "theme2"],
  "tone": "...",
  "key_insight": "..."
}

POST CONTENT:
$content
PROMPT
    else
        cat <<PROMPT
$CONTEXT_PROMPT

Your task is to extract:
1. A $SUMMARY_LENGTH summary of the post's main argument
2. The $NUM_QUOTES best "money quotes" - memorable, quotable sentences that capture key insights
3. Key themes (from: $THEMES_LIST)
4. The post's overall tone (e.g., critical, optimistic, reflective, satirical, analytical)
5. One sentence key insight capturing the core takeaway

Output as JSON (no markdown fences):
{
  "summary": "...",
  "key_points": [],
  "money_quotes": ["quote1", "quote2", ...],
  "themes": ["theme1", "theme2"],
  "tone": "...",
  "key_insight": "..."
}

POST CONTENT:
$content
PROMPT
    fi
}

analyze_post() {
    local post_file="$1"
    local filename=$(basename "$post_file" .md)
    local output_file="$OUTPUT_DIR/${filename}.json"

    # Skip if already analyzed (unless FORCE=1)
    if [[ -f "$output_file" && "$FORCE" != "1" ]]; then
        echo "Skipping $filename (already analyzed)"
        return 0
    fi

    echo "Analyzing: $filename"

    local content=$(cat "$post_file")
    local tmpfile=$(mktemp)
    local prompt=$(build_prompt "$content")

    # Use llm_call.sh for backend abstraction (codex or claude)
    echo "$prompt" | "$SCRIPT_DIR/llm_call.sh" "$tmpfile" 2>/dev/null || true

    if [[ -f "$tmpfile" && -s "$tmpfile" ]]; then
        # Extract JSON from the response using robust parsing
        python3 -c "
import sys
import json
import re

content = open('$tmpfile').read()

def extract_json(text):
    '''Extract JSON object from text, handling braces inside strings correctly.'''
    decoder = json.JSONDecoder()

    # First try: look for fenced json code block, extract content, parse with raw_decode
    fenced = re.search(r'\`\`\`json\s*(.*?)\s*\`\`\`', text, re.DOTALL)
    if fenced:
        fenced_content = fenced.group(1).strip()
        # Find first { in fenced content and use raw_decode
        start = fenced_content.find('{')
        if start != -1:
            try:
                obj, end = decoder.raw_decode(fenced_content[start:])
                if 'summary' in obj:
                    return fenced_content[start:start+end]
            except json.JSONDecodeError:
                pass  # Fall through to unfenced scan

    # Second try: find first { and use json.JSONDecoder to find matching }
    start = text.find('{')
    if start == -1:
        return None

    try:
        # Try to decode starting from each { until one works
        for i in range(start, len(text)):
            if text[i] == '{':
                try:
                    obj, end = decoder.raw_decode(text[i:])
                    if 'summary' in obj:  # Verify it's our expected object
                        return text[i:i+end]
                except json.JSONDecodeError:
                    continue
    except Exception:
        pass

    return None

json_str = extract_json(content)
if json_str:
    try:
        data = json.loads(json_str)
        data['filename'] = '$filename'
        # Ensure consistent schema with defaults
        data.setdefault('key_points', [])
        data.setdefault('key_insight', '')
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(json.dumps({'filename': '$filename', 'error': 'parse_failed', 'raw': content[:500]}))
else:
    print(json.dumps({'filename': '$filename', 'error': 'no_json', 'raw': content[:500]}))
" > "$output_file" 2>/dev/null || echo "{\"filename\": \"$filename\", \"error\": \"processing_failed\"}" > "$output_file"

        # Show output if single post mode
        if [[ -n "$POST_FILE" ]]; then
            echo ""
            echo "=== Analysis Result ==="
            cat "$output_file"
        fi

        rm -f "$tmpfile"
        echo "  Done: $filename"
    else
        echo "{\"filename\": \"$filename\", \"error\": \"llm_failed\"}" > "$output_file"
        rm -f "$tmpfile"
        echo "  Failed: $filename"
    fi
}

export -f analyze_post
export -f build_prompt
export OUTPUT_DIR
export CONTEXT_PROMPT
export THEMES_LIST
export SUMMARY_LENGTH
export DETAILED_BREAKDOWN
export MAX_WORDS
export NUM_QUOTES
export FORCE
export POST_FILE
export SCRIPT_DIR
export LLM_BACKEND

LLM_BACKEND="${LLM_BACKEND:-codex}"
echo "=== $AUTHOR_NAME Post Analysis with ${LLM_BACKEND} ==="
echo "Posts directory: $POSTS_DIR"
echo "Output directory: $OUTPUT_DIR"
echo "LLM backend: $LLM_BACKEND"
echo "Summary length: $SUMMARY_LENGTH"
echo "Detailed breakdown: $DETAILED_BREAKDOWN"
echo "Max words: $MAX_WORDS"
echo "Num quotes: $NUM_QUOTES"
echo ""

# Single post mode
if [[ -n "$POST_FILE" ]]; then
    echo "Single post mode: $POST_FILE"
    analyze_post "$PROJECT_DIR/$POST_FILE"
    exit 0
fi

# Count total posts
total=$(ls "$POSTS_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "Total posts to analyze: $total"
echo "Parallel jobs: $PARALLEL_JOBS"
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
data_dir = os.path.dirname(output_dir)
results = []

for f in sorted(glob.glob(os.path.join(output_dir, "*.json"))):
    try:
        with open(f) as fp:
            data = json.load(fp)
            results.append(data)
    except Exception as e:
        print(f"Error reading {f}: {e}")

# Save combined results
combined_file = os.path.join(data_dir, "llm_quotes.json")
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

quotes_file = os.path.join(data_dir, "best_quotes.json")
with open(quotes_file, "w") as fp:
    json.dump({"total": len(all_quotes), "quotes": all_quotes}, fp, indent=2)

print(f"Extracted {len(all_quotes)} money quotes into {quotes_file}")
PYEOF

echo ""
echo "Done!"
