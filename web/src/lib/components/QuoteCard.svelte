<script lang="ts">
  import type { Quote } from '$lib/types';
  import { selectedPost } from '$lib/stores';

  let { quote }: { quote: Quote } = $props();

  function formatDate(date: Date | undefined): string {
    if (!date) return '';
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  }

  function openPost() {
    selectedPost.set(quote.post);
  }
</script>

<button
  onclick={openPost}
  class="card card-hover text-left w-full cursor-pointer break-inside-avoid mb-4"
>
  <blockquote class="font-serif text-base sm:text-lg italic text-stone-700 leading-relaxed mb-4">
    "{quote.quote}"
  </blockquote>
  <div class="text-sm">
    <p class="font-medium text-stone-900">{quote.post.title}</p>
    <p class="text-stone-400">{formatDate(quote.post.date)}</p>
  </div>
</button>
