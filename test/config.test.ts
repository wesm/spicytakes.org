import { describe, it, expect } from 'vitest';
import { buildSourceUrl } from '../src/lib/config';
import type { BlogConfig } from '../src/lib/types';

// Helper to create minimal config for testing
function makeConfig(overrides: Partial<BlogConfig>): BlogConfig {
  return {
    id: 'test',
    name: 'Test Blog',
    tagline: 'Test',
    description: 'Test',
    sourceUrl: 'https://example.com',
    sourceLabel: 'example.com',
    scraper: { type: 'substack' },
    themes: {},
    llmAnalysis: { contextPrompt: '', depthLevel: '', summaryLength: '' },
    spiciness: { contextPrompt: '' },
    ...overrides,
  };
}

describe('buildSourceUrl', () => {
  describe('jekyll_feed with sourcePostPath', () => {
    it('uses custom sourcePostPath template', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://blog.cleancoder.com',
        scraper: {
          type: 'jekyll_feed',
          sourcePostPath: '/uncle-bob/{year}/{month}/{day}/{slug}.html',
        },
      });
      const result = buildSourceUrl('2023-05-15-clean-code.md', cfg);
      expect(result).toBe('https://blog.cleancoder.com/uncle-bob/2023/05/15/clean-code.html');
    });

    it('uses default sourcePostPath when not specified', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://example.com',
        scraper: { type: 'jekyll_feed' },
      });
      const result = buildSourceUrl('2023-05-15-my-post.md', cfg);
      expect(result).toBe('https://example.com/blog/jekyll/update/2023/05/15/my-post.html');
    });

    it('handles filename without .md extension', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://blog.cleancoder.com',
        scraper: {
          type: 'jekyll_feed',
          sourcePostPath: '/uncle-bob/{year}/{month}/{day}/{slug}.html',
        },
      });
      const result = buildSourceUrl('2023-05-15-clean-code', cfg);
      expect(result).toBe('https://blog.cleancoder.com/uncle-bob/2023/05/15/clean-code.html');
    });
  });

  describe('rss_generic with sourcePostPath', () => {
    it('uses custom sourcePostPath template', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://example.com',
        scraper: {
          type: 'rss_generic',
          sourcePostPath: '/articles/{slug}/',
        },
      });
      const result = buildSourceUrl('2023-05-15-my-article.md', cfg);
      expect(result).toBe('https://example.com/articles/my-article/');
    });

    it('uses default sourcePostPath when not specified', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://example.com',
        scraper: { type: 'rss_generic' },
      });
      const result = buildSourceUrl('2023-05-15-my-post.md', cfg);
      expect(result).toBe('https://example.com/blog/my-post/');
    });
  });

  describe('transcript handling', () => {
    it('returns video_url for transcripts', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://example.com',
        scraper: { type: 'substack' },
      });
      const result = buildSourceUrl('2023-05-15-transcript.md', cfg, {
        content_type: 'transcript',
        video_url: 'https://youtube.com/watch?v=abc123',
      });
      expect(result).toBe('https://youtube.com/watch?v=abc123');
    });

    it('returns empty string for transcripts without video_url', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://example.com',
        scraper: { type: 'substack' },
      });
      const result = buildSourceUrl('2023-05-15-transcript.md', cfg, {
        content_type: 'transcript',
      });
      expect(result).toBe('');
    });
  });

  describe('substack', () => {
    it('constructs URL with /p/ path', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://benn.substack.com',
        scraper: { type: 'substack' },
      });
      const result = buildSourceUrl('2023-05-15-my-post.md', cfg);
      expect(result).toBe('https://benn.substack.com/p/my-post');
    });
  });

  describe('github_markdown', () => {
    it('constructs URL with date path (no leading zeros)', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://lucumr.pocoo.org',
        scraper: { type: 'github_markdown' },
      });
      const result = buildSourceUrl('2023-05-03-my-post.md', cfg);
      expect(result).toBe('https://lucumr.pocoo.org/2023/5/3/my-post/');
    });
  });

  describe('paulgraham', () => {
    it('constructs URL with .html extension', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://paulgraham.com',
        scraper: { type: 'paulgraham' },
      });
      const result = buildSourceUrl('2023-05-15-my-essay.md', cfg);
      expect(result).toBe('https://paulgraham.com/my-essay.html');
    });
  });

  describe('blogger', () => {
    it('constructs URL with /YYYY/MM/slug.html pattern', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://steve-yegge.blogspot.com',
        scraper: { type: 'blogger' },
      });
      const result = buildSourceUrl('2018-01-23-why-i-left-google.md', cfg);
      expect(result).toBe('https://steve-yegge.blogspot.com/2018/01/why-i-left-google.html');
    });

    it('handles filename without .md extension', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://steve-yegge.blogspot.com',
        scraper: { type: 'blogger' },
      });
      const result = buildSourceUrl('2006-03-30-execution-in-kingdom-of-nouns', cfg);
      expect(result).toBe('https://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html');
    });
  });

  describe('source_url override', () => {
    it('uses source_url from post when available', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://steve-yegge.blogspot.com',
        scraper: { type: 'blogger' },
      });
      const result = buildSourceUrl('2025-10-15-beads-post.md', cfg, {
        source_url: 'https://steve-yegge.medium.com/beads-post-abc123',
      });
      expect(result).toBe('https://steve-yegge.medium.com/beads-post-abc123');
    });

    it('falls back to constructed URL when source_url not provided', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://steve-yegge.blogspot.com',
        scraper: { type: 'blogger' },
      });
      const result = buildSourceUrl('2018-01-23-my-post.md', cfg, {});
      expect(result).toBe('https://steve-yegge.blogspot.com/2018/01/my-post.html');
    });

    it('transcript video_url takes precedence over source_url', () => {
      const cfg = makeConfig({
        sourceUrl: 'https://example.com',
        scraper: { type: 'blogger' },
      });
      const result = buildSourceUrl('2023-05-15-talk-transcript.md', cfg, {
        content_type: 'transcript',
        video_url: 'https://youtube.com/watch?v=abc123',
        source_url: 'https://example.com/should-not-use-this',
      });
      expect(result).toBe('https://youtube.com/watch?v=abc123');
    });
  });
});
