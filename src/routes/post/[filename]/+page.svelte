<script lang="ts">
  import { onMount } from 'svelte';
  import { browser } from '$app/environment';
  import { postsStore } from '$lib/stores';
  import { heatColor, type Post } from '$lib/types';
  import { THEME_LABELS, getSourceUrl, getSourceLabel, config, formatDate } from '$lib/config';
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();

  function toPost(serverPost: any): Post | undefined {
    if (!serverPost) return undefined;
    return {
      ...serverPost,
      date: new Date(serverPost.dateStr)
    };
  }

  let post = $derived(
    data.post
      ? toPost(data.post)
      : $postsStore.find(p => p.filename === data.filename)
  );

  let highlightedQuote: number | null = $state(null);
  let copiedQuote: number | null = $state(null);
  let showTranscript = $state(false);

  function updateHighlight() {
    if (!browser) return;
    const hash = window.location.hash;
    const match = hash.match(/^#quote-(\d+)$/);
    highlightedQuote = match ? parseInt(match[1]) : null;

    if (highlightedQuote !== null) {
      setTimeout(() => {
        document.getElementById(`quote-${highlightedQuote}`)
          ?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 100);
    }
  }

  function selectQuote(index: number) {
    if (!browser) return;
    window.location.hash = `quote-${index}`;
    highlightedQuote = index;
  }

  async function copyQuoteLink(
    index: number, event: MouseEvent
  ) {
    event.stopPropagation();
    if (!browser) return;
    const url =
      `${window.location.origin}` +
      `${window.location.pathname}#quote-${index}`;
    try {
      await navigator.clipboard.writeText(url);
      copiedQuote = index;
    } catch {
      // Clipboard API not available
    }
    highlightedQuote = index;
    window.location.hash = `quote-${index}`;
    setTimeout(() => { copiedQuote = null; }, 2000);
  }

  onMount(() => {
    updateHighlight();
    window.addEventListener('hashchange', updateHighlight);
    return () => {
      window.removeEventListener('hashchange', updateHighlight);
    };
  });
</script>

<svelte:head>
  {#if post}
    <title>{post.title} - {config?.name}</title>
    <meta name="description" content={post.summary} />
  {/if}
</svelte:head>

{#if post}
  {@const sourceUrl = getSourceUrl(post.filename, post)}
  <div class="post-page">
    <!-- Back link -->
    <a href="/" class="back-link">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M15 19l-7-7 7-7"/>
      </svg>
      Back to all posts
    </a>

    <article class="post-article" style="--heat: {heatColor(post.spiciness ?? 5)}">
      <div class="article-heat" aria-hidden="true"></div>
      <div class="article-body">
        <!-- Meta row -->
        <div class="meta-row">
          <div class="meta-left">
            <span class="meta-date">
              {formatDate(post.date)}
            </span>
            {#if sourceUrl}
              <span class="meta-dot"></span>
              <a
                href={sourceUrl}
                target="_blank"
                rel="noopener noreferrer"
                class="meta-source"
              >
                {getSourceLabel(post)}
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>
              </a>
            {/if}
          </div>
          {#if post.spiciness != null}
            <span class="spiciness-badge" style="color: {heatColor(post.spiciness)}" role="img" aria-label="Spiciness: {post.spiciness} out of 10">
              {post.spiciness}
            </span>
          {/if}
        </div>

        <!-- Title -->
        <h1 class="post-title">{post.title}</h1>

        <!-- Themes -->
        {#if post.themes?.length}
          <div class="theme-list">
            {#each post.themes as theme}
              <span class="theme-tag">
                {THEME_LABELS[theme] || theme}
              </span>
            {/each}
          </div>
        {/if}

        <!-- Summary -->
        <div class="section">
          <h2 class="section-label">Summary</h2>
          <p class="section-text">{post.summary}</p>
        </div>

        <!-- Key Insight -->
        {#if post.key_insight}
          <div class="section">
            <h2 class="section-label">Key Insight</h2>
            <blockquote class="insight-quote">
              {post.key_insight}
            </blockquote>
          </div>
        {/if}

        <!-- Money Quotes -->
        {#if post.money_quotes?.length}
          <div class="section">
            <h2 class="section-label">
              Spicy Quotes
              <span class="section-hint">(click to share)</span>
            </h2>
            <ul class="quote-list">
              {#each post.money_quotes as quote, i}
                {@const score = post.quote_spiciness?.[i] ?? 5}
                <li>
                  <div
                    id="quote-{i}"
                    onclick={() => selectQuote(i)}
                    role="button"
                    tabindex="0"
                    onkeydown={(e) => e.key === 'Enter' && selectQuote(i)}
                    class="quote-item"
                    class:highlighted={highlightedQuote === i}
                  >
                    <span class="quote-score" style="color: {heatColor(score)}" role="img" aria-label="Spiciness: {score} out of 10">{score}</span>
                    <p class="quote-text">{quote}</p>
                    <button
                      onclick={(e) => copyQuoteLink(i, e)}
                      class="copy-btn"
                      title={copiedQuote === i ? 'Copied!' : 'Copy link to quote'}
                    >
                      {#if copiedQuote === i}
                        <svg width="14" height="14" fill="none" stroke="#16a34a" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                        </svg>
                      {:else}
                        <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/>
                        </svg>
                      {/if}
                    </button>
                  </div>
                </li>
              {/each}
            </ul>
          </div>
        {/if}

        <!-- Tone -->
        {#if post.tone}
          <div class="section">
            <h2 class="section-label">Tone</h2>
            <p class="section-text muted">{post.tone}</p>
          </div>
        {/if}
      </div>
    </article>

    {#if data.transcriptHtml}
      <div class="transcript-panel">
        <button
          onclick={() => showTranscript = !showTranscript}
          class="transcript-toggle"
        >
          <span class="transcript-label">
            {showTranscript ? 'Hide Transcript' : 'Read Transcript'}
          </span>
          <svg
            width="16" height="16"
            viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2"
            class="transcript-chevron"
            class:open={showTranscript}
          >
            <path d="M6 9l6 6 6-6"/>
          </svg>
        </button>
        {#if showTranscript}
          <div class="transcript-body">
            <div class="prose">
              {@html data.transcriptHtml}
            </div>
          </div>
        {/if}
      </div>
    {/if}
  </div>
{:else}
  <div class="post-page">
    <div class="empty-state">
      <h1 class="empty-title">Post not found</h1>
      <p class="empty-hint">
        The post you're looking for doesn't exist.
      </p>
      <a href="/" class="empty-link">Back to all posts</a>
    </div>
  </div>
{/if}

<style>
  .post-page {
    max-width: 60rem;
    margin: 0 auto;
    padding: 1.5rem 1.5rem 3rem;
  }

  /* ── Back link ─────────────────────────────── */
  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.78rem;
    font-weight: 500;
    color: #78716c;
    text-decoration: none;
    margin-bottom: 1.25rem;
    transition: color 0.12s;
  }
  .back-link:hover {
    color: #dc2626;
  }

  /* ── Article card ──────────────────────────── */
  .post-article {
    display: flex;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.75rem;
    overflow: hidden;
  }

  .article-heat {
    width: 4px;
    flex-shrink: 0;
    background: var(--heat);
  }

  .article-body {
    flex: 1;
    min-width: 0;
    padding: 2rem 2.5rem;
  }

  /* ── Meta row ──────────────────────────────── */
  .meta-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.5rem;
  }

  .meta-left {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .meta-date {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
  }

  .meta-dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #d6d3d1;
  }

  .meta-source {
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
    font-size: 0.72rem;
    font-weight: 500;
    color: #dc2626;
    text-decoration: none;
    transition: color 0.12s;
  }
  .meta-source:hover {
    color: #b91c1c;
  }

  .spiciness-badge {
    font-size: 1.35rem;
    font-weight: 800;
    font-variant-numeric: tabular-nums;
  }

  /* ── Title ─────────────────────────────────── */
  .post-title {
    font-family: var(--font-family-serif);
    font-size: 1.6rem;
    font-weight: 600;
    color: #1c1917;
    line-height: 1.3;
    margin-bottom: 1rem;
  }

  /* ── Themes ────────────────────────────────── */
  .theme-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-bottom: 1.5rem;
  }

  .theme-tag {
    font-size: 0.68rem;
    font-weight: 500;
    padding: 0.15rem 0.5rem;
    background: #f5f5f4;
    color: #78716c;
    border-radius: 0.25rem;
  }

  /* ── Sections ──────────────────────────────── */
  .section {
    margin-bottom: 1.5rem;
  }

  .section-label {
    font-size: 0.6rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
    margin-bottom: 0.5rem;
  }

  .section-hint {
    font-weight: 400;
    text-transform: none;
    letter-spacing: normal;
    color: #d6d3d1;
  }

  .section-text {
    font-size: 0.88rem;
    line-height: 1.6;
    color: #44403c;
  }
  .section-text.muted {
    color: #78716c;
  }

  /* ── Key Insight ───────────────────────────── */
  .insight-quote {
    padding-left: 1rem;
    border-left: 3px solid #dc2626;
    font-family: var(--font-family-serif);
    font-size: 1.05rem;

    line-height: 1.55;
    color: #57534e;
    margin: 0;
  }

  /* ── Quotes ────────────────────────────────── */
  .quote-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .quote-item {
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
    position: relative;
    padding: 0.75rem 2.5rem 0.75rem 1rem;
    background: #fafaf9;
    border: 1px solid #f5f5f4;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s,
      box-shadow 0.2s;
  }
  .quote-item:hover {
    background: #f5f5f4;
    border-color: #e7e5e4;
    box-shadow: 0 2px 6px rgba(28, 25, 23, 0.04);
  }
  .quote-item.highlighted {
    background: rgba(234, 88, 12, 0.06);
    border-color: #ea580c;
    box-shadow: 0 0 0 2px rgba(234, 88, 12, 0.12);
  }

  .quote-score {
    font-size: 0.82rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
  }

  .quote-text {
    font-family: var(--font-family-serif);
    font-size: 1.05rem;

    line-height: 1.55;
    color: #1c1917;
    margin: 0;
  }

  .copy-btn {
    position: absolute;
    right: 0.5rem;
    top: 50%;
    transform: translateY(-50%);
    padding: 0.3rem;
    border-radius: 0.25rem;
    background: none;
    border: none;
    color: #a8a29e;
    cursor: pointer;
    transition: color 0.12s, background 0.12s;
  }
  .copy-btn:hover {
    color: #57534e;
    background: #e7e5e4;
  }

  /* ── Transcript ────────────────────────────── */
  .transcript-panel {
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.75rem;
    margin-top: 1rem;
    overflow: hidden;
  }

  .transcript-toggle {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.5rem;
    background: none;
    border: none;
    cursor: pointer;
    color: #57534e;
    transition: color 0.12s;
  }
  .transcript-toggle:hover {
    color: #1c1917;
  }

  .transcript-label {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }

  .transcript-chevron {
    transition: transform 0.2s;
  }
  .transcript-chevron.open {
    transform: rotate(180deg);
  }

  .transcript-body {
    padding: 0 2rem 2rem;
  }

  .prose {
    font-size: 0.9rem;
    line-height: 1.7;
    color: #44403c;
  }
  .prose :global(h1),
  .prose :global(h2),
  .prose :global(h3) {
    font-family: var(--font-family-serif);
    color: #1c1917;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
  }
  .prose :global(p) {
    margin-bottom: 0.75rem;
  }
  .prose :global(a) {
    color: #dc2626;
    text-decoration: underline;
    text-underline-offset: 2px;
  }
  .prose :global(a:hover) {
    color: #b91c1c;
  }
  .prose :global(blockquote) {
    border-left: 3px solid #d6d3d1;
    padding-left: 1rem;
    color: #78716c;

  }
  .prose :global(code) {
    font-size: 0.85em;
    background: #f5f5f4;
    padding: 0.1rem 0.3rem;
    border-radius: 0.2rem;
  }

  /* ── Empty state ───────────────────────────── */
  .empty-state {
    text-align: center;
    padding: 5rem 0;
  }

  .empty-title {
    font-family: var(--font-family-serif);
    font-size: 1.25rem;
    font-weight: 600;
    color: #57534e;
    margin-bottom: 0.5rem;
  }

  .empty-hint {
    font-size: 0.85rem;
    color: #a8a29e;
    margin-bottom: 1.5rem;
  }

  .empty-link {
    font-size: 0.82rem;
    font-weight: 500;
    color: #dc2626;
    text-decoration: none;
    transition: color 0.12s;
  }
  .empty-link:hover {
    color: #b91c1c;
  }

  /* ── Responsive ────────────────────────────── */
  @media (max-width: 640px) {
    .article-body {
      padding: 1.5rem;
    }
    .post-title {
      font-size: 1.25rem;
    }
  }
</style>
