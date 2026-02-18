---
title: "Learning to like design documents"
date: 2016-06-03
url: https://jvns.ca/blog/2016/06/03/learning-to-like-design-documents/
slug: learning-to-like-design-documents
word_count: 1407
---


Hi everyone! Today we’re going to talk about software engineering and process!


A design document is where, before starting to implement a system, you write up a thing explaining what the system is supposed to do first and how you’re planning to accomplish that. I think there are basically two goals:

- tell people what you’re doing
- figure out design problems with the system before you’ve been coding for 2 months


I understand that it’s super important to think ahead a lot before huge projects, but a little bit of thinking can be helpful even for smaller projects. I asked some people recently if they write design docs for small projects and some of them said “yeah totally! small ones! it helps! :D”.


I used to get kind of grumpy when someone was like “hey julia can you write a design document for your system?” It would seem like a reasonable idea, though, so I’d try to do it! But the first couple of times I tried to write one I felt like it didn’t actually really help me! I liked the idea in principle, but I didn’t really know how to apply it and I felt like it was hard to get good feedback.


Last week I wrote a design doc and I thought it was sort of helpful. Here are some current thoughts.


### it’s hard to get someone to read it


One of the first reasons to be grumpy about writing a design document is “UGH. NOBODY IS EVEN GOING TO READ THIS. TOO MANY WORDS. WHY?!”. And I think it’s actually kind of true! Getting a good review of a system design is hard! If it is a big system, the person reviewing your system has to put this whole hypothetical thing into their head, and think about every single thing that could go wrong, and think about the risks of all those things, and what already exists, and how it fits with those things, and how it will scale, and UGH.


So it’s not like a simple code review where you’re like “hey can you take a look after lunch?”. I ended up trying to think about it as a personal tool – I came up with some questions I wanted to answer before I started writing code, wrote down the options, and then for each one picked an answer that seemed reasonable to me.


I realized that instead of trying to get someone to read it, I could just talk to them and explain everything in the document to them and my thinking, and then they could suggest ideas for what that might work better, or things that could go wrong that I hadn’t thought of!


So then instead of it being like “Here is a LARGE DOCUMENT for you to read please review” it was more like “I have written extensive notes so that I can make sure to ask you all the most important questions I have and we can have a SUPER PRODUCTIVE MEETING”. A+


### but what color will we paint the bikeshed


The second reason to be grumpy is “oh no I will write it and I’ll get a lot of contradictory feedback that is not that constructive”.


A couple years ago at work, I had a small project, and I wrote an email with my thinking & questions about the project to try to think through how I was going to do it. Good idea, julia!


But then a bunch of people replied with a whole bunch of different suggestions and started a long discussion on the email thread that was not that useful to me.


This wasn’t a disaster – everyone was just trying to help! Nobody was being a jerk. It did not ruin my life. I asked my manager to talk it through with me and we came up with a reasonable plan and the project got done and everything was fine.


a couple of things about this:

- asking more people for feedback isn’t always better. Sometimes asking just one or two people is ok if it’s a small thing.
- I like to remember that having a bunch of conflicting opinions is actually a normal (and often good!) thing that won’t go away, and you just need to figure out some tactics to deal with it (maybe: “have a meeting with exactly one person from each team involved”, “figure out what hidden assumptions people have that are different”)


### smoke tests


Also, on “nobody reads the whole thing” – it’s really useful to go in-depth into the design with *someone*, but every single person doesn’t need to spend hours thinking about the thing.


I think it’s sometimes useful to ask “hey just read this for 10 minutes and see if anything makes you EXTREMELY TERRIFIED AND WORRIED”. And often the answer is “yeah seems fine”, which is good! It doesn’t mean there are no problems, but it means that that person has some vague idea of what you’re doing and doesn’t think it’s totally unreasonable.


### ask about one thing


Also also on “nobody reads the whole thing” – in general with any large review it’s way easier if you’re like “hey, i’m worried about this specific aspect and I know you know a lot about it – what do you think?” instead of “please read all the pages and tell me everything you think about everything”.


### coding is easier if you think first


This is maybe sort of obvious! But – sometimes I start coding, and then an hour or day in I’m like “oh no, I didn’t think about this whole aspect of this project, hmm, what do I do?”


After writing this design doc, when I went to write the code I was like, oh, I made a lot of these decisions already. This is easy to write! Cool! And there were still unexpected difficulties (surprise: unexpected difficulties never actually go away), but I felt like it helped.


### you can’t predict everything and it’s okay


Another thing that made me grumpy about design docs was that – this idea that you can predict all the flaws in advance and design the perfect system is actually a total lie. I still ran into things that I’d forgotten to consider!


So I think writing a design doc isn’t necessarily about predicting **everything** that could ever possibly go wrong. I mean, maybe there are magical wizards who can predict everything. But for me it really helped to let go of this idea that we’re going to be able to design the perfect system just because now I have a document with “Design” written at the top and some people to help me review it.


Instead, we do the best we can, and make changes to adapt as we go along!


### watch your decisions change


I asked a bunch of wonderful people about design docs a couple months ago and someone – I forget who right now – said “the reason you write them is **because** your requirements & ideas of how things should work will change over time, and it’s useful to track that”. And this is totally true! Often I’ll make a design decision, forget about it, and then 8 months later be like “ugh who made that decision and why???”. And then it was me, and I need to dig up an IM conversation from 8 months ago to try to figure it out.


Things change in software all the time. Maybe:

- 2 years later, the software you decided to not use is a lot more mature
- the thing you thought was awesome, after doing some more research, had some really serious flaws that might now be a dealbreaker
- you suddenly are handling 20x more data than you thought you would be
- you did user research and the users said a lot of really unexpected things that make you want to reprioritize


So if nothing else, I think design documents are cool as archaeological artifacts so that people from the future can understand you and why you decided what you did.


### what does design document mean to you?


I think the word “design document” means some really specific things to
different people. Maybe it means a totally different thing to you! I’d be
interested in reading things that you found helpful when designing systems. As always I’m [on twitter](https://twitter.com/b0rk).
