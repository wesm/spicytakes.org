<script lang="ts">
  import { filteredQuotes, selectedPost, yearsStore } from '$lib/stores';
  import { filterQuotes } from '$lib/filter';
  import { formatDate } from '$lib/config';
  import { heatColor, type Quote } from '$lib/types';

  let sortBy = $state<'date' | 'spiciness'>('date');
  let selectedYear = $state<number | null | 'all'>('all');
  let minSpiciness = $state(1);

  function openPost(quote: Quote) {
    selectedPost.set(quote.post);
  }

  let displayQuotes = $derived.by(() => {
    let result = filterQuotes($filteredQuotes, minSpiciness, selectedYear);

    if (sortBy === 'spiciness') {
      result = [...result].sort((a, b) => b.spiciness - a.spiciness);
    } else {
      result = [...result].sort(
        (a, b) => (b.date?.getTime() ?? 0) - (a.date?.getTime() ?? 0)
      );
    }

    return result;
  });

  let spiciestByYear = $derived.by(() => {
    const result: Record<string, Quote[]> = {};
    for (const year of $yearsStore) {
      const yearKey = year === null ? 'undated' : String(year);
      const yearQuotes = filterQuotes($filteredQuotes, minSpiciness, year);
      result[yearKey] = [...yearQuotes]
        .sort((a, b) => b.spiciness - a.spiciness)
        .slice(0, 5);
    }
    return result;
  });


</script>

<div class="quotes-view">
  <!-- Controls -->
  <div class="controls">
    <div class="control-group">
      <label for="sort-select" class="control-label">Sort</label>
      <div class="select-wrap">
        <select id="sort-select" bind:value={sortBy} class="control-select">
          <option value="date">Chronological</option>
          <option value="spiciness">Spiciest First</option>
        </select>
        <svg class="select-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
      </div>
    </div>

    <div class="control-group">
      <label for="year-select" class="control-label">Year</label>
      <div class="select-wrap">
        <select id="year-select" bind:value={selectedYear} class="control-select">
          <option value={'all'}>All</option>
          {#each $yearsStore as year}
            <option value={year}>{year === null ? 'Undated' : year}</option>
          {/each}
        </select>
        <svg class="select-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
      </div>
    </div>

    <div class="control-group">
      <label for="spice-range" class="control-label">Heat</label>
      <div class="range-wrap">
        <input
          id="spice-range"
          type="range"
          min="1" max="10" step="1"
          bind:value={minSpiciness}
          class="control-range"
          style="--range-pct: {((minSpiciness - 1) / 9) * 100}%"
        />
        <span class="range-value" style="color: {heatColor(minSpiciness)}">{minSpiciness}+</span>
      </div>
    </div>

    <span class="control-count">{displayQuotes.length}</span>
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
          <div class="quote-list">
            {#each yearSpicy as quote}
              <button onclick={() => openPost(quote)} class="quote-card" style="--heat: {heatColor(quote.spiciness)}">
                <div class="card-heat" aria-hidden="true"></div>
                <div class="card-body">
                  <div class="card-top">
                    <blockquote class="card-quote">{quote.quote}</blockquote>
                    <span class="card-score" style="color: {heatColor(quote.spiciness)}">{quote.spiciness}</span>
                  </div>
                  <div class="card-meta">
                    <span class="card-source">{quote.post.title}</span>
                    <time class="card-date">{formatDate(quote.date, 'short')}</time>
                  </div>
                </div>
              </button>
            {/each}
          </div>
        </section>
      {/if}
    {/each}
  {:else if displayQuotes.length === 0}
    <div class="empty-state">
      <p class="empty-title">No quotes found</p>
      <p class="empty-hint">Try adjusting your filters</p>
    </div>
  {:else}
    <div class="quote-list">
      {#each displayQuotes as quote, i (quote.quote + quote.post.filename + i)}
        <button onclick={() => openPost(quote)} class="quote-card" style="--heat: {heatColor(quote.spiciness)}">
          <div class="card-heat" aria-hidden="true"></div>
          <div class="card-body">
            <div class="card-top">
              <blockquote class="card-quote">{quote.quote}</blockquote>
              <span class="card-score" style="color: {heatColor(quote.spiciness)}">{quote.spiciness}</span>
            </div>
            <div class="card-meta">
              <span class="card-source">{quote.post.title}</span>
              <time class="card-date">{formatDate(quote.date, 'short')}</time>
              {#if quote.themes.length > 0}
                {#each quote.themes.slice(0, 2) as theme}
                  <span class="card-theme">{theme.replace(/_/g, ' ')}</span>
                {/each}
              {/if}
            </div>
          </div>
        </button>
      {/each}
    </div>
  {/if}
</div>

<style>
  .quotes-view {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  /* ── Controls (same as TimelineView) ─────────── */
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

  .select-wrap { position: relative; }

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
    width: 12px; height: 12px;
    border-radius: 50%;
    background: #fff;
    border: 2px solid #ef4444;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    cursor: pointer;
  }
  .control-range::-moz-range-thumb {
    width: 12px; height: 12px;
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

  .year-badge {
    font-size: 0.72rem;
    font-weight: 600;
    color: #dc2626;
    background: rgba(239, 68, 68, 0.06);
    border-radius: 9999px;
    padding: 0.1rem 0.45rem;
  }

  /* ── Quote cards ─────────────────────────────── */
  .quote-list {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
  }

  .quote-card {
    display: flex;
    text-align: left;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.6rem;
    overflow: hidden;
    cursor: pointer;
    transition: border-color 0.15s, box-shadow 0.15s;
  }
  .quote-card:hover {
    border-color: #d6d3d1;
    box-shadow: 0 2px 8px rgba(28, 25, 23, 0.06);
  }

  .card-heat {
    width: 3px;
    flex-shrink: 0;
    background: var(--heat);
    border-radius: 3px 0 0 3px;
    opacity: 0.6;
    transition: opacity 0.15s;
  }
  .quote-card:hover .card-heat {
    opacity: 1;
  }

  .card-body {
    flex: 1;
    min-width: 0;
    padding: 0.75rem 1rem;
  }

  .card-top {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    margin-bottom: 0.4rem;
  }

  .card-quote {
    font-family: var(--font-family-serif);
    font-size: 1rem;

    line-height: 1.55;
    color: #44403c;
    flex: 1;
    min-width: 0;
    margin: 0;
  }

  .card-score {
    font-size: 0.92rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
  }

  .card-meta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .card-source {
    font-size: 0.82rem;
    font-weight: 600;
    color: #57534e;
    transition: color 0.12s;
  }
  .quote-card:hover .card-source {
    color: #dc2626;
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

  @media (max-width: 640px) {
    .controls {
      flex-wrap: wrap;
      gap: 0.6rem;
    }
    .control-range { width: 3.5rem; }
  }
</style>
