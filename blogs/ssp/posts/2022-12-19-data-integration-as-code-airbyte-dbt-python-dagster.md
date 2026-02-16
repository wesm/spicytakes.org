---
title: "Data Integration as Code: Configuring Airbyte and dbt with Python (Dagster)"
date: 2022-12-19
url: https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/
slug: data-integration-as-code-airbyte-dbt-python-dagster
word_count: 1924
---

![Data Integration as Code: Configuring Airbyte and dbt with Python (Dagster)](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/airbyte-dagster-feature-code.jpg)

Contents

I tried the newÂ [Dagster](https://glossary.airbyte.com/term/dagster)Â feature to configure the Airbyte withÂ **Python code**. Why would you want to do that, and what is the difference between usingÂ [Octavia CLI](https://github.com/airbytehq/airbyte/tree/master/octavia-cli)Â with the YAML configurations?


This feature allows for the dynamic creation of Airbyte sources, destinations, or connections depending on external factors such as changing API inputs, files that change (event-driven approach), or anything else that is not static.


I created a short demo where I scraped theÂ [Awesome Data Engineering List](https://github.com/igorbarinov/awesome-data-engineering)Â links withÂ [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)Â and ingested the stars from each GitHub repository to a Postgres databaseâseeing the trends for each. We could add any other excellent list and scrape all awesome lists from GitHub if we wanted to.

Code available on GitHub
The code to all of here shown you find on theÂ
[Open Data Stack](https://github.com/airbytehq/open-data-stack/)
Â project underÂ
[dagster](https://github.com/airbytehq/open-data-stack/tree/main/dagster)
.

## When to use it?


When to use this pythonic configuration? With our Octavia CLI, as explained in theÂ [version control Airbyte configurations](https://airbyte.com/tutorials/version-control-airbyte-configurations)Â article, you can import, edit, and apply Airbyte application configurations based on YAML files. These can be checked into git and automatically be used, as shown in the article.


What now if you are dependent on incoming metadata that can? If the configs are not hard coded, you’d need a script on top to generate the configurations dynamically. Dagster as a Python orchestrator implemented this, plus they created wrappers on top of theÂ [source](https://docs.airbyte.com/integrations/#sources)Â andÂ [destination](https://docs.airbyte.com/integrations/#destinations)Â connectors.


For example, in my demo, I used theÂ [GithubSource](https://github.com/dagster-io/dagster/blob/master/python_modules/libraries/dagster-airbyte/dagster_airbyte/managed/generated/sources.py#L5629), which provides all configurations that theÂ [Airbyte GitHub Source](https://docs.airbyte.com/integrations/sources/github)Â has to configure with Python, and the same forÂ [PostgresDestination](https://github.com/dagster-io/dagster/blob/ef723a6569224278c4208f9e5a16a26aded97a79/python_modules/libraries/dagster-airbyte/dagster_airbyte/managed/generated/destinations.py#L2391). TheÂ [AirbyteConnection](https://github.com/dagster-io/dagster/blob/master/python_modules/libraries/dagster-airbyte/dagster_airbyte/managed/types.py#L228)Â sets configure both together as a connection in Airbyte.


These features open instrumental use cases forÂ **data integration as code**. Imagine you need to provision Airbyte, have multi-tenancy requirements for teams or customers, or read from a dynamic API (imagine the Notion API where the content is nested into the databases and constantly evolves). Based on these configs, you can automatically apply new sync based on the latest status. Everything is versioned, which leads to changes with confidence.


## How does it work


So much for when to use it. Let’s explore now how it all works.


Dagster offers the interfaces that we can define our Airbyte connections with Python and a command line tool calledÂ [dagster-airbyte](https://github.com/dagster-io/dagster/blob/master/python_modules/libraries/dagster-managed-elements/dagster_managed_elements/cli.py)Â that allows two functions to check or apply the defined connections to the Airbyte instance.


As the name suggests, checking is verifying against the current live Airbyte instance vs. your pythonic configurations. Apply will delete an existing source, destination, and connection and re-apply based on your updated configs.

Skipping Postgres Setup
Below, I will skip the step on setting up Airbyte and Postgres database; You can find that in theÂ
[ReadMe](https://github.com/airbytehq/open-data-stack/tree/main/dagster/readme.md)
Â orÂ
[Postgres Replication Tutorial](https://airbyte.com/tutorials/postgres-replication)
.

## Configure Airbyte Connections in Python


For myÂ [demo](https://github.com/airbytehq/open-data-stack/tree/main/dagster), I am scraping a GitHub repo that is evolving.


### Define Airbyte Instance


First, I define the airbyte instance in my dagster python code:



| `1
2
3
4
5
6
7
8
` | `airbyte_instance = airbyte_resource.configured(
    {
        "host": "localhost",
        "port": "8000",
        "username": "airbyte",
        "password": {"env": "AIRBYTE_PASSWORD"},
    }
)
` |


Setting ENV Variable
Make sure you set the environment variableÂ
Â on your laptop. The default password is password. As well asÂ
[create](https://github.com/settings/tokens)
Â a tokenÂ
Â for fetching the stargazers from the public repositories in the below code.

### Define Airbyte GitHub Source


After we create our Airbyte source with:



| `1
2
3
4
5
6
7
` | `gh_awesome_de_list_source = GithubSource(
    name="gh_awesome_de_list",
    credentials=GithubSource.PATCredentials(AIRBYTE_PERSONAL_GITHUB_TOKEN),
    start_date="2020-01-01T00:00:00Z",
    repository=get_awesome_repo_list(),  # The magic happens here
    page_size_for_large_streams=100,
)
` |



#### Web Scraping GitHub List with Beautiful Soup


TheÂ `get_awesome_repo_list()`Â could be any arbitrary Python code. In this demo, this function does web scraping with Beautiful Soup from the awesome repo list. Note: I limited it to 10 items for this demo case.



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
` | `def get_awesome_repo_list() -> str:

    url = "https://github.com/igorbarinov/awesome-data-engineering"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    # parse all links into a list starting with github.com
    links = [
        link.get("href")
        for link in soup.find_all("a")
        if link.get("href").startswith("https://github.com")
    ]
    # remove links that start with url
    links = [
        link
        for link in links
        if not link.startswith(url) and not link.endswith("github.com")
    ]
    # remove last slash if there
    links = [link[:-1] if link.endswith("/") else link for link in links]
    # remove repos without organization
    links = [link for link in links if len(link.split("/")) == 5]
    # check if links are still existing in parallel to save time
    existings_links = asyncio.run(check_websites_exists(links))
    # remove `https://github.com/` from links
    links = [link.replace("https://github.com/", "") for link in existings_links]

    # due to timeout limits while airbyte is checking each repo, I limited it here to make this demo work for you
    links = links[0:10]

    # return links as a string with blank space as separator
    return " ".join(links)
` |



### Define Airbyte Postgres Destination


And the destination with:



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
` | `postgres_destination = PostgresDestination(
    name="postgres",
    host="localhost",
    port=5432,
    database="postgres",
    schema="public",
    username="postgres",
    password=POSTGRES_PASSWORD,
    ssl_mode=PostgresDestination.Disable(),
)
` |



### Define Airbyte Connection


When we have both source and destination, we can merge them in an Airbyte connection where we specify the tables we sync with stream_config; in our demo case, we only need the tableÂ `stargazers`. Other configurations can be set, such asÂ [Airbyte Sync Modes](https://docs.airbyte.com/understanding-airbyte/connections/#sync-modes)Â andÂ [Normalization](https://docs.airbyte.com/cloud/core-concepts#normalization).



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
` | `stargazer_connection = AirbyteConnection(
    name="fetch_stargazer",
    source=gh_awesome_de_list_source,
    destination=postgres_destination,
    stream_config={"stargazers": AirbyteSyncMode.incremental_append_dedup()},
    normalize_data=True,
)

#We'll supply our new connection to the reconciler we defined above:
airbyte_reconciler = AirbyteManagedElementReconciler(
    airbyte=airbyte_instance,
    connections=[stargazer_connection],
)
` |



### Applying Airbyte Configuration to Instance


As we defined the necessary Airbyte source, destination, and connection, we will apply it to the Airbyte instance withÂ `dagster-airbyte`Â as follow:



| `1
` | `dagster-airbyte check --module assets_modern_data_stack.assets.stargazer:airbyte_reconciler
` |



The output might look something like this:



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
` | `Found 1 reconcilers, checking...

Changes found:
+ gh_awesome_de_list:
  + page_size_for_large_streams: 100
  + repository: sindresorhus/awesome rqlite/rqlite pingcap/tidb pinterest/mysql_utils rescrv/HyperDex alticelabs/kyoto iondbproject/iondb pcmanus/ccm scylladb/scylla filodb/FiloDB
  + start_date: 2020-01-01T00:00:00Z
  + credentials:
    + personal_access_token: **********
+ postgres:
  + schema: public
  + password: **********
  + database: postgres
  + host: localhost
  + port: 5432
  + username: postgres
  + ssl_mode:
    + mode: disable
+ fetch_stargazer:
  + destination: postgres
  + normalize data: True
  + destination namespace: SAME_AS_SOURCE
  + source: gh_awesome_de_list
  + streams:
    + stargazers:
      + syncMode: incremental
      + destinationSyncMode: append_dedup
` |



After theÂ checkÂ identified the changes between our configurations in Python with the Airbyte instance, we canÂ applyÂ these changes with the following:



| `1
` | `dagster-airbyte apply --module assets_modern_data_stack.assets.stargazer:airbyte_reconciler
` |



The output might look something like this:



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
` | `Found 1 reconcilers, applying...

Changes applied:
+ gh_awesome_de_list:
  + start_date: 2020-01-01T00:00:00Z
  + repository: sindresorhus/awesome rqlite/rqlite pingcap/tidb pinterest/mysql_utils rescrv/HyperDex alticelabs/kyoto iondbproject/iondb pcmanus/ccm scylladb/scylla filodb/FiloDB
  + page_size_for_large_streams: 100
  + credentials:
    + personal_access_token: **********
+ postgres:
  + username: postgres
  + host: localhost
  + password: **********
  + port: 5432
  + database: postgres
  + schema: public
  + ssl_mode:
    + mode: disable
+ fetch_stargazer:
  + destination: postgres
  + normalize data: True
  + destination namespace: SAME_AS_SOURCE
  + source: gh_awesome_de_list
  + streams:
    + stargazers:
      + destinationSyncMode: append_dedup
      + syncMode: incremental
` |



### Verify generated components in Airbyte UI


Let’s look at the Airbyte UI before we apply anything.


![/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/airbyte-empty-before-dagster-apply.png](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/airbyte-empty-before-dagster-apply.png)

*Before I applied the changes, only my manual added connections.*


After applying the changes,Â `fetch_stargazer`Â popped up with its corresponding GitHub source and Postgres destination.


![/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/airbyte-source-destination-connection.png](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/airbyte-source-destination-connection.png)

*After we applied the Dagster Python configurations*

Equivalent to using GUI
This is equivalent to going into the Airbyte UI and setting up the source and destination with clicks.

## Set up Dagster Software Defined Assets


[Software-Defined Asset](https://glossary.airbyte.com/term/software-defined-assets)Â in Dagster treats each of our destination tables from Airbyte as aÂ [Data Product](https://glossary.airbyte.com/term/data-product)âenabling the control plane to see the latest status of eachÂ [Data Asset](https://glossary.airbyte.com/term/data-asset/)Â and its valuable metadata.


We can set them up with a little bit of code in Dagster. As we created the Airbyte components with Dagster already, Dagster has all the information already:



| `1
2
3
4
5
` | `airbyte_assets = load_assets_from_connections(
    airbyte=airbyte_instance,
    connections=[stargazer_connection],
    key_prefix=["postgres"],
)
` |



The same we do for our dbt project that is underÂ [dbt_transformation](https://github.com/airbytehq/open-data-stack/tree/main/dagster/dbt_transformation). The dbt projects create aÂ `mart_gh_cumulative`Â view on top of our replicated GitHub tables, which we can visualize with Metabase later. But first, let’s define the dbt assets simply by pointing them to the dbt folder:



| `1
2
3
` | `dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR, io_manager_key="db_io_manager", key_prefix="postgres"
)
` |



When we start Dagster UI called Dagit with:



| `1
2
3
` | `cd dagster/stargazer/
pip install -e ".[dev]"
dagit
` |



We should see the asset view.


![/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/dagster-airbyte-asset-metadata-schema.png](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/dagster-airbyte-asset-metadata-schema.png)

*Global Asset Lineage Graph with integrated Metadata, e.g., table_schema of Airbyte*


You see the Global Asset Lineage view in Dagster based on our generated Airbyte connection and dbt models creating views. On the right-hand side, you see the metadata that Dagster fetches, e.g., for Airbyte, the schema of each table, and for dbt, the generated SQL statement:


![/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/dagster-dbt-asset-metadata-sql.png](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/dagster-dbt-asset-metadata-sql.png)

*Global Asset Lineage Graph with integrated Metadata, e.g. raw SQL of dbt*


Next, we can run the assets defined.


## Run Airbyte and dbt Assets with Dagster


If we now hit the button âMaterialize allâ, Dagster will run our sync, fetching the stargazer for all repositories from GitHub, which dynamically fetch what we defined inÂ `get_awesome_repo_list()`.


Suppose you head over to the Airbyte UI after materializing the Dagster assets. The log will look something like the one below. It will take a while due to the rate limit of GitHub.


When finished, the dagster job will look like this:


Including theÂ dbt runÂ that Dagster triggered for us:


And more interestingly, the Global Asset Lineage with the latest run information:


And finally, Airbyte UI finished successfully too as we can see below.


## Starting up Metabase and see Dashboard


When we start Metabase as described in theÂ [Readme](https://github.com/airbytehq/open-data-stack/blob/main/visualization/metabase/readme.md)Â and head over to a straightforward dashboard, we can see the imported stars over the two-year timeline.


![/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/metabase-dashboard-stargazer.png](https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/images/metabase-dashboard-stargazer.png)

*Metabase Dashboard that points to dbt viewmart_gh_cumulative, which accumulates the stars per month over time.*

Metabase Dashboard
In the dashboard image, I replicatedj all 79 linked GitHub repos. For the sake of the demo and to avoid time-outs, I limited it to 10. But you can permanently remove that limitation.

## Wrapping Up


Weâve seen how the new capabilities of Dagster can streamline traditional software engineering practices, such as testing and version control, to data integration with Airbyte.


The Pythonic definition of all Airbyte components opened the pandora box for more even-based use cases orchestrated by Dagster.


Ben from Dagster implemented a similar project usingÂ [Data Integration as Code](https://youtu.be/JD0SNuihY-w); check it out. I also thank Ben for his support while trialing these new experimental features myself.


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/data-integration-as-code-airbyte-dbt-python-dagster/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[Yaml](https://www.ssp.sh/tags/yaml/)
[Airbyte](https://www.ssp.sh/tags/airbyte/)
[Dagster](https://www.ssp.sh/tags/dagster/)
[Dbt](https://www.ssp.sh/tags/dbt/)
[Metabase](https://www.ssp.sh/tags/metabase/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
