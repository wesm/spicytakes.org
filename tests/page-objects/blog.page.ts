import { type Page, type Locator, expect } from '@playwright/test';
import { BasePage } from './base.page';

export class BlogPage extends BasePage {
  // Header elements
  readonly siteTitle: Locator;
  readonly blogName: Locator;
  readonly searchInput: Locator;
  readonly themePills: Locator;
  readonly clearFiltersButton: Locator;

  // View tabs
  readonly postsTab: Locator;
  readonly quotesTab: Locator;
  readonly themesTab: Locator;

  // Stats
  readonly postsCount: Locator;
  readonly quotesCount: Locator;

  // View controls
  readonly sortSelect: Locator;
  readonly yearSelect: Locator;
  readonly spicySlider: Locator;
  readonly displayCount: Locator;

  // Content
  readonly postCards: Locator;
  readonly quoteCards: Locator;
  readonly yearSections: Locator;

  constructor(page: Page) {
    super(page);

    // Header
    this.siteTitle = page.locator('header a:has-text("Spicy Takes")');
    this.blogName = page.locator('header h1');
    this.searchInput = page.locator('input[placeholder*="Search"]');
    this.themePills = page.locator('button.theme-pill');
    this.clearFiltersButton = page.locator('button:has-text("Clear filters")');

    // View tabs
    this.postsTab = page.locator('nav button:has-text("Posts")');
    this.quotesTab = page.locator('nav button:has-text("Quotes")');
    this.themesTab = page.locator('nav button:has-text("Themes")');

    // Stats in the stats bar
    this.postsCount = page.locator('div:has(strong):has-text("posts")').first();
    this.quotesCount = page.locator('div:has(strong):has-text("quotes")').first();

    // View controls (shared between Posts and Quotes views)
    this.sortSelect = page.locator('select').filter({ has: page.locator('option:has-text("Chronological")') });
    this.yearSelect = page.locator('select').filter({ has: page.locator('option[value="all"]') });
    this.spicySlider = page.locator('input[type="range"]');
    this.displayCount = page.locator('.control-count');

    // Content cards
    this.postCards = page.locator('button:has(h4)');
    this.quoteCards = page.locator('button:has(blockquote)');
    this.yearSections = page.locator('section:has(h3)');
  }

  async goto() {
    await super.goto('/');
  }

  async switchToView(view: 'posts' | 'quotes' | 'themes') {
    switch (view) {
      case 'posts':
        await this.postsTab.click();
        break;
      case 'quotes':
        await this.quotesTab.click();
        break;
      case 'themes':
        await this.themesTab.click();
        break;
    }
    await this.page.waitForTimeout(100); // Let view transition
  }

  async search(query: string) {
    await this.searchInput.fill(query);
    await this.waitForDebounce();
  }

  async clearSearch() {
    await this.searchInput.clear();
    await this.waitForDebounce();
  }

  async toggleTheme(themeName: string) {
    await this.page.locator(`button.theme-pill:has-text("${themeName}")`).click();
  }

  async setMinSpiciness(value: number) {
    await this.spicySlider.fill(String(value));
  }

  async selectYear(year: string) {
    await this.yearSelect.selectOption({ label: year });
  }

  async selectSort(option: 'Chronological' | 'Spiciest First') {
    await this.sortSelect.selectOption({ label: option });
  }

  async getDisplayedCount(): Promise<number> {
    const text = await this.displayCount.textContent();
    const match = text?.match(/(\d+)/);
    return match ? parseInt(match[1]) : 0;
  }

  async clickFirstPost() {
    await this.postCards.first().click();
  }

  async clickFirstQuote() {
    await this.quoteCards.first().click();
  }

  getThemePill(name: string): Locator {
    return this.page.locator(`button.theme-pill:has-text("${name}")`);
  }

  async isThemeActive(name: string): Promise<boolean> {
    const pill = this.getThemePill(name);
    const classes = await pill.getAttribute('class');
    return classes?.split(/\s+/).includes('active') ?? false;
  }
}
