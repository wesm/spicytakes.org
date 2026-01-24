import { defineConfig, devices } from '@playwright/test';

// Use dev servers for E2E testing to avoid build interference issues
// between landing and blog projects sharing the same output directory
export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI
    ? [['github'], ['html', { outputFolder: 'playwright-report', open: 'never' }]]
    : 'html',
  timeout: 60000,
  use: {
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'landing',
      use: { ...devices['Desktop Chrome'], baseURL: 'http://localhost:4173' },
      testMatch: /landing\.spec\.ts/,
    },
    {
      name: 'blog-benn',
      use: { ...devices['Desktop Chrome'], baseURL: 'http://localhost:4174' },
      testIgnore: /landing\.spec\.ts/,
    },
  ],
  webServer: [
    {
      command: 'VITE_BLOG_ID=landing npx vite dev --port 4173',
      port: 4173,
      reuseExistingServer: !process.env.CI,
      timeout: 120000,
    },
    {
      command: 'VITE_BLOG_ID=benn npx vite dev --port 4174',
      port: 4174,
      reuseExistingServer: !process.env.CI,
      timeout: 120000,
    },
  ],
});
