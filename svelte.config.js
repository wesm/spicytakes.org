import adapter from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const blogId = process.env.VITE_BLOG_ID || 'benn';
const isLanding = blogId === 'landing';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
			runtime: 'nodejs22.x',
			includeFiles: isLanding
				? ['blogs/feed_index.json']
				: [
						`blogs/${blogId}/posts/**/*.md`,
						`blogs/${blogId}/data/llm_quotes.json`,
						`blogs/${blogId}/data/spicy_quotes.json`,
						`blogs/${blogId}/data/posts_index.json`,
					]
		})
	}
};

export default config;
