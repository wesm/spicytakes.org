#!/bin/bash
# Grade quotes on "spiciness" (1-10) using LLM
# Scores how provocative, sardonic, or biting each quote is
#
# Usage: BLOG_ID=benn ./scripts/grade_spiciness.sh
#
# Environment variables:
#   BLOG_ID: required - which blog to process
#   LLM_BACKEND: "claude" (default) or "codex"

set -e

# Require BLOG_ID
if [[ -z "$BLOG_ID" ]]; then
    echo "Error: BLOG_ID environment variable required"
    echo "Usage: BLOG_ID=benn ./scripts/grade_spiciness.sh"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$PROJECT_DIR/config/${BLOG_ID}.json"
BLOG_DIR="$PROJECT_DIR/blogs/$BLOG_ID"
export DATA_DIR="$BLOG_DIR/data"
export OUTPUT_FILE="$DATA_DIR/spicy_quotes.json"

# Validate config exists
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Config file not found: $CONFIG_FILE"
    exit 1
fi

# Read config values
AUTHOR_NAME=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['name'])")
SPICY_CONTEXT=$(python3 -c "import json; print(json.load(open('$CONFIG_FILE'))['spiciness']['contextPrompt'])")

export AUTHOR_NAME
export SPICY_CONTEXT
export LLM_BACKEND="${LLM_BACKEND:-claude}"
export LLM_CALL_SCRIPT="$SCRIPT_DIR/llm_call.sh"

echo "=== Grading Spiciness with ${LLM_BACKEND} ==="
echo "Blog: $BLOG_ID"
echo "LLM backend: $LLM_BACKEND"
echo ""

# Read all quotes and process them
python3 <<'PYEOF'
import json
import os
import subprocess
import tempfile
from pathlib import Path

DATA_DIR = Path(os.environ.get('DATA_DIR', 'data'))
OUTPUT_FILE = Path(os.environ.get('OUTPUT_FILE', 'data/spicy_quotes.json'))
AUTHOR_NAME = os.environ.get('AUTHOR_NAME', 'Author')
SPICY_CONTEXT = os.environ.get('SPICY_CONTEXT', '')
LLM_CALL_SCRIPT = os.environ.get('LLM_CALL_SCRIPT', 'scripts/llm_call.sh')

# Load existing quotes
llm_quotes_file = DATA_DIR / 'llm_quotes.json'
if not llm_quotes_file.exists():
    print(f"Error: {llm_quotes_file} not found. Run llm_analyze.sh first.")
    exit(1)

with open(llm_quotes_file) as f:
    data = json.load(f)

# Build list of all quotes with metadata
all_quotes = []
for post in data['posts']:
    if 'error' in post or 'money_quotes' not in post:
        continue
    for quote in post['money_quotes']:
        all_quotes.append({
            'quote': quote,
            'filename': post['filename'],
            'themes': post.get('themes', []),
            'tone': post.get('tone', ''),
            'summary': post.get('summary', ''),
            'key_insight': post.get('key_insight', '')
        })

print(f"Total quotes to grade: {len(all_quotes)}")

# Check for existing graded quotes
existing = {}
if OUTPUT_FILE.exists():
    with open(OUTPUT_FILE) as f:
        existing_data = json.load(f)
        for q in existing_data.get('quotes', []):
            key = q['quote'] + q['filename']
            existing[key] = q.get('spiciness', 0)
    print(f"Found {len(existing)} already graded")

# Process in batches of 10 (smaller for better context)
BATCH_SIZE = 10
graded_quotes = []

for i in range(0, len(all_quotes), BATCH_SIZE):
    batch = all_quotes[i:i+BATCH_SIZE]
    batch_num = i // BATCH_SIZE + 1
    total_batches = (len(all_quotes) + BATCH_SIZE - 1) // BATCH_SIZE

    # Check if all in batch already graded
    all_graded = all((q['quote'] + q['filename']) in existing for q in batch)
    if all_graded:
        for q in batch:
            q['spiciness'] = existing[q['quote'] + q['filename']]
            graded_quotes.append(q)
        print(f"Batch {batch_num}/{total_batches}: skipped (already graded)")
        continue

    print(f"Batch {batch_num}/{total_batches}: grading {len(batch)} quotes...")

    # Build prompt with full context for each quote
    quotes_with_context = []
    for j, q in enumerate(batch):
        context = f"""{j+1}. QUOTE: "{q['quote']}"
   POST SUMMARY: {q['summary']}
   POST TONE: {q['tone']}
   KEY INSIGHT: {q['key_insight']}"""
        quotes_with_context.append(context)

    quotes_text = "\n\n".join(quotes_with_context)

    prompt = f"""You are grading quotes from {AUTHOR_NAME}'s blog on "spiciness" - how provocative, sardonic, biting, or contrarian the take is.

{SPICY_CONTEXT}

A spicy quote is one that:
- Takes a contrarian or unpopular position
- Uses sharp wit, irony, or sarcasm
- Critiques industry conventions, hype, or sacred cows
- Makes a bold, potentially controversial claim
- Punctures pretension or calls out hypocrisy
- Has a memorable, quotable "drop the mic" quality

Score each quote from 1-10:
- 1-3: Mild - straightforward observation, neutral insight
- 4-5: Moderate - some edge but mostly analytical
- 6-7: Pointed - clear opinion with bite
- 8-9: Spicy - provocative, memorable, quotable zinger
- 10: Maximum heat - devastating takedown or brilliantly biting

QUOTES TO GRADE (with post context):

{quotes_text}

Return ONLY a JSON array of {len(batch)} integers, one score per quote, in order.
Example for {len(batch)} quotes: {json.dumps(list(range(5, 5 + len(batch))))}

JSON array of scores:"""

    # Call LLM via llm_call.sh helper
    result_file = tempfile.mktemp(suffix='.txt')

    try:
        result = subprocess.run([
            LLM_CALL_SCRIPT,
            result_file
        ], input=prompt, text=True, timeout=180, stdout=subprocess.PIPE)

        with open(result_file) as f:
            result_text = f.read().strip()

        # Parse scores
        import re
        match = re.search(r'\[[\d,\s]+\]', result_text)
        if match:
            scores = json.loads(match.group())
            if len(scores) == len(batch):
                for j, q in enumerate(batch):
                    q['spiciness'] = scores[j]
                    graded_quotes.append(q)
                print(f"  Scores: {scores}")
            else:
                print(f"  FATAL: got {len(scores)} scores for {len(batch)} quotes")
                print(f"  Raw response: {result_text[:200]}")
                # Save progress before exiting
                if graded_quotes:
                    output = {'total': len(graded_quotes), 'quotes': graded_quotes, 'incomplete': True}
                    with open(OUTPUT_FILE, 'w') as f:
                        json.dump(output, f, indent=2)
                    print(f"  Saved {len(graded_quotes)} quotes before failure")
                exit(1)
        else:
            print(f"  FATAL: couldn't parse scores from response")
            print(f"  Raw response: {result_text[:200]}")
            # Save progress before exiting
            if graded_quotes:
                output = {'total': len(graded_quotes), 'quotes': graded_quotes, 'incomplete': True}
                with open(OUTPUT_FILE, 'w') as f:
                    json.dump(output, f, indent=2)
                print(f"  Saved {len(graded_quotes)} quotes before failure")
            exit(1)

    except Exception as e:
        print(f"  FATAL: {e}")
        # Save progress before exiting
        if graded_quotes:
            output = {'total': len(graded_quotes), 'quotes': graded_quotes, 'incomplete': True}
            with open(OUTPUT_FILE, 'w') as f:
                json.dump(output, f, indent=2)
            print(f"  Saved {len(graded_quotes)} quotes before failure")
        exit(1)
    finally:
        if os.path.exists(result_file):
            os.unlink(result_file)

    # Save progress every 10 batches
    if batch_num % 10 == 0:
        output = {'total': len(graded_quotes), 'quotes': graded_quotes, 'incomplete': True}
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(output, f, indent=2)
        print(f"  Progress saved ({len(graded_quotes)} quotes)")

# Sort by date (filename contains date)
graded_quotes.sort(key=lambda q: q['filename'], reverse=True)

# Save results
output = {
    'total': len(graded_quotes),
    'quotes': graded_quotes
}

with open(OUTPUT_FILE, 'w') as f:
    json.dump(output, f, indent=2)

print(f"\nSaved {len(graded_quotes)} graded quotes to {OUTPUT_FILE}")

# Print some stats
scores = [q['spiciness'] for q in graded_quotes]
print(f"\nScore distribution:")
for s in range(1, 11):
    count = scores.count(s)
    bar = '#' * (count // 5) if count > 0 else ''
    print(f"  {s:2d}: {bar} ({count})")

avg = sum(scores) / len(scores) if scores else 0
print(f"\nAverage spiciness: {avg:.1f}")

# Show top 10 spiciest
print(f"\nTop 10 spiciest quotes:")
sorted_quotes = sorted(graded_quotes, key=lambda q: q['spiciness'], reverse=True)
for i, q in enumerate(sorted_quotes[:10]):
    print(f"  {i+1}. [{q['spiciness']}] \"{q['quote'][:80]}...\"")
PYEOF

echo ""
echo "Done!"
