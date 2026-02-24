<script lang="ts">
  import { activeThemes, activeView, themesStore } from '$lib/stores';
  import type { ThemeData } from '$lib/types';

  function selectTheme(themeName: string) {
    activeThemes.set(new Set([themeName]));
    activeView.set('quotes');
  }

  function getTopSpicy(theme: ThemeData) {
    return [...theme.quotes]
      .sort((a, b) => b.spiciness - a.spiciness)
      .slice(0, 3);
  }

  function getAvgSpiciness(theme: ThemeData) {
    if (theme.quotes.length === 0) return 0;
    const total = theme.quotes.reduce((sum, q) => sum + q.spiciness, 0);
    return Math.round(total / theme.quotes.length * 10) / 10;
  }

  function heatColor(spiciness: number): string {
    if (spiciness >= 7) return '#dc2626';
    if (spiciness >= 6) return '#ea580c';
    if (spiciness >= 5) return '#d97706';
    return '#78716c';
  }
</script>

<div class="themes-view">
  <p class="themes-hint">Click a theme to view its spiciest quotes</p>

  <div class="themes-grid">
    {#each $themesStore as theme}
      {@const topSpicy = getTopSpicy(theme)}
      {@const avgSpice = getAvgSpiciness(theme)}
      <button onclick={() => selectTheme(theme.name)} class="theme-card">
        <div class="card-header">
          <div class="card-identity">
            <span class="card-icon">{theme.icon}</span>
            <div>
              <h3 class="card-name">{theme.label}</h3>
              <p class="card-counts">{theme.posts.length} posts, {theme.quotes.length} quotes</p>
            </div>
          </div>
          <div class="card-avg">
            <span class="avg-label">Avg</span>
            <span class="avg-value" style="color: {heatColor(avgSpice)}">{avgSpice}</span>
          </div>
        </div>

        <div class="card-quotes">
          <span class="quotes-label">Top Spicy Takes</span>
          {#each topSpicy as q}
            <div class="mini-quote">
              <span class="mini-score" style="color: {heatColor(q.spiciness)}">{q.spiciness}</span>
              <p class="mini-text">{q.quote}</p>
            </div>
          {/each}
        </div>

        <div class="card-cta">
          View all {theme.quotes.length} quotes
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </div>
      </button>
    {/each}
  </div>
</div>

<style>
  .themes-view {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .themes-hint {
    font-size: 0.78rem;
    color: #a8a29e;
  }

  .themes-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
  }

  .theme-card {
    text-align: left;
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.6rem;
    padding: 1rem 1.25rem;
    cursor: pointer;
    transition: border-color 0.15s, box-shadow 0.15s;
  }
  .theme-card:hover {
    border-color: #d6d3d1;
    box-shadow: 0 2px 8px rgba(28, 25, 23, 0.06);
  }

  .card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 0.75rem;
  }

  .card-identity {
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .card-icon {
    font-size: 1.25rem;
    flex-shrink: 0;
  }

  .card-name {
    font-size: 0.9rem;
    font-weight: 600;
    color: #1c1917;
    transition: color 0.12s;
  }
  .theme-card:hover .card-name {
    color: #dc2626;
  }

  .card-counts {
    font-size: 0.72rem;
    color: #a8a29e;
    margin-top: 0.1rem;
  }

  .card-avg {
    text-align: right;
    flex-shrink: 0;
  }

  .avg-label {
    display: block;
    font-size: 0.6rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
  }

  .avg-value {
    font-size: 1.1rem;
    font-weight: 800;
    font-variant-numeric: tabular-nums;
  }

  .card-quotes {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    border-top: 1px solid #f5f5f4;
    padding-top: 0.6rem;
  }

  .quotes-label {
    font-size: 0.6rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
    margin-bottom: 0.15rem;
  }

  .mini-quote {
    display: flex;
    align-items: baseline;
    gap: 0.4rem;
  }

  .mini-score {
    font-size: 0.65rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
  }

  .mini-text {
    font-family: var(--font-family-serif);
    font-size: 0.78rem;
    font-style: italic;
    line-height: 1.45;
    color: #78716c;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    line-clamp: 2;
    margin: 0;
  }

  .card-cta {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    margin-top: 0.75rem;
    font-size: 0.75rem;
    font-weight: 600;
    color: #dc2626;
    transition: color 0.12s;
  }
  .theme-card:hover .card-cta {
    color: #b91c1c;
  }

  @media (max-width: 768px) {
    .themes-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
