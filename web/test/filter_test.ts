import { filterPosts } from '../src/lib/filter.js';
import type { Post } from '../src/lib/types';

function assert(condition: any, message: string) {
    if (!condition) {
        throw new Error(message);
    }
}

function runTests() {
  console.log('Running filterPosts tests...');

  const posts: Post[] = [
    { filename: '1', summary: 's1', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 5, year: 2021 },
    { filename: '2', summary: 's2', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 3, year: 2021 },
    { filename: '3', summary: 's3', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: 8, year: 2022 },
    { filename: '4', summary: 's4', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: undefined, year: 2022 },
    { filename: '5', summary: 's5', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: NaN, year: 2023 },
    { filename: '6', summary: 's6', money_quotes: [], themes: [], tone: '', key_insight: '', spiciness: null as any, year: 2023 }, // Force null for test
  ];

  // Test 1: Filter by minSpiciness
  const res1 = filterPosts(posts, 4, null);
  // Should include: 1 (5), 3 (8), 4 (undefined), 5 (NaN), 6 (null)
  // Should exclude: 2 (3)
  assert(res1.length === 5, 'Test 1 Failed: Length mismatch');
  assert(res1.find(p => p.filename === '1'), 'Test 1 Failed: Missing p1');
  assert(!res1.find(p => p.filename === '2'), 'Test 1 Failed: Included p2');
  assert(res1.find(p => p.filename === '4'), 'Test 1 Failed: Missing undefined spiciness');
  assert(res1.find(p => p.filename === '5'), 'Test 1 Failed: Missing NaN spiciness');
  assert(res1.find(p => p.filename === '6'), 'Test 1 Failed: Missing null spiciness');

  // Test 2: Filter by Year
  const res2 = filterPosts(posts, 1, 2021);
  // Should include: 1, 2
  assert(res2.length === 2, 'Test 2 Failed: Length mismatch');
  assert(res2.every(p => p.year === 2021), 'Test 2 Failed: Year mismatch');

  // Test 3: Filter by Both
  const res3 = filterPosts(posts, 4, 2021);
  // Should include: 1 (5)
  // Should exclude: 2 (3)
  assert(res3.length === 1, 'Test 3 Failed: Length mismatch');
  assert(res3[0].filename === '1', 'Test 3 Failed: Wrong post');

  console.log('All tests passed!');
}

runTests();