/**
 * DuckDB-WASM service for client-side analytics queries
 */

import * as duckdb from '@duckdb/duckdb-wasm';
import { browser } from '$app/environment';
import { base } from '$app/paths';

let db: duckdb.AsyncDuckDB | null = null;
let conn: duckdb.AsyncDuckDBConnection | null = null;
let initPromise: Promise<duckdb.AsyncDuckDBConnection> | null = null;

/**
 * Initialize DuckDB-WASM and load the analytics parquet file
 */
export async function initDuckDB(): Promise<duckdb.AsyncDuckDBConnection> {
  if (!browser) {
    throw new Error('DuckDB-WASM can only be used in the browser');
  }

  // Return existing connection if available
  if (conn) return conn;

  // Return pending initialization if in progress
  if (initPromise) return initPromise;

  initPromise = (async () => {
    // Select bundles based on browser capabilities
    const JSDELIVR_BUNDLES = duckdb.getJsDelivrBundles();

    // Select a bundle based on browser capabilities
    const bundle = await duckdb.selectBundle(JSDELIVR_BUNDLES);

    const worker_url = URL.createObjectURL(
      new Blob([`importScripts("${bundle.mainWorker!}");`], { type: 'text/javascript' })
    );

    // Instantiate the async worker
    const worker = new Worker(worker_url);
    const logger = new duckdb.ConsoleLogger();
    db = new duckdb.AsyncDuckDB(logger, worker);
    await db.instantiate(bundle.mainModule, bundle.pthreadWorker);
    URL.revokeObjectURL(worker_url);

    // Connect
    conn = await db.connect();

    // Fetch the parquet file and register it
    const parquetUrl = `${base}/data/analytics_quotes.parquet`;
    const response = await fetch(parquetUrl);
    if (!response.ok) {
      throw new Error(`Failed to fetch parquet file: ${response.statusText}`);
    }
    const parquetBuffer = await response.arrayBuffer();

    // Register the file with DuckDB
    await db.registerFileBuffer('analytics.parquet', new Uint8Array(parquetBuffer));

    // Load the parquet file into a table
    await conn.query(`
      CREATE TABLE quotes AS
      SELECT * FROM read_parquet('analytics.parquet')
    `);

    return conn;
  })();

  return initPromise;
}

/**
 * Convert BigInt values to numbers recursively
 */
function convertBigInts(obj: any): any {
  if (obj === null || obj === undefined) return obj;
  if (typeof obj === 'bigint') return Number(obj);
  if (Array.isArray(obj)) return obj.map(convertBigInts);
  if (typeof obj === 'object') {
    const result: Record<string, any> = {};
    for (const key in obj) {
      result[key] = convertBigInts(obj[key]);
    }
    return result;
  }
  return obj;
}

/**
 * Execute a query and return results as an array of objects
 */
export async function query<T = Record<string, unknown>>(sql: string): Promise<T[]> {
  const connection = await initDuckDB();
  const result = await connection.query(sql);
  return result.toArray().map((row: any) => convertBigInts(row.toJSON())) as T[];
}

/**
 * Get yearly spiciness statistics
 */
export async function getYearlyStats(): Promise<{
  year: number;
  avg_spiciness: number;
  std_spiciness: number;
  quote_count: number;
  max_spiciness: number;
}[]> {
  return query(`
    SELECT
      post_year as year,
      ROUND(AVG(spiciness), 2) as avg_spiciness,
      ROUND(STDDEV(spiciness), 2) as std_spiciness,
      COUNT(*) as quote_count,
      MAX(spiciness) as max_spiciness
    FROM quotes
    WHERE post_year IS NOT NULL
    GROUP BY post_year
    ORDER BY post_year
  `);
}

/**
 * Get monthly spiciness statistics
 */
export async function getMonthlyStats(): Promise<{
  year: number;
  month: number;
  avg_spiciness: number;
  quote_count: number;
}[]> {
  return query(`
    SELECT
      post_year as year,
      post_month as month,
      ROUND(AVG(spiciness), 2) as avg_spiciness,
      COUNT(*) as quote_count
    FROM quotes
    WHERE post_year IS NOT NULL AND post_month IS NOT NULL
    GROUP BY post_year, post_month
    ORDER BY post_year, post_month
  `);
}

/**
 * Get top spicy quotes overall or for a specific year
 */
export async function getTopQuotes(limit = 25, year?: number): Promise<{
  quote_text: string;
  spiciness: number;
  author_name: string;
  author_id: string;
  post_title: string;
  post_url: string;
  post_filename: string;
  post_year: number;
  themes: string[];
}[]> {
  const yearFilter = year ? `AND post_year = ${year}` : '';
  return query(`
    SELECT
      quote_text,
      spiciness,
      author_name,
      author_id,
      post_title,
      post_url,
      post_filename,
      post_year,
      themes
    FROM quotes
    WHERE spiciness IS NOT NULL ${yearFilter}
    ORDER BY spiciness DESC, quote_length DESC
    LIMIT ${limit}
  `);
}

/**
 * Get author leaderboard
 */
export async function getAuthorStats(year?: number): Promise<{
  author_id: string;
  author_name: string;
  quote_count: number;
  avg_spiciness: number;
  max_spiciness: number;
  perfect_10s: number;
}[]> {
  const yearFilter = year ? `WHERE post_year = ${year}` : '';
  return query(`
    SELECT
      author_id,
      author_name,
      COUNT(*) as quote_count,
      ROUND(AVG(spiciness), 2) as avg_spiciness,
      MAX(spiciness) as max_spiciness,
      COUNT(*) FILTER (WHERE spiciness = 10) as perfect_10s
    FROM quotes
    ${yearFilter}
    GROUP BY author_id, author_name
    ORDER BY avg_spiciness DESC
  `);
}

/**
 * Get quotes with optional filters
 */
export async function getFilteredQuotes(options: {
  authorId?: string;
  year?: number;
  limit?: number;
}): Promise<{
  quote_text: string;
  spiciness: number;
  author_name: string;
  author_id: string;
  post_title: string;
  post_url: string;
  post_filename: string;
  post_year: number;
  post_month: number;
  themes: string[];
}[]> {
  const { authorId, year, limit = 100 } = options;
  const conditions: string[] = ['spiciness IS NOT NULL'];

  if (authorId) {
    conditions.push(`author_id = '${authorId}'`);
  }
  if (year) {
    conditions.push(`post_year = ${year}`);
  }

  const whereClause = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';

  return query(`
    SELECT
      quote_text,
      spiciness,
      author_name,
      author_id,
      post_title,
      post_url,
      post_filename,
      post_year,
      post_month,
      themes
    FROM quotes
    ${whereClause}
    ORDER BY spiciness DESC, post_year DESC
    LIMIT ${limit}
  `);
}

/**
 * Get quotes for a specific year
 */
export async function getQuotesForYear(year: number, limit = 50): Promise<{
  quote_text: string;
  spiciness: number;
  author_name: string;
  author_id: string;
  post_title: string;
  post_url: string;
  post_filename: string;
  post_year: number;
  post_month: number;
  themes: string[];
}[]> {
  return query(`
    SELECT
      quote_text,
      spiciness,
      author_name,
      author_id,
      post_title,
      post_url,
      post_filename,
      post_year,
      post_month,
      themes
    FROM quotes
    WHERE post_year = ${year}
    ORDER BY spiciness DESC, post_month
    LIMIT ${limit}
  `);
}

/**
 * Get overall stats
 */
export async function getOverallStats(): Promise<{
  total_quotes: number;
  total_authors: number;
  avg_spiciness: number;
  min_year: number;
  max_year: number;
  perfect_10s: number;
}> {
  const result = await query<{
    total_quotes: number;
    total_authors: number;
    avg_spiciness: number;
    min_year: number;
    max_year: number;
    perfect_10s: number;
  }>(`
    SELECT
      COUNT(*) as total_quotes,
      COUNT(DISTINCT author_id) as total_authors,
      ROUND(AVG(spiciness), 2) as avg_spiciness,
      MIN(post_year) as min_year,
      MAX(post_year) as max_year,
      COUNT(*) FILTER (WHERE spiciness = 10) as perfect_10s
    FROM quotes
    WHERE post_year IS NOT NULL
  `);
  return result[0];
}
