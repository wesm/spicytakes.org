<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import Modal from '$lib/components/Modal.svelte';
  import { stats } from '$lib/data';
  import { config } from '$lib/config';

  let { children } = $props();
</script>

<svelte:head>
  <title>{config.name} - {config.tagline}</title>
  <meta name="description" content={config.description} />
</svelte:head>

<div class="min-h-screen flex flex-col">
  <Header />
  <main class="flex-1">
    {@render children()}
  </main>
  <footer class="border-t border-stone-200 py-8 text-center text-sm text-stone-500">
    <p>Exploring {stats.totalPosts} posts from <a href={config.sourceUrl} target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">{config.sourceLabel}</a></p>
    <p class="mt-1 text-stone-400">Built with LLM-powered analysis</p>
  </footer>
</div>

<Modal />
