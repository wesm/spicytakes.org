---
title: "Configure, Don't Code: How Declarative Data Stacks Enable Enterprise Scale"
date: 2025-05-20
url: https://www.ssp.sh/blog/declarative-data-stack-enterprise/
slug: declarative-data-stack-enterprise
word_count: 2869
---

![Configure, Don't Code: How Declarative Data Stacks Enable Enterprise Scale](https://www.ssp.sh/blog/declarative-data-stack-enterprise/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Imagine building enterprise data infrastructure where you write 90% less code but deliver twice the value. This is the promise of declarative data stacks.


The open and modern data stack freed us from vendor lock-in, allowing teams to select best-of-breed tools for ingestion, ETL, and orchestration. But this freedom comes at a cost: fragmented governance, security gaps, and potential technical debt when stacking disconnected tools across your organization.


On the flip side, closed-source platforms offer unified experiences but trap you in their ecosystems where you can’t access the code or extend beyond their feature sets in case of need.


**What if we could have the best of both worlds?**


Enter declarative data stacks – open-source solutions that seamlessly integrate powerful orchestration tools like Airflow and Dagster while covering your entire data lifecycle. These are complete data platforms with “batteries included” where configuration replaces coding, dramatically reducing complexity while implementing best practices by default.


In this article, we’ll explore how declarative data stacks manage enterprise data complexity. You’ll discover how Starlake, an open-source declarative data stack, enables data transformations through simple configurations, helping teams deliver production-ready platforms in days instead of months while automatically maintaining governance and lineage.


At its core, Starlake serves as your **data warehouse orchestrator** – a unified control center that manages your entire data ecosystem through a single, coherent lineage. Not just a tool, but an **end-to-end OSS data platform** that makes “configure, don’t code” a practical reality for enterprise teams.


## What Is a Declarative Data Stack?


A declarative data stack is essentially an end-to-end data engineering tool that is made for complexity. It has all the features you need included. It extracts, loads, transforms, and orchestrates. The mantra: Code less, deliver more.


What’s the catch? You need to align with a common configuration style. You need a framework, a tool, something that abstracts and does the hard work, so that we, the users, can simply configure and run it. This is where **YAML** comes in. Some also call it the [YAML Engineer](https://juhache.substack.com/p/from-data-engineer-to-yaml-engineer-ed2).


In this Part 1, we will go through the benefits and anatomy of declarative data stacks, and see how [Starlake](https://starlake.ai/) can help us with that. In [Part 2](https://www.ssp.sh/blog/beyond-basic-etl) we’ll have a look at an end-to-end data engineering project that does ingestion from any configurable source, using SQL transformation and orchestrating it with Airflow, Dagster, or even [Snowflake Tasks](https://docs.snowflake.com/en/user-guide/tasks-intro) (you choose!), showing a declarative data stack in action.


And then finally, we’ll choose a BI dashboard to visualize the data (not part of Starlake).


### The Evolution Toward Declarative Data Engineering


If we look back at where we come from, we can see that 20 years back, everyone just picked a vendor like SAP, Oracle, or Microsoft, and ran with their database or business intelligence solutions. You had lots of options, but if you needed anything specific, you had to request that feature and hope someone implemented it. You were captured in a **monolithic** system.


Because these were widely spread, you had a good chance that what you wanted was already there. But there was always this one customer that wanted that one extra thing. That’s why a little later, the **boom with open-source** happened. All of a sudden, plenty of US startups were sharing their tools like Hadoop and its whole ecosystem. Everyone got used to sharing their code and became excited about solving tough problems together.


This also took over the data space and became one of the starting points for data engineering when Maxime Beauchemin started sharing his trilogy about functional data engineering. More and more tools got open-sourced and this is where we landed a while back with the explosion of tools and the [Modern Data Stack](https://www.moderndatastack.xyz/), or [Open Data Stack](https://www.ssp.sh/brain/open-data-stack/), a **modular** system. Usually the deployment and DevOps involved are quite a massive effort; think [Terraform](https://developer.hashicorp.com/terraform), [Helm Charts](https://helm.sh/), or [Kustomize](https://kustomize.io/) and how these democratized declarative engineering over the last decades.


Today we are entering the next phase of the cycle. We are back to one platform ruling them all, or better, bringing together the strengths from both of these worlds: having one platform integrated with open-source tools. But how do we achieve this? Exactly, you guessed it right, with declarative data stacks.


### What Makes a Data Stack Declarative?


This transition from a monolithic to a modular system, back to a monolithic platform but with OSS plug-and-play tools to choose from with integrated templates, is a great evolution learning from the past. And declarative data stacks are the key to that.


But maybe you haven’t heard of that term, or are unsure what it means. I have written about it at length in [The Rise of the Declarative Data Stack](https://www.rilldata.com/blog/the-rise-of-the-declarative-data-stack), but here is the short version of it:


> A declarative data stack is a set of tools and, precisely, its configs can be thought of as a **single function** such as *run_stack(serve(transform(ingest)))* that can recreate the entire data stack.
> Instead of having one framework for one piece, we want a combination of multiple tools combined into a single declarative data stack. Like theModern Data Stack, but integrated the way Kubernetes integrates all infrastructure into a **single deployment**, like YAML.
> We focus on the end-to-end data engineering lifecycle, from ingestion to visualization. But what does the combination with declarative mean? Think of [functional data engineering](https://ssp.sh/brain/functional-data-engineering), which leaves us in a place of **confident reproducibility** with little side effects (hopefully none) and uses idempotency to restart functions to recover and reinstate a particular state with conviction or rollback to a specific version.


At its core, we can define the full data stack with a single configuration file (or files). And instead of defining the *how*, we can configure *what* we want to achieve. Essentially **code less and deliver more** with the benefit of a more reproducible and maintainable data stack.


### Breaking Free from Black Boxes


Declarative data stacks also **break free from black boxes** of different OSS tools that you have a hard time integrating. Instead, you get a **data-aware** data platform that integrates through [parametric configuration](https://preset.io/blog/why-data-teams-keep-reinventing-the-wheel/) into the end-to-end data pipeline.


Unlike Airflow, where each task has no idea what is happening inside of it, it’s a black box. As more complex data platforms become the norm, knowing if a task has finished or not is not enough. With a declarative approach, you focus more on the *what*, the data assets. This means we define them, their logic, dependencies, down to their column-level lineage and types. This opens up the black box for us in an easy and approachable way, mainly in YAML.


The YAML configuration approach makes the internal workings more explicit and accessible, rather than hiding them, making the configuration and produced assets transparent and accessible to us and our users.


The YAML configs also make it approachable to non-programmers, as YAML is the universal configuration language. YAML is also easy to integrate with LLMs, more so as it’s a superset of JSON and easily integrates with [JSON Schema](https://json-schema-everywhere.github.io/yaml). This means each YAML can be converted to JSON and integrated with the powerful data serialization language of JSON Schema. This leads to a (longer) context window where AI and humans can iterate on and integrate into any code editor or architecture. Ultimately, it helps to make English engineering a reality.


## Don’t Code, Declare.


This is the main mantra behind declarative data stacks: don’t code, but declare and get a fully-fledged data platform.


### The Anatomy of an Open Declarative Data Stack


But what does that data platform include, and what’s the anatomy of such a data stack? A declarative data stack does not only support one part of the data engineering lifecycle but the entire process end-to-end.


We go from extracting data to orchestrating them all in one platform:

- **Extract**: Configuration-driven data ingestion
- **Load**: Zero-code data loading with built-in validations
- **Transform**: SQL-based transformations with automatic optimizations
- **Orchestrate**: Integration with existing workflow managers
- **Visualization**: Present and visualize created data assets
- **Lineage**: Visibility across the entire stack


If you will, these are the core bones and skeleton of a declarative data stack. There are now many ways one could implement this. In the following chapters, we’ll analyze how Starlake implemented these components, and how it can help us support complex data landscapes.


## Starlake: An Open Source Declarative Data Platform


[Starlake](https://starlake.ai) gets you all the discussed benefits of a declarative data stack in one single platform, configurable by YAML. It offers a powerful [open-source solution](https://github.com/starlake-ai/starlake) to embrace declarative data engineering end-to-end.


![/blog/declarative-data-stack-enterprise/starlake-overview.png](https://www.ssp.sh/blog/declarative-data-stack-enterprise/starlake-overview.png)

*Starlake Overview*


In a nutshell, Starlake is a comprehensive declarative data platform that:

- Is based in France, is entirely open-source, and had its first [commit](https://github.com/starlake-ai/starlake/commit/e55c4ba34e988702bdc150225a8b88aed9bedc6a) on `May 21 2018`, but was created 20 years ago by [Hayssam Saleh](https://github.com/hayssams) ([LinkedIn](https://www.linkedin.com/in/hayssams/))
- Runs on JVM (built with Scala) for cross-platform compatibility, bringing type safety and performance
- Uses a YAML-based configuration approach (similar to how Terraform works for infrastructure)
- Covers the entire data lifecycle: extract, load, transform, test, and orchestrate
- Supports multiple data warehouse engines (Snowflake, BigQuery, Databricks, etc.)
- Integrates with popular orchestrators like Airflow, Dagster, Snowflake Tasks, and Databricks scheduler (coming soon)
- Eliminates complex coding with a “declare, don’t code” philosophy
- Features built-in data governance, validation, and lineage tracking
- Enables development in-memory and local DuckDB, as well as deployment to any supported platform
- Supports [multi-engine and cross-engine capabilities](https://docs.starlake.ai/#multi-engine--cross-engine) (query one warehouse, write to another)


It has automated data quality checks and validation, native integration with major data warehouses, and no-code and low-code paradigms support. It also comes with enterprise-grade security and governance out of the box and supports both batch and real-time processing.


[Starlake](https://docs.starlake.ai/) bridges the gap between open-source flexibility and enterprise-ready data platforms, allowing organizations to build **robust data pipelines** with minimal code while maintaining complete visibility and control. It builds and orchestrates data warehouses with the complexity of data in mind from the get-go.


### Why Starlake for Enterprises?


But why would you use Starlake at a large enterprise? What are the **immediate benefits**? In condensed form, you could say it helps address these **three main problems** that we face in the field of data engineering:

- Overwhelming complexity in managing data pipelines
- Inefficiencies in transforming and orchestrating data workflows
- Lack of robust governance and data quality assurance


Starlake simplifies the data management effort with configuration-driven ingestion, transformation, and orchestration, and reduces manual implementation of each data pipeline.


This enhances data quality and the **overall reliability** of the platform with enforced governance, schema validation, rules, and SLAs across the system. It **accelerates time to insights** and opens up opportunities to create additional data pipelines with less technical people through the UI and configuration interface.


If we compare it to traditional ETL tools, the table below will help us understand the differences:



| Feature | Starlake.ai | Traditional ETL Tools | Benefits |
| **Core Architecture** | Declarative (YAML-based) | Imperative (code-heavy) | Reduced maintenance burden, improved readability |
| **No-Code Ingestion** | â | â (requires custom coding) | Faster implementation, accessible to non-programmers |
| **Declarative Transformations** | â | â | Simplified maintenance, consistent patterns |
| **Automated Orchestration** | â (integrates with Airflow/Dagster) | â (requires manual setup) | Reduced setup time, automated dependency management |
| **Built-in Governance** | â | â | Enforced data quality and consistency |
| **Cross-Engine Capabilities** | â | â | Flexibility to work across different platforms |
| **Multi-Engine Support** | â | â | Prevents vendor lock-in |
| **Automated Schema Evolution** | â | â | Adapts to changing data structures automatically |
| **SQL Transpilation** | â | â | Write once, deploy anywhere capability |
| **Local Development** | â (with DuckDB) | â | Faster development cycles, reduced cloud costs |
| **Data Quality Validation** | â (built-in) | â ï¸ (limited/add-on) | Higher data reliability |
| **End-to-End Lineage** | â (column-level) | â ï¸ (typically table-level) | Enhanced visibility and troubleshooting |
| **Row/Column Level Security** | â | â ï¸ (often requires add-ons) | Better compliance capabilities |
| **Gen AI Readiness** | â (via JSON Schema) | â | Future-proof architecture |
| **Learning Curve** | Moderate (YAML) | High (multiple languages/tools) | Faster team onboarding |
| **Implementation Time** | Fast | Slow | Quicker time to insights |
| **Maintenance Burden** | Low | High | Reduced technical debt |



In the end, it manages complexity and the return on investment in the platform grows with rising complexity. The reason is the declarative nature and the encapsulation of complexity into the platform (Starlake), allowing the data engineer and user of the platform to focus on the business requirements and analytics.


Contrast that with manually writing [imperative](https://www.ssp.sh/brain/imperative) Python scripts to schedule your data pipeline or managing your infrastructure by manually installing multiple tools and making them work altogether. This is the main challenge the current landscape faces, and the **hidden cost of imperative data work**.


That’s why integrated systems are on the rise and where configuration-driven stacks bridge the gap to become easier to maintain and more reliable.


### When Is Starlake the Wrong Option?


If you have a simple POC, or you know for a fact that the platform will never get wider use or grow bigger, or the requirements are in constant change, then it’s easier to custom-make an imperative solution. Though you can still use Starlake to quickly start up with all batteries included, it’s still a better fit to abstract a big complex data landscape into a manageable data platform, with an integrated governed solution.


If your focus is on visualization, Starlake comes with no presentation tool, though it can be easy to hook up one to the generated data assets. Best would be to stay in the code-first and declarative approach with BI solutions such as [Rill](https://www.rilldata.com/), [Evidence](https://evidence.dev/), or [Lightdash](https://www.lightdash.com/).


Starlake is especially strong with large enterprises, which shows with the current customer base, mostly large enterprises with high volumes (100 GB/day and 100 TB in BigQuery), multi-cloud such as Google Cloud and reports on Azure, or on the other spectrum, streaming-like requirements with new small files every minute, ingested into Redshift and visualized in Superset.


### Multiple Verticals into Data Engineering


Starlake spans across **multiple verticals** within the data landscape and isn’t limited to one aspect of data engineering. Just as YAML has become the universal configuration language for various domains, declarative data stacks integrate several critical verticals of the data engineering ecosystem under a unified configuration approach.

- **Orchestration**: Rather than writing complex DAG code, workflows are defined in YAML and automatically translated to Airflow or Dagster execution plans. This abstracts away the complexity of pipeline scheduling and dependency management.
- **Transformation**: SQL is already declarative by nature, but Starlake enhances it with automated optimizations and transpilation across different warehouse dialects—write once, run anywhere.
- **Infrastructure**: Similar to how Terraform revolutionized infrastructure management, Starlake applies declarative principles to data infrastructure, enabling version-controlled data assets.
- **API Integration**: Much like OpenAPI Specification uses YAML to define REST APIs, Starlake allows declarative configuration of data sources and destinations.
- **Governance**: Data quality rules, schema validation, and access controls are all defined declaratively rather than scattered across multiple codebases.


## When to Choose a Declarative Approach


That’s it, that’s why you shouldn’t code but configure if you want to optimize for a large enterprise. This article is part one of three. Before we check Starlake in action in [Part 2](https://www.ssp.sh/blog/beyond-basic-etl) and analyze what’s possible today with declarative data stacks as well as the future of it, including how to integrate well with the latest GenAI and GenBI capabilities, let’s wrap up this article.


We have learned that declarative data stacks represent a paradigm shift in enterprise data engineering - “Declare your intent, don’t code it.” By embracing configuration over custom coding, organizations gain reproducibility, maintainability, and governance without sacrificing flexibility. With tools like Starlake, you can develop and test locally on DuckDB using your target warehouse’s SQL dialect, reducing costs and enabling faster development cycles while ensuring consistent quality through automated testing.


Breaking free from black boxes doesn’t mean abandoning the open data stack, but rather integrating best-in-class tools under a unified, configuration-driven approach. The result is a data platform that scales with your complexity, reduces technical debt, and democratizes data engineering by making it accessible to YAML engineers alongside traditional coders. As data landscapes grow increasingly complex, the declarative approach offers a sustainable path forward that balances enterprise requirements with development agility.


I believe the future of data engineering will change significantly, but with a declarative data stack, we are ready for whatever changes come with an adaptable configuration-first system that nicely abstracts implementation logic from business requirements. This allows the future of data pipeline development to be adaptable, governed, and ready to evolve with organizational needs.


---


```
Full article published at Starlake.ai - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/declarative-data-stack-enterprise/)
|
[Declarative Data Stack](https://www.ssp.sh/tags/declarative-data-stack/)
[Starlake](https://www.ssp.sh/tags/starlake/)
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Open Data Stack](https://www.ssp.sh/tags/open-data-stack/)
[Modern Data Stack](https://www.ssp.sh/tags/modern-data-stack/)
[Services](https://www.ssp.sh/tags/services/)
[Yaml](https://www.ssp.sh/tags/yaml/)
