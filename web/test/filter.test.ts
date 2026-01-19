import { describe, it, expect } from 'vitest';
import { filterPosts, filterQuotes } from '../src/lib/filter';
import type { Post, Quote } from '../src/lib/types';

describe('filterPosts', () => {
  const posts: Post[] = [
    { filename: '1', summary: 's1', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 5, year: 2021 },
    { filename: '2', summary: 's2', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 3, year: 2021 },
    { filename: '3', summary: 's3', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 8, year: 2022 },
    { filename: '4', summary: 's4', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: undefined, year: 2022 },
    { filename: '5', summary: 's5', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: NaN, year: 2023 },
  ];

  it('filters by minSpiciness', () => {
    const res1 = filterPosts(posts, 4, null);
    // Should include: 1 (5), 3 (8)
    // Should exclude: 2 (3), 4 (undefined -> 1), 5 (NaN -> 1)
    expect(res1.length).toBe(2);
    expect(res1.find(p => p.filename === '1')).toBeDefined();
    expect(res1.find(p => p.filename === '3')).toBeDefined();
    expect(res1.find(p => p.filename === '2')).toBeUndefined();
    expect(res1.find(p => p.filename === '4')).toBeUndefined();
  });

  it('filters by Year', () => {
    const res2 = filterPosts(posts, 1, 2021);
    // Should include: 1, 2
    expect(res2.length).toBe(2);
    expect(res2.every(p => p.year === 2021)).toBe(true);
  });

  it('filters by Year and minSpiciness', () => {
    const res3 = filterPosts(posts, 4, 2021);
    // Should include: 1 (5, 2021)
    // Should exclude: 2 (3, 2021), 3 (8, 2022)
    expect(res3.length).toBe(1);
    expect(res3[0].filename).toBe('1');
  });
});

describe('filterQuotes', () => {
  const mockPost: Post = { filename: 'p1', summary: '', money_quotes: [], themes: [], tone: '', key_insight: '', year: 2021 };
  const quotes: Quote[] = [
    { quote: 'q1', post: mockPost, themes: [], spiciness: 5, year: 2021 },
    { quote: 'q2', post: mockPost, themes: [], spiciness: 2, year: 2021 },
    { quote: 'q3', post: mockPost, themes: [], spiciness: 8, year: 2022 },
    { quote: 'q4', post: mockPost, themes: [], spiciness: NaN, year: 2022 },
    { quote: 'q5', post: mockPost, themes: [], spiciness: undefined, year: 2022 },
  ];

  it('filters by minSpiciness (handles NaN/missing)', () => {
    const res = filterQuotes(quotes, 4, null);
    // Includes q1(5), q3(8)
    // Excludes q2(2), q4(NaN->1), q5(undefined->1)
    expect(res.length).toBe(2);
    expect(res.find(q => q.quote === 'q1')).toBeDefined();
    expect(res.find(q => q.quote === 'q3')).toBeDefined();
    expect(res.find(q => q.quote === 'q4')).toBeUndefined();
    expect(res.find(q => q.quote === 'q5')).toBeUndefined();
  });

  it('filters by Year', () => {
    const res = filterQuotes(quotes, 1, 2022);
    // q3 (8), q4 (NaN->1) and q5 (undefined->1) are all included because minSpiciness is 1
    expect(res.length).toBe(3);
    expect(res.find(q => q.quote === 'q3')).toBeDefined();
    expect(res.find(q => q.quote === 'q4')).toBeDefined();
    expect(res.find(q => q.quote === 'q5')).toBeDefined();
  });
});