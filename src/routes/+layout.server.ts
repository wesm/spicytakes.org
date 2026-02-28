import type { LayoutServerLoad } from './$types';
import {
  type RawPost,
  type SpicyQuote,
  type PostIndexEntry,
  readBlogJson,
  parseDate,
  formatTitle,
} from '$lib/server/blog-data';

const blogId = import.meta.env.VITE_BLOG_ID || 'benn';
const isLandingMode = blogId === 'landing';

export const load: LayoutServerLoad = async () => {
  if (isLandingMode) {
    return { blogData: null };
  }

  const [rawData, spicyData, postsIndex] = await Promise.all([
    readBlogJson<{ posts: RawPost[] }>(
      blogId, 'llm_quotes.json', { posts: [] }
    ),
    readBlogJson<{ quotes: SpicyQuote[] }>(
      blogId, 'spicy_quotes.json', { quotes: [] }
    ),
    readBlogJson<{ posts: PostIndexEntry[] }>(
      blogId, 'posts_index.json', { posts: [] }
    ),
  ]);

  // Build lookups from posts_index.json
  // Index by filename (with/without .md) and by slug for compatibility
  const titleLookup: Record<string, string> = {};
  const urlLookup: Record<string, string> = {};
  const videoUrlLookup: Record<string, string> = {};
  const contentTypeLookup: Record<string, string> = {};
  const tagsLookup: Record<string, string[]> = {};
  for (const p of postsIndex.posts || []) {
    if (p.filename) {
      const keys = [p.filename, p.filename.replace(/\.md$/, '')];
      if (p.title) for (const k of keys) titleLookup[k] = p.title;
      if (p.url) for (const k of keys) urlLookup[k] = p.url;
      if (p.video_url) for (const k of keys) videoUrlLookup[k] = p.video_url;
      if (p.content_type) for (const k of keys) contentTypeLookup[k] = p.content_type;
      if (p.tags) for (const k of keys) tagsLookup[k] = p.tags;
      // Also index by slug (for Substack blogs where posts_index uses slug)
      const slug = (p as any).slug;
      if (slug) {
        if (p.title) titleLookup[slug] = p.title;
        if (p.url) urlLookup[slug] = p.url;
      }
    }
  }

  // Build spiciness lookup
  const spicyLookup: Record<string, number> = {};
  for (const q of spicyData.quotes || []) {
    const key = JSON.stringify([q.quote, q.filename]);
    spicyLookup[key] = q.spiciness || 5;
  }

  // Process posts
  const posts = rawData.posts
    .filter(p => !p.error)
    .map(post => {
      const dateStr = parseDate(post.filename);
      const year = dateStr ? parseInt(dateStr.split('-')[0], 10) : null;
      // Use real title from posts_index.json, fall back to formatTitle if not found
      // Try filename first, then extract slug from filename (for Substack: 2021-02-02-slug -> slug)
      const slug = post.filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
      const title = titleLookup[post.filename] || titleLookup[slug] || formatTitle(post.filename);
      // Get source URL from posts_index.json if available (for blogs with multiple sources like Medium + Blogger)
      const source_url = urlLookup[post.filename] || urlLookup[slug];
      // Merge video_url, content_type, tags from posts_index (for transcript-based blogs)
      const video_url = videoUrlLookup[post.filename] || videoUrlLookup[slug];
      const content_type = contentTypeLookup[post.filename] || contentTypeLookup[slug];
      const post_tags = tagsLookup[post.filename] || tagsLookup[slug];
      return {
        ...post,
        dateStr,
        title,
        year,
        source_url,
        ...(video_url && { video_url }),
        ...(content_type && { content_type }),
        ...(post_tags && { post_tags }),
      };
    })
    // Sort: dated posts by date descending, undated posts at the end
    .sort((a, b) => {
      if (a.dateStr && b.dateStr) return b.dateStr.localeCompare(a.dateStr);
      if (a.dateStr && !b.dateStr) return -1;
      if (!a.dateStr && b.dateStr) return 1;
      return a.title.localeCompare(b.title); // Sort undated alphabetically
    });

  // Compute post-level and per-quote spiciness
  posts.forEach(post => {
    const scores = (post.money_quotes || []).map(quote => {
      const key = JSON.stringify([quote, post.filename]);
      return spicyLookup[key] ?? 5;
    });
    (post as any).quote_spiciness = scores;
    if (scores.length > 0) {
      const avg = scores.reduce((sum, s) => sum + s, 0) / scores.length;
      (post as any).spiciness = Math.round(avg * 10) / 10;
    }
  });

  // Build quotes array
  const quotes = posts.flatMap(post =>
    (post.money_quotes || []).map(quote => {
      const key = JSON.stringify([quote, post.filename]);
      return {
        quote,
        filename: post.filename,
        themes: post.themes || [],
        spiciness: spicyLookup[key] || 5,
        dateStr: post.dateStr,
        year: post.year
      };
    })
  ).sort((a, b) => {
    // Sort: dated quotes by date descending, undated quotes at the end
    if (a.dateStr && b.dateStr) return b.dateStr.localeCompare(a.dateStr);
    if (a.dateStr && !b.dateStr) return -1;
    if (!a.dateStr && b.dateStr) return 1;
    return 0;
  });

  // Extract years, keeping null (undated) separate
  const datedYears = [...new Set(posts.map(p => p.year).filter((y): y is number => y !== null))].sort((a, b) => b - a);
  const hasUndated = posts.some(p => p.year === null);
  // years array: dated years descending, then null at the end for "Undated"
  const years: (number | null)[] = hasUndated ? [...datedYears, null] : datedYears;
  const minYear = datedYears.length > 0 ? Math.min(...datedYears) : new Date().getFullYear();
  const maxYear = datedYears.length > 0 ? Math.max(...datedYears) : new Date().getFullYear();

  return {
    blogData: {
      posts,
      quotes,
      spicyLookup,
      years,
      stats: {
        totalPosts: posts.length,
        totalQuotes: quotes.length,
        yearRange: years.length === 0 ? '' : (minYear === maxYear ? `${minYear}` : `${minYear}-${maxYear}`),
        hasSpiciness: Object.keys(spicyLookup).length > 0
      }
    }
  };
};
