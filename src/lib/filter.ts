import type { Post, Quote } from './types';

/**
 * Filters posts based on spiciness and year.
 * Missing spiciness is treated as 1.
 * selectedYear can be: 'all' (no filter), a number (specific year), or null (undated posts only)
 */
export function filterPosts(posts: Post[], minSpiciness: number, selectedYear: number | null | 'all'): Post[] {
  return posts.filter(p => {
    // Spiciness check
    const rawSpiciness = p.spiciness;
    const spiciness = (typeof rawSpiciness === 'number' && Number.isFinite(rawSpiciness)) ? rawSpiciness : 1;
    const passSpiciness = spiciness >= minSpiciness;

    // Year check: 'all' = no filter, null = undated only, number = specific year
    const passYear = selectedYear === 'all' || p.year === selectedYear;

    return passSpiciness && passYear;
  });
}

/**
 * Filters quotes based on spiciness and year.
 * Missing spiciness is treated as 1.
 * selectedYear can be: 'all' (no filter), a number (specific year), or null (undated quotes only)
 */
export function filterQuotes(quotes: Quote[], minSpiciness: number, selectedYear: number | null | 'all'): Quote[] {
  return quotes.filter(q => {
    // Spiciness check
    const rawSpiciness = q.spiciness;
    const spiciness = (typeof rawSpiciness === 'number' && Number.isFinite(rawSpiciness)) ? rawSpiciness : 1;
    const passSpiciness = spiciness >= minSpiciness;

    // Year check: 'all' = no filter, null = undated only, number = specific year
    const passYear = selectedYear === 'all' || q.year === selectedYear;

    return passSpiciness && passYear;
  });
}
