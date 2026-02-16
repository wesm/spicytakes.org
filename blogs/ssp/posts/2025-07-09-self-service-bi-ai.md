---
title: "Has Self-Serve BI Finally Arrived Thanks to AI?"
date: 2025-07-09
url: https://www.ssp.sh/blog/self-service-bi-ai/
slug: self-service-bi-ai
word_count: 3919
---

![Has Self-Serve BI Finally Arrived Thanks to AI?](https://www.ssp.sh/blog/self-service-bi-ai/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Two decades ago, we talked about self-serve business intelligence when we could filter dashboards compared to pixel-perfect reports. Today, twenty years later, does conversational BI through MCP and semantic context finally deliver on the true promise of self-serve by allowing us to prompt our way through data analysis?


With the right setup, **conversations can generate BI artifacts**. When we chat with a large language model about data, the output is typically narrowâa single number, a specific interpretation tied to one problem. But what if we could transform these focused conversations into comprehensive insights that executives can act on? What if narrow analysis could expand into full organizational views, complete with interactive filters and explorable dimensions?


In Part 1, [BI-as-Code, and the New Era of GenBI](https://www.ssp.sh/blog/bi-as-code-and-genbi), we explored iterating through BI dashboards and models with generative AI. This Part 2 dives deeper into how conversational BI transforms the human workflow and finally solves the self-serve promise that’s persisted for decades. We’ll examine the different conversational styles emerging in BI, the three distinct output types that matter most, and why Model Context Protocol (MCP) represents such a fundamental shift.


The goal is to showcase the convergence of AI and BI, which enables more quantitative insights than traditional BI ever could.


## GenBI, What Is It? A Recap


At its core, GenBI delivers an **effective human interface** that iterates quickly, mostly based on BI-as-Code. In [BI-as-Code and the New Era of GenBI](https://www.ssp.sh/blog/bi-as-code-and-genbi), we illustrated how an iterative and refined process with generative tools can improve the overall workflow compared to a more manual process.


As a recap, GenBI shifts how we create and interact with business intelligence by leveraging AI large language models. These understand the business context through BI artifacts. Unlike traditional BI tools that hide business logic in proprietary UI configurations, GenBI defines dashboards and metrics as code, such as YAML or SQL. This provides AI models with the semantic context to understand how metrics are calculated, how dimensions relate, and what domain knowledge drives the business.


The result is an interface where non-technical business people can describe their analytical needs in plain language and receive instant dashboards in seconds rather than hours.


### Why Generative BI, why Conversational BI?


Despite the hype around artificial intelligence, I believe business intelligence interfaces are the best place for using LLMs.


Within BI, we have domain knowledge from the organization, the field, and the business. It’s the **convergence between the business and technical** stack, empowering business and domain experts to do more themselves and [shift more left](https://www.rilldata.com/blog/what-shifting-left-means-and-why-it-matters-for-data-stacks) while **verifying the numbers** during creation.


Domain experts know the business and numbers best, so they are also the best ones to check the numbers and iteratively create BI artifacts such as dashboards and visuals. It’s a continuous, iterative **human-AI collaboration**, where BI-as-Code is the enabler for collaboration via YAML or SQL definitions.


With the latest Model Context Protocol (MCP) added to the mix, LLMs get direct access to the underlying database. This makes LLMs more autonomous and accurate, as they can verify the actual facts and numbers by querying the database.


Generative BI ultimately enables a better BI workflow. It changes the way people interact with data by combining the power of natural language and analytics, enabling **conversational BI**.


### Where We Are Coming From: Self-Serve BI


Let’s look back a couple of years, for example, in 2003, when I started my career in data. We were delivering pixel-perfect reporting, and a little later switched to dashboards with the tool stack of Oracle and Microsoft. We called it revolutionary and talked about **self-serve BI** as users could self-serve their analytics needs by filtering regions, dates, and other dimensions. Later, with Tableau, QlikView, and other drag-and-drop tools, we could build and collaborate on more sophisticated dashboards and integrate SQL transformations.


There were many more cloud BI tools and the age of the Modern Data Stack. However, the bigger shift was in 2019 with dbt, where BI users not only created dashboards but could **write aggregations and transformations** within the SQL templates of dbt. Depending on the setup, even non-technical business users could commit SQL changes to a repo, and with a simple pipeline, this would be deployed directly and potentially executed.


But today, with AI-powered large language models, the workflow can be improved much more. In fact, **self-serve might just be possible** for the first time.


## Why is MCP and Conversational BI so Powerful


So, what is Model Context Protocol (MCP) anyway? Why is it so powerful?


The MCP is a client-server architectureÂ [inspired by the Language Server Protocol (LSP)](https://spec.modelcontextprotocol.io/specification/2024-11-05/), which helps connect any IDE with different programming languages. Instead of VSCode needing to integrate Python language servers and PyCharm, we have one implementation and an LSP for Python that can get integrated by any IDE in a standardized way.


You can consider it aÂ **common definition**, like an API interface,Â that standardizes the interfaces to integrate LLMs. Another example is [LSP (Language Server Protocol)](https://en.wikipedia.org/wiki/Language_Server_Protocol), which did the same for language integration into editors with a protocol between the AI model and the client.  MCP is the same for **plug-and-play** any AI model to any IDE, whether Claude, Cursor, VS Code, Neovim, we can interact with AI with external systems in a standardized way through the [MCP standard](https://github.com/modelcontextprotocol).


*Example of Rill’s MCP Integration with Claude*


This integration allows large language models (LLMs) to query, inspect, and interact with various tools like databases, code repositories, and APIs, usually guided by your prompts or through AI Agents.


It was originally introduced byÂ AnthropicÂ in 2024, and made [open-source on GitHub](https://github.com/modelcontextprotocol). MCP quickly gained traction among AI-first developer tools and is now the way to integrate any AI model.


I won’t go into the details of how it works and what it is; there’s a lot of content out there. Instead, I will explain why it’s powerful for the data ecosystem and BI specifically.


### Conversational BI with MCP Showcase


To best explain it, here’s a short example of how a [Rill’s MCP](https://docs.rilldata.com/explore/mcp) integration with Claude Desktop works.


In this example, we use the MCP integration as a new interface compared to a dashboard, where we can ask questions instead of clicking our way through it. The magic is that it’s connected to the Rill API and its underlying database, which means it can autonomously figure out your request with actual queries against its database and existing metrics.


In the example below, I connected Rill locally to my NYC taxi ride dataset, joined with pickup locations, and prompted:


> Using MCP Rill, can you give me `avg tip` per ride in NYC with pickup zone JFK Airport?


Here’s how the whole interaction looks, including:

1. Listing existing metrics views
2. Getting metrics of listed metrics views
3. It found existing measures: `average_tips_measure` and `pickup_zone`
4. It checks the time range available
5. It automatically filters on JFK pickup with `JFK Airport`
6. It returns the answer of **$3.72** as the average tip per ride, with the additional context of total trips and the date period of the dataset


The fantastic part of this is that not only does it do everything autonomously, but we can also follow each step along the way, including the queries it fired against the Rill API and underlying database. It’s truly self-serve, based on a single prompt.


Not only did we get the answer, but it also **provides additional context** that helps us understand the numbers better, which is extremely helpful when we are not familiar with this dataset.


On the contrary, we don’t know if the answer is actually correct. To quickly verify, I created a dashboard that showed that the answer is correct:


![/blog/self-service-bi-ai/verify-numbers.png](https://www.ssp.sh/blog/self-service-bi-ai/verify-numbers.png)

*Verifying numbers by checking the Rill dashboard and filtering on JFK Airport*


But does this mean we need to create visuals for each prompt to verify our result?


This is where it gets a bit harder to explain. In general, as the MCP has access to the underlying data, it should not hallucinate as much since it has access to the actual data. Plus, if we ask about a very narrow data issue, it is much more likely to have all the context to figure it out correctly. But we will never know 100%.


But if dashboards are created with domain experts involved, they’re less likely to contain elements that don’t make sense. Maybe that business expert can even query 2-3 statements to check if the data is correct, or usually, that person has a sharp understanding of what the number should be.


Also, we can say, instead of querying the data manually, where errors can occur, MCP can quickly query OLAP cubes and verify that his assumptions were correct, or quickly query a data model or source data, even if allowed, **reducing the likelihood of errors**. Humans make errors, too, so if we **combine the human and AI** with MCP, this is a big win for BI and the enhanced workflow provided.


But we get ahead of ourselves, we will dig into that problem a bit more later.

Find Source Code and Example on GitHub
The dataset queried with NYC Taxi Trip Data and NYC Taxi Zones can be found on GitHub
[sspaeti/rill-nyc-taxi](https://github.com/sspaeti/rill-nyc-taxi)
. Also, see the data sources links (hosted or for local download) in the README.

## Supporting Conversation Interactions: Input and Output Definitions


Let’s look a little deeper at what conversational BI means and what the input and output of such a conversation are. Why do we connect AI with BI, and what does it offer? Why don’t we just use **text-to-SQL**?


As alluded to in earlier chapters, BI offers rich semantic metadata that is simple for AI to understand. Metrics are defined as metrics like `average_tips_measure = AVG(tips)` that hold information unavailable in pure table schemas. Also, it’s much more precise than human language, so there are fewer misunderstandings.


BI usually has direct access to the data layer; in the best case, it is a fast analytical database that responds in sub-seconds to queries. Many **data warehouses or data lakes arenât fast enough to support conversation-speed interrogations**.


A lot of conversational BI and generative AI is “**retrieval and rendering**”. In the next two chapters, we will have a closer look at what that means in terms of conversational style, the inputs and outputs of such systems, and how to render it to benefit the BI user.


### Input Conversational-Style


In conversational style AI interaction, we have different conversational inputs. Each of them has a slightly different purpose. Today, we can identify three main paths and styles:

1. **Notebook-style conversation** with embedded images generated through MCP
2. **Text-only conversation** with external links to BI visualizations
3. Conversation that optionally can **generate a [Canvas Dashboard](https://www.rilldata.com/blog/introducing-canvas-dashboards-a-new-way-to-visualize-metrics)** summarizing key insights


The most interesting path is number three. Generating not only text as chat, a *[canvas dashboard](https://docs.rilldata.com/build/canvas/)* has the advantage of using the visualization as an output to share with executives, as opposed to a chat conversation. We can even add a high-level summary of the conversation we had in the conversation to generate this dashboard.


By adding the visual, the user can then explore other areas, dates, and dimensions of interest, as opposed to the narrow analysis of the specific chat conversation (e.g., only JFK Airport).


### Three Distinct Output Types


As hinted in the diagram, more interesting and valuable than the input style is the output it produces.


Conversational BI involves prompt inputs that provide **three forms of output** in combination with MCP integration. Let’s compare the different outputs:



| Output Type | Purpose | Key Characteristics | Examples |
| **Retrieval - Numerical Data** 
(metrics via MCP) | **Objective**: Provide factual data that cannot be hallucinated | â¢ Must come from MCP-generated queries
â¢ Act like vector stores for AI
â¢ Must be fast for real-time interaction
â¢ RAG-like retrieval for metrics | “Revenue for last 7 days”
Raw conversion rates
Sales figures |
| **Generation - Text** 
(interpretations via data + world model) | **Subjective**: AI-powered insights and analysis | â¢ Where AI brings its power
â¢ Combines retrieved data with world knowledge
â¢ Interprets numerical data with context
â¢ Can be included in AI-generated reports | “What is campaign performance?"
“Conversion rate below 1% is low compared to benchmarks”
Strategic recommendations |
| **Generation - Visuals** 
(charts and tables as BI-as-code) | **Visual**: Human interpretation and exploration | â¢ Only for human consumption
â¢ LLMs/MCP should not use directly
â¢ Serve as “leaping off” point for exploration
â¢ Convert narrow analysis to broad views | Time-series profit trends
Top-selling products table
Airport performance dashboards |



Key insights are that numerical facts and visuals provide **validation and verification** of textual interpretations.


And **visuals can manifest textual interpretations**, converting chat analysis from one dimension (one airport, one day) - very narrow analysis - to a more comprehensive view (all airports, every day).


With the three output methods, we can also understand where the improved “workflow” comes from; **combining facts with context and interpretations**.


### Narrow Context, Better Results: Making AI More Deterministic


From the input conversation style and the output types, we learn that AI is actually not suited for a large context of what typical BI high-level dashboards represent. But generative AI is super powerful at analyzing a specific day, with very specific filters and fewer data points to give us valuable context and assessment. For example, inspecting an unknown spike or anything that looks suspicious in a dataset.


By going narrower, like analyzing a spike in a dashboard, it’s much less likely to hallucinate and makes its prediction more **deterministic** (even more so with MCP, as it can autonomously query the data).


The **non-deterministic characteristics** are influenced by the questions we humans ask. If we use the wrong word or ask a question that is a little unclear, the outcome might vary a lot. But if we can be as specific as one data point on the dashboard and provide the model with **factual data retrieval** and numbers from that day and situation, it’s much less likely to be wrong.


Essentially, you get the best of both worlds: benefits of relational databases (with retrieval, schema, integrity, etc.) and facts, while BI tools add a more **human-friendly interface** on top of it for interpreting.


The visuals, on the other hand, provide verification and validation for us humans. We can check if the model output as text is correct. It’s also much more “**self-serve**”, as we humans can interactively drill by region, product, and any dimension offered by the BI tools, compared to a chat interface where we’d need many hours to ask and iterate through each region, each year. In contrast, a visual dashboard can answer these comparisons within seconds, displayed on one screen if you want to.


Conversational BI is self-serve, too, but it is **slower and more imprecise in a grand context**, though super helpful in a narrow context.


### Persistent Artifacts of Conversational BI


The value of conversational BI comes from what can be persistent and built on top of; we are talking of our three output types, such as **numerical data**, **text insights**, and **visual charts**.


![/blog/self-service-bi-ai/conversational_bi_flow.webp](https://www.ssp.sh/blog/self-service-bi-ai/conversational_bi_flow.webp)

*Conversational BI Architecture Flow*


Wouldn’t it be nice if we could combine the different output types as an artifact in our BI tool? With Rill, we could imagine integrating these into a single **[Canvas Dashboard](https://docs.rilldata.com/build/canvas/)** where we summarize the conversational insight (text) as part of a Markdown text box, adding relevant visuals to back the numerical fact including BI default filtering on dimension, instant exploration capabilities and even a pivot presentation layer to dig into more details.


This gives us all three output types concluded into persistent BI artifacts that can be shared with executives and users of the BI portal to learn the new insights gained.


![/blog/self-service-bi-ai/genbi_rill_mock.png](https://www.ssp.sh/blog/self-service-bi-ai/genbi_rill_mock.png)

*Canvas Dashboard with the extracted summary of natural language conversation on the right (Mockup of potential upcoming feature) alongside the numerical BI facts (measures)*

Everything is a 'Metrics View'
In the end, every output is a
**metrics view**
. What does this mean? When we look at any persistent output, it’s always an aggregation with a combination of measures (e.g., tip money) and dimensions (e.g., pickup location).

## Workflow: Human in the Loop


AI workflows have transformed business intelligence **from creation to consumption**, especially in how we consume.


With all of these leaps and excitement that conversational BI is bringing and improving our BI workflow, we must state that at the heart of this workflow are we, the human. As most LLMs as of now are just probabilities, they could at any point take the wrong turn and go down a path that makes no sense.


Also, without a human steering the model, we might just get average insights that are common among the datasets (where LLMs are trained). Still, with a domain expert who knows the data well, that person can ask specific and important prompts regarding the available data, making the conversational BI and all the work put into it much more insightful.


It’s a human-AI collaboration. I believe we are just at the start of integrating natural language into BI, but the **output quality** is critical to how much humans drive the generation.


### Critical Components for Conversational BI


BI is *the* Interface for Business. As humans, it is crucial to steer and adjust that interface with human oversight.


Humans provide irreplaceable experiential knowledge that AI can’t access from training data. As AI handles faster iterative BI collaborations, human judgment/context becomes the differentiator. But how can we do this?


Critical components to make conversational BI key are **semantics**, **speed**, and **BI-as-code**. The first one is quality data; without that, no insights. But as this is obvious, I will ignore that for now and focus on three more:

- **Semantic Understanding -> Metrics**: Necessary to define the world of BI more precisely than the English language.
- **Speed -> Real-Time databases and OLAP cubes**: No one would use them without swift reactions and dataset responses.
- **BI-as-Code -> declarative way**: Having dashboards, models, and BI artifacts as YAML or SQL. This is the human-AI interface where humans and AI can collaborate. Without that, AI would only have context windows of the active session. But with a declarative file, we can iterate on it.


Why do these examples matter? Speed is key as we can’t wait one minute to get a simple query back. That’s where **[real-time databases](https://www.rilldata.com/blog/scaling-beyond-postgres-how-to-choose-a-real-time-analytical-database)** and OLAP systems like DuckDB, MotherDuck, ClickHouse, and Starrocks shine.


A declarative and code-first approach, combined with descriptive metrics, works best for conversational BI because **generative BI needs context** to understand your business.

Related: The Language of AI

LLMs and AI-powered workflows work well with **declarative interfaces** that provide rich business context. Think of it as establishing a **common language** between humans and AI.


The declarative foundation typically combines:

- **YAML** - for configuration, dashboards, and BI artifacts
- **SQL** - for metrics definitions and business logic


This approach works because SQL is the universal language and more precise than the English language, removing ambiguity. Unlike traditional BI tools that hide logic in proprietary configurations, declarative definitions give AI models the semantic context they need to understand how metrics relate, how dimensions connect, and what drives business decisions.


### Considerations and Limitations


With the LLMs and conversational BI, we also come across some limitations and considerations we need to know.


> We don't need more dashboards, we already have 100 or more dbt models in the landscape


It’s true that the advancement of faster generation of insights and dashboards might lead to more unused dashboards. But on the other hand, MCP can also be used to extend existing dashboards with additional measures. So, as always, it’s also a question of data governance.


> What about if AI generates an error?


This is something we need to keep a close eye on. But if domain experts are iterating through it, they know the data, and during the time of creation, it is the best time to verify. And there are no better people than business people who use BI dashboards. Plus, aren’t humans also very prone to making errors (sometimes)? ð


Implementing **Guardrails** is another method of limiting this factor. As Mike Driscoll says, he would like to allow Rill MCP only to generate code that can be based on the metric view of Rill. This means it can’t hallucinate a measure that does not exist. This means dashboards are based on numerical facts (data sources), which would make them more efficient.


> How do you check if the numbers are correct?


As explained above, a combination of visuals (based on facts) with an interpreted context of an LLM is based on existing metrics, and the hallucination can be kept much lower. Even more deterministic, if the domain and analysis are kept narrow, we let the AI interpret a specific date or occurrence to make it understand more easily.


## Conclusion: Conversations Can Generate Code


The key insight from our exploration of conversational BI is fundamental: **conversations can generate code**, and code generates insights.


This represents a shift in how we approach business intelligence, enabling faster iterations and bridging the persistent gap between technical and business people within BI, away from traditional click interfaces.


**Improving the BI Workflow with GenBI**:

At the heart of this transformation is BI, which serves as the core **driver of domain knowledge**. Our analysis reveals three distinct output types that define generative BI: numerical data, text insights, and visual charts. These outputs serve different purposes in the BI ecosystem, distinguishing between generating effective BI artifacts and creating new presentation layers through conversational interfaces.


We must recognize two primary modes of generation: generating or altering code to create **BI artifacts**, and interpreting data to answer questions as a **presentation layer**. This distinction clarifies how conversational BI operates across different use cases.


**The Semantic Understanding Advantage**:

What makes this approach powerful is the additional **context** that LLMs and MCP provide, helping humans iterate much faster and more efficiently. The semantic understanding comes from an additional **metrics layer** that holds the **semantic context** AI needs to understand your business. This enables **non-SQL** engineers to add business value through BI tools immediately, creating exceptional **time-to-value**.


**Conversational BI Bridges the 20-Year Gap**:

Conversational BI finally delivers on the promise of **self-serve BI** that the industry has pursued for two decades. LLMs provide the missing interface that makes this vision achievable. **MCPs** supply the crucial missing piece on top of LLMs for **plug-and-play** AI integration, following the same standardization approach as LSPs for language servers and protocols.


BI’s **semantic business layer** provides the **context** that AI systems need to understand your business domain. This contextual foundation transforms **time-to-insight** from days to minutes, benefiting non-technical users who can engage directly with data analysis.


*The future of BI is declarative, contextual, and AI-powered. Conversational BI reduces manual work, enables faster iterations, and expands the number of people who can create meaningful BI insights.*


---


Check out Rill’s conversational [BI integration with MCP](https://docs.rilldata.com/explore/mcp) and [OpenAI generation of dashboard and models](https://www.rilldata.com/blog/one-click-dashboards-with-generative-ai-and-bi-as-code), which makes the self-serve promise a reality. Everything is open-source and available on [GitHub](https://github.com/rilldata/rill), and can be run locally with a [single command](https://www.rilldata.com/).


---


```
Full article published at Rilldata.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/self-service-bi-ai/)
|
[Declarative Data Stack](https://www.ssp.sh/tags/declarative-data-stack/)
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Artifical Intelligence](https://www.ssp.sh/tags/artifical-intelligence/)
[Analytics](https://www.ssp.sh/tags/analytics/)
[Genbi](https://www.ssp.sh/tags/genbi/)
[Rill](https://www.ssp.sh/tags/rill/)
[Services](https://www.ssp.sh/tags/services/)
