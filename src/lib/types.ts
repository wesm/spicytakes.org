export interface Post {
  filename: string;
  summary: string;
  money_quotes: string[];
  themes: string[];
  tone: string;
  key_insight: string;
  // Optional fields from scrapers
  video_url?: string;
  content_type?: string;
  // Computed fields
  date?: Date;
  title?: string;
  year?: number;
  spiciness?: number | null;
}

export interface Quote {
  quote: string;
  post: Post;
  themes: string[];
  spiciness: number;
  date?: Date;
  year?: number;
}

export interface ThemeData {
  name: string;
  label: string;
  icon: string;
  posts: Post[];
  quotes: Quote[];
}

export interface ThemeConfig {
  label: string;
  icon: string;
}

export interface ScraperConfig {
  type: 'substack' | 'github_markdown' | 'quarto_blog';
  substackUrl?: string;
  localPath?: string;
  postsPath?: string;
  blogPath?: string;
  transcriptsPath?: string;
}

export interface BlogConfig {
  id: string;
  name: string;
  tagline: string;
  description: string;
  sourceUrl: string;
  sourceLabel: string;
  scraper: ScraperConfig;
  themes: Record<string, ThemeConfig>;
  llmAnalysis: {
    contextPrompt: string;
    depthLevel: string;
    summaryLength: string;
  };
  spiciness: {
    contextPrompt: string;
  };
}

export interface BlogCard {
  id: string;
  name: string;
  tagline: string;
  description: string;
  subdomain: string;
  photo: string;
  stats: {
    posts: number;
    quotes: number;
  };
}

export interface LandingConfig {
  id: string;
  title: string;
  tagline: string;
  description: string;
  blogs: BlogCard[];
}

export function getSpicyLabel(spiciness: number): string {
  if (spiciness <= 3) return 'Mild';
  if (spiciness <= 5) return 'Moderate';
  if (spiciness <= 7) return 'Pointed';
  if (spiciness <= 9) return 'Spicy';
  return 'Maximum Heat';
}

export function getSpicyColor(spiciness: number): string {
  if (spiciness <= 3) return 'bg-green-100 text-green-700';
  if (spiciness <= 5) return 'bg-yellow-100 text-yellow-700';
  if (spiciness <= 7) return 'bg-orange-100 text-orange-700';
  if (spiciness <= 9) return 'bg-red-100 text-red-700';
  return 'bg-red-200 text-red-800';
}

export function getSpicyTextColor(spiciness: number): string {
  if (spiciness <= 3) return 'text-green-600';
  if (spiciness <= 5) return 'text-yellow-600';
  if (spiciness <= 7) return 'text-orange-600';
  if (spiciness <= 9) return 'text-red-600';
  return 'text-red-700';
}
