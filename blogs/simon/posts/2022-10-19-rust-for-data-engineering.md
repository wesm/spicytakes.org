---
title: "Rust for Data Engineering10-19"
date: 2022-10-19
url: https://www.ssp.sh/blog/rust-for-data-engineering/
slug: rust-for-data-engineering
word_count: 1806
---

![Rust for Data Engineering](https://www.ssp.sh/blog/rust-for-data-engineering/feature-rust-vs-python.jpg)

Contents

Will Rust kill Python for Data Engineers? If you only came here to know this, my answer is no. Betteridge’s Law strikes again!


But then again, you have to ask: wasÂ *Python*Â made for Data Engineering in the first place?


Rust may not replace Python outright, but it has consumed more and more of JavaScript tooling and there are increasingly many projects trying to do the same with Python/Data Engineering. Let’s explore why Rust has potential for data engineers, what it does well and why it has become the most loved programming language for 7 years running.Â


## What is Rust?


Former Mozilla employee Graydon Hoare initially createdÂ [Rust](https://glossary.airbyte.com/term/rust)Â as a personal project. The first stable release, Rust 1.0 was released on May 15, 2015. Rust is aÂ **[multi-paradigm programming language](https://en.wikipedia.org/wiki/Comparison_of_multi-paradigm_programming_languages)**Â that supports imperative procedural, concurrent actor, object-oriented and pureÂ [functional](https://glossary.airbyte.com/term/functional-programming)Â styles, supporting generic programming and metaprogramming statically and dynamically.


> The goal of Rust is to be a good programming language for creating highlyÂ **concurrent, safe, and performant systems**.


## What Is Unique about Rust?


Rust solves pain points from other programming languages with minimal downsides. With Rust being a compiled programming language, strong type and system checks are enforced during compile-timeâmeaning pre-runtime! UnlikeÂ [Python](https://glossary.airbyte.com/term/python)’s interpreted way, most errors only surface during the coding phase. It can be frustrating to fight every single mistake before being able to test or run a quick script, but at the same time, a prominent feature like the compiler is much faster at finding bugs than me. Additionally, the Rust community puts a lot of effort into making the error messages super informative.


![/blog/rust-for-data-engineering/images/rust-compiler-in-action.jpg](https://www.ssp.sh/blog/rust-for-data-engineering/images/rust-compiler-in-action.jpg)

*Anexampleof how Rust surfaces an error during development and suggests changes*

Ownership, Memory Saftey, Reference Borrowing
There are much more specifics that differentiate Rust from other programming languages. Concepts such asÂ
[Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
Â for memory safety,Â
[Reference Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
, and many more, but this article is not meant to be a deep dive into Rust, but rather map it to the field of data engineering.

## Why Rust for Data Engineers?


When you write any code, the goal is that the code doesn’t break during the weekend or at night when you sleep. Rust will show you errors and improvements while coding and fails as much as possible at compile-time, which is less costly than later in production at run-time.


The go-to language for data engineers is Python, which isn’t the most robust or safe language, as many engineers working with data will agree. Rust’s developer experience goes much further than just offering a language specification and a compiler; many aspects of creating and maintaining production-quality software are treated as first-class citizens in the Rust ecosystem


### What Rust Does Well


Python is dynamically typed (with only recent support forÂ [type hints](https://docs.python.org/3/library/typing.html)) and requires writing extensive tests to catch these costly errors. But that takes a lot of time, and you must foresee all potential errors to write a test for it.


Rust is the opposite; it forces you toÂ **define types**Â (or does it implicitly withÂ [type inference](https://doc.rust-lang.org/rust-by-example/types/inference.html)) and enforces them. This does not obsolete testing of course, but for example, the rust compiler will analyze e.g.Â [borrow checking](https://rustc-dev-guide.rust-lang.org/borrow_check.html), and doesÂ [things](https://rustc-dev-guide.rust-lang.org/overview.html)Â to your code that other compilers don’t doâcheck outÂ [rust-analyzer](https://rust-analyzer.github.io/)Â for bringing them into your IDE of choice. This makes it very good for data engineers as we have many moving parts such as incoming data sets that we do not control.Â **Defining expectations**Â with data types and having vigorous checks at coding and compile time will prevent many errors.


Less relevant for data engineers, but super helpful:Â **speed**. Rust, as a compiled language, is super fast at run-time. To many, Rust is primarily an alternative to other systems programming languages, like C or C++. But you don’t need a systems use case to use a systems language, as bothÂ [Vercel](https://leerob.io/blog/rust)Â andÂ [Crowdstrike](https://www.crowdstrike.com/blog/data-science-test-drive-of-rust-programming-language/)Â are noticing.


Another one isÂ **integrations**. With data pipelines being the glue code in most cases, connecting otherwise foreign systems, Rust almost runs platform agnostic. Rust makes it easy to integrate and communicate with other languages through a so-calledÂ [*foreign function interface (FFI)*](https://en.wikipedia.org/wiki/Foreign_function_interface). The FFI provides aÂ **zero-cost abstraction**Â where function calls between Rust and C have identical performance to C function calls. Rust can be called easily from C, Python, Ruby, and vice-versa. Find more onÂ [Rust Once, Run Everywhere](https://blog.rust-lang.org/2015/04/24/Rust-Once-Run-Everywhere.html).


A less technical but still important element is toÂ **love**Â or haveÂ **fun**, enjoying your programming language. Rust is a more complex language to learn, but it was the most loved technology for seven years ([2022](https://survey.stackoverflow.co/2022/#section-most-loved-dreaded-and-wanted-programming-scripting-and-markup-languages),Â [2021](https://insights.stackoverflow.com/survey/2021#technology-most-loved-dreaded-and-wanted),Â [2020](https://insights.stackoverflow.com/survey/2020#most-loved-dreaded-and-wanted),Â [2019](https://insights.stackoverflow.com/survey/2019#technology-_-most-loved-dreaded-and-wanted-languages),Â [2018](https://insights.stackoverflow.com/survey/2018#technology-_-most-loved-dreaded-and-wanted-languages),Â [2017](https://insights.stackoverflow.com/survey/2017#technology-_-most-loved-dreaded-and-wanted-languages),Â [2016](https://insights.stackoverflow.com/survey/2016#technology-most-loved-dreaded-and-wanted)) in a row on the Stack Overflow survey:


![/blog/rust-for-data-engineering/images/love-vs-dreaded-wanted-programming-languages.jpg](https://www.ssp.sh/blog/rust-for-data-engineering/images/love-vs-dreaded-wanted-programming-languages.jpg)

*Loved vs. Dreaded and most Wanted Programming Language on StackOverflow Survey 2022*


Besides the love, it’s also rising in awareness of different trends such asÂ [Google Trend](https://trends.google.com/trends/explore?date=today%205-y&q=%2Fm%2F0dsbpg6), one from 2019Â [Ranking on GitHub](http://www.benfrederickson.com/ranking-programming-languages-by-github-users/), or the StackOverflow below:


![/blog/rust-for-data-engineering/images/recent-programming-language-trends-stackoverflow.jpg](https://www.ssp.sh/blog/rust-for-data-engineering/images/recent-programming-language-trends-stackoverflow.jpg)

*StckOverflow Trends*

Why Rust is Popular
For software engineers, many issues around systems programming are memory errors. Rust’s goal is to design a project with quality code management, readability, and quality performance at runtime.

## Interesting Open-Source Rust Projects


The language is always only as good as its community. Let’s look at some of the existing open-source tools and frameworks built in and around Rust:

- [DataFusion](https://github.com/apache/arrow-datafusion)Â based onÂ [Apache Arrow](https://glossary.airbyte.com/term/apache-arrow): Apache Arrow DataFusion SQL Query Engine similar toÂ [Spark](https://glossary.airbyte.com/term/apache-spark)
- [Polars](https://github.com/pola-rs/polars): It’s a fasterÂ [Pandas](https://glossary.airbyte.com/term/pandas). Probably going to compete withÂ [DuckDB](https://glossary.airbyte.com/term/duckdb)Â (?)
- [Delta Lake Rust](https://github.com/delta-io/delta-rs): A native Rust library forÂ [Delta Lake](https://glossary.airbyte.com/term/delta-lake), with bindings into Python and Ruby
- [Cube](https://github.com/cube-js/cube.js): Headless BI for Building Data Applications
- [Vector.dev](https://github.com/vectordotdev/vector): A high-performance observability data pipeline for pulling system data (logs, metadata)
- [ROAPI](https://github.com/roapi/roapi): Create full-fledged APIs for slowly moving datasets without writing a single line of code
- [Meilisearch](https://github.com/meilisearch/meilisearch): Lightning Fast, Ultra Relevant, and Typo-Tolerant search engine
- [Tantivy](https://github.com/quickwit-oss/tantivy): A full-text search engine library
- [PRQL](https://github.com/prql/prql): Pipelined Relational Query Language for transforming data
- Many more; please let me know of any


Less relevant to data engineering, but still cool:

- [Deno](https://github.com/denoland/deno): This is a fast Node.js version
- [Tauri](https://github.com/tauri-apps/tauri): Tauri is a framework for building tiny, blazingly fast binaries for all major desktop platforms
- [Yew](https://github.com/yewstack/yew): A modern Rust framework for creating multi-threaded front-end web apps with WebAssembly.


Read more on a currated [List of great Open-Source Rust Projects](https://www.ssp.sh/brain/great-open-source-tools-in-rust/).


## Rust vs. Python


The downside of Rust, the learning curve is much higher than other languages, such as Python. That’s why most Rust programs in data engineering will have a PythonÂ [wrapper](https://github.com/PyO3/pyo3)Â for integrating it into any Python data pipelines for a long time. It’s also a shift from an interpreted language such as Python to a moreÂ [Functional Language (FP)](https://glossary.airbyte.com/term/functional-programming)Â style, which Rust certainly supports.

The upside and downside of the Python language

What makes Python popular right now:

- Itâs old
- Itâs beginner-friendly
- Itâs versatile


The downsides of Python:

- Speed / Multithreading
- Scope
- Mobile Development
- Runtime Errors


Check more onÂ [Why Python is not the programming language of the future](https://towardsdatascience.com/why-python-is-not-the-programming-language-of-the-future-30ddc5339b66)Â or aÂ [small Twitter poll](https://twitter.com/sspaeti/status/1580551324281999360)Â if Rust is suited for data engineering.


### Other Recent Programming Languages


Newer programming languages follow the functional programming approach. New functional programming languages started, such asÂ [Scala](https://github.com/scala/scala)Â withÂ [Akka](https://github.com/akka/akka),Â [Elixir](https://github.com/elixir-lang/elixir), or multi-paradigm programming languages such asÂ [Julia](https://github.com/JuliaLang/julia),Â [Kotlin](https://github.com/JetBrains/kotlin)Â (aÂ [fastest-growing](https://insights.stackoverflow.com/trends?tags=rust%2Cscala%2Celixir%2Cclojure%2Cgo%2Chaskell%2Ckotlin)Â language since Google made it default for Android development), andÂ [Rust](https://github.com/rust-lang/rust).


[GoLang](https://github.com/golang/go)Â seems to be a good compiled programming language usedinÂ [DevOps](https://glossary.airbyte.com/term/dev-ops).


[Elixir](https://github.com/elixir-lang/elixir)Â has servers monitoring data pipelines and re-tries included in the language; no framework is needed. It makes an excellent fit for data engineering and would replace parts of theÂ [Data Orchestrators](https://glossary.airbyte.com/term/data-orchestrator).


### Rust as a Primary Language?


Let’s see an example of a modern data pipeline integrating withÂ [Airbyte](http://airbyte.com/),Â [dbt](http://getdbt.com/), and some ML models in Python.


Each step can have errors and data mismatches. That’s why we have orchestrator frameworks such asÂ [Dagster](http://dagster.io/), which force you to write functional code or the concept ofÂ [Functional Data Engineering](https://glossary.airbyte.com/term/functional-data-engineering/). There is also lots of adoption in Python with the type hint or writing moreÂ [Python and Functional Programming](https://towardsdatascience.com/how-to-make-your-python-code-more-functional-b82dad274707)Â style. Or to bring up an example of another language, JavaScript, the rise ofÂ [TypeScript](https://github.com/microsoft/TypeScript).

Will Rust be adapted?
The exciting question to me is whether Rust will be adapted as aÂ
**primary language**
Â and can do data orchestration work?

As we typically load data into a data frame and transform or add some business logic within our data pipelines. This could be done efficiently with Rust and Apache Arrow, and DataFusion, which is type-safe, and a good ecosystem. Time will tell.


## Will Rust Be the Programming Language for Data Engineers?


Rust is a multi-use language and gets the job done for many problems of a data engineer. But the data engineering space is dominated by Python (andÂ [SQL](https://glossary.airbyte.com/term/sql)) and will stay that way for the foreseeable future. There is no “until people fully move into Rust”. It’s hard to express how manyÂ [tools and frameworks](https://en.wikipedia.org/wiki/List_of_Python_software)Â are written in Python to interoperate with other Python tools. It’s pretty hard to imagine that inertia changing substantially in the next decade.


The Rust projects we have seen above are excellent and will continue to grow for vital and core components, but for them to be helpful for the average data engineer. What was once supposed to be Scala will now be Rust âa backend tooling language to do tasks that need fast and well-maintained code, including a Python wrapper on top.


Writing libraries in Rust feels more like writing long-term infrastructure than writing in higher-level languages such as Python, Java, or the JVM.


What do you think? What is your take on Rust for data engineers?


### Resources to Learn More on the Topic


Suppose you want to be up and running within minutes. Karim Jedda has anÂ [article](https://karimjedda.com/carefully-exploring-rust/), carefully exploring the Rust programming ecosystem as a 10+ years Python developer, checking how to do everyday programming tasks and what the tooling looks like. Shared Services of Canada did aÂ [hands-on example](https://www.statcan.gc.ca/en/data-science/network/engineering-rust)Â with Rust converting raw archive files into JSON for data analysis. Or Mehdi Ouazza’s article where he debates theÂ [Battle for Data Engineer’s Favorite Programming Language](https://betterprogramming.pub/the-battle-for-data-engineers-favorite-programming-language-is-not-over-yet-bb3cd07b14a0).Â


Learning Rust has many excellent resources.Â [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust),Â [The Rust Book](https://doc.rust-lang.org/book/),Â [Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/),Â [Read Rust](https://readrust.net/), orÂ [This Week In Rust](https://this-week-in-rust.org/).


OrÂ [Learning Rust](https://learning-rust.github.io/)Â with different kinds of formats:

- [Are we web yet?](http://www.arewewebyet.org/)
- [Are we game yet?](http://arewegameyet.com/)
- [Are we learning yet?](http://www.arewelearningyet.com/)
- [Are we GUI yet?](https://areweguiyet.com/)
- [Are we audio yet?](https://areweaudioyet.com/)


Or do you want to get hands-on and search for an example project? How about building anÂ [Airbyte Delta Lake Destination](https://github.com/airbytehq/airbyte/issues/16322)Â (Python interface) withÂ [delta-rs](https://github.com/delta-io/delta-rs)?


---


```
Originally published at Airbyte.com
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/rust-for-data-engineering/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Rust](https://www.ssp.sh/tags/rust/)
[Python](https://www.ssp.sh/tags/python/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
