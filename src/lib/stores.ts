import { writable, derived } from 'svelte/store';
import type { Post, Quote } from './types';
import { posts, quotes } from './data';

// Active view
export const activeView = writable<'timeline' | 'quotes' | 'themes'>('timeline');

// Search query
export const searchQuery = writable('');

// Active theme filters
export const activeThemes = writable<Set<string>>(new Set());

// Filtered posts
export const filteredPosts = derived(
  [searchQuery, activeThemes],
  ([$searchQuery, $activeThemes]) => {
    return posts.filter(post => {
      // Theme filter
      if ($activeThemes.size > 0) {
        const postThemes = post.themes || [];
        if (!postThemes.some(t => $activeThemes.has(t))) {
          return false;
        }
      }

      // Search filter
      if ($searchQuery) {
        const query = $searchQuery.toLowerCase();
        const searchFields = [
          post.title,
          post.summary,
          post.key_insight,
          ...(post.money_quotes || [])
        ].filter(Boolean).join(' ').toLowerCase();

        if (!searchFields.includes(query)) {
          return false;
        }
      }

      return true;
    });
  }
);

// Filtered quotes
export const filteredQuotes = derived(
  [searchQuery, activeThemes],
  ([$searchQuery, $activeThemes]) => {
    return quotes.filter(item => {
      // Theme filter
      if ($activeThemes.size > 0) {
        if (!item.themes.some(t => $activeThemes.has(t))) {
          return false;
        }
      }

      // Search filter
      if ($searchQuery) {
        const query = $searchQuery.toLowerCase();
        if (!item.quote.toLowerCase().includes(query) &&
            !item.post.title?.toLowerCase().includes(query)) {
          return false;
        }
      }

      return true;
    });
  }
);

// Selected post for modal
export const selectedPost = writable<Post | null>(null);

// Helper to toggle theme
export function toggleTheme(theme: string) {
  activeThemes.update(themes => {
    const newThemes = new Set(themes);
    if (newThemes.has(theme)) {
      newThemes.delete(theme);
    } else {
      newThemes.add(theme);
    }
    return newThemes;
  });
}

// Helper to clear filters
export function clearFilters() {
  searchQuery.set('');
  activeThemes.set(new Set());
}
