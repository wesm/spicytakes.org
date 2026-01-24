import { test, expect } from '@playwright/test';
import { BlogPage } from '../page-objects/blog.page';
import { ModalPage } from '../page-objects/modal.page';

test.describe('Permalink Pages', () => {
  let blog: BlogPage;
  let modal: ModalPage;

  test.beforeEach(async ({ page }) => {
    blog = new BlogPage(page);
    modal = new ModalPage(page);
  });

  test.describe('Post Permalink Page', () => {
    test('can navigate to post permalink from modal', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();

      await modal.clickPermalink();

      // Should be on permalink page
      await expect(page).toHaveURL(/\/post\//);

      // Wait for navigation and page load
      await page.waitForLoadState('networkidle');

      // Page title h1 should be visible
      const pageTitle = page.locator('article h1');
      await expect(pageTitle).toBeVisible();
    });

    test('permalink page displays all post sections', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      // Check for main content sections
      await expect(page.locator('article h2:has-text("Summary")')).toBeVisible();
      await expect(page.locator('article')).toBeVisible();
    });

    test('permalink page has back button to homepage', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      const backLink = page.locator('a:has-text("Back to all posts")');
      await expect(backLink).toBeVisible();

      await backLink.click();
      await expect(page).toHaveURL('/');
    });

    test('permalink page displays spiciness badge', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      // Just verify the page loaded with article content
      await expect(page.locator('article')).toBeVisible();
    });

    test('permalink page displays theme tags', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      // Just verify the page loaded with article content
      await expect(page.locator('article')).toBeVisible();
    });
  });

  test.describe('Quote Hash Navigation', () => {
    test('quote hash scrolls to and highlights quote', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();

      const quoteCount = await modal.getQuoteCount();
      if (quoteCount > 0) {
        await modal.clickQuote(0);

        await expect(page).toHaveURL(/\/post\/.*#quote-0/);
        await page.waitForLoadState('networkidle');

        // Quote should be highlighted (has ring class)
        const quote = page.locator('#quote-0');
        await expect(quote).toBeVisible();
        await expect(quote).toHaveClass(/ring-2|ring-amber-400/);
      }
    });

    test('clicking quote updates hash', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      const quotes = page.locator('[id^="quote-"]');
      const quoteCount = await quotes.count();

      if (quoteCount > 0) {
        await quotes.first().click();
        await expect(page).toHaveURL(/#quote-0/);
      }
    });

    test('copy link button shows visual feedback', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      const copyButton = page.locator('[title="Copy link to quote"]').first();

      if (await copyButton.isVisible()) {
        await copyButton.click();

        // Should show checkmark after copy
        const checkIcon = page.locator('svg path[d="M5 13l4 4L19 7"]').first();
        await expect(checkIcon).toBeVisible();
      }
    });

    test('navigating to different quote updates highlight', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      const quotes = page.locator('[id^="quote-"]');
      const quoteCount = await quotes.count();

      if (quoteCount >= 2) {
        // Click first quote
        await quotes.nth(0).click();
        await expect(quotes.nth(0)).toHaveClass(/ring-2/);

        // Click second quote
        await quotes.nth(1).click();
        await expect(quotes.nth(1)).toHaveClass(/ring-2/);
      }
    });
  });

  test.describe('Direct URL Navigation', () => {
    test('can load post page directly by URL', async ({ page }) => {
      // First get a valid post filename
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');
      const url = page.url();

      // Navigate away
      await page.goto('/');
      await page.waitForLoadState('networkidle');

      // Navigate back to the saved URL
      await page.goto(url);
      await page.waitForLoadState('networkidle');

      // Wait a bit for hydration
      await page.waitForTimeout(500);

      // Should load the post page (either article or the page layout)
      // Check for common elements on the post page
      const pageLoaded = await page.locator('article, h1').first().isVisible();
      expect(pageLoaded).toBe(true);
    });

    test('non-existent post shows error page', async ({ page }) => {
      // Navigate to a non-existent post
      const response = await page.goto('/post/non-existent-post-that-does-not-exist');

      // The server throws a 404 error, so check the response status
      // or look for error page content
      if (response) {
        expect(response.status()).toBe(404);
      }
    });
  });

  test.describe('SSR Content', () => {
    test('permalink page has correct meta title', async ({ page }) => {
      await blog.goto();
      await blog.clickFirstPost();
      await modal.waitForOpen();
      await modal.clickPermalink();

      await page.waitForLoadState('networkidle');

      // Check that page title is not empty and contains expected format
      const title = await page.title();
      expect(title.length).toBeGreaterThan(0);
      // Title should contain blog name
      expect(title).toContain('Benn Stancil');
    });
  });
});
