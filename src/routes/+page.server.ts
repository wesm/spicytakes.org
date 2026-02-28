import type { PageServerLoad } from './$types';
import { landing } from '$lib/config';
import {
  spicyQuotesModules,
  getBlogData,
} from '$lib/server/blog-data';

const isLandingMode = (import.meta.env.VITE_BLOG_ID || 'benn') === 'landing';

export const load: PageServerLoad = async () => {
  if (!isLandingMode) {
    return { blogSpiciness: {} };
  }

  const blogs = landing.blogs.filter(b => !b.hidden);
  const blogSpiciness: Record<string, number | null> = {};

  for (const blog of blogs) {
    const spicyData = getBlogData(
      spicyQuotesModules, blog.id, { quotes: [] }
    );
    const quotes = spicyData.quotes || [];
    if (quotes.length === 0) {
      blogSpiciness[blog.id] = null;
      continue;
    }
    const sum = quotes.reduce((s, q) => s + (q.spiciness || 5), 0);
    blogSpiciness[blog.id] = Math.round((sum / quotes.length) * 10) / 10;
  }

  return { blogSpiciness };
};
