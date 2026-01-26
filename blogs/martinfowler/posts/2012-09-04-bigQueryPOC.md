---
title: "A Proof-of-Concept of BigQuery"
description: "Can Googleâs newBigQueryservice give customers Big Data analytic     power without the need for expensive software or new     infrastructure? Thoughtworks and AutoTrader conducted a weeklong     pro"
date: 2012-09-04T00:00:00
tags: ["data analytics"]
url: https://martinfowler.com/articles/bigQueryPOC.html
slug: bigQueryPOC
word_count: 1366
---


Google recently upgraded its enterprise offerings with an
    improved version of Google App Engine and some new tooling. Google
    BigQuery is the new online service for running interactive queries
    over vast amounts of dataâup to billions of rowsâwith great speed.
    Itâs good for analyzing large quantities of data quickly, but not
    for modifying it. In data analysis terms, BigQuery is an OLAP
    (online analytical processing) system, aimed at helping
    organisations work with Big Data.


We were very interested in putting this technology to the test,
    so we searched for a partner with a data set worthy of the label
    âBigâ. One of our clients in the UK, AutoTrader, had both Big Data
    and a business issue that they hoped to see if BigQuery could help
    them with.


[AutoTrader](http://www.autotrader.co.uk/) is the top-ranked online site to buy and sell new
    and used cars in the UK, and also publishes a weekly classified ad
    magazine. Two questions a dealer wants to know the answer to when
    a used car comes onto the lot are: how much to offer for it; and
    how long it might take to sell it. The answers lie within
    AutoTraderâs historical data.


We borrowed data from AutoTrader covering all ads placed on
    their website over the last five years, including how long the ad
    was displayed and the price of the vehicle when it was removed
    from the site (the assumption being that was the selling price of
    the vehicle). The test data set contained over 750 million rows,
    and had been uploaded to Amazonâs EC2.


## Getting the data into BigQuery


Dealing with Big Data, file size limits are an issue. We used
      the Unix command line 'split' to break the data file into chunks
      of the right size, taking care to break files apart on line
      boundaries rather than the middle of a record. Both Google Cloud
      Storage (GCS) limits and the BigQuery import limits have to be
      considered when doing this.


As soon as we had Googleâs GCS command line tool [gsutil](https://developers.google.com/storage/docs/gsutil)
      successfully installed, we used it to move the data from Amazon
      into GCS, which turned out to be the slowest part of the whole
      process. The total rows took around 12 hours to transfer to GCS.
      We tried using the parallel upload facility in gsutil but this
      just led to our EC2 instance becoming I/O bound. With hindsight,
      we could have spent more time experimenting with Amazon regions,
      file sizes and parallel uploads to make this process quicker.


With the data in GCS, we next created a very simple text file
      to represent the schema and used it with the Big Query command
      line tool ([bq](https://developers.google.com/bigquery/docs/cli_tool)) to set up tables in BigQuery. We checked it out
      first with a small subset of the data, doing a few queries from
      the BigQuery [web console](https://bigquery.cloud.google.com) to be sure everything was suitable
      before we loaded the whole dataset.


The next stage was to complete the transfer from GCS into the
      newly defined BigQuery database. Because of the problems we ran
      into with parallel uploads into GCS from our source on Amazon,
      we didnât try to use the parallel facility for the load into
      BigQuery. Later we found we could have done this and probably
      cut our 8 hour transfer time down to around 15 minutes.


Once we had all the data uploaded we tried a few queries. At
      the start, these were very slow, perhaps to do with some
      internal distributions not having happened inside of BigQuery.
      Initially these queries were taking a few minutes, but the next
      morning things took around 7 to 10 seconds and this remained
      reasonably consistent for the remainder of the exercise.


## Creating Big Data web analytics using BigQuery and Google Charts


We decided to use [Google App Engine](https://developers.google.com/appengine/) to create a simple web
      front-end to our queries, with [Google Charts](https://developers.google.com/chart/) embedded for
      interactive visualisation of the output.


Our web pages made RESTful calls to our App which in turn
      used the Java Big Query API (Python is an option as well) to
      make RESTful calls to invoke queries on the data. The results
      were then rendered client-side using the Google Charts
      libraries. In addition to the interactive charts, we were able
      to add a simple export mechanism, taking advantage of the fact
      that BigQuery results are saved into a temporary table which can
      be accessed via a âjob IDâ. This makes for a very simple and
      quick way to export the results of queries into GCSâand hence
      into other Google tools or as a CSV file. All of this was
      secured via OAUTH giving us fine-grained control over who could
      see, access and invoke queries using the App.


We began looking into changing our web app to use
      asynchronous mechanisms for invoking BigQuery, but ran out of
      time. That said, it looked pretty straightforward, using the
      jobID to query for intermediate results. Given the chance again,
      we would go with an asynchronous approach from start.


## Conclusions and benefits


Overall we were impressed with what we were able to achieve
      in a short amount of time with BigQuery, the APIs and utilities.
      We were able to experiment with different ways of visualising
      and querying a very large volume of data with a relatively low
      investment in terms of time and without needing expensive
      infrastructure.


For organisations longing to gain insights into very large
      datasets, BigQuery could be a viable option that requires no
      purchases of specialised software or additional infrastructure.
      Even for organisations that already have an enterprise data
      warehouse, BigQuery is an option for testing out theories, or
      for other instances where the keepers of the data warehouse
      place restrictions on use.


## Issues and Lessons


We encountered issues during the proof of concept that others
      can learn from.


### Installing the Google utilities


Make sure the right version of Python is installed, and
        multiple versions are not on the path, to avoid issues. We
        found it best to use the downloadable versions of the tools,
        as our early attempt, trying to use easy_install with an older
        version of python caused a lot of problems.


### Google codebase examples


It proved actually quite difficult to find some working
        Java examples of BigQuery used from within App Engine,
        especially around the OAUTH mechanisms. But once we'd created
        a few classes to handle the work, we had no further issues,
        even with a four-stage redirect (as Thoughtworks uses its own
        corporate OAUTH mechanism with Google apps). Some more thought
        would be needed to make these mechanisms work with something
        like webdriver and automated acceptance tests.


### Charts and BigQuery have slightly different JSON
        formats


Another issue is that the JSON format returned from
        BigQuery is slightly different from the one Charts expects.
        While there are good reasons for this, having Charts able to
        directly consume some of the JSON would have cut the amount of
        code we had to create.


### Timestamps were a problem


Our data included timestamps in a non-standard format (from
        the Google toolâs perspective). This made it difficult to
        construct queries that selected by time periods. While we were
        able to work around this, it did limit some of what we'd hoped
        to do with the data. We've passed this along to the BigQuery
        team and expect they'll have some more flexibility around
        date/time formats in the future.


### Use the web console


While experimenting we found the BigQuery web console
        invaluable for trying out queries before adding them into the
        code.


### Experiment with gsutil and bq parallel loading


While we encountered I/O issues loading from Amazon to GSC, we
        later found we could have saved many hours by using the parallel load
        from GCS into BigQuery itself. It is worth testing the various options
        available with gsutil and bq to see which give the best performance
        for your environment.


### Watch your data usage as you execute queries and develop
        with small datasets


If you are doing a lot of testing of a full dataset, you can get
        into several or more terabytes of data usage, which can generate a
        high charge. Queries come back so fast, you forget that return sets
        can be many gigabytesâand they add up fast.


---
