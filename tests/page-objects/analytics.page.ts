import { type Page, type Locator } from '@playwright/test';
import { BasePage } from './base.page';

export class AnalyticsPage extends BasePage {
  readonly heroTitle: Locator;
  readonly loadingIndicator: Locator;
  readonly errorMessage: Locator;
  readonly vegaChart: Locator;
  readonly authorLeaderboard: Locator;
  readonly quotesTable: Locator;
  readonly resetFilterButton: Locator;
  readonly yearFilter: Locator;

  constructor(page: Page) {
    super(page);
    this.heroTitle = page.locator('h1:has-text("Spicy Analytics")');
    this.loadingIndicator = page.locator('text=Loading');
    this.errorMessage = page.locator('text=/Error:/');
    this.vegaChart = page.locator('svg.marks');
    // Use the parent container of the h2 for these sections
    this.authorLeaderboard = page.locator('.bg-white.rounded-xl:has(h2:has-text("Leaderboard"))');
    this.quotesTable = page.locator('.bg-white.rounded-xl:has(h2:has-text("Spiciest Quotes"))');
    this.resetFilterButton = page.locator('button:has-text("Reset")');
    this.yearFilter = page.locator('span.bg-red-100');
  }

  async goto() {
    await this.page.goto('/analytics');
  }

  async waitForDataLoad(timeout = 30000) {
    // Wait for loading to disappear
    await this.page.waitForSelector('text=Loading', { state: 'hidden', timeout });
  }

  async getAuthorCount(): Promise<number> {
    return await this.authorLeaderboard.locator('tbody tr').count();
  }

  async getQuoteCount(): Promise<number> {
    return await this.quotesTable.locator('div.rounded-full:has-text("🌶️")').count();
  }

  async hasResetButton(): Promise<boolean> {
    return await this.resetFilterButton.isVisible();
  }

  async getPermalinkCount(): Promise<number> {
    return await this.quotesTable.locator('a[title*="Spicy Takes"]').count();
  }
}
