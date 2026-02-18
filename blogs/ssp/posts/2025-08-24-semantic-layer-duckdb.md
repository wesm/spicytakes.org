---
title: "Why Semantic Layers Matter—and How to Build One with DuckDB"
date: 2025-08-24
url: https://www.ssp.sh/blog/semantic-layer-duckdb/
slug: semantic-layer-duckdb
word_count: 4573
---

![Why Semantic Layers Matter—and How to Build One with DuckDB](https://www.ssp.sh/blog/semantic-layer-duckdb/featured-image.png)

Contents
ð¶
Featured on Hacker News.
[Read the comments](https://news.ycombinator.com/item?id=44953575)
This article was written as part of
[my services](https://www.ssp.sh/services)

Many ask themselves, “Why would I use a semantic layer? What is it anyway?” In this hands-on guide, we’ll build the simplest possible semantic layer using just a YAML file and a Python script—not as the goal itself, but as a way to understand the value of semantic layers. We’ll then query 20 million NYC taxi records with consistent business metrics executed using DuckDB and Ibis. By the end, you’ll know exactly when a semantic layer solves real problems and when it’s overkill.


It’s a topic that I’m passionate about as I’ve been using semantic layers within a Business Intelligence (BI) tool for over twenty years, and only recently have we gotten full-blown semantic layers that can sit outside of a BI tool, combining the advantages of a logical layer with sharing them across your web apps, notebooks, and BI tools. With a semantic layer, your revenue KPI or other complex company measures are defined once in a single source of truth—no need to re-implement them over and over again.


We’ll have a look at the simplest possible semantic layer, which uses a simple YAML file (for the semantics) and a Python script for executing it with Ibis and DuckDB. We’ll do a quick recap of the semantic layer before diving into a practical code example.

Find the Code on GitHub

For all the examples shown in this article, find the code on the GitHub repository [semantic-layer-duckdb](https://github.com/sspaeti/semantic-layer-duckdb).


## When You Don’t Need a Semantic Layer


Let’s start by exploring when you don’t need a semantic layer and when it’s the wrong choice. The simplest and most straightforward reasons are:

- You’re just getting started with analytics and only have one consumer, meaning you only have one way of showcasing analytics data, for example, a BI tool, notebooks, or a web app, but not multiple ways of presenting data. This means you don’t apply calculated logic in different places.
- You don’t have extensive business logic that you query ad hoc; you have simple counts, SUMs, or averages.
- You preprocess all your metrics as SQL transformations into physical tables, meaning your downstream analytics tools get all metrics preprocessed and aggregated, and filtering is fast enough.


## Why Use a Semantic Layer?


So when do we actually need one, and what is it? There’s a lot of information out there, including from myself about the [history and rise [2022]](https://www.ssp.sh/blog/rise-of-semantic-layer-metrics/), comparing it to an [MVC-like approach](https://cube.dev/blog/exploring-the-semantic-layer-through-the-lens-of-mvc), or explaining its [capabilities](https://cube.dev/blog/universal-semantic-layer-capabilities-integrations-and-enterprise-benefits). That’s why in this article I focus on the *why* and showcase how to use it in a practical example in the next chapter.


To better understand the reasons for using a semantic layer—without needing to read the full article above—let’s start with a helpful definition from [Julian Hyde](https://communityovercode.org/wp-content/uploads/2023/10/mon_dataeng_building-a-semantic-metrics-layer-using-calcite-julian-hyde.pdf?ref=ssp.sh):


> A semantic layer, also known as a metrics layer, lies between business users and the database, and lets those users compose queries in the concepts that they understand. It also governs access to the data, manages data transformations, and can tune the database by defining materializations.
> Like many new ideas, the semantic layer is a distillation and evolution of many old ideas, such as query languages, multidimensional OLAP, and query federation.


The main reasons for using a semantic layer may be one or more of the following needs:

1. **Unified place** to define ad hoc queries once, version-controlled and collaboratively, with the possibility of pulling them into different BI tools, web apps, notebooks, or AI/MCP integration. Avoid **duplication** of metrics in every tool, making **maintainability** and data governance much easier; resulting in a **consistent business layer** with encapsulated business logic.


***Example***: Most organizations quickly run multiple BI tools simultaneously with additional Excel or Google Sheets. Instead of maintaining separate calculated fields and business logic in each tool in a proprietary format, semantic layers provide one definition that works across all platforms.

1. **Caching** is needed for ad hoc queries that are based on various source databases. Defining the metrics that enable pre-calculations for sub-second query responses can benefit any downstream analytics tools compared to implementing custom database connections and different databases. Eliminating potential **data movement costs** by querying data where it lives, using dialect-optimized SQL pushdown across heterogeneous sources. This reduces infrastructure overhead and cloud computing costs.


****Example***: For a non-production or high-load OLTP source, the semantic layer can directly query the various data sources (e.g., IoT data, logs, and other data) instead of moving them into a data lake or data warehouse, and through the cache of the semantic layer, it’s fast enough without data movement.

1. Unified **access-level security** through **various APIs** (REST, GraphQL, SQL, ODBC/JDBC, MDX/Excel) as well. Unified Analytics API enables self-serve BI by allowing users to connect Excel to a cleaned, fast, and unified API.


***Example***: Centralized row-level and column-level security that works consistently across all downstream analytics tools, rather than trying to manage access controls separately in each BI tool or analytics tool that has access to the data. Users can connect directly with Excel and have the correct permissions and calculated business metrics out of the box.

1. **Dynamic query rewriting** automatically translates simple, business-friendly queries into complex, optimized SQL across multiple databases. This enables users to write intuitive queries using business concepts (like “average_order_value”) without needing to know the underlying data model complexity, table relationships, or database-specific syntax. The semantic layer **abstracts** complex analytics, such as ratios at different grains, time ranges (YoY, trailing periods), and custom calendars, into simple semantic queries.


***Example***: Complex analytics simplified by handling sophisticated calculations that are painful in raw SQL: ratios at different grains (like per-member-per-month in insurance), time intelligence (year-over-date, trailing 12 months, period-over-period), and custom calendar logic. These become simple semantic queries rather than complex subqueries with distinct counts.

1. Context for LLMs to improve accuracy and natural language querying can be significantly enhanced with a semantic layer, which provides business context and prevents AI from hallucinating frequently, as most of the business logic is configured and defined in a semantic layer, sometimes even data models, to help LLMs further understand the business.


***Example***: Internal Large Language Models (LLMs) or Retrieval-Augmented Generation (RAG) systems need business context to understand the business. A semantic layer’s connection of dimensions and facts, along with metric definitions, can help the model understand and suggest better SQL queries or responses through natural language.


---


More broadly, semantic layers bridge the gap between business needs and data source integration in a very organized and governed way. They are best optimized for larger enterprises with numerous scattered KPIs that can afford to add another layer to their data stack. However, the example below uses the simplest and smallest semantic layer, even with little data.

If you want to know more

Brian Bickell gave a great talk at the Practical Data Community about semantic layers and the problem they solve. I highly recommend checking that out too at [Semantic Layer Deep Dive](https://youtu.be/kcctcQhlxOw?si=hdRHLFlWY11bYNgl&t=1119). If you’re already on the Practical Data show from Joe Reis, also check out Hamilton Ulmer’s presentation about [Instant SQL with DuckDB/MotherDuck](https://www.youtube.com/watch?v=EOpkSsSDv40&t=2457s), not entirely about semantic layers, but related to the history of SQL and CTEs and how instant SQL can help.


### Datasets vs. Aggregations


An important distinction is whether we need **persistent** datasets or we want **ad hoc** queries. These are typically very different. Ad hoc queries must be flexible and change granularity based on added dimensions. This means someone running a query might switch from a daily view to a weekly or monthly one, add a region, and then decide to roll it up to a country level; all of this can happen in a couple of seconds. Therefore, there is no time to refresh or process the data.


Calculated measures need to be added on the fly, without requiring an ETL job to be reprocessed. A common workaround is to create multiple persistent physical datasets with dbt, each containing the same data but with varying granularity, allowing for the display of different charts in the BI tool with different focuses. A semantic layer, or ad hoc queries, does that on the fly.


We can differentiate and say:

- dataset â  aggregations
- table columns â  metrics
- physical table â  logical definition


If you find yourself needing the concepts on the right side, that’s when you need a semantic layer—whether built into a BI tool or implemented separately for the reasons mentioned above.


## How a Semantic Layer Works: A Practical Example


Now let’s see this in action by analyzing the most pragmatic semantic layer there is. The simplest semantic layer I found is by Julien Hurault, who recently announced the release of the [Boring Semantic Layer (BSL)](https://github.com/boringdata/boring-semantic-layer) project. We use DuckDB as the query engine and Python with [Ibis](https://github.com/ibis-project/ibis) for the execution layer.

What this Semantic Layer does not have

This is a relatively simple semantic layer. More advanced ones include additional features such as multiple robust APIs (REST, GraphQL, SQL, ODBC, Excel), advanced security controls, and a powerful caching layer.


This example focuses on the [Logical Data Model](https://en.wikipedia.org/wiki/Logical_schema), where we can define our business requirements within YAML, an abstraction above our physical layer. Although this is quite close to the physical layer, this is where more advanced semantic layer tools (Cube, dbt SL, GoodData, AtScale) give you more advantages in an enterprise setting.


We’re going to build something like what’s illustrated below—where we have YAML definitions as our metrics, such as calculated measures and dimensions, and Ibis for the query translation to run [any execution engine](https://github.com/ibis-project/ibis#how-it-works); here we use DuckDB.


![/blog/semantic-layer-duckdb/sl-duckdb-bsl-architecture.png](https://www.ssp.sh/blog/semantic-layer-duckdb/sl-duckdb-bsl-architecture.png)

*Simple Architecture Overview of an Semantic Layer Implementation*

Data Catalogs

If you wonder how [DuckLake](https://ducklake.select/) or other open table format catalogs (Iceberg, Unity, Polaris) fit into the picture, they would be connected to the metrics definition. Hence, the catalog has the complete list of available data assets. You can view open data catalogs as a lookup service for the datasets in your data lake. If you use a semantic layer as we implement here, you won’t need an additional catalog because all your metrics and dimensions are defined within the semantic layer itself.


### Getting Started


Let’s create a virtual environment where we install our dependencies and install the semantic layer:



| `1
2
` | `git clone git@github.com:sspaeti/semantic-layer-duckdb.git
uv sync #installs dependencies
` |



That will not only install the semantic layer, but also Ibis and other requirements.


Now we are ready to define our metrics. To simplify this example and focus on the metrics rather than the data, I utilized the [NYC Taxi Dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), which we all know and are familiar with. They have a lookup table for pickups and lots of data we can use, and it is available via HTTPS.

You can use MotherDuck Shared datasets

If you want to use MotherDuck’s shared datasets, please check out [Example Datasets](https://motherduck.com/docs/getting-started/sample-data-queries/datasets/), for example the [NYC 311 Service Requests Data](https://motherduck.com/docs/getting-started/sample-data-queries/nyc-311-data/) is uploaded, as well as [Foursquare](https://motherduck.com/docs/getting-started/sample-data-queries/foursquare/) and other helpful ones. You can query this data instantly by running duckdb and connecting to MotherDuck as showcased below:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
` | `â¯ duckdb
D ATTACH 'md:'; #needs `motherduck_token` or authentication will be prompted
D select count(*) from sample_data.nyc.taxi;
ââââââââââââââââââ
â  count_star()  â
â     int64      â
ââââââââââââââââââ¤
â    3252717     â
â (3.25 million) â
ââââââââââââââââââ
` |



As we know now, semantic layers are suitable for defining metrics in a central and configurable way, so we use YAML for this. YAML has minimal overhead and is easy to read, which is why most semantic layers use it. Alternatively, SQL would be a better choice, but it lacks essential features like variables and tends to become overly nested and challenging to maintain. YAML, combined with occasional SQL injection, proves to be the most effective solution.


First, let’s check out what data we are working with—we can quickly count and describe the tables:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
` | `D select count(*) FROM read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2025-06.parquet");
âââââââââââââââââââ
â  count_star()   â
â      int64      â
âââââââââââââââââââ¤
â    19868009     â
â (19.87 million) â
âââââââââââââââââââ
D DESCRIBE FROM read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2025-06.parquet");
ââââââââââââââââââââââââ¬ââââââââââââââ¬ââââââââââ¬ââââââââââ¬ââââââââââ¬ââââââââââ
â     column_name      â column_type â  null   â   key   â default â  extra  â
â       varchar        â   varchar   â varchar â varchar â varchar â varchar â
ââââââââââââââââââââââââ¼ââââââââââââââ¼ââââââââââ¼ââââââââââ¼ââââââââââ¼ââââââââââ¤
â hvfhs_license_num    â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â dispatching_base_num â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â originating_base_num â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â request_datetime     â TIMESTAMP   â YES     â NULL    â NULL    â NULL    â
â on_scene_datetime    â TIMESTAMP   â YES     â NULL    â NULL    â NULL    â
â pickup_datetime      â TIMESTAMP   â YES     â NULL    â NULL    â NULL    â
â dropoff_datetime     â TIMESTAMP   â YES     â NULL    â NULL    â NULL    â
â PULocationID         â INTEGER     â YES     â NULL    â NULL    â NULL    â
â DOLocationID         â INTEGER     â YES     â NULL    â NULL    â NULL    â
â trip_miles           â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â trip_time            â BIGINT      â YES     â NULL    â NULL    â NULL    â
â base_passenger_fare  â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â tolls                â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â bcf                  â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â sales_tax            â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â congestion_surcharge â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â airport_fee          â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â tips                 â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â driver_pay           â DOUBLE      â YES     â NULL    â NULL    â NULL    â
â shared_request_flag  â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â shared_match_flag    â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â access_a_ride_flag   â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â wav_request_flag     â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â wav_match_flag       â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â cbd_congestion_fee   â DOUBLE      â YES     â NULL    â NULL    â NULL    â
ââââââââââââââââââââââââ´ââââââââââââââ´ââââââââââ´ââââââââââ´ââââââââââ´ââââââââââ¤
â 25 rows                                                          6 columns â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
` |



As well as the CSV lookups:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
` | `D select count(*) from read_csv("https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv");
ââââââââââââââââ
â count_star() â
â    int64     â
ââââââââââââââââ¤
â     265      â
ââââââââââââââââ
D describe from read_csv("https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv");
ââââââââââââââââ¬ââââââââââââââ¬ââââââââââ¬ââââââââââ¬ââââââââââ¬ââââââââââ
â column_name  â column_type â  null   â   key   â default â  extra  â
â   varchar    â   varchar   â varchar â varchar â varchar â varchar â
ââââââââââââââââ¼ââââââââââââââ¼ââââââââââ¼ââââââââââ¼ââââââââââ¼ââââââââââ¤
â LocationID   â BIGINT      â YES     â NULL    â NULL    â NULL    â
â Borough      â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â Zone         â VARCHAR     â YES     â NULL    â NULL    â NULL    â
â service_zone â VARCHAR     â YES     â NULL    â NULL    â NULL    â
ââââââââââââââââ´ââââââââââââââ´ââââââââââ´ââââââââââ´ââââââââââ´ââââââââââ
` |



This gives us a good sense of what we are dealing with. From the [data dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_hvfhs.pdf), we understand that `PULocationID` and `DOLocationID` represent the Taxi zones to be joined with the above zone lookup by the column `LocationID`.


Usually what I do next is use the [`SUMMARIZE` command](https://duckdb.org/docs/stable/guides/meta/summarize.html), which is a DuckDB-specific query type that gives us statistics about the data such as `min`, `max`, `approx_unique`, `avg`, `std`, `q25`, `q50`, `q75`, `count`. This gives us a fast and handy overview of what we are dealing with.


#### Defining Metrics in Boring Semantic Layer


Next, we can start defining our metrics. Let’s start by setting the timestamp and its granularity (required by BSL), followed by the dimensions, which looks something like this:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
` | `fhvhv_trips:
  table: trips_tbl
  time_dimension: pickup_datetime
  smallest_time_grain: TIME_GRAIN_SECOND
  
  dimensions:
    hvfhs_license_num: _.hvfhs_license_num
    dispatching_base_num: _.dispatching_base_num
    originating_base_num: _.originating_base_num
    request_datetime: _.request_datetime
    pickup_datetime: _.pickup_datetime
    dropoff_datetime: _.dropoff_datetime
    trip_miles: _.trip_miles
    trip_time: _.trip_time
    base_passenger_fare: _.base_passenger_fare
    tolls: _.tolls
    bcf: _.bcf
    sales_tax: _.sales_tax
    congestion_surcharge: _.congestion_surcharge
    airport_fee: _.airport_fee
    tips: _.tips
    driver_pay: _.driver_pay
    shared_request_flag: _.shared_request_flag
    shared_match_flag: _.shared_match_flag
    access_a_ride_flag: _.access_a_ride_flag
    wav_request_flag: _.wav_request_flag
    wav_match_flag: _.wav_match_flag
` |



The `pickup_datetime` is the time column, with the grain set to seconds, and all other columns are treated as dimensions.


The interesting part is when we set the measures, which are the calculations, that can become very complex and potentially depend on many layers of existing measures. This is how we define our measures:



| `1
2
3
4
5
6
7
8
` | `  measures:
    trip_count: _.count()
    avg_trip_miles: _.trip_miles.mean()
    avg_trip_time: _.trip_time.mean()
    avg_base_fare: _.base_passenger_fare.mean()
    total_revenue: _.base_passenger_fare.sum()
    avg_tips: _.tips.mean()
    avg_driver_pay: _.driver_pay.mean()
` |



And some more that only aggregate flagged data, such as shared trip or wheelchair requested:



| `1
2
` | `    shared_trip_rate: (_.shared_match_flag == 'Y').mean()
    wheelchair_request_rate: (_.wav_request_flag == 'Y').mean()
` |



To create a functional dashboard and drill down into different angles, we need **dimensions** that provide more context when querying data. For example, if we want to aggregate on **borough** in New York City, this information is not in the trips data, but in our lookup table, as we saw in the above `DESCRIBE`. Let’s now join this table and use this information.


First, we define the additional dataset in the YAML as follows:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
` | `taxi_zones:
  table: taxi_zones_tbl
  primary_key: LocationID
  
  dimensions:
    location_id: _.LocationID
    borough: _.Borough
    zone: _.Zone
    service_zone: _.service_zone
    
  measures:
    zone_count: _.count()
` |



Lastly, we need to join the two datasets. This can be specified like this - added to the `fhvhv_trips` dataset:



| `1
2
3
4
5
` | `  joins:
    pickup_zone:
      model: taxi_zones
      type: one
      with: _.PULocationID
` |



### Query Data through Python/Ibis and DuckDB


Next, we need to set up our execution logic—which is Python code in this case—and use the translation layer Ibis to run DuckDB queries as our SQL engine locally.


I’ll explain the most important steps here, but I’ll skip some details—the full script you can find in [nyc_taxi.py](https://github.com/sspaeti/semantic-layer-duckdb/blob/main/nyc_taxi.py). First, we import Ibis and our `SemanticModel` class from Boring Semantic Layer and we define the datasets and execution engine via Ibis—again, here we use DuckDB and read the dataset directly from [CloudFront](https://aws.amazon.com/cloudfront/):



| `1
2
3
4
5
6
7
8
` | `import ibis
from boring_semantic_layer import SemanticModel

con = ibis.duckdb.connect(":memory:") #or use `"md:"` for MotherDuck engine
tables = {
    "taxi_zones_tbl": con.read_csv("https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"),
    "trips_tbl": con.read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2025-06.parquet"),
}
` |


Scale Up with MotherDuck

With one simple change, we can use MotherDuck as the [Ibis query engine](https://ibis-project.org/backends/duckdb#motherduck). Instead of `con = ibis.duckdb.connect(":memory:")`, we can use `con = ibis.duckdb.connect("md:")`


Now that we have read the metrics definition we created in the YAML `nyc_taxi.yml` file above and mapped it to the tables dataset, the boring semantic layer knows which dataset we have and can query it:



| `1
2
3
4
` | `models = SemanticModel.from_yaml(f"nyc_taxi.yml", tables=tables)

taxi_zones_sm = models["taxi_zones"] #dataset name from the yaml file
trips_sm = models["fhvhv_trips"] 
` |



And then we define our query as a Python expression with Ibis and BSL—here the **trip volume by pickup borough**:



| `1
2
3
4
5
6
` | `expr = trips_sm.query(
  dimensions=["pickup_zone.borough"],
  measures=["trip_count", "avg_trip_miles", "avg_base_fare"],
  order_by=[("trip_count", "desc")],
  limit=5,
)
` |



And we can execute and print it with:



| `1
` | `print(expr.execute())
` |



The result looks something like this:



| `1
2
3
4
5
6
` | `  pickup_zone_borough  trip_count  avg_trip_miles  avg_base_fare
0           Manhattan     7122571        5.296985      33.575738
1            Brooklyn     5433158        4.215820      23.280429
2              Queens     4453220        6.379047      29.778835
3               Bronx     2541614        4.400500      20.313596
4       Staten Island      316533        5.262288      22.200712
` |



So what just happened? We defined the dimension (`pickup_zone.borough`) in which we want to display the measure, configured the three measures to be shown, and specified the order and the number of rows to return with LIMIT.


The magic is that we can now change the metric in the YAML file, add a CASE WHEN statement, or fix a formatting error all without touching the query or code. Less technical people gain access through a [DSL (Domain Specific Language)](https://en.wikipedia.org/wiki/Domain-specific_language) and a separate configuration file, which we can version control, collaborate on, or even utilize LLMs to create new measures and dimensions.


Ibis gives us the flexibility to do it in a Pythonic way.


Find more examples such as the popular pickup zones, service zone analysis, revenue analysis by trip distance, and accessibility metrics in the whole script `nyc_taxi.py` and yaml in `nyc_taxi.yml`.

Limitations

I [wasn’t able](https://github.com/boringdata/boring-semantic-layer/issues/32) to join the dataset twice, once for pickup and once for drop-off locations. That’s why I only joined it once in this example.


### Materialization


If you wish to speed things up and create a **persistent cube**, the option is there with the help of [Xorq](https://github.com/xorq-labs/xorq)—example from [example_materialize.py](https://github.com/boringdata/boring-semantic-layer/blob/main/examples/example_materialize.py).



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
` | `import pandas as pd
import xorq as xo

from boring_semantic_layer import SemanticModel

df = pd.DataFrame(
    {
        "date": pd.date_range("2025-01-01", periods=5, freq="D"),
        "region": ["north", "south", "north", "east", "south"],
        "sales": [100, 200, 150, 300, 250],
    }
)

con = xo.connect()
tbl = con.create_table("sales", df)

sales_model = SemanticModel(
    table=tbl,
    dimensions={"region": lambda t: t.region, "date": lambda t: t.date},
    measures={
        "total_sales": lambda t: t.sales.sum(),
        "order_count": lambda t: t.sales.count(),
    },
    time_dimension="date",
    smallest_time_grain="TIME_GRAIN_DAY",
)

cube = sales_model.materialize(
    time_grain="TIME_GRAIN_DAY",
    cutoff="2025-01-04",
    dimensions=["region", "date"],
    storage=None,
)

print("Cube model definition:", cube.json_definition)

df_cube = cube.query(
    dimensions=["date", "region"], measures=["total_sales", "order_count"]
).execute()
` |



### More Complex Measures


This example is relatively simple, but showcases how you can use a simple semantic layer on top of your data lake with DuckDB.


If you need more advanced measures that are **dependent on each other**, you can imagine how beneficial it would be. The beauty of semantic layers lies in their ability to simply define dependencies on complex measures, eliminating the need to repeat 100 lines of SQL code in your CTE query.


Obviously, you could use dbt to manage dependencies, but you wouldn’t have the ad hoc query capability, the on-the-fly filtering, or nicely defined YAML files that represent your dynamic queries.


### Visualizing


Interestingly, the BSL also includes some visualization capabilities with a built-in wrapper around **[Vega-Lite](https://vega.github.io/vega-lite/)** (JSON-based grammar for creating interactive visualizations that provides a declarative approach to chart creation) and its Python wrapper **[Altair](https://altair-viz.github.io/)**.


Just install with `uv add 'boring-semantic-layer[visualization]' altair[all]` and you can create a simple visualization. This is a bit extended to create a nice-looking image, but you can imagine this being much shorter with only the title, for example:



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
` | `# Charting example
png_bytes = expr.chart(
  format="png",  # Add format parameter here
  spec={
	"title": {
	    "text": "NYC Taxi Trip Volume by Borough",
	    "fontSize": 16,
	    "fontWeight": "bold",
	    "anchor": "start"
	},
	"mark": {
	    "type": "bar",
	    "color": "#2E86AB",
	    "cornerRadiusEnd": 4
	},
	"encoding": {
	    "x": {
		  "field": "pickup_zone_borough",
		  "type": "nominal",
		  "sort": "-y",
		  "title": "Borough",
		  "axis": {
			"labelAngle": -45,
			"titleFontSize": 12,
			"labelFontSize": 10
		  }
	    },
	    "y": {
		  "field": "trip_count",
		  "type": "quantitative",
		  "title": "Number of Trips",
		  "axis": {
			"format": ".2s",
			"titleFontSize": 12,
			"labelFontSize": 10
		  }
	    }
	},
	"width": 500,
	"height": 350,
	"background": "#FAFAFA"
  }
)

# Save as file
with open("trip-volume-by-pickup-borough-styled.png", "wb") as f:
  f.write(png_bytes)
` |



The generated PNG looks like this:

[

](https://www.ssp.sh/blog/semantic-layer-duckdb/nyc-taxy-visualization.webp)


## What If Questions [FAQ]


This showed you how to implement a semantic layer with DuckDB and simple tools pragmatically. Moreover, I hope it has provided you with a better understanding of the semantic layer and its appropriate usage.


Before we wrap up, let’s go through the most common questions when it comes to a semantic layer.


> **But why can’t we just use a database?**


The key is the semantic logic layer, abstracting the physical world from the modeling world. This gives you better flexibility to implement what the business wants, rather than what the physical data model can do.


Try implementing a ‘revenue per customer by quarter with year-over-year comparison’ across five different BI tools using just database views—you’ll most probably end up with five different implementations that drift apart over time.


> **What if we have 100s of metrics, do we need a semantic layer?**


That’s precisely when you *need* a semantic layer most. Managing 100+ metrics across multiple tools without a single unified view becomes a governance nightmare. Each tool ends up with slightly different calculations, and nobody knows which version is the correct one. A semantic layer gives you one source of truth.


> **Isn’t a semantic layer adding too much complexity to the already complex data landscape?**


Modern data stacks usually come with a handful of tools. A semantic layer most often reduces complexity in a large organization by eliminating metric duplication across those tools.


The initial setup cost pays for itself when you’re not debugging why revenue numbers differ between Tableau and your web app.


> **What if my data changes frequently? Won’t the semantic layer become a bottleneck for updates?**


This is a strength of semantic layers. Unlike pre-computed aggregation tables that need to be reprocessed when source data changes, semantic layers generate queries on demand. Your metrics automatically reflect the latest data because they’re calculated in real-time from the source. You only need to update the YAML definitions when business logic changes, not when data refreshes.


And it can make the process more agile than maintaining dozens of dbt models for different granularities.


> **What if I want to use MCP with it?**


If you wish to add [Model Context Protocol (MCP)](https://motherduck.com/blog/faster-data-pipelines-with-mcp-duckdb-ai/) with Claude Code, for example, the boring semantic layer is built out of the box with it in combination with [xorq](https://github.com/xorq-labs/xorq). Check out a quick showcase in this [LinkedIn demo](https://www.linkedin.com/posts/sven-gonschorek-16b5b0177_i-didnt-expect-connecting-a-data-warehouse-activity-7359199238884417537-En3D) by Sven Gonschorek.


You can also check out the [repo for further information](https://github.com/boringdata/boring-semantic-layer#model-context-protocol-mcp-integration) with `uv add 'boring-semantic-layer[mcp]'`. But in this article, I focus on the semantic layer capabilities first, and the importance of using one.


> **What are other popular semantic layer tools?**


Cube, AtScale, dbt Semantic Layer, GoodData. Some of these tools are more powerful than others; not all support enhanced security, low-level security, or powerful APIs like Excel or caching. I curate a small list of these tools at [Semantic Layer Tools](https://www.ssp.sh/brain/semantic-layer#semantic-layer-tools).


> **How do I use a semantic layer with MotherDuck?**


Here are a couple of integrations that work out of the box:

- Check out the [integration](https://cube.dev/blog/introducing-duckdb-and-motherduck-integrations) with Cube on [MotherDuck Semantic Layer with Cube](https://cube.dev/integrations/motherduck-semantic-layer-with-cube). There’s also this [webinar](https://youtu.be/z_nb-31Y30I?si=oVtuLmgq4sFckXar).
- [Boost Efficiency](https://www.gooddata.com/blog/gooddata-and-motherduck-take-flight-together/) with GoodData integration


---


```
Full article published at MotherDuck.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/semantic-layer-duckdb/)
|
[Roadmap](https://www.ssp.sh/tags/roadmap/)
[Dataengineer](https://www.ssp.sh/tags/dataengineer/)
[Devops](https://www.ssp.sh/tags/devops/)
[Learning](https://www.ssp.sh/tags/learning/)
[Motherduck](https://www.ssp.sh/tags/motherduck/)
[Services](https://www.ssp.sh/tags/services/)
