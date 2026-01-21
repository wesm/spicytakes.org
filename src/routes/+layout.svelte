<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import Modal from '$lib/components/Modal.svelte';
  import { config, isLandingMode, landing } from '$lib/config';
  import { statsStore } from '$lib/stores';
  import { initializeData } from '$lib/data';
  import type { LayoutData } from './$types';

  let { children, data }: { children: any; data: LayoutData } = $props();

  // Initialize stores from server data synchronously (runs during SSR and hydration)
  // Note: data.blogData is set once by SvelteKit and doesn't change, so synchronous access is safe
  // svelte-ignore state_referenced_locally
  if (data.blogData) {
    initializeData(data.blogData);
  }

  const title = isLandingMode ? `${landing.title} - ${landing.tagline}` : `${config?.name} - ${config?.tagline}`;
  const description = isLandingMode ? landing.description : config?.description;
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />
</svelte:head>

{#if isLandingMode}
  <div class="min-h-screen flex flex-col">
    <main class="flex-1">
      {@render children()}
    </main>
    <footer class="border-t border-stone-200 py-8 text-center text-sm text-stone-500">
      <p class="text-stone-400">Curated archives with LLM-powered analysis</p>
    </footer>
  </div>
{:else}
  <div class="min-h-screen flex flex-col">
    <Header />
    <main class="flex-1">
      {@render children()}
    </main>
    <footer class="border-t border-stone-200 py-8 text-center text-sm text-stone-500">
      <p>Exploring {$statsStore.totalPosts} posts from <a href={config?.sourceUrl} target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">{config?.sourceLabel}</a></p>
      <p class="mt-2 text-stone-400">
        Made with <span class="text-red-500">❤️</span> by <a href="https://wesmckinney.com" target="_blank" rel="noopener noreferrer" class="text-stone-500 hover:text-red-500 transition-colors">Wes McKinney</a>
      </p>
    </footer>
  </div>
  <Modal />
{/if}
