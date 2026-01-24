---
title: "Revisiting the XML Angle Bracket Tax"
date: 2008-06-23
url: https://blog.codinghorror.com/revisiting-the-xml-angle-bracket-tax/
slug: revisiting-the-xml-angle-bracket-tax
word_count: 1115
---

Occasionally I’ll write about things that I find sort of mildly, vaguely thought provoking, and somehow that writing turns out to be *ragingly controversial* once posted here. Case in point, [XML: The Angle Bracket Tax](https://blog.codinghorror.com/xml-the-angle-bracket-tax/). I’m still encountering people online **who almost literally *hate my guts* because I wrote that post**. You’d think I kicked their dog, or made inappropriate romantic overtures toward their significant other.


Well, first of all, we are talking about XML the markup language, [not XML the religion](https://blog.codinghorror.com/software-development-its-a-religion/), right?


I hope so. I try not to get emotionally involved with the tools and technologies that I use, if I can avoid it. This doesn’t mean I can’t be enthusiastic or critical of those tools and technologies, but I’m not *married* to the stuff either way. Who needs all the emotional baggage?


Obviously I failed to communicate this before. I talked about this a little bit [on Stack Overflow podcast #5](http://blog.stackoverflow.com/2008/05/podcast-5/) with Joel, where I tried to amplify and explain my position a little better.


> I wasn’t trying to present it as “Oh, XML is bad, let’s all switch to this new markup language that all the cool guys are using.” What I was trying to say is **why don’t we think about what we’re doing?** That’s the general theme of a lot of the stuff in my blog. Can we just stop programming for a minute to think about what we’re doing and not make a blind choice based on “Well this is what my tool does, so that’s what I have to do”?
> I think obviously there’s pros and cons to each. I’m not saying that one is the right solution all the time. But I think, ironically, that *is* what is happening with XML. I think people are saying “It’s always the right answer, because it can store anything, right? And all the stuff I use uses it, so it must be the right choice for everything.” That bothers me a little. Maybe I’m just contrarian. Maybe I’m an iconoclast and I want to try different things and see different things, but I think **actually understanding the alternatives helps you understand XML better, a little bit, too.**
> And I hope people reading my blog would not get the idea that it’s about a knee-jerk reaction one way or the other. It’s about understanding the tradeoffs and applying those tradeoffs to your particular situation. I think that is the absolute art of programming. It’s understanding what you *could* do, and which one of those things fits your situation best. Versus what so many programmers do, which is “I’ve learned to use a hammer, and I’m gonna hammer everything.” Ultimately, to me, it’s about self-awareness.


By the way, I’d like to thank everyone who pitches in to make those Stack Overflow podcast transcriptions possible. It is because of your generously donated time that I am able to quote that audio here.


I don’t post stuff to push people’s buttons, I post it because I want programmers to **think** about their tools, their technologies, their methods.


![](https://blog.codinghorror.com/content/images/2025/04/image-156.png)


If what I post here seems unnecessarily confrontational sometimes, a far [smarter person than myself](http://www.skrenta.com/2007/08/crypto_vs_the_working_coder.html) said it better than I can:


> **I blog to help others and also to learn. As it turns out both are aided by getting folks to actually read the stuff. Please pardon the necessary devices.**


Please do pardon the necessary devices; I find that I often learn best through [the smackdown learning model](https://blog.codinghorror.com/in-defense-of-the-smackdown-learning-model/). That works for me. Maybe it doesn’t work for you, and that’s OK. There are millions of websites to choose from.


That said, I do actually **have a problem with XML**, or I wouldn’t have written anything in the first place. I think there’s a real issue here that is, for the most part, being completely ignored. [XML fever](http://dret.net/netdret/docs/wilde-cacm2008-xml-fever.html) may not be as debilitating as, say, [Dengue fever](http://en.wikipedia.org/wiki/Dengue), but it has side effects as well.


Consider [Norman Walsh’s Defending the Tax](http://norman.walsh.name/2008/05/13/thetax). Norman is an XML Standards Architect at Sun.

kg-card-begin: html

> On the other hand, the difference between:
> fruit=pear
> vegetable=carrot
> topping=wax
> and
> <doc>
> <fruit>pear</fruit>
> <vegetable>carrot</vegetable>
> <topping>wax</topping>
> </doc>
> isn’t really that large, is it? (Or maybe you think it is, *de gustibus non est disputandum*.)

kg-card-end: html

The *de gustibus* dismissal means Norman considers it is a matter of taste, but it isn’t. **The difference is large**. There is a very real mental cost to parsing even a few short lines of XML.


As a Visual Studio ecosystem programmer, XML is pervasive, in every nook and cranny of a project. Every time I look at my web.config XML file, there’s a mental cost of me having to parse all these tags in the file. Here’s this tag, which lines up with this tag. Here’s this giant, verbose thing where only half of it actually *matters*.


Sure, it’s a small effort. Insignificant, even. But what’s **the mental cost of that insignificant effort times the number of developers in the world, times the number of projects in the world?**


I also posit that these minor headaches may be more significant than you realize. In [Stumbling on Happiness](http://www.amazon.com/dp/1400077427), author Dan Gilbert makes a similar assertion.


![](https://blog.codinghorror.com/content/images/2025/04/image-155.png)


His research found that people are bad at predicting their own future happiness. They tend to radically overestimate the positive or negative impact of large events in their lives – losing your job, getting rich, getting divorced, having children. That’s generally good; it means we have defense mechanisms in place to adapt and survive in our changing circumstances as human beings. But, **we also tend to radically *underestimate* the impact of the dozens of small events in our lives throughout the day**. Thus, small injustices don’t trigger our defenses. The effect of that squeaky screen door, the neighbor’s barking dog, the interrupting telephone call – all of these may have far more profound cumulative impact on your day to day happiness than you realize.


It’s a fascinating book, and I’m only paraphrasing the smallest part of it. I highly recommend reading it if this is at all interesting to you. It won’t exactly unlock the secrets to happiness, I’m afraid, but you may gain a deeper understanding of why we tend to make the choices we do in our never ending pursuit of happiness.


I’m not trying to change the world overnight, but I wouldn’t mind planting a few seeds of dissent in people’s minds. **This small stuff *matters***.


The next time you’re trying to figure out an XML file, just think about it.


That’s all I’m saying.

[xml](https://blog.codinghorror.com/tag/xml/)
[markup language](https://blog.codinghorror.com/tag/markup-language/)
[xml angle bracket tax](https://blog.codinghorror.com/tag/xml-angle-bracket-tax/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
