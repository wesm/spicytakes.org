import adapter from '@sveltejs/adapter-vercel';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const blogId = process.env.VITE_BLOG_ID || 'benn';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
			runtime: 'nodejs22.x',
			includeFiles: [`blogs/${blogId}/posts/**/*.md`]
		})
	}
};

export default config;
