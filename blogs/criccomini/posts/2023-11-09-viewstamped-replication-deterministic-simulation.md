---
title: "Viewstamped Replication in Go, Deterministic Testing at Dropbox, FoundationDB's Simulation, and more..."
subtitle: "Viewstamped Replication makes a comeback; I dig into distributed simulation testing with Dropbox, FoundationDB, and Tigerbeetle."
date: 2023-11-09T11:12:20+00:00
url: https://materializedview.io/p/viewstamped-replication-deterministic-simulation
slug: viewstamped-replication-deterministic-simulation
word_count: 588
---


## View Stamped Replication in Go


Joran Dirk Greef(ofTigerbeetle[$]) has me on theViewstamped Replicationband wagon. Viewstamped Replication is a consistency algorithm that predatesPaxosandRaft. See Joran’slovely talkfor more details on it.


There seem to be relatively few actual implementations. I’ve only seenTigerbeetle’s Zig implementation, aRust library, and some abandoned attempts in Go (vrr-go,vrgo). So I am excited to see thatUtkarsh Srivastavais working on a newGo implementation.


![](https://substackcdn.com/image/fetch/$s_!a_b0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4f09030-2a4a-47ed-a2c2-f568b10c3704_692x238.png)


It’s a young project but he’s building in the open and it’s already an instructive learning tool.


## Deterministic simulation testing at Dropbox


Utkarsh’s comment on simulation testing led me to Dropbox’slengthy technical write-upof their “sync engine” rewrite in 2020. Sync engine merges a user’s local and remote filesystem changes. States are modeled as file trees and a “sync tree” (similar to aVCSdiff) is generated to determine changes.


The post covers strategies to write deterministic and easily testable code.


> In Nucleus, we sought to make writing tests as ergonomic and predictable as possible. Nearly all of our code runs on a single “control” thread. Operations benefiting from concurrency (e.g. network I/O, filesystem I/O, and CPU-intensive work like hashing) are offloaded to dedicated threads or thread pools. When it comes to testing, we can serialize the entire system. Asynchronous requests can be serialized and run on the main thread instead of in the background. Say goodbye to flaky tests! This single-threaded design is the key to the determinism and reproducibility of our randomized testing systems.


Many of these ideas apply when testing consensus algorithms like Utkarsh’s Viewstamped Replication library, above.


As an aside, Dropbox mentions using SQLite for client state. I’ve beensearching for more examplesof SQLite in large production deployments; this is definitely one.


## Writing deterministic code


Continuing on the deterministic code theme,Alex Kladov’s recent talk has been making the rounds. As the title suggests, TigerBeetle [$] uses similar techniques to Dropbox. The talk is a pithy 15 minute watch.


Alex recommends reducing variability in both space (IO) and time (clocks), and gives some pointers to do this. The claimed benefits are that deterministic code:

- Is easier to debug and test.
- Improves runtime predictability because resources are managed statically.
- Improves runtime throughput because, again resources are statically managed. (Especially if dynamic memory management goes away.)


## FoundationDB’s simulation testing


FoundationDB’s Simulation is a real-world example of simulation testing.Will Wilsontalks about the framework in a 2014Strangeloop(🪦) presentation.


See thewrite-upon FoundationDB’s site for a more bite-sized introduction.


One interesting technique FoundationDB uses in Simulation is something called swizzle-clogging.


> To swizzle-clog, you first pick a random subset of nodes in the cluster. Then, you “clog” (stop) each of their network connections one by one over a few seconds. Finally, you unclog them in a random order, again one by one, until they are all up. This pattern seems to be particularly good at finding deep issues that only happen in the rarest real-world cases.


## Parting thoughts


The core take-away from all of these systems is to:

1. Stamp out non-determinism in your code.
2. Write a framework that runs with a pseudo-random number seed so you can reproduce failures.


This is harder than it sounds, hence all of this wonderful content.


## More Awesome Infrastructure


Keep up with new projects onawesome-infraGithub repo. New submissions are encouraged.


ReadySet- A lightweight query cache that sits between an application and database turning SQL reads into lookups.


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
