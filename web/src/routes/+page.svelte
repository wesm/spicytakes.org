<script lang="ts">
  import { activeView, filteredPosts, filteredQuotes } from '$lib/stores';
  import { stats } from '$lib/data';
  import TimelineView from '$lib/components/TimelineView.svelte';
  import QuotesView from '$lib/components/QuotesView.svelte';
  import ThemesView from '$lib/components/ThemesView.svelte';
</script>

<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
  <!-- Stats bar -->
  <div class="flex gap-6 py-3 mb-6 border-b border-stone-200 text-sm text-stone-500">
    <span><strong class="text-stone-900">{$filteredPosts.length}</strong> posts</span>
    <span><strong class="text-stone-900">{$filteredQuotes.length}</strong> quotes</span>
    <span><strong class="text-stone-900">{stats.yearRange}</strong></span>
  </div>

  <!-- Active view -->
  {#if $activeView === 'timeline'}
    <TimelineView />
  {:else if $activeView === 'quotes'}
    <QuotesView />
  {:else if $activeView === 'themes'}
    <ThemesView />
  {/if}
</div>
