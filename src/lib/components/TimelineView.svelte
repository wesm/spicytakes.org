<script lang="ts">
  import { filteredPosts, selectedPost, yearsStore } from '$lib/stores';
  import { filterPosts } from '$lib/filter';
  import { THEME_LABELS, formatDate } from '$lib/config';
  import { heatColor, type Post } from '$lib/types';

  function openPost(post: Post) {
    selectedPost.set(post);
  }

  function topQuotes(post: Post, n = 3) {
    return (post.money_quotes || [])
      .map((q, i) => ({
        quote: q,
        spiciness: post.quote_spiciness?.[i] ?? 5,
      }))
      .sort((a, b) => b.spiciness - a.spiciness)
      .slice(0, n);
  }

  function truncate(text: string, max: number): string {
    if (!text || text.length <= max) return text || '';
    return text.slice(0, max) + '\u2026';
  }

  let sortBy = $state<'date' | 'spiciness'>('date');
  let selectedYear = $state<number | null | 'all'>('all');
  let minSpiciness = $state(1);

  let displayPosts = $derived.by(() => {
    let result = filterPosts(
      $filteredPosts, minSpiciness,
      selectedYear === 'all' ? 'all' : selectedYear
    );

    if (sortBy === 'spiciness') {
      result = [...result].sort(
        (a, b) => (b.spiciness ?? 0) - (a.spiciness ?? 0)
      );
    } else {
      result = [...result].sort(
        (a, b) => (b.date?.getTime() ?? 0) - (a.date?.getTime() ?? 0)
      );
    }

    return result;
  });

  function getPostsByYear(posts: Post[]) {
    const byYear: Record<string, Post[]> = {};
    posts.forEach(post => {
      const yearKey = post.year == null ? 'undated' : String(post.year);
      if (!byYear[yearKey]) byYear[yearKey] = [];
      byYear[yearKey].push(post);
    });
    return Object.entries(byYear)
      .sort(([a], [b]) => {
        if (a === 'undated') return 1;
        if (b === 'undated') return -1;
        return Number(b) - Number(a);
      })
      .map(([year, posts]) => ({
        year: year === 'undated' ? null : Number(year), posts,
      }));
  }

  let groupedPosts = $derived(getPostsByYear(displayPosts));

  let spiciestByYear = $derived.by(() => {
    const result: Record<string, Post[]> = {};
    for (const year of $yearsStore) {
      const yearKey = year === null ? 'undated' : String(year);
      const yearPosts = displayPosts.filter(p => p.year === year);
      result[yearKey] = [...yearPosts]
        .sort((a, b) => (b.spiciness ?? 0) - (a.spiciness ?? 0))
        .slice(0, 5);
    }
    return result;
  });


</script>

<div class="timeline">
  <!-- Controls -->
  <div class="controls">
    <div class="control-group">
      <label for="timeline-sort" class="control-label">Sort</label>
      <div class="select-wrap">
        <select id="timeline-sort" bind:value={sortBy} class="control-select">
          <option value="date">Chronological</option>
          <option value="spiciness">Spiciest First</option>
        </select>
        <svg class="select-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
      </div>
    </div>

    <div class="control-group">
      <label for="timeline-year" class="control-label">Year</label>
      <div class="select-wrap">
        <select id="timeline-year" bind:value={selectedYear} class="control-select">
          <option value={'all'}>All</option>
          {#each $yearsStore as year}
            <option value={year}>{year === null ? 'Undated' : year}</option>
          {/each}
        </select>
        <svg class="select-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
      </div>
    </div>

    <div class="control-group">
      <label for="timeline-spice" class="control-label">Heat</label>
      <div class="range-wrap">
        <input
          id="timeline-spice"
          type="range"
          min="1" max="10" step="1"
          bind:value={minSpiciness}
          class="control-range"
          style="--range-pct: {((minSpiciness - 1) / 9) * 100}%"
        />
        <span class="range-value" style="color: {heatColor(minSpiciness)}">{minSpiciness}+</span>
      </div>
    </div>

    <span class="control-count">{displayPosts.length}</span>
  </div>

  {#if selectedYear === 'all' && sortBy === 'spiciness'}
    <!-- Spiciest per year -->
    {#each $yearsStore as year}
      {@const yearKey = year === null ? 'undated' : String(year)}
      {@const yearSpicy = spiciestByYear[yearKey]}
      {#if yearSpicy && yearSpicy.length > 0}
        <section class="year-section">
          <div class="year-header">
            <h3 class="year-label">{year === null ? 'Undated' : year}</h3>
            <span class="year-badge">Top 5</span>
          </div>
          <div class="post-list">
            {#each yearSpicy as post (post.filename)}
              {@const quotes = topQuotes(post)}
              <button onclick={() => openPost(post)} class="post-card" style="--heat: {heatColor(post.spiciness ?? 5)}">
                <div class="card-heat" aria-hidden="true"></div>
                <div class="card-body">
                  <div class="card-top">
                    <h4 class="card-title">{post.title}</h4>
                    {#if post.spiciness != null}
                      <span class="card-score" style="color: {heatColor(post.spiciness)}">{post.spiciness}</span>
                    {/if}
                  </div>
                  {#if post.key_insight}
                    <p class="card-insight"><strong>Key Insight:</strong> {post.key_insight}</p>
                  {/if}
                  {#if post.summary}
                    <p class="card-summary">{post.summary}</p>
                  {/if}
                  {#if quotes.length > 0}
                    <div class="card-quotes">
                      {#each quotes as q}
                        <blockquote class="card-quote">
                          <span class="card-quote-score" style="color: {heatColor(q.spiciness)}">{q.spiciness}</span>
                          <p>{truncate(q.quote, 180)}</p>
                        </blockquote>
                      {/each}
                    </div>
                  {/if}
                  <div class="card-meta">
                    <time class="card-date">{formatDate(post.date, 'short')}</time>
                    {#if post.themes?.length}
                      {#each post.themes.slice(0, 2) as theme}
                        <span class="card-theme">{THEME_LABELS[theme] || theme.replace(/_/g, ' ')}</span>
                      {/each}
                    {/if}
                  </div>
                </div>
              </button>
            {/each}
          </div>
        </section>
      {/if}
    {/each}
  {:else if displayPosts.length === 0}
    <div class="empty-state">
      <p class="empty-title">No posts found</p>
      <p class="empty-hint">Try adjusting your search or filters</p>
    </div>
  {:else}
    {#each groupedPosts as { year, posts }}
      <section class="year-section">
        <div class="year-header">
          <h3 class="year-label">{year === null ? 'Undated' : year}</h3>
          <span class="year-count">{posts.length}</span>
        </div>
        <div class="post-list">
          {#each posts as post (post.filename)}
            {@const quotes = topQuotes(post)}
            <button onclick={() => openPost(post)} class="post-card" style="--heat: {heatColor(post.spiciness ?? 5)}">
              <div class="card-heat" aria-hidden="true"></div>
              <div class="card-body">
                <div class="card-top">
                  <h4 class="card-title">{post.title}</h4>
                  {#if post.spiciness != null}
                    <span class="card-score" style="color: {heatColor(post.spiciness)}">{post.spiciness}</span>
                  {/if}
                </div>
                {#if post.key_insight}
                  <p class="card-insight"><strong>Key Insight:</strong> {post.key_insight}</p>
                {/if}
                {#if post.summary}
                  <p class="card-summary">{post.summary}</p>
                {/if}
                {#if quotes.length > 0}
                  <div class="card-quotes">
                    {#each quotes as q}
                      <blockquote class="card-quote">
                        <span class="card-quote-score" style="color: {heatColor(q.spiciness)}">{q.spiciness}</span>
                        <p>{truncate(q.quote, 180)}</p>
                      </blockquote>
                    {/each}
                  </div>
                {/if}
                <div class="card-meta">
                  <time class="card-date">{formatDate(post.date, 'short')}</time>
                  {#if post.themes?.length}
                    {#each post.themes.slice(0, 2) as theme}
                      <span class="card-theme">{THEME_LABELS[theme] || theme.replace(/_/g, ' ')}</span>
                    {/each}
                  {/if}
                </div>
              </div>
            </button>
          {/each}
        </div>
      </section>
    {/each}
  {/if}
</div>

<style>
  .timeline {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  /* ── Controls ────────────────────────────────── */
  .controls {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 0.5rem 0.75rem;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.6rem;
  }

  .control-group {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .control-label {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
  }

  .select-wrap {
    position: relative;
  }

  .control-select {
    appearance: none;
    font-size: 0.85rem;
    font-weight: 500;
    color: #44403c;
    background: #f5f5f4;
    border: 1px solid #d6d3d1;
    border-radius: 0.4rem;
    padding: 0.3rem 1.5rem 0.3rem 0.5rem;
    cursor: pointer;
    transition: border-color 0.15s;
  }
  .control-select:focus {
    outline: none;
    border-color: #ef4444;
    box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.1);
  }

  .select-chevron {
    position: absolute;
    right: 0.35rem;
    top: 50%;
    transform: translateY(-50%);
    color: #a8a29e;
    pointer-events: none;
  }

  .range-wrap {
    display: flex;
    align-items: center;
    gap: 0.35rem;
  }

  .control-range {
    width: 4.5rem;
    height: 4px;
    appearance: none;
    -webkit-appearance: none;
    background: linear-gradient(
      to right,
      #ef4444 0%, #ef4444 var(--range-pct),
      #d6d3d1 var(--range-pct), #d6d3d1 100%
    );
    border-radius: 2px;
    cursor: pointer;
    outline: none;
  }
  .control-range::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid #ef4444;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    cursor: pointer;
  }
  .control-range::-moz-range-thumb {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid #ef4444;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    cursor: pointer;
  }

  .range-value {
    font-size: 0.8rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    min-width: 1.5rem;
    text-align: center;
  }

  .control-count {
    margin-left: auto;
    font-size: 0.8rem;
    font-weight: 500;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  /* ── Year sections ───────────────────────────── */
  .year-section {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .year-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding-bottom: 0.35rem;
    border-bottom: 2px solid #1c1917;
  }

  .year-label {
    font-family: var(--font-family-serif);
    font-size: 1.2rem;
    font-weight: 600;
    color: #1c1917;
  }

  .year-count, .year-badge {
    font-size: 0.72rem;
    font-weight: 600;
    color: #a8a29e;
    background: #f5f5f4;
    border-radius: 9999px;
    padding: 0.1rem 0.45rem;
    font-variant-numeric: tabular-nums;
  }

  .year-badge {
    color: #dc2626;
    background: rgba(239, 68, 68, 0.06);
  }

  /* ── Post cards ──────────────────────────────── */
  .post-list {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .post-card {
    display: flex;
    text-align: left;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.75rem;
    overflow: hidden;
    cursor: pointer;
    transition: border-color 0.15s, box-shadow 0.15s;
  }
  .post-card:hover {
    border-color: #d6d3d1;
    box-shadow:
      0 4px 12px rgba(28, 25, 23, 0.06),
      0 1px 3px rgba(28, 25, 23, 0.04);
  }

  .card-heat {
    width: 3px;
    flex-shrink: 0;
    background: var(--heat);
    border-radius: 3px 0 0 3px;
    opacity: 0.7;
    transition: opacity 0.15s;
  }
  .post-card:hover .card-heat {
    opacity: 1;
  }

  .card-body {
    flex: 1;
    min-width: 0;
    padding: 1rem 1.25rem;
  }

  .card-top {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 0.35rem;
  }

  .card-title {
    font-family: var(--font-family-serif);
    font-size: 1.15rem;
    font-weight: 700;
    color: #1c1917;
    line-height: 1.35;
    transition: color 0.12s;
  }
  .post-card:hover .card-title {
    color: #dc2626;
  }

  .card-score {
    font-size: 0.85rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
  }

  .card-insight {
    font-size: 0.925rem;
    line-height: 1.55;
    color: #1c1917;
    margin-bottom: 0.5rem;
  }

  .card-summary {
    font-size: 0.9rem;
    line-height: 1.6;
    color: #57534e;
    margin-bottom: 0.6rem;
  }

  .card-quotes {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    margin-bottom: 0.6rem;
    padding-left: 0.25rem;
    border-left: 2px solid #f5f5f4;
  }

  .card-quote {
    display: flex;
    align-items: baseline;
    gap: 0.45rem;
    margin: 0;
    padding: 0.2rem 0;
  }

  .card-quote-score {
    font-size: 0.72rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
    opacity: 0.85;
  }

  .card-quote p {
    font-family: var(--font-family-serif);
    font-size: 0.9rem;
    line-height: 1.55;
    color: #44403c;
    margin: 0;
  }

  .card-meta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    padding-top: 0.5rem;
    border-top: 1px solid #f5f5f4;
  }

  .card-date {
    font-size: 0.8rem;
    color: #a8a29e;
  }

  .card-theme {
    font-size: 0.72rem;
    font-weight: 500;
    padding: 0.1rem 0.4rem;
    background: #f5f5f4;
    color: #78716c;
    border-radius: 0.25rem;
  }

  /* ── Empty state ─────────────────────────────── */
  .empty-state {
    text-align: center;
    padding: 4rem 0;
  }

  .empty-title {
    font-size: 1rem;
    color: #78716c;
  }

  .empty-hint {
    font-size: 0.9rem;
    color: #a8a29e;
    margin-top: 0.25rem;
  }

  /* ── Responsive ──────────────────────────────── */
  @media (max-width: 640px) {
    .controls {
      flex-wrap: wrap;
      gap: 0.6rem;
    }

    .control-range {
      width: 3.5rem;
    }

    .card-body {
      padding: 0.75rem 1rem;
    }

    .card-title {
      font-size: 0.95rem;
    }

    .card-quote p {
      font-size: 0.78rem;
    }
  }
</style>
