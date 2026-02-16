---
title: "Alenka Frim: What yoga teaches us about discipline and collaboration in data science"
summary: "Podcast at The Test Set (Posit)"
date: 2026-02-09T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-alenka-frim
word_count: 10201
source_file: transcripts/2026-02-09-test-set-alenka-frim.md
content_type: transcript
event: "The Test Set (Posit)"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow, Hadley Wickham, and I talk with Alenka Frim, a data engineer, Apache Arrow committer and PMC member, and Iyengar yoga teacher. The conversation starts with what makes an open source community healthy. I note that healthy communities add and retain people, and that members feel comfortable raising concerns constructively. Alenka highlights the respectful communication culture in the Arrow project and credits the Apache Foundation's structure for setting clear expectations.

We discuss what Arrow is and how it has spread across the data ecosystem. Alenka explains Arrow as a specification for storing data in memory in a columnar format, with implementations across many languages. I describe how projects like DuckDB have aligned their internal representations with Arrow to reduce the cost of data interchange. We talk about the challenge of supporting a project that succeeds by being invisible to end users.

Alenka shares her path into Arrow. She was teaching yoga full-time when the pandemic gave her time to explore programming again. A friend pointed her to Arrow, and she started contributing R bindings. She landed a position through an Ursa Labs grant from the Chan Zuckerberg Initiative after just a few contributions. She talks candidly about imposter syndrome, noting that many experienced contributors feel it, and that having people who acknowledge your work makes a real difference. The Arrow community is now working on processes to highlight contributions and reduce those feelings.

We spend time on how learning and pedagogy are changing with AI tools. I share my own experience using coding agents daily, noting that while they make me more productive than ever, the human judgment layer remains essential. I describe Arrow as an "AI-resistant" technology in the sense that AI makes it more important, not less. Alenka describes using agents for repetitive documentation cleanup in Arrow and for learning unfamiliar tools in her data engineering work.

The conversation closes with Alenka drawing parallels between yoga and open source. Both require discipline, sustained practice, and the willingness to progress slowly rather than jumping between things. She notes that her yoga practice has shaped how she collaborates in the Arrow community and beyond.

## Key Quotes

> "I think the big signs are whether the community is adding people, like people are coming and staying, and also are members of the community comfortable raising concerns about what's not working and having constructive dialogue about how to fix it without blaming or pointing fingers." -- Wes McKinney

> "When I started contributing to Arrow, I had no idea that in the meantime, Polars happened because I was using R in central bank. Pandas was big, but I haven't really used it before. So it was -- I was really kind of new." -- Alenka Frim

> "What yoga teaches you, if you really want to get into it, it teaches you how to not give up... progressing into making your own practice regularly, it takes effort. It takes discipline. So that kind of teaches you how to work in open source, not to jump really fast and then move away, but kind of progress slowly, look back what you did, how much you learned." -- Alenka Frim

> "Maybe the field of software engineering will shrink, but I think maybe it will stay the same size and we'll all be building 10 to 100 times more software." -- Wes McKinney

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field.

On this episode, we jam with Alenka Frim, mathematician turned yogi, turned all-star Apache Arrow committer, who notes that open source and yoga's revolved side angle pose have more in common than you'd think.

**Michael Chow:** Hey everybody, welcome to The Test Set. We're joined today by Alenka Frim, who's a data engineer and software developer, and a committer to Apache Arrow, and on the Project Management Committee, or PMC, and an Iyengar yoga teacher. And I'm joined by my two co-hosts, Hadley Wickham, who's chief scientist at Posit, and Wes McKinney, who's principal architect at Posit. And we're so excited to talk today. I feel like maybe one theme in hearing and in reading a little bit about you, Alenka, is it seems like the theme of sort of how do open source systems stay healthy? And sometimes they're big systems like Arrow, which sort of undergird a lot of data work and tools that people use. So thanks so much for coming on The Test Set. I thought maybe we could start today with just a little icebreaker, which might be maybe we could just go around and I'd be curious to hear from people. What do you think are, like, what's a sign to each of you of a healthy open source community, would you say?

**Wes McKinney:** I'm happy to go first. I'm very interested in Alenka's take, especially after being involved in -- I mean, I've also been very involved in Arrow since the beginning, but I've been less involved actively in the last five years. And so I think Alenka's understanding and knowledge of the Arrow community is actually really interesting for this conversation, because I have a lot of experience -- like Arrow, the first five years, Alenka, Arrow, the last five years. And so together we can really speak accurately to what a whole 10 years of the Arrow project has looked like.

But for me, I think the big signs are whether the community is adding people -- like people are coming and staying -- and also are members of the community comfortable raising concerns about what's not working and having constructive dialogue about how to fix it without blaming or pointing fingers.

**Alenka Frim:** Yeah, I would definitely agree. I think what I see on Arrow, which I feel it shows of a healthy community, is the way we interact on GitHub, which is the main point of interaction, I would say, not only with PRs, but there's discussions, there is issues. Together with the mailing lists -- one is for developers, one is for users. I feel there's a lot of motion, a lot of people raising questions, giving PRs, even reviews from a broader community, not just people you know. And I think that really shows, and the communication is really so respectful. I'm not sure about open source in general, but my experience with Arrow is really, really positive in that sense. So I think that shows of health.

I'm not sure how much Apache here influences -- I think it has a strong, it stands on a strong foundation because it's under the Apache umbrella, I would say, because there's already a structure that people know and they follow it, you know -- what, how to communicate, what's expected, what's not. So I think that's really helpful.

**Hadley Wickham:** The thing that first came to my mind, kind of building on what Wes says, but the first thing that came to my mind was turnover. Not just adding new people, but I think it's also really healthy to have people leave the community because that's the sign that you've built something that's more than just one or two people. And I do think one of the things we don't talk about enough in general is death as a part of the life cycle -- not death as in the ending of things, but people moving on to new things, changing roles, putting down things that they've looked after over a long time. I think that's super, super important.

**Michael Chow:** Yeah. It's so interesting that that aspect of people leaving, and I know Wes, you mentioned you were with Arrow for the first five years and Alenka came in for the last five years. Maybe to kick things off, Alenka, I'd be really curious to hear maybe a little bit about -- what is Arrow and how did you get involved with it?

**Alenka Frim:** Well, Arrow in the core, the way I see it, the way I understand it now is a format that specifies an optimal way of saving data in memory. So it can be analyzed the best, like the optimal way of analyzing versus having row by row as it's in conventional databases. But then this is just kind of an idea -- I mean, the format -- but then you have to build on it. So it's useful. And then there's so many languages connected to it. So it's not just a format, it's like a specification for languages, for applications. I mean, it's so broad.

And then every implementation, every language has kind of a structure. So you can actually use data in memory or data on disk with this kind of format. So it's a really broad thing. I hope I kind of helped understand this because it's not something people use. It's something that it's already there used by applications. So they're faster and more optimal. But in the essence it's just making things easier for a computer to calculate and analyze, making it faster and more efficient.

**Michael Chow:** It sounds like you're saying a lot of people, even if they don't realize it, are probably using Arrow when they're doing data analysis or maybe querying a database or loading a file of data.

**Wes McKinney:** And the project has quietly crept into all corners of the data world. I actually just read a blog post on a data engineering substack titled "Apache Arrow is eating the world," basically channeling Marc Andreessen's famous "software is eating the world." And it's kind of true. If you look at the data ecosystem increasingly -- you look at the Venn diagram and you look at projects that support or use Arrow in some fashion, the ones that don't -- the bubble that supports Arrow or uses it in some fashion has continued to grow. And the other bubble has shrunk as time has gone on. Which has been very interesting to watch.

But also, I think it speaks to the credibility that the community has built. Part of the credibility of an open source project like Arrow that you want everybody -- all these hundreds of projects in open source and commercial projects -- to depend on is that they have to believe in the Arrow community to keep being healthy, to keep delivering good software, because it has become this piece of critical infrastructure. And I think people like Alenka have been responsible for building and developing the community to create that credibility that has led to the project's success.

I admit that I've forgotten the details of how we came to be connected and how you got involved in the project's beginning. But I think all that is very interesting to me because you started out as a contributor and have grown into a leading member of the community. And I think that's a really interesting arc and your growth as an open source community leader.

Can you paint the picture for us -- what were you up to when you started contributing to Arrow?

**Alenka Frim:** Well, the interesting thing is that I wasn't up to anything. At that time, I was solely teaching yoga for five years and doing nothing with computers. So, yeah, before I was working on this in the central bank as, you know, on a statistical department, just helping with anything they needed. And I graduated and I'm a mathematician.

So when the pandemic hit, I had less, of course, less classes. They were mostly online. I had a bit more time and I realized I missed something. So I started doing some research, what could be a nice way for me to get back into -- I didn't know even what space, like is it data science, data analytics, data engineering? I had no idea. But I wanted to try to see if it still intrigues me.

So when I started contributing to Arrow, I had no idea that in the meantime, Polars happened because I was using R in central bank. Pandas was big, but I haven't really used it before. So I was really kind of new. I had a friend that was working on Arrow at that time. So we were brainstorming what could I try? And open source sounded a great place because I wasn't looking for a job. I was looking for an opportunity to try out and to learn and to have fun.

So I'm not sure why I picked Arrow. We talked about different things. I think I like hard problems. So I was really interested in if I can figure things out. The thing I struggled with a bit was that I wasn't a user. So I wasn't using Arrow in any sense. So it's kind of harder to understand it then because it would be much easier. But at the same time, I think the perspective I got from just trying to contribute was a different one. And it has other positive things.

So when I started, I did some contributions to R because that was the language that I was most comfortable with. And I was just lucky that right after my fourth or fifth contribution, we had a nice communication, nice collaboration with the R maintainers. There was a position open because there were grants. I think Ursa Labs got a grant from CZI. So it was just -- I think I was just at the right place at the right time, really.

**Michael Chow:** And just to give a little context to people who might not know about what an R contribution to Arrow is like -- what is an R contribution to Arrow?

**Alenka Frim:** It can be different things. What I did was something that I thought would be the easiest, which is a binding. What that means is that our R package, our Arrow R package is connected to the C++ implementation. So you have a C++ code base that defines the format, the zero copying. It defines how to read Parquet files, how to save them, all of that in C++. And then you don't have to do all of this magic again in R. You just kind of connect it, right? So there's different layers and you have to just figure out what are the pieces of a puzzle that you need. So my strategy was just look at PRs that were done before on a similar thing. And just try to figure out what's needed.

**Hadley Wickham:** You kind of mentioned earlier you weren't a user of Arrow, which made me wonder -- who do you think is a user of Arrow? Like, I think of Arrow as mostly this kind of invisible technology, right? It succeeds because things just work and you don't -- ideally, I think you don't know that Arrow is being involved. It's just, oh, I can use my data from wherever I'm working and wherever it lives. Who do you think of as the users of Arrow?

**Alenka Frim:** It also depends on the implementation, I think. But mostly, for most of the Arrow implementations, the users are actually developers that build on. For example, a query engine uses this format and you just build things on them. You have Pandas, for example, trying to use PyArrow, so Arrow part of the kernels to do some of the things faster, better. So, yeah, it's not an end user, I would say. Maybe in R package, that's a bit more usual to have an end user using it.

But mostly -- I mean, even in PyArrow, it's really interesting that a lot of PRs, a lot of contributions are done by developers that have so much knowledge and they already know exactly what they need. They just make a PR and you're like, okay, I need a week to understand it. So, yeah, these are experienced developers of applications that use it. It doesn't necessarily -- the application will be for the end user, but it can be. Sometimes it's already also an application for an application, if that makes sense.

I do remember one of the first meetings I had with Arrow project, I still remember what they said and they were saying that we are doing a good job if nobody knows about Arrow, right? So, it totally makes sense, but I still feel that people should know about Arrow. If not for general knowledge, for support, because if you don't know about Arrow, then how will people get support for maintenance and working on that?

**Wes McKinney:** I mean, the way I've looked at it is I've told end users -- they don't need to know necessarily details of how to use Arrow or how to implement it, but rather when they're evaluating their other technology choices, that's something they should ask as part of their due diligence checklist -- does this system support Arrow? And if it doesn't, is Arrow support on the roadmap? Because essentially that shows that a project is looking at the landscape of the open source ecosystem through a progressive lens of this is something that it need not constrain systems necessarily, but it makes them more interoperable and more efficient.

And so if there's a downstream project that doesn't see that kind of interoperability or that kind of performance improvement that Arrow provides, that is, for me, a bit of a strike against the project. And that's not necessarily fully disqualifying, but definitely it would make me second guess a choice of a critical piece of data technology.

**Hadley Wickham:** It is an interesting challenge though. When an open source product primarily exists to kind of remove pain -- people, as soon as it percolates -- people kind of forget, oh, this is actually really annoying and frustrating to do before. And that just becomes normalized so quickly. And then how do you tell that story? Like, okay, you should support this project because it's actually making your life much -- like people don't really appreciate that story, right? That's like, oh, when I used to walk to school, it snowed every day and I had to walk uphill both ways. It's an interesting challenge.

**Alenka Frim:** I'm not sure if necessarily developers or users need to know that or need to feel that. I think it's more on the managers and more on the leaders of these applications or companies. I think it's more on them to know how serious this is.

**Michael Chow:** Yeah, and I guess maybe to make it concrete too for folks, projects like Polars use Arrow and I think Pandas has Arrow support. And I think DuckDB as well is built on or largely --

**Alenka Frim:** As far as I understand, they are influenced. So they use the same format structure, but it's not something they -- they don't depend on Arrow per se.

**Wes McKinney:** Yeah, DuckDB's internal data representation that it uses for all of its query processing is very Arrow-like. And they actually, early on, we started working with Hannes and Mark prior to even the existence of DuckDB Labs and the DuckDB Foundation to essentially figure out how to better align DuckDB with the Arrow ecosystem. And they did make changes in DuckDB to make the interface between Arrow and DuckDB work better, but without doing it in such a way that it sacrificed performance in just only using DuckDB. I think they had the requirement -- they're like, well, we don't want to make DuckDB slower in order to reduce the impedance mismatch with Arrow. And so they were able to find a path where the bridge between Arrow and DuckDB -- it's not a totally free bridge, but they wanted the toll on the bridge to be as low as possible. And so the toll is pretty -- you can query, use DuckDB as an engine to process streams of Arrow data. And it's one of the most effective ways to build an application nowadays.

**Alenka Frim:** Maybe it's easier for folks to understand these differences if you think of Arrow specification, which is same or shared between Polars, DuckDB, and Arrow projects. So the idea is the same of how you store data and then just implementations themselves. Arrow provides an implementation you can use or DuckDB has its own or Polars has its own. It's a Rust implementation, but they -- because it's all the same spec, it's kind of -- some people just say it's built on Arrow, but it's just compatible.

**Hadley Wickham:** How do you think about that? It's always difficult to -- specifications are hard to narrow. Get every single, everyone agreeing on all these things that you don't think about when you're writing it. How is the specification and the implementations of Arrow co-evolved over time?

**Alenka Frim:** I think that's a good question for Wes. I can say from how I'm observing it -- you need to have a really good idea of how to make it in a way that people will be using it. So it's kind of user-friendly in a way. So they're like, okay, yes, we can use that. It makes sense.

And then also I think what I see when working with Arrow, especially in PyArrow, because then separately Python has a lot of specifications for interchange -- you have DLPack, you have data interchange. I mean, there's a lot of them, so what's the difference? I think it's just when there's a need, something arises. And then with Arrow, I think the way community feels is that we're building something solid. And then if people need something different, that's fine. But kind of the main thing is solid and we're going to work on it. And then more people adopt it, then it just kind of grows by itself. It's like spontaneous.

**Michael Chow:** I feel like we've hit so many interesting things, which is like Arrow is largely behind the scenes, driving a lot of stuff. It's hard for that to surface. People might enjoy Arrow without even knowing it. And there's the question of how do you support that kind of stuff? And then it's interesting to hear even with DuckDB, there's the spec and people who might not just use Arrow, but maybe it might rhyme with Arrow or they might keep Arrow in mind. And how do you write a good specification?

One thing I thought I'd flag too is that I saw in a talk you gave before that Arrow has thousands of issues open. There's tons of issues.

**Alenka Frim:** We came under 4,000 now with Nick Crane's help.

**Wes McKinney:** Yeah, incredible. Are you using some AI tools to help with grouping and summarization, linking, categorization and things like that?

**Alenka Frim:** I haven't dared to use -- I haven't yet for going through issues and helping with backlog curation. One thing Nick and I did was create a dashboard, which surfaces, for example, issues that were not answered, issues that were opened by a new contributor, because that's some things you want to kind of jump on first. Same for PRs and et cetera. So that's what we use, which I think it's useful because otherwise what I tend to do is just answer things where I'm pinged because it's so much stuff going on.

**Hadley Wickham:** I mean, here's like -- this is, I don't really mean this, but like, how can I trust a project that has 4,000 open issues? How do you think about that?

**Wes McKinney:** It's the closed issues, Hadley. Look at how many closed issues there are.

**Alenka Frim:** Yes.

**Wes McKinney:** Yeah, it was probably like 20,000 closed issues.

**Hadley Wickham:** Yeah, yeah. Because I mean, how do you think -- because I think I've evolved this pretty unusual way of dealing with issues just because I think fewer R users are comfortable on GitHub. So the number of issues you get for an R package is much, much smaller. So I like this inbox zero approach of issues. To me, the ideal number of issues in a repository is under 25, because that's one page on GitHub. But I just can't even imagine, how do you think about that? When you think about those 4,000 issues, you just don't care that there's all these open issues? Where's the -- do you see them as being valuable or useful? I see the point of an issue is to be closed, I guess, but that's clearly not --

**Alenka Frim:** If you look at the issues as bug reports, then yes. But there's a lot of feature requests. There's a lot of documentation issues. There's user questions. It would be really nice to have zero, but I think it's important to understand the scope of Arrow. It's just not one project that we normally think of. It's so broad.

Just maybe to put it in perspective, we have in the repo multiple languages and every language is for a couple of projects, right? In Python, it's just one part. And you have C++, you have R, you have -- I'm not really sure how many languages are still there, because some of them are separate to make it easier. And then per language, you have so much parts of the implementation. For example, in Python, in PyArrow, you have a part of the code base that deals with pandas compatibility. So you have issues for that. Then you have issues for file systems. And it's just such a broad thing that we're not stressing about it.

We would like to have them all -- not all closed, because there's always going to be something that will need to be done in Arrow, I think, because it's an evolving thing. It's not a project that it's just there and it will be used. It's more like it's developing. There's new data types being included. There's some new things like Parquet -- you have a specific code part where you deal with Parquet reading and writing. So Parquet is being evolved and you have to match that. So I think you have to have a different mindset for Arrow project versus other packages.

**Wes McKinney:** I mean, the way I look at it is every language implementation of Arrow -- aside from the ones that are a little more like wrapper layers, like R and Python -- you can think of them as almost being little operating system kernels for low level data operations. I mean, it's not exactly as grandiose as a "Linux kernel for data" -- that would be a silly way to market it. But it's kind of true in a way.

And I think the toolbox -- I think we always envision the project as building on the specification, but the specification alone is only so useful without the toolbox and the framework of things that you need to build real world systems. And as time has gone on, I think that toolbox has grown. And sometimes it's expanded in ways where we've been like, oh, maybe that was a mistake to take on that piece. And we've pruned -- I think the project has pruned things that were not getting maintained or that there just wasn't that much community interest in continuing to keep around or maybe spinning off into a side project.

But it's been a little bit of -- I think Neil Richardson described Arrow as a bit of a radical social experiment. And I do feel that way. And some of that, the anarchy of the sprawling federated nature of the project has certainly made things more complicated, but also I think has helped keep the community together and keep it thriving and productive.

**Michael Chow:** I mean, it seems like you've really latched on to Arrow as a contributor and done so much for the ecosystem and open source. I'm really curious, what do you think are the ingredients to really get started with something like that? How does someone get a foot into contributing and succeed at doing that kind of thing?

**Alenka Frim:** I think to get started, you have to -- I don't know what would be the motivation. I think everybody has a different reason. But I think the more I think of it, the more I talk to people, it's mainly experience or to grow or to learn or to just interact with a new community.

I mean, there's for sure a lot of contributors, especially in Arrow, where they use the tool and they need some feature or some bug fixed, which is so awesome in open source -- that you can actually have the possibility to do that. It's not like I'm waiting for somebody to fix my problem. It's like you have the option to do that and not just for you, but for somebody else for sure.

So how to succeed? I think, well, I'm not sure if I would succeed without people around me that helped. I mean, I did have to do the work and do the research and just stick with it. But just building Arrow from source locally, it's not an easy thing to do. And if I wouldn't have somebody helping me, it's quite possible that I wouldn't continue.

So having this group and just having people encourage you -- I think it was my third or second contribution that I was already being pinged like, oh, are you interested in doing this too? And this means so much because you're like, oh my God, they noticed me. In a project like this, it's an amazing feeling. So small things like that, when somebody would think it's maybe even rude to ping people -- it's not. It's like you show somebody that they're worth collaborating with and you put some trust in them.

**Michael Chow:** Yeah, I could see like if you get pinged, it really shows -- just realizing that people appreciated it and noticed it really makes it nice. And I wonder if related to -- I saw you gave a keynote at PyData Paris, which is awesome.

**Alenka Frim:** Yeah, it was fun.

**Michael Chow:** And I saw one thing you talked about was imposter syndrome, how to sort of approach that as a person in open source. I'm curious your thoughts -- what would you say is kind of the takeaway for people experiencing imposter syndrome and looking to contribute in open source?

**Alenka Frim:** Yeah, one thing worth mentioning maybe is that you're not the only one feeling imposter syndrome. I think it's a really -- a lot of people feel that. When I talk to people after the keynote, when I talk to people I work with, which I feel they are the most brilliant people I've ever met -- and they are saying that I feel I don't understand, I feel I'm not capable. I would say a lot of people feel that.

And how to overcome? Well, again, maybe I'm repeating myself, but having somebody you could talk to. I talked to Raul a lot. He's a PyArrow friend, a contributor and a PMC member. Also, he's involved in the project a lot. I'm talking to Nick on a regular basis, also a contributor. And we see that it's a common thing, which maybe it shouldn't be. But I guess I don't know if it's open source related or just technology related or just happens in general with people because you're working with a lot of folks. You see what they do. You see it's something amazing and you always kind of want to match.

But I think the real thing you need to do is find something you like and you feel comfortable and you feel motivated to do and you feel you have fun. And then after a while, you have to look back at all of the things you did, not just looking and comparing to others, but saying to yourself -- and maybe having a friend so you can talk to. And they will say, look, this is amazing what you did.

And that's also something I experience in Arrow -- people stop, they talk to you and they say, Alenka, this is amazing work you did. And it really kind of -- all the bad emotions you feel, they tend to go away. Yeah, I don't know. I was really intrigued by Dr. Kat Hicks. She was doing a keynote at Posit Conference. So that was a lot of research I did before my keynote. I wasn't talking a lot about imposter syndrome. I was just mentioning it and mentioning that we need to talk about it and do some research because I think it's really important.

And yeah, Dr. Kat Hicks has a lot of good ideas on how to tackle that. So one thing I want to mention before I stop with this part is that at the Arrow community now we're talking about -- I'm doing the still reading about what they're researching and we're talking about what could we do as a process in the community that would help remove these feelings. So one thing we are trying to do now is to make a blog post of highlighting contributions, saying, okay, this was a new contributor and they did amazing or this is such an amazing job done by somebody. I think that would help.

**Hadley Wickham:** Yeah. One of the things we've -- in the Tidyverse, when we do the release announcement for packages, we do just a round up, very low effort. But we're at least like, hey, thanks to all of these people who have interacted with us on GitHub. And even like, we hear every now and then people are like, oh, that's really cool to see my name. Or when people have done pull requests for the Alpha Data Science book, they get mentioned in the intro. It's small and obviously you can do much more. But even little gestures like that, I think people appreciate being recognized and acknowledged.

**Alenka Frim:** Very much. And maybe also, you know, we don't all have to be Hadley and Wes. It's fine if you're not the core developer. It's fine if you don't feel comfortable in doing something, but you feel comfortable in doing something else. I think we have to realize that we don't have to know everything. And then you start learning. And then if you have fun, you kind of see that you actually know a lot.

**Michael Chow:** Yeah, it seems really neat, acknowledging contributors and also emphasizing to people -- you don't have to be the best. Figure out what about this you like and why is this fun or interesting to you?

It is interesting. I think when you teach or when you TA a workshop and even if you feel kind of insecure in your knowledge -- but then you realize when you go and help the people taking the workshop, they kind of know literally nothing. And that -- it's so reinforcing to you how valuable -- it shows how much you've grown and how much you've learned, actually.

**Hadley Wickham:** Yeah, and I kind of experienced this afresh recently. I taught my first yoga class -- I subbed for my teacher and she prepared the class. I just gave it. But one thing that I found fascinating was -- I've always been like, how does a yoga teacher know how to do adjustments? How do they know all this? And I just kind of thought, oh, that -- and obviously some of it is years of experience and knowledge of anatomy and training. But some of it is also you just look at people from outside their body and you're like, oh my God, that looks so wonky and off. And just having that -- oh, actually, this is not as complicated as I thought it was. It's such an empowering experience to be like, okay, just being outside of a person can be -- having that fresh perspective, you don't have to be that much more knowledgeable than them to be helpful and useful and to make their journey a little nicer.

**Michael Chow:** Interesting thought where if you're the person doing yoga, you might have the thought, how did the teacher know to adjust me? But once you're the teacher, you're seeing 20 people and it stands out.

Let's see. This is our chance to turn this into a podcast solely about yoga. But one interesting thing we could maybe turn to the group is -- I know you mentioned a couple of questions that might be interesting to ask folks here. Maybe this is kind of related to yoga and learning. I think one thing you mentioned is, for learning, do people prefer to learn as you go or to stop and take a course to focus on things? Did I get that question right?

**Alenka Frim:** Yes, correct.

**Michael Chow:** Yeah, I'd be curious, folks' take on that. Do you think it's better to -- when you want to learn something, do you prefer to stop and take a course or kind of learn as you go?

**Hadley Wickham:** I teach a lot of workshops, but I have to say, I hate taking workshops myself because the pace is set by someone else. First of all, now I'm so used to watching videos on YouTube at 1.5 or 2x speed. I'm like, why is this person talking so slowly? This is so inefficient. And then there's a bit of an ability to go on and off on your own little learning tangent. So in some ways, classes feel so -- I don't know. Yeah, I don't enjoy them.

On the other hand, I take yoga classes and that is something where I'm like, okay, I just -- it's also nice just to be told what to do every now and then. And just -- here is a path. I don't have to forge my own path. I'm just going to follow someone else's path. And that is really nice sometimes.

**Wes McKinney:** Yeah, for me, I definitely prefer hands-on learning where possible. And so whenever I dive into something new, I will try to learn just enough to be able to start doing and then try to create a virtuous cycle of doing and then running into the things that I don't know how to do and trying to figure it out and then looping. And over the course of time, I guess that develops mastery.

It turns out that when it comes to programming, all of that is being broken apart and destroyed maybe forever right now. But coding used to be the perfect example of the ultimate hands-on learning. You learn how to do Hello World and then you learn how to assign variables and write a loop and then write a function. And then you learn how to think about organizing groups of functions and modules and thinking about object oriented programming and state management and multi-threading and distributed systems and data storage and file systems.

And not to hijack the topic. But I feel like the whole subject of learning is being turned on its head right now. Part of me is like, ah, the quaint old days of reading a book and learning how to do things that way. I'm actually ideating what the fourth edition of Python for Data Analysis looks like. And part of me is like, do people even still read this book? And I look at the book sales and the book sales have dropped substantially because people aren't buying programming books as much anymore. And you know why.

So I think book authors and people creating learning materials and tutorials -- it's a whole new world. And I feel like the whole domain of pedagogy is going to have to remake itself in order to remain relevant and to keep up with the way that things are changing. Otherwise, why would people go to a class or read a book when they can sit with their chatbot and self-tutor and explore topics of their own choosing in whatever order they wish? Because all the chatbots have already ingested all of our books.

And the other interesting connection, I think, is -- on the whole, I'm still optimistic about software engineering as a career. I think software engineers are so valuable. And at least right now, it feels like AI is kind of a force multiplier. But we are also at this sort of interesting point where you're like, well, it's also -- being a yoga teacher, AI is not going to take that over anytime soon. It's just sort of interesting where you're like, that's actually kind of nice to have in your back pocket, these things that are so specifically human where that human connection is so important. Those sorts of careers feel a lot safer than software engineering right now.

**Alenka Frim:** That's true. But I think still for really diving into a harder subject that's not documented yet, you still need to have people that are intrigued by discovery and learning. So I don't think it's going to -- but for general programming, I would say, yeah, it's a strange time.

**Wes McKinney:** Yeah, certainly developers of data entry CRUD applications are, I think, first on the chopping block.

I actually think, in a talk that I gave recently and maybe in another podcast, I described the Arrow project as being what I felt like an AI-resistant project or AI-resistant technology. And I wanted to see what you thought about that, both in the sense that AI doesn't make Arrow irrelevant -- in some ways it makes it even more important, as a grand unifier. But also you think about 10 years of development on this project. And I'm using coding agents every day to build little applications to make my life a little more streamlined, a little more productive. And even seeing how difficult it is to guide chatbots to create correct and useful software requires so much human-in-the-loop attention and intervention and guidance and review and feedback.

There's this whole narrative around artificial general intelligence and super intelligence. But personally, I don't buy it because I'm using these agents every day. And the more you're using these things -- yes, they're tremendously useful. I'm building more software, more productive than I ever have been in my life, which is insane. But at the same time, the human element of judgment feels more essential than ever.

And so I'm curious how much you thought about that and how you're seeing that play out in the Arrow ecosystem.

**Alenka Frim:** Yeah. I mean, you could use agents to help you when you need to debug something in Arrow -- it can be quite complicated to find what's wrong. So there's some help there that I use, especially since Paris, when me and Wes talked and I was like, oh, Claude Code sounds really cool. So I'm actually a late user. Pretty cool. Yeah.

But you still need to have agents there for when you get stuck or for repetitive things. For example, now there's a lot of documentation in Arrow, especially in Python. And we have somewhere IPython code blocks, somewhere Python code blocks. So it's kind of a mixture because different people contribute. And this is a perfect thing for an agent because it's just -- you need to unify it. But yeah, doing some real work or even usage of Arrow, I think you still need to depend on yourself and just do some digging and research.

I actually started using agents more when I started doing the data engineering work that's not related to Arrow. It's totally on the other side, which is having to ingest a lot of data from different sources and using so many tools I never used before. This is a local telco company that I help. And I was an R user, a Python user. So when I started to work with them, they were like, okay, which tools do you use? And I'm like, Python. And they're like, okay, we use Kafka, Airflow, Meltano, dbt, Snowflake. I mean, it's so many tools. And there I really had a lot of help from the agents just to see, okay, what's the structure? What's the syntax that this tool uses or that one? And it really saved me a lot of time.

**Hadley Wickham:** Yeah, coming back to Wes's point about pedagogy, I think one of the things that's really interesting -- it feels like now if you know how to program in one language, that skill is so transferable to other languages because you're not constantly stuck in this -- oh, how do I write a for loop? But how do we -- how are people going to get to that? How do you become a competent programmer, a really good programmer, when for the first maybe two or three years of your career, a chatbot is going to do everything better than you?

**Alenka Frim:** When I was in college and we learned to program, what I heard a lot was that mathematicians are good programmers because the way you need to think as a programmer is easier because of the way you have to think in mathematics to solve problems. So what do you think about this? This idea of you still need to have the mindset to program. It's not just practice. You need to think in a different way. So that still needs to be learned, right?

**Wes McKinney:** I guess the way I look at it is I think the field of software engineering is -- maybe the difference between before the printing press or before books, I'm trying to come up with the right analogy. So plenty of people read books, they read literature, they go to school to study literature, they do analysis of writing and they can understand what good writing looks like. And there's whole fields of liberal arts scholars that study and scrutinize and learn about what constitutes good literature.

And so I think the field of software engineering is going to go from -- essentially the agent is doing all of the typing, but you're still doing most of the critical thinking about what is the proper shape and structure of the system, essentially creating the algebraic structure of the layers that you're building.

And I do think that new tools will emerge to help visualize and orchestrate the different layers of the system that need to be compartmentalized in such a way that -- I think the problem right now with agents is that they create code bases that are so entangled that the agent starts getting confused about all of the commingled responsibilities and things.

And so I'm hopeful that some new software engineering practices emerge that enable that more -- to your point -- that more mathematical mindset of -- I was also a mathematician. And so I approached software engineering from a very mathematician-centric viewpoint of thinking about things in terms of stacks of lemmas and theorems and trying to prove things by layering things on top of each other. And I think maybe that drove part of what was so intellectually appealing about Arrow. And maybe since you're a mathematician, maybe something that appealed to you is that notion of composability and the interoperability and the layering of software, almost as a mathematical concept in a way. I found the idea really intellectually appealing.

And I find that -- not to stereotype, but I do find that a lot of folks who have computer science degrees often approach software engineering from a more pragmatic mindset and less of a theoretical or design perspective. Not to say that in general, but if you took a room full of a hundred mathematicians turned software engineers and a hundred computer science degrees turned software engineers, I do think that different thought patterns would emerge in terms of the inherent approach to building software. Of course, I'd be interested in actually doing some studies and learning more about that. This is just my anecdotal experience, which is probably BS. So if you're listening, feel free to call BS. It's just my gut feeling.

**Michael Chow:** Your comment about literature reminded me -- I should try and find this again. But a few years ago, I read this -- I don't know if it was a proposal or an actual thing -- but it was an MFA, a master's in fine arts in programming or software engineering, attacking it from -- one of the ways you learn how to do painting is you go and look at the great works of the past and you recreate them. And it does feel like we've got a lot we can learn from the humanities in terms of studying and thinking about these volumes of texts we're producing.

**Wes McKinney:** I mean, truly we can begin to think and actually dedicate energy to the aesthetic qualities of a code base. And that used to be the stuff of -- oh, you're wasting time beautifying the code base. But when beautifying the code base has one thousandth of the cost that it used to have, of course the code base should be beautiful. Of course it should be well-structured and easy to reason about.

So I think that's -- I'm optimistic. Maybe the field of software engineering will shrink, but I think maybe it will stay the same size and we'll all be building 10 to 100 times more software. I think that's my hope actually -- that we're building a lot more, we're building the software tools that would never have been justifiable to build in the past, like personalized apps that only serve 100 people or less, really hyper-specialized tools that deliver incredible value to small groups of people. And in the past, maybe it would cost a million dollars to build that tool or that product. So you think, well, there's 100 people. Of course, we're not going to spend $10,000 a person to build that thing. But if you can build the same thing now in a week or two and a $200 Claude Max plan -- of course, somebody has to babysit the agent and their time is not free. So you could back out the cost, but maybe the cost of a million dollar bespoke software product now requires somebody who's an expert in agentic programming and two weeks of time, and maybe you pay them five or ten thousand dollars for that service.

And so clearly there's a market and a need for expertise in using these tools. But I think the result is I expect the number of unique shipped software products to be a minimum an order of magnitude what it was in the past, if not two orders of magnitude. And if I look at my personal sphere of the software that I'm creating for myself, I'm building all kinds of stuff that I would have never been able to build in the past, just stuff that I would sit and think about on vacation. I'm like, wouldn't it be nice if I had a thing to do this thing in my life? But I couldn't possibly take time away from maintaining Arrow.

**Hadley Wickham:** So the other place I've found interesting is the cost of refactoring, the cost of writing tests, the cost of improving the quality of code has gone down as well. So maybe we get an order of magnitude more software, or maybe we get software that's an order of magnitude higher quality. So it's -- I don't know, it's definitely interesting times to be a software engineer, but for many reasons.

**Michael Chow:** It does remind me too of Wes's point about beautification -- I feel like a lot of the designs I had, it wasn't like I thought it was the most beautiful, or two years on, I might even have arrived at a better way, but not have wanted to go back and change it. But it is crazy to see today, you can be like, refactor into this new setup, and almost just know within five or ten minutes -- does this feel better? Which is really kind of mind blowing to me.

**Hadley Wickham:** Yeah, I also remember in the past, there'd be those refactorings where it felt like as you got further and further into the swamp, you're like, oh, should I just give up? But I've been working on this for three days. So I'm going to just push on through. And now you're like, oh, well, Claude just spent an hour on that. Screw it. I don't like where I went. I'll just throw it all away.

**Wes McKinney:** Yeah, for real. And I think there was this point about small apps too. I really had a kind of mind blowing experience recently where I studied Cantonese a little bit, which is -- it's really hard to get written resources for Cantonese because it's only spoken, not really written. So seven, eight years ago, I would pay people through Upwork to transcribe materials. And it's crazy to think today, I just use Whisper and an LLM to then clean it up. And yeah, have an app that spun up so fast to help me track this and read transcripts. And it did kind of blow my mind that I get to, as a person who's a cognitive psychologist, now I get to almost decide to be a cognitive psychologist and leave the coding to Claude Code. For this activity, I'm not even thinking about the code.

And I think to Wes's point of small, nice apps, it's kind of mind blowing to have that ability to not even come into it as a programmer, but to still get to experience a new tool that, on vacation, you thought it'd be neat to try this out.

**Wes McKinney:** Yes, I'm super curious what people end up building. Wes, I saw you had a tool for code review. Is that pretty recent?

Just this week, yeah, I built a little tool called RoboRev in Go. And I've never written a line of Go in my life, true story. So Claude helped me build it in Go. And the idea is that RoboRev runs as a background service. And the idea is that if there's a repo that you're working in with agents, you run RoboRev in it and it will install a Git commit hook in the repository. And so whenever one of your agents -- because you might have multiple agents working in the same repo in the same branch, which sounds crazy, but actually it's okay if you ask them to work on distinct things -- but whenever one of the agents commits, immediately RoboRev will pick up the Git commit hook, will enqueue a review request. And you can choose the coding agent that you want to review that commit.

And so basically it will kick off Claude or Codex or Gemini or Copilot with a prompt that includes repo-specific instructions. So maybe there's guidelines around what you want reviewed and what you care about, what you don't care about. And then it includes, if the diff is small, it includes the diff inline, which is good. Otherwise the LLM can hallucinate when it's inspecting the diffs with tool calls. But if the diffs are too big, then you just let it use tool calls to look at the commits.

And then basically it has a terminal user interface. So you can have -- I work with a stack of terminals in Kitty terminal and macOS. So you'll have four or five terminals stacked on top of each other. And so I've got my RoboRev terminal queue of reviews and then my agents that are working. And so basically an agent commits, the review triggers, it takes two to four minutes to run. I read the review and then I copy-paste the review back into the agent that wrote the commit. And I'm like, fix this. And it fixes it. So that's pretty cool. Check it out.

Speaking of the transcription thing, another thing I did over the holidays -- I always wanted to have transcripts and descriptions about talks that I've given in the past. So I used Claude to transcribe every talk that I've ever given that has a video online and generate a transcript and a 500-word-or-less summary of the talk. And it did it. Use Whisper to transcribe and then use Claude to summarize. And yeah, that's all on my website now, which is mostly for me, but I found it very satisfying. And it's one of those things where I could never have justified the expense for the time to do that in the past. And now it's done.

And I actually had a podcast that I recorded that was released this morning. And I fired up the agent. I said, here's the YouTube link of this podcast that I did, transcribe it, summarize it according to my preferences, which are in the Claude MD file, and push it to my website. Oh, I reviewed it first and I pushed it manually, but get it ready to push. And it took about five minutes and voila, it was done. So pretty cool stuff.

**Michael Chow:** Yeah, it's freaky.

Well, Alenka, I know you asked -- you had a question about learning and we went into a deep optimistic doom spiral on AI, but that may be relevant for programmers thinking about the pedagogy and why we program and how. I think we're getting up to time, but I'd be really curious maybe closing out -- I know you spent a few years teaching yoga before getting into Arrow and open source. I wonder, almost closing out, do you have any insights coming from your practice teaching yoga, any inspiration you've taken for contributing to open source?

**Alenka Frim:** I think what I took from Arrow to maybe not really yoga classes or instructions per se, but more of a collaboration, which is kind of funny. I think Arrow really taught me how to collaborate also in the yogic space. Because in Slovenia, we have an Iyengar yoga association. And I think it's teaching me a lot about how to work with people. Because I don't think we are doing that well in the association.

And the other way around -- it's a really hard question because yoga teaches you so much. And I think anything I do in Arrow or going on the keynote, everything's connected in my opinion to what I do on the mat in the morning.

But mostly I would say what yoga teaches you, if you really want to get into it, it teaches you how to not give up. Because, okay, one thing is to go to classes, as Hadley said, it's really nice. You go there and people tell you what to do. And it's -- you still need to work a bit, but it's easier. But then progressing into making your own practice regularly, it takes effort. It takes discipline. So that kind of teaches you how to work in open source, not to jump really fast and then move away, but kind of progress slowly, look back what you did, how much you learned. Yeah. I think that would be the first idea that comes to my mind.

**Michael Chow:** Like if you're looking to contribute, you're not an imposter and maybe rather than opening an issue, you could hit a yoga mat first to build the skills.

Alenka, thanks so much for coming on and for all your work on these undergirding systems that quietly keep so much of what we do afloat. It's been so nice to hear about how you can contribute to open source and everything that goes into it. So really glad to have you on and thanks for joining us.

**Alenka Frim:** Thank you for having me, for inviting me. Thanks.

**Wes McKinney:** Thanks for being here.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio Adji. For more episodes, visit thetestset.co or find us on your favorite podcast platform.