#!/usr/bin/env python3
"""Tests for base scraper save_index ordering and None pub_date handling."""

import json
import unittest
from unittest.mock import patch, MagicMock

from base import BaseScraper


class ConcreteScraper(BaseScraper):
    """Minimal concrete subclass for testing."""

    def scrape(self):
        return []


class TestSaveIndex(unittest.TestCase):
    @patch.object(BaseScraper, "__init__", lambda self, *a, **kw: None)
    def _make_scraper(self, tmp_dir):
        scraper = ConcreteScraper.__new__(ConcreteScraper)
        scraper.data_dir = tmp_dir
        return scraper

    def test_sort_with_none_pub_date(self):
        """Posts with None pub_date should not crash and should sort last."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            scraper = self._make_scraper(tmp_path)

            posts = [
                {"slug": "a", "pub_date": None},
                {"slug": "b", "pub_date": "2024-06-01"},
                {"slug": "c", "pub_date": "2025-01-15"},
                {"slug": "d"},  # missing key entirely
            ]
            scraper.save_index(posts)

            index_file = tmp_path / "posts_index.json"
            data = json.loads(index_file.read_text())

            slugs = [p["slug"] for p in data["posts"]]
            # Dated posts first (descending), then None/missing last
            self.assertEqual(slugs, ["c", "b", "a", "d"])

    def test_trailing_newline(self):
        """Output JSON should end with a trailing newline."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            scraper = self._make_scraper(tmp_path)
            scraper.save_index([{"slug": "x", "pub_date": "2024-01-01"}])

            raw = (tmp_path / "posts_index.json").read_text()
            self.assertTrue(raw.endswith("\n"))
            # Should not end with double newline
            self.assertFalse(raw.endswith("\n\n"))

    def test_last_updated_utc_z(self):
        """last_updated should end with 'Z' for UTC."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            scraper = self._make_scraper(tmp_path)
            scraper.save_index([])

            data = json.loads((tmp_path / "posts_index.json").read_text())
            self.assertTrue(data["last_updated"].endswith("Z"))


if __name__ == "__main__":
    unittest.main()
