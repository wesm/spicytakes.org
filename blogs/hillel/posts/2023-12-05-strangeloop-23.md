---
title: "Notes on Every Strangeloop 2023 Talk I Attended"
date: 2023-12-05
url: https://www.hillelwayne.com/post/strangeloop-23/
slug: strangeloop-23
word_count: 1450
---

This is my writeup of all the talks I saw at Strangeloop, written on the train ride back, while the talks were still fresh in my mind. Now that all the talks are online I can share it. This should have gone up like a month ago but I was busy and then sick. Enjoy!


### [How to build a meaningful career](https://www.youtube.com/watch?v=_egQrM13qyM)


Topic: How to define what “success” means to you in your career and then be successful. Mostly focused on psychological maxims, like “put in the work” and “embrace the unknown”.


I feel like I wasn’t the appropriate audience for this; it seemed intended for people early in their career. I like that they said it’s okay to be in it for the money. Between the “hurr dur you must be in it for the passion” people and the “hurr durr smash capitalism” people, it’s nice to hear some acknowledgement that money makes your life nice.


### [Playing with Engineering](https://www.youtube.com/watch?v=6Ao8GS488hA)


Topic: the value of “play” (as in “play make believe”, or “play with blocks”) in engineering. Some examples of how play leads to innovation, collaboration, and cool new things.


Most of the talk is about the unexpected directions her “play” went in, like how her work in education eventually lead to a series of collaborations with OK Go. I think it was more inspirational than informative, to try to get people to “play” rather than to provide deep insight into the nature of the world. Still pretty fun.


### [Is my Large Language Model a Strange Loop?](https://www.youtube.com/watch?v=Gx2mDuVAClo)


(Disclosure, I didn’t actually see this talk live, I watched [Zac Hatfield-Dodds](https://zhd.dev/) rehearse and gave feedback. Also Zac is a friend and we’ve collaborated before on [Hypothesis](https://hypothesis.works/) stuff.)


Topic: Some of the unexpected things we observe in working LLMs, and some of the unexpected ways they’re able to self-reference themselves.


Zac was asked to give the talk at the last minute due to a sickness cancellation by another speaker. Given the time crunch, I think he pulled it together pretty well. Even so it was a bit too technical for me; I don’t know if he was able to simplify it in time for the final presentation.


Like most practical talks on AI, intentionally or not he slipped in a few tricks to eke more performance out of an LLM. Like if you ask them to answer a question, and then rate the confidence of the question they asked, they tend to be decently accurate at their confidence.


Zac’s also a manager at [Anthropic](anthropic,com), which gave the whole talk some neat “forbidden knowledge” vibes.


### [Concatenative Languages Talk](https://www.youtube.com/watch?v=umSuLpjFUf8)


(Disclaimer: Douglas is a friend, too.)


Topic: Why stack-based languages are an interesting computational model, how they can be Turing-complete, and some of the unusual features you get from stack programming.


The first time I’ve seen a stack-based language talk that wasn’t about Forth. Instead, it used his own homegrown stack language so he could just focus on the computer science aspects. The two properties that stick out to me are:

1. Stack programs don’t need to start from an empty stack, which means entire programs will naturally compose. Like you can theoretically pipe the output of a stack program into another stack program, since they’re all effectively functions of type `Stack -> Stack`.
2. Stack ops are associative: if you chop a stack program into subprograms and pipe them into each other, it doesn’t matter where you make the cuts, you still get the same final stack. That’s really, really cool.


My only experience with stack machines is [golfscript](https://www.hillelwayne.com/talks/esolangs/). Maybe I’ll try to pick up [uiua](https://www.uiua.org/) or something.


### [Comedy Writing With Small Generative Models](https://www.youtube.com/watch?v=M2o4f_2L0No)


Topic: “Small” generative AI models, like “taking all one-star amazon reviews for the statue of liberty and throwing them into a [Markov chain](https://benhoyt.com/writings/markov-chain/)”.


This was my favorite session of the conference. The technical aspects are pretty basic, and it’s explained simply enough that even layfolk should be able to follow. His approach generates dreamy nonsense that should be familiar to anyone who’s played with Markov chains before.


And then he pulls out a guitar.


The high point was his “Weird Algorithm”, which was like a karaoke machine which replaced the lyrics of songs with corpus selections that matched the same meter and syllables. Like replacing “oh I believe in yesterday” with “this is a really nice Hyundai”.


I don’t know how funny it’ll be in the video, it might be one of those “you had to be there” things.


### [An approach to computing and sustainability inspired from permaculture](https://www.youtube.com/watch?v=T3u7bGgVspM)


Topic: The modern pace of tech leaves a lot of software, hardware, and people behind. How can we make software more sustainable, drawn from the author’s experiences living on a boat.


Lots of thoughts on this one. The talk was a crash course on all the different kinds of sustainability: making software run on old devices, getting software guaranteed to run on *future* devices, computing under significant power/space/internet constraints, and everything in between. I think it’s intended as a call to arms for us to think about doing better.


I’m sympathetic to the goals of permacomputing; what do I do with the five old phones in my closet? That’s a huge amount of computing power just gone to waste. The tension I always have is how this scales. [Devine Lu Levinga](https://100r.co/site/home.html) is an artistic savant (they made [Orca](https://metasyn.srht.site/learn-orca/)!) and the kind of person who can live on a 200-watt boat for seven years. I’m not willing to give up my creature comforts of central heating and Geforce gaming. Obviously there’s a huge spectrum between “uses less electricity than a [good cyclist](https://www.trainerroad.com/forum/t/targeting-200-watts-for-1-hour/40043)” and “buys the newest iPhone every year”, the question is what’s the right balance between sustainability and achievability.


There’s also the whole aesthetic/cultural aspect to permacomputing. Devine used images in dithered black/white. AFAICT
 this is because [Hypercard](https://en.wikipedia.org/wiki/HyperCard) was black/white, lots of retrocomputing fans love hypercard, and there’s a huge overlap between retrocomputing and permacomputing. But [Kid Pix](https://en.wikipedia.org/wiki/Kid_Pix) is just as old as Hypercard and does full color. It’s just not part of the culture.


Nit: at the end Devine discussed how they were making software preservation easier by writing a special VM. This was interesting but the discussion on how it worked ended up going way over time and I had to run to the next session.


### [Can a Programming Language Reason About Systems?](https://www.youtube.com/watch?v=FuhEHuPExso)


(Disclaimer: Jesus I’m friends with way too many people on the conference circuit now)


Topic: Formal methods is useful to reason about existing legacy systems, but has too high a barrier to entry. Marianne made a new FM language called “Fault” with a higher levels of abstraction. Some discussion of how it’s implemented.


This might just be the friendship talking, but Fault looks like one of the more interesting FM languages to come out recently. I’m painfully aware of just how *hard* grokking FM can be, and anything that makes it more accessible is good. I’ll have to check it out.


When she said that the hardest part is output formatting I felt it in my soul.


### [Making Hard Things Easy](https://www.youtube.com/watch?v=30YWsGDr8mA)


Topic: Lots of “simple” things take years to learn, like Bash or DNS. How can we make it easier for people to learn these things? Four difficult technologies, and different approaches to making them tractable.


I consider myself a very good teacher. This talk made me a better one.


Best line was “behind every best practice is a gruesome story.” That’ll stick with me.


### Drawing Comics at Work


Topic: Randal Munroe (the xkcd guy)’s closing keynote. No deep engineering lessons, just a lot of fun.


## Postmortem


Before Julia Evans’ talk, Alex did [A Long Strange Loop](https://www.youtube.com/watch?v=suv76aL0NrA), how it went from an idea to the monolith it is today. Strange Loop was his vision, an eclectic mix of academia, industry, art, and activism. And it drew a diverse crowd because of that. I’ve made many friends at Strangeloop, people like [Marianne](https://www.bellotti.tech/about) and [Felienne](https://en.wikipedia.org/wiki/Felienne_Hermans). I don’t know if I’ll run into them at any other conferences, because I don’t think other conferences will capture that lightning in a bottle. I’ll miss them.


I also owe my career to Strangeloop. Eight years ago they accepted [Tackling concurrency bugs with TLA+](https://www.youtube.com/watch?v=_9B__0S21y8), which got me started both speaking and writing formal methods professionally.


There’s been some talk about running a successor conference (someone came up with the name “estranged loop”) but I don’t know if it will ever be the same. There are lots of people can run a good conference, but there’s only one person who can run *Alex’s conference*. Whatever comes next will be fundamentally different. Still good, I’m sure, but different.
