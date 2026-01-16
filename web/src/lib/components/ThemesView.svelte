<script lang="ts">
  import { themes } from '$lib/data';
  import { activeThemes, activeView } from '$lib/stores';

  function selectTheme(themeName: string) {
    activeThemes.set(new Set([themeName]));
    activeView.set('timeline');
  }

  function getRandomQuotes(quotes: any[], count: number) {
    const shuffled = [...quotes].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
  }
</script>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
  {#each themes as theme}
    <button
      onclick={() => selectTheme(theme.name)}
      class="card card-hover text-left cursor-pointer"
    >
      <div class="flex items-start gap-3 mb-4">
        <span class="text-2xl">{theme.icon}</span>
        <div>
          <h3 class="text-lg font-semibold text-stone-900">{theme.label}</h3>
          <p class="text-sm text-stone-500">
            {theme.posts.length} posts, {theme.quotes.length} quotes
          </p>
        </div>
      </div>

      <div class="space-y-3 border-t border-stone-100 pt-4">
        {#each getRandomQuotes(theme.quotes, 2) as item}
          <p class="font-serif text-sm italic text-stone-600 line-clamp-2">
            "{item.quote}"
          </p>
        {/each}
      </div>

      <div class="mt-4 text-sm text-blue-600 font-medium">
        View all posts in this theme &rarr;
      </div>
    </button>
  {/each}
</div>

<style>
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
