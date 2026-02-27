<script lang="ts">
  import { isLandingMode } from '$lib/config';
  import LandingPage from '$lib/components/LandingPage.svelte';
  import { activeView, filteredPosts, filteredQuotes, statsStore } from '$lib/stores';
  import TimelineView from '$lib/components/TimelineView.svelte';
  import QuotesView from '$lib/components/QuotesView.svelte';
  import ThemesView from '$lib/components/ThemesView.svelte';
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();

  function setView(view: 'timeline' | 'quotes' | 'themes') {
    activeView.set(view);
  }
</script>

{#if isLandingMode}
  <LandingPage blogSpiciness={data.blogSpiciness} />
{:else}
  <div class="page-shell">
    <div class="view-bar">
      <nav class="view-tabs">
        <button
          onclick={() => setView('timeline')}
          class="view-tab"
          class:active={$activeView === 'timeline'}
        >
          Posts
        </button>
        <button
          onclick={() => setView('quotes')}
          class="view-tab"
          class:active={$activeView === 'quotes'}
        >
          Quotes
        </button>
        <button
          onclick={() => setView('themes')}
          class="view-tab"
          class:active={$activeView === 'themes'}
        >
          Themes
        </button>
      </nav>

      <div class="view-stats">
        <span><strong>{$filteredPosts.length}</strong> posts</span>
        <span class="stat-dot"></span>
        <span><strong>{$filteredQuotes.length}</strong> quotes</span>
        <span class="stat-dot"></span>
        <span>{$statsStore.yearRange}</span>
      </div>
    </div>

    {#if $activeView === 'timeline'}
      <TimelineView />
    {:else if $activeView === 'quotes'}
      <QuotesView />
    {:else if $activeView === 'themes'}
      <ThemesView />
    {/if}
  </div>
{/if}

<style>
  .page-shell {
    max-width: 60rem;
    margin: 0 auto;
    padding: 1.25rem 1.5rem 3rem;
  }

  .view-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.25rem;
  }

  .view-tabs {
    display: flex;
    gap: 0;
    border-bottom: 2px solid #e7e5e4;
  }

  .view-tab {
    padding: 0.5rem 0.9rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: #a8a29e;
    background: none;
    border: none;
    border-bottom: 2px solid transparent;
    margin-bottom: -2px;
    cursor: pointer;
    transition: color 0.12s, border-color 0.12s;
    text-transform: uppercase;
    letter-spacing: 0.06em;
  }
  .view-tab:hover {
    color: #57534e;
  }
  .view-tab.active {
    color: #1c1917;
    border-bottom-color: #dc2626;
  }

  .view-stats {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.82rem;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  .view-stats strong {
    color: #57534e;
    font-weight: 600;
  }

  .stat-dot {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #d6d3d1;
  }

  @media (max-width: 640px) {
    .view-bar {
      flex-direction: column;
      align-items: flex-start;
      gap: 0.5rem;
    }
  }
</style>
