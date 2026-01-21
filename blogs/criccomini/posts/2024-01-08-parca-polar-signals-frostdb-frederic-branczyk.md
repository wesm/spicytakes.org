---
title: ""
date: 2024-01-08T12:48:00+00:00
url: https://materializedview.io/p/parca-polar-signals-frostdb-frederic-branczyk
slug: parca-polar-signals-frostdb-frederic-branczyk
word_count: 191
---


I recently talked withFrederic Branczyk. Fredric is the founder ofPolar Signals, a new always-on, zero-instrumentation profiler. Before Polar Signals, Fredric spent time atRed HatandCoreOS, where he worked onKubernetesandPrometheus.


In this interview, Frederic and I break down Polar Signals’s architecture and its main components:ParcaandFrostDB. Parca is of particular interest; it is able to achieve its minimally invasive profiling claims by using aneBPFfilter that samples the entire OS’s stack at 19hz. Data is then passed to a server and stored into FrostDB, an embedded storage engine built onDatafusionandParquet.


During the discussion, Frederic mentions several influential papers:

- Google-Wide Profiling: A Continuous Profiling Infrastructure for Data Centers
- BOLT: A Practical Binary Optimizer for Data Centers and Beyond
- Propeller: A Profile Guided, Relinking Optimizer for Warehouse-Scale Applications
- Large-scale Incremental Processing Using Distributed Transactions and Notifications


---


Share


---


You can support me by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to new software engineers that you know.


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
