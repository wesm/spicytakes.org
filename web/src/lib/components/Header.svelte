<script lang="ts">
  import { activeView, searchQuery, activeThemes, clearFilters } from '$lib/stores';
  import { themes } from '$lib/data';
  import { THEME_LABELS } from '$lib/types';

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

  function setView(view: 'timeline' | 'quotes' | 'themes') {
    activeView.set(view);
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
        <h1 class="text-xl font-bold tracking-tight text-stone-900">Benn Stancil</h1>
        <span class="hidden sm:inline text-stone-400 font-medium">Spicy Takes</span>
      </div>

      <!-- Navigation -->
      <nav class="flex gap-1 bg-stone-100 p-1 rounded-lg">
        <button
          onclick={() => setView('timeline')}
          class="px-4 py-2 text-sm font-medium rounded-md transition-all duration-150 {$activeView === 'timeline' ? 'bg-white text-stone-900 shadow-sm' : 'text-stone-600 hover:text-stone-900'}"
        >
          Timeline
        </button>
        <button
          onclick={() => setView('quotes')}
          class="px-4 py-2 text-sm font-medium rounded-md transition-all duration-150 {$activeView === 'quotes' ? 'bg-white text-stone-900 shadow-sm' : 'text-stone-600 hover:text-stone-900'}"
        >
          Quotes
        </button>
        <button
          onclick={() => setView('themes')}
          class="px-4 py-2 text-sm font-medium rounded-md transition-all duration-150 {$activeView === 'themes' ? 'bg-white text-stone-900 shadow-sm' : 'text-stone-600 hover:text-stone-900'}"
        >
          Themes
        </button>
      </nav>
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
        {#each themes as theme}
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
