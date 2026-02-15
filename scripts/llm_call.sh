#!/bin/bash
# LLM backend abstraction - supports codex and claude
#
# Usage:
#   echo "prompt" | ./scripts/llm_call.sh output.txt
#   LLM_BACKEND=claude echo "prompt" | ./scripts/llm_call.sh output.txt
#
# Environment variables:
#   LLM_BACKEND: "claude" (default) or "codex"
#   LLM_MODEL: model to use (codex: o3-mini, claude: default from CLI)

set -e

OUTPUT_FILE="${1:--}"
LLM_BACKEND="${LLM_BACKEND:-claude}"

# Preflight check: verify selected backend is available
case "$LLM_BACKEND" in
    codex)
        if ! command -v codex &> /dev/null; then
            echo "Error: codex CLI not found. Install it or set LLM_BACKEND=claude." >&2
            exit 1
        fi
        ;;
    claude)
        if ! command -v claude &> /dev/null; then
            echo "Error: claude CLI not found. Install it or set LLM_BACKEND=codex." >&2
            exit 1
        fi
        ;;
esac

# Read prompt from stdin
PROMPT=$(cat)

case "$LLM_BACKEND" in
    codex)
        echo "  [LLM] Using codex (OpenAI)" >&2
        # Use codex exec with read-only sandbox
        tmpfile=$(mktemp)
        codex exec --skip-git-repo-check --sandbox read-only -c reasoning_effort=medium \
            -o "$tmpfile" - <<< "$PROMPT" >/dev/null 2>&1

        if [[ "$OUTPUT_FILE" == "-" ]]; then
            cat "$tmpfile"
            rm -f "$tmpfile"
        else
            mv "$tmpfile" "$OUTPUT_FILE"
        fi
        ;;

    claude)
        echo "  [LLM] Using claude (Anthropic)" >&2
        # Use claude CLI in print mode with streaming JSON
        # Unset API key to use Max plan instead of API credits
        unset ANTHROPIC_API_KEY
        # Suppress sounds for non-interactive sessions
        export CLAUDE_NO_SOUND=1

        tmpfile=$(mktemp)
        parsedfile=$(mktemp)

        # Call claude with prompt via stdin
        # Output is newline-delimited JSON, we need to extract the text content
        if ! echo "$PROMPT" | claude -p --verbose --output-format stream-json 2>/dev/null > "$tmpfile"; then
            echo "  [LLM] Warning: claude CLI returned non-zero exit code" >&2
        fi

        # Parse the streaming JSON to extract the result
        # Look for "result" type or concatenate "assistant" message contents
        python3 -c "
import json
import sys

result_text = ''
with open('$tmpfile') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            # Check for result type (final output)
            if data.get('type') == 'result':
                result_text = data.get('result', '')
                break
            # Collect assistant message content
            elif data.get('type') == 'assistant':
                msg = data.get('message', {})
                content = msg.get('content', [])
                if isinstance(content, str):
                    result_text += content
                elif isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get('type') == 'text':
                            result_text += block.get('text', '')
                        elif isinstance(block, str):
                            result_text += block
        except json.JSONDecodeError:
            continue

if not result_text.strip():
    sys.exit(1)
print(result_text)
" > "$parsedfile" || true

        # Check for empty/whitespace-only output (backend failure)
        if [[ ! -s "$parsedfile" ]] || ! grep -q '[^[:space:]]' "$parsedfile"; then
            echo "  [LLM] Error: claude produced empty output" >&2
            rm -f "$tmpfile" "$parsedfile" 2>/dev/null || true
            exit 1
        fi

        if [[ "$OUTPUT_FILE" == "-" ]]; then
            cat "$parsedfile"
        else
            mv "$parsedfile" "$OUTPUT_FILE"
        fi
        rm -f "$tmpfile" "$parsedfile" 2>/dev/null || true
        ;;

    *)
        echo "Error: Unknown LLM_BACKEND '$LLM_BACKEND'. Use 'codex' or 'claude'." >&2
        exit 1
        ;;
esac
