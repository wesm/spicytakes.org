<script lang="ts">
  import { filteredPosts, selectedPost } from '$lib/stores';
  import { years } from '$lib/data';
  import { filterPosts } from '$lib/filter';
  import { getSpicyColor, THEME_LABELS } from '$lib/types';
  import type { Post } from '$lib/types';

  function formatDate(date: Date | undefined): string {
    if (!date) return '';
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  function openPost(post: Post) {
    selectedPost.set(post);
  }

  let sortBy = $state<'date' | 'spiciness'>('date');
  let selectedYear = $state<number | null>(null);
  let minSpiciness = $state(1);

  // Filter and sort posts
  let displayPosts = $derived.by(() => {
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

  let groupedPosts = $derived(getPostsByYear(displayPosts));

  // Get spiciest posts per year
  let spiciestByYear = $derived.by(() => {
    const result: Record<number, Post[]> = {};
    for (const year of years) {
      const yearPosts = displayPosts.filter(p => p.year === year);
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
      {displayPosts.length} posts
    </div>
  </div>

  <!-- Year-by-Year Spiciest (when no year selected and sorting by spiciness) -->
  {#if !selectedYear && sortBy === 'spiciness'}
    <div class="space-y-8">
      {#each years as year}
        {@const yearSpicy = spiciestByYear[year]}
        {#if yearSpicy.length > 0}
          <section>
            <h3 class="text-xl font-bold text-stone-900 mb-4 pb-2 border-b-2 border-stone-900">
              {year}
              <span class="text-sm font-normal text-stone-500 ml-2">Top 5 Spiciest</span>
            </h3>
            <div class="space-y-3">
              {#each yearSpicy as post (post.filename)}
                <button
                  onclick={() => openPost(post)}
                  class="w-full text-left bg-white border border-stone-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-lg transition-all duration-200"
                >
                  <div class="flex items-start gap-4">
                    {#if post.spiciness != null}
                      <div class="flex-shrink-0 w-12 h-12 flex items-center justify-center rounded-full {getSpicyColor(post.spiciness)} font-bold" role="img" aria-label="Spiciness score: {post.spiciness} out of 10" title="Spiciness: {post.spiciness}/10 (how provocative or contrarian)">
                        <span aria-hidden="true">🌶️{post.spiciness}</span>
                      </div>
                    {/if}
                    <div class="flex-1 min-w-0">
                      <h4 class="font-serif text-lg font-semibold text-stone-900 mb-2 leading-snug">
                        {post.title}
                      </h4>
                      <p class="text-sm text-stone-600 mb-3 line-clamp-2">
                        {post.summary}
                      </p>
                      <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm">
                        <span class="text-stone-400">{formatDate(post.date)}</span>
                        {#if post.themes?.length}
                          <div class="flex gap-1">
                            {#each post.themes.slice(0, 2) as theme}
                              <span class="text-xs px-2 py-0.5 bg-stone-100 text-stone-500 rounded">
                                {THEME_LABELS[theme] || theme.replace(/_/g, ' ')}
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
          </section>
        {/if}
      {/each}
    </div>
  {:else if displayPosts.length === 0}
    <div class="text-center py-16">
      <p class="text-stone-500 text-lg">No posts found</p>
      <p class="text-stone-400 mt-1">Try adjusting your search or filters</p>
    </div>
  {:else}
    <div class="space-y-8">
      {#each groupedPosts as { year, posts }}
        <section>
          <h3 class="text-xl font-bold text-stone-900 mb-4 pb-2 border-b-2 border-stone-900">
            {year}
            <span class="text-sm font-normal text-stone-500 ml-2">{posts.length} posts</span>
          </h3>
          <div class="space-y-3">
            {#each posts as post (post.filename)}
              <button
                onclick={() => openPost(post)}
                class="w-full text-left bg-white border border-stone-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-lg transition-all duration-200"
              >
                <div class="flex items-start gap-4">
                  {#if post.spiciness != null}
                    <div class="flex-shrink-0 w-12 h-12 flex items-center justify-center rounded-full {getSpicyColor(post.spiciness)} font-bold" role="img" aria-label="Spiciness score: {post.spiciness} out of 10" title="Spiciness: {post.spiciness}/10 (how provocative or contrarian)">
                      <span aria-hidden="true">🌶️{post.spiciness}</span>
                    </div>
                  {/if}
                  <div class="flex-1 min-w-0">
                    <h4 class="font-serif text-lg font-semibold text-stone-900 mb-2 leading-snug">
                      {post.title}
                    </h4>
                    <p class="text-sm text-stone-600 mb-3 line-clamp-2">
                      {post.summary}
                    </p>
                    <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm">
                      <span class="text-stone-400">{formatDate(post.date)}</span>
                      {#if post.themes?.length}
                        <div class="flex gap-1">
                          {#each post.themes.slice(0, 2) as theme}
                            <span class="text-xs px-2 py-0.5 bg-stone-100 text-stone-500 rounded">
                              {THEME_LABELS[theme] || theme.replace(/_/g, ' ')}
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
        </section>
      {/each}
    </div>
  {/if}
</div>

<style>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    line-clamp: 2;
  }
</style>
