#!/bin/bash
set -euo pipefail

# Build analytics parquet file for the landing site.
# Runs as an npm prebuild hook — skips silently for non-landing builds.

if [ "${VITE_BLOG_ID:-}" != "landing" ]; then
    exit 0
fi

echo "Building analytics parquet file..."
uv run --with duckdb --with pyarrow scripts/build_analytics_parquet.py
