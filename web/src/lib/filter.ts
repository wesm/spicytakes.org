import type { Post, Quote } from './types';

/**
 * Filters posts based on spiciness and year.
 * Missing spiciness is treated as 0.
 */
export function filterPosts(posts: Post[], minSpiciness: number, selectedYear: number | null): Post[] {
  return posts.filter(p => {
    // Spiciness check
    const spiciness = p.spiciness ?? 0;
    const passSpiciness = spiciness >= minSpiciness;
    
    // Year check
    const passYear = selectedYear == null || p.year === selectedYear;

    return passSpiciness && passYear;
  });
}

/**
 * Filters quotes based on spiciness and year.
 * Missing spiciness is treated as 0.
 */
export function filterQuotes(quotes: Quote[], minSpiciness: number, selectedYear: number | null): Quote[] {
  return quotes.filter(q => {
    // Spiciness check
    const spiciness = q.spiciness ?? 0;
    const passSpiciness = spiciness >= minSpiciness;
    
    // Year check
    const passYear = selectedYear == null || q.year === selectedYear;

    return passSpiciness && passYear;
  });
}