import { test, expect } from '@playwright/test';
import { BlogPage } from '../page-objects/blog.page';

test.describe('Blog Navigation', () => {
  let blog: BlogPage;

  test.beforeEach(async ({ page }) => {
    blog = new BlogPage(page);
    await blog.goto();
  });

  test('displays header with site branding and blog name', async () => {
    await expect(blog.siteTitle).toBeVisible();
    await expect(blog.blogName).toContainText('Benn Stancil');
  });

  test('shows Posts view by default', async () => {
    // Posts tab should be active (has white background)
    await expect(blog.postsTab).toHaveClass(/bg-white/);
    // Post cards should be visible
    await expect(blog.postCards.first()).toBeVisible();
  });

  test('switches to Quotes view', async () => {
    await blog.switchToView('quotes');
    await expect(blog.quotesTab).toHaveClass(/bg-white/);
    await expect(blog.quoteCards.first()).toBeVisible();
  });

  test('switches to Themes view', async () => {
    await blog.switchToView('themes');
    await expect(blog.themesTab).toHaveClass(/bg-white/);
    // Themes view shows theme headers
    await expect(blog.page.locator('h2, h3').first()).toBeVisible();
  });

  test('switches between all views', async () => {
    // Start with Posts
    await expect(blog.postCards.first()).toBeVisible();

    // Switch to Quotes
    await blog.switchToView('quotes');
    await expect(blog.quoteCards.first()).toBeVisible();

    // Switch to Themes
    await blog.switchToView('themes');

    // Switch back to Posts
    await blog.switchToView('posts');
    await expect(blog.postCards.first()).toBeVisible();
  });

  test('displays stats bar with post and quote counts', async () => {
    await expect(blog.postsCount).toBeVisible();
    await expect(blog.quotesCount).toBeVisible();

    const postsText = await blog.postsCount.textContent();
    const quotesText = await blog.quotesCount.textContent();

    expect(postsText).toMatch(/\d+ posts/);
    expect(quotesText).toMatch(/\d+ quotes/);
  });

  test('displays theme pills in header', async () => {
    const pillCount = await blog.themePills.count();
    expect(pillCount).toBeGreaterThan(0);
  });

  test('view controls are visible in Posts view', async () => {
    await expect(blog.sortSelect).toBeVisible();
    await expect(blog.yearSelect).toBeVisible();
    await expect(blog.spicySlider).toBeVisible();
  });

  test('view controls are visible in Quotes view', async () => {
    await blog.switchToView('quotes');
    await expect(blog.sortSelect).toBeVisible();
    await expect(blog.yearSelect).toBeVisible();
    await expect(blog.spicySlider).toBeVisible();
  });
});
