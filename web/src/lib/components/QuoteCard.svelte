<script lang="ts">
  import type { Quote } from '$lib/types';
  import { getSpicyColor } from '$lib/types';
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
      <div class="flex items-center gap-3 text-sm">
        <span class="font-medium text-stone-700">{quote.post.title}</span>
        <span class="text-stone-400">{formatDate(quote.date)}</span>
      </div>
    </div>
  </div>
</button>
