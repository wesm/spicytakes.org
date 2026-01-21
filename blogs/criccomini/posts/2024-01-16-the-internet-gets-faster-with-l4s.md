---
title: "The Internet Gets Faster With L4S, Terminal Benchmarking Tools, Zed Unifies Data Models, and more..."
subtitle: "There's a new protocol to save streaming; 1brc elevates some cool terminal benchmarking tools; and I compare Zed to Recap."
date: 2024-01-16T11:43:14+00:00
url: https://materializedview.io/p/the-internet-gets-faster-with-l4s
slug: the-internet-gets-faster-with-l4s
word_count: 1019
---


Materialized View crossed 1,000 subscribers in January! It’s encouraging to see such growth, and to get positive feedback. I just want to say thank you for subscribing.


---


## Low Latency, Low Loss, Scalable Throughput (L4S)


A friend (and Apple fanboy) recently pointed me at Apple’sLow Latency, Low Loss, Scalable throughput(L4S) WWDC 2023 video. L4S isa new architecture from the IETFthat optimizes internet bottlenecks.


> … L4S is based on the insight that the root cause of queuing delay is in the capacity-seeking congestion controllers of senders, not in the queue itself.  With the L4S architecture, all Internet applications could (but do not have to) transition away from congestion control algorithms that cause substantial queuing delay and instead adopt a new class of congestion controls that can seek capacity with very little queuing.  These are aided by a modified form of Explicit Congestion Notification (ECN) from the network.  With this new architecture, applications can have both low latency and high throughput.


Realtime applications—video and gaming—are an important part of our lives. These applications don’t do well when their network path is congested; users see stalls in their video, audio, or game. Lag is caused when slowest hop in a network traversal can’t keep up. Packets begin to queue, which causes lag and eventually a stall.


L4S reduces queuing and packet loss in the network to eliminate these stalls. Clients set an explicit congestion notification (ECN) bit in the packets they send. This bit signals that they support L4S. When a server in the network path begins to queue packets it receives, it marks the queued packets with a bit. The server (the final destination of the packet) counts flagged packets and reports back to the client. The client can then slow down its send rate.


Apple’s WWDC videoshows a real-world demo and compares RTT and packet loss metrics.


![](https://substackcdn.com/image/fetch/$s_!6zxu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9789b338-ee33-479f-9e75-cfe421ffb988_811x452.png)


The drop in tail latency notable, as this is where stalls are most egregious.


Since L4S sits low in the network stack—in both layer 3 (IP) and layer 4 (TCP/UDP) of theOSI model—your code should automatically benefit without any changes. The OS and routing hardware are what need to evolve.Apple, Google and ISPsare all working together to support L4S. On Mac, L4S is automatically supported in OS X Sonoma when using HTTP/3, QUIC, HTTP/2, or TCP. On Linux, there’s aGithub repocontaining the requisite kernel patches.


## Terminal Benchmarking Tools


Gunnar’s1brc challengehas elevated a bunch of benchmarking tools. Three that caught my eye arehyperfine,poop, andflameshow. All three are terminal tools.


Hyperfine is by far the most popular. It’s a glorifiedtimecommand with a bunch of cool features:


> Statistical analysis across multiple runs.Support for arbitrary shell commands.Constant feedback about the benchmark progress and current estimates.Warmup runs can be executed before the actual benchmark.Cache-clearing commands can be set up before each timing run.Statistical outlier detection to detect interference from other programs and caching effects.Export results to various formats: CSV, JSON, Markdown, AsciiDoc.Parameterized benchmarks (e.g. vary the number of threads).Cross-platform


![](https://substackcdn.com/image/fetch/$s_!xiuC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb85a075-d031-4a63-999c-fc2b7a6b1108_756x278.png)


Poop is similar, but has a most excellent name. Unlike Hyperfine, it only runs on Linux so it can take advantage ofperf_event_open.


> However, poop does report peak memory usage as well as 5 other hardware counters, which I personally find useful when doing performance testing. Hey, maybe it will inspire the Hyperfine maintainers to add the extra data points!Poop does not run the commands in a shell. This has the upside of not including shell spawning noise in the data points collected, and the downside of not supporting strings inside the commands.


Flameshow is a terminalFlameGraphviewer that supports both pprof and FlameGraph formats. From the original ACM article,The Flame Graph:


> A flame graph visualizes a collection of stack traces (aka call stacks), shown as an adjacency diagram with an inverted icicle layout. Flame graphs are commonly used to visualize CPU profiler output, where stack traces are collected using sampling.


Max Rydahl Andersenshowshow to use flamegraph with the JVMfor 1brc:


![](https://substackcdn.com/image/fetch/$s_!5nCg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96b810b0-d43f-4da5-af77-432ca7b6d22d_688x647.png)


## Project Highlight: Zed


Zedis an umbrella project for a collection of data lake tools. The project includes adata model,storage format(s), transactionaltable format,query language, and more.


Zed’s data model is what I’m most interested in. I’ve been working onRecapfor the past year. Recap lets you work with web service, database, and streaming schemas ina single format. Zed’sdata modelhas a very similar goal:


> Zed is a new data model that unifies the JSON and relational models to make data as easy as ever.


I am happy to see that Zed’s data model isverysimilar to Recap’s. We both made the same design choices independently. This is validating and bodes well for both projects.


Zed, however, is a much more ambitious project than Recap. It includes serialized formats (ZNG, VNG, ZSON, ZJSON), a query language, and more. I can’t speak to the whole tool chain, but the data model looks well thought out. If you’re using Zed I’d love to hear about it.


So when should you pick Zed, and when should you pick Recap for your projects? Zed is a much larger ecosystem; if you want serialization or data lake table formats, it’s the right call.


Recap is much slimmer; it deliberately limits itself to reading, writing, and converting between service, event, and database schemas. Recap also has aslightlymore robust model allowing for things like logical types, required fields, fixed length arrays and maps, and so on. I suggest Recap if your main use case is data modeling or schema conversion.Gable[$] is using Recap as their data model and I would love to see more adoption.


## More Awesome Infrastructure


Keep up with new infrastructure projects as they’re added toawesome-infra. New submissions are welcome!

- optd- CMU-DB's Cascades optimizer framework for query engines. Currently, optd is integrated into Apache Arrow Datafusion as a physical optimizer.


---


Share


---


You can support me by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to new software engineers that you know.


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
