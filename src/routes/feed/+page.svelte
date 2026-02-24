<script lang="ts">
  import { base } from '$app/paths';
  import type { PageData } from './$types';
  import { getSpicyColor, heatColor } from '$lib/types';

  let { data }: { data: PageData } = $props();

  const PAGE_SIZE = 100;

  let selectedBlog = $state<string>('all');
  let minSpiciness = $state(1);
  let currentPage = $state(1);

  let filtered = $derived.by(() => {
    let result = data.posts;
    if (selectedBlog !== 'all') {
      result = result.filter(p => p.blogId === selectedBlog);
    }
    if (minSpiciness > 1) {
      result = result.filter(
        p => p.spiciness !== null && p.spiciness >= minSpiciness
      );
    }
    return result;
  });

  let totalPages = $derived(Math.max(1, Math.ceil(filtered.length / PAGE_SIZE)));

  // Clamp page when filters reduce results
  let safePage = $derived(Math.min(currentPage, totalPages));

  let paged = $derived(
    filtered.slice((safePage - 1) * PAGE_SIZE, safePage * PAGE_SIZE)
  );

  let grouped = $derived.by(() => {
    const groups: { label: string; posts: typeof paged }[] = [];
    let currentLabel = '';
    let currentGroup: typeof paged = [];

    for (const post of paged) {
      if (!post.dateStr) continue;
      const d = new Date(post.dateStr);
      const label = d.toLocaleDateString('en-US', {
        month: 'long',
        year: 'numeric',
      });
      if (label !== currentLabel) {
        if (currentGroup.length > 0) {
          groups.push({ label: currentLabel, posts: currentGroup });
        }
        currentLabel = label;
        currentGroup = [post];
      } else {
        currentGroup.push(post);
      }
    }
    if (currentGroup.length > 0) {
      groups.push({ label: currentLabel, posts: currentGroup });
    }
    return groups;
  });

  function goToPage(page: number) {
    currentPage = page;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function formatFeedDate(dateStr: string | null): string {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    return d.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
    });
  }

  function truncate(text: string, max: number): string {
    if (!text || text.length <= max) return text || '';
    return text.slice(0, max) + '\u2026';
  }


</script>

<svelte:head>
  <title>The Spicy Feed</title>
  <meta name="description" content="The latest spicy takes from {data.authors.length} tech blogs, sorted by date" />
</svelte:head>

<div class="feed-page">
  <!-- Header -->
  <header class="feed-header">
    <div class="feed-header-inner">
      <a href="{base}/" class="back-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Spicy Takes
      </a>
      <div class="header-title-block">
        <h1 class="feed-title">The Spicy Feed</h1>
        <p class="feed-subtitle">
          {data.posts.length} recent posts across {data.authors.length} voices
        </p>
      </div>
    </div>
  </header>

  <!-- Sticky filter bar -->
  <div class="filter-bar">
    <div class="filter-bar-inner">
      <div class="filter-group">
        <label for="blog-filter" class="filter-label">Author</label>
        <div class="select-wrap">
          <select id="blog-filter" bind:value={selectedBlog} onchange={() => { currentPage = 1; }} class="filter-select">
            <option value="all">All</option>
            {#each data.authors as author}
              <option value={author.id}>{author.name}</option>
            {/each}
          </select>
          <svg class="select-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
        </div>
      </div>

      <div class="filter-divider"></div>

      <div class="filter-group">
        <label for="spiciness-filter" class="filter-label">Heat</label>
        <div class="range-wrap">
          <input
            id="spiciness-filter"
            type="range"
            min="1"
            max="10"
            step="1"
            bind:value={minSpiciness}
            oninput={() => { currentPage = 1; }}
            class="filter-range"
            style="--range-pct: {((minSpiciness - 1) / 9) * 100}%"
          />
          <span class="range-value" style="color: {heatColor(minSpiciness)}">{minSpiciness}+</span>
        </div>
      </div>

      <span class="filter-count">
        {#if totalPages > 1}
          {(safePage - 1) * PAGE_SIZE + 1}–{Math.min(safePage * PAGE_SIZE, filtered.length)} of {filtered.length}
        {:else}
          {filtered.length}
        {/if}
      </span>
    </div>
  </div>

  <!-- Feed content -->
  <main class="feed-main">
    {#if filtered.length === 0}
      <div class="empty-state">
        <p>No posts match your filters.</p>
        <button onclick={() => { selectedBlog = 'all'; minSpiciness = 1; }}>
          Reset filters
        </button>
      </div>
    {:else}
      {#each grouped as group, gi}
        <section class="month-group" style="--stagger: {gi}">
          <div class="month-header">
            <span class="month-label">{group.label}</span>
            <span class="month-count">{group.posts.length}</span>
          </div>

          <div class="posts-list">
            {#each group.posts as post, pi}
              <article
                class="post-card"
                style="--delay: {pi * 30}ms; --heat: {heatColor(post.spiciness ?? 5)}"
              >
                <!-- Heat strip -->
                <div class="heat-strip" aria-hidden="true"></div>

                <div class="post-body">
                  <!-- Author + date row -->
                  <div class="post-meta">
                    <img
                      src={post.authorPhoto}
                      alt=""
                      class="author-avatar"
                      onerror={(e) => { (e.currentTarget as HTMLImageElement).style.display = 'none'; }}
                    />
                    <span class="author-name">{post.authorName}</span>
                    <span class="meta-dot"></span>
                    <time class="post-date">{formatFeedDate(post.dateStr)}</time>
                    {#if post.spiciness !== null}
                      <span class="spicy-badge {getSpicyColor(post.spiciness)}">
                        {post.spiciness}
                      </span>
                    {/if}
                  </div>

                  <!-- Title -->
                  <h3 class="post-title">
                    <a href={post.spicytakesUrl} target="_blank" rel="noopener noreferrer">
                      {post.title}
                    </a>
                  </h3>

                  <!-- Key Insight -->
                  {#if post.key_insight}
                    <p class="post-insight"><strong>{post.key_insight}</strong></p>
                  {/if}

                  <!-- Summary -->
                  {#if post.summary}
                    <p class="post-summary">{truncate(post.summary, 240)}</p>
                  {/if}

                  <!-- Quotes -->
                  {#if post.topQuotes.length > 0}
                    <div class="quotes-section">
                      {#each post.topQuotes as q}
                        <blockquote class="feed-quote">
                          <span class="quote-score" style="color: {heatColor(q.spiciness)}">{q.spiciness}</span>
                          <p>{truncate(q.quote, 180)}</p>
                        </blockquote>
                      {/each}
                    </div>
                  {/if}

                  <!-- Action links -->
                  <div class="post-actions">
                    <a href={post.spicytakesUrl} target="_blank" rel="noopener noreferrer" class="action-primary">
                      Full analysis
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>
                    </a>
                    {#if post.sourceUrl}
                      <a href={post.sourceUrl} target="_blank" rel="noopener noreferrer" class="action-secondary">
                        Original
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                      </a>
                    {/if}
                  </div>
                </div>
              </article>
            {/each}
          </div>
        </section>
      {/each}
    {/if}

    <!-- Pagination -->
    {#if totalPages > 1}
      <nav class="pagination" aria-label="Feed pages">
        <button
          class="page-btn"
          disabled={safePage <= 1}
          onclick={() => goToPage(safePage - 1)}
          aria-label="Previous page"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg>
        </button>

        {#each Array.from({ length: totalPages }, (_, i) => i + 1) as page}
          {#if totalPages <= 7 || page === 1 || page === totalPages || (page >= safePage - 1 && page <= safePage + 1)}
            <button
              class="page-btn"
              class:active={page === safePage}
              onclick={() => goToPage(page)}
              aria-label="Page {page}"
              aria-current={page === safePage ? 'page' : undefined}
            >
              {page}
            </button>
          {:else if page === safePage - 2 || page === safePage + 2}
            <span class="page-ellipsis">...</span>
          {/if}
        {/each}

        <button
          class="page-btn"
          disabled={safePage >= totalPages}
          onclick={() => goToPage(safePage + 1)}
          aria-label="Next page"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
        </button>
      </nav>
    {/if}
  </main>

  <footer class="feed-footer">
    <p>
      Made with <span class="heart">&#10084;&#65039;</span> by
      <a href="https://wesmckinney.com" target="_blank" rel="noopener noreferrer">Wes McKinney</a>
    </p>
  </footer>
</div>

<style>
  /* ── Page shell ────────────────────────────────── */
  .feed-page {
    --filter-bar-height: 49px;
    min-height: 100vh;
    background: linear-gradient(180deg, #fafaf9 0%, #fff 40%);
  }

  /* ── Header ────────────────────────────────────── */
  .feed-header {
    padding: 2.5rem 1.5rem 1.75rem;
    border-bottom: 1px solid #e7e5e4;
    background:
      radial-gradient(ellipse 80% 60% at 50% -20%, rgba(239, 68, 68, 0.04), transparent),
      #fafaf9;
  }

  .feed-header-inner {
    max-width: 52rem;
    margin: 0 auto;
  }

  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.8rem;
    font-weight: 500;
    color: #78716c;
    text-decoration: none;
    letter-spacing: 0.02em;
    transition: color 0.15s;
  }
  .back-link:hover { color: #44403c; }
  .back-link svg { opacity: 0.6; }

  .header-title-block {
    margin-top: 0.75rem;
  }

  .feed-title {
    font-family: var(--font-family-serif);
    font-size: 2.5rem;
    font-weight: 600;
    color: #1c1917;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }

  .feed-subtitle {
    margin-top: 0.4rem;
    font-size: 0.9rem;
    color: #78716c;
    letter-spacing: 0.01em;
  }

  /* ── Filter bar ────────────────────────────────── */
  .filter-bar {
    position: sticky;
    top: 0;
    z-index: 20;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid #e7e5e4;
    box-shadow: 0 1px 3px rgba(28, 25, 23, 0.04);
  }

  .filter-bar-inner {
    max-width: 52rem;
    margin: 0 auto;
    padding: 0.6rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .filter-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .filter-label {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
  }

  .select-wrap {
    position: relative;
  }

  .filter-select {
    appearance: none;
    font-size: 0.8rem;
    font-weight: 500;
    color: #44403c;
    background: #f5f5f4;
    border: 1px solid #d6d3d1;
    border-radius: 0.5rem;
    padding: 0.35rem 1.75rem 0.35rem 0.65rem;
    cursor: pointer;
    transition: border-color 0.15s;
  }
  .filter-select:focus {
    outline: none;
    border-color: #ef4444;
    box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.1);
  }

  .select-chevron {
    position: absolute;
    right: 0.5rem;
    top: 50%;
    transform: translateY(-50%);
    color: #a8a29e;
    pointer-events: none;
  }

  .filter-divider {
    width: 1px;
    height: 1.25rem;
    background: #d6d3d1;
  }

  .range-wrap {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .filter-range {
    width: 5.5rem;
    height: 4px;
    appearance: none;
    -webkit-appearance: none;
    background: linear-gradient(
      to right,
      #ef4444 0%,
      #ef4444 var(--range-pct),
      #d6d3d1 var(--range-pct),
      #d6d3d1 100%
    );
    border-radius: 2px;
    cursor: pointer;
    outline: none;
  }
  .filter-range::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid #ef4444;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    cursor: pointer;
    transition: transform 0.1s;
  }
  .filter-range::-webkit-slider-thumb:hover {
    transform: scale(1.15);
  }
  .filter-range::-moz-range-thumb {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid #ef4444;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    cursor: pointer;
  }

  .range-value {
    font-size: 0.75rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    min-width: 1.5rem;
    text-align: center;
  }

  .filter-count {
    margin-left: auto;
    font-size: 0.75rem;
    font-weight: 500;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  /* ── Main feed ─────────────────────────────────── */
  .feed-main {
    max-width: 52rem;
    margin: 0 auto;
    padding: 0 1.5rem 4rem;
  }

  /* ── Empty state ───────────────────────────────── */
  .empty-state {
    text-align: center;
    padding: 5rem 0;
    color: #78716c;
    font-size: 0.9rem;
  }
  .empty-state button {
    margin-top: 0.75rem;
    font-size: 0.8rem;
    color: #ef4444;
    background: none;
    border: none;
    cursor: pointer;
    text-decoration: underline;
    text-underline-offset: 2px;
  }

  /* ── Month groups ──────────────────────────────── */
  .month-group {
    margin-top: 2.5rem;
  }
  .month-group:first-child {
    margin-top: 1.5rem;
  }

  .month-header {
    position: sticky;
    top: var(--filter-bar-height);
    z-index: 10;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 0;
    margin-bottom: 0.75rem;
    background: rgba(250, 250, 249, 0.92);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
  }

  .month-label {
    font-family: var(--font-family-serif);
    font-size: 0.85rem;
    font-weight: 500;
    color: #57534e;
    letter-spacing: 0.01em;
  }

  .month-count {
    font-size: 0.65rem;
    font-weight: 600;
    color: #a8a29e;
    background: #f5f5f4;
    border-radius: 9999px;
    padding: 0.1rem 0.45rem;
    font-variant-numeric: tabular-nums;
  }

  /* ── Post cards ────────────────────────────────── */
  .posts-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .post-card {
    display: flex;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.75rem;
    overflow: hidden;
    transition: box-shadow 0.2s, border-color 0.2s;
    animation: card-in 0.35s ease-out both;
    animation-delay: var(--delay);
  }
  .post-card:hover {
    border-color: #d6d3d1;
    box-shadow:
      0 4px 12px rgba(28, 25, 23, 0.06),
      0 1px 3px rgba(28, 25, 23, 0.04);
  }

  @keyframes card-in {
    from {
      opacity: 0;
      transform: translateY(8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .heat-strip {
    width: 3px;
    flex-shrink: 0;
    background: var(--heat);
    border-radius: 3px 0 0 3px;
    opacity: 0.7;
    transition: opacity 0.2s;
  }
  .post-card:hover .heat-strip {
    opacity: 1;
  }

  .post-body {
    flex: 1;
    min-width: 0;
    padding: 1rem 1.25rem;
  }

  /* ── Post meta ─────────────────────────────────── */
  .post-meta {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    margin-bottom: 0.5rem;
  }

  .author-avatar {
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid #e7e5e4;
    flex-shrink: 0;
  }

  .author-name {
    font-size: 0.78rem;
    font-weight: 600;
    color: #44403c;
  }

  .meta-dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #d6d3d1;
    flex-shrink: 0;
  }

  .post-date {
    font-size: 0.75rem;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  .spicy-badge {
    margin-left: auto;
    font-size: 0.65rem;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 9999px;
    flex-shrink: 0;
  }

  /* ── Title ─────────────────────────────────────── */
  .post-title {
    font-size: 1.05rem;
    font-weight: 700;
    line-height: 1.35;
    color: #1c1917;
    margin-bottom: 0.35rem;
  }
  .post-title a {
    text-decoration: none;
    color: inherit;
    transition: color 0.15s;
  }
  .post-title a:hover {
    color: #dc2626;
  }

  /* ── Summary ───────────────────────────────────── */
  .post-insight {
    font-size: 0.85rem;
    line-height: 1.55;
    color: #1c1917;
    margin-bottom: 0.5rem;
  }

  .post-summary {
    font-size: 0.835rem;
    line-height: 1.6;
    color: #57534e;
    margin-bottom: 0.6rem;
  }

  /* ── Quotes ────────────────────────────────────── */
  .quotes-section {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    margin-bottom: 0.6rem;
    padding-left: 0.25rem;
    border-left: 2px solid #f5f5f4;
  }

  .feed-quote {
    display: flex;
    align-items: baseline;
    gap: 0.45rem;
    margin: 0;
    padding: 0.2rem 0;
  }

  .quote-score {
    font-size: 0.65rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
    opacity: 0.85;
  }

  .feed-quote p {
    font-family: var(--font-family-serif);
    font-size: 0.82rem;

    line-height: 1.55;
    color: #44403c;
    margin: 0;
  }

  /* ── Actions ───────────────────────────────────── */
  .post-actions {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding-top: 0.5rem;
    border-top: 1px solid #f5f5f4;
  }

  .action-primary,
  .action-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.75rem;
    font-weight: 600;
    text-decoration: none;
    transition: color 0.15s;
  }

  .action-primary {
    color: #dc2626;
  }
  .action-primary:hover {
    color: #b91c1c;
  }

  .action-secondary {
    color: #a8a29e;
  }
  .action-secondary:hover {
    color: #57534e;
  }

  /* ── Pagination ─────────────────────────────────── */
  .pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.25rem;
    margin-top: 2.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid #e7e5e4;
  }

  .page-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 2rem;
    height: 2rem;
    padding: 0 0.5rem;
    font-size: 0.8rem;
    font-weight: 500;
    color: #57534e;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: all 0.15s;
    font-variant-numeric: tabular-nums;
  }
  .page-btn:hover:not(:disabled):not(.active) {
    border-color: #d6d3d1;
    background: #f5f5f4;
  }
  .page-btn:disabled {
    opacity: 0.35;
    cursor: default;
  }
  .page-btn.active {
    background: #1c1917;
    color: #fff;
    border-color: #1c1917;
  }

  .page-ellipsis {
    font-size: 0.8rem;
    color: #a8a29e;
    padding: 0 0.15rem;
    user-select: none;
  }

  /* ── Footer ────────────────────────────────────── */
  .feed-footer {
    border-top: 1px solid #e7e5e4;
    padding: 2rem 1.5rem;
    text-align: center;
    font-size: 0.8rem;
    color: #a8a29e;
  }
  .feed-footer a {
    color: #78716c;
    text-decoration: none;
    transition: color 0.15s;
  }
  .feed-footer a:hover { color: #dc2626; }
  .feed-footer .heart { color: #ef4444; }

  /* ── Responsive ────────────────────────────────── */
  @media (max-width: 640px) {
    .feed-title {
      font-size: 1.75rem;
    }

    .filter-bar-inner {
      gap: 0.6rem;
      padding: 0.5rem 1rem;
    }

    .filter-bar-inner {
      flex-wrap: wrap;
    }

    .feed-page {
      --filter-bar-height: 85px;
    }

    .filter-select {
      max-width: 8rem;
      text-overflow: ellipsis;
    }

    .filter-range {
      width: 4rem;
    }

    .post-body {
      padding: 0.75rem 1rem;
    }

    .post-title {
      font-size: 0.95rem;
    }

    .feed-quote p {
      font-size: 0.78rem;
    }
  }
</style>
