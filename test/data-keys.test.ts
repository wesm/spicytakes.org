import { describe, it, expect } from 'vitest';
import { makeSpicinessKey } from '../src/lib/data';

/**
 * Tests for the spiciness lookup key format.
 * The key must avoid collisions when quotes or filenames contain delimiters.
 */
describe('spiciness lookup key format', () => {
  // Use the production function from data.ts
  const makeKey = makeSpicinessKey;

  it('avoids collisions that would occur with pipe delimiter', () => {
    // These would collide with `${quote}|${filename}` format:
    // "a|b" + "c" => "a|b|c"
    // "a" + "b|c" => "a|b|c"
    const key1 = makeKey('a|b', 'c');
    const key2 = makeKey('a', 'b|c');

    expect(key1).not.toBe(key2);
  });

  it('handles quotes with special characters', () => {
    const key1 = makeKey('He said "hello"', 'post.md');
    const key2 = makeKey('He said \\"hello\\"', 'post.md');

    expect(key1).not.toBe(key2);
  });

  it('generates consistent keys for same input', () => {
    const quote = 'Test quote with | pipe';
    const filename = '2024-01-01-test-post';

    const key1 = makeKey(quote, filename);
    const key2 = makeKey(quote, filename);

    expect(key1).toBe(key2);
  });
});
