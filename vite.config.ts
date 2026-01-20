import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, searchForWorkspaceRoot } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	build: {
		// Target older browsers for iOS Safari compatibility
		target: ['es2019', 'safari12']
	},
	server: {
		fs: {
			allow: [searchForWorkspaceRoot(process.cwd()), 'blogs', 'config']
		}
	}
});
