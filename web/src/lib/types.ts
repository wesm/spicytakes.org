export interface Post {
  filename: string;
  summary: string;
  money_quotes: string[];
  themes: string[];
  tone: string;
  key_insight: string;
  // Computed fields
  date?: Date;
  title?: string;
  year?: number;
}

export interface Quote {
  quote: string;
  post: Post;
  themes: string[];
}

export interface ThemeData {
  name: string;
  label: string;
  icon: string;
  posts: Post[];
  quotes: Quote[];
}

export const THEME_LABELS: Record<string, string> = {
  'data_infrastructure': 'Data Infrastructure',
  'analytics_practice': 'Analytics Practice',
  'ai_llms': 'AI & LLMs',
  'startups_vc': 'Startups & VC',
  'career': 'Career',
  'industry_criticism': 'Industry Criticism',
  'tools_products': 'Tools & Products'
};

export const THEME_ICONS: Record<string, string> = {
  'data_infrastructure': '🏗️',
  'analytics_practice': '📊',
  'ai_llms': '🤖',
  'startups_vc': '🚀',
  'career': '💼',
  'industry_criticism': '🔍',
  'tools_products': '🛠️'
};
