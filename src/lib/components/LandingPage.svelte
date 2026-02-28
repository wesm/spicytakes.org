<script lang="ts">
  import { onMount } from 'svelte';
  import { base } from '$app/paths';
  import { landing } from '$lib/config';
  import { heatColorCompact, type BlogCard } from '$lib/types';

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
      <!-- Sort bar -->
      <div class="sort-bar">
        <span class="sort-label">Sort by</span>
        {#each [
          { key: 'name', label: 'Name' },
          { key: 'posts', label: 'Posts' },
          { key: 'quotes', label: 'Quotes' },
          { key: 'spiciness', label: 'Spiciness' },
        ] as item (item.key)}
          <button
            class="sort-btn"
            class:active={sortKey === item.key}
            onclick={() => toggleSort(item.key as SortKey)}
          >
            {item.label}
            {#if sortKey === item.key}
              <span class="sort-icon" class:desc={sortDir === 'desc'}>
                <svg width="10" height="10" viewBox="0 0 10 10"><path d="M5 2L8 6H2Z" fill="currentColor"/></svg>
              </span>
            {/if}
          </button>
        {/each}
      </div>

      <!-- Card grid -->
      <div class="blog-grid">
        {#each visibleBlogs as blog (blog.id)}
          <a href="https://{blog.subdomain}" class="blog-card">
            <div class="card-top">
              <img
                src={blog.photo}
                alt=""
                class="card-avatar"
                onerror={(e) => { (e.currentTarget as HTMLImageElement).style.display = 'none'; }}
              />
              <div class="card-identity">
                <span class="card-name">{blog.name}</span>
                <span class="card-tagline">{blog.tagline}</span>
              </div>
              {#if blogSpiciness[blog.id] != null}
                <span
                  class="card-spicy"
                  style="color: {heatColorCompact(blogSpiciness[blog.id]!)}"
                  role="img"
                  aria-label="Average spiciness: {blogSpiciness[blog.id]}"
                >{blogSpiciness[blog.id]}</span>
              {/if}
            </div>
            <p class="card-description">{blog.description}</p>
            <div class="card-footer">
              <span class="card-stat">{blog.stats.posts.toLocaleString()} posts</span>
              <span class="card-stat-dot"></span>
              <span class="card-stat">{blog.stats.quotes.toLocaleString()} quotes</span>
              <span class="card-arrow">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </span>
            </div>
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
    max-width: 60rem;
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
    max-width: 60rem;
    margin: 0 auto;
  }

  /* ── Sort bar ───────────────────────────────────── */
  .sort-bar {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.35rem;
    row-gap: 0.25rem;
    padding: 0.5rem 0;
    margin-bottom: 1rem;
    border-bottom: 1px solid #e7e5e4;
  }

  .sort-label {
    font-size: 0.68rem;
    font-weight: 500;
    color: #a8a29e;
    margin-right: 0.25rem;
  }

  .sort-btn {
    font-size: 0.68rem;
    font-weight: 500;
    color: #78716c;
    background: none;
    border: 1px solid transparent;
    padding: 0.2rem 0.55rem;
    border-radius: 0.3rem;
    cursor: pointer;
    transition: all 0.12s;
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
    user-select: none;
  }
  .sort-btn:hover {
    color: #1c1917;
    background: #f5f5f4;
  }
  .sort-btn.active {
    color: #1c1917;
    font-weight: 600;
    background: #f5f5f4;
    border-color: #e7e5e4;
  }

  .sort-icon {
    display: inline-flex;
    transition: transform 0.12s;
  }
  .sort-icon.desc {
    transform: rotate(180deg);
  }

  /* ── Blog card grid ─────────────────────────────── */
  .blog-grid {
    display: flex;
    flex-direction: column;
    gap: 0;
  }

  .blog-card {
    display: flex;
    flex-direction: column;
    padding: 1rem 0.75rem;
    text-decoration: none;
    border-bottom: 1px solid #f5f5f4;
    transition: background 0.12s;
  }
  .blog-card:hover {
    background: #fafaf9;
  }

  .card-top {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    margin-bottom: 0.75rem;
  }

  .card-avatar {
    width: 2.75rem;
    height: 2.75rem;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;
    border: 1px solid #e7e5e4;
  }

  .card-identity {
    flex: 1;
    min-width: 0;
  }

  .card-name {
    display: block;
    font-size: 0.95rem;
    font-weight: 600;
    color: #1c1917;
    line-height: 1.3;
    transition: color 0.12s;
  }
  .blog-card:hover .card-name {
    color: #dc2626;
  }

  .card-tagline {
    display: block;
    font-size: 0.75rem;
    color: #78716c;
    line-height: 1.3;
  }

  .card-spicy {
    font-size: 1.1rem;
    font-weight: 800;
    font-variant-numeric: tabular-nums;
    flex-shrink: 0;
    align-self: flex-start;
  }

  .card-description {
    font-size: 0.82rem;
    color: #57534e;
    line-height: 1.55;
    flex: 1;
  }

  .card-footer {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    margin-top: 0.75rem;
    padding-top: 0.65rem;
    border-top: 1px solid #f5f5f4;
  }

  .card-stat {
    font-size: 0.82rem;
    font-weight: 600;
    color: #1c1917;
    font-variant-numeric: tabular-nums;
  }

  .card-stat-dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #d6d3d1;
  }

  .card-arrow {
    margin-left: auto;
    color: #d6d3d1;
    display: flex;
    align-items: center;
    transition: all 0.15s;
  }
  .blog-card:hover .card-arrow {
    color: #dc2626;
    transform: translateX(2px);
  }

  /* ── How section ───────────────────────────────── */
  .how-section {
    background: #f5f5f4;
    padding: 3.5rem 1.5rem;
  }

  .how-inner {
    max-width: 60rem;
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

    .card-avatar {
      width: 2.25rem;
      height: 2.25rem;
    }
  }
</style>
