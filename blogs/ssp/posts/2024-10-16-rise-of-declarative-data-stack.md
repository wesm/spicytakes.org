---
title: "The Rise of the Declarative Data Stack"
date: 2024-10-16
url: https://www.ssp.sh/blog/rise-of-declarative-data-stack/
slug: rise-of-declarative-data-stack
word_count: 4078
---

![The Rise of the Declarative Data Stack](https://www.ssp.sh/blog/rise-of-declarative-data-stack/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Data stacks have come a long way, evolving from monolithic, one-fits-all systems like Oracle/SAP to today’s modular open data stacks. This begs the question, what’s next? Or why is the current not meeting our needs?


As we see more analytics engineering and software best practices, embracing codeful, Git-based, and more CLI-based workflows, the future looks more code-first. Beyond SQL transformations, across the entire data stack. From ingestion to transformation, orchestration, and measures in dashboards—all defined declaratively.


But what does this shift towards declarative data stacks mean? How does it change how we build and manage data stacks? And what are the implications for us data professionals? Let’s find out in this article.


## A Brief History of Declarative Systems


Often, we forget how hard it was in the old days.


Let’s take [Fortran](https://en.wikipedia.org/wiki/Fortran), one of the earliest high-level programming languages. It was revolutionary for its time, but it required programmers to think in terms of the computer’s architecture and know the ins and outs of everything.


Or SQL, did you know it’s declarative? Or Markdown, HTML, or Kubernetes? Most of them are growing in enthusiasm and support each year1, but why? The below table gives you an idea of how declarative is more straightforward, whereas imperative is very verbose and hard to read.



| Comparison | Declarative | Imperative |
| **Data Transformation (NumPy vs. Fortran)** | `import numpy as np
result = np.mean(np.array
  ([1, 2, 3, 4, 5]))` | `PROGRAM AVERAGE
  REAL :: numbers(5), sum, average
  DATA numbers /1.0, 2.0, 3.0, 4.0, 5.0/
  sum = 0.0
  DO i = 1, 5
    sum = sum + numbers(i)
  END DO
  average = sum / 5
  PRINT *, 'Average is:', average
END PROGRAM AVERAGE` |
| **Text Formatting (Markdown vs. Manual Text Manipulation)** | `**Bold text**` | `let text = "Bold text";
console.log("\x1b[1m" 
+ text + "\x1b[0m");` |
| **Data Query (SQL vs. Procedural Code)** | `SELECT * FROM users 
WHERE age > 18;` | `for user in users:
    if user.age > 18:
        result.append(user)` |
| **Container Orchestration (Kubernetes vs. Manual Setup)** | `kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:1.0` | (Multiple manual steps to set up and manage containers across multiple servers) |


1. SQL for database queries
2. Functional programming languages
3. Declarative UI frameworks (e.g. Rill, Evidence, React)
4. Configuration management tools (e.g. Kubernetes)


### Examples of Declarative Data Stack (Airflow/dbt/Kubernetes/Rill)


With Kubernetes, you declare what you want, and the system will bring it to that state. This means the how-to is abstracted away, and you can focus on the *what* of your app.


On the other hand, using **Airflow**, you define every little step of the how inside your DAG; mixing business logic with technical boilerplate makes it inherently complicated and hard to decouple and get clarity in your runtime pipelines.


If you see **Dagster**, where you have “only” the business logic, what you want to do as part of your DAG, and everything else is outsourced into [resources](https://docs.dagster.io/concepts/resources) or [Dagster Pipes](https://docs.dagster.io/concepts/dagster-pipes), defining your compute with a [simple annotation](https://github.com/dagster-io/dagster-modal-demo/blob/60f889cb7ce15fb09da4680bf314cf1d35095d7d/dagster_modal_demo/pipeline_factory.py#L74) `compute_kind="modal"` or `compute_kind="spark"`, not needing to care if it’s locally or on production, shows you the power of declarative with the side-effect of knowing your tools.


Comparing **dbt with SQLMesh** is another one, where SQLMesh understands plus parses the SQL with [SQLGlot](https://github.com/tobymao/sqlglot) to get a semantic understanding of what the SQL does, giving it advances for powerful context-aware functions that dbt won’t be able to do.


Semantic Layers and BI tools define metrics within YAML (**Cube, Rill**), dashboards can be created entirely in Markdown (Evidence), and data pipelines are created on top of YAML (Kestra, Dagster).


Call it Infrastructure as Code, Visualization as Code, BI as Code, or anything as code. YAML engineering, or DSL (Domain Specific Language)—no matter what, it’s the way the data stack evolved to **empower non-programmers** to create data pipelines and infrastructure without losing the benefits of SW engineering best practices through declarative methods.


## What Is a Declarative Data Stack?


A declarative data stack is a set of tools and, precisely, its configs can be thought of as a **single function** such as `run_stack(serve(transform(ingest)))` that can recreate the entire data stack.


Instead of having one framework for one piece, we want a combination of multiple tools combined into a single *declarative* data stack. Like the Modern Data Stack, but integrated the way Kubernetes integrates all infrastructure into a **single deployment**, like YAML.


We focus on the end-to-end [Data Engineering Lifecycle](https://ssp.sh/brain/data-engineering-lifecycle), from ingestion to visualization. But what does the combination with declarative mean? Think of [Functional Data Engineering](https://ssp.sh/brain/functional-data-engineering), which leaves us in a place of **confident reproducibility** with little side effects (hopefully none) and uses [idempotency](https://www.ssp.sh/brain/idempotency) to restart function to recover and reinstate a particular state with conviction or rollback to a specific version.

Doesn't Exist Today
This doesn’t exist like this today; some platforms come close, but they are either closed-source or only cover a subset of the complete data stack. See more on this in “What are the Alternatives?” in Part 2.

## Why a Declarative Data Stack


The opposite would be an imperative data stack. The imperative way works well for simple homogenous systems. It is flexible and gives us a high level of control. However, it has the downside of a hard-to-manage state, so automatic integrity checks or failure management are needed.


But it’s not the right choice if you combine a heterogeneous data stack into a **single data platform**. The declarative approach manages complexity in a simple interface for non-technical users by abstracting away implementation details and focusing on the outcomes instead. It builds the foundation for a consistent, reproducible data platform across diverse components.


A declarative data stack cleanly separates semantics from implementation, **decoupling** the business code from technical implementation, the *how* is rendered by the data stack engine. This gives us a **stateless stack** that can be recreated from scratch with its configuration, setting aside intermediate data assets (stateful) produced along the way.


Think of Markdown. It is **universally portable**, and almost every application can render it with its various engines, such as HackMD, Obsidian, iA Writer, Neovim, and GitHub, to name a few. There is no need to fiddle with setting things up or configuring, as the Markup language defines everything—the engine decides/handles the rendering. The best part is that even images can be declaratively defined with [Mermaid](https://www.ssp.sh/brain/mermaid). Similarly, the declarative stack is programming language agnostic.


Let’s compare when to use which stack.



|  | Declarative Data Stack | Imperative Data Stack Management |
| **Core Concept** | Define ‘what’ you want, the system handles ‘how’ | Specify each step and process explicitly |
| **Key Benefits** | - Single deployment file for entire stack
- Version-controlled infrastructure
- Reproducible environments
- Separation of business logic from technical details | - Granular control over components
- Flexibility for unique scenarios
- Easier optimization of individual parts |
| **Challenges** | - Learning curve for declarative syntax
- May require custom extensions for specific tools
- Debugging can be more complex | - Manual configuration and maintenance
- Risk of configuration drift
- Time-consuming setup and modifications
- Inconsistencies between environments
- Hard to track changes and rollback |
| **Empowerment** | - Enables less technical users to manage complex data systems:
- Infrastructure as Code for data
- Automated dependency management
- Built-in data governance and security
- Integrated monitoring and observability | Requires more technical expertise across the stack:
- Direct access to underlying systems |
| **Best For** | - Large-scale, consistent data operations
- Teams adopting software engineering practices (frequent iterations)
- Organizations prioritizing governance and compliance | - Small to medium-scale projects
- Highly customized or unique workflows |



### YAML: The Language of Declarative Configuration


YAML, Yet Another Markup Language, has become the configuration markup language for most modern tools. The reasons are simple: Compared to its predecessors, XML and JSON, which are still highly used, YAML is **less verbose**.


Image comparison between XML, JSON, and YAML


Besides their different reasons for use, XML is designed to support structured documents, while JSON should be simple and universal and can quickly be processed; JSON has been mainly used for small data sets and REST services. YAML has similar threats but tries to be a superset of JSON, although every JSON can effectively be a valid YAML file.


But why is YAML used for declarative configurations? It supports lists and dictionaries with almost no overhead. YAML is optimized for reading extended configurations. Its descriptive and portable structure across different programming languages and its clear interface make it easy to maintain, read, and modify, making it well-suited for this task.


YAML is also used when implementing a [DSL (Domain-Specific Language)](https://en.wikipedia.org/wiki/Domain-specific_language) in your application. A DSL abstracts the complexity behind a system. It is a general-purpose language aimed at any software problem. Like Markdown or another example of HTML, it’s programming language agnostic; the engine, the browser, does not care how you generated the HTML; it knows what to do with it. That’s the goal of DSL, too.

Longevity
Also, if you are declarative, you can make the code work for a very long time. For example, the browser runs the code from Craigslist from 1995, and it’s only possible to this day because HTML is declarative.

## Which Components Form an End-to-End Data Stack?


For it to be a complete data stack, we need to integrate data from its source systems, transform, aggregate, and clean data, and ultimately serve and visualize it, solving the [core challenges](https://www.dedp.online/part-1/1-introduction/challenges-in-data-engineering.html) in data engineering.


We cover all of these with the Data Engineering Lifecycle. Let’s go through them one by one.


Illustration of the data engineering lifecycle from the book [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)


### Ingestion


Ingestion is the part that integrates the data sources into your data stack. Usually, your source types are OLTP databases, some files in a S3 bucket, or APIs.


Naturally, this is a very imperative process. You write a bunch of code, historically with procedural code or, in the modern world, with Python. But everything is writing the integration code, meaning the how. So, how do we get a more declarative approach? Wasn’t there a declarative language that is quite popular?


Yes, SQL. SQL is declarative. You say which columns (`SELECT columns`) from which table (`FROM table`) and with some criteria (`WHERE`) and some aggregations (`GROUP BY`). The rest is done by the SQL engine, typically the database, the Spark cluster, or anything else.


The most straightforward way is using the SQL approach and wrapping `select * from s3://my-source-bucket/sales/*.parquet` into an orchestrator or using something like [dlt](https://github.com/dlt-hub/dlt). dlt is, per se, not a declarative tool (except the REST API), but you can use it in a declarative fashion, e.g., configure a YAML to define all the columns and tables you want to ingest. Or you can use Airbyte and Dagster to create sources and destinations declaratively, essentially [Data Integration as Code](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/). [Ibis](https://github.com/ibis-project/ibis) is another lightweight, universal interface for data transformation; it uses Python and, therefore, is not declarative out of the box. However, you can interchange your SQL engine, too, while writing the code only once.


### Transformation


The most significant layer of any data stack is the transformation or ETL part. As this is primarily done in SQL, we are fine here, right?


Not really. As SQL has limitations, no variables, lots of duplications, hard to define best practices, many have come to love dbt. dbt is a nice wrapper around SQL that gives you super powers through templating with [Jinja](https://www.ssp.sh/brain/jinja-template/) and with goodies of documentation including lineage, versioning, and automating of your lost SQLs.


But with that, we are back to an imperative way. As dbt doesn’t know anything about its SQLs, it **just runs** them; it’s limited to doing anything data-aware.


Newer tools, especially [SQLMesh](https://github.com/TobikoData/sqlmesh) and its open-source SQL parser SQLGlot, can analyze queries, traverse expression trees, and programmatically build SQL. We can also use them for declarative transformation. Especially with SQLMesh, we get a better understanding of semantics. This will give us the power to describe our transformations declaratively, even with live compiler checks, before running anything.


With that, it can automatically pre-detect breaking changes and run a missing backfill. The best thing is that SQLMesh is backward and compatible with dbt.


### Serving


Visualizing and serving data in the correct format, whether as a data app, AI, or dashboard, is essential in your data stack. No matter how good your data quality and insights are, cleaning and transforming will be well-spent if you can present them in an easy-to-understand way.


Speaking of waste, the second wasteful time you can do is recreate the same dashboards repeatedly and change the measure on each so very slightly. This is where the power of declarative hits for visualization. Could you copy and paste the definition of a dashboard and replace the measure? That is precisely what we do with Rill or Evidence (interestingly with Markdown).


Here’s a declarative dashboard example in Rill:


This example, **visualization as code**, takes this declarative approach further, allowing us to define visualizations using structured data modeling syntax. The [Grammar of Graphics](https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149) is a related concept, a theoretical framework that breaks down statistical graphics into semantic components. Tools like ggplot2 in R and [Vega-Light](https://vega.github.io/vega-lite/) implement this grammar, enabling users to describe the relationships between data and visual elements rather than specifying how to draw the chart.


By embracing these declarative approaches to visualization, we can create more maintainable, flexible, and robust data presentations as part of our declarative data stack, focusing on what we want to communicate rather than the intricacies of how to draw it.


An excellent feature that can be integrated into a declarative approach is [access permissions](https://docs.rilldata.com/reference/project-files/rill-yaml#testing-access-policies) with **access policies**.

A Fascinating Idea Is to Extend SQL with Analytical Capabilities
As Julian Hyde explains in his talks about Cubing and essentially
[Extending SQL for Analytics](https://www.youtube.com/watch?v=oo1uwJ3qHwE)
, SQL could be extended to incorporate a metrics or semantic layer directly into the language. This extension includes adding measures to SQL tables, allowing queries to return measures (expressions) instead of values, and introducing new syntax for cross-dimensional calculations. These extensions make complex analytical queries as concise and intuitive as natural language questions, potentially transforming how we approach data analysis and business intelligence. This approach aligns with the declarative nature of SQL and could further bridge the gap between data storage, analysis, and visualization in a unified, declarative framework.
How Does a Semantic Layer Play Into This?
A
[Semantic Layer](https://ssp.sh/brain/semantic-layer)
serves SQL and visualizes measures, and it can be a way of declaratively defining metrics and dimensions.

### Undercurrents


In addition to these three main components of a data stack, there are some undercurrents across the data stack. We’ll focus only on three and keep it brief, as this could be another blog post.


#### Orchestration


Orchestration is the central piece that manages all moving parts. If you will, the orchestrator is the **engine** in which the *how* of your declarative data stack can be implemented. You can write the technical logic of fetching data from an API service, partition your data to optimize speed, and integrate different tools of your stack into a **single data platform**.


Orchestrators that already conform to a declarative way are Dagster, Kestra, KubeFlow, and many more. But as with browsers, you can have different engines, different orchestration tools, or even self-written code and small lambda functions. Even all this is up to you as the data stack engine architect.


#### Security


Security would greatly benefit from a declarative data stack, as you can configure your access rights at a central place and read that configuration for each of the components of your data stack instead of implementing it again at each layer.


#### DataOps


DataOps, as part of the data engineering lifecycle, could be seen as the place to manage your data stack engine. If we look at what DataOps is, a combination of efficiency, velocity, usability, and automation, this is precisely what the declarative data stack is about.


## What About the Data Assets?


Before we wrap it up, let’s connect critical pieces at the interception where **stateful** and **stateless** meet: *Data Assets*, also called *Data Products* (e.g. in Data Mesh).


What are data assets? These are stateful assets that hold data. Assets can be a Parquet file on S3, a Delta/Postgres table, or a data mart on your OLAP cube.


This is the only part of the declarative data stack that cannot be configured or defined by a function, as upstream data is constantly changing and outside our control.


However, in an ideal data stack, we can always recreate data assets from source data if we perform a full/initial load every time. The moment we perform an incremental load, it gets more complex.


An interesting approach is the [Software-Defined Asset](https://www.ssp.sh/brain/software-defined-asset), which adds declarative capabilities to your stateful assets—for example, defining to daily update the assets. That would check if downstream events have changed or automatically versioning data assets. These are all things you can implement and attach to your data assets, which makes even the data asset behave more declarative.


You could imagine writing a *data stack engine* for all data assets that automatically backfills required data assets if the declaration of your data stack has changed. All while keeping the idempotency and functional data engineering paradigm in mind.


This significantly simplifies data governance, as rules could be embedded in the assets and even automatically censor sensitive data. There is no need to add security rules, as data gets censored automatically. I could make countless more examples, but you get the point.


### Durable State vs. Ephemeral State


We can further categorize the state into **durable** and **ephemeral**. The durable state, represented by our data assets, persists across system restarts and is crucial for maintaining long-term data integrity. On the other hand, the ephemeral state is temporary and often exists only during the execution of our declarative processes.


The challenge in a declarative system is managing the interaction between these state types. While our declarative configurations handle ephemeral states elegantly, the durable state (our data assets) requires special consideration. This is where concepts like Software-Defined Assets come into play, too, allowing us to apply declarative principles to durable state management.


### Low Code vs. Code First


An interesting parallel is that this is also where low/no-code vs. code first comes from. Once you have a declarative data stack, you essentially have your low-code or no-code platform, as you can build an API/UI on top of your configs, and every user could change the data stack, assuming that the features are implemented and exposed as configuration.


### Maslow’s Hierarchy of State in Declarative Data Stacks


Drawing inspiration from Maslow’s hierarchy of needs, we can conceptualize the hierarchies of state in declarative data systems in three levels, progressing from static to dynamic:

1. **Basic Declarative State**: The foundation consists of all declarations needed to recreate the data stack. This includes configurations, schemas, transformations, etc. It’s all *static*.
2. **Asset-added State**: Building on the basic state, we incorporate data assets. These can include source data, processed datasets, dashboards, reports, and other artifacts that represent the actual data and the *state* of the data stack.
3. **Self-Actualizing State**: The data stack becomes smarter and partially autonomous at the pinnacle. It can dynamically adapt to changes, such as automatically detecting new source data and generating appropriate declarative configs to integrate it into the entire stack. While the process remains deterministic based on the environment, it behaves *dynamically*.


As we move up this hierarchy, we increase the features and autonomy of our data stack, reducing manual intervention and increasing system “intelligence.”


Closed-source cloud data stacks usually achieve the self-actualizing state, as they have all the **metadata** and control the whole platform. But I believe this is also possible with an open declarative data stack. By centralizing the settings of the entire data stack in a single Git repository and ensuring end-to-end integration with comprehensive metadata, we can achieve similar levels of declarative deployment and setup. This approach allows for idempotent recreation of state across the entire data stack, mirroring the capabilities of closed-source platforms while maintaining openness and flexibility.


## The Declarative Data Stack Engine


Let’s see what that could look like and what the data stack engine **requires to implement**. If we think in functional terms, we need to define the whole data stack with a single function:



| `1
` | `run_stack(serve(transform(ingest)))
` |



In an ideal scenario, we could run the whole stack declaratively with this:



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
` | `run_stack(
    serve(
        template='github://covid/covid_dashboard.md',
        data=transform(
            {
                'groupby': 'country',
                'aggregate': {
                    'cases': 'sum',
                    'deaths': 'sum'
                }
            },
            ingest(
                source='duckdb',
                query='SELECT * FROM "s3://coviddata/covid_*.parquet"'
            )
        )
    )
)
` |



This example:

1. Ingests data from a Parquet file in S3 using DuckDB
2. Transforms the data by grouping it by country and summing cases and deaths
3. Serves the transformed data using a dashboard template from GitHub


The whole definition and functions a declarative data stack would need to implement could look something like this:



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
` | `def run_stack(serve_function):
    return serve_function()

def serve(template, data):
    # Logic to render the template with the provided data
    pass

def transform(transform_function, data):
    return transform_function(data)

def ingest(source, query):
    # Logic to execute the query on the specified source
    pass
` |



Note: I intentionally omitted detailed orchestration, as it could be the easiest way to implement such a data stack engine.

Side-Note about Validation
Each layer (ingestion, serving, transformation, etc.) should be able to validate itself, and the data stack engine would validate and stitch the missing pieces together. I could imagine having data contracts between the different interfaces, but that would be an implementation detail, and it is up to the engine how they want to implement it.

## What’s Next?


In Summary, we need three things to recreate a declarative data stack from scratch:

1. Exogenous/external data sources
2. Declarative artifacts
3. Rendering engine


Integrating everything into one git repo for all common configs (and metadata) will allow us to achieve things similar to those of closed-source data platforms.


This is part one of a series. Next, in [Part 2](https://www.ssp.sh/blog/bi-as-code-and-genbi/), we’ll explore the concept of “BI-as-code” and its effectiveness as an interface for GenBI (Generative Business Intelligence). We’ll begin with delving into why a declarative approach is a prerequisite for GenAI. We’ll also examine alternatives to the declarative data stack, providing a comprehensive view of the landscape. This part will highlight how the declarative paradigm is not just a trend but a fundamental shift in how we approach business intelligence in the age of AI.


Part 3 will take a practical turn as we attempt to build a declarative data stack example. Show how to implement this stack using AI, as declarative stacks allow a generative approach. The goal is to iterate and get one step closer to the open declarative data stack.


## Further Reading


### The Declarative Mindset in Data Stacks

1. Pedram Navid. “The Rise of the Data Platform Engineer.” Dagster Blog. *An in-depth look at the evolving role of data platform engineers in modern data architectures.* [Read the article](https://dagster.io/blog/rise-of-the-data-platform-engineer)
2. Benoit Pimpaud. “ELT with Kestra, DuckDB, dbt, Neon and Resend.” Medium. *A practical guide to implementing an ELT pipeline using various modern data tools.* [Read the article](https://medium.pimpaudben.fr/elt-with-kestra-duckdb-dbt-neon-and-resend-5bfd62160190)
3. Archie Wood. “An end-to-end data stack with just DuckDB: ETL is dead, long live ETV.” LinkedIn. *Explores the concept of Extract-Transform-Visualize (ETV) using DuckDB as the primary tool.* [Read the post](https://www.linkedin.com/posts/archiesarrewood_an-end-to-end-data-stack-with-just-duckdb-activity-7245362448545808385-ioK3)


### Code Reusability in Data Transformation

1. Maxime Beauchemin. “Why Data Teams Keep Reinventing the Wheel: The Struggle for Code Reuse in the Data Transformation Layer.” Preset. *Discusses the challenges and importance of code reusability in data transformation, introducing the concept of Parametric Data Pipelines.* [Read the article](https://preset.io/blog/why-data-teams-keep-reinventing-the-wheel/)


---


```
Full article published at Rilldata.com - written as part of my services
```


---

1. Markdown plaintext files, Obsidian, and GitHub Discussions were the most loved async tools for developers in 2024 according to [StackOverflow Survey](https://survey.stackoverflow.co/2024/technology#2-asynchronous-tools). ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/rise-of-declarative-data-stack/)
|
[Declarative](https://www.ssp.sh/tags/declarative/)
[Declarative Data Stack](https://www.ssp.sh/tags/declarative-data-stack/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Modern Data Stack](https://www.ssp.sh/tags/modern-data-stack/)
[Rill](https://www.ssp.sh/tags/rill/)
[Services](https://www.ssp.sh/tags/services/)
