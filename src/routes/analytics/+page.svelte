<script lang="ts">
  import { onMount } from 'svelte';
  import { base } from '$app/paths';
  import { heatColor } from '$lib/types';
  import {
    initDuckDB,
    getYearlyStats,
    getMonthlyStats,
    getTopQuotes,
    getAuthorStats,
    getOverallStats,
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

  type MonthlyStats = {
    year: number;
    month: number;
    avg_spiciness: number;
    quote_count: number;
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
  let selectedMonth = $state<{
    year: number; month: number
  } | null>(null);
  let selectedAuthor = $state<{
    id: string; name: string
  } | null>(null);
  let loadingData = $state(false);

  // Chart mode toggle
  let chartMode = $state<'yearly' | 'monthly'>('yearly');
  let displayedYearlyStats = $state<YearStats[]>([]);
  let displayedMonthlyStats = $state<MonthlyStats[]>([]);

  // Chart container ref and Vega view tracking
  let chartContainer = $state<HTMLDivElement>(undefined!);
  let currentView: any = null;
  let renderToken = 0;

  // Responsive state
  let isMobile = $state(false);
  let resizeObserver: ResizeObserver | null = null;

  let resizeTimeout: ReturnType<typeof setTimeout> | null = null;
  function handleResize() {
    if (resizeTimeout) clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      const wasMobile = isMobile;
      isMobile = window.innerWidth < 768;
      const data = chartMode === 'monthly'
        ? displayedMonthlyStats : displayedYearlyStats;
      if (wasMobile === isMobile
        && data.length > 0 && chartContainer) {
        renderChart(isMobile);
      }
    }, 100);
  }

  function getPermalink(quote: Quote): string {
    const filename =
      quote.post_filename?.replace('.md', '') || '';
    return `https://${quote.author_id}.spicytakes.org/post/${filename}`;
  }

  const monthNames = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
  ];

  async function refreshChartData() {
    try {
      const authorId = selectedAuthor?.id;
      if (chartMode === 'monthly') {
        displayedMonthlyStats =
          await getMonthlyStats(authorId);
      } else {
        displayedYearlyStats = authorId
          ? await getYearlyStats(authorId) : yearlyStats;
      }
    } catch (e) {
      console.error('Failed to refresh chart data:', e);
    }
  }

  async function renderChart(mobile: boolean = false) {
    if (!chartContainer) return;

    const isMonthly = chartMode === 'monthly';
    const sourceData = isMonthly
      ? displayedMonthlyStats : displayedYearlyStats;
    if (sourceData.length === 0) return;

    const thisRender = ++renderToken;

    if (currentView) {
      currentView.finalize();
      currentView = null;
    }

    const hoverParam = {
      name: 'hover',
      select: {
        type: 'point',
        on: 'pointerover',
        clear: 'pointerout'
      }
    };

    const colorEncoding = {
      condition: {
        test: 'datum.isSelected',
        field: 'avg_spiciness',
        type: 'quantitative',
        scale: {
          domain: [3, 5, 7, 10],
          range: ['#16a34a', '#d97706', '#ea580c', '#dc2626']
        },
        legend: null
      },
      value: '#d6d3d1'
    };

    const opacityEncoding = {
      condition: [
        { param: 'hover', empty: false, value: 0.85 },
        { test: 'datum.isSelected', value: 1 }
      ],
      value: 0.4
    };

    const strokeWidthEncoding = {
      condition: {
        param: 'hover', empty: false, value: 1.5
      },
      value: 0
    };

    const strokeEncoding = {
      condition: {
        param: 'hover', empty: false, value: '#78716c'
      },
      value: null
    };

    let spec: any;

    if (isMonthly) {
      const selectedSortKey = selectedMonth
        ? selectedMonth.year * 100 + selectedMonth.month
        : null;

      const monthlyData = displayedMonthlyStats.map(d => {
        const sortKey = d.year * 100 + d.month;
        return {
          ...d,
          label: `${monthNames[d.month - 1]} ${d.year}`,
          sortKey,
          isSelected:
            selectedSortKey === null
            || sortKey === selectedSortKey
        };
      });

      const tooltipEncoding = [
        { field: 'label', title: 'Month' },
        {
          field: 'avg_spiciness',
          title: 'Avg Spiciness', format: '.1f'
        },
        {
          field: 'quote_count',
          title: 'Quotes', format: ','
        }
      ];

      const yearBoundaryLabelExpr =
        "slice(datum.value, 0, 3) === 'Jan'"
        + " ? slice(datum.value, 4) : ''";

      spec = mobile ? {
        $schema:
          'https://vega.github.io/schema/vega-lite/v5.json',
        data: { values: monthlyData },
        params: [hoverParam],
        width: 'container',
        height: Math.max(400, monthlyData.length * 16),
        autosize: { type: 'fit', contains: 'padding' },
        mark: {
          type: 'bar',
          cornerRadiusBottomRight: 3,
          cornerRadiusTopRight: 3,
          cursor: 'pointer'
        },
        encoding: {
          y: {
            field: 'label', type: 'ordinal',
            sort: {
              field: 'sortKey', order: 'descending'
            },
            axis: {
              title: null, labelFontSize: 10,
              labelExpr: yearBoundaryLabelExpr
            }
          },
          x: {
            field: 'avg_spiciness',
            type: 'quantitative',
            scale: { domain: [0, 10] },
            axis: {
              title: null, grid: true, gridDash: [2, 2]
            }
          },
          color: colorEncoding,
          opacity: opacityEncoding,
          strokeWidth: strokeWidthEncoding,
          stroke: strokeEncoding,
          tooltip: tooltipEncoding
        },
        config: {
          view: { stroke: null },
          axis: {
            domainColor: '#d6d3d1',
            tickColor: '#d6d3d1'
          },
          background: 'transparent'
        }
      } : {
        $schema:
          'https://vega.github.io/schema/vega-lite/v5.json',
        data: { values: monthlyData },
        params: [hoverParam],
        width: 'container',
        height: 180,
        autosize: { type: 'fit', contains: 'padding' },
        mark: {
          type: 'bar',
          cornerRadiusTopLeft: 3,
          cornerRadiusTopRight: 3,
          cursor: 'pointer'
        },
        encoding: {
          x: {
            field: 'label', type: 'ordinal',
            sort: { field: 'sortKey' },
            axis: {
              title: null, labelAngle: 0,
              labelFontSize: 10,
              labelExpr: yearBoundaryLabelExpr
            }
          },
          y: {
            field: 'avg_spiciness',
            type: 'quantitative',
            scale: { domain: [0, 10] },
            axis: {
              title: null, grid: true, gridDash: [2, 2]
            }
          },
          color: colorEncoding,
          opacity: opacityEncoding,
          strokeWidth: strokeWidthEncoding,
          stroke: strokeEncoding,
          tooltip: tooltipEncoding
        },
        config: {
          view: { stroke: null },
          axis: {
            domainColor: '#d6d3d1',
            tickColor: '#d6d3d1'
          },
          background: 'transparent'
        }
      };
    } else {
      const dataWithSelection =
        displayedYearlyStats.map(d => ({
          ...d,
          isSelected:
            selectedYear === null || d.year === selectedYear
        }));

      const tooltipEncoding = [
        { field: 'year', title: 'Year' },
        {
          field: 'avg_spiciness',
          title: 'Avg Spiciness', format: '.1f'
        },
        {
          field: 'quote_count',
          title: 'Quotes', format: ','
        }
      ];

      spec = mobile ? {
        $schema:
          'https://vega.github.io/schema/vega-lite/v5.json',
        data: { values: dataWithSelection },
        params: [hoverParam],
        width: 'container',
        height: Math.max(
          400, displayedYearlyStats.length * 20
        ),
        autosize: { type: 'fit', contains: 'padding' },
        mark: {
          type: 'bar',
          cornerRadiusBottomRight: 3,
          cornerRadiusTopRight: 3,
          cursor: 'pointer'
        },
        encoding: {
          y: {
            field: 'year', type: 'ordinal',
            sort: 'descending',
            axis: { title: null, labelFontSize: 11 }
          },
          x: {
            field: 'avg_spiciness',
            type: 'quantitative',
            scale: { domain: [0, 10] },
            axis: {
              title: null, grid: true, gridDash: [2, 2]
            }
          },
          color: colorEncoding,
          opacity: opacityEncoding,
          strokeWidth: strokeWidthEncoding,
          stroke: strokeEncoding,
          tooltip: tooltipEncoding
        },
        config: {
          view: { stroke: null },
          axis: {
            domainColor: '#d6d3d1',
            tickColor: '#d6d3d1'
          },
          background: 'transparent'
        }
      } : {
        $schema:
          'https://vega.github.io/schema/vega-lite/v5.json',
        data: { values: dataWithSelection },
        params: [hoverParam],
        width: 'container',
        height: 180,
        autosize: { type: 'fit', contains: 'padding' },
        mark: {
          type: 'bar',
          cornerRadiusTopLeft: 3,
          cornerRadiusTopRight: 3,
          cursor: 'pointer'
        },
        encoding: {
          x: {
            field: 'year', type: 'ordinal',
            axis: {
              title: null, labelAngle: -45,
              labelFontSize: 10
            }
          },
          y: {
            field: 'avg_spiciness',
            type: 'quantitative',
            scale: { domain: [0, 10] },
            axis: {
              title: null, grid: true, gridDash: [2, 2]
            }
          },
          color: colorEncoding,
          opacity: opacityEncoding,
          strokeWidth: strokeWidthEncoding,
          stroke: strokeEncoding,
          tooltip: tooltipEncoding
        },
        config: {
          view: { stroke: null },
          axis: {
            domainColor: '#d6d3d1',
            tickColor: '#d6d3d1'
          },
          background: 'transparent'
        }
      };
    }

    const result = await embed(
      chartContainer, spec as any,
      {
        actions: false,
        renderer: 'svg',
        padding: { left: 5, right: 5, top: 5, bottom: 5 }
      }
    );

    if (thisRender !== renderToken) {
      result.view.finalize();
      return;
    }

    currentView = result.view;

    result.view.addEventListener(
      'click', (_event: any, item: any) => {
        if (!item?.datum) return;
        if (isMonthly
          && item.datum.year && item.datum.month) {
          handleMonthClick(
            item.datum.year, item.datum.month
          );
        } else if (item.datum.year) {
          handleYearClick(item.datum.year);
        }
      }
    );
  }

  $effect(() => {
    const _yearly = displayedYearlyStats;
    const _monthly = displayedMonthlyStats;
    const _mode = chartMode;
    const _year = selectedYear;
    const _month = selectedMonth;
    const _mobile = isMobile;

    const data = _mode === 'monthly'
      ? _monthly : _yearly;
    if (chartContainer && data.length > 0) {
      renderChart(_mobile);
    }
  });

  onMount(async () => {
    isMobile = window.innerWidth < 768;
    window.addEventListener('resize', handleResize);

    resizeObserver = new ResizeObserver(() => {
      if (yearlyStats.length > 0) handleResize();
    });

    try {
      await initDuckDB();

      const [yearly, quotes, authors, overall] =
        await Promise.all([
          getYearlyStats(),
          getTopQuotes(100),
          getAuthorStats(),
          getOverallStats()
        ]);

      yearlyStats = yearly;
      displayedYearlyStats = yearly;
      allTimeQuotes = quotes;
      displayedQuotes = quotes;
      allTimeAuthorStats = authors;
      displayedAuthorStats = authors;
      overallStats = overall;
      loading = false;

      if (chartContainer) {
        resizeObserver?.observe(chartContainer);
      }
    } catch (e) {
      error = e instanceof Error
        ? e.message : 'Failed to load analytics';
      loading = false;
    }

    return () => {
      window.removeEventListener('resize', handleResize);
      if (resizeTimeout) clearTimeout(resizeTimeout);
      resizeObserver?.disconnect();
      if (currentView) currentView.finalize();
    };
  });

  async function refreshQuotes() {
    loadingData = true;
    try {
      if (!selectedYear
        && !selectedMonth && !selectedAuthor) {
        displayedQuotes = allTimeQuotes;
      } else {
        displayedQuotes = await getFilteredQuotes({
          authorId: selectedAuthor?.id,
          year: selectedMonth?.year
            ?? selectedYear ?? undefined,
          month: selectedMonth?.month,
          limit: 100
        });
      }
    } catch (e) {
      console.error('Failed to load filtered data:', e);
    }
    loadingData = false;
  }

  async function handleYearClick(year: number) {
    if (selectedYear === year) {
      selectedYear = null;
    } else {
      selectedYear = year;
    }
    selectedMonth = null;

    loadingData = true;
    try {
      displayedAuthorStats =
        await getAuthorStats(selectedYear ?? undefined);
      await refreshQuotes();
    } catch (e) {
      console.error('Failed to load year data:', e);
    }
    loadingData = false;
  }

  async function handleMonthClick(
    year: number, month: number
  ) {
    if (selectedMonth?.year === year
      && selectedMonth?.month === month) {
      selectedMonth = null;
      selectedYear = null;
    } else {
      selectedMonth = { year, month };
      selectedYear = year;
    }

    loadingData = true;
    try {
      displayedAuthorStats =
        await getAuthorStats(selectedYear ?? undefined);
      await refreshQuotes();
    } catch (e) {
      console.error('Failed to load month data:', e);
    }
    loadingData = false;
  }

  async function handleAuthorClick(
    authorId: string, authorName: string
  ) {
    if (selectedAuthor?.id === authorId) {
      selectedAuthor = null;
    } else {
      selectedAuthor = { id: authorId, name: authorName };
    }
    await Promise.all([
      refreshChartData(), refreshQuotes()
    ]);
  }

  async function resetFilter() {
    selectedYear = null;
    selectedMonth = null;
    selectedAuthor = null;
    displayedYearlyStats = yearlyStats;
    displayedQuotes = allTimeQuotes;
    displayedAuthorStats = allTimeAuthorStats;
    if (chartMode === 'monthly') {
      try {
        displayedMonthlyStats =
          await getMonthlyStats();
      } catch (e) {
        console.error(
          'Failed to refresh monthly stats:', e
        );
        displayedMonthlyStats = [];
      }
    }
  }
</script>

<svelte:head>
  <title>Spicy Analytics</title>
  <meta name="description" content="Analytics dashboard for spicy takes across tech blogs" />
</svelte:head>

<div class="analytics-page">
  <!-- Header -->
  <header class="page-header">
    <div class="header-inner">
      <a href="{base}/" class="back-link">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 19l-7-7 7-7"/></svg>
        Back to Spicy Takes
      </a>
      <h1 class="page-title">Spicy Analytics</h1>
      <p class="page-subtitle">
        {overallStats?.total_quotes?.toLocaleString() ?? '...'} quotes across {overallStats?.total_authors ?? '...'} authors
      </p>
    </div>
  </header>

  {#if loading}
    <div class="loading-state">
      <p>Loading analytics...</p>
    </div>
  {:else if error}
    <div class="error-state">
      <p>Error: {error}</p>
    </div>
  {:else}
    <main class="page-main">

      <!-- Top row: Chart + Leaderboard -->
      <div class="top-row">
        <!-- Bar Chart -->
        <div class="chart-panel">
          <div class="panel-header">
            <div class="panel-title-row">
              <h2 class="panel-title">Spiciness</h2>
              {#if selectedAuthor}
                <span class="filter-badge author">
                  {selectedAuthor.name}
                  <button
                    onclick={() => handleAuthorClick(selectedAuthor!.id, selectedAuthor!.name)}
                    class="badge-dismiss"
                    title="Remove author filter"
                  >x</button>
                </span>
              {/if}
            </div>
            <div class="mode-toggle">
              <button
                onclick={async () => { chartMode = 'yearly'; selectedMonth = null; await refreshChartData(); }}
                class="mode-btn"
                class:active={chartMode === 'yearly'}
              >Yearly</button>
              <button
                onclick={async () => { chartMode = 'monthly'; selectedYear = null; selectedMonth = null; await refreshChartData(); }}
                class="mode-btn"
                class:active={chartMode === 'monthly'}
              >Monthly</button>
            </div>
          </div>
          <div bind:this={chartContainer} class="chart-container"></div>
          <p class="chart-hint">Click a bar to filter quotes</p>
        </div>

        <!-- Author Leaderboard -->
        <div class="leaderboard-panel">
          <div class="panel-header leaderboard-header">
            <div class="panel-title-row">
              <h2 class="panel-title">Leaderboard</h2>
              <span class="panel-hint">Click to filter</span>
            </div>
            {#if selectedYear}
              <span class="year-indicator">{selectedYear}</span>
            {/if}
          </div>
          <div class="leaderboard-scroll">
            <table class="leaderboard-table">
              <thead>
                <tr>
                  <th class="col-rank"></th>
                  <th class="col-name">Author</th>
                  <th class="col-avg">Avg</th>
                  <th class="col-count">#</th>
                </tr>
              </thead>
              <tbody>
                {#each displayedAuthorStats as author, i}
                  <tr
                    class="author-row"
                    class:selected={selectedAuthor?.id === author.author_id}
                    onclick={() => handleAuthorClick(author.author_id, author.author_name)}
                  >
                    <td class="col-rank">
                      {#if i < 3}
                        <span class="rank-medal rank-{i + 1}">{i + 1}</span>
                      {:else}
                        <span class="rank-num">{i + 1}</span>
                      {/if}
                    </td>
                    <td class="col-name">
                      <span class="author-name">{author.author_name}</span>
                    </td>
                    <td class="col-avg">
                      <span class="avg-score" style="color: {heatColor(author.avg_spiciness)}">{author.avg_spiciness}</span>
                    </td>
                    <td class="col-count">{author.quote_count}</td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Quotes Table -->
      <div class="quotes-panel">
        <div class="panel-header quotes-header">
          <div class="panel-title-row">
            <h2 class="panel-title">Spiciest Quotes</h2>
            {#if selectedMonth}
              <span class="filter-badge time">
                {monthNames[selectedMonth.month - 1]} {selectedMonth.year}
              </span>
            {:else if selectedYear}
              <span class="filter-badge time">{selectedYear}</span>
            {/if}
            {#if selectedAuthor}
              <span class="filter-badge author">{selectedAuthor.name}</span>
            {/if}
            {#if selectedYear || selectedMonth || selectedAuthor}
              <button onclick={resetFilter} class="reset-btn">Reset</button>
            {:else}
              <span class="all-time-label">All Time</span>
            {/if}
          </div>
          <span class="quote-total">{displayedQuotes.length} quotes</span>
        </div>

        {#if loadingData}
          <div class="loading-inline">Loading...</div>
        {:else}
          <div class="quotes-scroll">
            {#each displayedQuotes as quote, i}
              <div class="quote-row">
                <div class="quote-rank">
                  {#if i < 3 && !selectedYear}
                    <span class="rank-medal rank-{i + 1}">{i + 1}</span>
                  {:else}
                    <span class="rank-num">{i + 1}</span>
                  {/if}
                </div>

                <span class="quote-score" style="color: {heatColor(quote.spiciness)}">{quote.spiciness}</span>

                <div class="quote-content">
                  <p class="quote-text">"{quote.quote_text.length > 250 ? quote.quote_text.slice(0, 250) + '...' : quote.quote_text}"</p>
                  <div class="quote-meta">
                    <span class="quote-author">{quote.author_name}</span>
                    <span class="meta-dot"></span>
                    <span>{quote.post_year}</span>
                    <span class="meta-dot"></span>
                    <span class="quote-post-title">{quote.post_title}</span>
                  </div>
                </div>

                <a
                  href={getPermalink(quote)}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="quote-link"
                  title="View on {quote.author_name}'s Spicy Takes"
                >
                  <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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

  <footer class="page-footer">
    <p>
      Powered by <a href="https://duckdb.org/docs/api/wasm/overview" target="_blank" rel="noopener noreferrer">DuckDB-WASM</a>
    </p>
  </footer>
</div>

<style>
  /* ── Page shell ────────────────────────────────── */
  .analytics-page {
    min-height: 100vh;
    background: linear-gradient(180deg, #fafaf9 0%, #fff 40%);
  }

  /* ── Header ────────────────────────────────────── */
  .page-header {
    padding: 2rem 1.5rem 1.5rem;
    border-bottom: 1px solid #e7e5e4;
    text-align: center;
  }

  .header-inner {
    max-width: 64rem;
    margin: 0 auto;
  }

  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.78rem;
    font-weight: 500;
    color: #78716c;
    text-decoration: none;
    margin-bottom: 0.75rem;
    transition: color 0.12s;
  }
  .back-link:hover {
    color: #dc2626;
  }

  .page-title {
    font-family: var(--font-family-serif);
    font-size: 1.75rem;
    font-weight: 700;
    color: #1c1917;
    margin-bottom: 0.25rem;
  }

  .page-subtitle {
    font-size: 0.82rem;
    color: #78716c;
  }

  /* ── Loading / Error ───────────────────────────── */
  .loading-state {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8rem 0;
    font-size: 0.85rem;
    color: #78716c;
  }

  .error-state {
    max-width: 32rem;
    margin: 0 auto;
    padding: 4rem 1.5rem;
    text-align: center;
    font-size: 0.85rem;
    color: #dc2626;
    font-weight: 500;
  }

  .loading-inline {
    padding: 2rem;
    text-align: center;
    font-size: 0.82rem;
    color: #78716c;
  }

  /* ── Main ──────────────────────────────────────── */
  .page-main {
    max-width: 64rem;
    margin: 0 auto;
    padding: 1.5rem 1.5rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }

  /* ── Panels (shared) ───────────────────────────── */
  .chart-panel,
  .leaderboard-panel,
  .quotes-panel {
    background: #fff;
    border: 1px solid #e7e5e4;
    border-radius: 0.6rem;
    overflow: hidden;
    min-width: 0;
  }

  .panel-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 1rem;
    border-bottom: 1px solid #f5f5f4;
  }

  .panel-title-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .panel-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: #1c1917;
  }

  .panel-hint {
    font-size: 0.65rem;
    color: #a8a29e;
  }

  /* ── Top row grid ──────────────────────────────── */
  .top-row {
    display: grid;
    grid-template-columns: 3fr 1fr;
    gap: 1rem;
  }

  /* ── Chart ─────────────────────────────────────── */
  .chart-container {
    width: 100%;
    padding: 0 0.5rem;
    overflow-x: auto;
  }
  .chart-container :global(.vega-embed) {
    width: 100% !important;
  }

  .chart-hint {
    font-size: 0.65rem;
    color: #a8a29e;
    padding: 0.35rem 1rem 0.75rem;
  }

  .mode-toggle {
    display: flex;
    border: 1px solid #e7e5e4;
    border-radius: 0.35rem;
    overflow: hidden;
  }

  .mode-btn {
    padding: 0.25rem 0.6rem;
    font-size: 0.7rem;
    font-weight: 600;
    color: #78716c;
    background: none;
    border: none;
    cursor: pointer;
    transition: background 0.12s, color 0.12s;
  }
  .mode-btn:hover {
    background: #f5f5f4;
  }
  .mode-btn.active {
    background: #1c1917;
    color: #fff;
  }

  /* ── Filter badges ─────────────────────────────── */
  .filter-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    font-size: 0.68rem;
    font-weight: 600;
    padding: 0.15rem 0.5rem;
    border-radius: 0.25rem;
  }
  .filter-badge.time {
    background: rgba(220, 38, 38, 0.06);
    color: #dc2626;
  }
  .filter-badge.author {
    background: rgba(234, 88, 12, 0.06);
    color: #ea580c;
  }

  .badge-dismiss {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 0.72rem;
    color: inherit;
    opacity: 0.6;
    padding: 0;
    line-height: 1;
  }
  .badge-dismiss:hover {
    opacity: 1;
  }

  .reset-btn {
    font-size: 0.72rem;
    font-weight: 500;
    color: #78716c;
    background: none;
    border: none;
    cursor: pointer;
    text-decoration: underline;
    text-underline-offset: 2px;
    transition: color 0.12s;
  }
  .reset-btn:hover {
    color: #dc2626;
  }

  .all-time-label {
    font-size: 0.72rem;
    color: #a8a29e;
  }

  .year-indicator {
    font-size: 0.68rem;
    font-weight: 600;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  /* ── Leaderboard ───────────────────────────────── */
  .leaderboard-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
  }
  .leaderboard-header .panel-title-row {
    width: 100%;
    justify-content: space-between;
  }

  .leaderboard-scroll {
    max-height: 16rem;
    overflow-y: auto;
  }

  .leaderboard-table {
    width: 100%;
    font-size: 0.78rem;
    border-collapse: collapse;
  }

  .leaderboard-table thead {
    position: sticky;
    top: 0;
    background: #fafaf9;
    z-index: 1;
  }

  .leaderboard-table th {
    font-size: 0.6rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #a8a29e;
    padding: 0.4rem 0.5rem;
    text-align: left;
    border-bottom: 1px solid #f5f5f4;
  }

  .col-rank { width: 2rem; text-align: center; }
  .col-avg { text-align: right; }
  .col-count { text-align: right; }

  .leaderboard-table th.col-avg,
  .leaderboard-table th.col-count {
    text-align: right;
  }

  .author-row {
    cursor: pointer;
    transition: background 0.1s;
  }
  .author-row:hover {
    background: #fafaf9;
  }
  .author-row.selected {
    background: rgba(220, 38, 38, 0.04);
  }

  .author-row td {
    padding: 0.35rem 0.5rem;
    border-bottom: 1px solid #f5f5f4;
  }

  .rank-medal {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 1.25rem;
    height: 1.25rem;
    font-size: 0.6rem;
    font-weight: 800;
    color: #fff;
    border-radius: 50%;
  }
  .rank-medal.rank-1 { background: #ca8a04; }
  .rank-medal.rank-2 { background: #9ca3af; }
  .rank-medal.rank-3 { background: #b45309; }

  .rank-num {
    font-size: 0.68rem;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  .author-name {
    font-weight: 600;
    color: #1c1917;
    transition: color 0.12s;
  }
  .author-row:hover .author-name {
    color: #dc2626;
  }
  .author-row.selected .author-name {
    color: #dc2626;
  }

  .avg-score {
    font-weight: 800;
    font-variant-numeric: tabular-nums;
  }

  .author-row td.col-count {
    font-size: 0.68rem;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
  }

  /* ── Quotes panel ──────────────────────────────── */
  .quotes-header {
    gap: 0.75rem;
  }

  .quote-total {
    font-size: 0.68rem;
    color: #a8a29e;
    font-variant-numeric: tabular-nums;
    flex-shrink: 0;
  }

  .quotes-scroll {
    max-height: 37.5rem;
    overflow-y: auto;
  }

  .quote-row {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    padding: 0.6rem 1rem;
    border-bottom: 1px solid #f5f5f4;
    transition: background 0.1s;
  }
  .quote-row:hover {
    background: #fafaf9;
  }

  .quote-rank {
    width: 1.5rem;
    flex-shrink: 0;
    text-align: center;
    padding-top: 0.1rem;
  }

  .quote-score {
    font-size: 0.82rem;
    font-weight: 800;
    flex-shrink: 0;
    font-variant-numeric: tabular-nums;
    padding-top: 0.1rem;
  }

  .quote-content {
    flex: 1;
    min-width: 0;
  }

  .quote-text {
    font-family: var(--font-family-serif);
    font-size: 1rem;
    line-height: 1.55;
    color: #1c1917;
  }

  .quote-meta {
    display: flex;
    align-items: center;
    gap: 0.35rem;
    flex-wrap: wrap;
    margin-top: 0.25rem;
    font-size: 0.68rem;
    color: #a8a29e;
  }

  .quote-author {
    font-weight: 600;
    color: #57534e;
  }

  .meta-dot {
    width: 2.5px;
    height: 2.5px;
    border-radius: 50%;
    background: #d6d3d1;
    flex-shrink: 0;
  }

  .quote-post-title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width: 12rem;
  }

  .quote-link {
    flex-shrink: 0;
    padding: 0.35rem;
    color: #a8a29e;
    border-radius: 0.25rem;
    transition: color 0.12s, background 0.12s;
  }
  .quote-link:hover {
    color: #dc2626;
    background: rgba(220, 38, 38, 0.06);
  }

  /* ── Footer ────────────────────────────────────── */
  .page-footer {
    border-top: 1px solid #e7e5e4;
    padding: 1.25rem;
    text-align: center;
    font-size: 0.72rem;
    color: #a8a29e;
  }
  .page-footer a {
    color: #dc2626;
    text-decoration: none;
    transition: color 0.12s;
  }
  .page-footer a:hover {
    color: #b91c1c;
  }

  /* ── Responsive ────────────────────────────────── */
  @media (max-width: 768px) {
    .top-row {
      grid-template-columns: 1fr;
    }
    .page-title {
      font-size: 1.35rem;
    }
    .page-main {
      padding: 1rem;
    }
    .quote-post-title {
      max-width: 8rem;
    }
  }
</style>
