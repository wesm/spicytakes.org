<script module lang="ts">
  declare const __GIT_HASH__: string;
</script>

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

  const gitHash = __GIT_HASH__;
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={description} />
</svelte:head>

{#if isLandingMode}
  <div class="layout">
    <main class="layout-main">
      {@render children()}
    </main>
    <footer class="layout-footer">
      <p class="footer-note">Curated archives with LLM-powered analysis</p>
      <p class="footer-hash">{gitHash}</p>
    </footer>
  </div>
{:else}
  <div class="layout">
    <Header />
    <main class="layout-main">
      {@render children()}
    </main>
    <footer class="layout-footer">
      <p>Exploring {$statsStore.totalPosts} posts from <a href={config?.sourceUrl} target="_blank" rel="noopener noreferrer" class="footer-link">{config?.sourceLabel}</a></p>
      <p class="footer-credit">
        Made with <span class="heart">&#10084;&#65039;</span> by <a href="https://wesmckinney.com" target="_blank" rel="noopener noreferrer">Wes McKinney</a>
      </p>
      <p class="footer-hash">{gitHash}</p>
    </footer>
  </div>
  <Modal />
{/if}

<style>
  .layout {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  .layout-main {
    flex: 1;
  }

  .layout-footer {
    border-top: 1px solid #e7e5e4;
    padding: 2rem 1.5rem;
    text-align: center;
    font-size: 0.875rem;
    color: #a8a29e;
  }

  .layout-footer a {
    color: #78716c;
    text-decoration: none;
    transition: color 0.15s;
  }
  .layout-footer a:hover {
    color: #dc2626;
  }

  .footer-link {
    font-weight: 500;
  }

  .footer-note {
    color: #a8a29e;
  }

  .footer-credit {
    margin-top: 0.5rem;
    color: #a8a29e;
  }

  .footer-hash {
    margin-top: 0.5rem;
    font-size: 0.78rem;
    color: #d6d3d1;
  }

  .heart {
    color: #ef4444;
  }
</style>
