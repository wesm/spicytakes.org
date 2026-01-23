import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, searchForWorkspaceRoot } from 'vite';
import { execSync } from 'child_process';

const gitHash = execSync('git rev-parse --short HEAD').toString().trim();

export default defineConfig({
	plugins: [sveltekit()],
	define: {
		__GIT_HASH__: JSON.stringify(gitHash)
	},
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
