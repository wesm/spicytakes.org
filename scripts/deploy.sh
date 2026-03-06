#!/bin/bash
# Deploy spicytakes blogs to Vercel
#
# Usage:
#   ./scripts/deploy.sh <blog_id> [--prod]   # Deploy one blog
#   ./scripts/deploy.sh --all [--prod]       # Deploy all blogs
#   ./scripts/deploy.sh --changed [--prod]   # Deploy only changed blogs
#   ./scripts/deploy.sh --list               # List available blogs
#
# Examples:
#   ./scripts/deploy.sh landing --prod
#   ./scripts/deploy.sh geohot --prod
#   ./scripts/deploy.sh --all --prod

set -e

# Map blog ID to Vercel project name
get_project_name() {
    case "$1" in
        landing)   echo "spicytakes.org" ;;
        benn)      echo "spicy-takes-benn" ;;
        armin)     echo "spicy-takes-mitsuhiko" ;;
        wesm)      echo "spicy-takes-wesm" ;;
        danluu)    echo "spicy-takes-danluu" ;;
        bcantrill) echo "spicy-takes-bcantrill" ;;
        jessfraz)  echo "spicy-takes-jessfraz" ;;
        geohot)    echo "spicy-takes-geohot" ;;
        mrocklin)  echo "spicy-takes-mrocklin" ;;
        criccomini) echo "spicy-takes-criccomini" ;;
        skamille) echo "spicy-takes-skamille" ;;
        mitchellh) echo "spicy-takes-mitchellh" ;;
        mathbabe) echo "spicy-takes-mathbabe" ;;
        nayafia) echo "spicy-takes-nayafia" ;;
        joereis) echo "spicy-takes-joereis" ;;
        ssp) echo "spicy-takes-ssp" ;;
        paulg) echo "spicy-takes-paulg" ;;
        atwood) echo "spicy-takes-atwood" ;;
        unclebob) echo "spicy-takes-unclebob" ;;
        hillel) echo "spicy-takes-hillel" ;;
        steveyegge) echo "spicy-takes-steveyegge" ;;
        martinfowler) echo "spicy-takes-martinfowler" ;;
        hannes) echo "spicy-takes-hannes" ;;
        mempko) echo "spicy-takes-mempko" ;;
        spolsky) echo "spicy-takes-spolsky" ;;
        dhh) echo "spicy-takes-dhh" ;;
        fperez) echo "spicy-takes-fperez" ;;
        charity) echo "spicy-takes-charity" ;;
        devault) echo "spicy-takes-devault" ;;
        cmuratori) echo "spicy-takes-cmuratori" ;;
        zedshaw) echo "spicy-takes-zedshaw" ;;
        jvns) echo "spicy-takes-jvns" ;;
        daringfireball) echo "spicy-takes-daringfireball" ;;
        patio11) echo "spicy-takes-patio11" ;;
        *)         echo "" ;;
    esac
}

ALL_BLOGS="landing benn armin wesm danluu bcantrill jessfraz geohot mrocklin criccomini skamille mitchellh mathbabe nayafia joereis ssp paulg atwood unclebob hillel steveyegge martinfowler hannes mempko spolsky dhh fperez charity devault cmuratori zedshaw jvns daringfireball patio11"

PROD_FLAG=""
DEPLOY_ALL=false
DEPLOY_CHANGED=false
LIST_ONLY=false
BLOG_ID=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --prod)
            PROD_FLAG="--prod"
            shift
            ;;
        --all)
            DEPLOY_ALL=true
            shift
            ;;
        --changed)
            DEPLOY_CHANGED=true
            shift
            ;;
        --list)
            LIST_ONLY=true
            shift
            ;;
        -h|--help)
            echo "Deploy spicytakes blogs to Vercel"
            echo ""
            echo "Usage:"
            echo "  ./scripts/deploy.sh <blog_id> [--prod]   Deploy one blog"
            echo "  ./scripts/deploy.sh --all [--prod]       Deploy all blogs"
            echo "  ./scripts/deploy.sh --changed [--prod]   Deploy only changed blogs"
            echo "  ./scripts/deploy.sh --list               List available blogs"
            echo ""
            echo "Options:"
            echo "  --prod      Deploy to production (default is preview)"
            echo "  --changed   Deploy only blogs with real content changes"
            echo ""
            exit 0
            ;;
        *)
            BLOG_ID="$1"
            shift
            ;;
    esac
done

# List blogs
if [ "$LIST_ONLY" = true ]; then
    echo "Available blogs:"
    for blog in $ALL_BLOGS; do
        echo "  $blog -> $(get_project_name $blog)"
    done
    exit 0
fi

# Check for Vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "Error: Vercel CLI not installed"
    echo "Install with: npm i -g vercel"
    echo "Then run: vercel login"
    exit 1
fi

write_vercelignore() {
    local blog_id="$1"
    cat > .vercelignore <<'STATIC'
# Large directories not needed for build
.git
node_modules
.svelte-kit

# Per-post LLM analysis (combined data is in llm_quotes.json)
blogs/*/data/llm_analysis/

# Audio/video files
blogs/*/transcripts/audio/
blogs/**/*.mp3
blogs/**/*.mp4
blogs/**/*.wav
blogs/**/*.m4a

# Development/docs
*.log
.DS_Store

# Playwright
playwright-report/
test-results/

# Exclude all blog posts (only current blog's posts are needed)
blogs/*/posts/
blogs/*/transcripts/
STATIC

    # Re-include the current blog's posts and transcripts
    if [ "$blog_id" != "landing" ]; then
        echo "" >> .vercelignore
        echo "# Re-include current blog" >> .vercelignore
        echo "!blogs/${blog_id}/posts/" >> .vercelignore
        echo "!blogs/${blog_id}/transcripts/" >> .vercelignore
    fi
}

deploy_blog() {
    local blog_id="$1"
    local project_name
    project_name=$(get_project_name "$blog_id")

    if [ -z "$project_name" ]; then
        echo "Error: Unknown blog ID '$blog_id'"
        echo "Run ./scripts/deploy.sh --list to see available blogs"
        return 1
    fi

    echo "========================================"
    echo "Deploying: $blog_id"
    echo "Project:   $project_name"
    echo "Mode:      ${PROD_FLAG:-preview}"
    echo "========================================"

    # Generate .vercelignore excluding other blogs' posts
    write_vercelignore "$blog_id"

    # Link to the correct Vercel project
    echo "Linking to project..."
    vercel link --yes --project="$project_name" \
        ${VERCEL_TOKEN:+--token="$VERCEL_TOKEN"}

    # Deploy (builds on Vercel servers using VITE_BLOG_ID from project env vars)
    vercel ${PROD_FLAG:+"$PROD_FLAG"} --yes \
        ${VERCEL_TOKEN:+--token="$VERCEL_TOKEN"}

    echo "Done: $blog_id"
    echo ""
}

# Deploy only changed blogs (excludes posts_index.json timestamp noise)
if [ "$DEPLOY_CHANGED" = true ]; then
    CHANGED=$(git diff --name-only -- . ':!**/posts_index.json' \
        | grep '^blogs/' | cut -d/ -f2 | sort -u || true)

    if git diff --name-only -- config/ | grep -q .; then
        CHANGED="landing${CHANGED:+ $CHANGED}"
    fi

    if [ -z "$CHANGED" ]; then
        echo "No blogs changed — skipping deployment"
        exit 0
    fi

    echo "Deploying changed blogs: $CHANGED"
    for blog in $CHANGED; do
        deploy_blog "$blog" || echo "Warning: Failed to deploy $blog"
    done
    echo "Done deploying changed blogs!"
    exit 0
fi

# Deploy all or single blog
if [ "$DEPLOY_ALL" = true ]; then
    echo "Deploying ALL blogs..."
    echo ""
    for blog in $ALL_BLOGS; do
        deploy_blog "$blog" || echo "Warning: Failed to deploy $blog"
    done
    echo "Done deploying all blogs!"
else
    if [ -z "$BLOG_ID" ]; then
        echo "Error: No blog specified"
        echo ""
        echo "Usage: ./scripts/deploy.sh <blog_id> [--prod]"
        echo "       ./scripts/deploy.sh --all [--prod]"
        echo ""
        echo "Run ./scripts/deploy.sh --list to see available blogs"
        exit 1
    fi
    deploy_blog "$BLOG_ID"
fi
