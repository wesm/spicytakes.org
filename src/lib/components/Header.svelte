<script lang="ts">
  import { searchQuery, activeThemes, clearFilters, themesStore } from '$lib/stores';
  import { base } from '$app/paths';
  import { config, landing } from '$lib/config';

  // Look up blogger photo from landing config
  const bloggerPhoto = landing.blogs.find(b => b.id === config?.id)?.photo;

  let searchValue = $state('');
  let searchTimeout: ReturnType<typeof setTimeout>;

  // Sync local searchValue with store (for when clearFilters is called)
  $effect(() => {
    if ($searchQuery === '' && searchValue !== '') {
      searchValue = '';
    }
  });

  function handleSearch(e: Event) {
    const value = (e.target as HTMLInputElement).value;
    searchValue = value;
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      searchQuery.set(value);
    }, 200);
  }

  function toggleTheme(theme: string) {
    activeThemes.update(themes => {
      const newThemes = new Set(themes);
      if (newThemes.has(theme)) {
        newThemes.delete(theme);
      } else {
        newThemes.add(theme);
      }
      return newThemes;
    });
  }
</script>

<header class="sticky top-0 z-50 bg-white/95 backdrop-blur-sm border-b border-stone-200">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <!-- Top bar -->
    <div class="flex items-center justify-between py-4">
      <div class="flex items-center gap-3">
        <!-- Spicy Takes logo and link -->
        <a href="https://spicytakes.org" class="flex items-center gap-1.5 hover:opacity-80 transition-opacity flex-shrink-0" aria-label="Spicy Takes home">
          <img src={`${base}/logo.jpeg`} alt="" aria-hidden="true" class="w-8 h-8 rounded-md" />
        </a>
        <span class="text-stone-300">|</span>
        <!-- Blogger photo and name -->
        <div class="flex items-center gap-2">
          {#if bloggerPhoto}
            <img src={`${base}${bloggerPhoto}`} alt={config?.name} class="w-8 h-8 rounded-full object-cover ring-1 ring-stone-200 flex-shrink-0" />
          {/if}
          <div class="flex flex-col sm:flex-row sm:items-center sm:gap-2">
            <h1 class="text-lg sm:text-xl font-bold tracking-tight text-stone-900">{config?.name}</h1>
            <span class="hidden sm:inline text-stone-400 font-medium">{config?.tagline}</span>
          </div>
        </div>
        <a href={config?.sourceUrl} target="_blank" rel="noopener noreferrer" class="hidden sm:inline text-blue-600 hover:text-blue-700 text-sm font-medium ml-auto">
          {config?.sourceLabel} →
        </a>
      </div>
    </div>

    <!-- Search and filters -->
    <div class="pb-4 space-y-3">
      <div class="relative max-w-md">
        <input
          type="text"
          placeholder="Search posts, quotes, insights..."
          value={searchValue}
          oninput={handleSearch}
          class="w-full pl-10 pr-4 py-2.5 bg-stone-50 border border-stone-200 rounded-lg text-sm placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
        />
        <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-stone-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <circle cx="11" cy="11" r="8" stroke-width="2"/>
          <path stroke-width="2" d="m21 21-4.35-4.35"/>
        </svg>
      </div>

      <!-- Theme pills -->
      <div class="flex flex-wrap gap-2">
        {#each $themesStore as theme}
          <button
            onclick={() => toggleTheme(theme.name)}
            class="theme-pill {$activeThemes.has(theme.name) ? 'theme-pill-active' : 'theme-pill-default'}"
          >
            <span class="mr-1">{theme.icon}</span>
            {theme.label}
            <span class="ml-1 opacity-60">({theme.posts.length})</span>
          </button>
        {/each}
        {#if $activeThemes.size > 0 || $searchQuery}
          <button
            onclick={clearFilters}
            class="theme-pill bg-red-50 text-red-600 hover:bg-red-100"
          >
            Clear filters
          </button>
        {/if}
      </div>
    </div>
  </div>
</header>
