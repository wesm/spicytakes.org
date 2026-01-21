---
title: "Keep it Simple, Dingus"
date: 2012-01-18
url: https://www.elidedbranches.com/2012/01/keep-it-simple-dingus.html
word_count: 562
---

Earlier this week, I took a few devs from my company over to visit
[Art.sy](http://art.sy/)
.
[dB](http://www.dblock.org/)
had offered to talk front-end technology choices and techniques with us, and it ended up being a very useful overview of lessons that they learned in building out their incredibly beautiful UI.
Much of the content went over my head. As you may be able to tell from the ultra-boilerplate layout of this blog, I'm not much of a front-end developer. But one thing that dB said in passing really hit home. When asked why he had chosen to use (or not use) some technology, he made the point that he wanted to keep the set of different systems he was using very limited to begin with because he thought that the architectural complexity overhead would be bad for a small startup.
I've been thinking a lot about that idea this week as I build out a new back end system to host our product data. We've already decided to go with
[MongoDB](http://www.mongodb.org/)
for the storage layer. It's easy to set up, supported by Play modules, and our ops people know how to administer it. Most importantly, it works very well for the type of data that we are sticking into it. Everything about the project has gone smoothly, and so over the past couple of days I've been trying to figure out how to do generic text search over the data. I want to use something that has all the goodies of
[lucene](http://lucene.apache.org/java/docs/index.html)
built-in, and I don't think that the MongoDB text search is going to quite do it (although using Mongo to provide fast filtering has been a dream).
I quickly found myself down a rabbit hole. Solr couldn't immediately parse the bson that Mongo spit out for our documents (not surprising), and I didn't find any easy translators online. I started looking at what modules existed in Play to enable integration with a search system and came across
[elasticsearch](http://www.elasticsearch.org/)
, then fell further down the rabbit hole trying to get the module to support not only JPA objects but morphia-generated Mongo objects. In the process I re-read articles and notes on the idea of using solr as the storage layer with no other backing store, was pointed at
[SenseiDB](http://www.senseidb.com/)
, and generally began to feel a sense of despair at the complexity of it all.
I like systems. I like to learn systems, to understand their strengths and weaknesses, to read their code. In the 6 or so weeks I've been on this new job, I've had to resist the urge to push immediately moving to a Hadoop-based analytics platform, our own distributed file system for image stores, possibly a different nosql for our user data. I realize now that I need to fight that urge even more. Using the perfect tool for every job incurs an administrative overhead and attention thrashing that an infrastructure team of 3 cannot possibly hope to manage well.
So tomorrow I'm going to take a step back and think about how I can simplify my text search problem. Maybe the answer is to just do it in Mongo for now, and save the feature/complexity tradeoff for another day. One thing is certain: right now, it's more important that I become an expert in the systems I have than pick the perfect technology for each tiny problem.