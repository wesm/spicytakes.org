---
title: "State Of Dev Ops Report"
description: "The State of DevOps Report is an annual report that uses a statistical analysis   of survey data to determine effective practices for software delivery   organizations. Its principal authors are Nicol"
date: 2019-05-29T00:00:00
tags: ["continuous delivery", "productivity"]
url: https://martinfowler.com/bliki/StateOfDevOpsReport.html
slug: StateOfDevOpsReport
word_count: 611
---


The State of DevOps Report is an annual report that uses a statistical analysis
  of survey data to determine effective practices for software delivery
  organizations. Its principal authors are [Nicole
  Forsgren](https://twitter.com/nicolefv), [Jez Humble](https://twitter.com/jezhumble?), and [Gene Kim](https://itrevolution.com/faculty/gene-kim/).


The report is based on surveys of tens of thousands of professional
  software developers.
  The survey consists of questions designed to identify components of a
  construct - something that can't be measured directly, such as organizational
  culture. In this case the constructs represent capabilities of a software
  delivery organization 1 such as practices (continuous integration) and
  environmental factors (team culture).
  For each construct survey questions are designed to identify these
  indirectly, so they don't ask âdo you do continuous integrationâ (which we
  know would give [very unreliable answers](https://martinfowler.com/bliki/ContinuousIntegrationCertification.html)), but
  instead ask for concrete things that are part of CI (eg âdoes everyone push to a
  shared mainline dailyâ).
  They then use a variety of statistical techniques to test if the questions in
  fact measure the underlying concept.
  Further analysis can then test hypothesis about how
  these constructs link together.


1: Software delivery is the process from when a developer
    completes work on a change to a software system, to when that change is
    deployed in production. It doesn't include figuring what changes are
    required and how the development team works on the change until it is done
    within the development environment.


One of the most striking results from this survey is how teams cluster into
  four standards of software delivery performance (elite, high, medium, and
  low). Elite performers deploy many times a day, taking under an hour to take a
  change completed by a developer into production. Low performers, in contrast,
  take months to deploy a change into production. This high throughput
  does not come at the cost of system stability, since elite teams have a change
  failure rate of less than 15% (compared to 46-60% for low performance teams)
  and can recover from a failure in minutes rather than weeks.


The best place to start reading more about this is the [2019 State of DevOps Report](https://research.google/pubs/pub48455/), which is freely available.
  For more depth on the results and the techniques used to discover them, I
  [strongly recommend](https://martinfowler.com/articles/accelerate-foreword.html) their book [Accelerate](https://www.amazon.com/gp/product/B07B9F83WM/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07B9F83WM&linkCode=as2&tag=martinfowlerc-20). 2


2: 
      The [Dora community](https://dora.community), although without the
      involvement of the original founders, continues this work.


## Four Key Metrics from 2019 report



|  | elite | high | medium | low |
| Deployment Frequency | on demand (> 1/day) | 1/hour to 1/day | 1/week to 1/month | 1-6 months |
| Lead Time | < 1 day | 1 day to 1 week | 1 week to 1 month | 1-6 months |
| Time to Restore | < 1 hour | < 1 day | < 1 day | 1 week to 1 month |
| Change Failure rate | 0-15% | 0-15% | 0-15% | 46-60% |



The report clustered the surveyed organizations based
    on similarities in the four key metrics.

- **Deployment Frequency:** how often the team deploys code to production
- **Lead Time:** time from code committed to code successfully
      running in production
- **Time to Restore:** time to restore service when a defect occurs
- **Change Failure Rate:** what percentage of changes result in problems that require remediation


## Notes


1: Software delivery is the process from when a developer
    completes work on a change to a software system, to when that change is
    deployed in production. It doesn't include figuring what changes are
    required and how the development team works on the change until it is done
    within the development environment.


2: 
      The [Dora community](https://dora.community), although without the
      involvement of the original founders, continues this work.
