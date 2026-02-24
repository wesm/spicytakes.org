<script lang="ts">
  import { onMount } from 'svelte';
  import { base } from '$app/paths';
  import { landing } from '$lib/config';
  import type { BlogCard } from '$lib/types';

  let { blogSpiciness }: { blogSpiciness: Record<string, number | null> } = $props();

  type SortKey = 'name' | 'posts' | 'quotes' | 'spiciness';
  type SortDir = 'asc' | 'desc';

  function shuffle<T>(array: T[]): T[] {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  }

  const blogs = landing.blogs.filter(b => !b.hidden);

  // Random order stored once on mount
  let randomOrder: BlogCard[] = $state(blogs);

  let sortKey = $state<SortKey | null>(null);
  let sortDir = $state<SortDir>('desc');

  onMount(() => {
    randomOrder = shuffle(blogs);
  });

  function toggleSort(key: SortKey) {
    const defaultDir: SortDir = key === 'name' ? 'asc' : 'desc';
    const reverseDir: SortDir = defaultDir === 'asc' ? 'desc' : 'asc';
    if (sortKey === key) {
      if (sortDir === defaultDir) {
        sortDir = reverseDir;
      } else {
        sortKey = null;
      }
    } else {
      sortKey = key;
      sortDir = defaultDir;
    }
  }

  let visibleBlogs = $derived.by(() => {
    if (sortKey === null) return randomOrder;
    const sorted = [...randomOrder];
    const dir = sortDir === 'asc' ? 1 : -1;
    switch (sortKey) {
      case 'name':
        sorted.sort((a, b) => dir * a.name.localeCompare(b.name));
        break;
      case 'posts':
        sorted.sort((a, b) => dir * (a.stats.posts - b.stats.posts));
        break;
      case 'quotes':
        sorted.sort((a, b) => dir * (a.stats.quotes - b.stats.quotes));
        break;
      case 'spiciness':
        sorted.sort((a, b) => {
          const av = blogSpiciness[a.id];
          const bv = blogSpiciness[b.id];
          if (av == null && bv == null) return 0;
          if (av == null) return 1;
          if (bv == null) return -1;
          return dir * (av - bv);
        });
        break;
    }
    return sorted;
  });

  function heatColor(spiciness: number): string {
    if (spiciness >= 7) return '#dc2626';
    if (spiciness >= 6) return '#ea580c';
    if (spiciness >= 5) return '#d97706';
    return '#78716c';
  }

  const totalPosts = blogs.reduce((s, b) => s + b.stats.posts, 0);
  const totalQuotes = blogs.reduce((s, b) => s + b.stats.quotes, 0);
</script>

<div class="landing">
  <!-- Hero -->
  <header class="hero">
    <div class="hero-inner">
      <div class="logo-row">
        <img src={`${base}/logo.jpeg`} alt="" aria-hidden="true" class="logo" />
        <h1 class="site-title">{landing.title}</h1>
      </div>
      <p class="tagline">{landing.tagline}</p>
      <p class="description">{landing.description}</p>

      <div class="hero-stats">
        <span>{blogs.length} blogs</span>
        <span class="stat-dot"></span>
        <span>{totalPosts.toLocaleString()} posts</span>
        <span class="stat-dot"></span>
        <span>{totalQuotes.toLocaleString()} quotes</span>
      </div>

      <div class="hero-actions">
        <a href="{base}/feed" class="btn-primary">
          Latest Takes
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="{base}/analytics" class="btn-secondary">
          Analytics
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </header>

  <!-- Blog list -->
  <section class="blog-list-section">
    <div class="blog-list-inner">
      <div class="list-header" role="row">
        <button class="col-header col-name" class:active={sortKey === 'name'} onclick={() => toggleSort('name')}>
          Author
          <span class="sort-icon" class:asc={sortKey === 'name' && sortDir === 'asc'} class:desc={sortKey === 'name' && sortDir === 'desc'}>
            <svg width="10" height="10" viewBox="0 0 10 10"><path d="M5 2L8 6H2Z" fill="currentColor"/></svg>
          </span>
        </button>
        <span class="col-header col-tagline">Focus</span>
        <button class="col-header col-posts" class:active={sortKey === 'posts'} onclick={() => toggleSort('posts')}>
          Posts
          <span class="sort-icon" class:asc={sortKey === 'posts' && sortDir === 'asc'} class:desc={sortKey === 'posts' && sortDir === 'desc'}>
            <svg width="10" height="10" viewBox="0 0 10 10"><path d="M5 2L8 6H2Z" fill="currentColor"/></svg>
          </span>
        </button>
        <button class="col-header col-quotes" class:active={sortKey === 'quotes'} onclick={() => toggleSort('quotes')}>
          Quotes
          <span class="sort-icon" class:asc={sortKey === 'quotes' && sortDir === 'asc'} class:desc={sortKey === 'quotes' && sortDir === 'desc'}>
            <svg width="10" height="10" viewBox="0 0 10 10"><path d="M5 2L8 6H2Z" fill="currentColor"/></svg>
          </span>
        </button>
        <button class="col-header col-spicy" class:active={sortKey === 'spiciness'} onclick={() => toggleSort('spiciness')}>
          Avg
          <span class="sort-icon" class:asc={sortKey === 'spiciness' && sortDir === 'asc'} class:desc={sortKey === 'spiciness' && sortDir === 'desc'}>
            <svg width="10" height="10" viewBox="0 0 10 10"><path d="M5 2L8 6H2Z" fill="currentColor"/></svg>
          </span>
        </button>
        <span class="col-header col-arrow"></span>
      </div>

      <div class="blog-list">
        {#each visibleBlogs as blog, i (blog.id)}
          <a
            href="https://{blog.subdomain}"
            class="blog-row"
          >
            <div class="row-col-name">
              <img
                src={blog.photo}
                alt=""
                class="row-avatar"
                onerror={(e) => { (e.currentTarget as HTMLImageElement).style.display = 'none'; }}
              />
              <div class="row-name-block">
                <span class="row-name">{blog.name}</span>
                <span class="row-description">{blog.description}</span>
              </div>
            </div>
            <span class="row-col-tagline">{blog.tagline}</span>
            <span class="row-col-posts">{blog.stats.posts.toLocaleString()}</span>
            <span class="row-col-quotes">{blog.stats.quotes.toLocaleString()}</span>
            <span class="row-col-spicy">
              {#if blogSpiciness[blog.id] != null}
                <span class="spicy-val" style="color: {heatColor(blogSpiciness[blog.id]!)}">{blogSpiciness[blog.id]}</span>
              {:else}
                <span class="spicy-val" style="color: #d6d3d1">—</span>
              {/if}
            </span>
            <span class="row-col-arrow">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </span>
          </a>
        {/each}
      </div>
    </div>
  </section>

  <!-- How it works -->
  <section class="how-section">
    <div class="how-inner">
      <h2 class="how-title">How it works</h2>
      <div class="how-grid">
        <div class="how-step">
          <div class="how-icon">📥</div>
          <h3>Archive</h3>
          <p>Every post scraped and stored as searchable markdown with metadata.</p>
        </div>
        <div class="how-step">
          <div class="how-icon">🤖</div>
          <h3>Analyze</h3>
          <p>LLMs extract summaries, key insights, and memorable "money quotes."</p>
        </div>
        <div class="how-step">
          <div class="how-icon">🌶️</div>
          <h3>Rate</h3>
          <p>Each quote gets a spiciness score from 1-10 based on how provocative it is.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="landing-footer">
    <p>
      Made with <span class="heart">&#10084;&#65039;</span> by
      <a href="https://wesmckinney.com" target="_blank" rel="noopener noreferrer">Wes McKinney</a>
    </p>
  </footer>
</div>

<style>
  /* ── Page ───────────────────────────────────────── */
  .landing {
    min-height: 100vh;
    background: linear-gradient(180deg, #fafaf9 0%, #fff 50%);
  }

  /* ── Hero ───────────────────────────────────────── */
  .hero {
    padding: 3.5rem 1.5rem 2.5rem;
    background:
      radial-gradient(ellipse 80% 50% at 50% -10%, rgba(239, 68, 68, 0.035), transparent),
      #fafaf9;
  }

  .hero-inner {
    max-width: 52rem;
    margin: 0 auto;
  }

  .logo-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .logo {
    width: 2.75rem;
    height: 2.75rem;
    border-radius: 0.5rem;
    flex-shrink: 0;
  }

  .site-title {
    font-family: var(--font-family-serif);
    font-size: 2.5rem;
    font-weight: 600;
    color: #1c1917;
    letter-spacing: -0.025em;
    line-height: 1.1;
  }

  .tagline {
    margin-top: 0.6rem;
    font-size: 1.05rem;
    color: #57534e;
    line-height: 1.5;
    max-width: 36rem;
  }

  .description {
    margin-top: 0.35rem;
    font-size: 0.85rem;
    color: #a8a29e;
    max-width: 36rem;
    line-height: 1.55;
  }

  .hero-stats {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-top: 1rem;
    font-size: 0.78rem;
    font-weight: 500;
    color: #78716c;
    font-variant-numeric: tabular-nums;
  }

  .stat-dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #d6d3d1;
  }

  .hero-actions {
    display: flex;
    gap: 0.5rem;
    margin-top: 1.25rem;
  }

  .btn-primary,
  .btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.5rem 1rem;
    font-size: 0.8rem;
    font-weight: 600;
    border-radius: 0.5rem;
    text-decoration: none;
    transition: all 0.15s;
  }

  .btn-primary {
    background: #1c1917;
    color: #fff;
  }
  .btn-primary:hover {
    background: #292524;
  }

  .btn-secondary {
    background: #fff;
    color: #57534e;
    border: 1px solid #d6d3d1;
  }
  .btn-secondary:hover {
    background: #f5f5f4;
    border-color: #a8a29e;
  }

  /* ── Blog list ─────────────────────────────────── */
  .blog-list-section {
    padding: 0 1.5rem 3rem;
  }

  .blog-list-inner {
    max-width: 52rem;
    margin: 0 auto;
  }

  /* ── Column grid ───────────────────────────────── */
  .list-header,
  .blog-row {
    display: grid;
    grid-template-columns: 1fr 12rem 3.5rem 3.5rem 3rem 1.5rem;
    align-items: center;
    gap: 1rem;
  }

  .list-header {
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid #e7e5e4;
  }

  /* ── Column headers (sortable) ─────────────────── */
  .col-header {
    font-size: 0.65rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #a8a29e;
    background: none;
    border: none;
    padding: 0;
    cursor: default;
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
  }

  button.col-header {
    cursor: pointer;
    transition: color 0.12s;
    user-select: none;
  }
  button.col-header:hover {
    color: #57534e;
  }
  button.col-header.active {
    color: #1c1917;
  }

  .col-posts,
  .col-quotes,
  .col-spicy {
    text-align: right;
    justify-content: flex-end;
  }

  /* ── Sort indicator ────────────────────────────── */
  .sort-icon {
    opacity: 0;
    transition: opacity 0.12s, transform 0.12s;
    display: inline-flex;
  }
  button.col-header:hover .sort-icon {
    opacity: 0.3;
  }
  button.col-header.active .sort-icon {
    opacity: 1;
  }
  .sort-icon.desc {
    transform: rotate(180deg);
  }
  .sort-icon.asc {
    transform: rotate(0deg);
  }

  /* ── Blog list rows ────────────────────────────── */
  .blog-list {
    display: flex;
    flex-direction: column;
  }

  .blog-row {
    padding: 0.65rem 0.75rem;
    text-decoration: none;
    border-bottom: 1px solid #f5f5f4;
    transition: background 0.12s;
  }
  .blog-row:hover {
    background: #fafaf9;
  }

  .row-col-name {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    min-width: 0;
  }

  .row-avatar {
    width: 2rem;
    height: 2rem;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;
    border: 1px solid #e7e5e4;
  }

  .row-name-block {
    display: flex;
    flex-direction: column;
    min-width: 0;
  }

  .row-name {
    font-size: 0.85rem;
    font-weight: 600;
    color: #1c1917;
    transition: color 0.12s;
    line-height: 1.3;
  }
  .blog-row:hover .row-name {
    color: #dc2626;
  }

  .row-description {
    font-size: 0.72rem;
    color: #a8a29e;
    line-height: 1.4;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .row-col-tagline {
    font-size: 0.75rem;
    color: #78716c;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .row-col-posts,
  .row-col-quotes {
    font-size: 0.78rem;
    font-weight: 500;
    color: #57534e;
    text-align: right;
    font-variant-numeric: tabular-nums;
  }

  .row-col-spicy {
    text-align: right;
  }

  .spicy-val {
    font-size: 0.78rem;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
  }

  .row-col-arrow {
    color: #d6d3d1;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.15s;
  }
  .blog-row:hover .row-col-arrow {
    color: #dc2626;
    transform: translateX(2px);
  }

  /* ── How section ───────────────────────────────── */
  .how-section {
    background: #f5f5f4;
    padding: 3.5rem 1.5rem;
  }

  .how-inner {
    max-width: 52rem;
    margin: 0 auto;
  }

  .how-title {
    font-family: var(--font-family-serif);
    font-size: 1.35rem;
    font-weight: 500;
    color: #1c1917;
    margin-bottom: 1.75rem;
  }

  .how-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }

  .how-step h3 {
    font-size: 0.82rem;
    font-weight: 600;
    color: #1c1917;
    margin-bottom: 0.25rem;
  }

  .how-step p {
    font-size: 0.78rem;
    color: #78716c;
    line-height: 1.55;
  }

  .how-icon {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }

  /* ── Footer ────────────────────────────────────── */
  .landing-footer {
    border-top: 1px solid #e7e5e4;
    padding: 2rem 1.5rem;
    text-align: center;
    font-size: 0.8rem;
    color: #a8a29e;
  }
  .landing-footer a {
    color: #78716c;
    text-decoration: none;
    transition: color 0.15s;
  }
  .landing-footer a:hover { color: #dc2626; }
  .landing-footer .heart { color: #ef4444; }

  /* ── Responsive ────────────────────────────────── */
  @media (max-width: 768px) {
    .site-title {
      font-size: 1.75rem;
    }

    .tagline {
      font-size: 0.95rem;
    }

    .list-header,
    .blog-row {
      grid-template-columns: 1fr 3.5rem 3.5rem 3rem 1.5rem;
    }
    .col-tagline,
    .row-col-tagline { display: none; }

    .how-grid {
      grid-template-columns: 1fr;
      gap: 1.25rem;
    }
  }

  @media (max-width: 480px) {
    .hero {
      padding: 2.5rem 1.25rem 2rem;
    }

    .blog-list-section {
      padding: 0 1rem 2.5rem;
    }

    .list-header,
    .blog-row {
      grid-template-columns: 1fr 3rem 3rem 1.5rem;
    }
    .col-tagline,
    .row-col-tagline,
    .col-quotes,
    .row-col-quotes { display: none; }

    .row-avatar {
      width: 1.75rem;
      height: 1.75rem;
    }

    .row-name {
      font-size: 0.82rem;
    }

    .row-description {
      display: none;
    }
  }
</style>
