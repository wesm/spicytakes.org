import type { Post, Quote, ThemeData } from './types';
import { THEME_LABELS, THEME_ICONS } from './types';
import rawData from '../../data/llm_quotes.json';

// Try to load spicy quotes if available
let spicyData: any = null;
try {
  const module = await import('../../data/spicy_quotes.json');
  spicyData = module.default || module;
} catch {
  // Spicy quotes not yet generated
}

function parseDate(filename: string): Date {
  const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (match) {
    return new Date(parseInt(match[1]), parseInt(match[2]) - 1, parseInt(match[3]));
  }
  return new Date();
}

function formatTitle(filename: string): string {
  const titlePart = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '');
  return titlePart
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

// Build spiciness lookup
const spicyLookup: Record<string, number> = {};
if (spicyData?.quotes) {
  for (const q of spicyData.quotes) {
    const key = q.quote + q.filename;
    spicyLookup[key] = q.spiciness || 5;
  }
}

// Process posts
export const posts: Post[] = (rawData as any).posts
  .filter((p: any) => !p.error)
  .map((post: any) => ({
    ...post,
    date: parseDate(post.filename),
    title: formatTitle(post.filename),
    year: parseDate(post.filename).getFullYear()
  }))
  .sort((a: Post, b: Post) => (b.date?.getTime() || 0) - (a.date?.getTime() || 0));

// Build quotes array with spiciness
export const quotes: Quote[] = posts.flatMap(post =>
  (post.money_quotes || []).map(quote => {
    const key = quote + post.filename;
    const date = post.date;
    return {
      quote,
      post,
      themes: post.themes || [],
      spiciness: spicyLookup[key] || 5,
      date,
      year: date?.getFullYear()
    };
  })
).sort((a, b) => (b.date?.getTime() || 0) - (a.date?.getTime() || 0));

// Group quotes by filename for O(Q) lookup instead of O(P*Q)
const quotesByFilename: Record<string, Quote[]> = {};
quotes.forEach(q => {
  const filename = q.post.filename;
  if (!quotesByFilename[filename]) quotesByFilename[filename] = [];
  quotesByFilename[filename].push(q);
});

// Compute post-level spiciness (average of quote spiciness scores)
posts.forEach(post => {
  const postQuotes = quotesByFilename[post.filename] || [];
  const validScores = postQuotes
    .map(q => q.spiciness)
    .filter(s => typeof s === 'number' && Number.isFinite(s));
  if (validScores.length > 0) {
    const avg = validScores.reduce((sum, s) => sum + s, 0) / validScores.length;
    post.spiciness = Math.round(avg * 10) / 10;
  }
});

// Build themes data
export const themes: ThemeData[] = (() => {
  const themeMap: Record<string, ThemeData> = {};

  posts.forEach(post => {
    (post.themes || []).forEach(theme => {
      if (!themeMap[theme]) {
        themeMap[theme] = {
          name: theme,
          label: THEME_LABELS[theme] || theme,
          icon: THEME_ICONS[theme] || '📝',
          posts: [],
          quotes: []
        };
      }
      themeMap[theme].posts.push(post);
    });
  });

  // Add quotes to themes
  quotes.forEach(q => {
    q.themes.forEach(theme => {
      if (themeMap[theme]) {
        themeMap[theme].quotes.push(q);
      }
    });
  });

  return Object.values(themeMap).sort((a, b) => b.posts.length - a.posts.length);
})();

// Group posts by year
export const postsByYear: Record<number, Post[]> = posts.reduce((acc, post) => {
  const year = post.year || new Date().getFullYear();
  if (!acc[year]) acc[year] = [];
  acc[year].push(post);
  return acc;
}, {} as Record<number, Post[]>);

// Group quotes by year
export const quotesByYear: Record<number, Quote[]> = quotes.reduce((acc, quote) => {
  const year = quote.year || new Date().getFullYear();
  if (!acc[year]) acc[year] = [];
  acc[year].push(quote);
  return acc;
}, {} as Record<number, Quote[]>);

export const years = Object.keys(postsByYear).map(Number).sort((a, b) => b - a);

// Stats
export const stats = {
  totalPosts: posts.length,
  totalQuotes: quotes.length,
  yearRange: `${Math.min(...years)}-${Math.max(...years)}`,
  hasSpiciness: Object.keys(spicyLookup).length > 0
};
