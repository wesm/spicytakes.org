<script lang="ts">
  import { selectedPost } from '$lib/stores';
  import { THEME_LABELS, getSourceUrl, getSourceLabel, config, formatDate } from '$lib/config';

  function close() {
    selectedPost.set(null);
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape') close();
  }

  function heatColor(spiciness: number): string {
    if (spiciness >= 9) return '#dc2626';
    if (spiciness >= 7) return '#ea580c';
    if (spiciness >= 5) return '#d97706';
    if (spiciness >= 3) return '#65a30d';
    return '#16a34a';
  }
</script>

<svelte:window on:keydown={handleKeydown} />

{#if $selectedPost}
  {@const sourceUrl = getSourceUrl($selectedPost.filename, $selectedPost)}
  <div class="modal-overlay">
    <!-- Backdrop -->
    <button
      class="backdrop"
      onclick={close}
      aria-label="Close modal"
    ></button>

    <!-- Modal content -->
    <div class="modal-panel">
      <!-- Close button -->
      <button
        onclick={close}
        aria-label="Close"
        class="close-btn"
      >
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>

      <div class="modal-body">
        <!-- Heat strip -->
        {#if $selectedPost.spiciness != null}
          <div class="modal-heat" style="--heat: {heatColor($selectedPost.spiciness)}"></div>
        {/if}

        <div class="modal-content">
          <!-- Date, Link, and Spiciness -->
          <div class="meta-row">
            <div class="meta-left">
              <span class="meta-date">
                {formatDate($selectedPost.date)}
              </span>
              {#if sourceUrl}
                <span class="meta-dot"></span>
                <a
                  href={sourceUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="meta-source"
                >
                  {getSourceLabel($selectedPost)}
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>
                </a>
              {/if}
            </div>
            {#if $selectedPost.spiciness != null}
              <span class="spiciness-badge" style="color: {heatColor($selectedPost.spiciness)}">
                {$selectedPost.spiciness}
              </span>
            {/if}
          </div>

          <!-- Title -->
          <h2 class="modal-title">
            {$selectedPost.title}
            <a
              href="/post/{$selectedPost.filename}"
              onclick={close}
              class="permalink-btn"
              title="Open permalink page"
            >
              <svg width="13" height="13" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/>
              </svg>
              Permalink
            </a>
          </h2>

          <!-- Themes -->
          {#if $selectedPost.themes?.length}
            <div class="theme-list">
              {#each $selectedPost.themes as theme}
                <span class="theme-tag">
                  {THEME_LABELS[theme] || theme}
                </span>
              {/each}
            </div>
          {/if}

          <!-- Summary -->
          <div class="section">
            <h3 class="section-label">Summary</h3>
            <p class="section-text">
              {$selectedPost.summary}
            </p>
          </div>

          <!-- Key Insight -->
          {#if $selectedPost.key_insight}
            <div class="section">
              <h3 class="section-label">Key Insight</h3>
              <blockquote class="insight-quote">
                {$selectedPost.key_insight}
              </blockquote>
            </div>
          {/if}

          <!-- Money Quotes -->
          {#if $selectedPost.money_quotes?.length}
            <div class="section">
              <h3 class="section-label">
                Spicy Quotes
                <span class="section-hint">(click to share)</span>
              </h3>
              <ul class="quote-list">
                {#each $selectedPost.money_quotes as quote, i}
                  <li>
                    <a
                      href="/post/{$selectedPost.filename}#quote-{i}"
                      onclick={close}
                      class="quote-item"
                    >
                      <span class="quote-mark">"</span>
                      <p class="quote-text">{quote}</p>
                    </a>
                  </li>
                {/each}
              </ul>
            </div>
          {/if}

          <!-- Tone -->
          {#if $selectedPost.tone}
            <div class="section">
              <h3 class="section-label">Tone</h3>
              <p class="section-text muted">{$selectedPost.tone}</p>
            </div>
          {/if}
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .modal-overlay {
    position: fixed;
    inset: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
  }

  .backdrop {
    position: absolute;
    inset: 0;
    background: rgba(28, 25, 23, 0.5);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    border: none;
    cursor: pointer;
  }

  .modal-panel {
    position: relative;
    background: #fff;
    border-radius: 0.75rem;
    box-shadow:
      0 20px 60px rgba(28, 25, 23, 0.15),
      0 4px 16px rgba(28, 25, 23, 0.08);
    max-width: 42rem;
    width: 100%;
    max-height: 85vh;
    overflow-y: auto;
    animation: modal-in 0.2s ease;
  }

  @keyframes modal-in {
    from { opacity: 0; transform: scale(0.97) translateY(4px); }
    to { opacity: 1; transform: scale(1) translateY(0); }
  }

  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    width: 2rem;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: #f5f5f4;
    color: #78716c;
    border: none;
    cursor: pointer;
    transition: background 0.12s, color 0.12s;
    z-index: 1;
  }
  .close-btn:hover {
    background: #e7e5e4;
    color: #44403c;
  }

  .modal-body {
    display: flex;
  }

  .modal-heat {
    width: 4px;
    flex-shrink: 0;
    background: var(--heat);
    border-radius: 0.75rem 0 0 0.75rem;
  }

  .modal-content {
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
    font-size: 1.25rem;
    font-weight: 800;
    font-variant-numeric: tabular-nums;
  }

  /* ── Title ─────────────────────────────────── */
  .modal-title {
    font-family: var(--font-family-serif);
    font-size: 1.35rem;
    font-weight: 600;
    color: #1c1917;
    line-height: 1.35;
    margin-bottom: 1rem;
    padding-right: 2rem;
  }

  .permalink-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    margin-left: 0.5rem;
    padding: 0.15rem 0.5rem;
    border-radius: 0.25rem;
    background: #f5f5f4;
    color: #a8a29e;
    font-family: var(--font-family-sans, sans-serif);
    font-size: 0.7rem;
    font-weight: 500;
    text-decoration: none;
    vertical-align: middle;
    transition: background 0.12s, color 0.12s;
  }
  .permalink-btn:hover {
    background: #e7e5e4;
    color: #57534e;
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
    font-size: 1rem;
    font-style: italic;
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
    display: block;
    position: relative;
    padding: 0.75rem 1rem 0.75rem 1.75rem;
    background: #fafaf9;
    border: 1px solid #f5f5f4;
    border-radius: 0.5rem;
    text-decoration: none;
    transition: background 0.12s, border-color 0.12s,
      box-shadow 0.12s;
    cursor: pointer;
  }
  .quote-item:hover {
    background: #f5f5f4;
    border-color: #e7e5e4;
    box-shadow: 0 2px 6px rgba(28, 25, 23, 0.04);
  }

  .quote-mark {
    position: absolute;
    left: 0.5rem;
    top: 0.35rem;
    font-family: var(--font-family-serif);
    font-size: 1.5rem;
    color: #d6d3d1;
    line-height: 1;
  }

  .quote-text {
    font-family: var(--font-family-serif);
    font-size: 1rem;
    font-style: italic;
    line-height: 1.55;
    color: #1c1917;
    margin: 0;
  }

  /* ── Responsive ────────────────────────────── */
  @media (max-width: 640px) {
    .modal-content {
      padding: 1.5rem;
    }
    .modal-title {
      font-size: 1.15rem;
    }
  }

  @media (min-width: 1024px) {
    .modal-panel {
      max-width: 52rem;
    }
  }
</style>
