import { marked, type Tokens } from 'marked';

/** Strip YAML frontmatter delimited by --- from raw markdown. */
export function stripFrontmatter(content: string): string {
  const match = content.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/);
  if (match) {
    return content.slice(match[0].length);
  }
  return content;
}

const SAFE_PROTOCOLS = /^(https?|mailto):/i;

/** Override link/image rendering to block dangerous protocols. */
const safeRenderer: Partial<marked.Renderer> = {
  link({ href, title, tokens }: Tokens.Link) {
    const text = this.parser.parseInline(tokens);
    if (href && !SAFE_PROTOCOLS.test(href)) {
      return text;
    }
    const titleAttr = title
      ? ` title="${title.replace(/"/g, '&quot;')}"` : '';
    return `<a href="${href}"${titleAttr}>${text}</a>`;
  },
  image({ href, title, text }: Tokens.Image) {
    if (href && !SAFE_PROTOCOLS.test(href)) {
      return text;
    }
    const titleAttr = title
      ? ` title="${title.replace(/"/g, '&quot;')}"` : '';
    const alt = text ? ` alt="${text.replace(/"/g, '&quot;')}"` : '';
    return `<img src="${href}"${alt}${titleAttr} />`;
  },
};

/** Strip dangerous HTML tags from rendered output. */
function sanitizeHtml(html: string): string {
  return html.replace(
    /<\/?(script|style|iframe|object|embed|form|input|textarea|button|select|meta|link|base)\b[^>]*>/gi,
    ''
  );
}

/** Strip frontmatter, parse markdown, and sanitize output. */
export function renderMarkdown(rawContent: string): string {
  const body = stripFrontmatter(rawContent);
  const html = marked.parse(body, {
    async: false,
    renderer: safeRenderer as marked.Renderer,
  }) as string;
  return sanitizeHtml(html);
}
