<script lang="ts">
  import { selectedPost } from '$lib/stores';
  import { THEME_LABELS, getSpicyColor } from '$lib/types';

  function close() {
    selectedPost.set(null);
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Escape') close();
  }

  function formatDate(date: Date | undefined): string {
    if (!date) return '';
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }

  function getSubstackUrl(filename: string): string {
    const slug = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '');
    return `https://benn.substack.com/p/${slug}`;
  }
</script>

<svelte:window on:keydown={handleKeydown} />

{#if $selectedPost}
  <div class="fixed inset-0 z-[100] flex items-center justify-center p-4">
    <!-- Backdrop -->
    <button
      class="absolute inset-0 bg-black/50 backdrop-blur-sm"
      onclick={close}
      aria-label="Close modal"
    ></button>

    <!-- Modal content -->
    <div class="relative bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[85vh] overflow-y-auto animate-in fade-in zoom-in-95 duration-200">
      <!-- Close button -->
      <button
        onclick={close}
        aria-label="Close"
        class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-stone-100 text-stone-500 hover:bg-stone-200 hover:text-stone-700 transition-colors"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>

      <div class="p-8">
        <!-- Date and Spiciness -->
        <div class="flex items-center justify-between mb-2">
          <p class="text-sm font-medium text-stone-400 uppercase tracking-wide">
            {formatDate($selectedPost.date)}
          </p>
          {#if $selectedPost.spiciness != null}
            <div class="flex items-center gap-2 {getSpicyColor($selectedPost.spiciness)} px-3 py-1 rounded-full" role="img" aria-label="Spiciness score: {$selectedPost.spiciness} out of 10" title="Spiciness: {$selectedPost.spiciness}/10 (how provocative or contrarian)">
              <span aria-hidden="true">🌶️</span>
              <span class="font-bold">{$selectedPost.spiciness}</span>
              <span class="text-xs opacity-75" aria-hidden="true">spiciness</span>
            </div>
          {/if}
        </div>

        <!-- Title -->
        <h2 class="font-serif text-2xl font-semibold text-stone-900 mb-4 pr-8">
          {$selectedPost.title}
        </h2>

        <!-- Link to original (prominent, at top) -->
        <a
          href={getSubstackUrl($selectedPost.filename)}
          target="_blank"
          rel="noopener noreferrer"
          class="flex items-center justify-center gap-2 w-full py-3 px-4 mb-6 bg-[#FF6719] hover:bg-[#e55a14] text-white font-semibold rounded-lg transition-colors"
        >
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22.539 8.242H1.46V5.406h21.08v2.836zM1.46 10.812V24L12 18.11 22.54 24V10.812H1.46zM22.54 0H1.46v2.836h21.08V0z"/>
          </svg>
          Read the full post on Substack
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
          </svg>
        </a>

        <!-- Themes -->
        {#if $selectedPost.themes?.length}
          <div class="flex flex-wrap gap-2 mb-6">
            {#each $selectedPost.themes as theme}
              <span class="px-2.5 py-1 bg-blue-50 text-blue-700 text-xs font-medium rounded">
                {THEME_LABELS[theme] || theme}
              </span>
            {/each}
          </div>
        {/if}

        <!-- Summary -->
        <div class="mb-6">
          <h3 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-2">Summary</h3>
          <p class="text-stone-700 leading-relaxed">
            {$selectedPost.summary}
          </p>
        </div>

        <!-- Key Insight -->
        {#if $selectedPost.key_insight}
          <div class="mb-6">
            <h3 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-2">Key Insight</h3>
            <blockquote class="pl-4 border-l-4 border-blue-500 font-serif text-lg italic text-stone-600">
              {$selectedPost.key_insight}
            </blockquote>
          </div>
        {/if}

        <!-- Money Quotes -->
        {#if $selectedPost.money_quotes?.length}
          <div class="mb-6">
            <h3 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-3">Money Quotes</h3>
            <ul class="space-y-3">
              {#each $selectedPost.money_quotes as quote}
                <li class="relative pl-4 py-3 bg-stone-50 rounded-lg">
                  <span class="absolute left-3 top-2 text-2xl text-blue-200 font-serif">"</span>
                  <p class="font-serif text-stone-700 pl-4">{quote}</p>
                </li>
              {/each}
            </ul>
          </div>
        {/if}

        <!-- Tone -->
        {#if $selectedPost.tone}
          <div class="mb-6">
            <h3 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-2">Tone</h3>
            <p class="text-stone-600">{$selectedPost.tone}</p>
          </div>
        {/if}

      </div>
    </div>
  </div>
{/if}

<style>
  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  @keyframes zoom-in-95 {
    from { transform: scale(0.95); }
    to { transform: scale(1); }
  }
  .animate-in {
    animation: fade-in 0.2s ease, zoom-in-95 0.2s ease;
  }
</style>
