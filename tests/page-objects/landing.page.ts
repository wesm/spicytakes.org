import { type Page, type Locator, expect } from '@playwright/test';
import { BasePage } from './base.page';

export class LandingPage extends BasePage {
  readonly heroTitle: Locator;
  readonly heroTagline: Locator;
  readonly blogCards: Locator;
  readonly howItWorksSection: Locator;
  readonly footer: Locator;

  constructor(page: Page) {
    super(page);
    // The landing page hero uses a div.min-h-screen container with header inside
    this.heroTitle = page.locator('header h1').first();
    this.heroTagline = page.locator('header p.text-xl').first();
    // Blog cards are links with href starting with https://
    this.blogCards = page.locator('section.max-w-5xl a[href^="https://"]');
    this.howItWorksSection = page.locator('section.bg-stone-100');
    this.footer = page.locator('footer');
  }

  async goto() {
    await super.goto('/');
  }

  getBlogCard(name: string): Locator {
    return this.page.locator(`a:has(h2:text("${name}"))`);
  }

  async getBlogCardCount(): Promise<number> {
    return await this.blogCards.count();
  }

  async expectBlogCardHasStats(name: string) {
    const card = this.getBlogCard(name);
    await expect(card).toBeVisible();
    // Should have posts count
    await expect(card.locator('text=/\\d+ posts/')).toBeVisible();
  }
}
