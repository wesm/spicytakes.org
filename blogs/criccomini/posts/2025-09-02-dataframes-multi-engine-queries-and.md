---
title: "DataFrames, Multi-Engine Queries, and Xorq With Hussain Sultan"
subtitle: "Hussain Sultan, the co-founder of Xorq, discusses the broken DataFrame ecosystem and how Xorq is fixing it."
date: 2025-09-02T11:07:32+00:00
url: https://materializedview.io/p/dataframes-multi-engine-queries-and
slug: dataframes-multi-engine-queries-and
word_count: 2607
---


In myprevious post, I mentioned thatMartinand I were working onDesigning Data Intensive Applications’s batch chapter. The chapter is now available in pre-release onSafari Online, and (among other things) includes a section onDataFrames.


While working on the DataFrame section, I was surprised to find how bifurcated the ecosystem remains. On one side, you have single-node libraries like R andPandas. On the other side, you have bolt-on Pandas-compatible APIs for distributed execution engines and cloud data warehouses such asApache Spark’spysparkandSnowflake’sSnowpark. It seems to me that a more unified approach is needed.


This post is an interview withHussain Sultan, the co-founder and CEO ofXorq﹩. We discuss the fragmented DataFrame ecosystem and how Xorq bridges the gap with its multi-engine DataFrame library built onIbis,Apache DataFusion, andApache Arrow. Hussain has a diverse background that spans electrical engineering,digital signal processing (DSP), data science, machine learning, and field engineering. I’m so excited about what Hussain and Xorq are doing that I’ve joined their most recent funding round.


---


C.R: Thanks for taking the time to talk. I'm interested inyour career path. I noticed you started as a hardware engineer before falling into the data space. How did you go from a background in digital signal processing to founding Xorq?


H.S.: Appreciate you asking—this has definitely not been a straight line. I’ve always been a builder. I had early access to a computer, picked up aVisual Basic for Applications (VBA)book before I knew what code really was, and hacked on WordPress sites in college. But knowing I could always fall back on software gave me the confidence to dive into other domains—hardware, embedded systems, DSP—where the problems felt more physical, more constrained.Electrical engineering gave me the tools to think in systems. I worked on turbine blade monitoring usingLabVIEWandField-programmable gate arrays (FPGAs)—very visual, very declarative. It was kind of like building adirected acyclic graph (DAG), just with wires. That led me into DSP, and eventuallyelectroencephalogram (EEG)denoising in grad school. EEGs were fascinating because they were a deeply human signal—full of noise, uncertainty, context. But inMATLABeverything felt so perfect, so sandboxed. I wanted data that was messier, more grounded in the real world, perhaps even macro behavior.That’s what pulled me toward other types of data. I got fascinated by the idea that how people transact and spend money reveals something real about human behavior—at scale. Purchase behavior is just another noisy signal, but at a macro level. So I went deep into consumer models, credit risk, customer behavior etc.That’s when I ran into real-world noise:SAS jobs, VBA macros, SQL you couldn’t trace, pipelines nobody owned. The business logic—net present value (NPV)models,Monte Carlosimulations, decision rules—was always trapped in brittle systems. And I knew there had to be a better way.


I turned to open source Python out of necessity: Pandas,Dask, and Arrow. When I found thePyDatacommunity, it felt likeWordPressagain: smart people solving hard problems together, in the open.Over the years, I took that mindset into big tech, avionics systems, and consulting for banks trying to modernize. We saved millions just by building reusable, inspectable pipelines. But I kept running into the same issue: compute wasn’t composable, but was rapidly being commoditized by things likeDuckDBand DataFusion. You couldn’t trace them, reuse them, or move them across engines…easily. It wasn’t an infra problem—it was an abstraction problem. Data has structure. Compute didn’t.That’s what led to Xorq. With Arrow, Ibis, and DataFusion, the primitives were finally ready. Xorq is a compute catalog: a place to put the logic itself. Expressions become portable, observable, and reusable. Multi-engine. Storage-agnostic. Versioned by default.


So no, this wasn’t some grand plan. I just kept chasing messy signals, building tools to make sense of them, and leaning on the communities that made that work possible.


C.R.: What does the compute logic in Xorq’s “compute catalog” look like? Are we talking about operators that can be run in a physical query plan executor—things like a “sort-merge join” operator? Or are these more bespoke pieces of logic? Some examples might help me understand more.


H.S.: Short answer: we don't deal with physical operators—you won’t see “sort-merge join” in our plan. What we store is arelational + functional + semantic planthat’s declarative, portable, and able to run across different engines.


You can think of this compute logic as a “high-level plan” that stitches together many logical plans for engines running in different places—DuckDB, DataFusion, Pandas, and so on. The bespoke logic shows up as PythonUDFs and UDAFs, and we leaned on DataFusion because it treats Arrow-based functions as first-class. At this level we also track tags, caching, and pipeline operators that move data between engines. Once the plan is executed into a backend, that’s when the physical choices—hash vs. sort-merge join, vectorization, parallelism—get made. We generally leave that up to the engine. Things like theinto_backendoperator to go from one engine to another andflight_udxfnodes for arbitrary computations appear often instead.


Since multi-engine workloads heavily lean on deterministic caching, we build a stable hash of the plan that can be used with a cache operator. If two subgraphs are the same, they map to the same cache key and return identical results, regardless of which engine runs them.


A concrete example: take a simplescikit-learnpipeline. We lift it into Xorq’sintermediate representation (IR), split it into train/test, add cache boundaries, and tag each step with metadata (step name, parameters, features, target). Under the hood,fitlowers to a UDAF that produces state (weights, scalers, encoders), andapplylowers to a scalar UDF that consumes that state row by row (normalize, lookup, predict). Xorq usesIbisheavily for its expression system and its the de facto user-facing IR.


So in this plan, the “predicted” column is literally a scalar UDF parameterized by the fitted model executed in the DataFusion engine. Reads flow through DuckDB, ML bits get routed to DataFusion and UDFs, and from the developer’s side it’s just Python (`expr.py` with `.fit(...)`, `.predict(...)`, tagging, and caching). Xorq then emits a build directory so the whole thing can be reproduced.


Because the entire workflow is captured in this relational algebra, we can lower ordinary Python pipelines into SQL engines, or extend them with arbitrary compute via `flight_udxf`. That’s what makes it a “high-level plan”—broader than a database logical plan, and able to tie together engines outside the SQL world (vector databases, graph systems like KuzuDB, etc.) and of course, coupled with a user-facing expression system in Ibis.


Aquick recordingis available if you’d like to see it in action;here’s a gistwith the complete build outputs, which might help readers understand it more concretely.


C.R.: Wow, OK, this is pretty slick. You mentioned that you re-use identical results if two subgraphs are the same. Does this work across queries, workflows, or even users as well? Also, how do you handle cache invalidation, where a subsequent query might want fresher data than the cache contains?


H.S.: It does—across queries, across workflows, and, within a workspace and its permissions, across users. The way we make that safe and predictable is by tackling the old, thorny problem of “naming things.” If you can name a computation deterministically, you can look it up later and recover its full lineage to the source. This isn’t a new idea; you see versions of it in content‑addressed storage and in Nix.


My co‑founder,Dan, and I have lived through this pain for years. Every time we’d run a new experiment, we’d save the training dataset and the splits, and then were left juggling with naming datasets and—even harder—when to invalidate the cache. Nix gave us a clean mental model: it hashes, builds deterministically and leverages binary caches. If two people produce the same build, Nix can tell you whether a valid artifact already exists or whether it needs to be rebuilt.


Xorq applies that principle to data compute. We derive a cache key for any expression by hashing the contents of the expression itself along with the relevant source descriptors. Depending on the caching strategy, we either incorporate a change signal—like a table’s last‑modified time—or we pin to a snapshot. If the upstream table changes and you’re in a “follow the source” mode, the stamp changes, the hash flips, and the cache is naturally bypassed so the computation is re‑materialized. If you’re in snapshot mode, the cache key stays stable until you explicitly ask for something fresher.


To make reuse work across users without surprises, the hash has to be stable. That means we strip away environment‑specific noise and avoid anything brittle like absolute local file paths. The result is a content‑addressed artifact that’s consistent regardless of who computes it, so long as they’re looking at the same logical expression and the same view of the source.


Because "cache" is just another node in the relational graph, you can attach it wherever it makes sense. You might cache a heavy transformation to accelerate iteration but choose not to cache a subsequent training step. The choice is surgical and composable.


An added benefit of stably hashing every node is discovery. We can compare expression nodes across different graphs—even across teams—and detect shared subgraphs. That lets us surface high‑value candidates for caching and reuse across an organization, not just within a single project.


On freshness guarantees, especially for near‑real‑time features like “activity_last_5m,” we combine strategies. We can materialize the feature in snapshot mode first—so we’re not chasing source modification times constantly—and then apply a time‑to‑live at retrieval. When the TTL expires, we recompute. That pattern will feel familiar to anyone who’s worked with feature stores for ML workloads.


So the short version is: reuse works across queries, workflows, and (with proper access controls) users, because everything is deterministically named. Invalidation is built into that identity—either via source‑change stamps for automatic freshness or via TTL‑driven policies when you want precise control.


C.R.: Hah, you walked right into my next question! I am curious if you’ve considered how streaming and realtime data fit into Xorq. Many other processing frameworks (Spark,Apache Flink,Feldera) are working towards a unified API for both modalities. It sounds like Xorq is pretty batch-focused. Are there any plans to add streaming or “micro-batch” support?


H.S.: You’re right—most of our current focus is on batch engines. I usually describe Xorq’s architecture as out-of-core i.e. we stream ArrowRecordBatchfragments between operators instead of materializing everything up front. That lets us handle datasets larger than memory while still feeding engines directly. The key distinction here is bounded vs. unbounded. Out-of-core workloads are bounded—they terminate— whereas micro-batch or real-time streaming engines operate over unbounded streams. DataFusion, our embedded engine, has also been a solid building block for unified models and even some emerging streaming use cases.


We’ve been actively experimenting with streaming engines like Flink because our expression system, through Ibis, can already describe watermark- and time-aware operations. The real difference comes at the source: if you attach a bounded table, you’re still in a mini-batch world; if you attach an unbounded source like Kafka or CDC, the exact same expression can be evaluated incrementally by the engine. Official Flink support is on our mid-term roadmap, but even in these early experiments it’s clear how naturally our model extends to streaming SQL. This is slated for mid-term priority on our roadmap and would be an indicator that we feel confident with batch use-cases and ready to tackle streaming/real-time engines. I am also super psyched about engines likeFeldera, since it turns the SQL that we know for batch cases and makes it incremental without changes. A unified API for both modalities is most welcomed!


What’s exciting is that the same caching and reuse story still holds. We can incorporate Flink’s operator state into our hashing model, which makes streaming computations just as stable and discoverable as batch ones.


This ties directly into how we think about freshness guarantees in research vs. production. In a research notebook, you might snapshot a feature like “activity_last_5m,” attach a TTL, and let the cache refresh when it expires. It’s reproducible and easy to debug. But in production, you want that feature continuously updated without extra orchestration.


And that’s really the arc: in research, you rely on explicit snapshots and cache nodes; in production, you lean on streaming engines and policies that manage freshness automatically.


C.R.: Similarly, how do you see Xorq fitting in with AI training and inference workloads?


H.S.: Xorq works great with AI/ML training and inference, but for tabular data. We model opaque compute with aflight_udxfnode, executed as anApache Arrow Flightdo_exchangeendpoint. This allows us to remain in a relational authoring surface—DataFrames and SQL—while offloading to tensor runtimes as opaque operations, all without leaving the plan.


Apache Arrow provides the typing system and transport layer. Crossing the boundary is efficient: Arrow arrays convert toDLPackand back with minimal overhead. Because training and inference typically run in mini-batches, our out-of-core streaming backbone remains unchanged, and relational engines compose seamlessly with arbitrary compute.


For scikit-learn–style machine learning, our goal was to unify training and inference into a single relational graph instead of two ad-hoc scripts. We achieve this with UDF/UDAF machinery in DataFusion: “fit” lowers to an aggregate UDF that emits state (weights, scalers, vocabularies) as bytes or artifact references; “apply” lowers to a UDF that consumes that state row-wise for predictions. Because DataFusion operates directly on Arrow RecordBatches, the pattern is fast in practice. And we can make these UDFs portable with Arrow Flight.


However, one key lesson is that DataFrame APIs excel for feature engineering and early-stage preprocessing, but late-stage preprocessing nearly always shifts to tensor operations; thinknn.Module/TensorDict, dense normalization, tokenization etc.. The next step is to make this “last mile” feel likePyTorch, instead of DataFrame-ey, while keeping the entire workflow declarative, optimizable, and reproducible. This will also unlock new workloads with unstructured data, videos, images etc.


Long-term, we are inspired by theDeclarative Sub‑Operators paper: expose a lower‑level, declarative layer beneath relational algebra so we can express things like tensor-prep. I am excited for the declarative future, where Tensor and DataFrame APIs can be used interchangeably.


C.R.: You’ve described so many directions that Xorq can go in. There’s clearly many years of work ahead; I look forward to seeing it evolve. In the meantime, it seems like a pretty solid batch multi-engine system. I really appreciate you taking the time to talk with me. I’ll give you the final word. Anything you’d like to add? Where should folks go if they’re interested in learning more?


H.S.: It’s a big vision, made possible only by standing on the shoulders of Apache Arrow, Ibis, and DataFusion. Across the ecosystem, teams are building semantic layers, generating request-time dynamic SQL, and with Xorq, making ML accessible to data and analytics engineers. In the multi-engine batch processing world, our early design partners report speeding up dynamicdbt-style workloads by 5-15x versus Jinja-based SQL model generation, cutting infrastructure costs by >10x compared with Snowpark, while providing end-to-end column-level lineages and greater transparency. This fits since our target audience tends to be multi-stakeholder organizations that span tech, business, and data. This means, we need to thread value across various stakeholders i.e. cost of ownership, time to value and policy-based governance.


Our catalog-first approach makes reuse, optimization, and governance first-class, while staying minimally invasive to how teams already run on SQL engines. We are super keen to get feedback from the community on the "compute catalog" concept. If this resonates, kick the tires and tell us what’s missing:

- GitHub:https://github.com/xorq-labs/xorq
- Docs:https://docs.xorq.dev
- Website:https://xorq.dev


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
