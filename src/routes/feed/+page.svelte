<script lang="ts">
  import { base } from '$app/paths';
  import type { PageData } from './$types';
  import { getSpicyColor, getSpicyLabel } from '$lib/types';

  let { data }: { data: PageData } = $props();

  // Filter state
  let selectedBlog = $state<string>('all');
  let minSpiciness = $state(1);

  // Filtered posts
  let filtered = $derived.by(() => {
    let result = data.posts;
    if (selectedBlog !== 'all') {
      result = result.filter(p => p.blogId === selectedBlog);
    }
    if (minSpiciness > 1) {
      result = result.filter(
        p => p.spiciness !== null && p.spiciness >= minSpiciness
      );
    }
    return result;
  });

  // Group by month/year
  let grouped = $derived.by(() => {
    const groups: { label: string; posts: typeof filtered }[] = [];
    let currentLabel = '';
    let currentGroup: typeof filtered = [];

    for (const post of filtered) {
      if (!post.dateStr) continue;
      const d = new Date(post.dateStr);
      const label = d.toLocaleDateString('en-US', {
        month: 'long',
        year: 'numeric',
      });
      if (label !== currentLabel) {
        if (currentGroup.length > 0) {
          groups.push({ label: currentLabel, posts: currentGroup });
        }
        currentLabel = label;
        currentGroup = [post];
      } else {
        currentGroup.push(post);
      }
    }
    if (currentGroup.length > 0) {
      groups.push({ label: currentLabel, posts: currentGroup });
    }
    return groups;
  });

  function formatFeedDate(dateStr: string | null): string {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    return d.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
    });
  }

  function truncate(text: string, max: number): string {
    if (!text || text.length <= max) return text || '';
    return text.slice(0, max) + '...';
  }
</script>

<svelte:head>
  <title>Latest Spicy Takes</title>
  <meta name="description" content="The latest spicy takes from {data.authors.length} tech blogs, sorted by date" />
</svelte:head>

<div class="min-h-screen bg-gradient-to-b from-stone-50 to-white">
  <!-- Header -->
  <header class="pt-8 pb-6 px-6 text-center border-b border-stone-200">
    <div class="max-w-4xl mx-auto">
      <a href="{base}/" class="inline-block mb-3 text-stone-500 hover:text-stone-700 text-sm">
        ← Back to Spicy Takes
      </a>
      <h1 class="text-3xl md:text-4xl font-bold text-stone-900 mb-2">
        Latest Spicy Takes
      </h1>
      <p class="text-stone-600">
        {data.posts.length} recent posts from {data.authors.length} blogs
      </p>
    </div>
  </header>

  <!-- Filter bar -->
  <div class="sticky top-0 z-10 bg-white/95 backdrop-blur-sm border-b border-stone-200 shadow-sm">
    <div class="max-w-4xl mx-auto px-6 py-3 flex flex-wrap items-center gap-4">
      <!-- Blog filter -->
      <div class="flex items-center gap-2">
        <label for="blog-filter" class="text-sm font-medium text-stone-600">Author</label>
        <select
          id="blog-filter"
          bind:value={selectedBlog}
          class="text-sm border border-stone-300 rounded-lg px-3 py-1.5 bg-white text-stone-800 focus:outline-none focus:ring-2 focus:ring-red-300"
        >
          <option value="all">All blogs</option>
          {#each data.authors as author}
            <option value={author.id}>{author.name}</option>
          {/each}
        </select>
      </div>

      <!-- Spiciness filter -->
      <div class="flex items-center gap-2">
        <label for="spiciness-filter" class="text-sm font-medium text-stone-600">Min spiciness</label>
        <input
          id="spiciness-filter"
          type="range"
          min="1"
          max="10"
          step="1"
          bind:value={minSpiciness}
          class="w-24 accent-red-500"
        />
        <span class="text-sm font-mono text-stone-700 w-5 text-right">{minSpiciness}</span>
      </div>

      <!-- Results count -->
      <span class="text-sm text-stone-400 ml-auto">
        {filtered.length} posts
      </span>
    </div>
  </div>

  <!-- Feed -->
  <main class="max-w-4xl mx-auto px-6 py-8">
    {#if filtered.length === 0}
      <div class="text-center py-16">
        <p class="text-stone-500">No posts match your filters.</p>
        <button
          onclick={() => { selectedBlog = 'all'; minSpiciness = 1; }}
          class="mt-3 text-sm text-red-500 hover:text-red-600 underline"
        >
          Reset filters
        </button>
      </div>
    {:else}
      {#each grouped as group}
        <!-- Month header -->
        <div class="sticky top-[57px] z-[5] bg-stone-50/95 backdrop-blur-sm -mx-6 px-6 py-2 mb-4 mt-8 first:mt-0 border-b border-stone-200">
          <h2 class="text-sm font-semibold text-stone-500 uppercase tracking-wide">{group.label}</h2>
        </div>

        <div class="space-y-5">
          {#each group.posts as post}
            <article class="bg-white rounded-xl border border-stone-200 shadow-sm overflow-hidden hover:shadow-md transition-shadow">
              <div class="p-5">
                <!-- Author row -->
                <div class="flex items-center gap-3 mb-3">
                  <img
                    src={post.authorPhoto}
                    alt={post.authorName}
                    class="w-9 h-9 rounded-full object-cover ring-1 ring-stone-200"
                    onerror={(e) => { (e.currentTarget as HTMLImageElement).style.display = 'none'; }}
                  />
                  <div class="flex-1 min-w-0">
                    <span class="text-sm font-semibold text-stone-800">{post.authorName}</span>
                    <span class="text-stone-300 mx-1.5">·</span>
                    <span class="text-sm text-stone-500">{formatFeedDate(post.dateStr)}</span>
                  </div>
                  {#if post.spiciness !== null}
                    <span class="flex-shrink-0 px-2.5 py-1 rounded-full text-xs font-bold {getSpicyColor(post.spiciness)}">
                      {getSpicyLabel(post.spiciness)} {post.spiciness}
                    </span>
                  {/if}
                </div>

                <!-- Title -->
                <h3 class="text-lg font-bold text-stone-900 mb-2 leading-snug">
                  <a
                    href={post.spicytakesUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="hover:text-red-600 transition-colors"
                  >
                    {post.title}
                  </a>
                </h3>

                <!-- Summary -->
                {#if post.summary}
                  <p class="text-stone-600 text-sm leading-relaxed mb-3">
                    {truncate(post.summary, 280)}
                  </p>
                {/if}

                <!-- Top quotes -->
                {#if post.topQuotes.length > 0}
                  <div class="space-y-2 mb-3">
                    {#each post.topQuotes as q}
                      <div class="flex items-start gap-2">
                        <span class="flex-shrink-0 mt-0.5 text-xs font-bold px-1.5 py-0.5 rounded {getSpicyColor(q.spiciness)}">
                          {q.spiciness}
                        </span>
                        <p class="text-stone-700 text-sm italic leading-relaxed">
                          "{truncate(q.quote, 200)}"
                        </p>
                      </div>
                    {/each}
                  </div>
                {/if}

                <!-- Links -->
                <div class="flex items-center gap-4 pt-2 border-t border-stone-100 text-sm">
                  <a
                    href={post.spicytakesUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-red-500 hover:text-red-600 font-medium flex items-center gap-1"
                  >
                    Full analysis
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                  </a>
                  {#if post.sourceUrl}
                    <a
                      href={post.sourceUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      class="text-stone-500 hover:text-stone-700 flex items-center gap-1"
                    >
                      Read original
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
                      </svg>
                    </a>
                  {/if}
                </div>
              </div>
            </article>
          {/each}
        </div>
      {/each}
    {/if}
  </main>

  <!-- Footer -->
  <footer class="border-t border-stone-200 py-6 text-center text-sm text-stone-500">
    <p>
      Made with <span class="text-red-500">❤️</span> by <a href="https://wesmckinney.com" target="_blank" rel="noopener noreferrer" class="text-stone-500 hover:text-red-500 transition-colors">Wes McKinney</a>
    </p>
  </footer>
</div>
