---
title: "Michael Chow: From psychology and Python to constrained creativity"
summary: "Podcast at The Test Set (Posit)"
date: 2025-09-26T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-michael-chow
word_count: 10540
source_file: transcripts/2025-09-26-test-set-michael-chow.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=Ss-xCQlp2jM"
---

{{< video https://www.youtube.com/watch?v=Ss-xCQlp2jM >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, I interview Michael Chow, a principal software engineer at Posit and creator of Siuba and Great Tables. Michael shares his path from a PhD in cognitive psychology at Princeton to becoming a Python open source developer, explaining how he wasn't sure about pursuing an academic career and pivoted toward data analysis and tool building. His work at DataCamp on grading systems for interactive exercises led him to think deeply about how people learn and analyze data.

We discuss the evolution of lazy expressions in Python DataFrame libraries, including how Siuba emerged from Michael's desire to keep pace with his boss Dave Robinson during live data analysis sessions. Michael explains how Siuba's underscore expression syntax eventually influenced Ibis, and how these projects collectively helped shape the modern DataFrame ecosystem including Polars. We also talk about Great Tables, the Python port of the GT R package, and how the growing ecosystem of specialized libraries allows projects like Polars to delegate table styling rather than building it themselves.

Michael reflects on what motivates him as a tool builder, citing the appeal of being able to "play in everyone's backyard" across different domains. He mentions transit data and the legal system as areas where data analysis has meaningful impact. We touch on the differences between analytics engineers and data engineers, the challenges of enterprise data governance, and Michael's experience working on Posit Connect and the pins package. The conversation concludes with Michael's surprising hot take: label makers are the greatest tool for artistic expression, embodying his belief that creativity thrives under constraint.

## Key Quotes

> "Statisticians get to play in everyone's backyard... I think with tools, it's sort of the same that a tool builder also often gets to play in everyone's backyard, that there are all these people doing data analysis in different domains." — Michael Chow

> "Siuba I was building to basically defeat my boss at data analysis... I need to data fight my boss to basically analyze data. He's analyzing data live in R and he's just like mocking Python. And I need to keep up with him." — Michael Chow

> "I think today, with AI, a lot of the problems I had—I'm embarrassed that I didn't know Princeton would pay for my PhD. I went to the visit at Princeton, and I didn't know that they would pay for my school. But ChatGPT or Claude would have just pummeled that, blasted that question." — Michael Chow

> "I love that Rich was just obsessed with this one activity and just digging deeper and deeper into it." — Michael Chow, on the creator of GT and Great Tables

> "If you think you have a competitor, you should just chat with them because you're two people obsessed with the same thing, maybe working for free. You might as well get a friend out of it." — Michael Chow

> "My favorite thing is when data scientists go straight into the buckets, like they go straight into the raw data. And the data engineers are kind of freaking out. And the analytics engineers are freaking out. But they're like, I just got to get this report out." — Michael Chow

> "People stunting on you with the tool you built—that's like the one nicest experience you can have as a tool builder." — Michael Chow

> "I think creativity thrives under constraint. So just having to generate words on a piece of tape, maybe with a beautified frame around it, and like 30 possible icons is actually the peak of artistry." — Michael Chow, on label makers

> "It feels like as big of a change as going from no internet to internet in many ways." — Wes McKinney, on AI's impact

> "There's going to be a growing segment of users that if you're building a new open source project, people aren't going to use your open source project until they can use it via vibe coding essentially, or until it gets indexed by the LLMs." — Wes McKinney

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field.

**Wes McKinney:** Hi everyone, I'm Wes McKinney, principal architect at Posit and co-host on The Test Set podcast. So a little while ago, we recorded and released a number of interviews where Michael Chow was the host. I was interviewed along with Hadley Wickham, Roger Peng, and Meena Cetinkaya-Rundel. But we wanted to turn the tables and interview Michael so you can learn more about him as we continue to build and produce this podcast.

So Michael Chow is a principal software engineer at Posit and a key contributor to the Python community. He received a PhD in cognitive psychology from Princeton University and is interested in what drives expert data science performance. This led him to build DataCamp's Signal Adaptive Test of Data Science Skill.

So I'll turn it over to you, Michael, to give a little brief intro to yourself and your career up until this point, and then we'll dive into all of the things that make you tick and the things that you're thinking about these days. And I've got a lot on my mind with everything that's going on with AI. So I'm sure we have a lot to talk about.

**Michael Chow:** Yeah, yeah. Excited for the inevitable AI blurb. And I have to say, as a person who works full time on Python open source at Posit, formerly RStudio, I'm a giant fan of all your work in Python, so I'm excited to be able to talk about just all data, but also what's going on in the Python ecosystem.

I guess as a little background, yeah, so I did a PhD in cognitive psychology. And I would say like a few years in, I sort of realized that I wasn't sure if I wanted to fight tooth and claw for an academic position. So I started to do way more Python and R for data analysis. And then, yeah, after graduating, I was able to go to DataCamp where I worked on sort of how do we grade people's submissions and how do instructors who are writing these interactive exercises write code to grade other people's code that they submit for these exercises? So very meta activity.

Yeah, so basically from there, I did a lot more data science into how people learn sort of on this interactive platform. And that sort of led me into like, how do I best analyze in Python and R? And then finally, I guess, took me to Posit where I'm really excited to work on open source tools around data analysis and to be able to think about what are the sort of nicest things we could do during data analysis to kind of speed people up or help them kind of go end to end from raw data to some kind of report or insight.

**Wes McKinney:** It's interesting because I found in our field of open source data science tool builders that there's a lot of people who started out in a scientific field. Cognitive psychology is a heavily statistical field where there's a lot of modeling and statistics and signal processing and latent factor models and that sort of thing. Myself, I started out in mathematics and then did quant finance and then statistics, more Bayesian statistics.

But I was also driven, attracted to the tool building aspect because of how difficult it was to work with data. And I found that just building tools and accelerating workflows and making people more productive was really satisfying. But I think it's important to have that background in science and actually doing statistics, doing data science to know what do good ergonomics look like and to be partly working to improve other people's productivity, but also from that own personal experience of having struggled with tools that maybe weren't designed the way that you would have liked.

I remember the first time that you came on my radar was through the Siuba project. And then more recently, you've worked on Great Tables and Quartodoc. And so Great Tables being a port or a reimagining of the GT R package. So bringing rich and beautiful tables to Python, which having spent a lot of time formatting and producing tabular output for pandas, it's nice that that work can be delegated to Great Tables now, because it can be extremely tedious to produce these nitty gritty tables that have all the bells and whistles. I guess you would know as much about that as anyone nowadays.

**Michael Chow:** I feel like I'm still learning a lot about that world. And for a little bit of background, I kind of joined up with this person, Rich, who did this package in R. And it is funny, I do feel like tables was not on my radar. I'd used the pandas styler a little bit, but this idea of being so obsessed with how to style a table and to produce a nice table was almost so fascinating to me that Rich was just obsessed with this one kind of singular activity.

I feel like it was really exciting to kind of be able to both ride along with and kind of figure out like in Python, how do we make it really easy to do? But I do love how these activities are super zany. Like, I feel like formatting a table is a really specific, tiny thing to get into. Like, I think most of the time when people are thinking of styling a table, it's like one of a whole giant set of things they're doing. I love that Rich was just obsessed with this one activity and just digging deeper and deeper kind of into it.

**Wes McKinney:** Yeah, well, I think it's cool also that now with the development of new data frame libraries like Polars, so in the past, we wanted to ship table rendering and plotting, table rendering, table styling, all those things in pandas. And so we built those things inside pandas, but now a library like Polars, starting from scratch, but also there's this much richer ecosystem of open source libraries. And so it's an easier decision to make to say, let's delegate out to a library like Great Tables rather than Polars implementing all of its table styling itself. So how have you found some of those types of collaborations in the open source ecosystem?

**Michael Chow:** I mean, I do think because we integrated with Polars really early in Great Tables, I do feel like it was almost kind of the perfect time, to your point, that we could tell Polars they have this thing called lazy expressions, and we could tell them like, hey, we think that if we just take the job of displaying tables and making them pretty, we can just use your lazy expressions to make it really easy to say, like, highlight a specific row, say like the row where some value is its maximum in the table, like we can do that with your expressions. And like, you can focus on how could people compute things in Polars and use a data frame, and we could just borrow this one piece and kind of like, do this job you don't want, or probably don't get a ton of joy out of.

I think you're right that it's tricky, like in pandas, the styler was kind of rolled into pandas, and that is a hard decision library builders have to make, like, can I quickly kind of provide a good enough way to do this in our tool? Should we really encourage someone else to do it? And I do think one of the challenges I'd imagine for pandas is like, once you roll it in, you sort of have to maintain it, and then if no one comes along and is really gassed up by the problem, it can be kind of tricky to keep maintaining all these pieces.

**Wes McKinney:** Yeah, yeah. And one issue that I've seen is that you also end up with a tightly coupled release process where maybe you want to be able to release bug fixes or incremental improvements in some of these presentation and styling layers, but those end up being gated. I think one of the challenges that we've seen, and occasionally it can be a frustration that whenever pandas makes a major release, and then somebody finds a bug in one of the peripheral parts of the project, there has to be like a bug release or patch release, and that can get hung up for a number of weeks.

But if you encounter a bug in Great Tables, you can roll out a new release with fixes much more easily, and that, like whereas Polars releases on its own schedule. Often, obviously, you don't want to break any APIs, that wouldn't be good. But if you encounter a bug, it's nice to be able to fix the bug and push out a new release.

So I wanted to get back to, you know, kind of maybe rewinding a little bit just like how you got involved in this field and sort of what makes you tick. So I'm curious, like core motivations, like what gets you out of bed in the morning personally and professionally, and what are some of the things that help keep you engaged in this space of open source tool building?

**Michael Chow:** When I was an undergrad, something that really appealed to me was my statistics advisor saying something like, statisticians get to play in everyone's backyard. I feel like something about that I just loved, that statistics is used in so many fields that you can sort of collaborate broadly across a lot of different fields of research.

And I think with tools, it's sort of the same that a tool builder also often gets to play in everyone's backyard, that there are all these people doing data analysis in different domains. And I think what gets me up is I've really liked diving into a few domains where I feel like data is used for incredible impact. So I think, for example, the legal system, I think data is used incredibly creatively and for public good oftentimes by nonprofits.

And then I think the other one is transit. I think public transit's a really nice area where data, we interact with data all the time, like when's my train coming? When's my bus coming? And advances like real-time tracking and all that have gone super far. But also being able to report like how busy is our network where and design affected transit networks I find to be a really impactful data problem.

So I think as a tool builder, I've really tried to kind of ground myself in different areas and I don't know if you ever felt this way. I think sometimes the longer I spend in open source tools, the less I actually do data analysis. So I've really tried to kind of like, yeah, I just need to touch grass and analyze some data. And I think those fields have been really fun and interesting to follow because I think a little bit of data analysis could be super impactful.

**Wes McKinney:** Yeah. Yeah. For me, one of the challenges also is that the feedback that you get from the open source community tends to be fairly delayed. And I think for some new open source contributors, that can be a little bit discouraging. But the reality is that it takes a while for the software to trickle out and for people to learn how to use something new. And my experience, six months is my expectation for when I can expect to really start getting some feedback about building something new. And so I'm wondering what your experience has been like that, both on the positive and negative.

**Michael Chow:** It's an interesting question because I think you're right that if you're putting open source tools out, it could be quite a long time before someone picks it up or you might even be frustrated and notice like nobody's picked it up. Your biggest risk maybe is obscurity sometimes.

But I do think one interesting kind of in-between that I've experienced is helping build tools internally in organizations. So I think there are a lot of sort of tool builders that aren't, they're not quite doing open source, but they start sort of internally inside a company building a package that does a thing and then they have really good feedback loops with this team that's using it in the company. And then maybe after a while, they kind of bring it into open source or it inspires a tool similar to that. And I find that arc to be really powerful where you can't be precious about it. You're building this tool for a specific group of people in your company. And so you get some of that kind of hustle of getting things out for them.

And I will say Siuba was a little bit like that. So yes, for some background, Siuba is a tool to analyze data in Python and it's sort of like wrapped pandas. And I would say its big thing is that it implemented lazy expressions so that you could say what you want to do.

**Wes McKinney:** Yeah, the way I describe it to people is dplyr is a library that Hadley Wickham created for R, which provides these lazy table expressions. And so I had created a project called Ibis, which was similar concept, but wasn't trying to pattern match or implement the exact same API flow as dplyr. It was its own portable data frame API, whereas I think what was cool about Siuba was if you had used dplyr and were working in Python, you could pick up Siuba and see the same concepts expressed. And you could work between dplyr expressions and Siuba expressions fairly comfortably.

**Michael Chow:** I think this is such a good example because Siuba I was building to basically defeat my boss at data analysis. Ibis had been out for a couple of years.

**Wes McKinney:** So you got nerd sniped, essentially.

**Michael Chow:** Yeah, yeah, by some kind of spite arc against my boss. But I will say just to foreshadow, I mean, I think today Ibis is probably like if people said, should I use Siuba? I would probably just point them to Ibis. And essentially, I do think a lot of it boils down to Ibis did implement lazy expressions. And in the PR, they mentioned like Siuba has these lazy expressions using underscore. Would it be useful? And I think at the time I was like, oh, that's interesting and neat. But now I feel like I really appreciate the Ibis team and respect especially Philip Cloud and your work.

But that team, I find really great, like Siuba was built as a kind of internal tool that then I brought into the world. But I think that I also love that Ibis and Siuba interacted and the result is actually something very nice to use.

**Wes McKinney:** Yeah, I mean, I think it was cool because there was a period of time where Ibis was in early development, like the first started around 2015, the first, say, five years of the project. But I think there was an era where the Python community was trying to figure out this lazy table expression API, like what is a good API? What do good API ergonomics look like? How do we get around the limitations of not having nonstandard evaluation?

So that's the feature in R where you can refer to—you can late bind variables based on the context. An expression inside of a function call, you can refer to column names in a data frame. And so within the evaluation layer, those are late bound to the physical columns within the table, whereas in Python you have to create actual objects that either are the column or are an expression object that can be composed with other expressions.

So I think there were a bunch of projects. So there was the Blaze project at Continuum Analytics, now Anaconda. And then I started Ibis and then Siuba. And so I think that cross pollination of ideas and the underscore expression builder was really cool and something that eventually got adopted in Ibis. But I think we emerged with some really nice tools on the other end.

And I think that all of this work definitely, directly or indirectly influenced the design of Polars and Polars' expression system, which I think works really well and people seem to be happy with.

There's another new project, Narwhals. I don't know if you've looked at Narwhals, but it's basically a Polars API compatibility layer for different backends. So it's like Ibis but if Ibis had the Polars API a little bit, which is cool. But I appreciate the goal there of wanting to simplify.

Yeah, I see all these projects as being part of a collective open source community effort to try to reckon with what do good ergonomics look like for lazy table expressions and data frame, efficient data frame operations across different types of backends.

**Michael Chow:** Yeah, I do think they've all kind of wrapped around that concept. In 2025, lazy expressions have kind of emerged in every tool. Pandas just added pd.col in the spirit of Polars. So they have their lazy expressions.

Yeah, I think to tie it all back, the Siuba story is in 2019, I need to data fight my boss to basically analyze data. He's analyzing data live in R and he's just like mocking Python. And I need to keep up with him. I think today, hopefully it'd be like Narwhals or Ibis, just kind of keeping pace.

I do remember, yeah, Dave Robinson's coding live streams and demos at meetups and things. So when I used to live in New York City, I would often see Dave at New York City data science meetups.

**Wes McKinney:** Yeah. So he was definitely a fixture in that world.

**Michael Chow:** It's also kind of cruel, too, because he's like an animal. He just goes so fast and he's just talking as he goes. And if you're not like—if I'm in Python and I can't keep up, I'm just—he's just pummeling me. He's like, you can't do this, but I'm just like having a good time.

**Wes McKinney:** Totally. Well, into a slightly different topic, going back a little bit to some of your origin story, was there a pivotal moment or experience that nudged you into the field of statistics and data science? Just thinking back, before you turn into the person you are today, what were some of the experiences that you feel put you on this path?

**Michael Chow:** Yeah, I've been thinking about this a lot because I visited my undergrad advisor, Candy Hurley, a couple weeks ago. And well, maybe I can start with the three most surprising things I tell people from undergrad, which is, I failed my first year of undergrad, just beautifully. I had like a 1.8 GPA, I ended up going to Princeton by the support of these really great mentors. And I think that I really had no idea how I was going to dig out. After I failed my first year, I found it so hard. And I remember my dad asked me how I was going to pay for Princeton, not—none of us realized that Princeton funds PhDs, like, it's fully paid and has a stipend.

So I think, to me, the most pivotal moment into data was connecting with my undergrad mentors. So Candy, who was in psychology and Dwayne Derryberry, who did stats. And just realizing how helpful professors are and how, getting so much support from them, just to figure out what grad programs were like and how to even pursue statistics.

But I will flag, I think today, with AI, a lot of the problems I had—I'm embarrassed that I didn't know Princeton would pay for my PhD. I went to the visit at Princeton, and I didn't know that they would pay for my school. And I only found out from my host, Fowder, that it's funded. But I think they kind of take for granted that it's obvious. But ChatGPT or Claude, I think would have just pummeled that, blasted that question.

**Wes McKinney:** Yeah, I mean, it's amazing how today with AI versus internet pre-AI is almost as big of a difference as—I mean, yes, you could have looked things up on Google or whatnot, but it feels like as big of a change as going from no internet to internet in many ways.

And this gets a little bit into the next topic that I wanted to talk with you a little bit about, and it does start to tie into AI. So I promise I'm going to get to more of the AI topics.

But as the Python ecosystem has expanded so rapidly in recent years—I started out building tools that I thought were for my idea of what is a data scientist. But now, if you look at people that are using Python, there's so many different types of business functions and roles. There's data engineers, there's AI infrastructure engineers, AI engineers, there's people doing machine learning and more modeling type work. And the way that people work and their level of technical ability and the other types of tools that they're using can vary so much.

And so I think for open source tool builders, it creates this challenge of who are you building for? Or who is your primary audience? And even like, what is a data scientist now in 2025? Is that even an outdated or old fashioned term at this point? So how do you think about what is a data scientist today? And how do you feel like that's changing with everything that's going on with AI?

**Michael Chow:** I think today, especially more and more so than six years ago, a lot of my thoughts are almost switching between how I thought of data six years ago, which was sort of using R or Python to take raw data and to put out a report or a dashboard or a model. And all of these tools could query databases. So if I had to, I could hit our warehouse as part of the process.

I think I switched between to give that kind of raw data to dashboard or a little dashboard warehouse in between to thinking about the dbt Labs community and this ELT analytics engineer data modeling world, where actually transforming data in the warehouse is this huge activity. And it's not just the coding of it, it's also the design of the warehouse.

And I think that thinking between those worlds, I find really interesting. I noticed that the analytics engineering community is much more focused on BI tools. So business intelligence, where there's often a UI where it's really quick to make plots and dashboards. And I would say, if you think of tools like Great Tables, it's a kind of funny example, because I think that a person who's using BI tools is probably not going to use Great Tables a lot, because they already are in a platform that has some way to format tables for them. But I think the challenge is, if that BI platform doesn't format the table in the way you want, or if it has kind of funky ergonomics, it's often hard to break out of the platform.

So I would say I've been thinking a lot about these two worlds. But a lot of the tool building I've been doing is still more focused on R and Python data scientists, who maybe are just trying to take raw data and churn out a report or a dashboard. And can use coding to kind of dune buggy over rough edges, or to get different tools to kind of do stuff that BI tools might sort of struggle to do.

**Wes McKinney:** Yeah, it's definitely something I've thought a fair bit about, especially being back at Posit the last couple of years, and I've gotten involved in doing development on Positron. So the new data science IDE, development environment that Posit has been building for the last few years.

And so it's interesting, because Posit as a company is still very focused and tends to remain focused on that data science archetype. So somebody with scientific skills is doing data analysis, data visualization, modeling, but also technical communication and needs to be able to build reports, static reports, interactive reports, maybe they're authoring some type of document that's going to be published. So there's many different publication modalities, but also they're still very involved in writing data analysis code doing interactive exploratory computing.

And so it's interesting to be building tools that are designed for this archetype, while there's all of these other very critical types of archetypes that are operating in the Python community, in particular, like the analytics engineers who are using dbt and tools like dbt, analytics engineering and data engineering. I'm not totally sure what's the difference. I'm sure somebody could explain to me it might depend on whether or not they interact with semantic layers and semantic models or how much they're interacting with dashboarding systems.

**Michael Chow:** I did a little consulting before joining Posit on with California Department of Transportation on a pipeline. And I do feel like that was what kind of demystified a lot of these roles for me, I ended up having to get a lot more into dbt and ended up going to Coalesce and almost like running into people there was so helpful.

But I do think coming out, meeting some of the data engineers and analytics engineers, I do feel like the big difference was data engineers could ship data through pipes, but they don't really care what the data is, they're like, pipe the data, whatever. And I'll think about it just enough to help you pipe it. Whereas analytics engineers, once it's in the warehouse, they just think so hard about the SQL transformations, and the representation and data marts.

**Wes McKinney:** Right. Yeah. And there's a big focus on semantic layers, like what are the metrics, essentially creating the higher level concepts to map onto the BI tools.

**Michael Chow:** Yeah, but I've never really wrapped my head around it completely in the sense that I've always wondered, are there a lot of problems where this kind of handoff struggles, like having a data engineer do the pipes, having an analytics engineer do the transforms, is this kind of handoff leaving some kind of really high leverage analyses, or putting it into kind of an intense pipe, where we're fire bucket style handed down.

And I do think that's the big difference in how I really like to work is that my favorite thing is when data scientists go straight into the buckets, like they go straight into the raw data. And the data engineers are kind of freaking out. And the analytics engineers are freaking out. But they're like, I just got to get this report out.

**Wes McKinney:** Yeah, makes sense. So these days, what are you actively working on right now? And what sort of tools do you use in your day-to-day activities?

**Michael Chow:** Well, so one thing is we're running—this is maybe a funny thing to mention for open source tools, but we run an annual table contest and plotting contest. So any tables you create in R or Python, or honestly, you could create the table anywhere. We just want submissions of cool, interesting, beautiful, publication ready tables.

I think we're taking submissions through early October. So it's the Posit 2025 table contest. And then plots, we did this last year, just looking for plots using plotnine, to make beautiful visuals.

But I'll say I actually love these contests, because it's just nice to see what people can do. And it's such a good reminder that people are better at using my tools than I am. I feel like that's the one nicest experience you can have as a tool builder is people stunting on you with the tool you built. So I'm excited to get stunted on two months from now.

I guess the other thing I've been looking at is, this is a kind of small thing to think about, but it's just this very tiny activity, auto completing the column names of your data frame in lazy expressions. It's more become a side obsession of seeing in all these different platforms, in the different places I can be within the platform, how and when do they auto complete the names of columns.

And I've been really interested in JupyterLab because I can control the suggestions it gives. But actually, the range of IDEs, it's an interesting issue because a lot of IDEs roll their own tooling to just handle data frame specifically. There's data frame specific code, or something that detects if you're using pandas or Polars. And I've always found that kind of funny that there's a million ways to auto complete a column name, but oftentimes it just doesn't happen yet in Python.

**Wes McKinney:** Right. Yeah, or you know, especially when people are writing these cascading, chained expressions and things like that. So you don't want to make an incorrect suggestion or something that isn't going to bind correctly.

I know one thing that we tried to do in Ibis was to constrain the column methods that are available based on the inferred type of the column. If you infer that this is a number or this is a string, then only string methods will be available on that expression object or only numerical. You can't call, you wouldn't want to call square root on a string, for example, or you wouldn't want to call dot contains or dot lower on a number.

But that also can be limiting. And there are situations where you can't necessarily, or might be challenging to infer the type of an expression. And so you don't want to paint yourself into a corner too much to just make things work for the user.

**Michael Chow:** Yeah. It's such an interesting dynamic of what do you offer? What do you take away? How close can you get to something? The risk of the map is not the territory. If you try to model the database really hard, but it turns out databases are really quirky, just the act of trying to take away options that shouldn't exist can become a really quirky problem. Just given the unpredictability of databases or their edge behaviors, things like that.

**Wes McKinney:** Right. I feel like that was one of the fun parts of Siuba. And I know Ibis has a tiny note, which is like cursed knowledge, which is some incredibly cryptic piece of information you learn about a database that you wish you didn't have to learn.

**Michael Chow:** It's called cursed knowledge. You end up stubbing, shooting your toes off on the same problem too many times. It's good to write down things that you wish you didn't have to commit to memory.

**Wes McKinney:** I've probably, if I thought about it, there's plenty of things—hard lessons learned that I wish I didn't have to learn, or I wish I didn't know so intimately.

**Michael Chow:** Yeah. I do think that it also hits on when you're designing tools, the pure relief of delegating to the user the figuring out of some aspect of the tool, like just being able to point them to—for example, that case, to be able to say, we aren't going to model the column types. But some of the things that you can express can't happen or might produce an error. But at least now it's your job to figure out, do these things, which you can say kind of error out versus not being able to say them at all.

**Wes McKinney:** I know one of the tricky things in Ibis is that there are some operations which are permissible in certain backends, but not in others, or maybe in some backends, there needs to be an explicit cast introduced in order for the operation to work. And so I think what the project has tried to do is to make things just work, but in a way that is safe, or it doesn't lead to potentially shooting your toes off.

But in there, I'm sure that there's ways to cook up diabolical expressions where it will execute correctly in one backend, but in this certain edge case with the certain kind of input data, it might error in another backend. But that's just one of the frictions that comes into play, the little subtle differences between different backends.

Ibis supports more than 20 different backends. And so there's bound to be certain incompatibilities or ways that you can concoct expressions, which don't work in a totally consistent manner. But I think at all times, there's the Zen of Python mantra, in the face of ambiguity, refuse the temptation to guess. And so I think we've tried to apply that mantra and not doing something that aspirationally would make something work, but potentially could yield errors or incorrect results in some small fraction of cases, because that would generate bug reports and unhappy users. Certainly.

**Michael Chow:** Yeah. And that's kind of how I knew—I love the Ibis team, which we met at, I think we met for the first time at SciPy and we were chatting a little bit. And then I feel like inevitably what happened was a few hours of just database quirk talk, like what things that keep us up at night when you try to translate something to different databases, like when you rank something, where do nulls go?

I feel like that was so nice to be able to nerd out. I feel like that's how I knew we had to put a ring on it that the Ibis team was sort of like my ride or die.

**Wes McKinney:** Yeah, no, it's a great team there. And I think in general, I've had just really wonderful experiences working with the pandas community. Philip Cloud, who has led Ibis for a number of years, we met through the pandas community. And so it's a really cool group of people.

**Michael Chow:** I will say too, one thing I often tell people working on open source libraries is if you think you have a competitor, you should just chat with them because you're two people obsessed with the same thing, maybe working for free. You might as well get a friend out of it. Cause you probably obsess about the same kinds of things.

But I do find sometimes tool creators are a little bit hesitant to chat with each other if they do similar things, just because I think that, I mean, we often create our tools in reaction to other tools, but at the end of the day, it's nice, I think, to just chat and realize that we have so much in common.

**Wes McKinney:** Yeah, I totally agree. Just being proactive about reaching out, proactive about communicating because open source, the whole intent is to be collaborative and not competitive. I know that people often ask me, Wes, how do you feel about Polars? And my answer is always, of course, learn Polars, but there's extraordinary amounts of pandas code in the wild and LLMs are really good at writing pandas code. So knowing how to use pandas is also a good idea because—so learn them both.

And I'm happy to see that there's innovation happening in DataFrame libraries and especially Polars is Arrow native. So that's the memory, kind of fast DataFrame memory representation layer that powers Polars and a bunch of other new open source projects. So I'm here for all of it.

But I guess the segue into somewhat related topic—firstly, I'm interested what AI tools you use in your day-to-day work. I'm curious, what are your daily drivers? And then after that, I think the next topic, after we talk about your tools, I'm really curious—a big thing that's been occupying a lot of my mental space lately is what open source development is going to look like for the rest of our careers, because it feels like this is a pretty permanent inflection point and how we approach tool building when everyone is now working in this more AI first fashion, where if they—if the LLM can't help them with something or can't suggest tools, if they want to use something, if the LLM doesn't know how to use that tool already, they're just not going to use it. They're going to use something that's in the training set for the LLM.

So I guess let's start with kind of what does your stack look like? What AI tools have you learned to so far you can't live without?

**Michael Chow:** I think, well, I will say my first tool in the LLM AI stack is Dread. You know, that I know that I should be learning tools and that there's actually so much out there that I feel like I'm very motivated right now to really dig a lot deeper.

I'd say Copilot, I use quite a bit for autocomplete. I was using Cline for a long time, every once in a while.

**Wes McKinney:** And what does Cline remind me again? I haven't actually used it.

**Michael Chow:** Yeah. Cline especially really early on. So Cline's an agentic assistant that can execute actions for you in VS Code. So it's a VS Code extension where you can ask it to do something and it will be like, should I write this code to this file?

And I think Cline—there's a fork of Cline called Roo Code, which I think a lot of people use now.

**Wes McKinney:** Yeah. That rings a bell.

**Michael Chow:** Yeah. And I don't doubt that there are going to be forks that end up being more compelling or people will move around. I think Cline was before Copilot had agentic mode. So it was sort of like a precursor to that.

But I would say I do a lot more Copilot autocomplete. Definitely Claude and ChatGPT, just quick question asking. And then I do use from time to time Chatlas, which is the—Posit's open source, kind of chat interface. And I find that is really nice for quick LLM interactions that you can code. So you can stitch together kind of workflows and interactions.

It's not—I feel like what I like about it is it's not like here's a million Lego pieces to create agents. It's like, here's chatting. You can, I think add images or audio, but it's a pretty simple interface.

**Wes McKinney:** The way I think of Chatlas is that it's like a port of the Elmer package for R, but it simplifies the whole process of using these different APIs and interacting with the LLMs, which if you're doing it from scratch can be a little bit tedious because every API has slightly different API incantations.

**Michael Chow:** Yeah. And I think that a lot of the other tools I've looked at are sort of like get ready to build a very production grade or get ready to build something. Whereas I feel like Chatlas is like a few actions and you're kind of up and running, which has been nice. It's almost like imagine the ChatGPT web UI or Claude AI UI, but now you're chatting from your console and you're able to take the responses and add a reasonable number of tools using Python code. It's sort of like just the right maybe level of customization.

**Wes McKinney:** So how do you feel—one thing that I've been thinking about a lot is that there's going to be a growing segment of users that if you're building a new open source project, people aren't going to use your open source project until they can use it via vibe coding essentially, or until it gets indexed by the LLMs. And like it reads the documentation and all of the example code it can find on GitHub and learns how to use your library.

And I've talked to people building new open source projects and they'd mentioned to me, they can pinpoint an exact point in time where their project got picked up in the training sets for Claude or for ChatGPT, the OpenAI models. And then they see this massive increase in usage, like installations on the Python package index or bug reports and things like that.

So I feel like that is going to have a major impact on folks like us that build new open source projects, that many people are going to be put off of really engaging with a new open source project until the LLMs know about it. But that also creates this chicken and egg problem where how do the LLM providers decide which projects to include in their training set and to index—I don't know what the right term is, but I called it index.

So I don't know how much you thought about this or how you anticipate this will change the way that you think about and build new projects, especially for the Python ecosystem.

**Michael Chow:** Yeah, it's a good question. I feel like it's something that we will have to reckon with. How will people find our tools and will the kind of way they're using and coding now, will our tools afford them the ability to use them sort of out of the box?

I'm so haunted by the challenge of just getting in front of a group of people and finding the challenge of zooming in, finding a person who is willing to use your tool every day, who you can talk to and see their frustration. I almost feel like the LLM issue just adds another thing to our plate, which is how will that person be able to interface with your tool?

But I guess for me, I've thought of so much of the challenge is just getting into a room with the right people that I suspect that will continue to be a big factor, maybe less so for really shooting your tool into the atmosphere in terms of popularity, but in terms of just being sure you're building the right thing. I just find it so hard to get into a room with people sometimes and watch them use the tool that I think that has stayed my north star.

But I do think the challenge of if it becomes hard for them at all to use your tool, I would want to be able to see that pain. And I don't doubt that in the next year or two, that is something that they'll hit. But yeah, I don't know. I think for people really going big though, this will be a big piece.

I know Polars, you mentioned, has this issue a little bit where I don't know how it is now. But autocomplete or suggestions for pandas do tend to be a bit better. Sometimes Polars suggestions are just straight wrong.

**Wes McKinney:** Which is—yeah, there's a combination of maybe API changes and the LLM is having outdated knowledge of Polars, or maybe it's the training set is a year old, or it's six months old, something like that. But sometimes there's just outright hallucinations. And because there's not as much training data from the internet and GitHub and whatnot, for Polars as there is for pandas. So probably I would guess that the incidence rate for hallucinations with Polars APIs is more significant, or maybe not hallucinations, but wishful thinking, like, wouldn't it be nice if this method existed?

I guess you could take the hallucinations and turn those into feature requests for Polars. Why not? Yeah, just make it real.

**Michael Chow:** But I do think you're right. I think, just to answer your question, will this challenge of LLMs indexing your tool and being able to give the right answers—I think to me, it is, all really, the signal to me is once I start seeing people battle this, getting bad advice, I think usually that's what sends me down these rabbit holes. And unfortunately, I haven't seen it yet. But I kind of know, I do think it's coming. So I do kind of dread that. But I don't think it's quite hit.

**Wes McKinney:** Yeah. Yeah, well, it's gonna be definitely very interesting. I think the field is going to be permanently different, but maybe not necessarily in a bad way. So I'm an avid user of AI tools myself. I can't live without Claude Code. I'm addicted, totally on the max plan and everything.

But yeah, I'm optimistic. And we'll see where things go. And I'm confident that there will still be work for folks like us that need to continue to build and innovate in open source.

But on a separate but related topic, we're both at Posit. Posit builds a large portion of engineering, builds open source software for data science, open source projects that we want to become freely available, widely adopted, but we also build professional products to empower enterprises to do open source data science and keep up with all of their security and compliance requirements and data governance and all the bells and whistles.

And so I'm curious, in your time as an engineer at Posit so far, what are some of your reflections or learnings on the common pain points that you see amongst users of Posit's pro products and basically the intersection of open source and business.

And I've found that a lot of open source developers maybe don't think too much about the practical issues that arise inside a business setting where you have teams of dozens or hundreds of data scientists that need to be able to work together and productively adopt the software and use it as part of their day-to-day work.

**Michael Chow:** Yeah. The enterprise is so interesting that I feel like a lot of people talk about innovation and the enterprise and tools doing really fancy things in the enterprise. But for me, the thing I find most compelling and surprising is that I feel like for an enterprise team, the number one thing I hear is I can't just do normal things.

Suddenly there's compliance, there's an IT team, there's a lot of hurdles in a business, especially a big business where suddenly even running Docker on your computer or working outside of a hosted Jupyter notebook, suddenly these things become a problem.

And so I think that it's interesting because when I came into Posit, I came from working, building out a data team for the government, for transit. And that was a very different place where we're hosting Jupyter notebooks for analysts. They can't run Docker on their machines, but we can run services for them. We're really working around to build these good pipelines that also really meet their analysts where they are.

And the first project I took up was pins, which is this tool to basically save data different places, and to really easily be able to say, okay, I have this thing called a pin board and I'm pinning my datasets to it. And basically every time I save or pin a new dataset, it saves the old version of the dataset. So it's really easy to share.

**Wes McKinney:** I mean, it's kind of like a caching solution for, let's say if you're building an R Shiny application or a Streamlit app or something, and then publishing it to Posit Connect. And you don't want to keep running the same expensive SQL query every time somebody runs the dashboard. Is that mostly the type of use case that you see?

**Michael Chow:** Yeah, I think so. Or even—I will say Ibis uses it now or did after we met at SciPy because they had example datasets and they were like, we want to fetch these example datasets, but we also don't want to fetch them every time. And so it just so happened that caching was kind of good enough in pins that they were like, we like the idea that you solve this and we don't have to figure it out.

**Wes McKinney:** Do they now have basically an S3 based pin board or something like that? And that's—yeah, that's cool.

**Michael Chow:** Yeah, I think so. So it's easy for users because you just say, fetch this pin and you have the data and you can list out your pins. So these are each of your datasets on this thing called the board, which is kind of like a folder.

But I will say in business, one really interesting use case I noticed is that—so Posit Connect is this publishing platform to run your reports and host dashboards and stuff.

**Wes McKinney:** Publishing platform. Yeah.

**Michael Chow:** Thanks. That's a much better word. I feel like I'm very much a freestyler when I'm describing things.

But I was really confused why we were implementing pins over Posit Connect. And in fact, I was like, this concept makes way less sense to me than pinning to S3. But one thing I realized is that data teams in large orgs with big IT groups, they might actually struggle to get an AWS bucket or something. So if they have Posit Connect, if you can let them pin data to Posit Connect, they don't have to battle their IT team to get say AWS buckets.

So it's this funny situation where it's like pinning, pins works good enough with Posit Connect. And as it turns out, when you can store data on Posit Connect, you can really work around a lot of maybe requirements from your IT team and just have things in one place. It's just really convenient when you're just trying to put up a report.

**Wes McKinney:** I think I know that one of the things that is interesting for me to get exposed to are some of the data governance and IT security concerns that businesses that have really sensitive data, maybe there's government compliance issues. And Posit has customers all around the world. And so every government has different data handling compliance requirements.

And so to have a publishing platform where you're publishing data and results and reports and things like that, it's really important to make sure that the wrong person doesn't access the wrong data, essentially. But in open source, we don't often, we don't really think too much about that. We're just building the tools and then we see it a little bit as somebody else's problem to figure out how to use those tools in a business environment that isn't really quite as much anything goes.

But for me, it's really insightful to be in touch with those, to see those challenges and to hear from, to talk to business users doing open source data science, especially since R and Python have seen over the last 10 to 15 years, there's been a big migration from proprietary software, things like MATLAB, SAS, SPSS, basically commercial computing platforms to open source, which is great.

But I think one of the roles that Posit has played has been filling the gap in terms of building the missing enterprise layer to handle single sign-on and the permissioning objects and published reports and things like that, as well as the building and hosting the development environments.

**Michael Chow:** And it is, yeah, it is so interesting because I do think data teams and especially people analyzing data are sort of pinched sometimes between a rock and a hard place where maybe there's compliance issues limiting where they can be and, or they need to be able to restrict who has access to what. But on the other end, I feel like sometimes I see data engineers and analytics engineers going crazy saying, oh, you got to put this in the warehouse. You can't just be pinning data. This actually needs to be part of the pipeline.

And I think that's actually kind of the beauty of Posit Connect, which is let analysts cook. Maybe they do have to move things back into the warehouse at some point, but I think that just facilitating that movement, let them at least store data for now and be able to support who can access it. So they have the luxury of time to migrate back into a pipeline, or maybe they put out a report and nobody's interested in it. And then they know we don't even need this in our pipeline. That's actually the best outcome because now you saved an analytics engineer some work.

But I feel like so much of it is that tension of business requirements, constraints, and then also just being able to move and do an end-to-end thing when there are sometimes centralized business forces trying to get you to move things upstream or really build out rigorously a data role.

I think that's why I love Posit Connect is I feel like you can quickly go kind of end-to-end, soup to nuts. Even if you're digging around the buckets and a data engineer is going crazy, you can see, is it useful to even look at the data this way?

**Wes McKinney:** Yeah. Cool. Well, I think we're getting pretty close to wrapping here. So I think I'll end the interview with let's call it the hot takes section. So curious, any top of mind hot takes or controversial opinions nowadays.

**Michael Chow:** For data or just in life?

**Wes McKinney:** It's totally up to you. It doesn't need to be data science, data science tools related. It doesn't need to be AI related at all. It feels like all content nowadays has become AI content. So non-data or AI related hot takes are totally okay as well.

**Michael Chow:** Maybe in a world of AI, this is a hot take that I feel like the people need, which is, I think that label makers are the greatest tool for artistic expression.

Meaning, in a world where you can generate anything, I actually think creativity thrives under constraint. So just having to generate words on a piece of tape, maybe with a beautified frame around it, and like 30 possible icons is actually the peak of artistry. And I think that so much of my work is inspired by artists that they take less and they do more. They just beautify anything they touch.

And I think that that's part of the challenge is how are we going to constrain—what does a good constraint do for me? And yeah, I'm a big fan. So we actually have a label maker at our house, but I left it downstairs. I can get it. I'm just saying, if you need a demo, just give the word, Wes.

**Wes McKinney:** That's all right. I admit that I also weirdly adore my label maker. And I don't know what—I think I went, I was probably 35 or so before I got my first label maker. And it was a little bit of this feeling of where's this been?

Yeah, so now I'm putting labels and labels on everything. And I do, it's something that, it's a small thing, but I appreciate its simplicity and its utility.

I've been learning a little bit of Japanese and I was thinking that I should seek out a Japanese label maker because the label maker I have, I think it's a Brother label maker. And it doesn't have the ability to write hiragana or katakana. And so I was thinking that I should seek out a Japanese label maker just so I can put little labels on things to remind myself of what that's called.

**Michael Chow:** I feel like the big question, do you have the—is it phone only, or do you have the tactile keyboard? Because people care a lot.

**Wes McKinney:** The tactile keyboard, yeah. Probably, yeah. Maybe the phone would be a better way because then you could probably input non-Roman character sets and whatnot and it would print it. So I'll look into that.

**Michael Chow:** Yeah. Game recognized game. Cause I started with the purely phone Bluetooth label maker, but nobody would use it at our house. And I actually had to switch to the tactile label maker because as it turns out the people in my house will not—they want the keys. The keys are so important.

**Wes McKinney:** I admit it's satisfying. I'm not gonna argue with it.

**Michael Chow:** Yeah. It slaps, it hits analog for sure. But yeah, there's a lot of cheeky notes around our house. I feel like that's the beauty is you can put your opinion on anything. And sometimes the names you call things are important messages to people.

So I feel like if people out there have not got a label maker in their life, I highly recommend it as just a soul enriching practice.

**Wes McKinney:** Yeah. I will keep that in mind and maybe give me some inspiration to be a little bit more creative with my labeling. I'm curious if Hadley has a label maker. That's like the big open question. Now we're like two for three.

**Michael Chow:** So yeah, I guess we'll have to find out on a future interview when Hadley joins us.

**Wes McKinney:** Yeah. Well, Michael, it's been a pleasure. So I appreciate your time and the conversation. And I look forward to doing more of these as a co-host on The Test Set. And so we will see you on a future episode and thanks everyone for tuning in.

**Michael Chow:** Yo, thanks so much. Yeah. So nice to chat.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio Agi. For more episodes, visit thetestset.co or find us on your favorite podcast platform.