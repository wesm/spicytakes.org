#!/usr/bin/env python3
"""
Daring Fireball scraper for Spicy Takes platform.
Scrapes John Gruber's original articles from the archive page.
"""

import os
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

from base import BaseScraper

REQUEST_DELAY = 1.0

MONTHS = {
    "jan": "01", "feb": "02", "mar": "03", "apr": "04",
    "may": "05", "jun": "06", "jul": "07", "aug": "08",
    "sep": "09", "oct": "10", "nov": "11", "dec": "12",
}


class DaringFireballScraper(BaseScraper):
    """Scraper for daringfireball.net articles."""

    def __init__(self, blog_id: str):
        super().__init__(blog_id)

        if self.config["scraper"]["type"] != "daringfireball":
            raise ValueError(
                f"Blog {blog_id} is not configured as "
                "daringfireball type"
            )

        self.base_url = self.config["scraper"]["baseUrl"].rstrip("/")
        self.archive_url = self.config["scraper"]["archiveUrl"]

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36"
            )
        }

    def fetch_page(self, url: str) -> BeautifulSoup | None:
        """Fetch a page and return parsed BeautifulSoup."""
        try:
            response = requests.get(
                url, timeout=30, headers=self.headers
            )
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def parse_archive_date(self, text: str) -> str | None:
        """Parse 'DD Mon YYYY' date to YYYY-MM-DD."""
        text = text.replace("\xa0", " ").strip()
        match = re.match(r"(\d{1,2})\s+(\w{3})\s+(\d{4})", text)
        if not match:
            return None
        day, month_abbr, year = match.groups()
        month = MONTHS.get(month_abbr.lower())
        if not month:
            return None
        return f"{year}-{month}-{int(day):02d}"

    def get_post_urls(self, soup: BeautifulSoup) -> list[dict]:
        """
        Parse all post entries from the archive page.
        Returns list of {url, slug, date, title, year, month}.
        """
        main = soup.find("div", id="Main")
        if not main:
            print("  No #Main div found on archive page")
            return []

        posts = []
        seen_slugs = set()

        for p_tag in main.find_all("p"):
            a_tag = p_tag.find("a")
            small_tag = p_tag.find("small")
            if not a_tag or not small_tag:
                continue

            href = a_tag.get("href", "")
            title = a_tag.get_text(strip=True)
            date_text = small_tag.get_text(strip=True)

            match = re.match(
                r"https://daringfireball\.net/"
                r"(\d{4})/(\d{2})/([\w-]+)",
                href,
            )
            if not match:
                continue

            year, month, slug = match.groups()
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)

            date_str = self.parse_archive_date(date_text)

            posts.append({
                "url": href,
                "slug": slug,
                "date": date_str,
                "title": title,
                "year": year,
                "month": month,
            })

        return posts

    def fetch_post(self, post_info: dict) -> dict | None:
        """Fetch and parse a single blog post."""
        url = post_info["url"]
        soup = self.fetch_page(url)
        if not soup:
            return None

        article = soup.find("div", class_="article")
        if not article:
            print(f"  No div.article found: {url}")
            return None

        # Check for 404 pages (they also use div.article)
        h1 = article.find("h1")
        if h1 and h1.get_text(strip=True) == "404":
            print(f"  404 page: {url}")
            return None

        # Remove title and dateline before converting content
        for tag in article.find_all("h1"):
            tag.decompose()
        for tag in article.find_all("h6", class_="dateline"):
            tag.decompose()

        content = self.html_to_markdown(article, self.base_url)
        word_count = len(content.split())

        if word_count < 50:
            print(
                f"  Skipping (only {word_count} words): "
                f"{post_info['title']}"
            )
            return None

        return {
            "url": url,
            "slug": post_info["slug"],
            "title": post_info["title"],
            "date": post_info["date"],
            "content": content,
            "word_count": word_count,
        }

    def make_post_content(self, post: dict) -> str:
        """Create markdown file content with YAML frontmatter."""
        escaped_title = post["title"].replace('"', "'")
        frontmatter = [
            "---",
            f'title: "{escaped_title}"',
            f"date: {post['date']}",
            f"url: {post['url']}",
            f"slug: {post['slug']}",
            f"word_count: {post['word_count']}",
            "---",
            "",
        ]
        return "\n".join(frontmatter) + "\n" + post["content"]

    def scrape(self) -> list[dict]:
        """Scrape all blog posts."""
        print(f"Fetching archive from {self.archive_url}...")
        soup = self.fetch_page(self.archive_url)
        if not soup:
            print("Failed to fetch archive page")
            return []

        post_infos = self.get_post_urls(soup)
        print(f"Found {len(post_infos)} posts in archive")

        existing_slugs = self.get_existing_slugs()
        to_scrape = [
            p for p in post_infos
            if p["slug"] not in existing_slugs
        ]

        if not to_scrape:
            print("All posts already scraped!")
            existing = self.load_existing_index()
            return existing.get("posts", [])

        print(f"Scraping {len(to_scrape)} new posts...")

        existing = self.load_existing_index()
        posts = existing.get("posts", [])

        for i, info in enumerate(to_scrape):
            title_preview = info["title"][:60]
            print(f"[{i+1}/{len(to_scrape)}] {title_preview}...")

            post = self.fetch_post(info)
            if post:
                filename = f"{post['date']}-{post['slug']}.md"

                post["filename"] = filename
                post["content"] = self.make_post_content(post)
                filepath = self.save_post(post)
                print(f"  Saved: {filepath}")

                index_entry = {
                    k: v for k, v in post.items()
                    if k != "content"
                }
                posts.append(index_entry)

                if (i + 1) % 25 == 0:
                    self.save_index(posts)
                    print(f"  Index saved ({len(posts)} posts)")

            time.sleep(REQUEST_DELAY)

        self.save_index(posts)
        return posts


def main():
    """Main entry point."""
    blog_id = os.environ.get("BLOG_ID")
    if not blog_id:
        print("Error: BLOG_ID environment variable required")
        print(
            "Usage: BLOG_ID=daringfireball "
            "python daringfireball.py"
        )
        sys.exit(1)

    scraper = DaringFireballScraper(blog_id)
    scraper.run()


if __name__ == "__main__":
    main()
