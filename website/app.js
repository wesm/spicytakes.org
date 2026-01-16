// Benn Stancil - Intellectual Footprint
// Interactive website for exploring posts and quotes

const THEME_LABELS = {
    'data_infrastructure': 'Data Infrastructure',
    'analytics_practice': 'Analytics Practice',
    'ai_llms': 'AI & LLMs',
    'startups_vc': 'Startups & VC',
    'career': 'Career',
    'industry_criticism': 'Industry Criticism',
    'tools_products': 'Tools & Products'
};

const THEME_ICONS = {
    'data_infrastructure': '🏗️',
    'analytics_practice': '📊',
    'ai_llms': '🤖',
    'startups_vc': '🚀',
    'career': '💼',
    'industry_criticism': '🔍',
    'tools_products': '🛠️'
};

let allPosts = [];
let allQuotes = [];
let activeThemes = new Set();
let searchQuery = '';

// Initialize the app
async function init() {
    try {
        const response = await fetch('../data/llm_quotes.json');
        const data = await response.json();

        allPosts = data.posts.filter(p => !p.error).map(post => ({
            ...post,
            date: parseDate(post.filename),
            title: formatTitle(post.filename)
        })).sort((a, b) => b.date - a.date);

        // Build quotes array
        allPosts.forEach(post => {
            if (post.money_quotes) {
                post.money_quotes.forEach(quote => {
                    allQuotes.push({
                        quote,
                        post,
                        themes: post.themes || []
                    });
                });
            }
        });

        updateStats();
        renderThemeFilters();
        renderTimeline();
        renderQuotes();
        renderThemes();
        setupEventListeners();

    } catch (error) {
        console.error('Failed to load data:', error);
    }
}

function parseDate(filename) {
    const match = filename.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (match) {
        return new Date(match[1], match[2] - 1, match[3]);
    }
    return new Date();
}

function formatTitle(filename) {
    // Remove date prefix and convert dashes to spaces
    const titlePart = filename.replace(/^\d{4}-\d{2}-\d{2}-/, '');
    return titlePart
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function formatDate(date) {
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function updateStats() {
    const filtered = getFilteredPosts();
    const filteredQuotes = getFilteredQuotes();

    document.getElementById('post-count').textContent = filtered.length;
    document.getElementById('quote-count').textContent = filteredQuotes.length;
    document.getElementById('footer-posts').textContent = allPosts.length;

    if (filtered.length > 0) {
        const years = filtered.map(p => p.date.getFullYear());
        const minYear = Math.min(...years);
        const maxYear = Math.max(...years);
        document.getElementById('year-range').textContent =
            minYear === maxYear ? `${minYear}` : `${minYear}-${maxYear}`;
    }
}

function getFilteredPosts() {
    return allPosts.filter(post => {
        // Theme filter
        if (activeThemes.size > 0) {
            const postThemes = post.themes || [];
            if (!postThemes.some(t => activeThemes.has(t))) {
                return false;
            }
        }

        // Search filter
        if (searchQuery) {
            const query = searchQuery.toLowerCase();
            const searchFields = [
                post.title,
                post.summary,
                post.key_insight,
                ...(post.money_quotes || [])
            ].filter(Boolean).join(' ').toLowerCase();

            if (!searchFields.includes(query)) {
                return false;
            }
        }

        return true;
    });
}

function getFilteredQuotes() {
    return allQuotes.filter(item => {
        // Theme filter
        if (activeThemes.size > 0) {
            if (!item.themes.some(t => activeThemes.has(t))) {
                return false;
            }
        }

        // Search filter
        if (searchQuery) {
            const query = searchQuery.toLowerCase();
            if (!item.quote.toLowerCase().includes(query) &&
                !item.post.title.toLowerCase().includes(query)) {
                return false;
            }
        }

        return true;
    });
}

function renderThemeFilters() {
    const container = document.getElementById('theme-filters');
    const themeCounts = {};

    allPosts.forEach(post => {
        (post.themes || []).forEach(theme => {
            themeCounts[theme] = (themeCounts[theme] || 0) + 1;
        });
    });

    container.innerHTML = Object.entries(themeCounts)
        .sort((a, b) => b[1] - a[1])
        .map(([theme, count]) => `
            <button class="theme-tag" data-theme="${theme}">
                ${THEME_LABELS[theme] || theme} (${count})
            </button>
        `).join('');
}

function renderTimeline() {
    const container = document.getElementById('timeline');
    const posts = getFilteredPosts();

    if (posts.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <h3>No posts found</h3>
                <p>Try adjusting your search or filters</p>
            </div>
        `;
        return;
    }

    // Group by year
    const byYear = {};
    posts.forEach(post => {
        const year = post.date.getFullYear();
        if (!byYear[year]) byYear[year] = [];
        byYear[year].push(post);
    });

    container.innerHTML = Object.entries(byYear)
        .sort((a, b) => b[0] - a[0])
        .map(([year, yearPosts]) => `
            <div class="year-section">
                <div class="year-header">
                    <h2>${year}<span class="year-stats">${yearPosts.length} posts</span></h2>
                </div>
                <div class="posts-grid">
                    ${yearPosts.map(post => renderPostCard(post)).join('')}
                </div>
            </div>
        `).join('');
}

function renderPostCard(post) {
    const themes = (post.themes || []).map(t =>
        `<span class="card-theme">${THEME_LABELS[t] || t}</span>`
    ).join('');

    return `
        <article class="post-card" data-filename="${post.filename}">
            <div class="date">${formatDate(post.date)}</div>
            <h3>${escapeHtml(post.title)}</h3>
            <p class="summary">${escapeHtml(post.summary || '')}</p>
            ${themes ? `<div class="card-themes">${themes}</div>` : ''}
        </article>
    `;
}

function renderQuotes() {
    const container = document.getElementById('quotes-grid');
    const quotes = getFilteredQuotes();

    if (quotes.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <h3>No quotes found</h3>
                <p>Try adjusting your search or filters</p>
            </div>
        `;
        return;
    }

    // Shuffle for variety but keep it deterministic
    const shuffled = [...quotes].sort((a, b) =>
        a.quote.length - b.quote.length + (a.post.filename.localeCompare(b.post.filename))
    );

    container.innerHTML = shuffled.slice(0, 100).map(item => `
        <article class="quote-card" data-filename="${item.post.filename}">
            <blockquote>${escapeHtml(item.quote)}</blockquote>
            <div class="quote-source">
                <strong>${escapeHtml(item.post.title)}</strong><br>
                ${formatDate(item.post.date)}
            </div>
        </article>
    `).join('');
}

function renderThemes() {
    const container = document.getElementById('themes-overview');
    const themeData = {};

    allPosts.forEach(post => {
        (post.themes || []).forEach(theme => {
            if (!themeData[theme]) {
                themeData[theme] = { posts: [], quotes: [] };
            }
            themeData[theme].posts.push(post);
            (post.money_quotes || []).forEach(q => {
                themeData[theme].quotes.push({ quote: q, post });
            });
        });
    });

    container.innerHTML = Object.entries(themeData)
        .sort((a, b) => b[1].posts.length - a[1].posts.length)
        .map(([theme, data]) => {
            const sampleQuotes = data.quotes
                .sort(() => 0.5 - Math.random())
                .slice(0, 2)
                .map(q => `<p class="sample-quote">"${escapeHtml(truncate(q.quote, 150))}"</p>`)
                .join('');

            return `
                <div class="theme-card" data-theme="${theme}">
                    <h3>
                        <span class="theme-icon">${THEME_ICONS[theme] || '📝'}</span>
                        ${THEME_LABELS[theme] || theme}
                    </h3>
                    <p class="theme-count">${data.posts.length} posts, ${data.quotes.length} quotes</p>
                    <div class="theme-quotes">
                        ${sampleQuotes}
                    </div>
                </div>
            `;
        }).join('');
}

function showModal(filename) {
    const post = allPosts.find(p => p.filename === filename);
    if (!post) return;

    const modal = document.getElementById('post-modal');
    const body = document.getElementById('modal-body');

    const themes = (post.themes || []).map(t =>
        `<span class="modal-theme">${THEME_LABELS[t] || t}</span>`
    ).join('');

    const quotes = (post.money_quotes || []).map(q =>
        `<li>${escapeHtml(q)}</li>`
    ).join('');

    body.innerHTML = `
        <div class="modal-date">${formatDate(post.date)}</div>
        <h2>${escapeHtml(post.title)}</h2>
        ${themes ? `<div class="modal-themes">${themes}</div>` : ''}

        <div class="modal-section">
            <h4>Summary</h4>
            <p class="modal-summary">${escapeHtml(post.summary || 'No summary available')}</p>
        </div>

        ${post.key_insight ? `
            <div class="modal-section">
                <h4>Key Insight</h4>
                <p class="modal-insight">${escapeHtml(post.key_insight)}</p>
            </div>
        ` : ''}

        ${quotes ? `
            <div class="modal-section">
                <h4>Money Quotes</h4>
                <ul class="modal-quotes">${quotes}</ul>
            </div>
        ` : ''}

        ${post.tone ? `
            <div class="modal-section">
                <h4>Tone</h4>
                <p class="modal-tone">${escapeHtml(post.tone)}</p>
            </div>
        ` : ''}

        <a href="https://benn.substack.com/p/${post.filename.replace(/^\d{4}-\d{2}-\d{2}-/, '')}"
           target="_blank" class="modal-link">
            Read on Substack
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                <polyline points="15 3 21 3 21 9"></polyline>
                <line x1="10" y1="14" x2="21" y2="3"></line>
            </svg>
        </a>
    `;

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function hideModal() {
    const modal = document.getElementById('post-modal');
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

function setupEventListeners() {
    // Navigation
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));

            btn.classList.add('active');
            const view = btn.dataset.view;
            document.getElementById(`${view}-view`).classList.add('active');
        });
    });

    // Theme filters
    document.getElementById('theme-filters').addEventListener('click', (e) => {
        if (e.target.classList.contains('theme-tag')) {
            const theme = e.target.dataset.theme;

            if (activeThemes.has(theme)) {
                activeThemes.delete(theme);
                e.target.classList.remove('active');
            } else {
                activeThemes.add(theme);
                e.target.classList.add('active');
            }

            updateStats();
            renderTimeline();
            renderQuotes();
        }
    });

    // Theme cards click to filter
    document.getElementById('themes-overview').addEventListener('click', (e) => {
        const card = e.target.closest('.theme-card');
        if (card) {
            const theme = card.dataset.theme;
            activeThemes.clear();
            activeThemes.add(theme);

            document.querySelectorAll('.theme-tag').forEach(tag => {
                tag.classList.toggle('active', tag.dataset.theme === theme);
            });

            // Switch to timeline view
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
            document.querySelector('[data-view="timeline"]').classList.add('active');
            document.getElementById('timeline-view').classList.add('active');

            updateStats();
            renderTimeline();
            renderQuotes();
        }
    });

    // Search
    const searchInput = document.getElementById('search');
    let searchTimeout;
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            searchQuery = e.target.value.trim();
            updateStats();
            renderTimeline();
            renderQuotes();
        }, 300);
    });

    // Post/Quote cards
    document.addEventListener('click', (e) => {
        const postCard = e.target.closest('.post-card');
        const quoteCard = e.target.closest('.quote-card');

        if (postCard) {
            showModal(postCard.dataset.filename);
        } else if (quoteCard) {
            showModal(quoteCard.dataset.filename);
        }
    });

    // Modal
    document.querySelector('.modal-backdrop').addEventListener('click', hideModal);
    document.querySelector('.modal-close').addEventListener('click', hideModal);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') hideModal();
    });
}

// Utilities
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function truncate(text, length) {
    if (text.length <= length) return text;
    return text.slice(0, length).trim() + '...';
}

// Start the app
document.addEventListener('DOMContentLoaded', init);
