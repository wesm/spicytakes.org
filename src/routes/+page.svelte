<script lang="ts">
  import { isLandingMode } from '$lib/config';
  import LandingPage from '$lib/components/LandingPage.svelte';

  // Only import blog-specific modules in blog mode
  let activeView: any;
  let filteredPosts: any;
  let filteredQuotes: any;
  let stats: any = { yearRange: '' };
  let TimelineView: any;
  let QuotesView: any;
  let ThemesView: any;

  if (!isLandingMode) {
    import('$lib/stores').then(m => {
      activeView = m.activeView;
      filteredPosts = m.filteredPosts;
      filteredQuotes = m.filteredQuotes;
    });
    import('$lib/data').then(m => {
      stats = m.stats;
    });
    import('$lib/components/TimelineView.svelte').then(m => { TimelineView = m.default; });
    import('$lib/components/QuotesView.svelte').then(m => { QuotesView = m.default; });
    import('$lib/components/ThemesView.svelte').then(m => { ThemesView = m.default; });
  }

  function setView(view: 'timeline' | 'quotes' | 'themes') {
    activeView?.set(view);
  }
</script>

{#if isLandingMode}
  <LandingPage />
{:else if activeView && filteredPosts && filteredQuotes && TimelineView && QuotesView && ThemesView}
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <!-- View toggle and stats -->
    <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
      <!-- View toggle - prominent centered tabs -->
      <nav class="flex gap-1 bg-stone-100 p-1.5 rounded-xl">
        <button
          onclick={() => setView('timeline')}
          class="px-5 py-2.5 text-sm font-medium rounded-lg transition-all duration-150 {$activeView === 'timeline' ? 'bg-white text-stone-900 shadow-sm' : 'text-stone-600 hover:text-stone-900 hover:bg-stone-50'}"
        >
          📚 Posts
        </button>
        <button
          onclick={() => setView('quotes')}
          class="px-5 py-2.5 text-sm font-medium rounded-lg transition-all duration-150 {$activeView === 'quotes' ? 'bg-white text-stone-900 shadow-sm' : 'text-stone-600 hover:text-stone-900 hover:bg-stone-50'}"
        >
          🌶️ Spicy Quotes
        </button>
        <button
          onclick={() => setView('themes')}
          class="px-5 py-2.5 text-sm font-medium rounded-lg transition-all duration-150 {$activeView === 'themes' ? 'bg-white text-stone-900 shadow-sm' : 'text-stone-600 hover:text-stone-900 hover:bg-stone-50'}"
        >
          🏷️ Themes
        </button>
      </nav>

      <!-- Stats -->
      <div class="flex gap-4 text-sm text-stone-500">
        <span><strong class="text-stone-900">{$filteredPosts.length}</strong> posts</span>
        <span><strong class="text-stone-900">{$filteredQuotes.length}</strong> quotes</span>
        <span><strong class="text-stone-900">{stats.yearRange}</strong></span>
      </div>
    </div>

    <!-- Active view -->
    {#if $activeView === 'timeline'}
      <svelte:component this={TimelineView} />
    {:else if $activeView === 'quotes'}
      <svelte:component this={QuotesView} />
    {:else if $activeView === 'themes'}
      <svelte:component this={ThemesView} />
    {/if}
  </div>
{:else}
  <div class="flex items-center justify-center min-h-[50vh]">
    <div class="text-stone-400">Loading...</div>
  </div>
{/if}
