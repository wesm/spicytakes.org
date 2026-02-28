/**
 * Shared blog data loading utilities.
 * Used by both +layout.server.ts (single-blog mode) and
 * the /feed route (cross-blog aggregation).
 *
 * Data is loaded via fs.readFile at request time (not bundled
 * by Vite), so each Vercel deployment only pays for the files
 * it actually needs.
 */

import { readFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

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

// Resolve project root: cwd in dev, relative to this file on Vercel.
const projectRoot = import.meta.env.DEV
  ? process.cwd()
  : join(
      dirname(fileURLToPath(import.meta.url)),
      '../../../../..'
    );

const jsonCache = new Map<string, unknown>();

export async function readBlogJson<T>(
  blogId: string,
  filename: string,
  defaultValue: T
): Promise<T> {
  const rel = `blogs/${blogId}/data/${filename}`;
  return readProjectJson(rel, defaultValue);
}

export async function readProjectJson<T>(
  relativePath: string,
  defaultValue: T
): Promise<T> {
  const cached = jsonCache.get(relativePath);
  if (cached !== undefined) return cached as T;

  const abs = join(projectRoot, relativePath);
  try {
    const raw = await readFile(abs, 'utf-8');
    const parsed = JSON.parse(raw) as T;
    jsonCache.set(relativePath, parsed);
    return parsed;
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code === 'ENOENT') {
      return defaultValue;
    }
    throw err;
  }
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
