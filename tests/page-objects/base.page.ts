import { type Page, type Locator } from '@playwright/test';

export class BasePage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async goto(path: string = '/') {
    await this.page.goto(path);
    await this.waitForHydration();
  }

  async waitForHydration() {
    // Wait for SvelteKit hydration to complete
    // The app is hydrated when interactive elements respond
    await this.page.waitForLoadState('networkidle');
    // Give Svelte a moment to mount
    await this.page.waitForTimeout(100);
  }

  async waitForDebounce(ms: number = 250) {
    // Wait for debounce timers (search uses 200ms debounce)
    await this.page.waitForTimeout(ms);
  }
}
