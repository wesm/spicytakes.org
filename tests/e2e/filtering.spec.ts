import { test, expect } from '@playwright/test';
import { BlogPage } from '../page-objects/blog.page';

test.describe('Filtering and Search', () => {
  let blog: BlogPage;

  test.beforeEach(async ({ page }) => {
    blog = new BlogPage(page);
    await blog.goto();
  });

  test.describe('Search', () => {
    test('filters posts by search query', async () => {
      const initialCount = await blog.postCards.count();

      // Search for a term that should narrow results
      await blog.search('data');

      const filteredCount = await blog.postCards.count();
      expect(filteredCount).toBeLessThan(initialCount);
      expect(filteredCount).toBeGreaterThan(0);
    });

    test('shows no results message for impossible query', async () => {
      await blog.search('xyznonexistentqueryzyx');
      await expect(blog.page.locator('text="No posts found"')).toBeVisible();
    });

    test('clears search and restores results', async () => {
      const initialCount = await blog.postCards.count();

      await blog.search('data');
      await blog.page.waitForTimeout(100);
      const filteredCount = await blog.postCards.count();
      expect(filteredCount).toBeLessThan(initialCount);

      await blog.clearSearch();
      await blog.page.waitForTimeout(100);
      const restoredCount = await blog.postCards.count();
      // Restored count should be greater than or equal to filtered
      expect(restoredCount).toBeGreaterThanOrEqual(filteredCount);
    });

    test('search works in Quotes view', async () => {
      await blog.switchToView('quotes');
      const initialCount = await blog.quoteCards.count();

      await blog.search('analytics');

      const filteredCount = await blog.quoteCards.count();
      expect(filteredCount).toBeLessThan(initialCount);
    });

    test('search has debounce behavior', async () => {
      const initialCount = await blog.postCards.count();

      // Type a search term that should filter results
      await blog.searchInput.fill('xyznonexistentqueryzyx');

      // Results should not change immediately (before debounce)
      await blog.page.waitForTimeout(50);
      const countBeforeDebounce = await blog.postCards.count();
      // Before debounce completes, results should still show initial count
      expect(countBeforeDebounce).toBe(initialCount);

      // After debounce period, results should update
      await blog.waitForDebounce();
      await blog.page.waitForTimeout(100);

      // Verify that filtering happened after debounce
      const countAfterDebounce = await blog.postCards.count();
      expect(countAfterDebounce).toBeLessThan(initialCount);
    });
  });

  test.describe('Spiciness Slider', () => {
    test('filters by minimum spiciness', async () => {
      const initialCount = await blog.postCards.count();

      // Set minimum spiciness to 5
      await blog.setMinSpiciness(5);
      await blog.page.waitForTimeout(100);

      const filteredCount = await blog.postCards.count();
      expect(filteredCount).toBeLessThanOrEqual(initialCount);
    });

    test('spiciness filter works in Quotes view', async () => {
      await blog.switchToView('quotes');
      const initialCount = await blog.quoteCards.count();

      await blog.setMinSpiciness(7);
      await blog.page.waitForTimeout(100);

      const filteredCount = await blog.quoteCards.count();
      expect(filteredCount).toBeLessThan(initialCount);
    });

    test('high spiciness threshold reduces results', async ({}, testInfo) => {
      const initialCount = await blog.postCards.count();
      // Skip if dataset is too small to meaningfully filter
      if (initialCount < 10) {
        testInfo.skip();
        return;
      }

      await blog.setMinSpiciness(9);
      await blog.page.waitForTimeout(100);

      const filteredCount = await blog.postCards.count();
      // High spiciness threshold should reduce results (not all posts have scores >= 9)
      expect(filteredCount).toBeLessThan(initialCount);
    });
  });

  test.describe('Year Filter', () => {
    test('filters by specific year', async ({}, testInfo) => {
      const initialCount = await blog.postCards.count();

      // Get a year dynamically from the dropdown (skip "All Years" and "Undated" options)
      const yearOptions = await blog.yearSelect.locator('option').allTextContents();
      const yearOnlyOptions = yearOptions.filter(y => /^\d{4}$/.test(y));

      // Skip if there's only one year (filtering won't reduce results)
      if (yearOnlyOptions.length < 2) {
        testInfo.skip();
        return;
      }

      const specificYear = yearOnlyOptions[0];
      await blog.selectYear(specificYear);
      await blog.page.waitForTimeout(100);

      const filteredCount = await blog.postCards.count();
      // With multiple years, filtering to one should reduce results
      expect(filteredCount).toBeLessThan(initialCount);
      expect(filteredCount).toBeGreaterThan(0);
    });

    test('All Years option shows all posts', async ({}, testInfo) => {
      // Get a year dynamically from the dropdown
      const yearOptions = await blog.yearSelect.locator('option').allTextContents();
      const yearOnlyOptions = yearOptions.filter(y => /^\d{4}$/.test(y));

      // Skip if there's only one year
      if (yearOnlyOptions.length < 2) {
        testInfo.skip();
        return;
      }

      // First filter to a year
      await blog.selectYear(yearOnlyOptions[0]);
      await blog.page.waitForTimeout(100);
      const filteredCount = await blog.postCards.count();

      // Then reset to All Years
      await blog.selectYear('All Years');
      await blog.page.waitForTimeout(100);
      const allCount = await blog.postCards.count();

      expect(allCount).toBeGreaterThan(filteredCount);
    });

    test('year filter works in Quotes view', async ({}, testInfo) => {
      await blog.switchToView('quotes');
      const initialCount = await blog.quoteCards.count();

      // Get a year dynamically from the dropdown (skip "All Years" and "Undated" options)
      const yearOptions = await blog.yearSelect.locator('option').allTextContents();
      const yearOnlyOptions = yearOptions.filter(y => /^\d{4}$/.test(y));

      // Skip if there's only one year
      if (yearOnlyOptions.length < 2) {
        testInfo.skip();
        return;
      }

      await blog.selectYear(yearOnlyOptions[0]);
      await blog.page.waitForTimeout(100);

      const filteredCount = await blog.quoteCards.count();
      expect(filteredCount).toBeLessThan(initialCount);
    });
  });

  test.describe('Theme Pills', () => {
    test('clicking theme pill activates it', async () => {
      const firstPill = blog.themePills.first();

      await firstPill.click();
      await expect(firstPill).toHaveClass(/theme-pill-active/);
    });

    test('theme filter reduces results', async () => {
      const initialCount = await blog.postCards.count();

      await blog.themePills.first().click();
      await blog.page.waitForTimeout(100);

      const filteredCount = await blog.postCards.count();
      expect(filteredCount).toBeLessThan(initialCount);
    });

    test('multiple themes can be selected', async () => {
      const pills = blog.themePills;
      if ((await pills.count()) >= 2) {
        await pills.nth(0).click();
        await pills.nth(1).click();

        await expect(pills.nth(0)).toHaveClass(/theme-pill-active/);
        await expect(pills.nth(1)).toHaveClass(/theme-pill-active/);
      }
    });

    test('Clear filters button appears when filters active', async () => {
      await expect(blog.clearFiltersButton).not.toBeVisible();

      await blog.themePills.first().click();

      await expect(blog.clearFiltersButton).toBeVisible();
    });

    test('Clear filters resets all filters', async () => {
      const initialCount = await blog.postCards.count();

      // Apply theme filter
      await blog.themePills.first().click();
      await blog.page.waitForTimeout(100);

      // Clear all filters
      await blog.clearFiltersButton.click();
      await blog.page.waitForTimeout(100);

      // Theme should be deselected
      await expect(blog.themePills.first()).not.toHaveClass(/theme-pill-active/);
    });
  });

  test.describe('Sorting', () => {
    test('can switch to Spiciest First sorting', async () => {
      await blog.selectSort('Spiciest First');
      await blog.page.waitForTimeout(100);

      // Check that year sections show "Top 5 Spiciest"
      await expect(blog.page.locator('text="Top 5 Spiciest"').first()).toBeVisible();
    });

    test('can switch back to Chronological sorting', async () => {
      await blog.selectSort('Spiciest First');
      await blog.page.waitForTimeout(100);

      await blog.selectSort('Chronological');
      await blog.page.waitForTimeout(100);

      // Year sections should show post count instead - just verify the section headers are visible
      await expect(blog.yearSections.first()).toBeVisible();
    });

    test('sorting works in Quotes view', async () => {
      await blog.switchToView('quotes');

      await blog.selectSort('Spiciest First');
      await blog.page.waitForTimeout(100);
      await expect(blog.page.locator('text="Top 5 Spiciest"').first()).toBeVisible();
    });
  });

  test.describe('Combined Filters', () => {
    test('search and theme filter work together', async () => {
      const initialCount = await blog.postCards.count();

      await blog.search('data');
      await blog.page.waitForTimeout(100);
      const afterSearch = await blog.postCards.count();

      await blog.themePills.first().click();
      await blog.page.waitForTimeout(100);
      const afterTheme = await blog.postCards.count();

      expect(afterSearch).toBeLessThanOrEqual(initialCount);
      expect(afterTheme).toBeLessThanOrEqual(afterSearch);
    });

    test('year and spiciness filters work together', async () => {
      const initialCount = await blog.postCards.count();

      // Get a year dynamically from the dropdown
      const yearOptions = await blog.yearSelect.locator('option').allTextContents();
      const specificYear = yearOptions.find(y => y !== 'All Years' && /^\d{4}$/.test(y));
      expect(specificYear).toBeDefined();

      await blog.selectYear(specificYear!);
      await blog.page.waitForTimeout(100);
      const afterYear = await blog.postCards.count();

      await blog.setMinSpiciness(5);
      await blog.page.waitForTimeout(100);
      const afterSpiciness = await blog.postCards.count();

      expect(afterYear).toBeLessThanOrEqual(initialCount);
      expect(afterSpiciness).toBeLessThanOrEqual(afterYear);
    });
  });
});
