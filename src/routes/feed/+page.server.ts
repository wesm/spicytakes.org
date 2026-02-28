import type { PageServerLoad } from './$types';
import type { FeedPost } from '$lib/types';
import { readProjectJson } from '$lib/server/blog-data';

interface FeedIndex {
  posts: FeedPost[];
  authors: { id: string; name: string }[];
}

export const load: PageServerLoad = async () => {
  const feedIndex = await readProjectJson<FeedIndex>(
    'blogs/feed_index.json',
    { posts: [], authors: [] }
  );

  return {
    posts: feedIndex.posts,
    authors: feedIndex.authors,
  };
};
