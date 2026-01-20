<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import Modal from '$lib/components/Modal.svelte';
  import { config, isLandingMode, landing } from '$lib/config';

  let { children } = $props();

  // Only import stats in blog mode (not landing)
  let stats = $state({ totalPosts: 0 });
  if (!isLandingMode) {
    import('$lib/data').then(m => { stats = m.stats; });
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
      <p>Exploring {stats.totalPosts} posts from <a href={config?.sourceUrl} target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">{config?.sourceLabel}</a></p>
      <p class="mt-1 text-stone-400">Built with LLM-powered analysis</p>
    </footer>
  </div>
  <Modal />
{/if}
