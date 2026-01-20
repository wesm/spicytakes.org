---
title: "Joining Forces for an Arrow-Native Future"
date: 2021-08-05T00:00:00
tags: ["work", "apache arrow"]
slug: from-ursa-to-voltrondata
word_count: 518
source_file: blog/from-ursa-to-voltrondata/index.qmd
content_type: blog
---

#### Joint Post from Wes McKinney and Josh Patterson

#### *Allow us to reintroduce ourselves*

Too often people say "let’s do something together" in passing, and
don’t. There's the occasional inter-project collaboration, but rarely will
people take that next step. There are countless reasons why this happens, and
aligning goals is challenging to say the least. But after spending the last
several years working separately on related problems in the data ecosystem, we
realized our best hope to make lasting progress was to build a stronger,
unified foundation. We needed to do something radically different.

## A Brief History

[Wes](https://twitter.com/wesmckinn) helped start the Apache Arrow project in
2015, and since then has continued to build a developer community to achieve
Arrow’s dual goals. The first goal is to be an efficient, language-independent
open standard for columnar data interchange. The second goal is to be a
portable, high-performance computing foundation for doing analytics on that
columnar data. To pursue these goals, Wes formed [Ursa
Labs](https://ursalabs.org/) in 2018 and [Ursa
Computing](https://ursalabs.org/blog/ursa-computing/) in 2020.

In parallel, [Josh](https://twitter.com/datametrician) and colleagues at NVIDIA
foresaw the potential of GPUs to accelerate analytics workloads. In 2017, they
created the [GPU Open Analytics
Initiative](https://developer.nvidia.com/blog/goai-open-gpu-accelerated-data-analytics/)
and later RAPIDS, which has demonstrated the potential of accelerated
high-performance columnar analytics. Josh and the cuDF developers collaborated
extensively with [BlazingSQL](https://www.blazingsql.com/) to bring
GPU-accelerated Arrow analytics not only to the Python community, but to modern
SQL workloads as well.

Over the last 5 years, Arrow has been rapidly adopted as the gold standard for
tabular data interchange across the data warehousing and data science
ecosystems, bringing massive performance and efficiency improvements to many
use cases. Arrow is also taking Flight ([pun
intended](https://arrow.apache.org/blog/2019/10/13/introducing-arrow-flight/))
as a replacement for slow database access protocols like ODBC and JDBC. These
organizations worked across numerous projects, but individually, each only
addressed some of the community's needs.

## United Foundation

The next stage of growth is to see Arrow adopted not only as the standard for
fast data movement but also as the native format for cost-effective analytical
computing. We envision a ubiquitous, hardware-optimized foundation that
simplifies and accelerates data analytics workloads across programming
languages.

Today, we are launching a new company, [Voltron Data](https://voltrondata.com),
that reflects this unified vision. The Ursa Computing and BlazingSQL teams
together with pioneers of RAPIDS and other open-source projects have joined
forces to form Voltron Data. Additionally, Ursa Labs is now [Voltron
Labs](https://voltrondata.com/labs), and it will continue to work for the
benefit of the open-source ecosystem around Apache Arrow. Josh and Wes are now
Voltron Data’s CEO and CTO, respectively. You’ll see us doing even more work in
the Arrow community than we have in the past, and we look forward to increasing
Arrow’s footprint in the world. Together we are unifying our collective
expertise in performance, portability, and programmability to build more
bridges across the data ecosystem to improve the tools you know and love.

We look forward to sharing more about Voltron Data in the coming months. In the
meantime, we have [many open roles](https://voltrondata.com/careers) and are
looking for talented software engineers around the globe to further our
mission. [Join us!](https://voltrondata.com/careers)