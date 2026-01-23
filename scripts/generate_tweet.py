#!/usr/bin/env python3
"""
Generate tweet content and screenshot for a blog post.

Usage:
    BLOG_ID=benn python scripts/generate_tweet.py <post_filename>

Example:
    BLOG_ID=benn python scripts/generate_tweet.py 2026-01-16-why-cowork-cant-work

Output:
    - Tweet text (summary + permalink)
    - Screenshot saved to blogs/<blog_id>/data/tweets/<filename>.png
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

# Optional: try to import playwright, give helpful error if missing
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Error: playwright not installed. Run: pip install playwright && playwright install chromium")
    sys.exit(1)


def get_project_dir() -> Path:
    return Path(__file__).parent.parent


def load_config(blog_id: str) -> dict:
    config_path = get_project_dir() / "config" / f"{blog_id}.json"
    with open(config_path) as f:
        return json.load(f)


def load_post_analysis(blog_id: str, filename: str) -> dict | None:
    """Load the LLM analysis for a post."""
    # Try individual analysis file first
    analysis_file = get_project_dir() / "blogs" / blog_id / "data" / "llm_analysis" / f"{filename}.json"
    if analysis_file.exists():
        with open(analysis_file) as f:
            return json.load(f)

    # Fall back to combined llm_quotes.json
    quotes_file = get_project_dir() / "blogs" / blog_id / "data" / "llm_quotes.json"
    if quotes_file.exists():
        with open(quotes_file) as f:
            data = json.load(f)
            for post in data.get("posts", []):
                if post.get("filename") == filename:
                    return post

    return None


def load_post_metadata(blog_id: str, filename: str) -> dict | None:
    """Load post metadata from posts_index.json."""
    index_file = get_project_dir() / "blogs" / blog_id / "data" / "posts_index.json"
    if index_file.exists():
        with open(index_file) as f:
            data = json.load(f)
            for post in data.get("posts", []):
                if post.get("filename") == f"{filename}.md":
                    return post
    return None


def get_site_url(blog_id: str) -> str:
    """Get the production URL for a blog."""
    # Map blog IDs to their production URLs
    url_map = {
        "benn": "https://benn.spicytakes.org",
        "armin": "https://armin.spicytakes.org",
        "wesm": "https://wesm.spicytakes.org",
    }
    return url_map.get(blog_id, f"https://{blog_id}.spicytakes.org")


def generate_tweet_text(analysis: dict, metadata: dict | None, blog_id: str, filename: str) -> str:
    """Generate tweet text from post analysis."""
    config = load_config(blog_id)
    author_name = config.get("name", blog_id)

    # Get the title from metadata or analysis
    title = ""
    if metadata:
        title = metadata.get("title", "")

    # Use key_insight as the tweet hook - it's already a one-sentence takeaway
    # Fall back to first sentence of summary if no key_insight
    hook = analysis.get("key_insight", "")
    if not hook:
        summary = analysis.get("summary", "")
        hook = summary.split(". ")[0] + "." if summary else ""

    # Build permalink
    site_url = get_site_url(blog_id)
    permalink = f"{site_url}/post/{filename}"

    # Compose tweet
    # Format: Hook + newline + permalink
    # Keep under 280 chars (Twitter limit), accounting for image attachment
    tweet = f"{hook}\n\n{permalink}"

    return tweet


def capture_screenshot(blog_id: str, filename: str, output_path: Path, use_local: bool = False) -> bool:
    """Capture screenshot of post content using Playwright."""
    if use_local:
        # Start local dev server
        url = f"http://localhost:5173/post/{filename}"
        server_proc = subprocess.Popen(
            ["npm", "run", "dev"],
            cwd=get_project_dir(),
            env={**os.environ, "VITE_BLOG_ID": blog_id},
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(5)  # Wait for server to start
    else:
        site_url = get_site_url(blog_id)
        url = f"{site_url}/post/{filename}"
        server_proc = None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()

            # Use a wider viewport for nicer screenshots
            page = browser.new_page(viewport={"width": 1200, "height": 800})

            page.goto(url, wait_until="networkidle")

            # SvelteKit apps need extra time to hydrate and load data
            # Wait for the article to appear (it's rendered client-side)
            page.wait_for_selector("article", timeout=15000, state="visible")

            # Extra wait for any animations/transitions to settle
            page.wait_for_timeout(500)

            # Hide the sticky header and back link for a cleaner screenshot
            page.evaluate("""
                // Hide sticky header
                const header = document.querySelector('header');
                if (header) header.style.display = 'none';
                // Hide back link
                const backLink = document.querySelector('a[href="/"]');
                if (backLink && backLink.textContent.includes('Back')) {
                    backLink.style.display = 'none';
                }
            """)

            # Get the article element and screenshot just that
            article = page.locator("article")

            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Take screenshot of just the article
            article.screenshot(path=str(output_path))

            browser.close()
            print(f"Screenshot saved: {output_path}")
            return True

    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return False
    finally:
        if server_proc:
            server_proc.terminate()
            server_proc.wait()


def main():
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print("Usage: BLOG_ID=benn python scripts/generate_tweet.py <post_filename>")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Error: Post filename required")
        print("Usage: BLOG_ID=benn python scripts/generate_tweet.py <post_filename>")
        sys.exit(1)

    filename = sys.argv[1]
    # Remove .md extension if provided
    if filename.endswith(".md"):
        filename = filename[:-3]

    # Check for --local flag
    use_local = "--local" in sys.argv

    print(f"Generating tweet for: {blog_id}/{filename}")
    print("=" * 50)

    # Load post analysis
    analysis = load_post_analysis(blog_id, filename)
    if not analysis:
        print(f"Error: No analysis found for {filename}")
        print("Run llm_analyze.sh first to analyze the post")
        sys.exit(1)

    # Load post metadata
    metadata = load_post_metadata(blog_id, filename)

    # Generate tweet text
    tweet_text = generate_tweet_text(analysis, metadata, blog_id, filename)

    print("\n📝 Tweet text:")
    print("-" * 40)
    print(tweet_text)
    print("-" * 40)
    print(f"Length: {len(tweet_text)} chars")

    # Capture screenshot
    tweets_dir = get_project_dir() / "blogs" / blog_id / "data" / "tweets"
    screenshot_path = tweets_dir / f"{filename}.png"

    print(f"\n📸 Capturing screenshot{'(local dev server)' if use_local else ''}...")
    success = capture_screenshot(blog_id, filename, screenshot_path, use_local=use_local)

    if success:
        print(f"\n✅ Tweet ready!")
        print(f"   Text: {len(tweet_text)} chars")
        print(f"   Image: {screenshot_path}")

        # Output JSON for programmatic use
        output = {
            "tweet_text": tweet_text,
            "screenshot_path": str(screenshot_path),
            "permalink": f"{get_site_url(blog_id)}/post/{filename}",
            "filename": filename,
            "blog_id": blog_id
        }

        # Save output JSON
        output_file = tweets_dir / f"{filename}.json"
        with open(output_file, "w") as f:
            json.dump(output, f, indent=2)
        print(f"   Metadata: {output_file}")
    else:
        print("\n❌ Screenshot capture failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
