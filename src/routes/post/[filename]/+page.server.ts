import type { PageServerLoad } from './$types';

// Disable prerendering for post pages to avoid Vercel's 2048 route limit
// Posts will be rendered on-demand via SSR instead
export const prerender = false;

export const load: PageServerLoad = async ({ params, parent }) => {
  const { blogData } = await parent();

  if (!blogData) {
    return { post: null };
  }

  const post = blogData.posts.find((p: { filename: string }) => p.filename === params.filename);

  return { post: post || null };
};
