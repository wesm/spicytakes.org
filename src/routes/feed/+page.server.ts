import type { PageServerLoad } from './$types';
import type { FeedPost } from '$lib/types';
import { configs, buildSourceUrl, landing } from '$lib/config';
import {
  llmQuotesModules,
  spicyQuotesModules,
  postsIndexModules,
  getBlogData,
  parseDate,
  formatTitle,
} from '$lib/server/blog-data';

export const load: PageServerLoad = async () => {
  const blogs = landing.blogs.filter(b => !b.hidden);
  const feedPosts: FeedPost[] = [];

  for (const blog of blogs) {
    const blogConfig = configs[blog.id];
    if (!blogConfig) continue;

    const rawData = getBlogData(
      llmQuotesModules, blog.id, { posts: [] }
    );
    const spicyData = getBlogData(
      spicyQuotesModules, blog.id, { quotes: [] }
    );
    const postsIndex = getBlogData(
      postsIndexModules, blog.id, { posts: [] }
    );

    // Build lookups (same pattern as +layout.server.ts)
    const titleLookup: Record<string, string> = {};
    const urlLookup: Record<string, string> = {};
    const videoUrlLookup: Record<string, string> = {};
    const contentTypeLookup: Record<string, string> = {};
    for (const p of postsIndex.posts || []) {
      if (!p.filename) continue;
      const keys = [
        p.filename,
        p.filename.replace(/\.md$/, ''),
      ];
      if (p.title) for (const k of keys) titleLookup[k] = p.title;
      if (p.url) for (const k of keys) urlLookup[k] = p.url;
      if (p.video_url) {
        for (const k of keys) videoUrlLookup[k] = p.video_url;
      }
      if (p.content_type) {
        for (const k of keys) contentTypeLookup[k] = p.content_type;
      }
      const slug = p.slug;
      if (slug) {
        if (p.title) titleLookup[slug] = p.title;
        if (p.url) urlLookup[slug] = p.url;
      }
    }

    // Build spiciness lookup
    const spicyLookup: Record<string, number> = {};
    for (const q of spicyData.quotes || []) {
      const key = JSON.stringify([q.quote, q.filename]);
      spicyLookup[key] = q.spiciness || 5;
    }

    for (const post of rawData.posts) {
      if (post.error) continue;

      const dateStr = parseDate(post.filename);
      if (!dateStr) continue; // Feed requires dates

      const slug = post.filename
        .replace(/^\d{4}-\d{2}-\d{2}-/, '')
        .replace(/\.md$/, '');
      const title = titleLookup[post.filename]
        || titleLookup[slug]
        || formatTitle(post.filename);

      const sourceUrl = buildSourceUrl(
        post.filename,
        blogConfig,
        {
          video_url: videoUrlLookup[post.filename]
            || videoUrlLookup[slug],
          content_type: contentTypeLookup[post.filename]
            || contentTypeLookup[slug],
          source_url: urlLookup[post.filename]
            || urlLookup[slug],
        }
      );

      // Compute per-quote spiciness and pick top 3
      const quotesWithSpiciness = (post.money_quotes || []).map(
        q => ({
          quote: q,
          spiciness: spicyLookup[
            JSON.stringify([q, post.filename])
          ] || 5,
        })
      );
      const topQuotes = [...quotesWithSpiciness]
        .sort((a, b) => b.spiciness - a.spiciness)
        .slice(0, 3);

      // Compute average post spiciness
      let spiciness: number | null = null;
      if (quotesWithSpiciness.length > 0) {
        const avg = quotesWithSpiciness.reduce(
          (sum, q) => sum + q.spiciness, 0
        ) / quotesWithSpiciness.length;
        spiciness = Math.round(avg * 10) / 10;
      }

      const filenameStem = post.filename.replace(/\.md$/, '');

      feedPosts.push({
        filename: post.filename,
        title,
        dateStr,
        blogId: blog.id,
        authorName: blog.name,
        authorPhoto: blog.photo,
        subdomain: blog.subdomain,
        summary: post.summary,
        key_insight: post.key_insight,
        topQuotes,
        spiciness,
        sourceUrl,
        spicytakesUrl: `https://${blog.subdomain}/post/${filenameStem}`,
      });
    }
  }

  // Sort by date descending, take top 1000
  feedPosts.sort((a, b) => b.dateStr!.localeCompare(a.dateStr!));
  const posts = feedPosts.slice(0, 1000);

  // Collect unique blog authors for filter options
  const authorSet = new Set(posts.map(p => p.blogId));
  const authors = blogs
    .filter(b => authorSet.has(b.id))
    .map(b => ({ id: b.id, name: b.name }));

  return { posts, authors };
};
