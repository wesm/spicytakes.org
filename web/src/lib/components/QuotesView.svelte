<script lang="ts">
  import { filteredQuotes } from '$lib/stores';
  import QuoteCard from './QuoteCard.svelte';

  // Limit to prevent performance issues
  const MAX_QUOTES = 150;

  let displayQuotes = $derived($filteredQuotes.slice(0, MAX_QUOTES));
</script>

<div>
  {#if $filteredQuotes.length === 0}
    <div class="text-center py-16">
      <p class="text-stone-500 text-lg">No quotes found</p>
      <p class="text-stone-400 mt-1">Try adjusting your search or filters</p>
    </div>
  {:else}
    <p class="text-sm text-stone-500 mb-6">
      Showing {displayQuotes.length} of {$filteredQuotes.length} quotes
    </p>
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-4">
      {#each displayQuotes as quote, i (quote.quote + quote.post.filename + i)}
        <QuoteCard {quote} />
      {/each}
    </div>
  {/if}
</div>
