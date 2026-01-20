import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, searchForWorkspaceRoot } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	build: {
		// Target older browsers for iOS Safari compatibility
		target: ['es2020', 'safari13', 'chrome87', 'firefox78']
	},
	server: {
		fs: {
			allow: [searchForWorkspaceRoot(process.cwd()), 'blogs', 'config']
		}
	}
});
