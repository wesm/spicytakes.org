---
title: "Will we ever have clean data?"
subtitle: "Probably not, but maybe we can work with messy data."
date: 2023-07-28T17:17:13+00:00
url: https://benn.substack.com/p/will-we-ever-have-clean-data
slug: will-we-ever-have-clean-data
word_count: 2061
---


![undefined](https://substackcdn.com/image/fetch/$s_!kGZl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8777e48-a0bb-4794-a621-916ea05f8cf7_1920x2179.jpeg)

*You gotta work smarter, not harder,my man.*


There are two types of people in the data industry. The first are the starry-eyed optimistswho are hypnotizedby possibility and promise. Theyignore the ugly realitieson the ground—messy data, mismatched dashboards, broken pipelines, the three thousand single-tenant Db2 databases that are four versions behind and running in a data center thatJeffset up in Milpitas—and insteadimagine what might beover the horizon. They marvel at every release from OpenAI; they see the potential in every new open-source framework; theywrite blog poststhat sketch out some beautiful and impossible future by recklessly hand-waving past how things really work.


The second group are the cynics who like to remind the first group of how things really work. All of these ideas are just hype for a hypothetical world,they say. We need quality; we need reliability; fine, dream big, but withstable infra. Garbage in, garbage out. Your insights are only as good as your data.Your SQL chatbot won’t work.They’ve toiled in the trenches; debugged a revenue dashboard twenty minutes before a board meeting; migrated enterprise clients off of and back onto Oracle;seen things you people wouldn’t believe. They’ve walked through the valley of the shadow of death, and fear no evil—only Jeff.


This week, the latter groupgot a new tool:


> SDF is a compiler and build system that leverages static analysis to comprehensively examine SQL code at warehouse scale. By considering all queries in any dialect simultaneously, SDF builds a rich dependency graph and provides a holistic view of your data assets, empowering you to uncover problems proactively and optimize your data infrastructure like never before.The standout feature of SDF is its ability to annotate your SQL sources with rich metadata and reason about them together. SDF metadata can range from simple types and classifiers (PII) to table visibility and privacy policies (Anonymize). When SDF performs its static analysis, it takes this metadata into account, propagates it throughout your SQL sources withInformation Flow Theory, and enforces built-in and user-defined rules. We call these Checks. Here are some simple examples of powerful SDF Checks:Check Data Privacy: Ensure all personally identifiable information (PII) is appropriately anonymizedCheck Data Ownership: Guarantee every table has an owner (a staple of GDPR)Check Data Quality: Prevent different currency types from combining in calculations (e.g. preventing £ + $ )


Excellent; we all love these things. Do I want easy ways to anonymize PII?For sure.Do I want to violate some GDPR policy and have Europolput me in a roomthat’s too short to stand up in and not wide enough to lie down in? Nope. Do I worry about accidentally summing dollars and yen and overstating our revenue by14,000 percent? Not really, though I bet big companies do, and they spend a lot more money on data infrastructure than me.


But do these features address the underlying problems that make data so unwieldy to work with? Mostly, no. Companies’ data infrastructures—including those at many young startups—are often terminally messy, full of brittle scripts, manually updated CSVs, and “pipelines” that involve transferring an Excel file from one computer to another with a USB drive.1Like most other products that are roughly related to data quality and reliability, tools like SDF can help us find and debug the inevitable problems that emerge from this unworkable stack, but they don’tfixthem. They’re small improvements at the edges,dwarfedby the scale of the problem, anointment for a cannonball woundor a painkiller for a cancer patient: Useful, potentially worth a lot of money and ultimately, more of a temporary comfort than a lasting cure.


To be clear, this isn’t a criticism of SDF, which doesn’t claim to solve these problems, or of any other similar tool. Data observability; data contracts; even “semantic linters” like SDF—I’d rather manage a data stack that had all of these things than one that didn’t. And for SDF specifically, I’m sure their initial launch is just the beginning, with more to come.2


Instead, it’s a question about why this keeps happening. Why do we keep feeding data reliability products into the maw of the problem they’re trying to solve? Why have hundreds of very smart people spent thousands of hours and millions of dollars on data quality tooling, and most of us still can’t even make trustworthy dashboards? Why is this so hard?


After thinking about it for hours—hours!—I have my guess.


# Data quality is a tradeoff


When people talk about data quality and reliability, they often implicitly frame it as an unambiguous fight against entropy. We win if we’re persistent, prudent, disciplined, and thoughtful; we lose if we are lazy, reckless, inattentive, or foolish. But we would never lose because wechoseto.


I’m not so sure that’s true. Though we’d never quite characterize it this way, I think a lot of data teams implicitlyand reasonablychoose disorder and disorganization.


Consider how a company builds out their data infrastructure. They start with a few basic pipelines that power a handful of simple reports and dashboards. The business grows; more functions need more reporting; some marketing project unexpectedly catches fire and data tooling has to rapidly expand to support it; some partner initiative fails and a data sharing program gets axed. In hindsight, the Frankenstein stack that gets created—planned one step at a time, full of half-built experiments and partially-deprecated failures—looks like a huge mistake. But,just as true of analysis, the mess has a purpose:


> Because no company is the same, measuring a business, as was the case for us when we were measuring our win rates, is a creative process. Inevitably, even the best laid reporting plans give way to a lot of exploratory messes. Each potential metric produces a bunch of analyses to assess it; each analysis produces more questions and ad hoc offshoots. Multiply this by all the metrics and dashboards on your blueprint, and complicate it by constantly shifting the business underneath it, and the development process looks less like an organized construction site and more like anartist’s studioor awriter’s desk.


This dynamic actively works against a lot of our existing data quality tools. Those tools typically encourage a slow march towards stability—over time, data teams should gradually add more models, tests, policies, and contracts. But data and the things people create with it are often more dynamic than that (and, I’d suspect, more dynamic than the software systems that they’re borrowed from). A high-quality dataset is one that is consistent with the business concept it represents. Excluding the datasets that sit behind legally-defined financial metrics,3those business concepts are often fluid. New OKRs get spun up every quarter; projects take off or wind down; new data sources become urgent requirements as business initiatives change. Data teams have to absorb every change from every department they serve.


The good news, however, is that none of this is incompatible with data quality itself. We just have to imagine different ways to provide it. Instead of focusing on stability, for instance, are there ways to makeinstabilitysafer? Or, to take it even further, could we make things easier to refactor, and in fact, encouragemorerewrites?


Put differently, the modern data stack has created a number of cottage industries in its wake. One of them is for consultants to come in and reset the whole thing, by cleaning up data sources, tidying up dbt, consolidating metrics, and so on. For most companies, the day these consultants wrap up their job is probably the day their data is at its best, because it was designed for the business that exists in exactly that moment.


When consultants leave, companies have two choices: Try to move the business and its data in lockstep, or let them drift and make it easy to snap them back together when they do. I’m not convinced that the latter wouldn’t be easier to do.


How? I have no idea, but I can handwave some starry-eyed optimism at it.


# Data resiliency


Here’s a question related to messy data: How many dbt models is too many?


A thousand seems like a lot? Your average business doesn’t have that many metrics or entities to report on. At first glance, it seems crazy that a vanilla SaaS company or an ecommerce store that runs on Shopify would ever need anywhere near that many tables to describe and analyze their business.


But there are two reasons why dbt projects might get that big, or bigger. The first is boring—some source schemas are huge. Salesforce alone hasmore than 1,100 standard objectsin its application; if you want to query those, your dbt project can get big in a hurry.


The second reason is more interesting. When you’re trying to clean up a few raw tables into something useful—say, going from Salesforce accounts, opportunities, and opportunity line items to a table of something like customer contracts—there are often a lot of intermediate steps in that calculation. You have to join tables in one step, aggregate them in the second, join the aggregates in the third, apply a lag function to figure out when the account’s last contract ended in the fourth, dedupe in the fifth, and so on. These are the kinds of calculations that, if done in a single query, would probably happen in a series of CTEs. In dbt, however, it can make sense to pull each one (or some reasonable set of a few) out into their own models. This way, if you’re debugging this giant knot of logic, you can query that intermediate model directly. Or if it’s useful in other calculations, you can recycle it.


In this sense, dbt models can be akin to functions in a piece of software. You want them to beshort and non-repeating. To judge a dbt project by how many models it has is like judging a program by how many functions it has: More isn't better, but fewer isn’t better either. It’s about what the functions do, not how many there are.


Well, it’ssortalike that. dbt models reference each in a much cruder and more brittle way than proper functions. They can't take arbitrary inputs, and you can only reuse outputs, not the functions themselves. For example, you can’t create a function foradding sessions to an event stream, and then reuse that same transformational logic on several different tables.4The danger is it’s promising enoughanduncanny enough that it feels easier to create clean lineage graphs than it is. And because of that, it’s tempting to try but hard to get right, projects can becomesprawling5and redundant, and rewrites and updates get very hard.


SDF, actually, could start to fix this. From my understanding, the core technology behind SDF Is a generic SQL parser.6If that parser could trace the computational lineage of a column through a series of dbt models, analysts could start inspecting projects more like engineers inspect code. Today, to figure out exactly what90_day_new_user_retentionmeans, analysts have to read through every query that sits underneath the model with that column. A parser could, in theory, give a more succinct readout, showing exactly where that column came from—including beyond dbt—and what logic was applied to it in its upstream queries. That makes debugging and fixing problems much easier, especially if you can reverse the inspection, and see exactly what logic, and not just which queries, is downstream from a potential change. It's not a data reliability tool; it's a data resiliency tool.


Maybe it works. Maybe it doesn’t. Maybe I’m hypnotized by the possibility and promise of three-letter tools; maybe we’re all eventually moving back to Oracle. I don’t know. But the other approach—leaving it all up to Jeff—doesn’t seem to be working.

[1](https://benn.substack.com/p/will-we-ever-have-clean-data#footnote-anchor-1-135525323)

Fun fact: The pipeline to count the number of people using some part of Office 365 once included this step.

[2](https://benn.substack.com/p/will-we-ever-have-clean-data#footnote-anchor-2-135525323)

On the other hand,there is no step two.

[3](https://benn.substack.com/p/will-we-ever-have-clean-data#footnote-anchor-3-135525323)

Do I want to violate some GAAP policy and have the SEC put me in a room that’s too short to stand up in and not wide enough to lie down in? Nope.

[4](https://benn.substack.com/p/will-we-ever-have-clean-data#footnote-anchor-4-135525323)

Yes, you could do this in your Python orchestrator of choice, and you maaybe do with dbt macros? Maaaaaybe? But plain SQL is often more accessible.

[5](https://benn.substack.com/p/will-we-ever-have-clean-data#footnote-anchor-5-135525323)

Terrible video; top five single song performance I’ve ever seen live.

[6](https://benn.substack.com/p/will-we-ever-have-clean-data#footnote-anchor-6-135525323)

If SDF product doesn’t work but the SQL parser does, there’s probably a business to be had white-labeling it and selling it to other data vendors, all of whom wouldlove to have one.
