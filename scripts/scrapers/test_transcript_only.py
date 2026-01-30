#!/usr/bin/env python3
"""Tests for transcript_only scraper slug precedence logic."""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

from transcript_only import TranscriptOnlyScraper


class TestSlugPrecedence(unittest.TestCase):
    """Ensure frontmatter slug takes priority over filename stem."""

    def _make_scraper(self):
        with patch.object(TranscriptOnlyScraper, "__init__", lambda self, *a, **kw: None):
            scraper = TranscriptOnlyScraper.__new__(TranscriptOnlyScraper)
            scraper.blog_id = "test"
            return scraper

    def _parse(self, scraper, frontmatter_yaml: str, body: str, filename: str = "2024-01-15-my-talk.md"):
        with tempfile.TemporaryDirectory() as tmp:
            md_path = Path(tmp) / filename
            content = f"---\n{frontmatter_yaml}\n---\n{body}"
            md_path.write_text(content)
            with patch("transcript_only.get_blog_dir", return_value=Path(tmp)):
                return scraper.parse_transcript(md_path)

    def test_frontmatter_slug_preferred(self):
        scraper = self._make_scraper()
        result = self._parse(scraper, 'title: "My Talk"\nslug: custom-slug\ndate: 2024-01-15', "Hello world")
        self.assertEqual(result["slug"], "custom-slug")

    def test_missing_slug_falls_back_to_stem(self):
        scraper = self._make_scraper()
        result = self._parse(scraper, 'title: "My Talk"\ndate: 2024-01-15', "Hello world")
        self.assertEqual(result["slug"], "2024-01-15-my-talk")

    def test_empty_string_slug_falls_back_to_stem(self):
        scraper = self._make_scraper()
        result = self._parse(scraper, 'title: "My Talk"\nslug: ""\ndate: 2024-01-15', "Hello world")
        self.assertEqual(result["slug"], "2024-01-15-my-talk")


if __name__ == "__main__":
    unittest.main()
