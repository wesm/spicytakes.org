---
title: "The Universal Data Orchestrator: The Heartbeat of Data Engineering"
date: 2025-04-15
url: https://www.ssp.sh/blog/universal-data-orchestrator/
slug: universal-data-orchestrator
word_count: 3344
---

![The Universal Data Orchestrator: The Heartbeat of Data Engineering](https://www.ssp.sh/blog/universal-data-orchestrator/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

Data orchestrators have been essential since the inception of data workloads, because you need something to orchestrate your tasks and your business logic. In the old days that might have been a Makefile or a cron job.


But these days, with the challenges and complexity rising exponentially, and the tools still exploding, the orchestrator is the heart of any data engineering project, potentially any data platform.


Depending on your setup, this might not always be true, but I’d argue, in case of doubt, having an orchestrator from the very beginning does not hurt, and will save you a lot of work down the line, as they force you to a standard way of declaring data pipelines (if you have a code-first orchestrator).


In Part I of this article, we will analyze the challenges of today’s more modern data engineering, the historic events in data orchestration and why we still need an orchestrator. In [Part II](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action), we explore the unique dual interface paradigm that Kestra offers with UI + Code at the same time, and look at what the strengths and limitations are, plus a real-world example using Kestra to load Chess data with dlt into Snowflake.


## What Are the Challenges of Today’s Data Engineering?


To know why a universal data orchestrator is key to a functioning data engineering landscape, we need to look at the challenges we face today. With the open-source data stack and its freely and powerfully available tools that provide immense value from the get-go, I believe OSS tools won’t fade any time soon.


With that in mind, every data platform, whether big or small, needs some kind of orchestration. A data platform, similarly to air traffic control or a film director, needs to bring the different parts into one homogenous flow. Without a data orchestrator, you won’t have a scheduler, data lineage, visualizer, or handy function to restart a process. You end up with disjointed stored procedures. This is fine if you only use one database or one platform, but isn’t working if you have more. And I’d argue, if you don’t have a high-level buy-in into a single platform or vendor, you don’t have this.


So what’s the challenge then? Looking at the [Data Engineering Lifecycle](https://www.ssp.sh/brain/data-engineering-lifecycle), we see three core functions that data engineering platforms need to solve such as **ingestion, transforming and serving**. With the additional undercurrents like security, data management, DataOps, data architecture (big one!), software engineering and **orchestration**. The ultimate challenge is to run and **manage an end-to-end data stack** without losing control, overview, and governance.


Unless you require a real-time event-driven architecture like Kafka and OLAP systems, you most certainly should invest some time into a universal orchestration tool serving you any number of benefits overcoming longstanding [data engineering challenges](https://dedp.online/part-1/1-introduction/challenges-in-data-engineering.html) (and BI challenges before) over the last two decades.


What are these? We can summarize four main points:

- **Complexity management**: simplify the management of complex systems, ensuring seamless data flow and process integration.
- **Handling Heterogeneous Architectures**: incorporating and integrating diverse data tools, orchestrators adeptly manage these heterogeneous systems, providing a unified platform for data operations.
- **Continuous Data Quality and Error Handling**: constantly cleaning out data errors, reacting to new data inputs, maintaining data quality and integrity, and adapting to ongoing changes.
- **Data Governance**: ensuring compliance and enforcing data best practices. Help understand the data flow with data lineage end-to-end.


## Why Do We Still Need A Data Orchestrator?


With defined challenges, which are universal over two decades and will also not vanish in the near future, we can ask “why do we still need a data orchestrator”?


The tools used for orchestration have evolved from basic task schedulers like cron to modern orchestrators that integrate with the Modern Data Stack. This evolution reflects a shift from focusing solely on tasks to a more holistic approach to automate and unify the orchestration layer.


Modern orchestrators underline their growing importance in managing the sophisticated demands of today’s data engineering challenges. They are not just tools for scheduling and workflow management but have evolved into comprehensive solutions that cater to the nuanced needs of the data lifecycle.


### The Data Orchestration Evolution


To better understand why, let’s quickly revisit the chronological events that we’ve gone through. We went from terminal command line scheduler (cron), to graphical ETL drag and drop tools, to Python-based (Airflow) and declarative, YAML-based orchestrators


In a complex landscape, it’s important to get software engineering best practices in place for our central orchestration tool. Practices such as versioning our pipelines in version control to go back in case of a faulty new version, and CI/CD to detect bugs early in the lifecycle. But how do we do that? One helping factor is to have our pipelines defined in a declarative way. Even better when we have the option to define and change configurations within a simple UI that, at the same time, produces artifacts in, for example, YAML.


Declarative means we can configure and specify what we want to orchestrate, and isolate the how (technical implementation). For example, Kestra abstracts them away with out-of-the box [plugins](https://kestra.io/plugins), and even more so when you want to avoid duplicating yourself, or have technical implementation you can create [subflows](https://kestra.io/docs/workflow-components/subflows) for that. A declarative approach also lets you quickly update the pipeline with configurations, version it, rollback in case of error, test and automate, and **apply software engineering best practices** to data pipelines.


The shift also has gone further to simple tools that help **consolidate the ecosystem**. These integrate the strengths of different tools, and orchestrate them to get data governance and data quality under control. Especially if you have source connectors to major databases and REST APIs out of the box, this will help any team tremendously.


### Towards Integration: The Control Plane


With the ever-evolving data landscape, more integration and more complex data platforms, there is more to manage, more to schedule, and more to have an overview of.


Imagine an airplane; it’s vastly complex. No person, not even a pilot, can know the inside out of every jet, every piece. That’s why they created a cockpit, with hundreds of lights and knobs to turn and see what’s going on. Seeing what’s going on, managing the full system, having a **control plane**. But it is getting much more critical with the complexity of our data systems.


Unlike BI tools that only show what’s going on, the orchestrator manages and runs all the things. This obviously depends on how we design our data platforms. We can run them more in an event-based manner where small events trigger each other as opposed to one central orchestration tool that manages them all.


But I’d argue, the more complex the business, the more dangerous it is to let each system manage itself by being triggered by its previous task; instead, it needs a data orchestrator. This might work for self-orchestration in software applications themselves, if they need to be fast and run immediately, and not have a dependency on a single, too big to fail, central service. But **data workloads are different**. These are less time-critical and usually vastly complex with upstream data out of our control; we need to implement hack upon hack, and need to deliver high-quality data to the users. If we do not have a central tool, an orchestrator that gives us visualization end-to-end, especially if something fails, it’s very hard to keep it maintained well over the long run.


Not to mention all the benefits and features (backfilling, partitioning, integrations, etc.) an orchestrator provides us with, features we’d need to implement ourselves otherwise.


### The Single Orchestration is Useful


Another question you might have: why still use a centralized orchestration tool for all my data pipelines? Does it make sense to use them for multiple domains within my data domain? Isn’t that too constraining to integrate into one system?


Here I think we can argue in both directions. The pro of having a single orchestrator that can be deployed multiple times, or use Kubernetes to scale out, I think helps with end-to-end observability. It helps you understand your data flow, the architecture as a whole. Gaining efficiency by reusing well-crafted functions created by the data engineering team such as caching a table, or implementing Slowly Changing Dimension Type 2, or just having a standard across the organization - these are all huge benefits of a single orchestrator tool that comes with many more features included you don’t even need to build.


Counter arguments of being the bottleneck, or having one more software that your organization needs to rely on and make sure it stays alive all the time are valid arguments, and need to be assessed against your requirements.


But modern orchestrators have **[multi-tenant capabilities](https://kestra.io/docs/architecture/multi-tenancy)** and serve multiple teams or business units at the same time. Meaning, we have a central infrastructure that is managed by a dedicated team that knows how to operate software, signs SLAs and does all the monitoring, but then you have the data science team that implements and orchestrates its own models, the controlling team that runs some P&L pipelines, or the sales team that runs pipelines for their sales territory heads and numbers. As these teams know the numbers best, they can easily change the pipelines or transformations, even more with a UI-supportive orchestrator that generates YAML artifacts.


### Implicit Orchestration: When *Not* to Use a Universal Data Orchestrator


The alternative to central orchestration explained above and closed-source to event-driven triggers is implicit orchestration. What is implicit orchestration? It’s an abstraction to the otherwise invisible triggers that manage themselves. It’s the **ultimate abstraction** to event triggers. It’s the combination of orchestrator and micro-triggers, embracing the self-triggering nature of events.


The orchestration part is implicit, for example, when an S3 bucket gets new data, an event is triggered and a downstream task is started. It’s very similar to the microservices approach. In a way, it’s self-running, where we add logic on top of an asset, instead of having a job or [Directed Acyclic Graph (DAG)](https://www.ssp.sh/brain/dag) that *manages* the entire pipeline.


Universal data orchestrators, e.g., Kestra solve these with [Triggers](https://kestra.io/docs/workflow-components/triggers) with arbitrary logic you can add to trigger pipelines from external events.

Event-driven systems with Orchestration
Sometimes, you might orchestrate jobs and tasks by pure events and JSON-messages, for example, and an orchestrator is never explicitly created. It’s an implicit orchestration based on short-term storage queues. This is the OLAP system with integrated message queue like Kafka. Or sometimes
[you might](https://x.com/berenguel/status/1749706012276273410)
orchestrate jobs and tasks by message passing (as in Akka or Erlang actors) and an orchestrator is never explicitly created.

## The Convergence of Infrastructure-as-Code and Orchestration


The convergence between infrastructure as code and orchestration is real. Everything these days needs to be declarative, especially in the deployment world of DevOps. Infrastructure-as-code is also arriving in the data orchestration space, especially when deploying your orchestrator with Kubernetes, but not only that, data pipelines are also getting code-first as discussed and are called **declarative pipelines**. As orchestration takes on a more critical role as the heartbeat of the data application, it only makes sense that orchestration tools be as code as well.


### The Dual Interface Paradigm: UI + Code


The best example of this paradigm is [Kestra](https://kestra.io/), and the code + UI combination is where it shines. Let’s check now how Kestra works, as this new and powerful data orchestrator masters these tasks and does exactly that.


The big selling point is its **approachability**. Coding is hard, especially for business specialists who need to keep up within their field and domain and just need to get their jobs scheduled. You can’t expect them to learn programming on the side.


Maybe SQL, but not Python. So, how do you make it approachable for them? By having a nice UI that is **intuitive**. But unfortunately, sole UI-based tools have huge downsides. They can’t be versioned, automation is not possible, testing is manual, and they don’t support the mentioned [SDLC (Software Development Lifecycle)](https://aws.amazon.com/what-is/sdlc/).


Generally, software best practices are hard to apply to data engineering. We know that from the history of SSIS and Informatica, GUI-driven tools where you need to click through 100 tables if you want to load tables. Or if you want to automate, you need to hack something together.


Luckily, there is a **middle ground**:


[

](https://www.ssp.sh/blog/universal-data-orchestrator/setting-nocode.webp)YAML Editor can be on or off


Kestra for example has a functional UI, but produces “code” output on each change. In fact, it’s a configurable YAML file. It’s like JSON, but more readable. This allows us all the benefits of software best practices just described, but also the easy approachability and usability of the tool.


![/blog/universal-data-orchestrator/yaml-ui-editor.png](https://www.ssp.sh/blog/universal-data-orchestrator/yaml-ui-editor.png)

*The Dual Interface: UI editor on the left and code / YAML editor on the right*


Even more, with the latest GenAI, we can generate code and use Kestra to load that. For example, we just ask any [Large Language Model (LLM)](https://en.wikipedia.org/wiki/Large_language_model), “please generate me a transformation and aggregation for latest sales of March 2025 for each product line for all regions.” If you want, you can submit an example from the docs so it knows how Kestra needs to format it.


### The YAML Revolution in Orchestration (Why YAML?)


You might ask, why YAML? How is that better than a UI only?


YAML has had its [fair revolution](https://kestra.io/blogs/2023-12-01-yaml-pitfalls), I’d say. It’s made its way through all domains with the most prominent being DevOps where you potentially can build the entire infrastructure of any company with a single (though very large, and most of the time several) YAML file.


In case you don’t know what YAML is, think of JSON but less verbose. YAML is the language of [declarative configuration](https://www.ssp.sh/blog/rise-of-declarative-data-stack/#yaml-the-language-of-declarative-configuration). YAML, Yet Another Markup Language, has become the configuration markup language for most modern tools. The reasons are simple: Compared to its predecessors, XML and JSON, which are still highly used, YAML is **less verbose**. YAML is a **language-agnostic**, human-readable data serialization language.


Building on the revolution of YAML in DevOps, this markup language has expanded its influence far beyond infrastructure configuration. YAML’s minimalist syntax and human-readable format have made it the preferred choice for defining workflows in CI/CD pipelines, managing Kubernetes resources, and specifying cloud deployments and data pipelines, too.


This revolution has taken place in many other domains as well, because of its many advantages that we will look more into in this article. From data analytics platforms to machine learning model configurations, YAML’s declarative approach allows developers and operators to define “what” they want rather than “how” to achieve it, enabling systems to handle the complex implementation details while keeping configurations clean and maintainable. As we continue to move toward infrastructure-as-code and configuration-as-code paradigms, YAML’s position as the lingua franca of modern system orchestration only strengthens, bridging the gap between technical specifications and readable documentation.


## How Kestra Works


Besides what you already read, here’s some background on Kestra. Kestra is an orchestrator that was developed in France and is an excellent new one that suits both data engineers and also business users and any person interested in managing data and data integrations.


It has a beautiful UI that comes with [~700 plugins](https://kestra.io/plugins) out of the box connectors, that can be used plug and play, just needing configuration. Kestra works off of YAML. Simplified, you could say: Kestra is a fancy YAML editor.


Obviously it’s much more. This article introduces you to Kestra and its unique features. We go into how it works and what the key features are from the perspective of a data engineer. It’s not a getting started guide for beginners, but because Kestra is making orchestration approachable for everyone, these will be applicable for anyone knowing a little about computers. In [Part 2](https://www.ssp.sh/blog/enterprise-universal-data-orchestrator-in-action), we’ll create a data pipeline integrating data with the integration tool dlt and showcase how we can make use of the YAML code.


### Deployment


Kestra can be deployed nearly [anywhere](https://kestra.io/docs/installation), either using a standalone binary, a docker container, Docker-Compose stack or a Kubernetes release deployed with the official Helm Chart.


But it doesn’t end there; we can do the same for the critical business and data transformation logic, the pipelines. These hold the data transformations for our business, running our data lake, our data warehouses, the ingestions to an OLAP cube, or even uploading it somewhere for a data app. All these key tasks are held within YAML, as code, easy to be moved or deployed, automated, versioned, wherever we need.


### Kestra’s Strengths


Kestra’s approach to orchestration extends beyond just data pipelines; it comes with the mentioned **out of the box plugins**. This makes it super easy to ingest data from anywhere with prebuilt plugins that can be configured to our data sources and credentials, and started immediately. You might not need an integration tool if simple orchestration is what you need.


If you need more advanced connectors, or just need to read from a custom REST interface, it integrates with dlt to write tiny glue code to do that as well.


The strengths of Kestra are various. It’s a state-of-the-art orchestration tool for modern complex requirements. It has all batteries included, runs on any platform, is [open-source](https://github.com/kestra-io/kestra), and is easy to use for anyone with a beautiful UI editor. Or use YAML directly within your IDE of choice.


It’s **approachable** by everyone; some use it for [homelab](https://youtu.be/D4cixQ_Ek4Y?si=QprDcb6_YdH--rl_) organization, others use it for IoT, and still others use it for modern data orchestration. It’s easy to get going in minutes, and flexible with its unique way of blending technical features with an easy, yet powerful interface.


Kestra is **language-agnostic**, meaning any programming language can be run as it uses virtualization technologies with Dockerfiles to run anywhere. Python works too, but any language will as well.


Kestra offers [API-first design](https://kestra.io/features/api-first) principles, which means it is designed to enable programmatic access to all actions from managing workflows to user administration, seamlessly integrating into existing development workflows.


Kestra’s API-first approach provides comprehensive programmatic access to all platform functionalities, creating a flexible foundation that seamlessly integrates with existing development workflows and tools. It eases everything from workflow creation to user administration via API calls, supports CI/CD pipelines for streamlined deployment, and works with Terraform and upcoming language-specific SDKs. By prioritizing APIs, Kestra allows teams to build custom solutions, automate processes through HTTP requests and event-driven triggers, and maintain development flexibility whether coding in Kestra’s UI or a preferred IDEâall while preserving a single source of truth within version control systems.


Kestra tries to avoid building silos, which sometimes happens with drag-and-drop automation tools like Zapier. Zapier and co. are easier to start with, but they come with prebuilt integrations, there’s no heavy infrastructure to manage, and they require no coding skills. But as soon as you need something custom (like running a Python script in a container), these tools hit a wall.


Kestra bridges this gap between ultra-customizable and rigid drag-and-drop tools. It combines the flexibility of code-based orchestration with a no-code interface that anyone can learn in minutes. After all, Kestra can scale simple workflows to millions of events with a cloud-native architecture, high availability with no single point of failure and the discussed deployment flexibility.


This means your teams can start simple and scale up to complex distributed pipelinesâall within a single, unified platform.


## What’s Next?


This has provided you with a deep dive into the evolution of orchestration, the convergence between infrastructure-as-code and orchestration, and how Kestra fits into this picture with its **dual interface paradigm**.


The next Part of this series will focus on a real-world example of how to implement a dlt pipeline with Kestra, loading data into Snowflake, showcasing its simplicity and strengths. I’ll share tips and tricks I learned along the way when using Kestra, such as syncing your git repo between local IDE and Kestra.


---


```
This article is written as part of my services
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/universal-data-orchestrator/)
|
[Kestra](https://www.ssp.sh/tags/kestra/)
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Declarative](https://www.ssp.sh/tags/declarative/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Yaml](https://www.ssp.sh/tags/yaml/)
[Services](https://www.ssp.sh/tags/services/)
