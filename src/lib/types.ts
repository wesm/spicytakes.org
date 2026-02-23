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
  source_url?: string;  // Direct URL from posts_index.json (for blogs with multiple sources)
  post_tags?: string[];  // Tags from posts_index (e.g. ["podcast", "transcript"])
  // Computed fields
  date?: Date;
  title?: string;
  year?: number | null;
  spiciness?: number | null;
}

export interface Quote {
  quote: string;
  post: Post;
  themes: string[];
  spiciness: number;
  date?: Date;
  year?: number | null;
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
  type:
    | 'blogger'
    | 'caseymuratori'
    | 'daringfireball'
    | 'github_markdown'
    | 'hey_world'
    | 'hugo_homepage'
    | 'hugo_rss'
    | 'jekyll_feed'
    | 'jekyll_static'
    | 'jvns'
    | 'kalzumeus'
    | 'martinfowler'
    | 'medium'
    | 'paulgraham'
    | 'quarto_blog'
    | 'rss_generic'
    | 'rss_nextjs'
    | 'static_html'
    | 'substack'
    | 'transcript_only'
    | 'wordpress'
    | 'zedshaw';
  substackUrl?: string;
  baseUrl?: string;
  indexUrl?: string;
  localPath?: string;
  postsPath?: string;
  blogPath?: string;
  transcriptsPath?: string;
  sourcePostPath?: string;  // URL path template for post links, e.g., '/blog/{slug}/'
  excludeSlugsFile?: string;
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
  hidden?: boolean;
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

export interface FeedPost {
  filename: string;
  title: string;
  dateStr: string | null;
  blogId: string;
  authorName: string;
  authorPhoto: string;
  subdomain: string;
  summary: string;
  key_insight: string;
  topQuotes: { quote: string; spiciness: number }[];
  spiciness: number | null;
  sourceUrl: string;
  spicytakesUrl: string;
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
