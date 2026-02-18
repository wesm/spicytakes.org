---
title: "What «Shifting Left» Means and Why it Matters for Data Stacks"
date: 2025-04-14
url: https://www.ssp.sh/blog/shifting-left/
slug: shifting-left
word_count: 4785
---

![What «Shifting Left» Means and Why it Matters for Data Stacks](https://www.ssp.sh/blog/shifting-left/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Shifting left is an interesting concept that’s gaining momentum in modern data engineering. SDF has been among those sharing this approach, even making “shifting left” one of their main slogans. As Elias DeFaria, SDF’s co-founder, describes it, shifting left means “improving data quality by moving closer toward the data source”.


However, the benefits extend beyond just data quality improvements. With dbt Labs’ recent acquisition of SDF, many are wondering: what does this mean for the shifting left movement, and more importantly, what exactly is shifting left in the data context?


In this article, we’ll explore the core principles behind shifting left, examine how code-first approaches have made moving logic upstream more efficient, and answer the questions: Why should data teams shift left? What elements need to be shifted? And how can your organization implement this approach to build more maintainable, efficient data systems?


## What Is “Shifting Left?”


So, what is shifting left? And where did it come from? Following the flow of data throughout a data stack, we can see how raw data is processed and served to the very right. We have validations and complex transformations on the left and business aggregations on the right. The goal of shifting left is gaining better data quality and performance by moving responsibility and metrics upstream. Illustrated in the image below.


![/blog/shifting-left/how-shift-left-improves-data-pipelines.png](https://www.ssp.sh/blog/shifting-left/how-shift-left-improves-data-pipelines.png)

*Showcasing how Shifting Left can improve data pipelines*


A formal **definition for shifting left** applied to data could be like this:


> The strategic decision to move data quality checks, business logic, transformations, and governance processes earlier in the data lifecycle—closer to the source or ingestion phase—rather than handling these concerns downstream in BI tools or at the point of consumption.
> This approach focuses on detecting and resolving data issues earlier, creating more maintainable data systems and reducing development costs through prevention rather than detection, while also enabling consistent metric definitions and improved performance across the entire data stack.


But shifting left is more than just moving components left; it’s also about *how* we do it—the way to shift left easily with a declarative data platform. We don’t need to invest massive effort in exporting large SQL or code from our BI tool, or worse, hugely generated code, and trying to convert that to our low-code ETL anymore. We can move descriptive business logic **simply from one config file to another**, more on that later.


### The Origins of Shifting Left


Before we move to what we are shifting, and its benefits, here’s a quick discovery of where the name and concept came from.


The “Shift Left” concept evolved across multiple domains over decades. It emerged in the 1990s as a response to limitations of the [Waterfall model](https://en.wikipedia.org/wiki/Waterfall_model), which positioned testing only at the end of development. Larry Smith formally [coined](https://devopedia.org/shift-left) the term “**Shift-Left Testing**” in a 2001 Dr. Dobb’s article, defining it as “a better way of integrating quality assurance and development.” The approach gained broader adoption when **security engineering** embraced it around 2016-2018, creating what we now know as DevSecOps, integrating security practices directly into development workflows rather than treating them as afterthoughts. Donald Firesmith called it the [**four types of shift left testing**](https://insights.sei.cmu.edu/blog/four-types-of-shift-left-testing/), differentiating between traditional shift left, incremental shift left, Agile/DevOps shift left, and model-based shift left.


More recently, the data community has adopted these principles, with approaches like data contracts or tools like SDF applying a shift left to data quality and governance. This latest evolution focuses on pushing data validation and business logic upstream toward data producers, with companies like Gable, Confluent on [Shift Left in Data Integration](https://www.confluent.io/learn/what-is-shift-left/), and [SQLMesh](https://github.com/TobikoData/sqlmesh) expanding the concept.


The evolution from testing to security to data domains demonstrates how the shift left has become more talked about. I discovered shifting left while writing about [Designing a Declarative Data Stack](https://www.rilldata.com/blog/designing-a-declarative-data-stack-from-theory-to-practice), exploring how declarative systems enable generating data stacks, separating business and technical logic, and simplifying transformations.


## What Are We Shifting?


Now that we know what shifting left is, the question is, *what* exactly are we shifting? Is it code, queries, and business logic all together?


In essence, we shift two primary artifacts:

1. **Shift-left data quality**: Moving **responsibility, ownership and accountability** left to automate/integrate into data engineering. This is what most people mean when they say shifting left today.
2. **Shifting left code/logic (the *How*)**: Newer declarative approaches have recently made shifting left (logic) possible. This is a lesser-known topic, and I want to focus more on it in this article.


Here’s a simple example of what we are shifting:


![/blog/shifting-left/hero%20no%20title.png](https://www.ssp.sh/blog/shifting-left/hero%20no%20title.png)

*Showcasingwhatwe shift left*


The concrete examples of shifting components and their benefits are:

- **Moving joins out of the BI tool and into the database or data model** improves performance with faster dashboard queries by pre-computing complex joins.
- **Moving transformations from the database to ingestion/orchestration** reduces costs through less data transfer and leveraging cheaper compute resources outside the database.
- **Moving schema definitions from the database to source Iceberg tables** enhances data quality by enforcing data integrity constraints earlier in the pipeline, preventing bad data from entering the system.


### The Declarative Way of Shifting Left


Today, with a [declarative data stack](https://www.rilldata.com/blog/the-rise-of-the-declarative-data-stack) that has a code-first approach where configuration is defined as code, critical transformations can be shifted left, too.


This way, we can move logic (mostly business logic) upstream. Usually, data flows from source and ingestion on the left to consumption and dashboards on the right. If we load data from the source, add transformations, and visualize in a BI tool, a valuable business aggregation that is slow in the BI tool can be transferred to the ETL (e.g., SQLMesh, dbt) or into the semantic layer. I believe this is only possible with new code-first approaches.


Shifting left is especially advantageous when you’re just starting out because it allows you to place code/logic on the **far right side** initially and then **shift it left** when you **better understand** of your needs and architecture. By shifting left, we encounter data processes, validation, and quality controls earlier in the data lifecycle. When we think of transformation logic (mainly SQL), we can move that transformation around.


Errors identified and fixed earlier (more to the left) are **less expensive** and typically easier to debug. This was not possible with GUI-first approaches; **code-first tools** open up new possibilities.


A BI tool with its measures and dimensions expressed as “code” (mostly YAML) can easily move them to another tool that uses YAML to express its transformation. A Python transformation can be converted more easily than when SQL statements and aggregations are strongly integrated into the BI tool, hidden away from users with no code to copy or move the metrics downstream. Even more so with large language models (LLMs), we have the power to quickly translate YAML calculations to Python code if needed, opening the toolbox to many more people with less technical expertise.

Chad in The Shift Left Data Manifesto about 'Data as Code'
Most data quality problems are code quality problems. Chad
[emphasizes](https://dataproducts.substack.com/p/the-shift-left-data-manifesto)
that “data is produced by code” - a framing that connects data quality directly to software engineering practices. This perspective helps explain why data quality should be handled at the source rather than downstream and brings the declarative data stack (data as code) together with the data quality aspect of shifting left.

## Benefits: Why Are We Shifting Left


Why should we shift left? What are the key benefits of it?


We’ve all experienced it—CEOs or business users telling us that “the Data is Wrong”. This is an unfavorable place to discover problems, as **fixes must cascade through all layers** of the data lifecycle. It is also the furthest to the right a problem can appear. The earlier you catch issues (on the left), the easier they are to test and fix before they create business impact.


Elias DeFaria [says](https://www.linkedin.com/posts/eliasdefaria_dataquality-sdf-dbt-activity-7242955996338253826-weKX/?utm_source=share&utm_medium=member_ios&rcm=ACoAAA8b34wBAGePYTF8F0DKfvHgH6SdomuMzM8), “CI/CD checks, Write-Audit-Publish (WAP), and other methods help shift things left—but ultimately, data quality is best caught by tools that compile and check your SQL during development”. And he is right. Catching complex data errors early in the data flow will **save us** a lot of debugging, development time, and, ultimately, money.


We want to shift left whenever possible in a typical data engineering architecture with complex lineage and various data sources. This becomes particularly valuable as data platforms and architectures mature. It’s not typically the first optimization but becomes increasingly important when focusing on **performance** or **data quality** improvements.


The shift-left approach delivers several key benefits:

1. **Quality and Error Prevention**: Earlier error detection through unit tests in orchestrators and data runtime tools (SQLMesh, dbt) before they reach semantic layers or BI tools. Bugs caught closer to the source are easier and less expensive to fix.
2. **Cost and Performance Optimization**: Complex calculations happen once in the transformation layer instead of repeatedly at query time, reducing compute costs through pre-materialization. With a code-first approach, we can easily move aggregations/joins to the left.
3. **Business Logic Management**: Define calculations once without duplication across dashboards so all downstream tools use consistent definitions of key business metrics. This centralizes logic with teams responsible for data governance, improving maintainability and creating clearer lineage.
4. **Architectural Benefits**: A more modular design with better separation of concerns enables consistent governance policies. The declarative approach allows components to be moved throughout the pipeline without significant rewrites, simplifying impact analysis when changes are needed.
5. **Role Transformation**: Shift-left enables domain experts to implement data tests, allowing data-savvy people across the organization to contribute upstream. This applies software engineering best practices to data pipelines, making data quality a collective responsibility.


By shifting left, data teams can create more maintainable, performant, and reliable data systems while reducing duplication and inconsistency throughout the data stack.


### Better Data Quality: Earlier Validation


Data quality is the most significant benefit you gain. This does not come from day one; with a more mature data stack, the more you’d want to shift left, and the more data quality you’ll get from the data stack.


![/blog/shifting-left/data-quality-shift.png](https://www.ssp.sh/blog/shifting-left/data-quality-shift.png)

*Data quality shift | Image byÂdevopedia.org*


The goal is to test as much as possible to the left, focusing on quality earlier. Starting from your development environment and later within the CI/CD pipelines, to reduce data quality issues and errors in production. This means we can test critical code **before runtime** on production.


This is something we should try whenever possible, though it’s [trickier with data](https://airbyte.com/blog/data-quality-issues). Since data is created out of our control, we’re limited to testing what’s in our test datasets, making an important trade-off between comprehensive testing and pipeline speed. While unit testing key functions is valuable, [**integration tests**](https://en.wikipedia.org/wiki/Integration_testing) are often more powerful. These end-to-end tests use SQL queries to verify counts at different pipeline stages, ensuring we haven’t lost or duplicated data through transformations.


In my career, we often tried to skip these tests initially, only to add them later after spending too much time debugging. When implemented properly, these tests build trust in the data—engineers and business users know when data has no missing rows and get immediate alerts when issues arise.


Modern orchestration tools now allow embedding these tests directly within your workflow, strengthening governance and data quality at the core of computation.

Organizational Change
Shifting left in the data quality sense is also often a change of organization. You define that models are defined centrally by a team, or that schema validations are done earlier in the process, that business analysts are using existing aggregations instead of duplicating existing ones, or re-use complex business logic that is materialized in a cleaned and well-managed data layer. If we want to enforce these data quality improvements, most often it requires organizational change, not just a technical solution.

### Local Development Loop, Transpiling SQL-Dialects and CI/CD


If we look at the local development loop and its benefits, we can see that it improves **developer workflow** by shifting more to the developer, essentially to the client (the developer’s IDE). Tools like [linting](https://en.wikipedia.org/wiki/Lint_%5c%28software%5c%29) and compiling data artifacts allow rich tests without running them. This is the ultimate version of shift-left data quality. It enables developers to **catch bugs in their pipelines** literally as they’re writing them. If 100% of issues were caught during development, data quality would never be a concern.


The local development loop is now possible with tools that reach further into the data lineage. Instead of having to run it in production or creating a duplicate production environment, we can mimic cloud ETL and data warehouse locally with DuckDB and DataFusion and run our schema validation and data pipelines while we develop, detecting errors very early in the flow.


![/blog/shifting-left/shifting-left%20local%20dev%20cycle-loop.jpg](https://www.ssp.sh/blog/shifting-left/shifting-left%20local%20dev%20cycle-loop.jpg)

*Example of inner development cycle loop, including transpilation of SQL dialects*


This is also possible due to powerful SQL transpilers like [SQLGlot](https://github.com/tobymao/sqlglot). In times where SQL is most dominant, this is key. Let’s say you have a query that needs to run for Spark SQL, but locally you want to test with DuckDB. SQLGlot can transpile the Spark dialect to DuckDB without changing the code. As of today, SQLGlot transpiles [24 dialects](https://github.com/tobymao/sqlglot/blob/main/sqlglot/dialects/__init__.py). In fact, SQLMesh, built on top of SQLGlot, brings more benefits to the table that help us tremendously with shifting left. SQLGlot is not only a transpiler but also a SQL parser.


SQLMesh, a self-named DataOps solution for transformation, testing, and collaboration, reduces the likelihood of invalid SQL making it from development to production. It can validate and compile things on dev to test schemas across the whole data lineage. This includes catching breaking changes and avoiding potential backfills and unit testing CTEs. SQLMesh even supports table diffing between production and dev, which is valuable for better understanding the changes you’re about to deploy.


**Another place to catch errors** is after we have developed a solution and before pushing to production, in the **CI/CD pipeline**. This is the default in software engineering projects, but not yet in all data projects, as we need to do much more work, creating quality test data sets and defining some count-query statements (or if domain knowledge is available, we can add more complex ones).

SQL is Shifting to the Right
In contrast to data quality that is shifting left, SQL is shifting to the right as well. With the code-first BI tools and semantic layers and SQL being a ubiquitous language of data engineers, more and more SQL is going all the way to the right. SQL is also a consistent declarative language across the data stack, that we can easily shift around.

### Benefits of Declaratively Shifting Left


So far, we’ve explored shifting left mostly through the lens of improving data quality by moving ETL and code to the left. However, I want to add one more angle and improvement we get when embracing a declarative data stack: the *how*. How do we actually move aggregations, joins, and transformation logic to the left?


If we consider the data stack a declarative set of deployed and configured configurations, you can shift left by moving SQL from a BI tool to the ETL tool. The key is to shift left by moving the configuration easily. This is very hard, if not impossible, with distinct tooling as part of the data stack and configurations tightly coupled into the UI.


When we allow moving code and transformation more efficiently, we open up the possibility of moving transformative logic closer to the source, ultimately needing to **fix bugs on fewer levels**. This shifting left brings the complex transformation closer to the team in charge of data pipelines and data governance (e.g., data engineers, DevOps, etc.). Therefore, it’s governed and updated by a team with responsibilities. On the other hand, when logic remains to the right, domain experts and business people implement something quickly to achieve a specific KPI, not having maintainability, performance, or deployment in mind.


We save compute by moving code from the BI dashboard, which is executed every time a user clicks on the dashboard, to a pipeline where the query is pre-materialized and only paid for once. This approach also likely avoids code duplication at many places around the data stack.


### Shift of Data Roles


Through the code-first data stacks, it’s easier to shift code or configuration. This allows data roles’ responsibilities to move to the left, too. All of a sudden, domain experts can implement a data test in dbt, or data engineers can assert source data schemas. With data as code and declarative data stack, data-savvy people can shift more to the left.


QA engineers, testing teams, or domain experts involved in the data modeling process can now move further to the left and help improve data quality overall. Beyond that, we can define software best practices like source control versioning, testing, CI/CD, and code reviews because we have code end-to-end. As the saying goes, data quality isn’t a data team’s problem; it’s clearly defined best practices that everyone in the organization understands and can follow.

'ELT' compared to ETL is shifting right, an anti-pattern?
[ELT](https://en.wikipedia.org/wiki/Extract,_load,_transform)
, extracting and loading before we transform, is actually moving to the right. In terms of improving quality, performance and all the benefits discussed later, ELT can be seen as an anti-pattern of shifting left. Validations, transformations, and aggregations get moved right.

## Practical Examples of Shifting Left


Let’s look at a simple, but practical example. Broadly, the shifting left is illustrated like this:


![/blog/shifting-left/practical-example-shifting-left.jpg](https://www.ssp.sh/blog/shifting-left/practical-example-shifting-left.jpg)

*Example pipeline showcasing shifting left*


The above illustration shows how logic from the BI layer (right) moves upstream to the execution engine, transformation, and ingestion layers (left). Here’s how this works in practice with multiple dashboards.

Shown examples embrace the declarative approach already
The examples below already use a declarative approach, where the BI tool and metrics are defined with YAML.

### Before Shifting Left: Duplicate Complex Logic


Initially, multiple dashboards each implement similar complex calculations based on `trips_raw` with slight variations in their filtering logic.


**Executive Dashboard:**



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
` | `metrics:
  - name: high_value_trip_duration
    sql: >
      WITH trip_calculations AS (
        SELECT 
          pickup_zone_id,
          dropoff_zone_id,
          EXTRACT(HOUR FROM pickup_time) AS hour_of_day,
          TIMESTAMPDIFF(MINUTE, pickup_time, dropoff_time) AS duration_minutes,
          fare_amount + tip_amount AS total_fare
        FROM trips_raw
        WHERE trip_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
        AND trip_status = 'completed'
        AND fare_amount > 50 -- Executive wants to look at high-value trips above $50
      )
      SELECT AVG(duration_minutes)
      FROM trip_calculations
      WHERE hour_of_day BETWEEN 7 AND 10 -- Executive focus on morning rush hour
` |



**Operations Dashboard YAML:**



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
` | `metrics:
  - name: rush_hour_trip_duration
    sql: >
      WITH trip_calculations AS (
        SELECT 
          pickup_zone_id,
          dropoff_zone_id,
          EXTRACT(HOUR FROM pickup_time) AS hour_of_day,
          TIMESTAMPDIFF(MINUTE, pickup_time, dropoff_time) AS duration_minutes,
          fare_amount + tip_amount AS total_fare
        FROM trips_raw
        WHERE trip_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) -- Operations wants more recent data (30 days)
        AND trip_status = 'completed'
      )
      SELECT AVG(duration_minutes)
      FROM trip_calculations
      WHERE hour_of_day BETWEEN 16 AND 19 -- Operations focus on evening rush hour
` |



**Customer Experience Dashboard YAML:**



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
` | `metrics:
  - name: weekend_trip_duration
    sql: >
      WITH trip_calculations AS (
        SELECT 
          pickup_zone_id,
          dropoff_zone_id,
          EXTRACT(HOUR FROM pickup_time) AS hour_of_day,
          EXTRACT(DAYOFWEEK FROM pickup_time) AS day_of_week,
          TIMESTAMPDIFF(MINUTE, pickup_time, dropoff_time) AS duration_minutes,
          fare_amount + tip_amount AS total_fare
        FROM trips_raw
        WHERE trip_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY) -- Customer Experience wants medium-term data (60 days)
        AND trip_status = 'completed'
      )
      SELECT AVG(duration_minutes)
      FROM trip_calculations
      WHERE day_of_week IN (1, 7) -- Customer Experience focus on weekends
` |



What each of them wants is:



| Dashboard | Time Period | Trip Value Filter | Time Focus |
| **Executive** | 90 days (long-term) | High-value trips only

`(fare_amount > 50)` | Morning rush (7-10 AM) |
| **Operations** | 30 days (recent) | All trips | Evening rush (4-7 PM) |
| **Customer Experience** | 60 days (medium-term) | All trips | Weekends (day_of_week IN (1, 7)) |



Notice how all three dashboards share nearly identical calculations in the [CTE](https://www.atlassian.com/data/sql/using-common-table-expressions) with slightly different date range filters and apply different WHERE clauses to filter the same base calculation. This repeats the same business logic across dashboards.


### After Shifting Left: Centralized Logic in SQLMesh


By shifting left, we move the common calculation logic into a centralized SQLMesh model `trip_metrics.sql`:



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
` | `MODEL (
  name ride_service.trip_metrics,
  kind INCREMENTAL_BY_TIME_RANGE (
    time_column trip_date
  ),
  start '2025-01-01',
  cron '@daily',
  grain (trip_id, trip_date),
  description 'Incrementally processed trip metrics for analytics dashboards'
);

SELECT
  trip_id,
  pickup_zone_id,
  dropoff_zone_id,
  pickup_time,
  dropoff_time,
  EXTRACT(HOUR FROM pickup_time) AS hour_of_day,
  EXTRACT(DAYOFWEEK FROM pickup_time) AS day_of_week,
  EXTRACT(DATE FROM pickup_time) AS trip_date,
  TIMESTAMPDIFF(MINUTE, pickup_time, dropoff_time) AS duration_minutes,
  fare_amount,
  tip_amount,
  fare_amount + tip_amount AS total_fare,
  trip_status
FROM trips_raw
WHERE trip_status = 'completed'
AND trip_date BETWEEN @start_date AND @end_date
` |



With this pre-materialized table, our dashboard metrics become dramatically simpler:



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
` | `metrics:
  --Executive Dashboard YAML
  - name: high_value_trip_duration
    sql: >
      SELECT AVG(duration_minutes)
      FROM trip_metrics
      WHERE trip_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
      AND fare_amount > 50  -- Executive focus on high-value trips
      AND hour_of_day BETWEEN 7 AND 10  -- Morning commute time
  --Operations Dashboard YAML
  - name: rush_hour_trip_duration
    sql: >
      SELECT AVG(duration_minutes)
      FROM trip_metrics
      WHERE trip_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)  -- More recent operational data
      AND hour_of_day BETWEEN 16 AND 19  -- Evening rush hour
  --Customer Experience Dashboard YAML
  - name: weekend_trip_duration
    sql: >
      SELECT AVG(duration_minutes)
      FROM trip_metrics
      WHERE trip_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
      AND day_of_week IN (1, 7)  -- Weekend focus for customer experience team
` |



This is a simple example, and we could have done the same within a BI tool; they usually allow you to create datasets or tables, too, though these can become unmanageable relatively quickly.


Imagine this approach could be applied to any other part of the data stack. Imagine a dbt test that gets put into an orchestrator test that runs before execution, or a transformation from a BI dashboard to the central semantic layer if you want your KPIs to be accessible through the API to all your requesting applications instead of only in a single notebook or BI dashboard.


#### Changing Timestamp Column


Another practical example around data quality tests could be changing a timestamp column from local time to UTC.


Tools like SQLMesh, SDF, or Gable can detect this change before deployment, identify which downstream data pipeline or even data science models depend on that data in its current format, and notify the engineer and the data scientist about the potential impact.


## Limitations and Possibilities


Besides all these new features and possibilities, we won’t get around some core challenges every data team and organization has.


### Communication is still needed


We still need to communicate with the **data producers**. We need a process, which can also be a meeting, where big changes in the source applications are communicated.


Early in my career, we tried to **fix data upstream** as much as possible in the source. We set up meetings with the team producing the source data. We do the same with shifting left, but with more advanced tooling and, ideally, less manual interaction, though manual interactions will never disappear completely.


Another limitation that Stephen Bailey [talks about](https://stkbailey.substack.com/p/shift-left-ship-everywhere) is that **pipelines are not linear** but rather like a “maritime economy”. He calls it the “ship everywhere” instead of only “left”. He says that it’s more interconnected. Data products, the data assets and data sets produced, are heterogeneous, dependent, and extremely sensitive to external factors. This is true; upstream changes in the data source can have big impacts on our data stack, as can external consumers that process and use the insights from a data stack.


### Possibilities with GenAI Integration


Shifting left with the declarative code-first approach in mind gets even more powerful with new [GenAI tools](https://www.rilldata.com/blog/one-click-dashboards-with-generative-ai-and-bi-as-code#how-llm-code-generation-speeds-up-dashboard-creation). With large language models (LLMs), people are **enabled to move fast**—they build data transformations or aggregations quickly within their comfort zone of SQL or Python as data scientists. You could call that a shift right toward applications and AI integration, but to be honest, GenAI can be applied everywhere along the data lifecycle.


But once you want to put it into production, it gets trickier. The way to go is to shift left and put it into dbt, a proper orchestration tool, or anything else that makes the jobs run automatically, versioned, and with software best practices in mind. We get the separation between “exploration” and “production-ready”, verified, and tested.


LLMs can also help us speed up the translation from a data notebook in Python to SQL or from an ANSI SQL standard to a Snowflake dialect with enhanced options.


## Key Takeaways for Data Practitioners


So, what is the takeaway for everyday data work?


We can acknowledge that this is a very new term, but it represents something we have been doing in the data ecosystem for a long time. Data modeling or data architecture is, if you will, thinking about shifting left. We have the entire data flow in mind; we want to avoid duplication and create a fast data mart that serves our business users and dashboards. We choose tools and frameworks; we decide what to persist and how often. All these questions we analyze in data architecture are essential for knowing when and what to shift.


What has changed are the tools that allow us to do these data quality tests more in line, directly at the beginning, without adding an extra data pipeline just for testing or data quality.


What has also changed is the speed of computation. We can evaluate large datasets locally or use DuckDB or DataFusion as fast engines to quickly assess all types over the full data lineage. While we write our SQL within SQLMesh, the linter will tell us about errors based on richly collected metadata from source tables through nested lineage. Things like this weren’t possible 10 years ago.


A significant enabler of effective shifting left has been the [rise of declarative](https://www.rilldata.com/blog/the-rise-of-the-declarative-data-stack), the code-first approaches. By expressing transformations, metrics, and business logic as code instead of embedding them in GUI-based tools, we’ve unlocked the ability to move these components throughout the data pipeline easily. This declarative approach means we can start with logic positioned where it’s most convenient (often on the right), then systematically shift it leftward as our understanding of data patterns and performance needs evolves—all without significant rewrites or manual translations between systems.

Danny on Bluesky adds a good comment about how it simplifies pipelines
To me it
[means](https://bsky.app/profile/citizenkong.com/post/3lk6efjmrek2d)
pushing complexity upstream, keeping business logic inside the business process so that the data pipelines can be relatively simple. In my org, it means SMEs can keep control of their modeling, and as long as outputs adhere to the contract, everything downstream will still work.

Looking ahead, new approaches continue to emerge that will further enable shifting left. [Google’s Pipe Syntax](https://research.google/pubs/sql-has-problems-we-can-fix-them-pipe-syntax-in-sql/) in [SQL and extensions for analytics](https://www.datacouncil.ai/talks/cubing-and-metrics-in-sql) are making SQL more composable and maintainable, allowing complex analytical capabilities to be defined directly in the data layer rather than in BI tools. As data roles continue to evolve, shift-left principles are becoming increasingly important to building scalable, consistent data platforms.


I hope this article helped you better understand shifting left and why it’s a good practice to remember when building data platforms or pipelines. Again, shifting left is not a rigid or well-defined term, and everyone might interpret it differently, but we have identified the different angles that shifting left encompasses.


As you evaluate your data architecture, consider where shifting left might benefit your organization—creating more robust, reliable data quality and better equipping you to meet the demands of our increasingly data-driven world.


## Further Reads

- [“Shift left”—wtf does it mean?](https://sourcegraph.com/blog/shift-left-wtf-does-it-mean)
- Follow the Shift Left motion: [The Mindset Behind Declarative Programming](https://medium.pimpaudben.fr/the-mindset-behind-declarative-programming-31361ea5598f)
- If you want to know more, the data contract company Gable hosted a [Shift Left Data Conference](https://www.shiftleftdata.com/) ([video playlist](https://youtube.com/playlist?list=PL-WavejGdv7J9xcCfJJ84olMYRwmSzcq_&si=iWIK_Yz4rWnGc6da) is on YouTube).
- [The Shift Left Data Manifesto](https://dataproducts.substack.com/p/the-shift-left-data-manifesto)
- [Shift left, ship everywhere](https://stkbailey.substack.com/p/shift-left-ship-everywhere)


---


```
Full article published at Rilldata.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/shifting-left/)
|
[Rill](https://www.ssp.sh/tags/rill/)
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Data-Warehouse](https://www.ssp.sh/tags/data-warehouse/)
[Cloud Data Warehouse](https://www.ssp.sh/tags/cloud-data-warehouse/)
[Shifting Left](https://www.ssp.sh/tags/shifting-left/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Modern Data Stack](https://www.ssp.sh/tags/modern-data-stack/)
[Yaml](https://www.ssp.sh/tags/yaml/)
[Declarative Data Stack](https://www.ssp.sh/tags/declarative-data-stack/)
[Services](https://www.ssp.sh/tags/services/)
