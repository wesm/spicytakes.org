---
title: "Julia Silge Part 2: Glue work, licensing, and open source in the age of LLMs"
summary: "Podcast at The Test Set (Posit)"
date: 2025-10-21T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-julia-silge-part2
word_count: 5811
source_file: transcripts/2025-10-21-test-set-julia-silge-part2.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=WibR9Sumle4"
---

{{< video https://www.youtube.com/watch?v=WibR9Sumle4 >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this second part of our conversation with Julia Silge on The Test Set, we explore her approach to managing work across team boundaries at Posit, her thoughts on open source licensing in the age of LLMs, and what motivates her in data science. Julia describes how she gravitates toward "glue work" at the edges of teams and systems, where attention can have outsized impact even though the work is often thankless.

The conversation takes an interesting turn when we discuss Julia's time at Stack Overflow and the implications of LLMs having absorbed community-generated content for training. Julia raises important questions about what happens when the data generation that made these models possible has fundamentally changed because users now ask LLMs instead of contributing to public knowledge bases. She also shares Posit's evolving approach to open source licensing, explaining why Positron uses an Elastic license rather than MIT to prevent large cloud companies from directly monetizing the software without contributing back.

We also discuss the tension between focus time and cross-team connection in remote work, and Julia reflects on what drew her away from the academic specialization track in astronomy toward the applied, systems-oriented work of building data science tools.

## Key Quotes

> "There is so much space for massively leveling up how people perceive your tools when attention is spent at the boundaries of things. And it is often somewhat thankless work in the sense that you don't always get as much credit for stuff that ends up gluey." — Julia Silge

> "People can't acknowledge pain that they didn't experience. You're making pain go away, but it's because people never experienced it, it's hard for them to appreciate." — Julia Silge

> "One of the very valuable things you can do is convince people that this is their problem to solve. This is a real problem that exists. Maybe someone else should fix it, but they're not going to. You could have a really big impact by going outside of your comfort zone, tackling this problem that crosses some boundary you don't normally cross." — Hadley Wickham

> "The big model training organizations came and took data that I would say morally belongs to all of us. They took it and they trained a model, and now the data that was used to make that possible is now not being generated at the quantity or in the way that it was before." — Julia Silge

> "I'm not religious about these specific licenses, because I think they're just things we wrote. How are they turning out? How do we want to iterate on them? What do we think is best for us as a community?" — Julia Silge

> "Open source is kind of like a gift. This is a gift that I'm spending my time on and giving to the world, but if you're going to abuse that gift, I don't have to keep giving it." — Hadley Wickham

> "What will be the steps that will keep our ability to get answers to our coding questions? What got us to here is not what we are doing now because the ecosystem has substantively changed." — Julia Silge

> "I love working on data science tools because it is such applied, real world work. It comes up against the mess of people's data, and talking about systems and processes and tooling around that is really motivating to me." — Julia Silge

> "How will developers be motivated to discover and learn new technologies that their favorite LLM doesn't know about? And how is that going to affect the development of new open source software projects?" — Wes McKinney

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. This episode is part two of a conversation with Julia Silge, data science leader and engineering manager at Posit.

**Michael Chow:** Yeah, it's so interesting to hear the edge of experience as being your focus and even that inside of Posit and inside of companies being a big, from what I heard, like a challenge across teams. Where does that thinking show up for you usually? Is that in like a notebook or document? Where do you like to kind of refine your thoughts or shape them?

**Julia Silge:** Yeah, yeah, yeah, yeah. I think I work in a combination of GitHub issues. If things can be broken down into, say, like a fairly concrete piece of work, then I'm like, okay, I'm somewhere there. Another sort of way of working that I and people on my team work in is writing documents, whether that's like feature specs that are very technical or whether that's more like a description of the kind of behavior we expect to be a little more like high level.

I think that another way that this comes out is actually in like synthesizing bits of smaller information, whether that is, you know, we have as a public facing product where that has quite a number of users out there, right? So there's like stuff comes in on GitHub, of course. So, you know, stuff comes in. You know, we watch Stack Overflow. We watch like various discourse type boards and whatnot to like kind of be able to synthesize.

And often that involves like a kind of like a bottom up kind of organizational, like information organizational kind of thing of like how can we like how successfully can we understand how these things are related? Because they 100% are, right? Like very few, it's rare when something comes up and we're like, well, that's like nothing else we've seen before. Like we either these are thematically related or like they're different ways of the same kind of problem. So I would say in a practical sense, it's like, like I'm writing in different places depending on who the audience is or like how much and then in terms of organizationally thinking, I do a fair amount of like those kinds of like information organization kind of like activities.

**Michael Chow:** Do you have like a preferred like tool or system that you use? Like are you like a mind mapper or like really into Obsidian or?

**Julia Silge:** I feel like because of where our team stuff is, I end up in GitHub projects a lot, which are pretty good for things that are captured as really concrete type things. For things that are a little bit less concrete, I think I am mostly in documents and I am mostly in documents that are like shareable because like Obsidian is great for your internal stuff.

**Hadley Wickham:** I feel like you're talking around the fact that you did everything in Google Docs and you don't want to admit it.

**Julia Silge:** I don't want to admit it. I spent all day in Google Docs and I just don't want to admit it.

**Hadley Wickham:** You're like, there's a little Google Doc, but Obsidian and then the Google Docs show up.

**Julia Silge:** No, I mean, the thing is Obsidian, I don't know. You don't have any like shareable way of using Obsidian, do you? It has to be another.

**Hadley Wickham:** No.

**Julia Silge:** Yeah, yeah. And so much I mean, so much of what like I need to get feedback from people on it or like so the fact that I so much of what I do involves going to other people, either for their input or for them to agree, you know, like it's really the collaboration.

So speaking of that, we do have we do use actually Quarto as well for a good chunk of this because we have like really extensive internal documentation for like process like iterating on plans that is less like a that is less like a situation that might have been a GitHub issue and also less something that like might have been a feature spec that's like kind of throw away like right at one time do it, you know, like don't come back to it. But stuff that we maintain over time about process and about how things work that we do actually use Quarto for. And then the collaboration looks like Git looks like, you know, like those kinds of modes.

**Hadley Wickham:** Yeah, I'm really looking forward to the day where we figure out how to like have shareable commentable Quarto docs. That's the dream.

**Julia Silge:** That's a dream. Yeah.

**Wes McKinney:** I've become like a pretty heavy Obsidian user mainly as like a capture tool because like stuff will come up in like a Slack channel that I'm that I'm a part of or over email. And I find that like if I have too many like unread tasks in different places that eventually like I'll just forget things and I'll drop balls. And so I find like capturing things in Obsidian is like my personal don't forget this list of things to not forget and to get things out of my inbox. But then, you know, immediately bubble them up if it belongs in a GitHub issue that I open a GitHub issue for visibility or if it needs to go into Google document.

**Michael Chow:** I have to say too, I feel like you inside Posit like we find you wrangling a lot of kind of like meetings or I want to say like edgy, not edgy. Okay, edgy is the wrong term, like at the edge of experience types, things like if I could give one example, it's the Python open source meeting, you're really a facilitator of the Python open source meeting, which I've always found really, pretty inspiring that you like there was it seems like to me like there was a gap, like we need someone to fill this. And there are a lot of people floating around, but that you really kind of took it and ran.

**Julia Silge:** So I think there's different ways to operate as a manager. And some people who are really successful as managers have a really strong sense of ownership of like, this is my team, I am going to make them successful. If this thing is successful, I am successful. And that is great like that. But that's not quite the way I operate.

I think as a manager or a leader, there is so much space for a slam dunk experience, there is so much space for massively leveling up how people perceive your tools, when attention is spent at the boundaries of things. And it is often somewhat thankless work in the sense of like, you don't always get as much credit for stuff that ends up gluey, you know, like, it's also like pain, people can't acknowledge pain that they didn't experience.

**Hadley Wickham:** Yeah. Right?

**Julia Silge:** Yeah, I think that's like, you're making pain go away. But it's because people never experienced it, like, it's hard for them to appreciate.

**Hadley Wickham:** Yeah, yeah, yeah.

**Julia Silge:** Super. I think that sort of work is like, so incredibly important. It's important. And also, I feel like there's often a lot of space to really, you know, you're not like you're trying to eke out some tiny little bit of performance improvement, making something tiny. It's like, you can usually massively level up some sort of painful experience by paying attention at some boundary.

And so I do think, you know, like internally at Posit, I do end up doing things like maintain the Quarto extension for a while. I mean, you know, like, well, you know, stuff like that, because it's like, well, no one else is quite doing it. And it's important to this team and this team. And I think it's because I have seen a lot of, I have seen, I'm gonna say, really outsize impact from attention at those spots that I think have a big picture kind of like effect, I guess.

**Hadley Wickham:** It's sort of fascinating to me just how much like, kind of team identity starts to play. Like, I think like in general, I think it's a good thing for a team to have a strong sense of like, this is what we do. But it can mean that there's these things that like are really important that kind of fall between the gaps of every team.

And it's surprisingly valuable to me. Like, it surprises me. Like, I don't think it's really surprising. It surprises me. Like one of the very valuable things you can do is convince people that this is their problem to solve. Like, this is a real problem that exists. Maybe someone else should fix it, but they're not going to. Like, you could have a really big impact here by like, kind of going outside of your comfort zone, like tackling this problem that crosses some boundary you don't normally cross. That can be so, so valuable.

**Michael Chow:** Yeah, I feel like one question I have is, this is kind of like inside baseball, having seen, I've noticed people at Posit have a lot of chats, like monthly chats, just like catch ups and stuff like that. I'm really curious how, say Julia, you've approached kind of like keeping in touch with people, whether, I don't know if you have a chat with the Quarto team or if that's part of your strategy and how you approach kind of just catching up or water cooler type stuff.

**Julia Silge:** So our company is fully remote, right? Like it's fully remote and I am very comfortable with remote work. I've been working remotely for a really long time. So I'm very comfortable with like asynchronous communication. I'm very comfortable with like kind of a lot of habits around remote work. I don't feel disconnected. Like I don't feel isolated.

And I think part of that is because I do have habits around like kind of having a low bar to asking somebody, say, to pair or like having a low bar to like, hey, can I get on a call with so-and-so and like to talk about this thing that came up and that we might need to do.

And I think that the, you know, there's trade-offs there, of course, with time, you know, and like how much heads down uninterrupted time do you need for your work? And I, like most managers or I don't know, some proportion of managers at Posit, I do write code as well still. We're like, we're not, we're a place that tends to, at some companies, you know, people who manage the expectation is you will not write code. You cannot do a good job at both. And there, you know, there is some truth to people who make that argument that like, if you're going to be a really good manager, you can't also be trying to write hands-on code. But for better or worse, that's not, I would say, the norm for most people, like most managers at Posit. Most of us do have kind of roles where we do contribute, even like on a, like a concrete, like I wrote this code kind of way.

And so kind of balancing that, what's it like to have heads down, heads down, like focus kind of time with this connection? Like there's definitely a tension there. There's a tension there. I think at our company, there's often a lot of value placed on focus time on that. That's really where we get our, like why we are able to build excellent products is because we allow people to have this focus time. And I think that is totally true. And I think at the same time, that often is in tension with people knowing what's going on and other teams are being connected.

And I probably, for internally at Posit, I probably am one of the people that biases a little more towards boundaries, connections, like how are teams working together? Yeah.

**Michael Chow:** Yeah, that's really cool. I feel like with wrangling, like these kind of complex systems and doing hands-on work and managing, one thing I'm curious about too is just to go back to kind of a more basic question, what would you say gets you excited about data science?

**Julia Silge:** That's a great question. That's a great question. So yeah, no, I find, so my, you said my background is like academia. Like I, you know, I got, I did, I did like a physics undergrad and then an astronomy PhD. And so I went really narrow and I had a great time in grad school, actually. Like I loved my project. I had a good relationship with my advisor. Like I had a really good experience.

And then when I went to be a postdoc, there were a variety of reasons why I was like, wait, is this for me? One of them was, I was like back in a physics department and I was like, oh, that's right. Physics departments can be kind of toxic. Like overall astronomy departments tend to be full of much more practically minded people, like a lot more like applied kind of thinkers, people who make instruments, people who analyze real data.

And so part of it was being back in a physics department, but part of it was just progressing a bit in academia to find that, oh, right. I have to keep specializing for forever. I have to keep getting the better and higher, more and more expertise on the narrower and narrower thing. Like that's what this path is. And I kind of came to grips with the fact that actually I was not so interested in that. Like that was not, that did not bring me a lot of like joy and personal fulfillment.

And I started to think through like what, like actually what do I like doing? And that has like lasted through the whole rest of my adulthood and career to realize, oh, and now I would frame as what really motivates me, what I really get excited about is I really love learning about and being involved in how people's really applied work. And the processes and systems around people's, like how people are really doing their work.

And so I love working on data science tools because it is such applied, it is such like real world applied work. It comes up against like, it comes up against the mess of people's data and like talking about systems and processes and like tooling around that is like really motivating to me.

So part, like, do I think data science is the only thing I could be happy, like working in a field? No, honestly, part of it was random chance that like I came out of astronomy at a time when transitioning into data science was like a thing that people were doing. So part of it is this kind of random, like it probably could have been something else, but I think the reason why the characteristics of it that I'm like, oh yeah, this is for me, this is a really good fit for me is this, it gives me an opportunity to work on tools that are about like the design of applied systems that people use for their work. So, and I just love that. I love it. Yeah.

**Michael Chow:** Yeah. That's so cool. This is, I think a related thing on the point of these systems that people use for their work and these real world problems. One thing I was thinking about as I was preparing for this is I remember that you were at Stack Overflow and it almost made me think about this complexity of the system, thinking about how people get answers to things, to questions about programming.

I'm really curious, almost in the context of the age of AI and how people seek answers and complex systems. I'd be curious if you could say a bit about your time at Stack Overflow and whether you've thought about kind of that role of a site like Stack Overflow and how people get answers today with AI. I'd be so curious to hear.

**Julia Silge:** Yeah. So I was a data scientist at Stack Overflow for about five years and it's a very interesting place. So this was before, this was before the rise of LLMs. Like this was, I was there.

**Hadley Wickham:** Before the fall of Stack Overflow.

**Julia Silge:** So it was, it was a very interesting place to be a data scientist. Maybe roughly, let's say roughly half my time would be spent on working on what probably what you think of as like public Stack Overflow, like people who come, ask questions, answer questions, the voting system, comments. How do we deal with content? Like, or, you know, like how does the, how is content curated? How do people find content? So stuff, so maybe roughly half my time was spent on that.

Roughly half my time was spent on the ways that Stack Overflow at the time made money, which would be a combination of like ads, including like ad content-based ads. And then there was like a private Stack Overflow kind of like product, like the people would use internally kind of like as an alternative to, you know, like other internal knowledge kind of basis.

And it was, it was really interesting, both in like a web 2.0 way, like which what, like, because of the age I am, like that was a, that was like a big part of like how I experienced the internet, right? Was like, oh, actually the internet is for you to come and post your stuff on, you know? Like that was for me really empowering at the time, like back at the time. And so like Stack Overflow was part of that, that wave, right? Of like, what is internet technology like? What is technology like?

So it was interesting in like understanding, like, okay, how can such an organization be sustainable? Like, what are ways that like you could build a business on this? Because the founders of Stack Overflow were interested in building a business. They were not interested in like a Wikipedia-style model. Like they wanted to build like a value-generating business. Like, okay, what are some attempts of that like to go?

And now kind of after the advent of these LLM tools, which to be clear, slurped up all of Stack Overflow in their training data, you know? Like, what does it look like now? Like, are we in a, like a lot of sort of the back and forth, you know, question, asking, answering has now moved from a place that like it could be viewed as a communal resource. It has all been slurped into places that are not accessible to us as a community anymore.

So it's like the big model training organizations came and took, they took data that I would say morally belongs to all of us, right? Like morally, ethically, that's our data. That's our data as like human beings, right? And they took it and they trained a model. And now they have like, they have not only like made something they can make money with off of and made useful tools, right? But it means that the data that was used to make that possible is now not being generated at the quantity or in the way that it was before.

So I think it's super interesting to think about where are we today and what are going to be the, what are going to be the steps that will keep, for example, our ability to get answers to our coding questions, you know? Like, like what will, what will that look like going forward?

I'm not, I mean, I'm not a big doom and gloom person, you know, I'm not saying like the world's ending and anything like that, but I think it's some real questions because what got us to here is not what we are doing now because the ecosystem has substantively changed. The world has changed. The world has changed in terms of what, like where is that data coming from? Or like where are the questions and answers? Like, where is it such that it can be useful to the community as a whole?

**Hadley Wickham:** Do you think it's changed how you think about like, because I think Stack Overflow was all like Creative Commons licensed. So like kind of legally, the LLM providers are, you know, fine. Does it kind of change how you think about that license? Because I have to say for me, like for the longest time, that just seemed like absolutely the right thing to do. And now I'm like, I don't know, that's just giving all the stuff away for free is kind of, I don't know.

**Wes McKinney:** Well, there was like, there was an inflection point where I think the license for content posted on Stack Overflow changed where prior content prior to that date, it became this like massive IP contamination issue where developers would copy and paste stuff from Stack Overflow into their company's proprietary code bases. And then, you know, if you go to sell a software product that code would turn up during like, you know, IP legal due diligence, and say, oh, like you used code from Stack Overflow, and maybe it could just a small snippet, but either you have to figure out how to replace that code with your own IP, or you have to go and find the original author and ask them for permission to use that code.

I think in the meantime, it's been there was a change to make it more lenient, but still like any content that was posted prior to that date has like the old more restrictive license, but it's interesting. It's very interesting. The licensing around these kinds of issues is very, it's very, very interesting.

**Julia Silge:** And I think questions are on how these licenses gotten us what we thought they were going to get us like how these, because these all these open source licenses, you know, like came up and like have been hashed out in a time when like it was a technologically different kind of time than what we have now in terms of the constraints.

And people talk about like, okay, can we iterate on these? Can we think about these differently? Like something that, you know, there's still discussion about is like iterations on these licenses that make kind of moral or ethical claims, right? Like I want to exclude certain kinds of uses like there are these licenses that are like, mostly open source-ish, but they exclude some uses like maybe defense or something like that. So there's that sort of category of iterating.

There is the category of license that's like mostly open source-ish, but I put some restraints on say, how you can platform it. So in full disclosure, Positron has a license like that. Positron has a license that is not a true OSI approved license. It's an Elastic license. And the reason why we did that was because like our experience as a company working on open source software has showed us huge benefit. We're huge believers. We're committed to open source software, the pieces of the software that you can make money by platforming them. We ended up making the call that like, actually we don't want another giant, say cloud company to be able to get directly revenue from just making available the thing that we made.

So I think like I've been involved in open source for a pretty long time. I'm a huge believer in open source. I'm not religious though, about these specific licenses, because I think they're just things we wrote and how are they turning out? How do we want to iterate on them? Like, what do we think is best for us as a community?

I mean, our company, we're iterating with that. We're being really explicit, like this kind of software, like a Python package or an R package, it's like MIT, this kind of software, we're not going to do MIT anymore because we think it is not aligned with our long-term goals around the sustainability of our company. Super interesting questions.

**Hadley Wickham:** I think, yeah, to me, like a lot of it is about like, to me, like this open source is kind of like a gift. Like this is a gift that I'm, you know, I'm spending my time on and giving to the world, but it's not like, if you're going to like abuse that gift, like I don't have to keep giving it. Like there's some, I don't know, there's some sort of sense of, like, I want to be giving it to people who are like, they don't necessarily have to be giving it back to the community. Like again, not everyone's in a place, like I'm happy for, you know, a lot of this work just to be used by people, but it just starts to feel like exploitative when like big companies that are like tens or hundreds or thousands of times the size of Posit, like make money off our work. That just feels a little gross.

And yeah, I'm not like so religious about this. Like it's about freedom. It's about all of these other kind of like big philosophical ideas. Like to me, it's more about like community and, you know, trying to share what people are trying to do good in the world in some way, but at the same time accepting, like, if you try to pin down exactly what that means too, like you get lost in the details and you just have to accept that people are going to use it for things that you don't, you wouldn't personally like them to do. But I don't know, on the whole, I kind of hope that people are using open-source software, like make the world a better place, not just make money for themselves.

**Michael Chow:** Yeah. It's helpful to hear the kind of how Posit is trying to like thread the needle between things like MIT and the Elastic license and find things that kind of work for everyone in the different circumstances.

**Julia Silge:** It's for sure an experiment. It's like, okay, let's try this. How's this going to go? You know, like, and I think I mean, so many of these things are untested and like, we don't quite know, you know, like how these things will play out, but it definitely is interesting.

**Wes McKinney:** The thing that's been on my mind a lot is if, how will developers be motivated to discover and learn new technologies that their favorite LLM doesn't know about? And how is that going to affect the development of new open-source software projects? How did the LLMs get the content that they need to get trained on new projects?

And so, you know, for folks like us that have been in the business of teaching people how to do data science, building data science projects, it presents this conundrum, or this maybe chicken and egg problem of just the nature of building new open-source software for data science is, I feel like going to be permanently altered and how that affects like adoption rates. And just how long does it take before a new project is important enough that the LLM providers go to the effort of like creating a training corpus to teach the LLM how to use your new open-source library that doesn't have that much content available on GitHub.

**Hadley Wickham:** And we're on the kind of like the lucky side of this. Like most of the tools that we have created, like are now in the training sets. Like we are kind of like, but I don't think we want to be like locked. Like I don't want ggplot2 to be the visualization package used for the rest of humanity because it's impossible to create a new system because everyone uses LLMs. If it's not in an LLM, they don't use it. Like that doesn't seem like a win. Like how, what's the, like, how does the death part of the open-source life cycle, like how does that change?

**Julia Silge:** It's interesting with Stack Overflow too, like to these points, like a lot of my early experience with ggplot2 was on Stack Overflow where Hadley would answer questions, but you would see the question and then you would see like a couple different options. And one would be ggplot. So it's interesting to think about sometimes, yeah, the answers that people might get now, if they ask an LLM, if it both, you might not even see that Hadley's answering and you might not see the range of tools or you might only see certain tools, I guess, in the output to Wes's point.

**Michael Chow:** So yeah, Julia, I really appreciate you coming on and just like opening up the complexity of this, like data science workflow, how to reach your senator, you know, is there any parting words for people at home, either ways to help you with Positron or things you'd encourage people to check out?

**Julia Silge:** Yeah, yeah. So if what we've been talking about today has piqued your interest in Positron, you can go to positron.posit.co for installers and documentation. And I think I am excited for more and more people to get exposed to it and to try it out.

And it's been really delightful to talk with the three of you here today. Thank you so much for having me on and for asking such insightful questions. I honestly haven't thought about the pizza in quite a while. So it was a little bit delightful to get to revisit that.

**Wes McKinney:** No, it's been such a treat.

**Michael Chow:** Thanks so much for coming on.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio Adji. For more episodes, visit thetestset.co or find us on your favorite podcast platform.