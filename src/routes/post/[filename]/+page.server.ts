import { readFileSync, existsSync } from 'fs';
import { join } from 'path';
import type { EntryGenerator } from './$types';

const blogId = process.env.VITE_BLOG_ID || 'benn';
const isLandingMode = blogId === 'landing';

interface RawPost {
  filename: string;
  error?: boolean;
}

export const entries: EntryGenerator = async () => {
  if (isLandingMode) {
    return [];
  }

  const dataPath = join(process.cwd(), 'blogs', blogId, 'data', 'llm_quotes.json');

  if (!existsSync(dataPath)) {
    return [];
  }

  try {
    const data = JSON.parse(readFileSync(dataPath, 'utf-8')) as { posts: RawPost[] };
    return data.posts
      .filter(p => !p.error)
      .map(p => ({ filename: p.filename }));
  } catch (e) {
    console.error('Failed to load posts for prerender entries:', e);
    return [];
  }
};
