---
title: "Data Modeling - The Unsung Hero of Data Engineering: Architecture Pattern, Tools and the Future (Part 3)05-26"
date: 2023-05-26
url: https://www.ssp.sh/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/
slug: data-modeling-for-data-engineering-architecture-pattern-tools-future
word_count: 4634
---

![Data Modeling - The Unsung Hero of Data Engineering: Architecture Pattern, Tools and the Future (Part 3)](https://www.ssp.sh/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/data-modeling-architecture-pattern.jpg)

Contents
ð¶
Featured on Hacker News.
[Read the comments](https://news.ycombinator.com/item?id=36151441)

Welcome to the third and final installment of our series “Data Modeling: The Unsung Hero of Data Engineering.” If youâve journeyed with us fromÂ [Part 1](https://www.ssp.sh/blog/data-modeling-for-data-engineering-introduction/), where we dove into the importance and history of data modeling, or joined us inÂ [Part 2](https://www.ssp.sh/blog/data-modeling-for-data-engineering-approaches-techniques/)Â to explore various approaches and techniques, Iâm delighted youâve stuck around.


In this third part, weâll delve into data architecture patterns and their influence on data modeling. Weâll explore general and specialized patterns, debating the merits of various approaches like batch vs. streaming and lakehouse vs. warehouse, and the role of a semantic layer in complex data architecture.


Weâll also survey the landscape of data modeling tools, comparing commercial and open-source options, and ponder the potential of AI in data modeling. To wrap up, weâll introduce data modeling frameworks like ADAPTâ¢ and BEAM, designed to guide effective data model creation. Please join me as we take this exciting journey toward understanding data architecture better.


## Data Architecture Pattern with Data Modeling


Bringing together the best of the individual approaches and techniques and knowing the common problems, we must alwaysÂ **keep the bigger data architecture picture in mind**. Sometimes you want a data vault modeling for your first layer when your source system is constantly changing, or you need a dimensional model in your last layer to build data apps on top of it or allow self-serve analytics. But how are you doing this?


For these, we need to look at data architecture per se. In this chapter, I will list some of the most common architectural patterns Iâve seen, but without going into all details of each.


## General Purpose Data Architecture Pattern (Medallion, Core, etc.)


Letâs start with the one that suited me best, the one you have seen in one form or another. When I started at a consulting firm calledÂ [Trivadis](https://trivadis.com/), and here it was called “Foundational Architecture of Data Warehouse”. We followed best practices such as `staging>cleansing>core>mart>BI`.


![/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/data-warehouse-blueprint.png](https://www.ssp.sh/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/data-warehouse-blueprint.png)

*Fundamental Data Architecture of a Data Warehouse | Image fromÂData Warehouse Blueprints, September 2016*


We would design these layers from the top-down approach discussed above and decide the data modeling technique for each layer depending on requirements.


Letâs have a detailed look at each layer, as these are fundamental for every data architecture project, and they will help us understand why weâd want to model different layers differently. The following layers or areas belong to a complete Data Warehouse (DWH) architecture but can be implemented into any data lake or analytics product you use.


### Staging Area


Data from various source systems is first loaded into the Staging Area.

- In this first area, the data is stored as it is delivered; therefore, the stage tablesâ structure corresponds to the interface to the source system.
- No relationships exist between the individual tables.
- Each table contains the data from the final delivery, which will be deleted before the next delivery.
- For example: In a grocery store, the Staging Area corresponds to the loading dock where suppliers (source systems) deliver their goods (data). Only the latest deliveries are stored there before being transferred to the next area.


### Cleansing Area


It must be cleaned before the delivered data is loaded into the Core. Most of these cleaning steps are performed in the Cleansing Area.

- Faulty data must be filtered, corrected, or complemented with singleton (default) values.
- Data from different source systems must be transformed and integrated into a unified form.
- This layer also contains only the data from the final delivery.
- For example: In a grocery store, the Cleansing Area can be compared to the area where the goods are commissioned for sale. The goods are unpacked, vegetables and salad are washed, the meat is portioned, possibly combined with multiple products, and everything is labeled with price tags. The quality control of the delivered goods also belongs in this area.


### Core


The data from the different source systems are brought together in a central area, the Core, through the Staging and Cleansing Area and stored there for extended periods, often several years.

- A primary task of the Core is to integrate the data from different sources and store it in a thematically structured way rather than separated by origin.
- Often, thematic sub-areas in the Core are called “Subject Areas.”
- The data is stored in the Core so that historical data can be determined at any later point in time.
- The Core should be the only data source for the Data Marts.
- Direct access to the Core by users should be avoided as much as possible.


### Data Marts


In the Data Marts, subsets of the data from the Core are stored in a form suitable for user queries.

- Each Data Mart should only contain the data relevant to each application or a unique view of the data. This means several Data Marts are typically defined for different user groups and BI applications.
- This reduces the complexity of the queries, increasing the acceptance of the DWH system among users.
- For example, The Data Marts are the grocery storeâs market stalls or sales points. Each market stand offers a specific selection of goods, such as vegetables, meat, or cheese. The goods are presented so that they are accepted, i.e., purchased, by the respective customer group.

And as a Foundation, we have Metadata
Different types of metadata are needed for the smooth operation of the Data Warehouse. Business metadata contains business descriptions of all attributes, drill paths, and aggregation rules for the front-end applications and code designations. Technical metadata describes, for example, data structures, mapping rules, and parameters for ETL control. Operational metadata contains all log tables, error messages, logging of ETL processes, and much more. The metadata forms the infrastructure of a DWH system and is described as “data about data”.

### Not every architecture is the same


Only some data warehouses or data engineering projects have precisely this structure. Some areas are combined, such as the Staging and Cleansing areas, or differently named. The Core is sometimes referred to as the “Integration Layer” or “(Core) Data Warehouse.”


However, the overall system must be divided into different areas to decouple the other tasks, such as data cleaning, integration, historization, and user queries. In this way, the complexity of the transformation steps between the individual layers can be reduced.


### Why use it today?


Isnât it amazing that something from 2016 is still so current? Thatâs why data modeling is getting into vogue again, as it has never been entirely outdated.


Databricks renamed these layers withÂ **bronze, silver, and gold**Â to understand it may be a little better and called itÂ [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture), but itâs something every BI engineer works with every day. In essence, itâs the same concept.


Or if we look at theÂ [Data Engineering Lifecycle](https://glossary.airbyte.com/term/data-engineering-lifecycle/)Â introduced by theÂ [Fundamentals of Data Engineering](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302), we see a similar picture but on an even higher level. You could apply the different layers to theÂ *Storage*Â layer in the image below.


![/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/data-engineering-lifecycle.png](https://www.ssp.sh/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/data-engineering-lifecycle.png)

*The data engineering lifecycle, byÂFundamentals of Data Engineering*


## Specialized Data Architecture Patterns


In this chapter, we look at patterns that might not be considered in formal data modeling, but each of its decisions will highly influence the data modeling part. Besides the general data architecture, I call these specialized data architecture patterns as these are higher-level data architecture decisions.


### Batch vs. Streaming


An obvious decision you need to take early on is if you need real-time data for critical data application or batch with near real-time micro batching every minute, the hour is enough.


Still, to this day, steaming is primarily optional. Suppose you tell the business team you can achieve near real-time with hourly batching; they will be happy. The latest up-to-date data will little influence your data analytics. Most cases are looking at historical data anyway.


Nevertheless, some business-critical data solutions need real-time. However, be aware that theÂ **effort and challenges will be much more significant**Â as you can only partially recover if a stream fails. But the good idea is to set up your data pipeline as even based on the streaming approach, and therefore can go lower and lower with the latency of your batch to achieve near real-time.


### Data Lake/Lakehouse vs. Data Warehouse Pattern


As Srinivasan VenkatadriÂ [says](https://www.linkedin.com/feed/update/urn:li:activity:6991977435017728000?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6991977435017728000%2C6993007322495148032%29)Â correctly: “Data modeling, in general, should also talk about files (open formats),Â [Lakehouses](https://glossary.airbyte.com/term/data-lakehouse/), and techniques to convert or extract structural data from semi or unstructured would help.” This is precisely where data lake/lakehouse or data warehouse patterns apply. With these, you need to think about these questions.


With the long fight betweenÂ [ELT](https://glossary.airbyte.com/term/elt/)Â with Data Lakes and traditionalÂ [ETL](https://glossary.airbyte.com/term/etl/)Â with Data Warehouses, the different architectures greatly influence the data modeling architecture.


I will only go into some detail here, as IÂ haveÂ [written extensively](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi)Â about these topics. But the decision to go with a data lake or lakehouse will likely influence the data modeling to a more open source strategy and tools. Also, as you are dumping files into your lake, you need to work with large distributed files, whereÂ [Table Format](https://glossary.airbyte.com/term/data-lake-table-format/)Â makes a lot of sense, to get database-like features on top of files.


### Semantic Layer (In-memory vs. Persistence or Semantic vs. Transformation Layer)


The data lake decision is also highly influential with the newÂ [Rise of the Semantic Layer](https://airbyte.com/blog/the-rise-of-the-semantic-layer-metrics-on-the-fly), where you run a logical layer on top of your files in the case of a data lake and the possibility of a data warehouse on top of your data marts.


This is an interesting one, as we talked inÂ [part 1](https://www.ssp.sh/blog/data-modeling-for-data-engineering-introduction/)Â andÂ [part 2](https://www.ssp.sh/blog/data-modeling-for-data-engineering-approaches-techniques/)Â about theÂ [Conceptual, Logical, and Physical Data Models](https://airbyte.com/blog/data-modeling-unsung-hero-data-engineering-approaches-and-techniques#data-modeling-approaches)Â where aÂ [Semantic Layer](https://glossary.airbyte.com/term/semantic-layer/)Â could replace the logical model. The semantic layer stores the queries in declarative YAMLs, and data not persisted in physical storage is executed at run time or when the data is fetched.Â **Integrating the semantic layer into complex data architecture and overall data modeling makes sense**. It can serve a wide range of data consumers with different requirements, such as direct SQL, API (REST), or even GraphQL, with the great benefit of writing business logic only once. Here again, as business logic is the biggest treasure of data modeling, we have many new options to model our data with semantic layers.


The counter architecture pattern is to go with aÂ **transformation layer**Â that typically can be achieved with dbt or aÂ [Data Orchestrator](https://glossary.airbyte.com/term/data-orchestrator), where you persist each step into physical storage. Mainly to gain faster speed querying these data sets and reusing the data sets with other marts or data apps. The transformation layer and itsÂ **transformational modeling**Â make a decision betweenÂ [table formats](https://glossary.airbyte.com/term/data-lake-table-format/)Â vs.Â [in-memory formats](https://glossary.airbyte.com/term/in-memory-format/),Â [query push-downs](https://glossary.airbyte.com/term/push-down/), andÂ [data virtualization](https://glossary.airbyte.com/term/data-virtualization/).

Materialized Views
A transformation layer where you persist data is very similar to what materialized views did before theÂ
[modern era of data engineering](https://airbyte.com/blog/data-engineering-past-present-and-future)
.

### Modern/Open Data Stack Pattern


Next up isÂ [Modern Data Stack](https://glossary.airbyte.com/term/modern-data-stack)Â architecture, orÂ [Open Data Stack](https://www.ssp.sh/brain/open-data-stack/). This pattern is basically forÂ [sheer choice](https://mad.firstmark.com/)Â we have nowadays to choose from the open data stack. It is its architecture to choose the right tool best suited for the requirements at hand in the company.


It matters if you chose an open source tool, v0.5, that might get out of order in a couple of years or if you chose the v0.1 that made the crackdown the line. But these are complicated bets, and only experienced data architects and people working in the field can make decisions based on intuition for the right way a project is progressing.


It is also to say no to yesterdayâs new shiny tool, resist the urge, and wait until the product is more mature. But at the same time to take risks and bet on a tool that is open to success and embraces open-source philosophy instead of building a worse copy in-house. Each enterprise company either uses a closed-source solution to handle theÂ [data engineering lifecycle](https://glossary.airbyte.com/term/data-engineering-lifecycle/)Â or makes its stack or newer option, betting on a developed framework in the open.


### Imperative vs. Declarative Pattern


TheÂ [declarative](https://glossary.airbyte.com/term/declarative/)Â approach is manifesting itself more and more. Started within the fronted revolution where react was declaring components,Â [Kubernetes](https://glossary.airbyte.com/term/kubernetes/)Â did it forÂ [DevOps](https://glossary.airbyte.com/term/dev-ops/), DagsterÂ [revolutionized orchestration](https://airbyte.com/blog/data-orchestration-trends)Â withÂ [Software-Defined Assets](https://glossary.airbyte.com/term/software-defined-assets/)Â or us at Airbyte, where we created aÂ [Low-Code Connector developer kit](https://docs.airbyte.com/connector-development/config-based/low-code-cdk-overview/)Â to create data integrations in minutes by filling out a YAML file.


It is only possible because of drastically reduced complexity and the need to write many boilerplates. The declarative way describesÂ *what*Â and theÂ *how*Â is taken care of in the framework.


I have much more to say, but you can read more on our data glossary onÂ declarativeÂ and how it relates to [functional data engineering](https://glossary.airbyte.com/term/functional-data-engineering/) and what the opposite, [imperative](https://glossary.airbyte.com/term/imperative/) pattern is.


### Notebooks vs. Data Pipelines Pattern


A pattern directly related toÂ [orchestration](https://glossary.airbyte.com/term/data-orchestrator)Â is the notebooks versus data pipeline pattern, where you can write and run a pipeline solely aÂ [notebook](https://glossary.airbyte.com/term/notebooks/)Â or a mix of mature, unit-tested data pipelines with a stable orchestrator with all bells and whistles included.


### Centralized and Decentralized Pattern


Suppose you are in the field for a while. How many cycles have you been through from doing everything server side, switching everything to server rendering, and forth and back with the battle of client vs. server, microservices vs. monoliths, and lately, central cloud data warehouses vs. a yet-to-show decentralizedÂ [Data Mesh](https://glossary.airbyte.com/term/data-mesh/). And many more forth and back will follow.


Whatever you choose, start withÂ **simplicity**. You can always add complexity later when the product and solution mature.


### Everything else


There are so many more patterns I will write about but at some time later. For now, I leave you with pointers above, and Iâll come back to it sometime later.


## Data Modeling Tools


**Popular data modeling tools**Â includeÂ [Sqldbm](https://sqldbm.com/),Â [DBDiagrams](https://dbdiagram.io/),Â [Enterprise Architect](https://sparxsystems.com/), andÂ [SAP PowerDesigner](https://www.sap.com/products/technology-platform/powerdesigner-data-modeling-tools.html). These tools are widely used in the industry and offer powerful features such as data modeling, profiling, and visualization.


**Open-source data modeling tools**Â such asÂ [MySQL Workbench](https://www.mysql.com/products/workbench/)Â andÂ [OpenModelSphere](http://www.modelsphere.com/)Â are free and offer essential features for creating data models. They are helpful for small projects and provide an opportunity for data engineers to learn data modeling skills.


**Choosing the right data modeling tool**Â depends on the organizationâs needs, budget, and project size. Large organizations may require expensive enterprise-level tools, while small businesses may opt for open-source tools. Selecting a tool that is easy to use, has the needed features, and is compatible with the organizationâs database management system is essential.


Other tools areÂ [Ellie.ai](https://www.ellie.ai/), whose key features are Data Product Design, Data Modeling, Business Glossary, Collaboration, Reusability, and Open API.


dbt can be seen as a transformation modeling tool.Â [Dagster](https://glossary.airbyte.com/term/dagster/)Â can be used as aÂ [DAG](https://glossary.airbyte.com/term/dag-directed-acyclic-graph/)Â modeling tool. And so forth. But you can also useÂ [ExaliDraw](https://excalidraw.com/)Â for Markdown-based drawing orÂ [draw.io](https://draw.io/)Â (lots ofÂ [templates](https://www.drawio.com/example-diagrams)Â for AWS, Azure, etc.) to draw architectures.


If you struggle to think in dbt tables andÂ [SQL](https://glossary.airbyte.com/term/sql/)Â is not the SQL is not the right language. One problem, SQL is aÂ [declarative](https://glossary.airbyte.com/term/declarative/)Â language, which is a blessing and a curse. Especially if you do recurring queries, SQL gets nasty spaghetti coded, which again dbt helps withÂ [Jinja Templates](https://glossary.airbyte.com/term/jinja-template/), but as itâs not a language, without much in-built support.Â [Reconfigured](https://reconfigured.io/)Â (not free) was built for people without years of experience, focusing heavily on business logic.


### What about ChatGPT?


With all the hype of generative AI, specifically ChatGPT, it asks if AI can model our data.


If we recap the information from this series, most of it condenses into translating business requirements into a data model or semantics, also called business logic. As Chad Sanderson mentioned in hisÂ [post](https://www.linkedin.com/posts/chad-sanderson_dataengineering-activity-7045442450139607040-IrA6?utm_source=share&utm_medium=member_desktop,):


> The hard part of data development is understanding how codeÂ **translates to the real world**. Every business has a unique way of storing data. One customer ID could be stored in a MySQL DB. Another could be imported from Mixpanel as nested JSON, and a third might be collected from a CDP. All three IDs and their properties are slightly (or significantly) different and must be integrated.


As Chad continues, and I strongly agree, he says, “As smart as ChatGPT might be, it would need toÂ **understand the semantics**Â of how these IDs coalesce into something meaningful to automate any step of modeling or ETL. The algorithm must understand the real world, grok how the business works, and dynamically tie the data model to that understanding.”


This is not AI or ML anymore; that is more intuition, long-term experience in working in the field, and experiencing some of the challenges to get a feeling for it.


If there is a place where you do not want to use automation, then it would be in data modeling and the overall data architecture. Here we need discussions and a deep understanding (domain knowledge) of the field and data modeling.


On the other hand, based on your data model, you can use AI to generate schemas or the physical model of a database. Brainstorm with ChatGPT based on your created data model if something is missing or if it sees something that can be changed. Sometimes you get great insights from it by providing the solution you came up with.


Maybe most importantly, a data engineer will always be needed to assess the outcome, understand and make sense of the data in front of him and understand the overall data flow of the organization. That can only be delegated for a while.


## Data Modeling Frameworks


Besides tools, there are also helpful frameworks that help you model your data, asking the right questions.


### ADAPTâ¢


[ADAPT](http://www.symcorp.com/downloads/ADAPT_white_paper.pdf)Â says that more than existing data modeling techniques like ER and dimensional modeling is required for OLAP database design. Thatâs why ADAPT is a modeling techniqueÂ **designed specifically for OLAP databases**. It addresses the unique needs of OLAP data modeling. The basic building blocks of ADAPT areÂ **cubes and dimensions**, which are the core objects of the OLAP multidimensional data model.


Although ADAPT was created for OLAP cubes in the old days, most techniques and frameworks also apply to regular data modeling nowadays. There are nine ADAPT database objects, and their symbols illustrate how to use logos with simple examples.


![/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/adapt-legend.jpg](https://www.ssp.sh/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/images/adapt-legend.jpg)

*Legend of ADAPT Framework | Source unknown*


#### Why ADAPT over ER and dimensional modeling


ADAPT is considered superior to ER and dimensional modeling for several reasons:

1. **Incorporation of Both Data and Process**: ADAPT incorporates both data and process in its approach, which is particularly useful for designing (OLAP) data marts.
2. **Logical Modeling**: ADAPT emphasizes logical modeling. This prevents the designer from jumping to solutions before fully understanding the problem.
3. **Enhanced Communication**: ADAPT enhances communication among project team members, providing an everyday basis for discussion. This improved communication leads to higher-quality software applications and data models.
4. **Comprehensive Representation**: ADAPT allows for the representation of an (OLAP) application in its entirety without compromising the design due to the limitations of a modeling technique designed for another purpose.


In summary, ADAPT is a says to be a more flexible, comprehensive, and communication-enhancing modeling technique for OLAP databases compared to ER and dimensional modeling.


### BEAM for Agile Data Warehousing


[BEAM](http://www.decisionone.co.uk/), or Business Event Analysis & Modeling, is a method for agile requirement gathering designed explicitly for Data Warehouses, created by Lawrence Corr and Jim Stagnitto in theÂ [Agile Data Warehouse Design](https://www.amazon.com/Agile-Data-Warehouse-Design-Collaborative/dp/0956817203)Â book. BEAM centers requirement analysis around business processes instead of solely focusing on reports.


It uses an inclusive, collaborative modeling notation to document business events and dimensions in a tabular format. This format isÂ **easily understood**Â by business stakeholders and easily implemented by developers. The idea is to facilitate interaction among team members, enabling them to think dimensionally from the get-go and foster a sense of ownership among business stakeholders.


The principles of BEAM include:

- [**Modelstorming**](https://modelstorming.com/)**:**Â Business intelligence is driven by what users ask about their business. The technical setting is secondary. Storyboarding the data warehouse to discover and plan iterative development
- **Asking stories with 7W**: Telling dimensional data stories using the 7Ws (who, what, when, where, how many, why, and howâmodel by example, not abstraction; using data story themes.
- **Visual modeling**: Sketching timelines, charts, and grids to model complex process measurement â simply
- **Business Driven**: Well-documented data warehouses that take years to deploy will always need to be updated. Business users will look elsewhere. Usually with business units: “I need it now, or Iâd rather stick with Excel solution â¦.”
- **Customer Collaboration**: End usersâ business knowledge is your greatest resource.
- **Responding to Change**: Promoting change through the above actions, leading to weekly delivery cycles.
- **Agile design documentation**: Enhancing star schemas with BEAM dimensional shorthand notation


Lawrence Corr emphasizes the importance of asking the right questions or “data stories.” For instance, a customerâs product purchase could trigger questions about the order date, purchase and delivery locations, the quantity bought, purchase reason, and buying channel. A comprehensive picture of the business process is formed by carefully addressing these questions and providing the basis for technical specifications.


### Common Data Model


There are examples of standard data models, so you do not need to start from scratch. The concept behind these approaches is to transform data contained within those databases into a standard format (data model) and a common representation (terminologies, vocabularies, coding schemes), then perform systematic analyses using a library.


For example, every model needs dimensions such as customer, region, etc. Some references I found you see below:

- Microsoft startedÂ [The Common Data Model (CDM)](https://github.com/microsoft/CDM).
- [OMOP Common Data Model](https://www.ohdsi.org/data-standardization/)Â for health care. It allows for systematically analyzing disparate observational databases.
- Elastic has itsÂ [Common Schema (ECS) Reference](https://www.elastic.co/guide/en/ecs/current/index.html).
- A bit more advanced, but aÂ [DBML (Database Markup Language)](https://github.com/holistics/dbml), an open-source DSL language designed to define and document database schemas and structures, tries to create a standard for determining these models. DBML is intended to be simple, consistent, and highly readable. Works well withÂ [dbdiagram.io](https://dbdiagram.io/).


## Applying Data Modeling / Best Practices?


At the end of all we learned, how do you apply data modeling in practice? This series gave you a good introduction and some pointers to look for when you start with data modeling.


Below I found theÂ [Best Practices for Data Modeling](https://www.spiceworks.com/tech/big-data/articles/what-is-data-modeling/#_003), which guides you through some of the critical steps from one, designing the data model to eleven, verifying and testing the application of your data analytics:

1. Design the data model for visualization
2. Recognize the demands of the business and aim for relevant results
3. Establish a single source of truth
4. **Start with simple data modeling**Â and expand later
5. Double-check each step of your data modeling
6. Organize business queries according to dimensions, data, filters, and order
7. Perform computations beforehand to prevent disputes with end customers
8. Search for a relationship rather than just a correlation
9. Using contemporary tools and methods
10. Enhanced data modeling for improved business results
11. Verify and test the application of your data analytics


Another excellent best practice for dbt can be found inÂ [How to Write a High-Quality Data Model From Start to Finish Using dbt](https://airbyte.com/blog/dbt-data-model)Â byÂ [Madison](https://airbyte.com/blog-authors/madison-schott)Â or applying dimension model with Kimball and dbt inÂ [Building a Kimball dimensional model with dbt](https://docs.getdbt.com/blog/kimball-dimensional-model)Â ([GitHub](https://github.com/Data-Engineer-Camp/dbt-dimensional-modelling)) byÂ [Jonathan](https://www.linkedin.com/in/jonneo/).


## The Future of Data Modeling


As Iâve delved into the intricacies of data modeling in the previous parts of this series, itâs clear that weâre witnessing a revolution in the way we perceive, manage, and interact with data. The digital age is characterized by information overload, and data modeling provides the framework to harness this data and transform it into valuable insights.


Reflecting on the future of data modeling, I canât help but feel a sense of optimism mixed with anticipation. Itâs thrilling to envision a world where data-driven decisions are the norm rather than the exception, and I genuinely believe weâre on the right track.


Emerging technologies like AI and machine learning promise to streamline further and automate the process of data modeling. Thereâs potential for AI to take on a more active role in data modeling, translating complex business logic into coherent data structures.


This vision, however, doesnât mean we can become complacent. Itâs more crucial than ever for data professionals to stay on top of evolving industry trends and techniques. And then, thereâs the matter of the various data modeling tools available. The future will likely expand the number of open-source and proprietary options. But at the end of the day, selecting the right tool will always come down to your specific requirements, constraints, and the nature of your data.


We also must remember the importance of data architecture patterns. As data grows in volume and complexity, finding the most suitable architecture becomes increasingly critical. The choice between batch vs. streaming or data lake vs. data warehouse could significantly impact your data modeling efforts. So decisions around implementing a semantic layer, opting for a modern/open data stack, or navigating between centralized and decentralized patterns.


As I wrap up this series of data modeling, I encourage you all to keep learning, experimenting, and pushing the boundaries of whatâs possible with your data. Remember, the essence of data modeling is simplicity, no matter how complex the underlying data might be. The future of data modeling is constant change. But one is inevitable; it will be critical for every company. Iâm excited to see how the field evolves and how we, as data practitioners, continue to drive this evolution :).


## Learning more about Data Modeling


Below are some resources and helpful comments I gathered from you all; thank you for the valuable feedback throughout writing this article.


### Resources

- MongoDB Courses and Trainings, offering comprehensive guides to understanding and mastering MongoDB.Â [Link](https://learn.mongodb.com/courses/m320-mongodb-data-modeling)
- Book: “Agile Data Warehouse Design: Collaborative Dimensional Modeling, from Whiteboard to Star Schema” by Lawrence Corr. This is a foundational text for understanding dimensional modeling in an agile context.Â [Link](https://www.amazon.com/Agile-Data-Warehouse-Design-Collaborative/dp/0956817203)
- Book: “Data Warehouse Blueprints: Business Intelligence in der Praxis” by Dani Schnider, Claus Jordan, Peter Welker, and Joachim Wehner. This is an excellent resource for German speakers.Â [Link](https://www.amazon.com/Data-Warehouse-Blueprints-Business-Intelligence-ebook/dp/B01M0YX6AS/)
- Book: “[Data and Reality](https://www.amazon.com/Data-Reality-Perspective-Perceiving-Information/dp/1935504215)” - a timeless guide to data modeling, recommended byÂ [Jenna Jordan](https://twitter.com/JennaJrdn).
- Video: “Data Modeling in the Modern Data Stack” - a valuable resource for understanding the current state of data modeling.Â [Link](https://youtu.be/IdCmMkQLvGA)
- Article: “Introducing Entity-Centric Data Modeling for Analytics” on Preset - a good read for understanding an entity-centric approach to data modeling.Â [Link](https://preset.io/blog/introducing-entity-centric-data-modeling-for-analytics/)
- Website:Â [AgileData.io](http://agiledata.io/)Â by Shane Gibson - a resource for reducing the complexity of managing data for Leaders, Analysts, and Consultants.Â [Link](https://agiledata.io/)
- Podcasts: “Shane Gibson - Making Data Modeling Accessible - The Joe Reis Show” on Spotify.Â [Link](https://open.spotify.com/episode/4DNyy4cIttEFMUEWjKEHqV?si=df46c60e7d334e0e)


### Helpful comments

- Use well-defined ontologies that describe your business and relationships between components using common industry concepts, as suggested by Rayner DÃ¤ppen.Â [Link to comment](https://www.linkedin.com/feed/update/urn:li:activity:7044294859238567936?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7044294859238567936%2C7044383659683926016%29)
- Keep your data models updated, aligned, documented, validated, and verified with the business. This will ensure the models accurately reflect the current state of the company.
- Consider where to build the semantic/metrics layer to allow for fast, interactive analytics/dashboards and how to make it available to multiple tools to avoid various definitions.Â [Link to comment](https://twitter.com/Triamus1/status/1638612934455599119)
- From “[Data Modeling in the Modern Data Stack](https://youtu.be/IdCmMkQLvGA)” - computation is now the expensive part of data modeling, not storage. A hybrid approach is often used in modern data stacks to balance complexity, computational cost, data redundancy, and adaptability.


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-modeling-for-data-engineering-architecture-pattern-tools-future/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Data Modeling](https://www.ssp.sh/tags/data-modeling/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
