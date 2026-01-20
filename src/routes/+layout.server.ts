import { readFileSync, existsSync } from 'fs';
import { join } from 'path';
import type { LayoutServerLoad } from './$types';

const blogId = process.env.VITE_BLOG_ID || 'benn';
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

interface SpicyQuote {
  quote: string;
  filename: string;
  spiciness: number;
}

function loadJson<T>(path: string, defaultValue: T): T {
  try {
    if (existsSync(path)) {
      return JSON.parse(readFileSync(path, 'utf-8'));
    }
  } catch (e) {
    console.error(`Failed to load ${path}:`, e);
  }
  return defaultValue;
}

function parseDate(filename: string): string {
  const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (match) {
    return `${match[1]}-${match[2]}-${match[3]}`;
  }
  return new Date().toISOString().split('T')[0];
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

  const dataDir = join(process.cwd(), 'blogs', blogId, 'data');

  const rawData = loadJson<{ posts: RawPost[] }>(
    join(dataDir, 'llm_quotes.json'),
    { posts: [] }
  );

  const spicyData = loadJson<{ quotes: SpicyQuote[] }>(
    join(dataDir, 'spicy_quotes.json'),
    { quotes: [] }
  );

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
      return {
        ...post,
        dateStr,
        title: formatTitle(post.filename),
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
