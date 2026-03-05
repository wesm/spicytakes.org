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

/** Escape characters that are special inside HTML attributes. */
function escapeAttr(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/** Override link/image rendering to block dangerous protocols. */
const safeRenderer: Partial<marked.Renderer> = {
  link({ href, title, tokens }: Tokens.Link) {
    const text = this.parser.parseInline(tokens);
    if (href && !SAFE_PROTOCOLS.test(href)) {
      return text;
    }
    const titleAttr = title
      ? ` title="${escapeAttr(title)}"` : '';
    return `<a href="${escapeAttr(href)}"${titleAttr}>${text}</a>`;
  },
  image({ href, title, text }: Tokens.Image) {
    if (href && !SAFE_PROTOCOLS.test(href)) {
      return text;
    }
    const titleAttr = title
      ? ` title="${escapeAttr(title)}"` : '';
    const alt = text
      ? ` alt="${escapeAttr(text)}"` : '';
    return `<img src="${escapeAttr(href)}"${alt}${titleAttr} />`;
  },
};

/** Strip on* event handler attributes from inside an HTML tag. */
function stripEventHandlers(tag: string): string {
  return tag.replace(
    /[\s/]+on\w+\s*=\s*("[^"]*"|'[^']*'|[^\s>]*)/gi, ''
  );
}

/**
 * Match an HTML opening tag, aware of quoted attribute values
 * (so `>` inside quotes doesn't terminate the match early).
 * Each segment is: quoted string or non-quote/non-`>` char.
 */
const HTML_TAG_RE =
  /<[a-z](?:"[^"]*"|'[^']*'|[^"'>])*>/gi;

/** Strip dangerous HTML tags and event handler attributes. */
export function sanitizeHtml(html: string): string {
  return html
    .replace(
      /<\/?(script|style|iframe|object|embed|form|input|textarea|button|select|meta|link|base)\b(?:"[^"]*"|'[^']*'|[^"'>])*>/gi,
      ''
    )
    .replace(HTML_TAG_RE, (tag) => {
      if (/[\s/]+on\w+\s*=/i.test(tag)) {
        return stripEventHandlers(tag);
      }
      return tag;
    });
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
