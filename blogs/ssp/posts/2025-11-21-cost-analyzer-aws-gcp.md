---
title: "Multi-Cloud Cost Analytics: From Cost-Export to Parquet to Rill"
date: 2025-11-21
url: https://www.ssp.sh/blog/cost-analyzer-aws-gcp/
slug: cost-analyzer-aws-gcp
word_count: 3339
---

![Multi-Cloud Cost Analytics: From Cost-Export to Parquet to Rill](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Companies often use multiple platforms simultaneously: Lovable for apps, OpenAI and Claude for AI, AWS and GCP for infrastructure. Tracking costs across these services becomes nearly impossible without a unified dashboard. You’re looking at AWS bills in one place, GCP invoices in another, AI API costs in a third spreadsheet. Combining cloud costs with Monthly Recurring Revenue (MRR) to answer that? Even harder.


What’s missing is the combination of income and cost with a recurring margin board. Seeing your cloud costs, not only per one cloud, but overall, and adding MRR. Not a single vendor dashboard, but a single pane of glass for multiple sources of cost.


This article shows how to get insights into the cost expenses of multiple cloud vendors, extracted with dlt, integrated into a dimensional model with SQL and Python, and visualized with Rill.


I set myself the goal of creating a thorough project that can be reused by others to get their own **multi-cloud cost overview**. This is a tutorial on how I created this project, documenting the full journey and giving you the information to get started immediately with your own cost data, updated constantly.

If you only want to see the code

Jump directly to GitHub and create your own cost report, go ahead with the repo at [cloud-cost-analyzer](https://github.com/ssp-data/cloud-cost-analyzer). It’s a scaffold and working dlt and Rill scripts for getting a cost overview across cloud providers, extendable with dlt, Rill or Python. All the details explained in this article


## The Vision: A Unified Multi-Cloud Cost Dashboard


After reading the documentation and brainstorming with Mike Driscoll about what we were going to build and what to highlight, we had a plan. On a high level, we wanted to provide a repository that people can use to get instant cloud cost overview with pre-defined dashboards, highly inspired by [aws-cur-wizard](https://github.com/Twing-Data/aws-cur-wizard), which does this but only for Amazon, and the export is done manually or outside of the project.


We wanted to automate that process, include other cloud providers, and even include revenue to get an instant revenue and margin dashboard that shows income and outcomes based on Stripe, Shopify, Salesforce, or cloud provider costs.


### Breaking It Down: The Implementation Roadmap


Quickly I knew we would want to use [dlt](https://github.com/dlt-hub/dlt) as the integration CLI that speaks Python, super lightweight and integratable everywhere through a CLI. We wanted to store the data in DuckDB locally or ClickHouse in the cloud and visualize with Rill, including the pre-created dashboard by aws-cur-wizard.


With that, I set myself these goal tasks and steps to implement:

1. **Integrate Stripe** for revenue data via dlt
2. **Set up AWS Cost and Usage Reports** exporting to S3
3. **Configure GCP billing export** to BigQuery and load via dlt
4. **Unify all sources** into one dlt project with incremental loading
5. **Make it pluggable** so adding Azure, Cloudflare or other providers is straightforward
6. **Combine everything in DuckDB/Parquet** (with ClickHouse Cloud as the production option)
7. **Generate demo data** so people can test without real credentials
8. **Create Rill dashboards** adapting aws-cur-wizard for multi-cloud + revenue
9. **Run it locally first**, then extend to run cloud-native with GitHub Actions


Unfortunately, as simple as the list sounds, it took some engineering and surprises.


### Stripe Integration with dlt


I managed to cross off the first one quite easily. Thanks to dlt, the integration from Stripe was a piece of cake. I needed an external token, initialized dlt as explained in [their docs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/stripe), and with [uv](https://github.com/astral-sh/uv) as the setup, it was up and running almost immediately. From there I thought it was going to be easy.


### AWS Cost Export and Integration


The next step was to export from AWS. I thought to use an API or CLI to quickly export this data, similar to Stripe. Or so I thought. After I got started, I quickly noticed that wasn’t going to be that easy. You need to set up a Cost export report within the portal of AWS, store the data in an S3 bucket, and then from there you can download the data in the appropriate format.


I checked a couple of different ways, but no, that’s the official way to export, and after you have set up the right region, the bucket, permissions, and IAM roles correctly, it’s another piece of cake with dlt to configure and pull data from S3. But it needs a manual setup with someone setting up a couple of things to make it work (more on this later, and also detailed in the GitHub Repo).


### GCP Cost Export


The same goes for Google Cloud Platform, except you export into BigQuery instead of blob storage. After setting up a standard report and a detailed one, you get data automatically exported to BigQuery, and I set up a dlt load to load this data too. Figuring out all the different ways of authentication with project_id, private_key, client_email, and token_uri, which can be done through exporting a JSON key file, is easy too.


## Transforming Raw Costs into Insights: Data Modeling Part


The next part was to model the data, combine and join the same dimensions, align the facts, and visualize it.


Typical dimensions are:

- **Region**: which geographic location the data is stored in
- **Service / Product**: the service we pay for
- **Time**: the day and time we used the service
- **Cloud provider**: AWS, Google, etc.
- And so on


Typical facts are obviously:

- **Amount**: how much we need to pay (and what currency, though that’s a dimension related to amount)
- **Revenue**: income from Stripe or other income sources
- Combined metrics: **Margin** such as revenue minus costs, margins, etc.


Once these were defined, we had to write the SQL statements


## Showcase: The Dashboards in Action


But now to the project. I have built a GitHub repo that you can clone, and after you have set up your cost export reports on AWS and GCP, you can configure the secrets and ENVs, and you have a dashboard overview that you can run locally instantly.


This is the first part of the project. The next part will be how to set up in the cloud to share with others.


This solution is **composable**âdlt can ingest multi-cloud data and Rill can add any sources. The reports show a **single pane of glass** across multiple cost sources. See the dashboard examples below.


*This is a quick showcase of how the project works and what you’ll get from the reports. You’ll find the screenshots and detailed integration with setting up everything below | [Link](https://youtu.be/H9YjhdVNOOI)*

The data shown is based on my personal data

The data shown in the below example are based on my Stripe data (income for my book) and costs I created based on AWS and GCP over the last couple of days to showcase this example. You’ll see your services and costs accordingly.


### AWS Overview


**AWS Cost Dashboard**: Track unblended costs, RI savings, and spending trends across services:


![/blog/cost-analyzer-aws-gcp/cost_preview_8.webp](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_8.webp)

*AWS Cost Dashboard*


**Product Family and Service Breakdown**: Drill into product families, services, and operations with comparative breakdowns:


[

](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_9.webp)

Apparently the cost of creating the DB instance is quite expensive as we can see immediately. We can drill down more with the explore view.


**Explore View**: Interactive filtering by payer account, usage type, region, and more:


### GCP Overview


**GCP Cost Dashboard**: Monitor total costs, record counts, and top services at a glance:


**Service and SKU Breakdown**: Break down costs by service, SKU, project, and region with distribution charts:


We can immediately see that the licensing cost for SQL Server 2022 was the most expensive.


**Explore View**: Filter and pivot across all dimensions including billing account, location, and cost type:

The AWS Dashboards, Canvas and Explore Views are created by the aws-cur-wizard

This repo by Twing-Data provides the sophisticated dashboard generation logic. Besides flattening data, also analyzing dimensions and creating optimized visualizations in a meaningful way.. The generator examines cost coverage, identifies dominant spending categories, and selects the best chart types automatically. I adapted this approach for GCP as well. Check out their repo at [aws-cur-wizard](https://github.com/Twing-Data/aws-cur-wizard).


### Margin View: Total Cost + Revenue


**Combined Analytics Dashboard**: The unified view brings together Stripe revenue with AWS and GCP costs, showing total cost ($149), revenue ($45.8), net margin (-$104), and gross margin percentage.


Filter by cloud provider, region, or transaction type to identify where costs exceed revenue:

[

](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_2.webp)

This is not the most useful graph for my data, but if you have all revenue imported and cloud costs compared, this is probably the most anticipated dashboard by a CEO, whereas the more detailed drill-down might help the engineer find where to save some costs.


## The Technology Stack Used in This Project


The cloud-cost-analyzer project combines several modern data tools to create an end-to-end analytics solution.


The following diagram shows how the different components work together and shows the architecture overview:


![/blog/cost-analyzer-aws-gcp/tech-stack.png](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/tech-stack.png)

*Multi-Cloud Cost Analytics Tech Stack*


The key components are:

- **dlt (Data Load Tool)**: Python-based data integration framework that handles incremental loading from AWS S3, GCP BigQuery, and Stripe API.
- **DuckDB**: Embedded analytics query engine that queries **Parquet** files directly without requiring a separate database server (*Note*: I used Parquet as in the next step I want to ingest it directly to ClickHouse automatically)
- **Rill Developer**: Fast, opinionated BI tool that generates interactive dashboards from SQL models
- **Makefile**: Orchestrates the entire workflowâfrom data extraction to dashboard generation
- **Python & uv**: Modern Python package management with uv for fast dependency installation


### Data Flow & Pipeline Architecture


If we go one step ahead and look at the flow of the data and how it’s modeled, we can simply show this with this illustration:


![/blog/cost-analyzer-aws-gcp/data-flow.png](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/data-flow.png)

*Data Flow of this Project. Detailed flow see inGitHub Repo*


The project and its data pipeline do the following steps:

1. **Extraction**: Three independent dlt pipelines pull data from cloud providers
2. **Normalization** (when needed): Flattens nested data structures
3. **Storage**: All data stored as Parquet files in `viz_rill/data/` for local development, or ClickHouse Cloud for production
4. **Transformation**: Rill SQL models normalize dimensions and facts:
5. **Metrics Layer**: YAML-defined metrics provide reusable business logic (margins, totals, percentages)
6. **Visualization**: Rill dashboards render interactive analytics with sub-second query performance


## Setting Up Cost Exports: Initial Configurations


For each providerâwe use AWS and GCP in this repositoryâyou need to manually go into the web portal and create a report that exports to either S3 or BigQuery.


Below is the step-by-step explanation on how to do that.


### AWS CUR Export Creation


AWS CUR Export Process is commonly used when you work with costs. The export has a couple of setup steps and questions. AWS CUR export itself has to be done manually through the web UI.


For the one-time manual setup, go to your AWS console and follow these steps to start:

1. Go to [AWS Billing Console](https://us-east-1.console.aws.amazon.com/billing/home?region=us-east-1#/bills) and then `Cost & Usage Reports`
2. Click **Create export** and configure the following settings:


**Export Details:**

- Choose **Standard data export** (allows export for processing with tools like dlt)
- Give your export a unique name (e.g., `CUR-export-test`)
- Select **CUR 2.0** as the data table (the modern format with all cost details)


![/blog/cost-analyzer-aws-gcp/cost_preview_13.png](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_13.png)

*Create CUR export example: Configurations to choose*


**Data Table Configurations:**

- **Include resource IDs**: Check this box to get granular line-item details
- **Time granularity**: Choose **Hourly** or **Daily** depending on your needs


**Data Export Delivery Options:**

- **File format**: Select **Parquet** (required for this projectâmuch more efficient than CSV)
- **File versioning**: Choose **Overwrite existing data export file**


![/blog/cost-analyzer-aws-gcp/cost_preview_12.webp](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_12.webp)

*Data export settings options for AWS CUR export*


**Data Export Storage Settings:**

- **S3 bucket**: Enter your bucket name (e.g., `cost-analysis-demo-sspaeti` for my example)
- **S3 path prefix**: Optional, but recommended for organization (e.g., `cur/`)

1. Click **Create** to finalize the export


**After Setup:**

- AWS automatically generates and uploads CUR files to your S3 bucket daily (or hourly based on your granularity choice)
- The first export can take up to 24 hours to appear
- Files accumulate in the S3 bucket, partitioned by date


**Verify Your Export:**

You can check your existing reports in the Cost Explorer to see if data is flowing. The Cost Explorer (shown in the third screenshot) provides a quick sanity checkâif you see costs appearing there, your CUR export should be working.


![/blog/cost-analyzer-aws-gcp/cost_preview_4.webp](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_4.webp)

*Example of cost explorer in AWS UI.*


Once the export is configured, the [pipelines/aws_pipeline.py](https://github.com/ssp-data/cloud-cost-analyzer/blob/main/pipelines/aws_pipeline.py) will take care of the incremental import with dlt.

AWS doesn’t provide a fully automated CLI export

The Cost Management API requires an initial manual setup through the console. While the AWS CLI and boto3 can *read* existing reports, you still need to create the CUR export manually first. Tools like [Prometheus exporters](https://github.com/electrolux-oss/aws-cost-exporter) exist but face the same limitation.


### GCP Cost Report Export to BigQuery


Google Cloud uses BigQuery as its billing export destination, unlike AWS which uses S3. The setup is straightforward through the GCP Console.


**Setup Steps:**

1. Go to **Billing** in your [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **Billing export** in the left sidebar
3. Select the **BigQuery export** tab


![/blog/cost-analyzer-aws-gcp/cost_preview_11.webp](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_11.webp)

*Billing export in GCP cloud UI: See different export levels.*


You’ll see two export types available:


**Standard usage cost** (Enabled by default)

- Daily cost details per SKU
- Sufficient for most cost tracking needs
- Updates automatically each day


**Detailed usage cost** (Enable this for granular analysis)

- Line-item level details for each resource
- Required for this project to get service-level breakdowns
- Includes resource-specific metadata

1. Click **Edit settings** to configure:
2. Enable both **Standard** and **Detailed** exports


**Important Notes:**

- The first export can take **up to 24 hours** to populate
- Data updates daily, typically completing by the end of day
- **This export incurs BigQuery storage costs** (usually minimal, but not free)
- You can verify data is flowing by checking the “Top services” report in the billing overview


Once configured, the [pipelines/google_bq_incremental_pipeline.py](https://github.com/ssp-data/cloud-cost-analyzer/blob/main/pipelines/google_bq_incremental_pipeline.py) handles incremental loading with dlt.


**Service Account Setup (for dlt authentication):**

1. Navigate to **IAM & Admin â Service Accounts**
2. Click **CREATE SERVICE ACCOUNT**
3. Grant these roles:
4. Go to the **Keys** tab â **ADD KEY â Create new key**
5. Choose **JSON** format and download
6. Extract the credentials from the JSON file for your `secrets.toml`:


The service account JSON contains all the authentication details dlt needs to connect to BigQuery.

GCP exports cost less than $1/month for most organizations

BigQuery storage is cheap (~$0.02/GB/month), and the billing export typically generates only a few MB of data per month unless you have extensive resource usage.


This is how it looks inside the GCP UI:

[

](https://www.ssp.sh/blog/cost-analyzer-aws-gcp/cost_preview_3.webp)


### Stripe Integration


Stripe provides the revenue data for calculating margins against cloud costs. Setup requires only an API token.


**Generate API Token:**

1. Log in to your [Stripe Dashboard](https://dashboard.stripe.com/)
2. Click **âï¸ Settings** (top-right) â **Developers** â **API Keys**
3. Under “Standard Keys”, click **Reveal live key** next to the Secret Key
4. Copy the `sk_live_...` token for your `secrets.toml` configuration

Another example MRR

If you want to see other MRR, publicly shared, check out [TrustMRR](https://trustmrr.com/) for a verified startup revenue database.


## Why Multi-Cloud Cost Visibility Matters


This project started with what seemed like a simple idea: pull costs from a few APIs, throw them in a dashboard, done. But cloud cost data doesn’t work that way. Each provider has its own way of exporting that needs to be set up initially. AWS wants S3 buckets configured just right; GCP needs BigQuery datasets.


What makes this project worthwhile is the end result: **a clear overview of your actual costs across clouds**. Everything is made composable, meaning you can add extra extraction with dlt or query and visualize additional data with Rill without spinning up infrastructure. Rill handles SQL as dashboards and serves them instantly, feeling super fast. And because it’s all code and configuration, you can add Azure costs tomorrow or Anthropic API spend next week without rebuilding everything.


It’s not perfect obviously, and there’s room to improve (as always in DE work). But with the great pre-work of aws-cur-wizard reports and my extension, you can spin up a cost overview instantly after the initial hurdle of setting up the cost exports for each provider. The result with daily updates gives you visibility you didn’t have before.


If you want to dive deeper, check out the [FOCUS Specification](https://focus.finops.org/focus-specification/)âa FinOps Open Cost and Usage Specification that establishes common taxonomy, terminology, and metrics for cloud billing datasets from Cloud Service Providers (CSPs).


This project gives you a simple, running dashboard that shows whether the cloud bills are eating all the revenue in a single command, locally. Clone the code on GitHub, configure your secrets, run `make run-all` , and off you go with **actual multi-cloud costs**.


Or `run demo` to use demo data and get a gist of how the project work:



| `1
2
3
` | `git clone https://github.com/ssp-data/cloud-cost-analyzer.git
cd cloud-cost-analyzer
make demo
` |



Find all details on Github at [cloud-cost-analyzer](https://github.com/ssp-data/cloud-cost-analyzer/).


In the meantime, I’ll extend the project to run cloud-native too with ClickHouse Cloud, Rill Cloud, and GitHub Actions, in case you don’t want to run it locally. I will come back with [Part 2](https://www.ssp.sh/blog/finops-dlt-clickhouse-rill/) of this article. That’s what extensibility makes possible.


## Appendix


Below are some notes that might be valuable as a concrete example of how I used prompt engineering for parts of this project and how the benefits for a declarative project like this one can be the perfect spot to use agents.


### Building with AI Agent


I included some of the prompts I used and where I used Claude Code to help me. The reason I included them is because this project is a perfect example for using some of the agents to get a quick start-up since we have all the **data locally**, the **models and visualization done through code** with Rill as the BI visualization, and the **pipelines done in Python** with dlt.


Rill provides us with a powerful CLI, and so does dlt. Python is the language of data and Claude understands it better than I do. For the data, once we’ve downloaded it, Claude can use DuckDB to query it, get an understanding in a couple of minutes, and start proposing a simple data model as metric views in Rill as YAML, along with dashboards, canvases, and explore views.


We can even keep Rill running and see the result live while Claude is doing its work. Obviously, we need to check if it did the metrics we actually want, and we can steer it and update final changes ourselves. But the initial first draft will already be functioning and in a good state since Claude can check if it works with the Rill CLI and has verified the data and its content with DuckDB.


I went one step further and actually created a Rill scaffold with a pre-existing project that has margins and similar dashboards, and I told it to read an existing repo that had the AWS-CUR views we used in this repo too.


You can check the initial prompt, the outcome summary by Claude, and the final commit of this actual project:

- Prompt: [2_claude_prompt_rill_setup.md](https://github.com/ssp-data/cloud-cost-analyzer/blob/main/_prompts/2_claude_prompt_rill_setup.md)
- Outcome: [Summarized](https://github.com/ssp-data/cloud-cost-analyzer/blob/main/_prompts/2_claude_prompt_rill_setup.md)
- Commit: [2-claude code prompt generation](https://github.com/ssp-data/cloud-cost-analyzer/commit/1553989362a3f6c26b07d178662308df1250c897)


There are more [prompts](https://github.com/ssp-data/cloud-cost-analyzer/tree/main/_prompts) and results in this repo that you can check out. This doesn’t even use any MCP or similar, because everything is local and code-first with a **[declarative data stack](https://www.rilldata.com/blog/the-rise-of-the-declarative-data-stack)**âall configuration, all definition, all code, everything is in this single repo, even the data since it’s just Parquet files. If you want, you can vibe code new data sources into the project.


---


```
Full article published at Rilldata.com - written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/cost-analyzer-aws-gcp/)
|
[Cost](https://www.ssp.sh/tags/cost/)
[Aws](https://www.ssp.sh/tags/aws/)
[Gcp](https://www.ssp.sh/tags/gcp/)
[Stripe](https://www.ssp.sh/tags/stripe/)
[Rill](https://www.ssp.sh/tags/rill/)
[Dlt](https://www.ssp.sh/tags/dlt/)
[Open Source Project](https://www.ssp.sh/tags/open-source-project/)
[Dashboard](https://www.ssp.sh/tags/dashboard/)
[Business-Intelligence](https://www.ssp.sh/tags/business-intelligence/)
[Services](https://www.ssp.sh/tags/services/)
