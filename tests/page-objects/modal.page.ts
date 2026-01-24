import { type Page, type Locator, expect } from '@playwright/test';

export class ModalPage {
  readonly page: Page;
  readonly backdrop: Locator;
  readonly modalContent: Locator;
  readonly closeButton: Locator;
  readonly title: Locator;
  readonly date: Locator;
  readonly spicinessBadge: Locator;
  readonly summary: Locator;
  readonly keyInsight: Locator;
  readonly spicyQuotes: Locator;
  readonly themeTags: Locator;
  readonly permalinkButton: Locator;
  readonly sourceLink: Locator;

  constructor(page: Page) {
    this.page = page;
    this.backdrop = page.locator('.fixed.inset-0 button[aria-label="Close modal"]');
    this.modalContent = page.locator('.fixed.inset-0 .bg-white.rounded-2xl');
    this.closeButton = page.locator('button[aria-label="Close"]');
    this.title = page.locator('.fixed.inset-0 h2').first();
    this.date = page.locator('.fixed.inset-0 .uppercase.tracking-wide').first();
    this.spicinessBadge = page.locator('.fixed.inset-0 [aria-label^="Spiciness score"]');
    this.summary = page.locator('.fixed.inset-0 h3:has-text("Summary") + p');
    this.keyInsight = page.locator('.fixed.inset-0 h3:has-text("Key Insight") + blockquote');
    this.spicyQuotes = page.locator('.fixed.inset-0 ul li a[href^="/post/"]');
    this.themeTags = page.locator('.fixed.inset-0 .bg-blue-50.text-blue-700');
    this.permalinkButton = page.locator('.fixed.inset-0 a:has-text("Permalink")');
    this.sourceLink = page.locator('.fixed.inset-0 a[target="_blank"]');
  }

  async isVisible(): Promise<boolean> {
    return await this.modalContent.isVisible();
  }

  async waitForOpen() {
    await expect(this.modalContent).toBeVisible();
  }

  async waitForClose() {
    await expect(this.modalContent).not.toBeVisible();
  }

  async close() {
    await this.closeButton.click();
    await this.waitForClose();
  }

  async closeByBackdrop() {
    // Click at the top-left corner of the backdrop where modal content won't intercept
    const box = await this.backdrop.boundingBox();
    if (box) {
      await this.page.mouse.click(box.x + 10, box.y + 10);
    }
    await this.waitForClose();
  }

  async closeByEscape() {
    await this.page.keyboard.press('Escape');
    await this.waitForClose();
  }

  async clickPermalink() {
    await this.permalinkButton.click();
  }

  async clickQuote(index: number) {
    await this.spicyQuotes.nth(index).click();
  }

  async getTitle(): Promise<string> {
    // Get just the text node, excluding the Permalink button text
    const titleElement = this.title;
    const fullText = await titleElement.textContent();
    // Remove "Permalink" text that's part of the nested link
    return (fullText ?? '').replace(/\s*Permalink\s*/, '').trim();
  }

  async getSpiciness(): Promise<number | null> {
    const text = await this.spicinessBadge.locator('.font-bold').textContent();
    return text ? parseInt(text) : null;
  }

  async getQuoteCount(): Promise<number> {
    return await this.spicyQuotes.count();
  }
}
