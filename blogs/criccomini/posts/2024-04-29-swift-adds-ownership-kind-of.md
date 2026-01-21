---
title: "Swift Adds Ownership (Kind Of)"
subtitle: "I extol the virtues of Swift's ARC memory management only to discover that Apple has added Rust-like ownership to Swift."
date: 2024-04-29T21:25:39+00:00
url: https://materializedview.io/p/swift-adds-ownership-kind-of
slug: swift-adds-ownership-kind-of
word_count: 838
---


Materialized View blew past 2,000 subscribers in April! I’ve received a lot of positive feedback and I am humbled by its growth. Thanks!


---


I’ve beenhacking with Rust latelywhilebuilding a cloud native LSM database. The learning curve has been steep andRust’s borrow checkerhas gotten in the way a few times. Over breakfast a few months ago, one of my (Apple-fan) friends lamented that Rust should have adoptedSwift’s memory managementif, “infrastructure developers could just get over themselves.”


Swift usesautomatic reference counting(ARC) to manage application memory. For those unfamiliar, ARC counts pointers to data on the heap. When there are no more pointers to data on the heap, the memory is freed. This stands in contrast togarbage collected languageslike Java and Go, or manual management like C, C++, orZig.


There are, of course, rough edges to ARC. You can createcyclic references that never get freed, for example. Still, it’s (usually) fast and works pretty well. I posted this thought, and got a really interesting conversation.


![](https://substackcdn.com/image/fetch/$s_!YZvl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f723b73-ebe1-4629-a03d-a1fba90e6a5b_691x969.png)

*View Post*


I did some digging, and Swift’s evolution on the subject is interesting . It turns out thatsomeone from Appleposted anOwnership Manifestoproposing a more Rust-like ownership model more than 7 years ago. Theproblem statementsection largely summarizes the discussion above:


> The widespread use of copy-on-write value types in Swift has generally been a success. It does, however, come with some drawbacks:Reference counting and uniqueness testing do impose some overhead.Reference counting provides deterministic performance in most cases, but that performance can still be complex to analyze and predict.The ability to copy a value at any time and thus "escape" it forces the underlying buffers to generally be heap-allocated. Stack allocation is far more efficient but does require some ability to prevent, or at least recognize, attempts to escape the value.


Since the original post, it’s gonelargely untouched. Or so I thought. It turns out that there’s been more than three years of discussion on a Swift forum post calledA roadmap for improving Swift performance predictability: ARC improvements and ownership control. It’s a long and detailed history of the work going into Swift’s memory management. Work that has now surfaced in in Swift 5.9,released in September of 2023.


Swift 5.9adds a bevy of ownership-related features:

- Noncopyable structs and enums
- Consume operator to end the lifetime of a variable binding
- And—wait for it—borrowing and consuming parameter ownership modifiers


The release notes havean ownership sectiondescribing the changes:


> The new `consume` operator tells Swift to deinitialize a variable and transfer its contents without copying it. The `consuming` and `borrowing` parameter modifiers provide hints that Swift can use to eliminate unnecessary copying and reference-counting operations when passing a parameter. Finally,noncopyable structs and enumsallow you to create types which, like a class, can’t be meaningfully copied when assigned, but like a struct or enum, do not need to be reference-counted because only one storage location can own the instance at a time.


There’s alsosome discussion on HackerNews, includingthis spicy comment, “For current Rust users, if Rust kicks the bucket, Swift is a good plan B.”


I’m torn on these changes. On the one hand, I like Swift’s relatively simple memory management. On the other hand, I buy the argument that ARC can be slow in certain circumstances. Some of ARC’s edge cases happen to matter a lot when building deep infrastructure—the kind of stuff you build with Rust. Perhaps Swift has managed to thread the needle with their ownership semantics in a way that Rust hasn’t. If not,there’s always Mojo.


---


Share


---


#### Jobs

- Modal[$] - Modal is one of thecoolest kids in the AI space(and in the serverless infra space. The team has been growing and they’re now looking forAI, product, and systems engineers. They work with open source projects likegVisorand have home-grown tech built on Python and Rust.Apply hereif this is your thing.
- StarTree[$] - One of my former LinkedIn co-workers,Kishore Gopalakrishna, recently posteda mysterious recruiting request. The team is looking for, “humble and hungry engineers who want to work on a really exciting but very hard project.” StarTree has productizedApache Pinot, a slick realtime OLAP system that leveragesstar-tree indexes. Oh, and StarTree’s founding engineer is none other thanChinmay Soman, one of the first engineers to work with me onApache Samza. SendKishore a DMto work with them (they’re great).
- BlueSky- I am continually amazed at the craftsmanship coming out of BlueSky. I’m also rooting for them as a company. While reading Jaz’s recentYour Data Fits in Memory (GraphD Part 1), I noticedthey’re hiring backend engineers. They’ve got aGo backend, though Jaz ismessing a lot with Rust. They’ve also got an intriguing architecture (including *gasp* on-prem hardware). They’re having a lot of fun and building great stuff.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
