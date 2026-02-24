import { readFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { error } from '@sveltejs/kit';
import { config } from '$lib/config';
import { renderMarkdown } from '$lib/server/markdown';
import type { PageServerLoad } from './$types';

// Disable prerendering for post pages to avoid Vercel's 2048 route limit
// Posts will be rendered on-demand via SSR instead
export const prerender = false;

const blogId = import.meta.env.VITE_BLOG_ID || 'benn';

function isTranscript(post: { content_type?: string }): boolean {
  if (post.content_type === 'transcript') return true;
  return config?.scraper.type === 'transcript_only';
}

// Resolve the project root for reading post markdown files.
// In dev: process.cwd(). On Vercel: relative to this file.
const projectRoot = import.meta.env.DEV
  ? process.cwd()
  : join(dirname(fileURLToPath(import.meta.url)), '../../../../..');

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
    const mdPath = join(
      projectRoot, 'blogs', blogId, 'posts',
      `${params.filename}.md`
    );
    try {
      const raw = await readFile(mdPath, 'utf-8');
      transcriptHtml = renderMarkdown(raw);
    } catch (err) {
      if ((err as NodeJS.ErrnoException).code !== 'ENOENT') throw err;
    }
  }

  return { post, transcriptHtml };
};
