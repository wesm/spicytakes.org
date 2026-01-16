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
