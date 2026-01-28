<script lang="ts">
  import { onMount } from 'svelte';
  import { base } from '$app/paths';
  import {
    initDuckDB,
    getYearlyStats,
    getTopQuotes,
    getAuthorStats,
    getOverallStats,
    getQuotesForYear,
    getFilteredQuotes
  } from '$lib/duckdb';
  import embed from 'vega-embed';

  // Types
  type YearStats = {
    year: number;
    avg_spiciness: number;
    std_spiciness: number;
    quote_count: number;
    max_spiciness: number;
  };

  type Quote = {
    quote_text: string;
    spiciness: number;
    author_name: string;
    author_id: string;
    post_title: string;
    post_url: string;
    post_filename: string;
    post_year?: number;
    post_month?: number;
    themes: string[];
  };

  type AuthorStats = {
    author_id: string;
    author_name: string;
    quote_count: number;
    avg_spiciness: number;
    max_spiciness: number;
    perfect_10s: number;
  };

  type OverallStats = {
    total_quotes: number;
    total_authors: number;
    avg_spiciness: number;
    min_year: number;
    max_year: number;
    perfect_10s: number;
  };

  // State
  let loading = $state(true);
  let error = $state<string | null>(null);
  let yearlyStats = $state<YearStats[]>([]);
  let allTimeQuotes = $state<Quote[]>([]);
  let displayedQuotes = $state<Quote[]>([]);
  let allTimeAuthorStats = $state<AuthorStats[]>([]);
  let displayedAuthorStats = $state<AuthorStats[]>([]);
  let overallStats = $state<OverallStats | null>(null);

  // Filter state
  let selectedYear = $state<number | null>(null);
  let selectedAuthor = $state<{ id: string; name: string } | null>(null);
  let loadingData = $state(false);

  // Chart container ref
  let chartContainer: HTMLDivElement;

  // Responsive state for mobile detection
  let isMobile = $state(false);

  // Check if mobile on mount and resize
  function checkMobile() {
    isMobile = window.innerWidth < 768;
  }

  // Build permalink to author's spicytakes site
  function getPermalink(quote: Quote): string {
    const filename = quote.post_filename?.replace('.md', '') || '';
    return `https://${quote.author_id}.spicytakes.org/post/${filename}`;
  }

  // Render Vega-Lite chart when data is ready
  async function renderChart(selected: number | null = null, mobile: boolean = false) {
    if (!chartContainer || yearlyStats.length === 0) return;

    // Add selection state to data
    const dataWithSelection = yearlyStats.map(d => ({
      ...d,
      isSelected: selected === null || d.year === selected
    }));

    // Common encoding properties
    const colorEncoding = {
      condition: {
        test: 'datum.isSelected',
        field: 'avg_spiciness',
        type: 'quantitative',
        scale: {
          domain: [3, 5, 7, 10],
          range: ['#22c55e', '#eab308', '#f97316', '#ef4444']
        },
        legend: null
      },
      value: '#d6d3d1'  // Gray for unselected
    };

    const opacityEncoding = {
      condition: {
        test: 'datum.isSelected',
        value: 1
      },
      value: 0.4
    };

    const tooltipEncoding = [
      { field: 'year', title: 'Year' },
      { field: 'avg_spiciness', title: 'Avg Spiciness', format: '.1f' },
      { field: 'quote_count', title: 'Quotes', format: ',' }
    ];

    // Build spec based on mobile vs desktop
    const spec = mobile ? {
      // Mobile: horizontal bar chart, taller
      $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
      data: { values: dataWithSelection },
      width: 'container',
      height: Math.max(400, yearlyStats.length * 20),
      mark: {
        type: 'bar',
        cornerRadiusBottomRight: 3,
        cornerRadiusTopRight: 3,
        cursor: 'pointer'
      },
      encoding: {
        y: {
          field: 'year',
          type: 'ordinal',
          sort: 'descending',
          axis: {
            title: null,
            labelFontSize: 11
          }
        },
        x: {
          field: 'avg_spiciness',
          type: 'quantitative',
          scale: { domain: [0, 10] },
          axis: {
            title: null,
            grid: true,
            gridDash: [2, 2]
          }
        },
        color: colorEncoding,
        opacity: opacityEncoding,
        tooltip: tooltipEncoding
      },
      config: {
        view: { stroke: null },
        axis: { domainColor: '#d6d3d1', tickColor: '#d6d3d1' },
        background: 'transparent'
      }
    } : {
      // Desktop: vertical bar chart
      $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
      data: { values: dataWithSelection },
      width: 'container',
      height: 180,
      mark: {
        type: 'bar',
        cornerRadiusTopLeft: 3,
        cornerRadiusTopRight: 3,
        cursor: 'pointer'
      },
      encoding: {
        x: {
          field: 'year',
          type: 'ordinal',
          axis: {
            title: null,
            labelAngle: -45,
            labelFontSize: 10
          }
        },
        y: {
          field: 'avg_spiciness',
          type: 'quantitative',
          scale: { domain: [0, 10] },
          axis: {
            title: null,
            grid: true,
            gridDash: [2, 2]
          }
        },
        color: colorEncoding,
        opacity: opacityEncoding,
        tooltip: tooltipEncoding
      },
      config: {
        view: { stroke: null },
        axis: { domainColor: '#d6d3d1', tickColor: '#d6d3d1' },
        background: 'transparent'
      }
    };

    const result = await embed(chartContainer, spec as any, {
      actions: false,
      renderer: 'svg'
    });

    // Handle click events for drill-down
    result.view.addEventListener('click', (_event: any, item: any) => {
      if (item?.datum?.year) {
        handleYearClick(item.datum.year);
      }
    });
  }

  // Re-render chart when data, selection, or screen size changes
  $effect(() => {
    if (yearlyStats.length > 0 && chartContainer) {
      renderChart(selectedYear, isMobile);
    }
  });

  // Load data on mount
  onMount(async () => {
    // Set up responsive detection
    checkMobile();
    window.addEventListener('resize', checkMobile);

    try {
      await initDuckDB();

      // Load all data in parallel
      const [yearly, quotes, authors, overall] = await Promise.all([
        getYearlyStats(),
        getTopQuotes(100),
        getAuthorStats(),
        getOverallStats()
      ]);

      yearlyStats = yearly;
      allTimeQuotes = quotes;
      displayedQuotes = quotes;
      allTimeAuthorStats = authors;
      displayedAuthorStats = authors;
      overallStats = overall;
      loading = false;
    } catch (e) {
      error = e instanceof Error ? e.message : 'Failed to load analytics';
      loading = false;
    }

    return () => {
      window.removeEventListener('resize', checkMobile);
    };
  });

  // Refresh displayed quotes based on current filters
  async function refreshQuotes() {
    loadingData = true;
    try {
      if (!selectedYear && !selectedAuthor) {
        // No filters - use cached all-time data
        displayedQuotes = allTimeQuotes;
      } else {
        // Apply filters
        displayedQuotes = await getFilteredQuotes({
          authorId: selectedAuthor?.id,
          year: selectedYear ?? undefined,
          limit: 100
        });
      }
    } catch (e) {
      console.error('Failed to load filtered data:', e);
    }
    loadingData = false;
  }

  // Handle year click
  async function handleYearClick(year: number) {
    if (selectedYear === year) {
      // Toggle off - remove just year filter
      selectedYear = null;
    } else {
      selectedYear = year;
    }

    loadingData = true;
    try {
      // Update author stats for the year (or all time if no year selected)
      displayedAuthorStats = await getAuthorStats(selectedYear ?? undefined);
      // Refresh quotes with current filters
      await refreshQuotes();
    } catch (e) {
      console.error('Failed to load year data:', e);
    }
    loadingData = false;
  }

  // Handle author click for filtering
  async function handleAuthorClick(authorId: string, authorName: string) {
    if (selectedAuthor?.id === authorId) {
      // Toggle off - remove just author filter
      selectedAuthor = null;
    } else {
      selectedAuthor = { id: authorId, name: authorName };
    }

    await refreshQuotes();
  }

  // Reset filter to show all time
  function resetFilter() {
    selectedYear = null;
    selectedAuthor = null;
    displayedQuotes = allTimeQuotes;
    displayedAuthorStats = allTimeAuthorStats;
  }

  // Spiciness badge color (light background, dark text) - matches sub-site
  function getSpicyBadgeColor(spiciness: number): string {
    if (spiciness >= 10) return 'bg-red-200 text-red-800';
    if (spiciness >= 8) return 'bg-red-100 text-red-700';
    if (spiciness >= 6) return 'bg-orange-100 text-orange-700';
    if (spiciness >= 4) return 'bg-yellow-100 text-yellow-700';
    return 'bg-green-100 text-green-700';
  }

  function getSpicyTextColor(spiciness: number): string {
    if (spiciness >= 8) return 'text-red-600';
    if (spiciness >= 6) return 'text-orange-600';
    if (spiciness >= 4) return 'text-yellow-600';
    return 'text-green-600';
  }
</script>

<svelte:head>
  <title>Spicy Takes Analytics</title>
  <meta name="description" content="Analytics dashboard for spicy takes across tech blogs" />
</svelte:head>

<div class="min-h-screen bg-gradient-to-b from-stone-50 to-white">
  <!-- Header -->
  <header class="pt-8 pb-6 px-6 text-center border-b border-stone-200">
    <div class="max-w-5xl mx-auto">
      <a href="{base}/" class="inline-block mb-3 text-stone-500 hover:text-stone-700 text-sm">
        ← Back to Spicy Takes
      </a>
      <h1 class="text-3xl md:text-4xl font-bold text-stone-900 mb-2">
        🌶️ Spicy Analytics
      </h1>
      <p class="text-stone-600">
        {overallStats?.total_quotes?.toLocaleString() ?? '...'} quotes across {overallStats?.total_authors ?? '...'} authors
      </p>
    </div>
  </header>

  {#if loading}
    <div class="flex items-center justify-center py-32">
      <p class="text-stone-500">Loading...</p>
    </div>
  {:else if error}
    <div class="max-w-2xl mx-auto px-6 py-16 text-center">
      <p class="text-red-600 font-medium">Error: {error}</p>
    </div>
  {:else}
    <main class="max-w-6xl mx-auto px-6 py-8">

      <!-- Top row: Bar chart + Leaderboard side by side -->
      <div class="grid lg:grid-cols-3 gap-6 mb-8">
        <!-- Bar Chart (2/3 width) -->
        <div class="lg:col-span-2 bg-white rounded-xl shadow-sm border border-stone-200 p-4">
          <h2 class="text-lg font-semibold text-stone-900 mb-3">Spiciness by Year</h2>
          <div bind:this={chartContainer} class="w-full"></div>
          <p class="text-xs text-stone-400 mt-2">Click a bar to filter quotes</p>
        </div>

        <!-- Author Leaderboard (1/3 width) -->
        <div class="bg-white rounded-xl shadow-sm border border-stone-200 overflow-hidden">
          <div class="px-4 py-3 border-b border-stone-100 flex items-center justify-between">
            <div class="flex items-center gap-2">
              <h2 class="text-lg font-semibold text-stone-900">👑 Leaderboard</h2>
              <span class="text-xs text-stone-400">(Click to filter)</span>
            </div>
            {#if selectedYear}
              <span class="text-xs text-stone-400">{selectedYear}</span>
            {/if}
          </div>
          <div class="max-h-64 overflow-y-auto">
            <table class="w-full text-sm">
              <thead class="bg-stone-50 border-b border-stone-100 sticky top-0">
                <tr class="text-xs text-stone-500">
                  <th class="px-2 py-1.5 text-left w-8"></th>
                  <th class="py-1.5 text-left">Author</th>
                  <th class="px-2 py-1.5 text-right">Avg</th>
                  <th class="px-2 py-1.5 text-right">#</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-stone-100">
                {#each displayedAuthorStats.slice(0, 15) as author, i}
                  <tr
                    class="cursor-pointer transition-colors {selectedAuthor?.id === author.author_id ? 'bg-red-50' : 'hover:bg-stone-50'}"
                    onclick={() => handleAuthorClick(author.author_id, author.author_name)}
                  >
                    <td class="px-2 py-1.5 w-8">
                      {#if i < 3}
                        <span class="text-sm">{['🥇', '🥈', '🥉'][i]}</span>
                      {:else}
                        <span class="text-stone-400 text-xs">{i + 1}</span>
                      {/if}
                    </td>
                    <td class="py-1.5">
                      <span class="text-stone-800 font-medium text-sm {selectedAuthor?.id === author.author_id ? 'text-red-700' : 'hover:text-red-600'}">
                        {author.author_name}
                      </span>
                    </td>
                    <td class="px-2 py-1.5 text-right">
                      <span class="font-semibold {getSpicyTextColor(author.avg_spiciness)}">{author.avg_spiciness}</span>
                    </td>
                    <td class="px-2 py-1.5 text-right text-stone-400 text-xs">
                      {author.quote_count}
                    </td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Quotes Table -->
      <div class="bg-white rounded-xl shadow-sm border border-stone-200">
        <!-- Header with filter status -->
        <div class="px-4 py-3 border-b border-stone-200 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <h2 class="text-lg font-semibold text-stone-900">
              🔥 Spiciest Quotes
            </h2>
            {#if selectedYear}
              <span class="px-2 py-1 bg-red-100 text-red-700 text-sm font-medium rounded-lg">
                {selectedYear}
              </span>
            {/if}
            {#if selectedAuthor}
              <span class="px-2 py-1 bg-orange-100 text-orange-700 text-sm font-medium rounded-lg">
                {selectedAuthor.name}
              </span>
            {/if}
            {#if selectedYear || selectedAuthor}
              <button
                onclick={resetFilter}
                class="text-sm text-stone-500 hover:text-stone-700 underline"
              >
                Reset
              </button>
            {:else}
              <span class="text-sm text-stone-500">All Time</span>
            {/if}
          </div>
          <span class="text-sm text-stone-400">{displayedQuotes.length} quotes</span>
        </div>

        <!-- Quotes list -->
        {#if loadingData}
          <div class="p-8 text-center text-stone-500">Loading...</div>
        {:else}
          <div class="divide-y divide-stone-100 max-h-[600px] overflow-y-auto">
            {#each displayedQuotes as quote, i}
              <div class="flex items-start gap-3 px-4 py-3 hover:bg-stone-50">
                <!-- Rank -->
                <div class="w-8 text-center flex-shrink-0">
                  {#if i < 3 && !selectedYear}
                    <span class="text-lg">{['🥇', '🥈', '🥉'][i]}</span>
                  {:else}
                    <span class="text-stone-400 text-sm">{i + 1}</span>
                  {/if}
                </div>

                <!-- Spiciness badge -->
                <div class="flex-shrink-0 w-10 h-10 flex items-center justify-center rounded-full {getSpicyBadgeColor(quote.spiciness)} font-bold text-xs">
                  🌶️{quote.spiciness}
                </div>

                <!-- Quote content -->
                <div class="flex-1 min-w-0">
                  <p class="text-stone-800 text-sm leading-relaxed">"{quote.quote_text.length > 250 ? quote.quote_text.slice(0, 250) + '...' : quote.quote_text}"</p>
                  <div class="mt-1.5 flex flex-wrap items-center gap-2 text-xs text-stone-500">
                    <span class="font-medium text-stone-700">{quote.author_name}</span>
                    <span class="text-stone-300">•</span>
                    <span>{quote.post_year}</span>
                    <span class="text-stone-300">•</span>
                    <span class="truncate max-w-48">{quote.post_title}</span>
                  </div>
                </div>

                <!-- Permalink -->
                <a
                  href={getPermalink(quote)}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="flex-shrink-0 p-2 text-stone-400 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                  title="View on {quote.author_name}'s Spicy Takes"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                </a>
              </div>
            {/each}
          </div>
        {/if}
      </div>

    </main>
  {/if}

  <!-- Footer -->
  <footer class="border-t border-stone-200 py-6 text-center text-sm text-stone-500">
    <p>
      Powered by <a href="https://duckdb.org/docs/api/wasm/overview" target="_blank" rel="noopener noreferrer" class="text-blue-600 hover:underline">DuckDB-WASM</a> 🦆
    </p>
  </footer>
</div>
