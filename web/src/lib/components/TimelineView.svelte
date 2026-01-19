<script lang="ts">
  import { filteredPosts } from '$lib/stores';
  import { years } from '$lib/data';
  import { filterPosts } from '$lib/filter';
  import PostCard from './PostCard.svelte';
  import type { Post } from '$lib/types';

  let sortBy = $state<'date' | 'spiciness'>('date');
  let selectedYear = $state<number | null>(null);
  let minSpiciness = $state(1);

  // Filter and sort posts
  let displayPosts = $derived(() => {
    let result = filterPosts($filteredPosts, minSpiciness, selectedYear);

    if (sortBy === 'spiciness') {
      result = [...result].sort((a, b) => (b.spiciness || 0) - (a.spiciness || 0));
    } else {
      result = [...result].sort((a, b) => (b.date?.getTime() || 0) - (a.date?.getTime() || 0));
    }

    return result;
  });

  // Group posts by year for chronological view
  function getPostsByYear(posts: Post[]) {
    const byYear: Record<number, Post[]> = {};
    posts.forEach(post => {
      const year = post.year || new Date().getFullYear();
      if (!byYear[year]) byYear[year] = [];
      byYear[year].push(post);
    });
    return Object.entries(byYear)
      .sort(([a], [b]) => Number(b) - Number(a))
      .map(([year, posts]) => ({ year: Number(year), posts }));
  }

  let groupedPosts = $derived(getPostsByYear(displayPosts()));

  // Get spiciest posts per year
  let spiciestByYear = $derived(() => {
    const result: Record<number, Post[]> = {};
    for (const year of years) {
      const yearPosts = displayPosts().filter(p => p.year === year);
      result[year] = [...yearPosts].sort((a, b) => (b.spiciness || 0) - (a.spiciness || 0)).slice(0, 5);
    }
    return result;
  });
</script>

<div class="space-y-6">
  <!-- Controls -->
  <div class="flex flex-wrap items-center gap-4 p-4 bg-white rounded-xl border border-stone-200">
    <div class="flex items-center gap-2">
      <label for="timeline-sort" class="text-sm font-medium text-stone-600">Sort:</label>
      <select
        id="timeline-sort"
        bind:value={sortBy}
        class="text-sm border border-stone-200 rounded-lg px-3 py-1.5 bg-white focus:ring-2 focus:ring-blue-500"
      >
        <option value="date">Chronological</option>
        <option value="spiciness">Spiciest First</option>
      </select>
    </div>

    <div class="flex items-center gap-2">
      <label for="timeline-year" class="text-sm font-medium text-stone-600">Year:</label>
      <select
        id="timeline-year"
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
      <label for="timeline-spice" class="text-sm font-medium text-stone-600">Min Spice:</label>
      <input
        id="timeline-spice"
        type="range"
        min="1"
        max="10"
        bind:value={minSpiciness}
        class="w-24"
      />
      <span class="text-sm font-medium text-stone-700 w-4">{minSpiciness}</span>
    </div>

    <div class="ml-auto text-sm text-stone-500">
      {displayPosts().length} posts
    </div>
  </div>

  <!-- Year-by-Year Spiciest (when no year selected and sorting by spiciness) -->
  {#if !selectedYear && sortBy === 'spiciness'}
    <div class="space-y-8">
      {#each years as year}
        {@const yearSpicy = spiciestByYear()[year]}
        {#if yearSpicy.length > 0}
          <section>
            <div class="sticky top-[145px] z-10 bg-stone-50 py-3 border-b-2 border-stone-900 mb-6">
              <h2 class="text-2xl font-bold text-stone-900">
                {year}
                <span class="text-base font-normal text-stone-500 ml-2">Top 5 Spiciest</span>
              </h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {#each yearSpicy as post (post.filename)}
                <PostCard {post} />
              {/each}
            </div>
          </section>
        {/if}
      {/each}
    </div>
  {:else if displayPosts().length === 0}
    <div class="text-center py-16">
      <p class="text-stone-500 text-lg">No posts found</p>
      <p class="text-stone-400 mt-1">Try adjusting your search or filters</p>
    </div>
  {:else}
    <div class="space-y-12">
      {#each groupedPosts as { year, posts }}
        <section>
          <div class="sticky top-[145px] z-10 bg-stone-50 py-3 border-b-2 border-stone-900 mb-6">
            <h2 class="text-2xl font-bold text-stone-900">
              {year}
              <span class="text-base font-normal text-stone-500 ml-2">{posts.length} posts</span>
            </h2>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {#each posts as post (post.filename)}
              <PostCard {post} />
            {/each}
          </div>
        </section>
      {/each}
    </div>
  {/if}
</div>
