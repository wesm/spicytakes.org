import type { Post, Quote } from './types';

/**
 * Filters posts based on spiciness and year.
 * Missing spiciness is treated as 1.
 */
export function filterPosts(posts: Post[], minSpiciness: number, selectedYear: number | null): Post[] {
  return posts.filter(p => {
    // Spiciness check
    const rawSpiciness = p.spiciness;
    const spiciness = (typeof rawSpiciness === 'number' && Number.isFinite(rawSpiciness)) ? rawSpiciness : 1;
    const passSpiciness = spiciness >= minSpiciness;
    
    // Year check
    const passYear = selectedYear == null || p.year === selectedYear;

    return passSpiciness && passYear;
  });
}

/**
 * Filters quotes based on spiciness and year.
 * Missing spiciness is treated as 1.
 */
export function filterQuotes(quotes: Quote[], minSpiciness: number, selectedYear: number | null): Quote[] {
  return quotes.filter(q => {
    // Spiciness check
    const rawSpiciness = q.spiciness;
    const spiciness = (typeof rawSpiciness === 'number' && Number.isFinite(rawSpiciness)) ? rawSpiciness : 1;
    const passSpiciness = spiciness >= minSpiciness;
    
    // Year check
    const passYear = selectedYear == null || q.year === selectedYear;

    return passSpiciness && passYear;
  });
}
