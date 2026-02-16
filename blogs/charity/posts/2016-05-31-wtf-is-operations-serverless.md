---
title: "WTF is operations? #serverless"
date: 2016-05-31
url: https://charity.wtf/2016/05/31/wtf-is-operations-serverless/
word_count: 1263
---


I just got back from the very first ever [@serverlessconf ](http://serverlessconf.io/)in NYC.  I have a soft spot for well-curated single-track conferences, and the organizers did an incredible job.  Major kudos to [@iamstan](http://twitter.com/iamstan) and team for pulling together such a high-caliber mix of attendees as well as presenters.


I’m really honored that they asked me to speak.  And I had a lot of fun delivering my talk!  But in all honesty, I turned it down a few times — and then agreed, and then backed out, and then agreed again at the very last moment.  I just had this feeling like the attendees weren’t going to want to hear what I was gonna say, or like we weren’t gonna be speaking the same language.


Which … turned out to be mmmmostly untrue.  To the organizers’ credit, when I expressed this concern to them, they vigorously argued that they wanted me to talk *because* they wanted a heavy dose of real talk in the mix along with all the airy fairy tales of magic and success.


### So #serverless is the new cloud or whatever


Hi, I’m grouchy and I work with operations and data and backend stuff.  I spent 3.5 years helping Parse grow from a handful of apps to over a million.  Literally building serverless before it was cool TYVM.


So when I see kids saying “the future is serverless!” and “#NoOps!” I’m like okay, that’s cute.  I’ve lived the other side of this fairytale.  I’ve seen what happens when application developers think they don’t have to care about the skills associated with operations engineering.  When they forget that **no matter how pretty the abstractions are, you’re still dealing with dusty old concepts** like “persistent state” and “queries” and “unavailability” and so forth, or when they literally just think they can throw money at a service to make it go faster because that’s totally how services work.


I’m going to split this up into two posts.  I’ll write up a recap of my talk in a sec, but first let’s get some things straight.  Like words.  Like operations.


### What is operations?


Let’s talk about what “operations” actually means, in the year 2016, assuming a reasonably high-functioning engineering environment.


At a macro level, operational excellence is not a role, it’s an emergent property. ** It is how you get shit done.**


Operations is the sum of all of the skills, knowledge and values that your company has built up around the practice of shipping and maintaining quality systems and software.  It’s your implicit values as well as your explicit values, habits, tribal knowledge, reward systems.  Everybody from tech support to product people to CEO participates in your operational outcomes, even though some roles are obviously more specialized than others.


Saying you have an ops team who is solely responsible for reliability is about as silly as saying that “HR defines and owns our company culture!”  No.  Managers and HR professionals may have particular skills and responsibilities, but culture is an emergent property and everyone contributes (and it only takes a couple bad actors to spoil the bushel).


**Thinking about operational quality in terms of “a thing some other team is responsible for” is just generally not associated with great outcomes**.  It leads to software engineers who are less proficient or connected to their outcomes, ops teams who get burned out, and an overall lower quality of software and services that get shipped to customers.


These are the specialized skill sets that I associate with really good operations engineers.  Do these look optional to you?


It depends on your mission, but usually these are not particularly optional.  If you have customers, you need to care about these things.  Whether you have a dedicated ops team or not.  And you need to care about the tax it imposes on your humans too, especially when it comes to the cognitive overhead of complex systems.


So this is **my** definition of operations.  It doesn’t have to be your definition.  But I think it is a valuable framework for helping us reason about shipping quality software and healthy teams.  Especially given the often invisible nature of operations labor when it’s done really well.  It’s so much easier to notice and reward shipping shiny features than “something didn’t break”.


### The inglorious past


Don’t get me wrong — I understand why “operations” has fallen out of favor in a lot of crowds.  I get why Google came up with “SRE” to draw a line between what they needed and what the average “sysadmin” was doing 10+ years ago.


Ops culture has a number of well-known and well-documented pathologies: hero/martyr complexes, risk aversion, burnout, etc.  I understand why this is offputting and we need to fix it.


Also, historically speaking, ops has attracted a greater proportion of nontraditional oddballs who just love debugging and building things — fewer Stanford CS PhDs, more tinkerers and liberal arts majors and college dropouts (hi).  And so they got paid less, and had less engineering discipline, and burned themselves out doing too much ad hoc labor.


But — this is no longer our overwhelming reality, and it is certainly not the reality we are hurtling towards.  Thanks to the SRE movement, and the parallel and even more powerful & diverse open source DevOps movement, operations engineers are … engineers.  Who specialize in infrastructure.  And there’s **more value than ever in empathy and fluid skill sets**, in engineers who are capable of moving between disciplines and translating between specialties.  This is where the “full-stack developer” buzzword comes from.  It’s annoying, but reflects a real craving for generalist skill sets.


The BOFH stereotype is dead.  **Some of the most creative cultural and technical changes in the technical landscape are being driven by the teams most identified with operations and developer tooling**.  The best software engineers I know are the ones who consistently value the impact and lifecycle of the code they ship, and value deployment and instrumentation and observability.  In other words, they rock at ops stuff.


### The Glorious Future


And so I think **it’s time to bring back “operations” as a term of pride.**  As a thing that is valued, and rewarded.  As a thing that every single person in an org understands as being critical to success.  Every organization has unique operational needs, and figuring out what they are and delivering on them takes a lot of creativity and ingenuity on both the cultural and technical front.


“Operations” comes with baggage, no doubt.  But I just don’t think that distance and denial are an effective approach for making something better, let alone trash talking and devaluing the skill sets that you need to deliver quality services.


**You don’t make operational outcomes magically better by renaming the team “DevOps” or “SRE” or anything else.**  You make it better by naming it and claiming it for what it is, and helping everyone understand how their role relates to your operational objectives.


And now that I have written this blog post I can stop arguing with people who want to talk about “DevOps Engineers” and whether “#NoOps” is a thing and maybe I can even stop trolling them back about the nascent “#NoDevs” movement.  (Haha just kidding, that one is too much fun.)


I mean how hard can it be to just glue together APIs that other people have written and support and scale? 🤔  [#serverless](https://twitter.com/hashtag/serverless?src=hash&ref_src=twsrc%5Etfw) [#NoDevs](https://twitter.com/hashtag/NoDevs?src=hash&ref_src=twsrc%5Etfw)— Charity Majors (@mipsytipsy) [May 23, 2016](https://twitter.com/mipsytipsy/status/734833335160053762?ref_src=twsrc%5Etfw)


sufficiently advanced trolling is indistinguishable from thought leadering.  [#serverless](https://twitter.com/hashtag/serverless?src=hash&ref_src=twsrc%5Etfw) [#NoDevs](https://twitter.com/hashtag/NoDevs?src=hash&ref_src=twsrc%5Etfw)— Charity Majors (@mipsytipsy) [May 23, 2016](https://twitter.com/mipsytipsy/status/734860912822083584?ref_src=twsrc%5Etfw)


[Part 2: Operations in a #Serverless World](http://charity.wtf/2016/05/31/operational-best-practices-serverless/)
