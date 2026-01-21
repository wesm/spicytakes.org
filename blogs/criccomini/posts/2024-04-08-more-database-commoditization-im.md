---
title: "More Database Commoditization, I’m Caving on Rust, Zig Has Some Growing up To Do, and More..."
subtitle: "I talk database commoditization on YAIDD; Jack Vanlightly writes a follow-up; I'm learning Rust (again); Zig still excites me, but it's young; and I highlight mini-lsm."
date: 2024-04-08T10:33:43+00:00
url: https://materializedview.io/p/more-database-commoditization-im
slug: more-database-commoditization-im
word_count: 1070
---


I’m back! It’s been a couple of weeks since my last post. I took some family time and spent last week digging intoRust. I also joined theYet Another Infra Deep Dive podcasta few weeks ago. We discussed database commoditization and my recent post,Databases are a Commodity, Now What?


> Ian and Tim sat down with Chris Riccomini (ex-Distinguished eng at Wepay, co-creator of Apache Samza) to talk about the spicy takes he has been sharing on his blog Materialized View and even further takes in the future of what the data system world will look like!


---


## Jack Vanlightly Writes About Platforms


Jack Vanlightlywrote a thoughtful follow-up to myDatabases are a Commodity, Now What?post.The postdigs into the characteristics of a platform. His thoughts are framed around the bookStart With WHY, which I hadn’t heard of.


Jack leads with a quote from the book. The premise is essentially that first-mover advantage is very short-lived and most everything can be copied. The post spends time contemplating how platforms could help infrastructure vendors differentiate.


> A platform is a coherent and cohesive set of features that seamlessly work together to provide a service more than the sum of its parts. Platforms are difficult to build, they comprise a thousand tiny things to be developed and maintained, and that make sense as a whole.


The post also suggests that my third point of differentiation—HTAP—is really an instance of a larger potential for innovation. There are still unsolved problems, HTAP being one. I have to agree with Jack on this point. I’ve been spending time with Rust,RocksDB, andlog-structured merge-trees(LSMs) lately; it still amazes me how much work is left to do.


## I’m Caving on Rust


Did I mention I’m learning Rust? I’m learning Rust. I’m really annoyed that you all are making me. Alas, it seems to have truly taken hold of systems infrastructure. Either that or the community is really, really loud. (Likethat Crossfit joke, “How do you know if someone writes Rust? They will tell you.”)


I tried learning Rust in 2022 usingAdvent of Code. It was a disaster. I gave up after one day and switched toZig. Lifetimes and the borrow checker didn’t click with me. And my task—Advent of Code—had a lot of text parsing, which Rust isn’t the best at.


![](https://substackcdn.com/image/fetch/$s_!UzjU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6ef34f-07fe-4b5a-8509-cef6ca8d0306_1382x370.png)

*View Post*


This time around, things are going better.GPT-4 and Gemini have been a tremendous help. In 2022, I tried using LLMs when I was working with Zig. Unfortunately, GPT-3 hallucinated a lot. It frequently intermingledGoandPythonwith Zig, likely due to similar syntaxes and a dearth of Zig source material.


I am using the LLM like it’s a senior engineer sitting next to me. Here are some actual questions I’ve asked it:

- How do you remove tokio's sync feature from a dev dependency list?
- Show me how to use crossbeam's waitgroup in Rust?
- What happens when you await inside an async function in Rust?
- Show me how to use a Condvar in Rust.
- How do dependencies work in Rust when I build a library or binary? Do they get frozen and packaged up as part of the binary?


Both GPT-4 and Gemini have done quite well with such questions.


I also spent a week readingRust’s online book. A careful reading ofthe lifetime sectionmade things stick this time. It’s expertly written. Kudos to whoever worked on it.


But feature-wise, Rust is the opposite of what I want; it’s a thick language with a thin standard library. Rust’sstdis so thin that it doesn’t even come with an async runtime. You have to pull in something likeTokio. Even random numbers require an external package! InZig, Rust, and other languages,Phil Eatonwrites:


> People have been making jokes about node_modules for a decade now, but this problem is just as bad in Rust codebases I've seen.


I agree. It feels like I need to pull a package in to do just about anything with Rust. I don’t like this. I much prefer a thick standard library like Go or Python.


Finally, I came across Rust’sintroductory presentationfromGraydon Hoare, Rust’s progenitor. It provides a lot of context about the language and pairs well with Graydon’s,The Rust I Wanted Had No Future.


## Zig is Still Young


As usual, I gazed longingly at Zig every time I was tripped up in Rust. But this time I found myself less enthused. I still prefer Zig’s philosophy and syntax; its tagline—a dig at Rust—resonates with me:


> Focus on debugging your application rather than debugging your programming language knowledge.


But the ecosystem is quite immature; this is where Rust really excels. Ecosystems are more important than languages to me. Rust’s packaging system (Cargo) is excellent as is Rust’s documentation. There are libraries for everything (despite my earlier gripe). Zig is comparatively lacking. I’m making an unfair comparison, of course. Zig has only been around for about 7 years—Rust double that. I hope Zig matures gracefully.


One item thatgave me pausewasZig’s new package manager. It sounds like I need to write abuild.zigbuild file to do package management. Then I need to create aZig Object Notation(ZON) file. This is the equivalent of having developers write abuild.rsin order to use aCargo.toml.


I don’t find Zig’s build.zig and build.zig.zon user-friendly, especially since they ditched the ini format (why not TOML?) for ZON. The decision triggers deep-seatedsbtandbuild.gradletrauma in me. I’d much prefer a dependency manifest file like Cargo.toml without a build.zig (at least for the happy path case).


## Project Highlight: mini-lsm


I’ve been reading aboutlog-structured merge-trees(LSMs) lately. There are some great resources out there.RocksDB’s wikireflects the state of the art. For beginners, I recommend,How RocksDB works.


On a whim, I Googled, “Rust LSM,” and discoveredmini-lsm(Github). The project shows how to create an LSM database in Rust. Developers clone the repository and work along with the tutorial.


Each week is divided into a daily exercises. You start with memtables, data blocks, and so on. By the end you’re implementingmultiversion concurrency control(MVCC). I’m working through it. It’s also proving to be a great way to learn Rust. I highly recommend it if you can find the time.


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
