/**
 * Shared blog data loading utilities.
 * Used by both +layout.server.ts (single-blog mode) and
 * the /feed route (cross-blog aggregation).
 */

export interface RawPost {
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

export interface PostIndexEntry {
  filename: string;
  title: string;
  subtitle?: string;
  url?: string;
  video_url?: string;
  content_type?: string;
  tags?: string[];
  slug?: string;
}

export interface SpicyQuote {
  quote: string;
  filename: string;
  spiciness: number;
}

// Glob imports — bundled at build time by Vite
export const llmQuotesModules = import.meta.glob<{
  posts: RawPost[];
}>('/blogs/*/data/llm_quotes.json', { eager: true });

export const spicyQuotesModules = import.meta.glob<{
  quotes: SpicyQuote[];
}>('/blogs/*/data/spicy_quotes.json', { eager: true });

export const postsIndexModules = import.meta.glob<{
  posts: PostIndexEntry[];
}>('/blogs/*/data/posts_index.json', { eager: true });

export function getBlogData<T>(
  modules: Record<string, T>,
  blogId: string,
  defaultValue: T
): T {
  for (const [path, module] of Object.entries(modules)) {
    if (path.includes(`/blogs/${blogId}/`)) {
      return module;
    }
  }
  return defaultValue;
}

export function parseDate(filename: string): string | null {
  const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (match) {
    return `${match[1]}-${match[2]}-${match[3]}T12:00:00Z`;
  }
  return null;
}

export function formatTitle(filename: string): string {
  const titlePart = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '');
  const acronyms = [
    'bi', 'sql', 'ai', 'yc', 'vc', 'llm', 'llms',
    'mds', 'obp', 'svb', 'tam', 'mvp',
  ];

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
