import { test, expect } from '@playwright/test';
import { BlogPage } from '../page-objects/blog.page';
import { ModalPage } from '../page-objects/modal.page';

test.describe('Modal', () => {
  let blog: BlogPage;
  let modal: ModalPage;

  test.beforeEach(async ({ page }) => {
    blog = new BlogPage(page);
    modal = new ModalPage(page);
    await blog.goto();
  });

  test.describe('Opening Modal', () => {
    test('opens modal when clicking a post card', async () => {
      await blog.clickFirstPost();
      await modal.waitForOpen();
      expect(await modal.isVisible()).toBe(true);
    });

    test('opens modal when clicking a quote in Quotes view', async () => {
      await blog.switchToView('quotes');
      await blog.clickFirstQuote();
      await modal.waitForOpen();
      expect(await modal.isVisible()).toBe(true);
    });
  });

  test.describe('Modal Content', () => {
    test.beforeEach(async () => {
      await blog.clickFirstPost();
      await modal.waitForOpen();
    });

    test('displays post title', async () => {
      const title = await modal.getTitle();
      expect(title.length).toBeGreaterThan(0);
    });

    test('displays date', async () => {
      await expect(modal.date).toBeVisible();
    });

    test('displays spiciness badge when available', async ({ page }) => {
      // Most posts should have spiciness
      if (await modal.spicinessBadge.isVisible()) {
        const spiciness = await modal.getSpiciness();
        expect(spiciness).toBeGreaterThanOrEqual(1);
        expect(spiciness).toBeLessThanOrEqual(10);
      }
    });

    test('displays summary section', async () => {
      await expect(modal.summary).toBeVisible();
      const summaryText = await modal.summary.textContent();
      expect(summaryText?.length).toBeGreaterThan(0);
    });

    test('displays spicy quotes when available', async () => {
      const quoteCount = await modal.getQuoteCount();
      // Most posts should have quotes
      if (quoteCount > 0) {
        await expect(modal.spicyQuotes.first()).toBeVisible();
      }
    });

    test('displays source link', async () => {
      await expect(modal.sourceLink).toBeVisible();
      const href = await modal.sourceLink.getAttribute('href');
      expect(href).toMatch(/^https?:\/\//);
    });

    test('displays permalink button', async () => {
      await expect(modal.permalinkButton).toBeVisible();
    });

    test('displays theme tags when available', async () => {
      const tagCount = await modal.themeTags.count();
      // Most posts should have themes
      if (tagCount > 0) {
        await expect(modal.themeTags.first()).toBeVisible();
      }
    });
  });

  test.describe('Closing Modal', () => {
    test.beforeEach(async () => {
      await blog.clickFirstPost();
      await modal.waitForOpen();
    });

    test('closes with X button', async () => {
      await modal.close();
      expect(await modal.isVisible()).toBe(false);
    });

    test('closes with Escape key', async () => {
      await modal.closeByEscape();
      expect(await modal.isVisible()).toBe(false);
    });

    test('closes by clicking backdrop', async () => {
      await modal.closeByBackdrop();
      expect(await modal.isVisible()).toBe(false);
    });
  });

  test.describe('Modal Navigation', () => {
    test('permalink button navigates to post page', async ({ page }) => {
      await blog.clickFirstPost();
      await modal.waitForOpen();

      await modal.clickPermalink();

      // Should navigate away from modal to post page
      await expect(page).toHaveURL(/\/post\//);
      await modal.waitForClose();
    });

    test('clicking quote navigates to post page with hash', async ({ page }) => {
      await blog.clickFirstPost();
      await modal.waitForOpen();

      const quoteCount = await modal.getQuoteCount();
      if (quoteCount > 0) {
        await modal.clickQuote(0);

        await expect(page).toHaveURL(/\/post\/.*#quote-0/);
      }
    });
  });

  test.describe('Modal State', () => {
    test('opening different post updates modal content', async () => {
      // Open first post
      await blog.clickFirstPost();
      await modal.waitForOpen();
      const firstTitle = await modal.getTitle();

      // Close and open second post
      await modal.close();

      // Click second post
      const secondPost = blog.postCards.nth(1);
      await secondPost.click();
      await modal.waitForOpen();
      const secondTitle = await modal.getTitle();

      // Titles should be different
      expect(firstTitle).not.toBe(secondTitle);
    });
  });
});
