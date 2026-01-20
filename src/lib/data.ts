import type { Post, Quote, ThemeData } from './types';
import { THEME_LABELS, THEME_ICONS } from './config';
import { postsStore, quotesStore, themesStore, statsStore, yearsStore } from './stores';

// Types for server data
interface ServerPost {
  filename: string;
  summary: string;
  money_quotes: string[];
  themes: string[];
  tone: string;
  key_insight: string;
  video_url?: string;
  content_type?: string;
  dateStr: string;
  title: string;
  year: number;
  spiciness?: number;
}

interface ServerQuote {
  quote: string;
  filename: string;
  themes: string[];
  spiciness: number;
  dateStr: string;
  year: number;
}

interface ServerBlogData {
  posts: ServerPost[];
  quotes: ServerQuote[];
  spicyLookup: Record<string, number>;
  years: number[];
  stats: {
    totalPosts: number;
    totalQuotes: number;
    yearRange: string;
    hasSpiciness: boolean;
  };
}

/** Creates a collision-safe lookup key for quote + filename pairs */
export function makeSpicinessKey(quote: string, filename: string): string {
  return JSON.stringify([quote, filename]);
}

// Initialize stores from server data
export function initializeData(blogData: ServerBlogData) {
  // Convert server posts to client Post type with Date objects
  const posts: Post[] = blogData.posts.map(p => ({
    ...p,
    date: new Date(p.dateStr),
  }));

  // Build a lookup map for posts by filename
  const postsByFilename: Record<string, Post> = {};
  posts.forEach(p => {
    postsByFilename[p.filename] = p;
  });

  // Convert server quotes to client Quote type
  const quotes: Quote[] = blogData.quotes.map(q => ({
    quote: q.quote,
    post: postsByFilename[q.filename],
    themes: q.themes,
    spiciness: q.spiciness,
    date: new Date(q.dateStr),
    year: q.year
  }));

  // Build themes
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
  quotes.forEach(q => {
    q.themes.forEach(theme => {
      if (themeMap[theme]) {
        themeMap[theme].quotes.push(q);
      }
    });
  });
  const themes = Object.values(themeMap).sort((a, b) => b.posts.length - a.posts.length);

  // Update stores
  postsStore.set(posts);
  quotesStore.set(quotes);
  themesStore.set(themes);
  statsStore.set(blogData.stats);
  yearsStore.set(blogData.years);
}

