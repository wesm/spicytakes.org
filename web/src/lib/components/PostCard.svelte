<script lang="ts">
  import type { Post } from '$lib/types';
  import { THEME_LABELS, getSpicyColor } from '$lib/types';
  import { selectedPost } from '$lib/stores';

  let { post }: { post: Post } = $props();

  function formatDate(date: Date | undefined): string {
    if (!date) return '';
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric'
    });
  }

  function openPost() {
    selectedPost.set(post);
  }
</script>

<button
  onclick={openPost}
  class="card card-hover text-left w-full cursor-pointer"
>
  <div class="flex items-start justify-between gap-2 mb-2">
    <p class="text-xs font-medium text-stone-400 uppercase tracking-wide">
      {formatDate(post.date)}
    </p>
    {#if post.spiciness}
      <span class="flex-shrink-0 w-9 h-9 flex items-center justify-center rounded-full {getSpicyColor(post.spiciness)} text-xs font-bold" title="Spiciness score">
        🌶️{post.spiciness}
      </span>
    {/if}
  </div>
  <h3 class="font-serif text-lg font-semibold text-stone-900 mb-2 leading-snug">
    {post.title}
  </h3>
  <p class="text-sm text-stone-600 line-clamp-3 mb-3">
    {post.summary}
  </p>
  {#if post.themes?.length}
    <div class="flex flex-wrap gap-1.5">
      {#each post.themes.slice(0, 3) as theme}
        <span class="text-xs px-2 py-0.5 bg-stone-100 text-stone-500 rounded">
          {THEME_LABELS[theme] || theme}
        </span>
      {/each}
    </div>
  {/if}
</button>

<style>
  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    line-clamp: 3;
  }
</style>
