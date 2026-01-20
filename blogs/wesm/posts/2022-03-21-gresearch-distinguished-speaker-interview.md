---
title: "An Interview with Wes McKinney"
summary: "Interview at G-Research Distinguished Speaker Series"
date: 2022-03-21T00:00:00
tags: ["interview", "transcript"]
slug: gresearch-distinguished-speaker-interview
word_count: 1116
source_file: transcripts/2022-03-21-gresearch-distinguished-speaker-interview.md
content_type: transcript
event: "G-Research Distinguished Speaker Series"
video_url: "https://www.youtube.com/watch?v=pqMu18dmEdM"
---

{{< video https://www.youtube.com/watch?v=pqMu18dmEdM >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this interview for the G-Research Distinguished Speaker Series, I discuss Apache Arrow and its role in the data science ecosystem. I explain my journey from creating pandas to co-creating Arrow as a shared infrastructure layer for data science. I cover how Arrow provides a language-independent columnar format that enables zero-copy data sharing between systems, reducing data serialization overhead. I discuss open-source community building, the relationship between Arrow and projects like Parquet for storage, and how Arrow has enabled performance improvements in tools like PySpark through vectorized pandas UDFs. The talk also touches on the future of data processing, including the potential for Arrow to power next-generation dataframe libraries and enable efficient data microservices architectures.

## Key Quotes

> "I found that I enjoyed building data analysis tools and especially building tools for other people." — Wes McKinney

> "One of the things that's interesting about it is for many users, it's a project that they won't even know that's there. That it can go into all of the projects that you use and make them better." — Wes McKinney

> "The Arrow project started as an effort to build a more future-proof computing infrastructure for libraries like pandas." — Wes McKinney

> "We built effectively a query engine in Python and C to power all of the analytics that pandas performs. And so, everything is custom-built for pandas." — Wes McKinney

> "The Arrow project is intended to provide a reusable and modular computing foundation to power the next generation of data frame libraries, as well as accelerating the current generation of tools, including pandas." — Wes McKinney

> "Open-source is extremely important because it's the most efficient way for the software to have an impact when you have a piece of permissively licensed open-source software that can become a dependency of other open-source projects, as well as commercial software projects." — Wes McKinney

> "Open-source really enables that rapid adoption and reduces the barrier to entry, so that you can pick up the software. If it meets your needs, you can add it as a dependency in your project and build on it." — Wes McKinney

> "There needs to be a software solution to bring together innovation in hardware acceleration and computing efficiency, so being able to process more data per kilowatt hour, basically reducing the carbon footprint of data processing." — Wes McKinney

## Transcript

**Wes McKinney:** The world is changing dramatically in terms of data processing and analytics. And I'm excited to share that with you. So, let's get started.

I'm going to start by introducing myself. I'm Wes McKinney. I'm the CTO and co-founder of Voltron Data and co-creator of the Apache Arrow open source project. Many people know me as the creator of the Python pandas project and I've been working on data tools and systems for Python since 2008.

I was initially building a set of tools for myself to make it possible for me to do data analysis, you know, what we now call data science in Python. And I found that I enjoyed building data analysis tools and especially building tools for other people.

So, I was able to turn that into an open source project and eventually to make it successful and build a community around it.

I'm here giving a presentation about the Arrow open source project. How it's related to improving performance and data access and computing in data science and across at the intersection of database systems and data science tools.

I think a lot of people are excited about the Arrow project but I think one of the things that's interesting about it is for many users, it's a project that they won't even know that's there. That it can go into all of the projects that you use and make them better. And so, that makes it, for me, even more exciting to have the opportunity to build a piece of technology that makes many projects in the broader data science ecosystem much faster and more efficient.

The connection between pandas, you know, very popular Python open source project, and this presentation today is that for me, the Arrow project started as an effort to build a more future-proof computing infrastructure for libraries like pandas.

You know, when we built the pandas project, so myself and the other core developers, we had to reinvent many of the things that we were doing. So, we had to reinvent a lot of things. So, we built effectively a query engine in Python and C to power all of the analytics that pandas performs. And so, everything is custom-built for pandas.

So, the Arrow project is intended to provide a reusable and modular computing foundation to power the next generation of data frame libraries, as well as accelerating the current generation of tools, including pandas.

I mean, it's a really exciting project. We're excited to be able to launch this in the future, including pandas.

I mean, open-source is extremely important because it's the most efficient way for the software to have an impact when you have a piece of permissively licensed open-source software that can become a dependency of other open-source projects, as well as commercial software projects.

And we do actively track the reverse dependencies of a project like Arrow. And so, now, there are hundreds of other open-source projects that have taken on the Arrow Python library, PyArrow as a dependency, for example.

Open-source really enables that rapid adoption and reduces the barrier to entry, so that you can pick up the software. If it meets your needs, you can add it as a dependency in your project and build on it.

And I think what we're really excited about, what I'm very excited about, is there's a lot of innovation that's been happening in recent times around hardware accelerators and new types of silicon, but there needs to be a software solution to bring together innovation in hardware acceleration and computing efficiency, so being able to process more data per kilowatt hour, basically reducing the carbon footprint of data processing.

But in order to unlock the value of that new hardware, we have to build a really compelling, unified software layer to make things really easy for the users to be productive and tightly integrated with programming languages like Python and R, and also tie everything very cleanly into the storage layers.

It's kind of the new generation of open data warehouses, as well as thinking about designing next-generation file formats to continue to improve the performance of data access and processing efficiency.