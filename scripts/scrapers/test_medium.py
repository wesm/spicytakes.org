#!/usr/bin/env python3
"""Tests for Medium scraper date parsing."""

import unittest

from medium import parse_pub_date


class TestPubDateParsing(unittest.TestCase):
    def test_rfc2822(self):
        self.assertEqual(parse_pub_date("Sat, 18 Jan 2025 20:42:07 GMT"), "2025-01-18")

    def test_rfc2822_with_offset(self):
        self.assertEqual(parse_pub_date("Mon, 03 Feb 2025 12:00:00 +0000"), "2025-02-03")

    def test_iso8601(self):
        self.assertEqual(parse_pub_date("2025-01-18T20:42:07Z"), "2025-01-18")

    def test_iso8601_with_offset(self):
        self.assertEqual(parse_pub_date("2025-01-18T20:42:07+00:00"), "2025-01-18")

    def test_none_input(self):
        self.assertIsNone(parse_pub_date(None))

    def test_invalid_input(self):
        self.assertIsNone(parse_pub_date("not a date"))

    def test_empty_string(self):
        self.assertIsNone(parse_pub_date(""))


if __name__ == "__main__":
    unittest.main()
