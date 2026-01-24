import { test, expect } from '@playwright/test';
import { LandingPage } from '../page-objects/landing.page';

test.describe('Landing Page', () => {
  let landing: LandingPage;

  test.beforeEach(async ({ page }) => {
    landing = new LandingPage(page);
    await landing.goto();
  });

  test('displays hero section with title and tagline', async ({ page }) => {
    // The landing page should have "Spicy Takes" in the hero
    await expect(page.locator('h1:has-text("Spicy Takes")')).toBeVisible();
    // And a tagline paragraph
    await expect(page.locator('header p.text-xl')).toBeVisible();
  });

  test('displays multiple blog cards', async ({ page }) => {
    // Blog cards are in the section with grid layout
    const blogCards = page.locator('section.max-w-5xl a[href^="https://"]');
    const count = await blogCards.count();
    expect(count).toBeGreaterThan(0);
  });

  test('blog cards show name, description, and stats', async ({ page }) => {
    // Check that at least one card has expected elements
    const firstCard = page.locator('section.max-w-5xl a[href^="https://"]').first();
    await expect(firstCard).toBeVisible();

    // Card should have a name in h2
    await expect(firstCard.locator('h2')).toBeVisible();

    // Card should have description text
    await expect(firstCard.locator('p.text-stone-600')).toBeVisible();

    // Card should show posts count
    await expect(firstCard.locator('text=/\\d+ posts/')).toBeVisible();
  });

  test('blog cards link to subdomains', async ({ page }) => {
    const firstCard = page.locator('section.max-w-5xl a[href^="https://"]').first();
    const href = await firstCard.getAttribute('href');
    expect(href).toMatch(/^https:\/\/.+\.spicytakes\.org$/);
  });

  test('displays "How it works" section', async ({ page }) => {
    await expect(page.locator('h2:has-text("How it works")')).toBeVisible();
    await expect(page.locator('h3:has-text("Archive")')).toBeVisible();
    await expect(page.locator('h3:has-text("Analyze")')).toBeVisible();
    await expect(page.locator('h3:has-text("Rate")')).toBeVisible();
  });

  test('displays footer with attribution', async ({ page }) => {
    // Landing page has its own footer with attribution
    await expect(page.locator('footer').filter({ hasText: 'Wes McKinney' })).toBeVisible();
  });
});
