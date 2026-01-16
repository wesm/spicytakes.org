<script lang="ts">
  import { filteredPosts } from '$lib/stores';
  import PostCard from './PostCard.svelte';

  // Group filtered posts by year
  $effect(() => {
    // This will recompute when filteredPosts changes
  });

  function getPostsByYear(posts: typeof $filteredPosts) {
    const byYear: Record<number, typeof $filteredPosts> = {};
    posts.forEach(post => {
      const year = post.year || new Date().getFullYear();
      if (!byYear[year]) byYear[year] = [];
      byYear[year].push(post);
    });
    return Object.entries(byYear)
      .sort(([a], [b]) => Number(b) - Number(a))
      .map(([year, posts]) => ({ year: Number(year), posts }));
  }

  let groupedPosts = $derived(getPostsByYear($filteredPosts));
</script>

<div class="space-y-12">
  {#if $filteredPosts.length === 0}
    <div class="text-center py-16">
      <p class="text-stone-500 text-lg">No posts found</p>
      <p class="text-stone-400 mt-1">Try adjusting your search or filters</p>
    </div>
  {:else}
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
  {/if}
</div>
