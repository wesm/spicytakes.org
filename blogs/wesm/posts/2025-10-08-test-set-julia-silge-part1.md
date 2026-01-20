---
title: "Julia Silge Part 1: Positron, pineapple pizza, and the art of iteration"
summary: "Podcast at The Test Set (Posit)"
date: 2025-10-08T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-julia-silge-part1
word_count: 6432
source_file: transcripts/2025-10-08-test-set-julia-silge-part1.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=8E2p5o07-EI"
---

{{< video https://www.youtube.com/watch?v=8E2p5o07-EI >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow, Hadley Wickham, and I sit down with Julia Silge, data science leader and engineering manager at Posit. The conversation opens with an unexpected story about Julia's Wikipedia-documented incident of sending a pizza with a political message to her senator's office, which went viral.

The main discussion focuses on Positron, Posit's new data science IDE built as a fork of VS Code's open source code base (code OSS). Julia explains how Positron differs from general-purpose IDEs by specifically targeting the iterative, exploratory workflow that defines data science work. She articulates a key distinction: data scientists have high reproducibility needs combined with deeply iterative workflows where you often cannot know what code you will write next until you see the output of the current code. This tension between exploration and reproducibility shapes how Positron is designed.

We discuss the tradeoffs of building on VS Code's infrastructure, including the benefit of getting mature software engineering features (Git integration, file search) essentially for free, while being able to focus development effort on data science-specific features like the data explorer. Hadley shares his experience of having to go "cold turkey" from RStudio to really commit to using Positron, while I describe how Positron has finally given me an integrated Python data science experience after years of jumping between terminal-based workflows and Jupyter notebooks.

## Key Quotes

> "What's different between someone doing statistical analysis, data science, machine learning, and someone who might be doing more traditional software engineering is that the work of a data scientist has high reproducibility needs and high needs for supporting iterative exploratory workflows." — Julia Silge

> "You can't often get [VS Code] to work, right? You go install some sets of extensions, and then you can kind of bailing wire together an experience that you can then use to do data science. But our bet here is that we can do better." — Julia Silge

> "The work of a data scientist is more iterative. Even if you are all in on writing code to do your data science, often you literally cannot know what the next block of code you will write until you see the output of the first block of code." — Julia Silge

> "Building on top of already existing infrastructure reduces the amount of people hours you have to invest to have something that's working that people can actually get their hands on. But there's also tradeoffs." — Julia Silge

> "The things in Positron that are clearly superior to RStudio are the sort of data science adjacent things. Like the VS Code Git pane has had probably an order of two more magnitude of hours put into it than RStudio ever did." — Hadley Wickham

> "I had to go cold turkey off RStudio. For a while, I was like, okay, I'm going to, like, every day I'd start out with the goal of using Positron. And at the end of the day, I'd be, like, oh, that's weird. I'm in RStudio, like, and I don't remember." — Hadley Wickham

> "Learning anything new sucks. It's always painful. You immediately notice all of the things that were so easy before are now painful and frustrating. And if you don't push through that, you never get to all the cool new stuff." — Hadley Wickham

> "It's been pretty interesting working on Positron now, and feeling really, even as someone who works on it as my main job, feeling now, finally, like, ah, now I can use Python in this iterative way, where I have that sort of balance between the iterative exploratory work and the reproducible practices." — Julia Silge

> "When I think about success, say on any given day or week or month, a lot of my time is spent thinking about how a complex system fits together. I'm not someone anymore who goes really deep in one narrow area." — Julia Silge

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning. Digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. This episode is part one of a conversation with Julia Silge, data science leader and engineering manager at Posit.

**Michael Chow:** Hey everyone, welcome to The Test Set. We're joined by Julia Silge. And per usual, we have Wes McKinney here and Hadley Wickham, two data science leaders in the R and Python community. And we're so excited to talk about Julia's work on Positron and a whole array of things. All right, Julia, thanks so much for coming on to The Test Set, a podcast where we explore the people behind the data. And we're so excited to have you. For just a little background, you've written three books, you have a PhD in astronomy, and you're currently an engineering manager at Posit. But you've also done so much work in the R ecosystem building packages. So I'm really excited just to be able to talk about your open source and managing. Welcome.

**Julia Silge:** Thank you. Thank you so much for having me. I'm really glad to be here with talking with you and our other folks here today.

**Michael Chow:** Okay, one thing I thought we could just start out with right out of the gate is we had a question when we were talking with you before starting about if you like pineapple on your pizza. And I was not expecting the answer you gave. I don't think I could have predicted it. But as it turns out, your Wikipedia page speaks to this question that you one time as an activist sent a pizza to a senator. That's right. If it's too big out of the gate, but I thought maybe we could just open with that pineapple on your pizza. And why is it on your Wikipedia page?

**Julia Silge:** So in full disclosure, I do actually like pineapple on pizza. I am a pineapple and ham Hawaiian pizza. That's good to eat if you ask me. Several years ago, I did actually send a pizza to my senator. It was at a time that it was difficult to get through on the phone to your elected representatives. And there was somebody up for being confirmed for the cabinet at the time. And it was somebody that I had strong feelings about. I was really opposed to this person getting confirmed. And I was trying to get through on the phone. And the stupid mailbox was full, and they were not answering the phones.

And I was so upset because I was like, this person represents me. Thinking back, I am honestly not totally sure why my brain went there. But I thought I will send them a pizza and put my message in the delivery notes.

So I went on to a local pizza delivery place. And I put in the office at the federal building, the one that's here in my city. I live in the state capital of my city. So I put that as the delivery address, and then in the notes, I said, please vote no on this person. My name is Julia Silge. I live in this zip code. And I put a really big tip because I was a little bit like, I wasn't sure if the driver was gonna get through security. I wasn't sure how this was gonna go.

And I sent the order. And the order went in. I got a call from the delivery driver, actually, like, how do I get into this? And I said, oh, well, the office is on the such and such floor. I actually feel a little bit bad about the delivery driver having to have this experience, because I was like, man, I've kind of roped this other person into this whole experience. But they did get in, they delivered the pizza.

And a little bit later, I got a call from the security for the federal building here in the capital where I live. And the security person was like, we've gotten a report of a pizza being delivered. And I was so nervous. I was a little shaky and nervous.

It ended up, at the time, I had a moderately big Twitter following, mostly because of my engagement in the data science community. And I was kind of tweeting through it. I was really upset about how things were going and that this person was up for this cabinet position. So I was posting through it. And it went the most viral of anything I've ever done in my life.

And it was really, I think of it now as my 15 minutes of fame. It was on Rachel Maddow, and it was on the Washington Post and really went pretty broad. And it is really interesting what happens when you kind of escape your circle of people who know who you are and what you do. And it was the time that happened most dramatically, where something I had written had escaped. It was a real experience of context collapse. It was an interesting experience in a lot of ways. And yeah, it's on my Wikipedia page.

**Hadley Wickham:** Did it work? Like, did they vote no?

**Julia Silge:** No.

**Hadley Wickham:** Did they respond at all to your pizza?

**Julia Silge:** So the senator's office reached out to me after it went super viral and started getting picked up on news. And they said, oh, thank you. They're like, oh, it's just been so hard to hear from our constituents, because all these fake people are just filling up our... And I'm like, no, these are real people like me that were trying to get through. And they're like, oh, it's just so hard to hear from people.

And I took pleasure in voting against that senator every chance I got. I changed party registration so that I could vote against the senator, both in the primary and in the general.

**Michael Chow:** So you're firing on all cylinders, you're firing on pizzas, you're firing on parties.

**Julia Silge:** That's right. All the P's.

**Michael Chow:** That's incredible. I for sure was not expecting that. But I wonder if it's good context for life as an engineering manager, and working with complex systems. So I know you're working on an IDE called Positron at Posit right now, which I imagine probably has a lot of moving parts.

**Julia Silge:** Yeah. So Positron is a new next generation data science IDE. Us at Posit, we are the makers of RStudio. And so we are a group of people that have a lot of institutional muscle, a lot of institutional knowledge about what people who are doing data science, people who are doing statistical analysis, what are the tasks that they're trying to do.

So Positron is our new next iteration on providing a set of tools for people who do data science. Positron is a fork of code OSS, which is the open source software that is used to make VS Code. So if you're familiar with other forks of the VS Code infrastructure, like Cursor or Windsurf, it has some similarities to those in that it is built on this kind of underlying infrastructure.

But it's different from those other kinds of projects, because there's a different set of goals. The goal of Positron is to provide a data science first IDE. It's not built for general purpose software engineering. It's built specifically for the work that data scientists have to do.

A lot of people who might be used to, like, there are a lot of people who use VS Code for data science or other kinds of more general purpose IDEs. And you can't often get that to work, right? You go install some sets of extensions, and then you can kind of bailing wire together an experience that you can then use to do data science, to do machine learning, to do statistical analysis. But our hypothesis, our bet here is that we can do better.

We're not interested in making something for everyone. But our bet here is that we can do better specifically for people who have data analytic tasks, who have data science tasks, who have machine learning tasks to do. If we build a tool for them that is specifically built with that user in mind, we can make something that's more integrated, more pleasant, that you can have more fluent, ergonomic workflows.

**Hadley Wickham:** Obviously, I've got a lot of thoughts about this. But what do you think makes the data scientist workflow different to the software engineer workflow? Obviously, there are different tools and stuff, but it feels like the workflow is different to it.

**Julia Silge:** I do. And I think there are two characteristic things that I think really define what is data science work that maybe set it apart from other kinds of software engineering. And the first one is that it is more iterative. Even if you are all in on writing code to do your data science, often you literally cannot know what the next block of code you will write until you see the output of the first block of code. And so, it is more exploratory, more iterative.

At the same time, there's really high needs for reproducibility. And so, when you sit in this tension of my work is deeply iterative and I have high reproducibility needs, because we can't, like, sure, you can have a very iterative exploratory kind of work, say, in a pointy clicky GUI kind of tool, right? But if you don't have any way to make that set of steps you took reproducible, sure, you get the exploratory side, but then you don't have the repeatable, reproducible side.

So what I think is different, if you take people who write code for all kinds of different reasons, I think what's different between someone doing statistical analysis, data science, machine learning, and someone who might be doing more traditional software engineering, by which I mean, like, build a website, build an app, build something of that nature, it's that the work of a data scientist has high reproducibility needs and high needs for supporting iterative exploratory workflows.

I don't know, what do you think, Hadley? Is that a line?

**Hadley Wickham:** Yeah, absolutely. I'll tell you, there's one thing that I found really, I think the thing that I found most surprising, kind of about Positron, and it hints about really about VS Code, and that is it seems like most software engineers have one VS Code open. They're in one project, and they live in that project all the time, and that is really foreign coming from RStudio, where I'd have three or four projects, because you're often working on all these different things in tandem, you have different data analyses, different repos.

Whereas, I think, software engineers, many of them, at least many of them, just live in that one place, and are working on that one code base. And that just, this is fascinating to me. That's never something I would have predicted as being different between software engineers and data scientists. And it's one of the things that's kind of taken me, like, I think we're now at a good point with Positron. Now that I understand that, we've figured out what the workarounds are, and how do you use it. But just really fascinating that that was just such a journey to go on, to learn how do I manage multiple VS Code projects at once, because this is not a problem that most people using VS Code have.

**Julia Silge:** That's a really good point. It's so interesting to think about the workflow of, like, what about this area of work would lead someone to have four open, where the other person has one? It seems, in a way, such a small thing, but it is really surprising, a pretty striking dynamic.

There's also this whole idea of what is a project. One of the things that people coming from RStudio really have to reckon with when they move to Positron, it's like, what is a project? In RStudio, it's very clear. A project is a directory that has your Rproj file in it. Now you're in Positron, kind of anything can be a project. It's just a folder you're opening up into a workspace. And it's not like one is bad and one is good. It's just different, and now we help people manage that.

**Michael Chow:** Just to give some context on VS Code projects, a VS Code project is often like a code base, is that right? Like a package?

**Julia Silge:** So from a conceptual level, VS Code has concepts of a workspace, which is about the same thing as a folder, which is about the same thing as a little P project. These kinds of things are all conceptually about the same. People who came from RStudio have placed a strong amount of meaning on something that is like a capital P project, and it's like a folder that has been imbued with special meaning.

**Wes McKinney:** I think, for me, one of the interesting things, both using Positron and contributing to Positron, has also been the intersection of the experience of building and using RStudio for the last 15 years, and the experience of, from the Python ecosystem, more of the terminal-based data science through IPython, and then Jupyter notebooks.

And so I actually never, I've hardly used RStudio, only a little bit here and there. I used MATLAB and other data analysis environments in the past, but for the better part of 15 years, I've been mostly doing data science in the terminal and using Jupyter notebooks.

And I've run into a lot of the limitations and the rough edges of jumping back and forth between an actual development environment and a Jupyter notebook, where a Jupyter notebook is really great for that interactive exploratory work, looking at, spending a lot of time looking at your data, plotting, manipulating plots, looking at the data.

But to create this environment that's synthesizing all of those ideas in one place that's really optimized for looking at your data and iterating on your data visualizations and all of that, has been really satisfying, since I've in the past felt like I was always grappling with the rough edges of the code editor plus Jupyter-centric environment that I'd been using.

**Julia Silge:** It's so funny to hear you say that, Wes, because ten years ago, when I was transitioning into data science, when I was coming from a background in scientific computing, really comfortable at the terminal, really comfortable, I mostly wrote low-level code at the time, like C code for a lot of numerical kind of stuff.

And I was like, okay, time for me to transition into data science, time for me to get a new kind of job. And I attempted to learn Python first. And I actually never even heard of R, because I didn't come up through stats or anything like that. I literally had never heard of R. I was like, well, I have heard of Python, and other people I know have kind of started using it.

And when I think about, full disclosure, it didn't go very well. And I largely attribute, so there's two things I attribute it to actually, like, why did it go so badly ten years ago for me, when I was like, time to learn Python.

The first one was, I had some real challenges around environment management. Python environment management. Classic. And it was actually pretty frustrating, because I thought of myself as computationally pretty competent. It's like, I'm not bad at computers, why am I failing to manage Python environments?

But then the second one, I think, was that all the tools I was trying to use to do data analysis were not really a good fit. They were not really a good fit. At the time, I was not aware, maybe VS Code wasn't around, but at the time, I was like, can I use a Jupyter notebook? Can I use Emacs, org mode, all these extensions to do data science, and some combination here. And it really didn't go very well.

And it's been pretty interesting working on Positron now, and feeling really, even as someone who works on it as my main job, feeling now, finally, like, ah, now I can use Python in this iterative way, where I have that sort of balance between the iterative exploratory work and the reproducible practices.

**Michael Chow:** Oh, cool. I'm most curious, too, because I think everybody here's using Positron, but I'll just be curious to hear a little bit about what kind of things you've been doing in Positron. Like if you've been doing any data analysis I'd imagine. What kind of projects have you gotten up to driving Positron?

**Julia Silge:** I'll kick us off, and I'll say two examples of things I've recently done in Positron. One is a Python thing, and one is an R thing.

So, we have multiple repos that we use to build Positron, and it turns out, on GitHub, you cannot automatically put the same milestones on all repos. And so, I just did a little project where I used Python and Pydantic and requests to make a little thing that I could run that would pull all the milestones from one repo, match them up, which ones do and don't exist, and write them all to another one. So that's a little iterative exploratory mungy kind of thing.

And then another thing I recently did is, I do use Positron for my R package development. So I recently did a release of, I think the last thing that I did a release of was the pins package. And so I use Positron for my R package development work to be able to go through, run the tests, get it all ready to do a release to CRAN. So those are two for me. What about you all?

**Hadley Wickham:** I mean, like, 90% of what I do is R package development in Positron, and maybe 10% might be pushing it, data analysis. But mostly little stuff. One thing I've been trying to do data analysis-wise is, we have solar, and our solar has an API. And I was like, okay, I really want to get all the data from that downloaded so I can start to analyze it.

**Wes McKinney:** Do you say solar?

**Hadley Wickham:** Solar.

**Wes McKinney:** Solar. Solar power?

**Michael Chow:** It's the Kiwi accent tripping you out.

**Wes McKinney:** I thought it was some kind of enterprise API.

**Hadley Wickham:** I mean, the API was atrocious. So, I spent all last, it was just a little fun project. So I spent all of my allocated time getting through the auth process of the API. But I hope to start to look at the data soon. That'd be pretty fun.

**Michael Chow:** And are you doing 100% of your package development in Positron now? What does that look like?

**Hadley Wickham:** Yeah, 100%. Oh, I had to go cold turkey off RStudio. For a while, I was like, okay, I'm going to, every day I'd start out with the goal of using Positron. And at the end of the day, I'd be, like, oh, that's weird. I'm in RStudio, and I don't remember. Because my fingers are so accustomed. So I had to go cold turkey. I just deleted RStudio from my computer. Now I can go into RStudio when I need to. But yeah.

**Julia Silge:** To be clear, listeners at home, you do not have to switch.

**Michael Chow:** If you want to do like Hadley, you just have to delete RStudio, you know.

**Hadley Wickham:** But I mean, I think that is one of those things. When you are trying out something new, making that hard break and being like, I'm going to devote all my time. Learning anything new sucks. It's always painful. You immediately notice all of the things that were so easy before are now painful and frustrating. And if you don't push through that, you never get to all the good, the cool new stuff that's easier. And a lot of the pain just goes away because you get used to the new way of doing things. But again, you do have to be like, okay, I'm not doing this old thing anymore for a while. I'm going to switch to this new.

**Michael Chow:** Yeah, that's cool. What about you, Wes? And it might be helpful to know also what you're working on in Positron, some content, since I know you've been cooking up a lot on the data grid or data explorer.

**Wes McKinney:** Yeah, I've done a number of small one-off data analysis projects in Positron. So I've been doing development on Positron, building, working with the team, building the data explorer. So if you use Positron to look at a data frame or look at a Parquet file, you're seeing a data explorer that I've worked directly on designing and making a reality.

But recently, I've been interested in analyzing activity on GitHub. So I built some programs with the help of Claude Code to extract with the help of GitHub API keys, lots of activity data to look at what's happening in many of the most popular projects on GitHub. I was just looking at, actually need to wrangle all the data and make a blog post about it, but I was looking at activity across the 100 most popular Python packages on GitHub. And it was really interesting because there was a lot of packages that I've never heard of.

But it's been amazing how much Python has become just total AI land. All of the popular projects, seemingly all of the popular projects on GitHub, at least based on GitHub stars, which, who knows what that's worth, are AI related.

That plus, I've always had an interest in analyzing my personal finances. And so recently, I built a little system also with the help of Claude Code to ingest all of my Amazon and Whole Foods purchase history so that I could look at, you know, is the price of my produce going up over time? Or what are the things that I'm actually spending money on?

And so to be able to be in Positron and be able to pull up CSV files and look at them in the Data Explorer, or to interactively make plots and things like that. It's been really nice. So I'm happy that it's there.

**Julia Silge:** I do want to note, it's kind of interesting, the way Wes, you talk about using Positron is like, oh, I have this more iterative integrated experience. And I feel like things are like, you feel more fluent in some of the things to do.

It's interesting to think about that. Because, Hadley, when you talk about using Positron, sometimes you do sound a bit like, oh, I really had to adjust. And I think it's interesting thinking about the tools that we come from, what they prioritize before, what have various tools prioritized and what has that made that feel like at a transition, either pleasant, or, oh, there's some challenge in it, or there were trade offs. I think it's kind of interesting to notice the way you two talk about using Positron.

**Hadley Wickham:** I have to say, one thing's been really interesting for me is the data viewer in Positron, because I don't think I ever really used the data viewer in RStudio. But somehow the one on Positron, I've been reaching for it more often. I start writing a little bit of code to just find the row and look at it. And then I'm like, oh, actually, I could use the data viewer for this.

And I think something about the way you just click on a CSV file or Parquet file, and it just loads up instantly, it just makes that analysis, which I would have written tidyverse code for before, just feel like it's faster now to explore that directly.

**Wes McKinney:** And I think my sense is because Hadley, over a long period of time, was building and maintaining dozens, or maybe even hundreds at this point, of R packages. And RStudio was his primary development environment. So I could understand that going basically changing your entire development environment. Again, Positron was built to support R developers equally as well as Python developers. But to go from a development environment where he's become very accustomed to for over 10 years, yeah.

**Hadley Wickham:** The other thing is I've had a much more direct line of feedback to the RStudio developers than the VS Code developers. So the things that I really want, like, I don't know, I have to send them a pizza.

**Julia Silge:** That's the key.

**Hadley Wickham:** I do. Actually, I was thinking when Julia was saying that, I have a technique that I use that it's mostly jokingly, but I have these limited edition gold ggplot2 stickers that I sometimes offer to engineers in order to get them to implement a feature I really want.

**Michael Chow:** Wait, that's incredible. And did you, you've kept them limited edition by design?

**Hadley Wickham:** Yeah. You can only get them by being in great service to the tidyverse.

**Michael Chow:** So if people are listening at home, we know pizzas work, gold ggplot stickers work. We're just getting a list of ideas.

**Julia Silge:** People do a lot, people will do a lot for a sticker. That's one of the things.

**Wes McKinney:** Hadley, one thing you mentioned makes me think how interesting it is to be in a situation where we're building on top of a, let's call it a substrate that we don't entirely control.

And I think big picture, I think it's really interesting what the VS Code team has done by making code OSS MIT licensed. It has lowered the bar to experiments in the IDE space. And I think you see this flourishing and of course we can make jokes about, ha ha, did you make a new IDE or another fork? And you're like, yes, it's another fork.

But it is, I think, quite interesting to be in a situation where people can do quite a bit of experimentation in the IDE space because the building blocks are there. The building blocks are there to be able to take your own, make your own hypothesis of what may be a good fit for people.

**Julia Silge:** It definitely is something that has trade-offs, building on top of already existing infrastructure. It reduces the amount of people hours you have to invest to have something that's working that people can actually get their hands on. But there's also trade-offs.

The obvious one probably is any bugs that are in VS Code, we have, unless we decided to fix them separately or anything like that. But some of the other things come up, like sometimes it's surprisingly hard to make a change because of this infrastructure that we just have kind of absorbed.

Another thing is we merge from upstream once a month and that is work that it's kind of hard to predict if it's going to be a lot of work or a little bit of work. And so from a planning perspective, it's actually an interesting challenge. It's organizationally, technically, it's an interesting bet to have made.

I'm still all in. I think we have something that we wouldn't have had otherwise, and that we're able to make something we wouldn't have, but it's definitely not something that has no cost to kind of work through.

**Wes McKinney:** I mean, one of the big deals I see with the code OSS VS Code ecosystem is the plugin and extensions model. So in the past, you'd have an IDE and it would be this static, fairly immutable thing. Maybe you would get some extensions or add-ons from the developer of the IDE. Maybe it's an open source IDE or a commercial IDE, but really you wouldn't have this broad, massive extension ecosystem.

But now the table stakes is that people see something new and they're like, can I get that in a VS Code extension or as an open VSX extension? And so in a sense, that's created this massive gravity well for people building IDE technology. They build new open source tools that support development. And then the way they make that available to developers is through a VS Code extension.

So it's definitely a cost, but if Positron weren't building on the VS Code ecosystem, we would have to figure out a whole new model for how do extensions work and how do we get developers to build extensions and make them work well with Positron. So yeah.

**Hadley Wickham:** And the things in Positron that are clearly superior to RStudio. I like the sort of data science adjacent things. Like every data scientist, at least I believe every data scientist has to be using Git. The VS Code Git pane has had probably an order of two more magnitude of hours put into it than RStudio ever did. Or the find in files. All of this stuff is just kind of table stakes, IDE stuff. We now get that for free and we can invest our time in making really awesome data science specific stuff, which is a big win. Same with the extensions ecosystem.

**Julia Silge:** It's interesting here. It's a lot of the software engineering things kind of come in for free and then you can really cook on the data science and some of those more specific parts.

**Hadley Wickham:** Yeah. I mean, because that's the stuff we have, like we have the institutional muscle and care and experience about that. And those are the users we care about. So we now get to focus on that.

**Julia Silge:** It's interesting. Some of the people who work on Positron directly came over from the RStudio team. There is still an RStudio team, RStudio is maintained, but it's a smaller team now. And there's more people on Positron. So some people came over and it's really interesting hearing them talk about how now we focus on data science. Whereas before in RStudio, any given week, any given sprint of any given month, you had to be like, what are we going to do? Are we going to make some new kind of general IDE feature that people now want? Or are we going to focus on something that's specific to how data scientists work?

**Michael Chow:** So we talked a lot about Positron and some of what it brings to the data science workflow and how we're using it. I'm really curious as an engineering manager on Positron and an IDE, which is a sort of complex thing to bring into the world. And it seems tricky to kind of see it in operation and track. How do you measure success and how has that changed over time?

**Julia Silge:** I think that when I think about success, say on any given day or week or month, a lot of my time is spent thinking about how a complex system fits together. And so I'm not someone anymore who goes really deep in one narrow area. Now I do spend my time thinking about how things fit together and identifying what is the shape of our success and what is the shape of our deficits? And are we comfortable with where we are or what are the places we're not comfortable and we need to invest more in?

Often I find that rough edges happen at the intersections of tools or of teams or of projects. And one that comes to mind for me that I actually invest a fair amount of thinking and talking and literally writing code, talking to people is the intersection of Positron and Quarto. These are two separate teams. They're both at our company, but it's two separate teams. They kind of have different visions or different sort of things they feel like they're in charge of.

**Hadley Wickham:** People are saying it might be good to say what Quarto is a little bit.

**Julia Silge:** Yeah. So Quarto is an open source scientific and technical publishing system. So it is a piece of software that you can use for reproducible dynamic documents. So picture a report or a website or a dashboard that involves executable code in it so that your whole report or website or document can be generated using Python code, using R or Julia code, or even just JavaScript and Observable. So it's a system for, obviously, really important to the work of data scientists.

So for a Positron user, Quarto is really important because it is an engine for the kind of reporting, making websites, that type of thing. And so when we're at that intersection, both of us are important to the other team, but we don't quite report up to the same people. And so it's somewhere where I feel like it takes actually quite a lot of attention and specific energy to make at the boundaries of tools or teams to try to make that experience as good as possible.

So when I think about success, I often think about am I putting my attention at the right places? Is it the things that are important to users? Is it the places where we kind of have a bit of a deficit or a rough edge? I think that's how I think about it.

**Michael Chow:** One thing I'm curious about too is, just to go back to kind of a more basic question, what would you say gets you excited about data science?

**Julia Silge:** So my background is academia. I did a physics undergrad and then astronomy.

*[End of Part 1]*