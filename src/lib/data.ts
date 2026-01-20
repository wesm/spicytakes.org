import type { Post, Quote, ThemeData } from './types';
import { THEME_LABELS, THEME_ICONS, blogId } from './config';

// Import all blog data statically (Vite requires this for production builds)
import bennQuotes from '../../blogs/benn/data/llm_quotes.json';
// Armin's data will be imported once generated
let arminQuotes: any = { posts: [] };
try {
  arminQuotes = await import('../../blogs/armin/data/llm_quotes.json').then(m => m.default || m);
} catch {
  // Armin's data not yet generated
}
// Wesm's data
let wesmQuotes: any = { posts: [] };
try {
  wesmQuotes = await import('../../blogs/wesm/data/llm_quotes.json').then(m => m.default || m);
} catch {
  // Wesm's data not yet generated
}

// Select data based on blogId
const allBlogData: Record<string, any> = {
  benn: bennQuotes,
  armin: arminQuotes,
  wesm: wesmQuotes,
};
const rawData = allBlogData[blogId] || allBlogData.benn;

// Import spicy quotes for selected blog
let spicyData: any = null;
try {
  if (blogId === 'benn') {
    const module = await import('../../blogs/benn/data/spicy_quotes.json');
    spicyData = module.default || module;
  } else if (blogId === 'armin') {
    const module = await import('../../blogs/armin/data/spicy_quotes.json');
    spicyData = module.default || module;
  } else if (blogId === 'wesm') {
    const module = await import('../../blogs/wesm/data/spicy_quotes.json');
    spicyData = module.default || module;
  }
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

/** Creates a collision-safe lookup key for quote + filename pairs */
export function makeSpicinessKey(quote: string, filename: string): string {
  return JSON.stringify([quote, filename]);
}

// Build spiciness lookup
const spicyLookup: Record<string, number> = {};
if (spicyData?.quotes) {
  for (const q of spicyData.quotes) {
    const key = makeSpicinessKey(q.quote, q.filename);
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
    const key = makeSpicinessKey(quote, post.filename);
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
          icon: THEME_ICONS[theme] || '',
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
const minYear = years.length > 0 ? Math.min(...years) : new Date().getFullYear();
const maxYear = years.length > 0 ? Math.max(...years) : new Date().getFullYear();
export const stats = {
  totalPosts: posts.length,
  totalQuotes: quotes.length,
  yearRange: years.length === 0 ? '' : (minYear === maxYear ? `${minYear}` : `${minYear}-${maxYear}`),
  hasSpiciness: Object.keys(spicyLookup).length > 0
};
