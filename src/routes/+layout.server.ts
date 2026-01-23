import type { LayoutServerLoad } from './$types';

const blogId = import.meta.env.VITE_BLOG_ID || 'benn';
const isLandingMode = blogId === 'landing';

interface RawPost {
  filename: string;
  summary: string;
  money_quotes: string[];
  themes: string[];
  tone: string;
  key_insight: string;
  video_url?: string;
  content_type?: string;
  error?: boolean;
}

interface PostIndexEntry {
  filename: string;
  title: string;
  subtitle?: string;
}

interface SpicyQuote {
  quote: string;
  filename: string;
  spiciness: number;
}

// Import all blog data files at build time using Vite's glob import
// This bundles the data into the serverless function
const llmQuotesModules = import.meta.glob<{ posts: RawPost[] }>('/blogs/*/data/llm_quotes.json', { eager: true });
const spicyQuotesModules = import.meta.glob<{ quotes: SpicyQuote[] }>('/blogs/*/data/spicy_quotes.json', { eager: true });
const postsIndexModules = import.meta.glob<{ posts: PostIndexEntry[] }>('/blogs/*/data/posts_index.json', { eager: true });

function getBlogData<T>(modules: Record<string, T>, blogId: string, defaultValue: T): T {
  const key = `/blogs/${blogId}/data/${Object.keys(modules)[0]?.split('/').pop()}`;
  for (const [path, module] of Object.entries(modules)) {
    if (path.includes(`/blogs/${blogId}/`)) {
      return module;
    }
  }
  return defaultValue;
}

function parseDate(filename: string): string {
  const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (match) {
    // Use noon UTC to avoid timezone issues (midnight UTC shows as previous day in US timezones)
    return `${match[1]}-${match[2]}-${match[3]}T12:00:00Z`;
  }
  return new Date().toISOString().split('T')[0] + 'T12:00:00Z';
}

function formatTitle(filename: string): string {
  const titlePart = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '');
  const acronyms = ['bi', 'sql', 'ai', 'yc', 'vc', 'llm', 'llms', 'mds', 'obp', 'svb', 'tam', 'mvp'];

  return titlePart
    .split('-')
    .map(word => {
      const lowerWord = word.toLowerCase();
      if (acronyms.includes(lowerWord)) return lowerWord.toUpperCase();
      if (lowerWord === 'dbt') return 'dbt';
      return word.charAt(0).toUpperCase() + word.slice(1);
    })
    .join(' ');
}

export const load: LayoutServerLoad = async () => {
  if (isLandingMode) {
    return { blogData: null };
  }

  const rawData = getBlogData(llmQuotesModules, blogId, { posts: [] });
  const spicyData = getBlogData(spicyQuotesModules, blogId, { quotes: [] });
  const postsIndex = getBlogData(postsIndexModules, blogId, { posts: [] });

  // Build title lookup from posts_index.json
  // Index by filename (with/without .md) and by slug for compatibility
  const titleLookup: Record<string, string> = {};
  for (const p of postsIndex.posts || []) {
    if (p.title) {
      if (p.filename) {
        titleLookup[p.filename] = p.title;
        titleLookup[p.filename.replace(/\.md$/, '')] = p.title;
      }
      // Also index by slug (for Substack blogs where posts_index uses slug)
      const slug = (p as any).slug;
      if (slug) {
        titleLookup[slug] = p.title;
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
      const year = parseInt(dateStr.split('-')[0], 10);
      // Use real title from posts_index.json, fall back to formatTitle if not found
      // Try filename first, then extract slug from filename (for Substack: 2021-02-02-slug -> slug)
      const slug = post.filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
      const title = titleLookup[post.filename] || titleLookup[slug] || formatTitle(post.filename);
      return {
        ...post,
        dateStr,
        title,
        year
      };
    })
    .sort((a, b) => b.dateStr.localeCompare(a.dateStr));

  // Compute post-level spiciness
  posts.forEach(post => {
    const postQuotes = (post.money_quotes || []).map(quote => {
      const key = JSON.stringify([quote, post.filename]);
      return spicyLookup[key] || 5;
    });
    if (postQuotes.length > 0) {
      const avg = postQuotes.reduce((sum, s) => sum + s, 0) / postQuotes.length;
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
  ).sort((a, b) => b.dateStr.localeCompare(a.dateStr));

  const years = [...new Set(posts.map(p => p.year))].sort((a, b) => b - a);
  const minYear = years.length > 0 ? Math.min(...years) : new Date().getFullYear();
  const maxYear = years.length > 0 ? Math.max(...years) : new Date().getFullYear();

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
