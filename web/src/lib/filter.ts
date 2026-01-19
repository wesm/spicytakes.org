import type { Post } from './types';

/**
 * Filters posts based on spiciness and year.
 * Posts with undefined or NaN spiciness are treated as "missing" data and are INCLUDED
 * (i.e., they are not filtered out based on minSpiciness).
 */
export function filterPosts(posts: Post[], minSpiciness: number, selectedYear: number | null): Post[] {
  return posts.filter(p => {
    // Spiciness check
    // If spiciness is missing (undefined/null) or invalid (NaN), we include it
    // Otherwise, it must meet the minimum spiciness
    const passSpiciness = p.spiciness == null || !Number.isFinite(p.spiciness) || p.spiciness >= minSpiciness;
    
    // Year check
    const passYear = selectedYear == null || p.year === selectedYear;

    return passSpiciness && passYear;
  });
}
