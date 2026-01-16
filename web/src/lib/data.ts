import type { Post, Quote, ThemeData } from './types';
import { THEME_LABELS, THEME_ICONS } from './types';
import rawData from '../../data/llm_quotes.json';

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

// Build quotes array
export const quotes: Quote[] = posts.flatMap(post =>
  (post.money_quotes || []).map(quote => ({
    quote,
    post,
    themes: post.themes || []
  }))
);

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
      (post.money_quotes || []).forEach(q => {
        themeMap[theme].quotes.push({ quote: q, post, themes: post.themes || [] });
      });
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

export const years = Object.keys(postsByYear).map(Number).sort((a, b) => b - a);

// Stats
export const stats = {
  totalPosts: posts.length,
  totalQuotes: quotes.length,
  yearRange: `${Math.min(...years)}-${Math.max(...years)}`
};
