---
title: "Three ways to solve hard programming problems"
date: 2016-05-29
url: https://jvns.ca/blog/2016/05/29/three-ways-to-solve-hard-programming-problems/
slug: three-ways-to-solve-hard-programming-problems
word_count: 741
---


I thought of this framing yesterday on a boat and it felt kind of helpful to me. This is a pretty small idea so I’ll keep this short :)


So, you have a programming problem to solve that seems hard, and you have no software that does it right now. three ways to fix that:


### Realize that there is awesome existing software that you can repurpose


This is relatively easy and extremely fun.


A super simple example of something like this is – once I was doing a computer science competition, and we needed to create a diet plan that satisfied some nutritional requirements while costing as little as possible.


I realized that you could do this with [integer linear programming software](https://en.wikipedia.org/wiki/Integer_programming) because I was taking a class on the topic at the time, spent an hour formulating the problem as an integer linear program, and BAM. We totally won that part of competition. The tool we used was a commercial tool that my university had a license for that had probably been worked on by hundreds of people for years. My friend [Anton](https://twitter.com/ant6n) uses integer programming to solve problems a lot and it’s really cool.


The same kind of thing is true with dtrace on OS X/BSD/Solaris – that’s another tool that’s had a ton of effort put into it and if you learn the dtrace language, you can suddenly do things using it by writing small programs that were impossible before.


I sorta think of this blog as an extended fanzine for existing software mostly for this reason – to say “hey someone spend a bajillion hours developing this thing and it is amazing and maybe you could use it did you know about it???!”. Some fraction of the interesting posts on Hacker News or whatever are like this – they say “HEY DID YOU KNOW THAT SOMEONE WROTE EXTREMELY POWERFUL SOFTWARE???? I wrote a cool small wrapper to make that software do a new thing!”


### Steal an idea


So, sometimes you want to do a thing, and it seems hard, and there is no software you can really repurpose in a good way.


I think solving this problem is the whole goal of the [Papers We Love](http://paperswelove.org/) meetup, which is about making ideas in academic research more available to working programmers. Avi Bryant, being someone who likes to read papers and use the ideas in them in software, has a talk I like about this idea called [Bad hackers copy, great hackers steal](https://vimeo.com/4763707).


At work, an example of this I’ve seen is probabilistic data structures like bloom filters and hyperloglogs – it’s very possible that the language you’re using has no good library support for probabilistic data structures, but if they’re not available it’s not really that much work to go ahead and implement them yourself. Sometimes big ideas don’t take that much code to go implement!


Security research also seems like this – people constantly explain new exploit techniques at security conferences, but I get the impression that if you want to use it to find vulnerabilities then you need to write most of the code yourself.


### Come up with a new idea


This is basically what academic research is! ❤ academics ❤. They’re like “we do not have enough great ideas yet! TIME TO GENERATE MORE IDEAS”.


### ❤❤❤ when research labs publish software


I think people get so excited when research labs publish projects like [vowpal wabbit](https://github.com/JohnLangford/vowpal_wabbit) because they do ‘come up with a new idea’ and ‘implement the idea in a way that can be used by other people’ in one fell swoop, making it super easy to repurpose that software for your awesome ends.


The advantage of this would seem to be that you don’t need to wait for someone to pick up the paper at a Papers We Love meetup and say OH WOW I LOVE THIS SO MUCH I AM GOING TO SPEND A MONTH BUILDING THIS NOW. The people who think of the idea and the people who implement it can be in the same office which is more efficient.


The disadvantage is maybe that the research lab needs to hire people who are good at research and also people who can write software suitable for other people to use, which are actually different skills. So I guess you need a bigger budget. When people like Microsoft Research do this it seems to be really awesome though!
