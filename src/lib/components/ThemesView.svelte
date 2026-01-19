<script lang="ts">
  import { themes, years } from '$lib/data';
  import { activeThemes, activeView } from '$lib/stores';
  import { getSpicyColor, getSpicyTextColor } from '$lib/types';

  function selectTheme(themeName: string) {
    activeThemes.set(new Set([themeName]));
    activeView.set('quotes');
  }

  // Get top 3 spiciest quotes per theme
  function getTopSpicy(theme: typeof themes[0]) {
    return [...theme.quotes]
      .sort((a, b) => b.spiciness - a.spiciness)
      .slice(0, 3);
  }

  // Get avg spiciness per theme
  function getAvgSpiciness(theme: typeof themes[0]) {
    if (theme.quotes.length === 0) return 0;
    const total = theme.quotes.reduce((sum, q) => sum + q.spiciness, 0);
    return Math.round(total / theme.quotes.length * 10) / 10;
  }
</script>

<div class="space-y-6">
  <p class="text-sm text-stone-500">
    Click a theme to view its spiciest quotes
  </p>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
    {#each themes as theme}
      {@const topSpicy = getTopSpicy(theme)}
      {@const avgSpice = getAvgSpiciness(theme)}
      <button
        onclick={() => selectTheme(theme.name)}
        class="card card-hover text-left cursor-pointer"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="flex items-start gap-3">
            <span class="text-2xl">{theme.icon}</span>
            <div>
              <h3 class="text-lg font-semibold text-stone-900">{theme.label}</h3>
              <p class="text-sm text-stone-500">
                {theme.posts.length} posts, {theme.quotes.length} quotes
              </p>
            </div>
          </div>
          <div class="text-right">
            <div class="text-sm text-stone-400">Avg Spice</div>
            <div class="text-xl font-bold {getSpicyTextColor(avgSpice)}">{avgSpice}</div>
          </div>
        </div>

        <div class="space-y-3 border-t border-stone-100 pt-4">
          <div class="text-xs font-medium text-stone-400 uppercase tracking-wide">Top Spicy Takes</div>
          {#each topSpicy as q}
            <div class="flex items-start gap-2">
              <span class="flex-shrink-0 w-8 h-8 flex items-center justify-center rounded-full {getSpicyColor(q.spiciness)} text-xs font-bold" role="img" aria-label="Spiciness score: {q.spiciness} out of 10" title="Spiciness: {q.spiciness}/10">
                <span aria-hidden="true">🌶️{q.spiciness}</span>
              </span>
              <p class="font-serif text-sm text-stone-600 line-clamp-2">
                "{q.quote}"
              </p>
            </div>
          {/each}
        </div>

        <div class="mt-4 text-sm text-blue-600 font-medium">
          View all {theme.quotes.length} quotes &rarr;
        </div>
      </button>
    {/each}
  </div>
</div>

<style>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    line-clamp: 2;
  }
</style>