<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import Modal from '$lib/components/Modal.svelte';

  let { children } = $props();
</script>

<svelte:head>
  <title>Benn Stancil - Spicy Takes</title>
  <meta name="description" content="Explore the intellectual arc of Benn Stancil's writing on data, analytics, startups, and tech." />
</svelte:head>

<div class="min-h-screen flex flex-col">
  <Header />
  <main class="flex-1">
    {@render children()}
  </main>
  <footer class="border-t border-stone-200 py-8 text-center text-sm text-stone-500">
    <p>Exploring 238 posts from <a href="https://benn.substack.com" target="_blank" class="text-blue-600 hover:underline">benn.substack.com</a></p>
    <p class="mt-1 text-stone-400">Built with LLM-powered analysis</p>
  </footer>
</div>

<Modal />
