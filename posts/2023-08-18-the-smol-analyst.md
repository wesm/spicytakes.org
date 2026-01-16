---
title: "The smol analyst"
subtitle: "Maybe there’s a way to make these chatbots useful after all."
date: 2023-08-18T16:54:19+00:00
url: https://benn.substack.com/p/the-smol-analyst
slug: the-smol-analyst
word_count: 2208
---


![Netflix Announces 'Boss Baby' Animated Series](https://substackcdn.com/image/fetch/$s_!io5r!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F955754e8-f73d-4cb2-b9b1-6ef478f9fadf_1200x675.jpeg)

*Technically, this is asmol CEO.*


A few months ago,Shawn Wang, who is more widely known asswyx,launcheda viral GitHub project calledsmol developer.1At its core, the project is an AI agent for writing code, but it puts an innovative spin on what is quickly becoming a tired category: Rather than offering its users a chatbot that writes snippets of code on request, smol developer “scaffolds an entire codebase out for you once you give it a product spec.”


For example, a user might want to create a Chrome extension that blocks paid tweets.2They would write a short description of the extension, including what the tool is and details about what they want it to do—keep a counter of how many tweets it’s blocked; give me a way to whitelist some accounts; make the iconBam Adebayo. They submit the spec to smol developer; it returns the entire application.


Smol developer’s particularly clever twist is that, after it produces its first draft, it then provides a kind of feedback-oriented IDE where people can tell it what they like and don't like about the application that it just built. They can ask to change the design, request new functionality, or tell it anything that a product manager might tell an engineer after seeing an initial prototype. The bot takes this feedback, combines it with the original spec, and updates the app. And so the process continues, with the user and bot reinforcing one another—the app improves as the spec gets refined; the spec gets more descriptive as the app goes from imagined concept to testable product.


Does this work? Can it create complex apps? I have no idea. Still, the approach struck me as subtly revolutionary. Most of what’s been created with LLMs so far has either shoehorned them around existing workflows—e.g., an automated assistant in a code editor—or shoehorned workflows around chatbots—e.g., a Slackbot for writing SQL queries. Smol developer is a step outside of the lines. It doesn’t directly help its users write code; it instead uses code as a silent intermediary between product and product manager. And rather than a chatbot, there’s an interface designed specifically for drafting, testing, and improving a product spec. If LLMs do end up changing how we use computers, this type of approach—one that introduces new ways of accomplishing some task rather than accelerating old ways; the car rather than the faster horse—feels like a glimpse of the future.3


# “Make me a dashboard of song streams”


One of the small ironies of today’s SQL chatbots is that they help people do exactly a thing that data teams try to discourage. As analysts, we ask our colleagues to help us understandhow our work will be used. They shouldn’t request some piece of data; they should insteadtell us what they’re trying to achieve. And if they don’t tell us what they want to use some data pull for, the less tactful among uspepper them with demandsto explain why they need it.


Bad bedside manner notwithstanding, it’s good advice. And importantly, we don’t recommend that analysts ask these questions just to make their jobs easier; we also recommend it becausewe can’t give a useful answerwithout it.


Sowhyare chatbots different? If we have to ask a bunch of follow-up questions before we dig up some number for people, why are we excited about LLMs that mechanically do exactly that? What’s the difference?


There are two possibilities, I suppose. One is that we don’t actually need that context at all. Our back-and-forth could all be self-serving theater4to hide the fact thatwe’re mostly here to answer questions and build reports.5The second is thatchatbotsdoneedthat context. Without it, they’re just another code-free BI tool that’s useful for basic reporting, but under-delivers on the self-service nirvana that’s long been promised. But, encoding “business context” into some YAML file sounds ridiculous, and describing every detail to a chatbot anytime you want to answer a question sounds exhausting.6For this reason (among others) I’m generally skeptical that these bots willbe that revolutionary.


But the smol developer approach—treat the bot like an eager but inexperienced employee—offers a third possibility. Instead of asking for answers, people describe the report or dashboard that they want to create. The  LLM-powered “smol analyst” produces a rough dashboard, and the user provides feedback, just as they would a junior analyst. The spec gets more detailed; the dashboard gets more useful. And business context gets added indirectly, as needed, as the spec gets more precise.


Suppose, for instance, a music producer wants to figure out how anew releaseis performing.7They could write a couple paragraphs about the report they want—identical to what they’d send a data team today. They could say they want to see daily streams, streams by region, and how many people have listened to the song multiple times. The smol analyst could crank out a bunch of charts, write some loose narrative about them, and return it to the producer. Then, just as they’d do for a junior analyst, the producer would send back feedback: This number looks off; this explanation doesn’t quite make sense; can you dig into this unexpected anomaly? The bot creates another draft, the exec gives more direction, and so on.


This could have a handful of big advantages over the chatbot-based approach. First, and most obviously, it'd be more accurate than a zero-shot bot that has one chance to get the answer right.8Though today's chatbots are “trained” on prior answers, it's mostly through crude and infrequent up and down votes that only indirectly affect the underlying model. The smol analyst would instead get immediate and direct feedback on what it needs to improve, and could inject that feedback straight into a prompt.9Moreover, by gradually refining their requests, people could probably push this type of bot to answer far more complicated questions than a typical chatbot.


Second, the back-and-forth could also help peopleaskbetter questions. We often don’t know what we want until we start looking for it. Just as it’s almost impossible to write a perfect product spec without testing an imperfect prototype first, it’s very hard to ask exactly the right question before seeing the answers to a few of the wrong questions. A smol analyst would encourage this sort of iterative exploration, which is good for both user and agent.


Finally, it seems like this approach—if it works—could be applied to adjacent problems with relatively little difficulty. For example, could we create ETL pipelines in this way? Data models? Orchestration schedules? You could imagine someone describing a data model in plain language, and an smol analytics engineer using it produce some scaffolding in LookML or Malloy.


# The black box


There is, however, at least one very big reason why a smol analyst wouldn’t be as useful as a smol developer. In software,howcode works is in some sense irrelevant; all that matters is that it works. I can test my ad blocking Chrome extension without knowing a line of Javascript, or that Javascript exists at all. If the tool does what I want it to, it works, no matter how “bad” its codebase.


In data, black boxes don’t work. Computational process matters. You can’t validate a dashboard by testing that it produces a reasonable-looking chart; you have to make sure that the logic behind its calculations are correct. SQL isdeclarative, but used forimperativeends—we need to know how it works, step by step. Software is the opposite: It typically uses imperative means for declarative ends.10


That makes the test-and-refine feedback loop much harder for analytical work than engineering work. Whereas a PM can tell a smol developer that their Chrome extension doesn’t seem to be blocking video ads correctly, a producer can’t easily tell a smol analyst that their dashboard is improperlycounting skips as streams. Someone would have to review the code to know that.


One obvious solution to this is…to have someone review the code. Rather than giving every executive a personal data scientist, the smol approach could give every analyst a team underneath them. People ask (human) analysts questions; (human) analysts ask (smol) analysts for help; (smol) analysts produce the drafts, and (human) analysts review them. This is structurally similar to how a lot of data teams’ peer review processes work today, just with a lot more analysts.


# Multi-model BI


There could also be another way out of the black box. In most conversations about LLM-based applications, we talk about them as if there’s a single model underneath the product. A model writes a SQL query, for instance, or responds to a support ticket. And the product is as good as the training is for that model.


Viable, a company that automatically analyzes product feedback and has been building on top of LLMs for several years, found a different way to be successful. Instead of relying on one refined model, Viableuses a network of them, each of which specializes in a narrow task.11One organizes input data; one finds themes across those inputs; one writes summaries of each theme; one uses those summaries to author a final report that’s sent back to Viable’s users. Viable also uses ancillary LLMs to help people understand what it’s doing. There’s a model that describes the assumptions that the analytical models are making, and gives users a chance to correct them. If people want to clarify something, they explain it to the assumption model, which passes their feedback down to the analytical models, which update their work based on it.


A smol analyst could follow this same approach. When it’s asked to produce something, it could have one model describe a query plan back to the user, who could validate it or correct what it got wrong. Another model could translate queries into English summaries, just as an analyst might when they share their work back to an executive. And a different LLM could automatically create text-based data models likeTextQL’s capsulesfrom reports that were marked as correct.


Of course, none of this fully illuminates the black box. The query plan could get misinterpreted by the SQL-writing LLM, or the summary bot could get its explanation wrong. The only way to know for sure what a query or Python script does is by reading the query or Python script. But this kind of smol analyst—which, at this point, is moretol than smol—could go a long way in upgrading today’s bots from novel toys to potentially useful agents.

[1](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-1-136193385)

“Smol,”a popular social media app tells me, means “small,” but, like, in a cute way. I did not know this either.

[2](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-2-136193385)

Or, more accurately, an X extension thatunblocks unpaid posts.

[3](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-3-136193385)

I’m not saying that thisisthe future; I’m saying that it’s the future if LLMs live up to their hype. At this point, that’s an open question. My view on it has swung fromdefinitely yestoabsolutely not—so, uh, I guessBSstands for Benn Stancil?

[4](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-4-136193385)

The real self-serve analytics was the analysis we did to make it seem like we were important. (Alternative footnote: “Self-serving theater about data” isn’t a bad name for this blog.)

[5](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-5-136193385)

“Finding insights isn’t even our job. And it’s not making decisions, which is a common misconception. Because actually, our job? It’s just…numbers.”

[6](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-6-136193385)

That said,TextQL, a SQL chatbot, is trying to solve this problem in a pretty interesting way. When we define data models today, we usually default to doing it in a very structured way, like a YAML file of joins and metric formulas. TextQL throws that out, and asks its users to definecapsulesthat map questions and business topics to tables and columns—e.g., “to calculate revenue, join these two tables together, filter out these rows, and sum that column.” Not only is this easier for a human to read—including those who don’t know SQL—but it’s also probably a better way to express this information to an LLM. One of the hardest parts of building a SQL chatbot iscompressing a huge amount of schema informationinto a relatively small prompt. Capsules provide a direct way of doing that: “If you get a question about this topic, use these tables and columns.”

[7](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-7-136193385)

Y’all. It’s happening.August 31.(I think? Griff, big fan, but we gotta talk about this date format. 31.08.23? EvenExceldoesn’trecognizethat as a date.)

[8](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-8-136193385)

This highlights another irony with LLMs. With bots, we tend to fret a lot about accuracy. We don’t want to use it, unless we’re completely sure we can trust it. ButI used to be a junior analyst, and got a lot of stuff wrong—and people seemed kinda ok with that? I had to fix it, but there was some expectation that it might take me a couple tries. Why are we comfortable with that, but not comfortable with a bot that’s equally inaccurate?

[9](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-9-136193385)

Time and time again, the solution to making LLMs work seems to be “treat them like they work like a person.” That could apply here too. What would help a junior analyst produce a better report, a single unexplained like or dislike on their final draft, or immediate and direct feedback telling them exactly what to improve?

[10](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-10-136193385)

For more on declarative and imperative languages, check out this…AI-written advice column on LinkedIn?What on earth is that?

[11](https://benn.substack.com/p/the-smol-analyst#footnote-anchor-11-136193385)

Yet again, to make the most of an LLM, treat it like you would a person.
