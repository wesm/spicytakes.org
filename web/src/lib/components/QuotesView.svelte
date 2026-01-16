<script lang="ts">
  import { filteredQuotes } from '$lib/stores';
  import { years, quotesByYear } from '$lib/data';
  import { getSpicyColor } from '$lib/types';
  import { selectedPost } from '$lib/stores';
  import type { Quote } from '$lib/types';

  let sortBy = $state<'date' | 'spiciness'>('date');
  let selectedYear = $state<number | null>(null);
  let minSpiciness = $state(1);

  function formatDate(date: Date | undefined): string {
    if (!date) return '';
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  function openPost(quote: Quote) {
    selectedPost.set(quote.post);
  }

  // Filter and sort quotes
  let displayQuotes = $derived(() => {
    let result = $filteredQuotes.filter(q => q.spiciness >= minSpiciness);

    if (selectedYear) {
      result = result.filter(q => q.year === selectedYear);
    }

    if (sortBy === 'spiciness') {
      result = [...result].sort((a, b) => b.spiciness - a.spiciness);
    } else {
      result = [...result].sort((a, b) => (b.date?.getTime() || 0) - (a.date?.getTime() || 0));
    }

    return result;
  });

  // Get spiciest per year
  let spiciestByYear = $derived(() => {
    const result: Record<number, Quote[]> = {};
    for (const year of years) {
      const yearQuotes = $filteredQuotes.filter(q => q.year === year);
      result[year] = [...yearQuotes].sort((a, b) => b.spiciness - a.spiciness).slice(0, 5);
    }
    return result;
  });
</script>

<div class="space-y-6">
  <!-- Controls -->
  <div class="flex flex-wrap items-center gap-4 p-4 bg-white rounded-xl border border-stone-200">
    <div class="flex items-center gap-2">
      <label class="text-sm font-medium text-stone-600">Sort:</label>
      <select
        bind:value={sortBy}
        class="text-sm border border-stone-200 rounded-lg px-3 py-1.5 bg-white focus:ring-2 focus:ring-blue-500"
      >
        <option value="date">Chronological</option>
        <option value="spiciness">Spiciest First</option>
      </select>
    </div>

    <div class="flex items-center gap-2">
      <label class="text-sm font-medium text-stone-600">Year:</label>
      <select
        bind:value={selectedYear}
        class="text-sm border border-stone-200 rounded-lg px-3 py-1.5 bg-white focus:ring-2 focus:ring-blue-500"
      >
        <option value={null}>All Years</option>
        {#each years as year}
          <option value={year}>{year}</option>
        {/each}
      </select>
    </div>

    <div class="flex items-center gap-2">
      <label class="text-sm font-medium text-stone-600">Min Spice:</label>
      <input
        type="range"
        min="1"
        max="10"
        bind:value={minSpiciness}
        class="w-24"
      />
      <span class="text-sm font-medium text-stone-700 w-4">{minSpiciness}</span>
    </div>

    <div class="ml-auto text-sm text-stone-500">
      {displayQuotes().length} quotes
    </div>
  </div>

  <!-- Year-by-Year Spiciest (when no year selected) -->
  {#if !selectedYear && sortBy === 'spiciness'}
    <div class="space-y-8">
      {#each years as year}
        {@const yearSpicy = spiciestByYear()[year]}
        {#if yearSpicy.length > 0}
          <section>
            <h3 class="text-xl font-bold text-stone-900 mb-4 pb-2 border-b-2 border-stone-900">
              {year}
              <span class="text-sm font-normal text-stone-500 ml-2">Top 5 Spiciest</span>
            </h3>
            <div class="space-y-3">
              {#each yearSpicy as quote, i}
                <button
                  onclick={() => openPost(quote)}
                  class="w-full text-left bg-white border border-stone-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-lg transition-all duration-200"
                >
                  <div class="flex items-start gap-4">
                    <div class="flex-shrink-0 w-8 h-8 flex items-center justify-center rounded-full {getSpicyColor(quote.spiciness)} font-bold text-sm">
                      {quote.spiciness}
                    </div>
                    <div class="flex-1 min-w-0">
                      <blockquote class="font-serif text-lg text-stone-800 leading-relaxed mb-3">
                        "{quote.quote}"
                      </blockquote>
                      <div class="flex items-center gap-3 text-sm">
                        <span class="font-medium text-stone-700">{quote.post.title}</span>
                        <span class="text-stone-400">{formatDate(quote.date)}</span>
                      </div>
                    </div>
                  </div>
                </button>
              {/each}
            </div>
          </section>
        {/if}
      {/each}
    </div>
  {:else}
    <!-- Regular chronological list -->
    {#if displayQuotes().length === 0}
      <div class="text-center py-16">
        <p class="text-stone-500 text-lg">No quotes found</p>
        <p class="text-stone-400 mt-1">Try adjusting your filters</p>
      </div>
    {:else}
      <div class="space-y-3">
        {#each displayQuotes() as quote, i (quote.quote + quote.post.filename + i)}
          <button
            onclick={() => openPost(quote)}
            class="w-full text-left bg-white border border-stone-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-lg transition-all duration-200"
          >
            <div class="flex items-start gap-4">
              <div class="flex-shrink-0 w-10 h-10 flex items-center justify-center rounded-full {getSpicyColor(quote.spiciness)} font-bold">
                {quote.spiciness}
              </div>
              <div class="flex-1 min-w-0">
                <blockquote class="font-serif text-lg text-stone-800 leading-relaxed mb-3">
                  "{quote.quote}"
                </blockquote>
                <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm">
                  <span class="font-medium text-stone-700">{quote.post.title}</span>
                  <span class="text-stone-400">{formatDate(quote.date)}</span>
                  {#if quote.themes.length > 0}
                    <div class="flex gap-1">
                      {#each quote.themes.slice(0, 2) as theme}
                        <span class="text-xs px-2 py-0.5 bg-stone-100 text-stone-500 rounded">
                          {theme.replace(/_/g, ' ')}
                        </span>
                      {/each}
                    </div>
                  {/if}
                </div>
              </div>
            </div>
          </button>
        {/each}
      </div>
    {/if}
  {/if}
</div>
