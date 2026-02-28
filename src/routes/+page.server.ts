import type { PageServerLoad } from './$types';
import { readProjectJson } from '$lib/server/blog-data';

const isLandingMode = (import.meta.env.VITE_BLOG_ID || 'benn') === 'landing';

interface FeedIndex {
  blogSpiciness: Record<string, number | null>;
}

export const load: PageServerLoad = async () => {
  if (!isLandingMode) {
    return { blogSpiciness: {} };
  }

  const feedIndex = await readProjectJson<FeedIndex>(
    'blogs/feed_index.json',
    { blogSpiciness: {} }
  );

  return { blogSpiciness: feedIndex.blogSpiciness };
};
