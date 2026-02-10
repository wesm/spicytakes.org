#!/usr/bin/env python3
"""Tests for base scraper: save_index ordering, html_to_markdown conversion."""

import json
import unittest
from unittest.mock import patch

import sys
from pathlib import Path

_scraper_dir = str(Path(__file__).resolve().parent)
if _scraper_dir not in sys.path:
    sys.path.insert(0, _scraper_dir)
from base import BaseScraper

from bs4 import BeautifulSoup


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


class TestHtmlToMarkdown(unittest.TestCase):
    """Tests for html_to_markdown and related helper methods."""

    @patch.object(BaseScraper, "__init__", lambda self, *a, **kw: None)
    def _make_scraper(self):
        scraper = ConcreteScraper.__new__(ConcreteScraper)
        return scraper

    def _convert(self, html, base_url=""):
        scraper = self._make_scraper()
        soup = BeautifulSoup(html, "html.parser")
        return scraper.html_to_markdown(soup, base_url)

    def test_headings(self):
        md = self._convert("<h1>Title</h1><h2>Subtitle</h2><h3>Section</h3>")
        self.assertIn("# Title", md)
        self.assertIn("## Subtitle", md)
        self.assertIn("### Section", md)

    def test_paragraphs(self):
        md = self._convert("<p>First paragraph.</p><p>Second paragraph.</p>")
        self.assertIn("First paragraph.", md)
        self.assertIn("Second paragraph.", md)

    def test_blockquotes(self):
        md = self._convert("<blockquote>A wise saying.</blockquote>")
        self.assertIn("> A wise saying.", md)

    def test_unordered_list(self):
        md = self._convert("<ul><li>One</li><li>Two</li><li>Three</li></ul>")
        self.assertIn("- One", md)
        self.assertIn("- Two", md)
        self.assertIn("- Three", md)

    def test_ordered_list(self):
        md = self._convert("<ol><li>First</li><li>Second</li></ol>")
        self.assertIn("1. First", md)
        self.assertIn("2. Second", md)

    def test_nested_list(self):
        md = self._convert(
            "<ul><li>Parent<ul><li>Child</li></ul></li></ul>"
        )
        self.assertIn("- Parent", md)
        self.assertIn("Child", md)

    def test_inline_formatting(self):
        md = self._convert("<p>This is <strong>bold</strong> and <em>italic</em>.</p>")
        self.assertIn("**bold**", md)
        self.assertIn("*italic*", md)

    def test_links(self):
        md = self._convert('<p>Visit <a href="https://example.com">Example</a>.</p>')
        self.assertIn("[Example](https://example.com)", md)

    def test_relative_links(self):
        md = self._convert(
            '<p><a href="/about">About</a></p>',
            base_url="https://example.com"
        )
        self.assertIn("[About](https://example.com/about)", md)

    def test_code_inline(self):
        md = self._convert("<p>Use <code>print()</code> here.</p>")
        self.assertIn("`print()`", md)

    def test_code_block(self):
        md = self._convert("<pre>def hello():\n    pass</pre>")
        self.assertIn("```", md)
        self.assertIn("def hello():", md)

    def test_skip_tags_top_level(self):
        md = self._convert(
            "<p>Visible.</p><script>alert('xss')</script><style>.x{}</style>"
        )
        self.assertIn("Visible.", md)
        self.assertNotIn("alert", md)
        self.assertNotIn(".x{}", md)

    def test_skip_tags_nested_in_inline(self):
        """Skip tags nested inside inline elements should not leak content."""
        md = self._convert(
            "<p>Before <span><script>evil()</script></span> after.</p>"
        )
        self.assertNotIn("evil", md)
        self.assertIn("Before", md)
        self.assertIn("after.", md)

    def test_skip_tags_nested_in_paragraph(self):
        """Skip tags directly inside paragraphs should be excluded."""
        md = self._convert(
            "<p>Text <nav>navigation stuff</nav> more text.</p>"
        )
        self.assertNotIn("navigation stuff", md)
        self.assertIn("Text", md)
        self.assertIn("more text.", md)

    def test_exclude_tags_in_list(self):
        """Nested lists in <li> should not duplicate content."""
        html = "<ul><li>Parent item<ul><li>Nested item</li></ul></li></ul>"
        md = self._convert(html)
        # "Parent item" should appear once (from _get_direct_text excluding ul)
        # "Nested item" should appear once (from nested list rendering)
        self.assertEqual(md.count("Parent item"), 1)
        self.assertEqual(md.count("Nested item"), 1)

    def test_image(self):
        md = self._convert('<img src="pic.jpg" alt="A photo">')
        self.assertIn("![A photo](pic.jpg)", md)

    def test_figure_with_caption(self):
        md = self._convert(
            '<figure><img src="fig.png" alt="Figure"><figcaption>Caption text</figcaption></figure>'
        )
        self.assertIn("![Figure](fig.png)", md)
        self.assertIn("*Caption text*", md)

    def test_table(self):
        md = self._convert(
            "<table><tr><th>Name</th><th>Value</th></tr>"
            "<tr><td>A</td><td>1</td></tr></table>"
        )
        self.assertIn("| Name | Value |", md)
        self.assertIn("| A | 1 |", md)

    def test_hr(self):
        md = self._convert("<p>Above</p><hr><p>Below</p>")
        self.assertIn("---", md)

    def test_container_div(self):
        md = self._convert("<div><p>Inside a div.</p></div>")
        self.assertIn("Inside a div.", md)

    def test_tag_handlers_immutable(self):
        """_TAG_HANDLERS should be immutable (MappingProxyType)."""
        from types import MappingProxyType
        self.assertIsInstance(BaseScraper._TAG_HANDLERS, MappingProxyType)

    def test_skip_tags_is_frozenset(self):
        """_SKIP_TAGS should be a frozenset."""
        self.assertIsInstance(BaseScraper._SKIP_TAGS, frozenset)


if __name__ == "__main__":
    unittest.main()
