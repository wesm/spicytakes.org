<script lang="ts">
  import { landing } from '$lib/config';

  // Pepper emoji for brand
  const pepper = '🌶️';
</script>

<div class="min-h-screen bg-gradient-to-b from-stone-50 to-white">
  <!-- Hero Section -->
  <header class="pt-16 pb-12 px-6 text-center">
    <h1 class="text-5xl md:text-6xl font-bold text-stone-900 mb-4">
      <span class="text-red-500">{pepper}</span> {landing.title}
    </h1>
    <p class="text-xl md:text-2xl text-stone-600 max-w-2xl mx-auto">
      {landing.tagline}
    </p>
    <p class="mt-4 text-stone-500 max-w-xl mx-auto">
      {landing.description}
    </p>
  </header>

  <!-- Blog Cards Grid -->
  <section class="max-w-5xl mx-auto px-6 pb-20">
    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      {#each landing.blogs as blog}
        <a
          href="https://{blog.subdomain}"
          class="group block bg-white rounded-2xl shadow-sm border border-stone-200 overflow-hidden hover:shadow-lg hover:border-stone-300 transition-all duration-200"
        >
          <!-- Photo -->
          <div class="aspect-[3/2] bg-stone-100 relative overflow-hidden">
            <img
              src={blog.photo}
              alt={blog.name}
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
              onerror={(e) => { (e.currentTarget as HTMLImageElement).style.display = 'none'; }}
            />
            <!-- Fallback gradient if no photo -->
            <div class="absolute inset-0 bg-gradient-to-br from-red-400 to-orange-500 opacity-0 group-hover:opacity-10 transition-opacity"></div>
          </div>

          <!-- Content -->
          <div class="p-5">
            <h2 class="text-xl font-bold text-stone-900 group-hover:text-red-600 transition-colors">
              {blog.name}
            </h2>
            <p class="text-xs text-stone-500 mt-1 font-medium">
              {blog.tagline}
            </p>
            <p class="text-stone-600 mt-2 text-sm leading-relaxed">
              {blog.description}
            </p>

            <!-- Stats -->
            <div class="mt-3 pt-3 border-t border-stone-100 flex items-center gap-4 text-sm text-stone-500">
              <span class="flex items-center gap-1">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                {blog.stats.posts} posts
              </span>
              {#if blog.stats.quotes > 0}
                <span class="flex items-center gap-1">
                  <span class="text-red-500">{pepper}</span>
                  {blog.stats.quotes} quotes
                </span>
              {/if}
            </div>

            <!-- Visit link -->
            <div class="mt-3 text-red-500 font-medium text-sm group-hover:text-red-600 flex items-center gap-1">
              Explore archive
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </div>
          </div>
        </a>
      {/each}
    </div>
  </section>

  <!-- How it works -->
  <section class="bg-stone-100 py-16 px-6">
    <div class="max-w-4xl mx-auto text-center">
      <h2 class="text-2xl font-bold text-stone-900 mb-8">How it works</h2>
      <div class="grid md:grid-cols-3 gap-8 text-left">
        <div>
          <div class="text-3xl mb-3">📥</div>
          <h3 class="font-semibold text-stone-900 mb-2">Archive</h3>
          <p class="text-stone-600 text-sm">Every post scraped and stored as searchable markdown with metadata.</p>
        </div>
        <div>
          <div class="text-3xl mb-3">🤖</div>
          <h3 class="font-semibold text-stone-900 mb-2">Analyze</h3>
          <p class="text-stone-600 text-sm">LLMs extract summaries, key insights, and memorable "money quotes."</p>
        </div>
        <div>
          <div class="text-3xl mb-3">🌶️</div>
          <h3 class="font-semibold text-stone-900 mb-2">Rate</h3>
          <p class="text-stone-600 text-sm">Each quote gets a spiciness score from 1-10 based on how provocative it is.</p>
        </div>
      </div>
    </div>
  </section>
</div>
