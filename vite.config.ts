import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, searchForWorkspaceRoot } from 'vite';
import { execSync } from 'child_process';

// Get git hash - use Vercel env var if available, otherwise run git command
let gitHash = process.env.VERCEL_GIT_COMMIT_SHA?.slice(0, 7) || 'unknown';
if (gitHash === 'unknown') {
	try {
		gitHash = execSync('git rev-parse --short HEAD').toString().trim();
	} catch {
		// Not in a git repo (e.g., Vercel build without VERCEL_GIT_COMMIT_SHA)
	}
}

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
