---
title: "Database And Build Time"
description: "Here's an interesting contrast I recently picked up. Two enterprise application projects of a similar size (~100 KLOC), similar environments (Java and .NET). One can do a full build and test in an hou"
date: 2004-01-15T00:00:00
tags: ["continuous delivery", "testing"]
url: https://martinfowler.com/bliki/DatabaseAndBuildTime.html
slug: DatabaseAndBuildTime
word_count: 121
---


Here's an interesting contrast I recently picked up. Two
enterprise application projects of a similar size (~100 KLOC), similar
environments (Java and .NET). One can do a full build and test in an
hour, the other takes 2-3 minutes.


So what's the difference? Our analysis so far identifies database access.
Both projects have a big test suite and it's the tests that take the
most of the long build time, in particular the tests that access the
database - about 50% of the tests.


On the short build time project, they use a object-relational
mapping layer ([neo](http://neo.codehaus.org/)) that
isolates the application from the database. Only the tests for neo hit
the database, most tests are all in-memory and thus much faster.
