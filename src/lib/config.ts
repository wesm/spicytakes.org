/**
 * Blog configuration loader
 * Reads VITE_BLOG_ID env var and loads the appropriate config
 */

import type { BlogConfig, LandingConfig } from './types';

// Import all blog configs statically (Vite requires this for production builds)
import bennConfig from '../../config/benn.json';
import arminConfig from '../../config/armin.json';
import wesmConfig from '../../config/wesm.json';
import danluuConfig from '../../config/danluu.json';
import bcantrillConfig from '../../config/bcantrill.json';
import landingConfig from '../../config/landing.json';

// Map of blog configs - add new blogs here
const configs: Record<string, BlogConfig> = {
  benn: bennConfig as BlogConfig,
  armin: arminConfig as BlogConfig,
  wesm: wesmConfig as BlogConfig,
  danluu: danluuConfig as BlogConfig,
  bcantrill: bcantrillConfig as BlogConfig,
};

// Get blog ID from env, default to 'benn'
export const blogId = import.meta.env.VITE_BLOG_ID || 'benn';

// Check if we're in landing page mode
export const isLandingMode = blogId === 'landing';

// Export landing config for landing page
export const landing: LandingConfig = landingConfig as LandingConfig;

// Load the config for current blog (null in landing mode)
function loadConfig(): BlogConfig | null {
  if (isLandingMode) return null;
  const cfg = configs[blogId];
  if (!cfg) {
    throw new Error(`Unknown blog ID: "${blogId}". Valid options: ${Object.keys(configs).join(', ')}`);
  }
  return cfg;
}
export const config: BlogConfig | null = loadConfig();

// Export theme labels and icons derived from config (empty in landing mode)
export const THEME_LABELS: Record<string, string> = config?.themes
  ? Object.fromEntries(Object.entries(config.themes).map(([key, value]) => [key, value.label]))
  : {};

export const THEME_ICONS: Record<string, string> = config?.themes
  ? Object.fromEntries(Object.entries(config.themes).map(([key, value]) => [key, value.icon]))
  : {};

// Helper to get source URL for a post
// For transcripts, pass the post object to get video_url if available
// Returns empty string if transcript has no video_url (caller should hide link)
// Returns empty string if called in landing mode (no blog config)
export function getSourceUrl(filename: string, post?: { video_url?: string; content_type?: string }): string {
  // For transcripts, use video_url or return empty (no public URL for transcripts)
  if (post?.content_type === 'transcript') {
    return post.video_url || '';
  }

  // Guard against null config (landing mode)
  if (!config) {
    return '';
  }

  if (config.scraper.type === 'substack') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${config.sourceUrl}/p/${slug}`;
  }
  // For GitHub markdown blogs (lucumr), construct URL based on date
  // lucumr URLs are: /YYYY/M/D/slug/ (no leading zeros on month/day)
  if (config.scraper.type === 'github_markdown') {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+?)(\.md)?$/);
    if (match) {
      const [, year, month, day, slug] = match;
      const m = parseInt(month, 10);
      const d = parseInt(day, 10);
      return `${config.sourceUrl}/${year}/${m}/${d}/${slug}/`;
    }
  }
  // For quarto_blog blog posts, construct URL based on slug
  // wesmckinney.com URLs are: /blog/slug/
  if (config.scraper.type === 'quarto_blog') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${config.sourceUrl}/blog/${slug}/`;
  }
  // For static_html blogs (danluu), URL is just /slug/
  if (config.scraper.type === 'static_html') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${config.sourceUrl}/${slug}/`;
  }
  // For hugo_rss blogs (bcantrill), URL is /YYYY/MM/DD/slug/
  if (config.scraper.type === 'hugo_rss') {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+?)(\.md)?$/);
    if (match) {
      const [, year, month, day, slug] = match;
      return `${config.sourceUrl}/${year}/${month}/${day}/${slug}/`;
    }
  }
  return config.sourceUrl;
}
