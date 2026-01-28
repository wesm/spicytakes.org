import { test, expect } from '@playwright/test';
import { AnalyticsPage } from '../page-objects/analytics.page';
import { LandingPage } from '../page-objects/landing.page';

test.describe('Analytics Page', () => {
  let analytics: AnalyticsPage;

  test.beforeEach(async ({ page }) => {
    analytics = new AnalyticsPage(page);
  });

  test('loads and displays data', async ({ page }) => {
    await analytics.goto();

    // Should show loading state initially
    await expect(analytics.heroTitle).toBeVisible();

    // Wait for data to load
    await analytics.waitForDataLoad();

    // Should show leaderboard header
    await expect(page.locator('h2:has-text("Leaderboard")')).toBeVisible();

    // Should show quotes table header
    await expect(page.locator('h2:has-text("Spiciest Quotes")')).toBeVisible();

    // Should show the Vega chart (SVG)
    await expect(page.locator('svg.marks')).toBeVisible();
  });

  test('displays overall statistics', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Should show stats in header
    const headerText = await page.locator('header p.text-stone-600').textContent();
    expect(headerText).toMatch(/\d+.*quotes.*\d+.*authors/i);
  });

  test('displays Vega-Lite bar chart', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Should have a Vega SVG chart with marks class
    await expect(page.locator('svg.marks')).toBeVisible();

    // Chart should have rendered with year labels
    await expect(page.locator('h2:has-text("Spiciness by Year")')).toBeVisible();
  });

  test('shows top quotes with permalinks', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Should have quotes with spiciness badges
    const quoteCount = await analytics.getQuoteCount();
    expect(quoteCount).toBeGreaterThan(0);
    expect(quoteCount).toBeLessThanOrEqual(100);

    // Should have permalink icons
    const permalinkCount = await analytics.getPermalinkCount();
    expect(permalinkCount).toBeGreaterThan(0);
  });

  test('shows "All Time" label by default', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Should show "All Time" label
    await expect(page.locator('text=All Time')).toBeVisible();

    // Reset button should not be visible
    await expect(analytics.resetFilterButton).not.toBeVisible();
  });

  test('author leaderboard shows ranked authors', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Should have multiple authors
    const authorCount = await analytics.getAuthorCount();
    expect(authorCount).toBeGreaterThan(5);

    // Should have clickable author rows (now rows, not links)
    const authorRows = analytics.authorLeaderboard.locator('tbody tr');
    expect(await authorRows.count()).toBeGreaterThan(5);
  });

  test('clicking author filters quotes', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Click first author row
    const firstRow = analytics.authorLeaderboard.locator('tbody tr').first();
    await firstRow.click();

    // Should show the author filter badge (orange)
    await expect(page.locator('span.bg-orange-100')).toBeVisible();

    // Reset button should appear
    await expect(analytics.resetFilterButton).toBeVisible();
  });

  test('quotes have spiciness badges', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Should have spiciness badges with light backgrounds
    const badges = analytics.quotesTable.locator('div.rounded-full:has-text("🌶️")');
    const firstBadge = badges.first();
    await expect(firstBadge).toBeVisible();

    const classes = await firstBadge.getAttribute('class');
    expect(classes).toMatch(/bg-(red|orange|yellow|green)-(100|200)/);
  });

  test('clicking year bar filters quotes', async ({ page }) => {
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Get the Vega chart SVG - click on a bar element
    const chart = page.locator('svg.marks');
    await expect(chart).toBeVisible();

    // Find bar elements in the chart - must have at least one
    const bars = chart.locator('path[aria-roledescription="bar"]');
    const barCount = await bars.count();
    expect(barCount).toBeGreaterThan(0);

    // Click the first bar
    await bars.first().click();

    // Should show the year filter badge (red) after clicking
    await expect(page.locator('span.bg-red-100')).toBeVisible({ timeout: 5000 });

    // Reset button should appear
    await expect(analytics.resetFilterButton).toBeVisible();
  });
});

test.describe('Analytics Navigation', () => {
  test('landing page has link to analytics', async ({ page }) => {
    const landing = new LandingPage(page);
    await landing.goto();

    // Should have analytics button
    const analyticsLink = page.locator('a[href*="analytics"]:has-text("Analytics")');
    await expect(analyticsLink).toBeVisible();
  });

  test('can navigate from landing to analytics', async ({ page }) => {
    const landing = new LandingPage(page);
    await landing.goto();

    // Click analytics link
    await page.click('a[href*="analytics"]:has-text("Analytics")');

    // Should be on analytics page
    await expect(page.locator('h1:has-text("Spicy Analytics")')).toBeVisible();
  });

  test('analytics has back link to landing', async ({ page }) => {
    const analytics = new AnalyticsPage(page);
    await analytics.goto();

    // Should have back link
    const backLink = page.locator('a:has-text("Back to Spicy Takes")');
    await expect(backLink).toBeVisible();

    // Click it
    await backLink.click();

    // Should be on landing page
    await expect(page.locator('h1:has-text("Spicy Takes")')).toBeVisible();
  });
});

test.describe('Analytics Error Handling', () => {
  test('shows error if parquet file fails to load', async ({ page }) => {
    // Intercept the parquet request and make it fail
    await page.route('**/analytics_quotes.parquet', route => {
      route.abort('failed');
    });

    const analytics = new AnalyticsPage(page);
    await analytics.goto();

    // Should show error message
    await expect(analytics.errorMessage).toBeVisible({ timeout: 15000 });
  });
});

test.describe('Analytics Responsive Behavior', () => {
  test('shows horizontal bar chart on mobile viewport', async ({ page }) => {
    // Set mobile viewport before navigating
    await page.setViewportSize({ width: 375, height: 667 });

    const analytics = new AnalyticsPage(page);
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Chart should be visible
    const chart = page.locator('svg.marks');
    await expect(chart).toBeVisible();

    // Verify bars exist
    const bars = chart.locator('path[aria-roledescription="bar"]');
    expect(await bars.count()).toBeGreaterThan(0);

    // On mobile (horizontal bars), bars should be wider than tall
    const firstBar = bars.first();
    const box = await firstBar.boundingBox();
    expect(box).not.toBeNull();
    expect(box!.width).toBeGreaterThan(box!.height);
  });

  test('shows vertical bar chart on desktop viewport', async ({ page }) => {
    // Set desktop viewport
    await page.setViewportSize({ width: 1280, height: 720 });

    const analytics = new AnalyticsPage(page);
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Chart should be visible
    const chart = page.locator('svg.marks');
    await expect(chart).toBeVisible();

    // Verify bars exist
    const bars = chart.locator('path[aria-roledescription="bar"]');
    expect(await bars.count()).toBeGreaterThan(0);

    // On desktop (vertical bars), bars should be taller than wide
    const firstBar = bars.first();
    const box = await firstBar.boundingBox();
    expect(box).not.toBeNull();
    expect(box!.height).toBeGreaterThan(box!.width);
  });

  test('filter selection persists across viewport resize', async ({ page }) => {
    // Start at desktop size
    await page.setViewportSize({ width: 1280, height: 720 });

    const analytics = new AnalyticsPage(page);
    await analytics.goto();
    await analytics.waitForDataLoad();

    // Click a year bar to apply filter
    const chart = page.locator('svg.marks');
    const bars = chart.locator('path[aria-roledescription="bar"]');
    await bars.first().click();

    // Verify filter is applied
    await expect(page.locator('span.bg-red-100')).toBeVisible();

    // Resize to mobile
    await page.setViewportSize({ width: 375, height: 667 });

    // Wait for chart to re-render with horizontal orientation (width > height)
    // Poll until the bar dimensions indicate horizontal layout
    await expect(async () => {
      const box = await bars.first().boundingBox();
      expect(box).not.toBeNull();
      expect(box!.width).toBeGreaterThan(box!.height);
    }).toPass({ timeout: 5000 });

    // Filter should still be visible
    await expect(page.locator('span.bg-red-100')).toBeVisible();
  });
});
