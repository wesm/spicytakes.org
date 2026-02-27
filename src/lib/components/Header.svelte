<script lang="ts">
  import { searchQuery, activeThemes, clearFilters, themesStore } from '$lib/stores';
  import { base } from '$app/paths';
  import { config, landing } from '$lib/config';

  // Look up blogger photo from landing config
  const bloggerPhoto = landing.blogs.find(b => b.id === config?.id)?.photo;

  let searchValue = $state('');
  let searchTimeout: ReturnType<typeof setTimeout>;

  // Sync local searchValue with store (for when clearFilters is called)
  $effect(() => {
    if ($searchQuery === '' && searchValue !== '') {
      searchValue = '';
    }
  });

  function handleSearch(e: Event) {
    const value = (e.target as HTMLInputElement).value;
    searchValue = value;
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      searchQuery.set(value);
    }, 200);
  }

  function toggleTheme(theme: string) {
    activeThemes.update(themes => {
      const newThemes = new Set(themes);
      if (newThemes.has(theme)) {
        newThemes.delete(theme);
      } else {
        newThemes.add(theme);
      }
      return newThemes;
    });
  }
</script>

<header class="site-header">
  <div class="header-inner">
    <!-- Top bar -->
    <div class="header-top">
      <div class="header-identity">
        <a href="https://spicytakes.org" class="logo-link" aria-label="Spicy Takes home">
          <img src={`${base}/logo.jpeg`} alt="" aria-hidden="true" class="logo" />
        </a>
        <span class="divider"></span>
        {#if bloggerPhoto}
          <img src={`${base}${bloggerPhoto}`} alt={config?.name} class="author-photo" />
        {/if}
        <div class="name-block">
          <h1 class="blog-name">{config?.name}</h1>
          <span class="blog-tagline">{config?.tagline}</span>
        </div>
      </div>
      <a href={config?.sourceUrl} target="_blank" rel="noopener noreferrer" class="source-link">
        {config?.sourceLabel}
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/></svg>
      </a>
    </div>

    <!-- Search and filters -->
    <div class="header-filters">
      <div class="search-wrap">
        <svg class="search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <circle cx="11" cy="11" r="8"/>
          <path d="m21 21-4.35-4.35"/>
        </svg>
        <input
          type="text"
          placeholder="Search posts, quotes, insights..."
          value={searchValue}
          oninput={handleSearch}
          class="search-input"
        />
      </div>

      <div class="theme-pills">
        {#each $themesStore as theme}
          <button
            onclick={() => toggleTheme(theme.name)}
            class="theme-pill"
            class:active={$activeThemes.has(theme.name)}
          >
            <span class="pill-icon">{theme.icon}</span>
            {theme.label}
            <span class="pill-count">({theme.posts.length})</span>
          </button>
        {/each}
        {#if $activeThemes.size > 0 || $searchQuery}
          <button onclick={clearFilters} class="clear-btn">
            Clear filters
          </button>
        {/if}
      </div>
    </div>
  </div>
</header>

<style>
  .site-header {
    position: sticky;
    top: 0;
    z-index: 50;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid #e7e5e4;
    box-shadow: 0 1px 3px rgba(28, 25, 23, 0.04);
  }

  .header-inner {
    max-width: 60rem;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  /* ── Top bar ──────────────────────────────────── */
  .header-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 0;
  }

  .header-identity {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    min-width: 0;
  }

  .logo-link {
    flex-shrink: 0;
    transition: opacity 0.15s;
  }
  .logo-link:hover { opacity: 0.75; }

  .logo {
    width: 1.75rem;
    height: 1.75rem;
    border-radius: 0.35rem;
  }

  .divider {
    width: 1px;
    height: 1.25rem;
    background: #d6d3d1;
    flex-shrink: 0;
  }

  .author-photo {
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid #e7e5e4;
    flex-shrink: 0;
  }

  .name-block {
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    min-width: 0;
  }

  .blog-name {
    font-size: 1rem;
    font-weight: 700;
    color: #1c1917;
    letter-spacing: -0.01em;
    white-space: nowrap;
  }

  .blog-tagline {
    font-size: 0.78rem;
    color: #a8a29e;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .source-link {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.75rem;
    font-weight: 500;
    color: #78716c;
    text-decoration: none;
    flex-shrink: 0;
    transition: color 0.15s;
  }
  .source-link:hover {
    color: #dc2626;
  }

  /* ── Search + filters ─────────────────────────── */
  .header-filters {
    padding-bottom: 0.6rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .search-wrap {
    position: relative;
    max-width: 20rem;
  }

  .search-icon {
    position: absolute;
    left: 0.6rem;
    top: 50%;
    transform: translateY(-50%);
    color: #a8a29e;
    pointer-events: none;
  }

  .search-input {
    width: 100%;
    padding: 0.4rem 0.75rem 0.4rem 2rem;
    font-size: 0.8rem;
    color: #44403c;
    background: #f5f5f4;
    border: 1px solid #e7e5e4;
    border-radius: 0.5rem;
    outline: none;
    transition: border-color 0.15s, box-shadow 0.15s;
  }
  .search-input::placeholder {
    color: #a8a29e;
  }
  .search-input:focus {
    border-color: #ef4444;
    box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.1);
  }

  .theme-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
  }

  .theme-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.15rem;
    padding: 0.2rem 0.6rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 500;
    background: #f5f5f4;
    color: #78716c;
    border: 1px solid transparent;
    cursor: pointer;
    transition: all 0.12s;
  }
  .theme-pill:hover {
    background: #e7e5e4;
    color: #44403c;
  }
  .theme-pill.active {
    background: #1c1917;
    color: #fff;
    border-color: #1c1917;
  }

  .pill-icon {
    font-size: 0.7rem;
  }

  .pill-count {
    opacity: 0.55;
    font-size: 0.68rem;
  }

  .clear-btn {
    display: inline-flex;
    align-items: center;
    padding: 0.2rem 0.6rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 500;
    background: rgba(239, 68, 68, 0.06);
    color: #dc2626;
    border: none;
    cursor: pointer;
    transition: background 0.12s;
  }
  .clear-btn:hover {
    background: rgba(239, 68, 68, 0.12);
  }

  /* ── Responsive ───────────────────────────────── */
  @media (max-width: 640px) {
    .blog-tagline,
    .source-link { display: none; }
    .search-wrap { max-width: 100%; }
  }
</style>
