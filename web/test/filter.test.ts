import { describe, it, expect } from 'vitest';
import { filterPosts } from '../src/lib/filter.js';
import type { Post } from '../src/lib/types';

describe('filterPosts', () => {
  const posts: Post[] = [
    { filename: '1', summary: 's1', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 5, year: 2021 },
    { filename: '2', summary: 's2', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 3, year: 2021 },
    { filename: '3', summary: 's3', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 8, year: 2022 },
    { filename: '4', summary: 's4', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: undefined, year: 2022 },
    { filename: '5', summary: 's5', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: NaN, year: 2023 },
    { filename: '6', summary: 's6', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: null as any, year: 2023 }, // Force null for test
  ];

  it('filters by minSpiciness', () => {
    const res1 = filterPosts(posts, 4, null);
    // Should include: 1 (5), 3 (8), 4 (undefined), 5 (NaN), 6 (null)
    // Should exclude: 2 (3)
    expect(res1.length).toBe(5);
    expect(res1.find(p => p.filename === '1')).toBeDefined();
    expect(res1.find(p => p.filename === '2')).toBeUndefined();
    expect(res1.find(p => p.filename === '4')).toBeDefined();
    expect(res1.find(p => p.filename === '5')).toBeDefined();
    expect(res1.find(p => p.filename === '6')).toBeDefined();
  });

  it('filters by Year', () => {
    const res2 = filterPosts(posts, 1, 2021);
    // Should include: 1, 2
    expect(res2.length).toBe(2);
    expect(res2.every(p => p.year === 2021)).toBe(true);
  });

  it('filters by Both', () => {
    const res3 = filterPosts(posts, 4, 2021);
    // Should include: 1 (5)
    // Should exclude: 2 (3)
    expect(res3.length).toBe(1);
    expect(res3[0].filename).toBe('1');
  });
});
