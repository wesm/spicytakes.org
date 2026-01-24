---
title: "I’d Consider That Harmful, Too"
date: 2007-10-25
url: https://blog.codinghorror.com/id-consider-that-harmful-too/
slug: id-consider-that-harmful-too
word_count: 945
---

One of the seminal papers in computer science is [Edsger Dijkstra’s](http://en.wikipedia.org/wiki/Edsger_Dijkstra) 1968 paper [GOTO Considered Harmful](https://web.archive.org/web/20100208024052/http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html).


> For a number of years I have been familiar with the observation that the quality of programmers is a decreasing function of the density of go to statements in the programs they produce. More recently I discovered why the use of the go to statement has such disastrous effects, and I became convinced that the go to statement should be abolished from all “higher level” programming languages (i.e. everything except, perhaps, plain machine code).


The abuse of GOTO is, thankfully, a long forgotten memory in today’s modern programming languages. Of course, it’s only a minor hazard compared to the [COMEFROM statement](http://en.wikipedia.org/wiki/COMEFROM), but I’m glad to have both of those largely behind us.


![So then I typed GOTO 500 -- and here I am!](https://blog.codinghorror.com/content/images/uploads/2007/10/6a0120a85dcdae970b012877702759970c-pi.png)


[GOTO isn’t all bad](http://stevemcconnell.com/ccgoto.htm), though. It still has some relevance to today’s code. Along with many other programmers, I always recommend using guard clauses to [avoid arrow code](https://blog.codinghorror.com/flattening-arrow-code/), and I also recommend exiting early from a loop as soon as you find the value you’re looking for. What is an early `Return`, or an early `Exit For` other than **a tightly scoped GOTO?**

kg-card-begin: html

```
foreach my $try (@options) {
next unless exists $hash{$try};
do_something($try);
goto SUCCESS;
}
log_failure();
SUCCESS: ...

```

kg-card-end: html

The publication of such an influential paper in this particular format led to an almost immediate [snowclone effect](http://en.wikipedia.org/wiki/Snowclone), as [documented on Wikipedia](http://en.wikipedia.org/wiki/Considered_harmful):


> Frank Rubin published a criticism of Dijkstra’s letter in the March 1987 CACM where it appeared as *‘GOTO Considered Harmful’ Considered Harmful*. The May 1987 CACM printed further replies, both for and against, as ‘*“GOTO Considered Harmful” Considered Harmful’ Considered Harmful?*. Dijkstra’s own response to this controversy was titled [“On a somewhat disappointing correspondence.”](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD10xx/EWD1009.html)


That’s easily one of the funniest things I’ve ever read in Wikipedia. Who says computer scientists don’t have a sense of humor? But I digress. Most software developers are probably familiar, at least in passing, with Dijkstra’s GOTO Considered Harmful. But here’s what they might *not* know about it:

1. The paper was originally titled “A Case Against the Goto Statement;” the editor of the CACM at the time, [Niklaus Wirth](http://en.wikipedia.org/wiki/Niklaus_Wirth), changed the title to the more inflammatory version we know today.
2. In order to speed up its publication, the paper was converted into a “Letter to the Editor.”


In other words, Wirth poked and prodded the content until it became incendiary, to maximize its impact. The phrase “considered harmful” was used quite intentionally, [as documented](http://itre.cis.upenn.edu/~myl/languagelog/archives/004675.html) on the always excellent Language Log:


> However, “X considered harmful” was already a well-established journalistic cliché in 1968 – which is why Wirth chose it. The illustration below shows the headline of a letter to the New York Times published August 12, 1949: “Rent Control Controversy / Enacting Now of Hasty Legislation Considered Harmful.”
> I’m sure it’s not the earliest example of this phrase used in a headline or title, either – I chose it only as a convenient illustration of susage a couple of decades before the date of Dijkstra’s paper.
> Note that this example is also in the title of a slightly cranky letter to the editor – it’s probably not an accident that the first example that came to hand of “considered harmful” in a pre-Dijkstra title was of this type.


![Rent Control Controversy / Enacting Now of Hasty Legislation Considered Harmful](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeGP5dkAN717LD_ugIyMT1lD-28hfRgknbk5PHnKWhBruOpPXM-lDQJ_lOv2DAf8Q1pvXv8WUzOTUTr2sym8eE1xeT58hXYUghZYu2YCkPwRq9LlaVlYlypjss0KMJfEcFnvivsow?key=EFBg8Ij0aJ1EmCyuDte1jBlv)


So when you emulate the “considered harmful” style predicated on the work of these famous computer scientists in 1968, keep that history in mind. **You’re emulating a slightly cranky letter to the editor**. It’s frighteningly common – there are now [28,800 web pages](http://www.google.com/search?&q=intitle%3A%22considered+harmful%22) with the exact phrase “considered harmful” in the title.


This leads, perhaps inevitably, to Eric Meyer’s [“Considered Harmful” Essays Considered Harmful](http://meyerweb.com/eric/comment/chech.html). He points out that choosing this style of dialogue is ultimately counterproductive:

kg-card-begin: html

> There are three primary ways in which “Considered Harmful” essays cause harm.
> The writing of a “considered harmful” essay often serves to inflame whatever debate is in progress, and thus makes it that much harder for a solution to be found through any means. Those who support the view that the essay attacks are more likely to dig in and defend their views by any means necessary, and are less receptive to reasoned debate. By pushing the opposing views further apart, it becomes more likely that the essay will cause a permanent break between opposing views rather than contribute to a resolution of the debate.
> “Considered harmful” essays are most harmful to their own causes. The publication of a “considered harmful” essay has a strong tendency to alienate neutral parties, thus weakening support for the point of view the essay puts forth. A sufficiently dogmatic “considered harmful” essay can end a debate in favor of the viewpoint the essay considers harmful.
> They’ve become boring cliches. Nobody really wants to read “considered harmful” essays any more, because we’ve seen them a thousand times before and didn’t really learn anything from them, since we were too busy being annoyed to really listen to the arguments presented.

kg-card-end: html

If you have a point to make, by all means, [write a great persuasive essay](https://blog.codinghorror.com/whatever-happened-to-civility-on-the-internet/). If you want to maximize the effectiveness of your criticisms, however, you’ll leave “considered harmful” out of your writing. The “considered harmful” technique may have worked for Wirth and Dijkstra, but unless you’re planning to become a world famous computer scientist like those guys, I’d suggest leaving it back in 1968 where it belongs.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[goto statement](https://blog.codinghorror.com/tag/goto-statement/)
[code quality](https://blog.codinghorror.com/tag/code-quality/)
