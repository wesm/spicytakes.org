---
title: "MotherDuck Partnerships and Commercializing Open-Source"
summary: "Podcast at Founded & Funded Podcast (Madrona)"
date: 2023-04-20T00:00:00
tags: ["podcast", "transcript"]
slug: founded-funded-motherduck
word_count: 2355
source_file: transcripts/2023-04-20-founded-funded-motherduck.md
content_type: transcript
event: "Founded & Funded Podcast (Madrona)"
video_url: "https://www.madrona.com/motherduck-jordan-tigani-duckdbs-hannes-muhleisen-partnerships-commercializing-open-source-projects/"
---

*This transcript was sourced from the Madrona website.*

## Transcript

Coral: Welcome to Founded & Funded. This week, Madrona Partner Jon Turow brings us a story about a partnership between two people who had never met. You'll hear from Hannes Mühleisen, creator of the DuckDB open-source project, and Jordan Tigani, the database leader who saw an opportunity to commercialize it by creating MotherDuck. They share the lightning-bolt moment that led to one of them flying halfway around the world to meet.

Jon: I'm Jon Turow, a partner at Madrona. I'm really excited to be here with Jordan Tigani and Hannes Mühleisen. Thanks so much for joining.

Jordan: Great to have the chat with you, Jon.

Hannes: Yeah, great to be here. Thank you.

Jon: Jordan, you're the founder and CEO of MotherDuck. Can you tell us what MotherDuck is?

Jordan: MotherDuck is a serverless data analytics system based on DuckDB. We're a startup that started thinking about this in April 2022 and were funded by Madrona, among others, a few months afterward.

Jon: Hannes, can you talk about what DuckDB is and its genesis?

Hannes: DuckDB is a database management system — a SQL engine. It's special because it's an in-process database engine running inside another process. It's open-source, and we've been working on it for about five years. I created it with Mark Raasveldt, my Ph.D. student at the time, while I was a senior scientist at the Dutch National Research Lab for mathematics and computer science (CWI) in Amsterdam.

I was in a group called Database Architectures working on analytical data management engines. We noticed great ideas existed but weren't having real-world impact. People weren't using state-of-the-art solutions. We talked to practitioners and found that data management, transferring data back and forth, was really a concern. The end-to-end experience mattered more than individual algorithm speed.

We started implementing DuckDB in 2018. It seemed insane—two people writing a database management system when these typically require hundreds of people over ten years. But I tend to leap without looking sometimes.

Jon: Hannes, you've mentioned getting customer feedback early on, even in locked-down academic environments. How did that impact DuckDB?

Hannes: Yes, when trying other researchers' code in restrictive IT environments—ancient systems without root access and slow admin turnarounds—I developed an uncanny ability to run things without Docker and a deep hatred for dependencies. That conviction shaped DuckDB's design: it can't have dependencies. We also talked to data scientists, which is uncommon for database researchers. They told us what they didn't like, and we iterated on our ideas based on their feedback.

Jon: Did you consider turning DuckDB into a company yourself?

Hannes: It was a push-pull situation. Our research group had precedent spinning off companies. There was also significant pull—we open-sourced DuckDB in 2019, and people started asking, "When can we give you money?"

VCs kept asking if we'd considered starting a company. We were reluctant initially, but after months of people wanting to fund us, we eventually decided it was necessary. We discussed many things: business model, process, and who to trust.

VCs wanted us to become a Snowflake, but we didn't want that. We wanted to be technology providers, staying open and flexible. We talked to successful database-as-a-service founders who described their experiences. That was clear that we didn't want to do that, so we took a different approach: accept commercial users' money and run the company traditionally.

Jordan: I spotted DuckDB while at SingleStore, looking at benchmarking reports. I saw "DuckDB" and wondered what it was and why it was so fast. I read Hannes and Mark's papers, and they resonated deeply.

Most people don't actually have big data. I'd worked on BigQuery and SingleStore, where we built complex distributed transaction features and shuffle operations for joins and aggregations. In DuckDB, in order to do these joins, you just build a hash table, and then you share a pointer to the hash table. It's so much simpler.

Beyond complexity and scale, what impressed me was the focus on the complete end-to-end experience. Most databases focus on query execution, ignoring what happens before and after. Everybody focuses on what happens once the query starts and until it finishes. But there's a bunch of stuff that happens both before and after.

At BigQuery, we outsourced JDBC and ODBC drivers. A bug added 1.5 seconds to every query. For minute-long queries, that's negligible. For BI dashboards, it's terrible. We didn't realize this was even a problem.

DuckDB is actually focusing on these kinds of problems, I think, is why it's doing so well. Someone tweeted, "Why is DuckDB so fast?" The reason is all the stuff that everybody else isn't paying attention to, they're actually paying attention to.

Jon: You immediately recognized single-box execution could work in the cloud too, where hosts are just large single machines. You also saw opportunity in complementary business-building activities. Can you comment on that?

Jordan: I came from teams at Google and SingleStore building cloud services. I know the pain and mechanics of transitioning databases to the cloud. That shapes how I think.

In my career as a software engineer, then manager, I handled increasingly complex problems. As a manager, I designed organizations like distributed systems. Moving to product management expanded my palette further. The product space is just this even broader palette of things that you can do.

What actually matters is how are customers going to interact with something? If you build a beautiful piece of technology that nobody wants, it's going to be really disappointing because nobody's going to end up using it. Even though I love technology and databases, what excites me is building products. That involves not just the tech, not just the architecture, but also all the market, the pricing, the packaging, the customers.

Jon: Let's hear about when you got on a plane, Jordan. Tell that story.

Jordan: I was really excited about serverless. A serverless DuckDB should exist. It could scale down to zero, charge per use, rebalance, and move things around. It reminded me of BigQuery rotated ninety degrees—very wide and thin versus very thin and deep.

I thought I'd hack on this. After two days, I asked a friend for an intro to Hannes and Mark. That morning, after talking with them, this seems like it could actually work. They're not doing exactly what I'm talking about, but they kind of are looking for somebody to come in and build something like this.

That afternoon, I talked to Tomasz at Redpoint. Fifteen minutes in, he said, I like this idea. I want to fund it. Come to my partner meeting. I hadn't planned to start a company—my goal was learning Rust.

The next day, another VC asked, How much do you want? I had no idea what to say. Then I met with a Madrona neighbor who brought Jon to our coffee meeting. Within 48 hours, multiple VCs were interested.

I was vacationing in Portugal. Realizing the most important thing is I need to have a great relationship with Hannes and Mark, I rerouted to Amsterdam. Hannes blocked four hours. There's no way we're going to talk for four hours. Five hours later, we've been geeking out about databases—it was just sort of a really fun conversation. We're like, oh, we've got to get to dinner, where our spouses joined us. That was MotherDuck's start.

Jon: Was Jordan the first person offering to commercialize DuckDB?

Hannes: No, but he was credible. What made Jordan stand out was his background at SingleStore and BigQuery. That he considered our scrappy single-node system serious work was a big shock to me. We'd been ridiculed for not taking distributed systems seriously, yet someone with his credentials validated our approach. That was shocking. And I think it really was clear that if we were going to work with somebody that does this, it's going to be Jordan.

Hearing about Jordan's background activities moving that fast slightly surprised me, but when we first talked, we thought we can totally do this. Things moved incredibly quickly—within days of saying yes, arrangements began.

Jordan: I worried I'd freak them out. I was very cognizant of trying not to freak you and Mark too much, given how quickly things accelerated.

Hannes: At that point, we had spoken to enough Americans. My wife is American, so I exercise this daily. It wasn't scary, I thought. I don't know. It seemed so logical and obvious that I wasn't scared at all.

Jon: There's trust evident here, but also this credibility issue. Hannes, you mentioned that Jordan's background in distributed systems, then saying "scale-up is actually pretty cool," was a narrative surprise that gave credibility?

Hannes: There was a shock to me. Yes.

Jon: That seems to have animated MotherDuck's approach, right, Jordan?

Jordan: Most people don't have huge amounts of data. Even at BigQuery, most queries weren't big. People focused on getting data in and getting data out, and the user experience of the query and using the system is actually more important than size.

You can scale up. And you can always make it distributed later. Someone will build distributed DuckDB. We have an internal bet about whether we will. I bet no. Others disagree. At BigQuery, we had BI Engine, a scale-up single-node system on top of BigQuery storage. Limited machine sizes forced us to build scale-out eventually. It took a year and three or four engineers. Ideally, you wait as long as possible, and so you get as much innovation into the core engine until you have to do that.

Hannes: This transformation from scale-out to scale-up was surprising because our scale-up idea was based on feeling. We disliked systems like Spark based on intuition. We lacked data. Only around 2020 did Google publish the TF data paper stating 95 percentile of all our machine learning job size is like a hundred gigabytes or something like that.

Jordan, you'd seen this from the inside. I feel like if you haven't seen the big data, then probably no one has. So, it made the difference for us from a feeling to something that was actually a thing.

Jon: At our first coffee, I thought about the opposite of big data. What would we do if we changed that constraint and looked at the world as it is, not as we wish it? What became possible?

Jordan: When BigQuery started, our mantra came from Turing award winner Jim Gray: With big data, you want to move the compute to the data, not the data to the compute, because moving data is expensive and hard.

Once recognizing data may not be that large, how would you design differently? Can you move data to end users and leverage their compute power? George Fraser, Fivetran CEO, ran benchmarks. A 2-year-old Mac laptop was faster than a $35,000 a year data warehouse. Laptops were once underpowered; now they're powerful. Why wait three seconds for a cloud query while your powerful desk computer sits idle?

Why not actually let that computer on your desk participate in that query? It's cheaper because you've paid for it. It's a better user experience because you can get results back in milliseconds, not seconds.

Edge, mobile, and computing where data originates offer interesting possibilities versus consolidating everything centrally.

Jon: Two things are simultaneously true: marginal compute costs are lowest in the cloud due to scale, yet adding capacity to distributed analytics systems often produces congestion within months—like adding highway lanes.

Jordan: The reason that adding lanes to highway doesn't make things faster is because what's slow is getting things on and off the highway. Getting your query in and data out are most important. Getting back to sort of DuckDB is like getting your query in and getting your data out are very often the most important things. And what happens in the middle all converges to the same place over time.

Hannes: It is really shocking to see what is possible on laptops. It's something that we have kind of forgotten about. The marginal CPU cycle cost in the cloud isn't what cloud databases charge. There's also a big difference between what the cycle costs and what you are paying for the cycle. And I think it is maybe also part of the reason why it is so much nicer to run things locally.

Jon: You've each done complementary work that makes both DuckDB and MotherDuck possible. What have you learned from working together that made you stronger?

Hannes: My life has changed from a mostly academic researcher to somebody who is running a team of competent people that are building DuckDB here at DuckDB Labs in Amsterdam. I'm learning what Jordan describes—moving from pure technology building toward broader business-building. It's been really interesting for me to see how Jordan goes about doing things. Because he's been, of course, also building his company the last 10 months at a much greater speed than we do, of course. But since this is all so new to me, it's been extremely interesting and valuable.

Jordan: At year-end 2022, I told our team and investors that if there was one word to sum up 2022, it's lucky. We're incredibly fortunate hitching our star to DuckDB and Hannes and Mark's team, given the incredible tailwinds that come behind this really groundbreaking technology.

What worries me most is doing something to screw up that relationship. Other founders commercializing open-source have warned that it's going to get hard because your incentives are going to diverge, the things that you care about are going to be at odds. We need active work and deliberate trust in being willing to say, okay, well, maybe we wanted to do this, but for the sake of the relationship we will take a slightly different approach.

Jon: Hannes Mühleisen and Jordan Tigani, thanks so much. This has been really fun.

Hannes: Thanks for having us.

Jordan: Thanks, Jon. Thanks, Hannes.

Coral: Thank you for listening to Founded & Funded. For more on MotherDuck, visit MotherDuck.com. For DuckDB, visit duckdblabs.com. Tune in in a couple weeks for another episode.