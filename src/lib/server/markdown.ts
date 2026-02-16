import { marked } from 'marked';

/** Strip YAML frontmatter delimited by --- from raw markdown. */
export function stripFrontmatter(content: string): string {
  const match = content.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/);
  if (match) {
    return content.slice(match[0].length);
  }
  return content;
}

/** Strip frontmatter and convert markdown body to HTML. */
export function renderMarkdown(rawContent: string): string {
  const body = stripFrontmatter(rawContent);
  return marked.parse(body, { async: false }) as string;
}
