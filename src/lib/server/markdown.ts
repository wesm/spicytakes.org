import { marked } from 'marked';

/** Strip YAML frontmatter delimited by --- from raw markdown. */
export function stripFrontmatter(content: string): string {
  const match = content.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/);
  if (match) {
    return content.slice(match[0].length);
  }
  return content;
}

/** Strip raw HTML tags from markdown source to prevent XSS. */
function stripHtmlTags(md: string): string {
  return md.replace(/<\/?[a-zA-Z][^>]*>/g, '');
}

/** Strip frontmatter, sanitize, and convert markdown body to HTML. */
export function renderMarkdown(rawContent: string): string {
  const body = stripHtmlTags(stripFrontmatter(rawContent));
  return marked.parse(body, { async: false }) as string;
}
