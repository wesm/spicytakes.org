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
import jessfrazConfig from '../../config/jessfraz.json';
import geohotConfig from '../../config/geohot.json';
import mrocklinConfig from '../../config/mrocklin.json';
import criccominiConfig from '../../config/criccomini.json';
import skamilleConfig from '../../config/skamille.json';
import mitchellhConfig from '../../config/mitchellh.json';
import mathbabeConfig from '../../config/mathbabe.json';
import nayafiaConfig from '../../config/nayafia.json';
import joereisConfig from '../../config/joereis.json';
import sspConfig from '../../config/ssp.json';
import paulgConfig from '../../config/paulg.json';
import atwoodConfig from '../../config/atwood.json';
import unclebobConfig from '../../config/unclebob.json';
import hillelConfig from '../../config/hillel.json';
import landingConfig from '../../config/landing.json';

// Map of blog configs - add new blogs here
const configs: Record<string, BlogConfig> = {
  benn: bennConfig as BlogConfig,
  armin: arminConfig as BlogConfig,
  wesm: wesmConfig as BlogConfig,
  danluu: danluuConfig as BlogConfig,
  bcantrill: bcantrillConfig as BlogConfig,
  jessfraz: jessfrazConfig as BlogConfig,
  geohot: geohotConfig as BlogConfig,
  mrocklin: mrocklinConfig as BlogConfig,
  criccomini: criccominiConfig as BlogConfig,
  skamille: skamilleConfig as BlogConfig,
  mitchellh: mitchellhConfig as BlogConfig,
  mathbabe: mathbabeConfig as BlogConfig,
  nayafia: nayafiaConfig as BlogConfig,
  joereis: joereisConfig as BlogConfig,
  ssp: sspConfig as BlogConfig,
  paulg: paulgConfig as BlogConfig,
  atwood: atwoodConfig as BlogConfig,
  unclebob: unclebobConfig as BlogConfig,
  hillel: hillelConfig as BlogConfig,
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

// Date precision: "day" (default), "month", or "year"
export const datePrecision: 'day' | 'month' | 'year' = (config as any)?.datePrecision || 'day';

// Shared date formatter that respects config precision
export function formatDate(date: Date | undefined, monthFormat: 'long' | 'short' = 'long'): string {
  if (!date) return '';

  const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
  };

  // Only include month for day or month precision
  if (datePrecision === 'day' || datePrecision === 'month') {
    options.month = monthFormat;
  }

  if (datePrecision === 'day') {
    options.day = 'numeric';
  }

  return date.toLocaleDateString('en-US', options);
}

// Pure helper to build source URL from config - exported for testing
export function buildSourceUrl(
  filename: string,
  cfg: BlogConfig,
  post?: { video_url?: string; content_type?: string }
): string {
  // For transcripts, use video_url or return empty (no public URL for transcripts)
  if (post?.content_type === 'transcript') {
    return post.video_url || '';
  }

  if (cfg.scraper.type === 'substack') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${cfg.sourceUrl}/p/${slug}`;
  }
  // For GitHub markdown blogs (lucumr), construct URL based on date
  // lucumr URLs are: /YYYY/M/D/slug/ (no leading zeros on month/day)
  if (cfg.scraper.type === 'github_markdown') {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+?)(\.md)?$/);
    if (match) {
      const [, year, month, day, slug] = match;
      const m = parseInt(month, 10);
      const d = parseInt(day, 10);
      return `${cfg.sourceUrl}/${year}/${m}/${d}/${slug}/`;
    }
  }
  // For quarto_blog blog posts, construct URL based on slug
  // wesmckinney.com URLs are: /blog/slug/
  if (cfg.scraper.type === 'quarto_blog') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${cfg.sourceUrl}/blog/${slug}/`;
  }
  // For static_html blogs (danluu), URL is just /slug/
  if (cfg.scraper.type === 'static_html') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${cfg.sourceUrl}/${slug}/`;
  }
  // For hugo_rss blogs (bcantrill), URL is /YYYY/MM/DD/slug/
  if (cfg.scraper.type === 'hugo_rss') {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+?)(\.md)?$/);
    if (match) {
      const [, year, month, day, slug] = match;
      return `${cfg.sourceUrl}/${year}/${month}/${day}/${slug}/`;
    }
  }
  // For hugo_homepage blogs (jessfraz), URL is /post/slug/
  if (cfg.scraper.type === 'hugo_homepage') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${cfg.sourceUrl}/post/${slug}/`;
  }
  // For jekyll_feed blogs, URL pattern is configurable via sourcePostPath
  // Default: /blog/jekyll/update/{year}/{month}/{day}/{slug}.html (geohot)
  // Uncle Bob uses: /uncle-bob/{year}/{month}/{day}/{slug}.html
  if (cfg.scraper.type === 'jekyll_feed') {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+?)(\.md)?$/);
    if (match) {
      const [, year, month, day, slug] = match;
      const postPath = cfg.scraper.sourcePostPath || '/blog/jekyll/update/{year}/{month}/{day}/{slug}.html';
      return `${cfg.sourceUrl}${postPath
        .replace('{year}', year)
        .replace('{month}', month)
        .replace('{day}', day)
        .replace('{slug}', slug)}`;
    }
  }
  // For wordpress blogs (mathbabe), URL is /YYYY/MM/DD/slug/
  if (cfg.scraper.type === 'wordpress') {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})-(.+?)(\.md)?$/);
    if (match) {
      const [, year, month, day, slug] = match;
      return `${cfg.sourceUrl}/${year}/${month}/${day}/${slug}/`;
    }
  }
  // For jekyll_static blogs (nadia.xyz), URL is just /slug
  if (cfg.scraper.type === 'jekyll_static') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${cfg.sourceUrl}/${slug}`;
  }
  // For rss_generic blogs, use sourcePostPath from config or default to /blog/{slug}/
  if (cfg.scraper.type === 'rss_generic') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    const postPath = cfg.scraper.sourcePostPath || '/blog/{slug}/';
    return `${cfg.sourceUrl}${postPath.replace('{slug}', slug)}`;
  }
  // For paulgraham essays, URL is /slug.html
  if (cfg.scraper.type === 'paulgraham') {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '').replace(/\.md$/, '');
    return `${cfg.sourceUrl}/${slug}.html`;
  }
  return cfg.sourceUrl;
}

// Helper to get source URL for a post using the global config
// For transcripts, pass the post object to get video_url if available
// Returns empty string if transcript has no video_url (caller should hide link)
// Returns empty string if called in landing mode (no blog config)
export function getSourceUrl(filename: string, post?: { video_url?: string; content_type?: string }): string {
  // Guard against null config (landing mode)
  if (!config) {
    return '';
  }
  return buildSourceUrl(filename, config, post);
}
