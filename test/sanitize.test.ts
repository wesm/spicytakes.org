import { describe, it, expect } from 'vitest';
import { sanitizeHtml } from '../src/lib/server/markdown';

describe('sanitizeHtml', () => {
  it('strips script tags', () => {
    expect(sanitizeHtml('<script>alert(1)</script>'))
      .toBe('alert(1)');
  });

  it('strips iframe tags', () => {
    expect(sanitizeHtml('<iframe src="https://evil.com"></iframe>'))
      .toBe('');
  });

  it('strips event handlers with whitespace separator', () => {
    const result = sanitizeHtml('<img src="x" onerror="alert(1)">');
    expect(result).not.toContain('onerror');
    expect(result).toContain('<img src="x">');
  });

  it('strips event handlers with slash separator', () => {
    const result = sanitizeHtml('<svg/onload="alert(1)">');
    expect(result).not.toContain('onload');
  });

  it('strips event handlers without quotes on value', () => {
    const result = sanitizeHtml('<img src=x onerror=alert(1)>');
    expect(result).not.toContain('onerror');
  });

  it('handles > inside quoted attribute values', () => {
    const input = '<img src="x>y" alt="test">';
    const result = sanitizeHtml(input);
    expect(result).toBe(input);
  });

  it('handles > inside quoted attr with event handler', () => {
    const input = '<img src="x>y" onerror="alert(1)">';
    const result = sanitizeHtml(input);
    expect(result).not.toContain('onerror');
    expect(result).toContain('src="x>y"');
  });

  it('passes through safe tags unchanged', () => {
    const input = '<p>Hello <strong>world</strong></p>';
    expect(sanitizeHtml(input)).toBe(input);
  });

  it('passes through links unchanged', () => {
    const input = '<a href="https://example.com">link</a>';
    expect(sanitizeHtml(input)).toBe(input);
  });

  it('strips dangerous tags inside quoted attrs', () => {
    const input = '<script type="text/javascript">alert(1)</script>';
    expect(sanitizeHtml(input)).toBe('alert(1)');
  });
});
