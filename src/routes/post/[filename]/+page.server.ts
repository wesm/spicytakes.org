import { error } from '@sveltejs/kit';
import { config } from '$lib/config';
import { renderMarkdown } from '$lib/server/markdown';
import type { PageServerLoad } from './$types';

// Disable prerendering for post pages to avoid Vercel's 2048 route limit
// Posts will be rendered on-demand via SSR instead
export const prerender = false;

const blogId = import.meta.env.VITE_BLOG_ID || 'benn';

// Lazy glob for loading raw markdown post content.
// Excludes filenames containing '#' which break Rollup's resolver.
const markdownFiles = import.meta.glob<string>(
  ['/blogs/*/posts/*.md', '!/blogs/*/posts/*#*.md'],
  { query: '?raw', import: 'default' }
);

function isTranscript(post: { content_type?: string }): boolean {
  if (post.content_type === 'transcript') return true;
  return config?.scraper.type === 'transcript_only';
}

export const load: PageServerLoad = async ({ params, parent }) => {
  const { blogData } = await parent();

  if (!blogData) {
    throw error(404, 'Blog not found');
  }

  const post = blogData.posts.find(
    (p: { filename: string }) => p.filename === params.filename
  );

  if (!post) {
    throw error(404, 'Post not found');
  }

  let transcriptHtml: string | null = null;

  if (isTranscript(post)) {
    const mdPath = `/blogs/${blogId}/posts/${params.filename}.md`;
    const loader = markdownFiles[mdPath];
    if (loader) {
      const raw = await loader();
      transcriptHtml = renderMarkdown(raw);
    }
  }

  return { post, transcriptHtml };
};
