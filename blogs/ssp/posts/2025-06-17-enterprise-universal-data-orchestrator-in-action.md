---
title: "Universal Data Orchestrator in Action: Enterprise Best Practices"
date: 2025-06-17
url: https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/
slug: enterprise-universal-data-orchestrator-in-action
word_count: 3085
---

![Universal Data Orchestrator in Action: Enterprise Best Practices](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/featured-image.jpg)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Moving from orchestration theory to the enterprise level is a real challenge. How do you handle secrets across environments? Where does your business logic actually live? How do you make pipelines that work for both your senior engineers and the analysts who need to modify them?


In Part 1, [The Heartbeat of Data Engineering](https://www.ssp.sh/blog/universal-data-orchestrator/), we discussed the convergent orchestrator combining orchestration as code and no-code. The dual interface with an advanced UI but with the generated code as YAML helps automate and version control the data pipelines.


In Part 2, we will explore the workflows of enterprise orchestration, using Kestra, Snowflake, and dlt as examples. We will also examine the use of LLMs and MCP for data pipelines, how to set them up for enterprise use cases, and best practices for working on larger projects.


## Getting Started with Kestra


Before we start with the example project, let me explain the steps to start with Kestra and what I learned when I started using it.


First of all, Kestra is open source, and you can clone it and run it with Docker installed in the following way:



| `1
2
3
` | `curl -o docker-compose.yml \
https://raw.githubusercontent.com/kestra-io/kestra/develop/docker-compose.yml
docker compose up -d
` |



After pulling the Docker image (this might take a while the first time), you will have a Kestra container up and running:



| `1
2
3
4
` | `â¯ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS                            PORTS                              NAMES
1cdf7f265fdf   kestra/kestra:latest   "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds                      0.0.0.0:8080-8081->8080-8081/tcp   kestra-dlt-snowflake-kestra-1
aabb262aad3f   postgres               "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds (health: starting)   5432/tcp                           kestra-dlt-snowflake-postgres-1
` |



Once this is running, you can access a fully functional orchestrator running locally on [localhost:8080](http://localhost:8080/):


![/blog/enterprise-universal-data-orchestrator-in-action/kestra-ui.webp](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-ui.webp)

*Kestra UI localhost*


### Creating Pipelines


Pipelines can be simply created with Flows, and for data transformations, you can use plugins that allow you to define SQL queries directly within your YAML workflow definition or as separate files added from the built-in Namespace Files Editor in the UI. This unique dual interface (code + UI) in action looks as follows:



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
` | `  # Analyze filtered data with DuckDB
  - id: query
    type: io.kestra.plugin.jdbc.duckdb.Query
    fetchType: STORE
    inputFiles:
      products.json: "{{ outputs.transform.outputFiles['products.json'] }}"
    sql: |
      INSTALL json;
      LOAD json;
      SELECT brand, ROUND(AVG(price), 2) AS avg_price
      FROM read_json_auto('{{ workingDir }}/products.json')
      GROUP BY brand
      ORDER BY avg_price DESC;
` |



## Implementation Walkthrough: Building a Data Pipeline


Now, let’s move on to an example data pipeline built using Kestra combined with [dlt](https://dlthub.com/) and Snowflake. The code to follow for this project can be found on GitHub at [kestra-dlt-snowflake](https://github.com/sspaeti/kestra-dlt-snowflake).


### Explaining This Project: Setup


The [project](https://github.com/sspaeti/kestra-dlt-snowflake) demonstrates a real-world data pipeline using Kestra as the orchestrator, dlt (data load tool) for data ingestion, and Snowflake as the destination warehouse. The project uses modern data engineering patterns by extracting chess player data from the Chess.com API and loading it into Snowflake with the lean but powerful CLI-first dlt tool, supporting [all kinds of loading strategies](https://dlthub.com/docs/general-usage/full-loading) out of the box.


Here’s an architectural illustration of this Kestra dlt Snowflake pipeline project:


![/blog/enterprise-universal-data-orchestrator-in-action/kestra-project-mermaid.jpg](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-project-mermaid.jpg)

*Project Structure*

<div class="mermaid" id="id-2"></div>

The architecture leverages Kestra’s [`SyncNamespaceFiles`](https://kestra.io/docs/how-to-guides/syncnamespacefiles) plugin to automatically pull the entire data pipeline codebase from GitHub into the orchestrator, making the code available within Kestra’s namespace files.


This creates a powerful development workflow where data engineers can work locally with their preferred tools while the pipeline execution happens in a controlled, containerized environment. The project also demonstrates the practices of encrypted credential management (via the `encrypt.sh` script), incremental data loading patterns, and separation of concerns between orchestration logic and data processing code.


### Executing Demo Pipeline


The flow will clone the GitHub repo with the dlt code.


![/blog/enterprise-universal-data-orchestrator-in-action/flow.webp](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/flow.webp)

*Flow tasks*


Then, it runs the dlt data ingestion task, which extracts data from the Chess API and loads it into Snowflake.


![/blog/enterprise-universal-data-orchestrator-in-action/kestra-files.webp](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-files.webp)

*Flow tasks*


At any time, you can see what code and pipeline is executed.


We can verify that the data loaded within Snowflake with these queries executed in Snowflake:



| `1
2
3
4
` | `select * from dlt_data.CHESS_PLAYERS_GAMES_DATA._DLT_LOADS order by inserted_at desc LIMIT 3; 
select count(*) from dlt_data.CHESS_PLAYERS_GAMES_DATA.PLAYERS_ONLINE_STATUS; 
select count(*) from dlt_data.CHESS_PLAYERS_GAMES_DATA.PLAYERS_PROFILES     ; 
select count(*) from dlt_data.CHESS_PLAYERS_GAMES_DATA.PLAYERS_GAMES        ; 
` |



Result:



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
` | `+--------------------+-------------+--------+-------------------------------+...+
| LOAD_ID            | SCHEMA_NAME | STATUS | INSERTED_AT                   |...|
|--------------------+-------------+--------+-------------------------------+...|
| 1749549465.3164442 | chess       |      0 | 2025-06-10 09:57:48.409 +0000 |...|
| 1749549458.6228833 | chess       |      0 | 2025-06-10 09:57:44.448 +0000 |...|
| 1743454386.431451  | chess       |      0 | 2025-03-31 20:53:09.733 +0000 |...|
+--------------------+-------------+--------+-------------------------------+...+

+----------+
| COUNT(*) |
|----------|
|       48 |
+----------+
+----------+
| COUNT(*) |
|----------|
|        4 |
+----------+
+----------+
| COUNT(*) |
|----------|
|     4264 |
+----------+
` |



This example shows how to integrate any data with dlt to Snowflake with simple components available out of the box in Kestra. We could add OpenAI capabilities (example [here](https://github.com/dlt-hub/dlt-kestra-demo) by dlt), an MCP (more on this later), or any ETL process on top of your data integration.


Let’s next examine how we can use Kestra to write enterprise-ready data pipelines and some best practices to follow.


## Making it Ready for Enterprise


When working in an enterprise environment, there are additional best practices we need to follow. In this section, we answer some of the common setups that help you use Kestra, but also orchestration in general.


### Separation of Concerns: Orchestration vs. Business Logic


One key consideration in an enterprise setup is where to put the **business logic**. In the old days, we put it into stored procedures—custom code that databases had like PL/SQL in Oracle and T-SQL in Microsoft SQL Server. In the world of composable data stacks, the business logic is usually in SQL statements, Python, or YAML.


Kestra eases life as it allows us to focus on the business implementation as parts of plugins for the most part, and some of the heavy technical logic is abstracted away by the [plugins](https://kestra.io/plugins) themselves. Sometimes you still need to bring your custom code to adapt to unique needs of your organization. In the example pipeline, we added our custom dlt data ingestion logic within a separate Python file, and we can use Kestra’s native orchestration concepts, such as flows, tasks, and namespace files, to glue it all together while keeping business logic separated from orchestration code. Let’s look at some other ways of doing the separation.


#### Subflows


[Subflows](https://kestra.io/docs/workflow-components/subflows) allow us to build **modular** and **reusable** workflow components, and work similar to calling a function. This is where you can write [Functional Data Engineering](https://ssp.sh/brain/functional-data-engineering/) code, where a Subflow can be reused across multiple flows. For example, the integration with dlt, processing a specific file format that only your company has, or alerting errors to Slack and email—all of those can be encapsulated into a subflow and called from any other flow.


With subflows, you can avoid copying and duplicating code across your codebase and avoid reimplementing logic in multiple places. You can reuse components across multiple flows. Think of it as a resource that data engineers build, which less technical people can reuse.


### Multi-Tenancy


Another enterprise-ready feature that Kestra comes with are [Tenants](https://kestra.io/docs/enterprise/governance/tenants). Many of us, if we don’t build only for ourselves, have the need for separating different pipelines from different organizational departments or when people are not allowed to see others’ data. The tenant feature provides an **isolated environment** within a single Kestra instance.


It provides an elegant way to isolate your Kestra instance for different teams, business units, customers, or clients.


### Handling SQL within a Data Pipeline


Another important question when building data pipelines is where to put your SQL transformations—your traditional business logic.


Kestra offers several approaches depending on your complexity needs. As seen in the simple example above, you can **integrate simple SQL statements** within the flow code. For more complex cases, e.g., a SQL file with hundreds of lines of code, it’s recommended to store your SQL code as a separate Namespace File and reference it in your pipeline.


Alternatively, if you do everything from Terraform, you could also reference your file with a [Terraform Templatefile](https://developer.hashicorp.com/terraform/language/functions/templatefile):



| `1
2
3
4
5
` | `tasks:
  - id: "query"
  ....other options...
    sql: |
      ${indent(6, file("my-query.sql"))}
` |



The `indent(6, ...)` syntax indents spaces for the YAML syntax, the `file()` function reads the external file and `${...}` is used as the [Terraform syntax](https://developer.hashicorp.com/terraform/language/functions/templatefile).


Or as the third option and for maximum flexibility, you can **template entire flows** using Terraform’s `templatefile` resource:



| `1
2
3
4
5
6
7
8
` | `resource "kestra_flow" "analytics_pipeline" {
  namespace = "analytics.team"
  flow_id = "user-analytics"
  content = templatefile("flows/user-analytics.yaml", {
    database_url = var.database_url
    query_timeout = var.query_timeout
  })
}
` |



This last template option allows you to parameterize your flow with variables or include multiple external SQL files while creating reusable flow templates. This way, you can also separate configuration from logic.

As a Rule of Thumb
Store complex SQL files in a dedicated directory (e.g.,
or
), and use
**naming conventions**
with descriptive names that match your task IDs.

Also see all dedicated [SQL plugins](https://kestra.io/plugins?page=1&size=40&category=All+Categories&q=sql) that are available:


[

](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-sql.webp)SQL Plugins


### Handling Secrets


As opposed to demo use cases, handling [secrets](https://kestra.io/docs/concepts/secret) outside of your deployment and code is crucial in enterprise deployments. Kestra provides multiple options depending on your environment and requirements.


#### Use Built-in Secrets Management in Kestra


For enterprise deployments, Kestra [Enterprise Edition](https://kestra.io/docs/enterprise) provides API-first secret management where you can add secrets directly from the web interface under `Namespaces â Secrets` or via an API call. This approach integrates with [external secret managers](https://kestra.io/docs/enterprise/governance/secrets-manager) like [HashiCorp Vault](https://developer.hashicorp.com/vault), [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), or [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/), offering robust governance, audit trails, and centralized secret rotation. The Enterprise edition also supports more sophisticated secret backends and doesn’t require manual base64 encoding.


#### Encrypted Environment Variables


In the open-source version, you can fall back on encrypted environment variables. To do that, create an `.env` file:



| `1
2
3
` | `GITHUB_ACCESS_TOKEN=***
DESTINATION__SNOWFLAKE_CREDENTIALS=***
DESTINATION__SNOWFLAKE_PASSWORD=*** DESTINATION__SNOWFLAKE_HOST=***
` |



After that, run `./encrypt.sh`, which will encrypt it, prefix `SECRET_`, and create the file specified in `docker-compose.yml` called `.env_encoded`.


Here is the code for [`encrypt.sh`](https://github.com/sspaeti/kestra-dlt-snowflake/blob/main/encrypt.sh):



| `1
2
` | `#!/bin/bash
while IFS='=' read -r key value; do    echo "SECRET_$key=$(echo -n "$value" | base64)";done < .env > .env_encoded
` |



The encrypted file should look similar to `.env_encoded`:



| `1
2
3
` | `SECRET_GITHUB_ACCESS_TOKEN=Z2l0aHViX3BhdF8xMUFBR...
SECRET_DESTINATION__SNOWFLAKE_CREDENTIALS=InNub3dmbGFrZTovL2xvYWRlcjo8c...
SECRET_DESTINATION__SNOWFLAKE_PASSWORD=Ijxw...
` |



While the `.env` approach works well for development and smaller deployments, enterprise-grade secret managers provide better security, compliance features, and operational capabilities. In your flows, secrets are accessed using the same `{{ secret('SECRET_NAME') }}` syntax regardless of the backend, making it easy to migrate between open-source and Enterprise editions as your needs change.


Read more about all available secret management options and enterprise features in the [Kestra Secrets documentation](https://kestra.io/docs/concepts/secret).


### Triggers: React on Changing Events


Use **[Triggers](https://kestra.io/docs/workflow-components/triggers)** for scheduling or reacting to event-based upstream events automatically. For example, starting a downstream flow based on a REST event with the [Webhook Trigger](https://kestra.io/docs/workflow-components/triggers/webhook-trigger). There are many more triggers such as polling, real-time, S3, and Kafka—check them in the docs.


### YAML-based


As discussed in [Part 1](https://www.ssp.sh/blog/universal-data-orchestrator/), unlike many other orchestrators, you **do not need to know how to code** (in Python, Java) or have a technical background. You can use the elegant UI and implement many things yourself, or soon, using a built-in AI agent integrated into Kestra.


## Generative AI Integration in Kestra with MCP


Taking a step back after spotlighting the key parts and best practices for enterprise data pipelining: The key is still to ease the management of various tasks and components in a universal data orchestrator. To empower every user of Kestra, there’s obviously also an AI helper that improves the workflow in the form of [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol), helping us with data pipeline creation and maintenance.


MCPs help integrate different models in the same way; it’s a unified protocol that defines the interface between a server and client (in this case, Kestra). This way, we can add an MCP Server to Claude Desktop, Cursor, Neovim—basically in your Integrated Development Environment (IDE) of choice.


### Demos


I’m not going into more technical details on how to implement one, as there are great examples out there for you to pick and choose:

- [MCP with Kestra - Orchestrating using Natural Language](https://www.youtube.com/watch?v=zAE3oh85e4c): Demonstrates how to build an MCP server that allows natural language interaction with Kestra orchestration workflows, including executing flows and analyzing dependencies.
- [How to use MCP servers from a custom AI agent (step by step)](https://www.youtube.com/watch?v=x8LQC6ut53Y): Step-by-step tutorial showing how to build a custom AI agent using LangChain that connects to MCP servers and integrates the entire workflow using Kestra.
- [Observability for MCP servers with Kestra - Ready, Set, Cloud](https://www.readysetcloud.io/blog/allen.helton/kestra/): A blog post detailing how to implement async observability and analytics for MCP server tool usage using Kestra workflows and Momento cache.
- [Observability for MCP servers with Kestra featuring Allen Helton](https://www.youtube.com/watch?v=kAnFsNw9ZZ8&t=1933s): Interview and demo with Allen Helton showing how to track MCP server metrics and visualize tool usage analytics using Kestra workflows and Postman visualization.


But instead, what I will do is tell you why Kestra is in a **unique position** to use MCPs for data orchestration and what to keep an eye on.


### Why Generative AI in Kestra Can Make All the Difference?


As with all AI workflows, they need data and context. Because Kestra builds its whole flows and definitions as code, it’s easy for [Large Language Models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model) to pick up context around the pipeline.


It also allows the AI model to add to an existing project based on active best practices. The more specific the task, the more useful the output will be.


Why are code artifacts such as YAML the perfect setup for AI? Because AI has a very limited context window (a couple of prompts), but if you give it an intermediate stage, think of it like **in-memory RAM** that both the LLM and the human can work together on, building up that larger context that the AI hugely benefits from.


Combined with Kestra’s local sync capabilities, this creates an innovative workflow where humans and AI can collaboratively build and maintain complex data pipelines using the repository as shared “in-memory RAM” for larger contexts that benefit both parties.


Already without an MCP, we can use Cursor and ask to integrate an additional step to our [dlt-snowflake flow](https://github.com/sspaeti/kestra-dlt-snowflake/blob/e72d2a5e0ed004e077dfbe24a5e16d903012a670/kestra-sync/demo_dlt-chess-snowflake-demo.yml) like this:


[

](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-cursor1.webp)Using Cursor to add configuratively with AI


And so it added the following:


[

](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-cursor2.webp)Generate OpenAI configuration by Cursor


Which worked on the first try when I ran it—not the most useful step, but you could imagine adding something more sophisticated:


[

](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/kestra-openai.webp)Executed pipeline with OpenAI response


With MCP implementation, Cursor (or other IDEs) can work more autonomously, like agent mode where they might autonomously ask OpenAI a couple of times until they have the answer—as seen in the demo example linked.


## The State of Universal Data Orchestrator in Action


In this article and walkthrough with Kestra, dlt, and Snowflake, we learned how universal orchestration bridges the gap between technical complexity and practical usability. The combination of visual interfaces with generated YAML, Git synchronization, and AI assistance through MCPs creates workflows that work for both seasoned engineers and newcomers to data orchestration. This highlights enterprise best practices such as separation of concerns, how to integrate SQL and Python logic, and secret management.


Some upcoming features in the [next release](https://github.com/kestra-io/kestra/releases) include **WebSearch and MCP** client tools support, expanded **embedding store** providers for **LangChain4j**, and additional AI-powered workflow capabilities as well as enhanced **flow testing capabilities** beyond the current unit testing framework, improved **dependency caching for additional languages**, and expanded **tenant isolation features** for even stricter data governance requirements.


As Kestra is open-source, you can follow all releases on [GitHub](https://github.com/kestra-io/kestra/).


Data orchestration is becoming more accessible, but the underlying complexity hasn’t disappeared. Tools like Kestra handle that complexity so teams can focus on what their data should accomplish rather than how to move it around.


## Appendix


Not part of the blog, but interesting tips and tricks that might help setting up your project that I learned while playing around with Kestra.


### GenAI-Powered Pipeline Development


Kestra’s local flow synchronization creates a powerful feedback loop with AI models. By syncing flows locally as code, you can leverage Generative AI discussed above to actively update and enhance your pipelines.


**Example workflow:**

1. Sync your Kestra flows to local filesystem
2. Feed the YAML structure to your AI model
3. Request modifications: “Add a dlt ingestion to read data from PostgreSQL”
4. AI generates updated YAML with new tasks
5. Test and deploy the enhanced pipeline


### Development Environment Setup


**Package Management with [uv](https://github.com/astral-sh/uv):** Since Kestra runs in Docker but uv expects a virtual environment, use the `--system 2> /dev/null` flag to install packages system-wide without errors.


**[Local File Synchronization](https://kestra.io/docs/how-to-guides/local-flow-sync):** Enable real-time sync between Kestra and your local development environment. In docker-compose we add to `volume` and in `KESTRA_CONFIGURATION`:



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
` | `  kestra:
	image: kestra/kestra:latest
	...
	volumes:
	# all others here
	- /your/local/path:/kestra-sync
    env_file:
        - .env
    environment:
      KESTRA_CONFIGURATION: |
        kestra:
          # my configs
        micronaut:
          io:
            watch:
              enabled: true
              paths:
                - /kestra-sync
` |



### File Management Strategies


**Namespace Files:** Store scripts and resources within your namespace for easy reference:



| `1
2
3
4
5
6
7
8
9
` | `id: my-pipeline
namespace: company.team
tasks:
  - id: run-script
    type: io.kestra.plugin.scripts.python.Commands
    namespaceFiles:
      enabled: true
    commands:
      - python scripts/data-processor.py
` |



**Git Integration:** Use `SyncNamespaceFiles` to pull from existing repositories, or leverage [`PushFlows`](https://kestra.io/docs/how-to-guides/pushflows) to push validated flows from the UI directly to version control - combining visual development with proper Git workflows.


### Version Control with Git


A good overview when to use local IDE or built-in editor from [Kestra docs](https://kestra.io/docs/version-control-cicd/git):


[

](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/git.webp)Decision tree: Kestra version control with git


### Further Resources

- [dlt + Kestra deployment guide](https://dlthub.com/docs/walkthroughs/deploy-a-pipeline/deploy-with-kestra)
- [RAG implementation with Kestra and Gemini](https://kestra.io/blogs/rag-with-gemini-and-langchain4j)
- [Local flow synchronization docs](https://kestra.io/docs/how-to-guides/local-flow-sync)


---


```
This article is written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action/)
|
[Kestra](https://www.ssp.sh/tags/kestra/)
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Declarative](https://www.ssp.sh/tags/declarative/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Yaml](https://www.ssp.sh/tags/yaml/)
[Enterprise](https://www.ssp.sh/tags/enterprise/)
[Services](https://www.ssp.sh/tags/services/)
