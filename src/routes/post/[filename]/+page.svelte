<script lang="ts">
  import { onMount } from 'svelte';
  import { browser } from '$app/environment';
  import { postsStore } from '$lib/stores';
  import { getSpicyColor, type Post } from '$lib/types';
  import { THEME_LABELS, getSourceUrl, getSourceLabel, config, formatDate } from '$lib/config';
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();

  // Convert server post data to Post type with Date object
  function toPost(serverPost: any): Post | undefined {
    if (!serverPost) return undefined;
    return {
      ...serverPost,
      date: new Date(serverPost.dateStr)
    };
  }

  // Use server-loaded post for SSR, fall back to store for client navigation
  let post = $derived(data.post ? toPost(data.post) : $postsStore.find(p => p.filename === data.filename));

  let highlightedQuote: number | null = $state(null);
  let copiedQuote: number | null = $state(null);
  let showTranscript = $state(false);

  function updateHighlight() {
    if (!browser) return;
    const hash = window.location.hash;
    const match = hash.match(/^#quote-(\d+)$/);
    highlightedQuote = match ? parseInt(match[1]) : null;

    // Scroll to highlighted quote after a short delay to ensure DOM is ready
    if (highlightedQuote !== null) {
      setTimeout(() => {
        document.getElementById(`quote-${highlightedQuote}`)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 100);
    }
  }

  function selectQuote(index: number) {
    if (!browser) return;
    window.location.hash = `quote-${index}`;
    highlightedQuote = index;
  }

  async function copyQuoteLink(index: number, event: MouseEvent) {
    event.stopPropagation();
    if (!browser) return;
    const url = `${window.location.origin}${window.location.pathname}#quote-${index}`;
    try {
      await navigator.clipboard.writeText(url);
      copiedQuote = index;
    } catch {
      // Clipboard API not available or permission denied - just highlight the quote
    }
    highlightedQuote = index;
    window.location.hash = `quote-${index}`;
    setTimeout(() => {
      copiedQuote = null;
    }, 2000);
  }

  onMount(() => {
    updateHighlight();
    window.addEventListener('hashchange', updateHighlight);
    return () => window.removeEventListener('hashchange', updateHighlight);
  });
</script>

<svelte:head>
  {#if post}
    <title>{post.title} - {config?.name}</title>
    <meta name="description" content={post.summary} />
  {/if}
</svelte:head>

{#if post}
  {@const sourceUrl = getSourceUrl(post.filename, post)}
  <div class="max-w-3xl lg:max-w-5xl mx-auto px-4 py-8">
    <!-- Back link -->
    <a href="/" class="inline-flex items-center gap-2 text-stone-500 hover:text-stone-700 transition-colors mb-6">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
      Back to all posts
    </a>

    <article class="bg-white rounded-2xl shadow-lg p-8">
      <!-- Date, Link, and Spiciness -->
      <div class="flex items-center justify-between mb-2">
        <div class="flex items-center gap-2 text-sm text-stone-400">
          <span class="font-medium uppercase tracking-wide">
            {formatDate(post.date)}
          </span>
          {#if sourceUrl}
            <span>·</span>
            <a
              href={sourceUrl}
              target="_blank"
              rel="noopener noreferrer"
              class="text-[#FF6719] hover:text-[#e55a14] hover:underline transition-colors"
            >
              {getSourceLabel(post)} ↗
            </a>
          {/if}
        </div>
        {#if post.spiciness != null}
          <div class="flex items-center gap-2 {getSpicyColor(post.spiciness)} px-3 py-1 rounded-full" role="img" aria-label="Spiciness score: {post.spiciness} out of 10" title="Spiciness: {post.spiciness}/10 (how provocative or contrarian)">
            <span aria-hidden="true">🌶️</span>
            <span class="font-bold">{post.spiciness}</span>
            <span class="text-xs opacity-75" aria-hidden="true">spiciness</span>
          </div>
        {/if}
      </div>

      <!-- Title -->
      <h1 class="font-serif text-3xl font-semibold text-stone-900 mb-4">
        {post.title}
      </h1>

      <!-- Themes -->
      {#if post.themes?.length}
        <div class="flex flex-wrap gap-2 mb-6">
          {#each post.themes as theme}
            <span class="px-2.5 py-1 bg-blue-50 text-blue-700 text-xs font-medium rounded">
              {THEME_LABELS[theme] || theme}
            </span>
          {/each}
        </div>
      {/if}

      <!-- Summary -->
      <div class="mb-6">
        <h2 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-2">Summary</h2>
        <p class="text-stone-700 leading-relaxed">
          {post.summary}
        </p>
      </div>

      <!-- Key Insight -->
      {#if post.key_insight}
        <div class="mb-6">
          <h2 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-2">Key Insight</h2>
          <blockquote class="pl-4 border-l-4 border-blue-500 font-serif text-lg italic text-stone-600">
            {post.key_insight}
          </blockquote>
        </div>
      {/if}

      <!-- Money Quotes -->
      {#if post.money_quotes?.length}
        <div class="mb-6">
          <h2 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-3">
            Spicy Quotes
            <span class="text-stone-300 font-normal normal-case">(click to share)</span>
          </h2>
          <ul class="space-y-3">
            {#each post.money_quotes as quote, i}
              <li>
                <div
                  id="quote-{i}"
                  onclick={() => selectQuote(i)}
                  role="button"
                  tabindex="0"
                  onkeydown={(e) => e.key === 'Enter' && selectQuote(i)}
                  class="relative pl-4 pr-10 py-3 rounded-lg transition-all duration-300 cursor-pointer hover:shadow-md {highlightedQuote === i ? 'bg-amber-100 ring-2 ring-amber-400 shadow-md' : 'bg-stone-50 hover:bg-stone-100'}"
                >
                  <span class="absolute left-3 top-2 text-2xl {highlightedQuote === i ? 'text-amber-400' : 'text-blue-200'} font-serif">"</span>
                  <p class="font-serif text-stone-700 pl-4 pr-2">{quote}</p>
                  <button
                    onclick={(e) => copyQuoteLink(i, e)}
                    class="absolute right-2 top-1/2 -translate-y-1/2 p-1.5 rounded text-stone-400 hover:text-stone-600 hover:bg-stone-200 transition-colors"
                    title={copiedQuote === i ? 'Copied!' : 'Copy link to quote'}
                  >
                    {#if copiedQuote === i}
                      <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                      </svg>
                    {:else}
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/>
                      </svg>
                    {/if}
                  </button>
                </div>
              </li>
            {/each}
          </ul>
        </div>
      {/if}

      <!-- Tone -->
      {#if post.tone}
        <div class="mb-6">
          <h2 class="text-xs font-semibold text-stone-400 uppercase tracking-wider mb-2">Tone</h2>
          <p class="text-stone-600">{post.tone}</p>
        </div>
      {/if}
    </article>

    {#if data.transcriptHtml}
      <div class="bg-white rounded-2xl shadow-lg mt-6">
        <button
          onclick={() => showTranscript = !showTranscript}
          class="w-full flex items-center justify-between p-6
            text-stone-700 hover:text-stone-900 transition-colors"
        >
          <span class="text-sm font-semibold uppercase tracking-wider">
            {showTranscript ? 'Hide Transcript' : 'Read Transcript'}
          </span>
          <svg
            class="w-5 h-5 transition-transform duration-200
              {showTranscript ? 'rotate-180' : ''}"
            fill="none" stroke="currentColor" viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round" stroke-linejoin="round"
              stroke-width="2" d="M19 9l-7 7-7-7"
            />
          </svg>
        </button>
        {#if showTranscript}
          <div class="px-8 pb-8">
            <div class="prose prose-stone max-w-none">
              {@html data.transcriptHtml}
            </div>
          </div>
        {/if}
      </div>
    {/if}
  </div>
{:else}
  <div class="max-w-3xl lg:max-w-5xl mx-auto px-4 py-8">
    <div class="text-center py-16">
      <h1 class="text-2xl font-semibold text-stone-700 mb-4">Post not found</h1>
      <p class="text-stone-500 mb-6">The post you're looking for doesn't exist.</p>
      <a href="/" class="text-blue-600 hover:underline">Back to all posts</a>
    </div>
  </div>
{/if}
