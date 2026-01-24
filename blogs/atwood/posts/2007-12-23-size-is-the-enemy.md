---
title: "Size Is The Enemy"
date: 2007-12-23
url: https://blog.codinghorror.com/size-is-the-enemy/
slug: size-is-the-enemy
word_count: 1537
---

Steve Yegge’s latest, [Code’s Worst Enemy](http://steve-yegge.blogspot.com/2007/12/codes-worst-enemy.html), is like all of his posts: rich, rewarding, and *ridiculously freaking long*. Steve doesn’t write often, but when he does, it’s a doozy. As I [mentioned a year ago](https://blog.codinghorror.com/software-development-its-a-religion/), I’ve started a cottage industry mining Steve’s insanely great but I-hope-you-have-an-hour-to-kill writing and condensing it into its shorter form points. So let’s begin:

1. Steve began writing a multiplayer game in Java, [Wyvern](https://web.archive.org/web/20080509162719/http://www.cabochon.com/), around 1998. If you’re curious what it looks like, see fan screenshots [one](https://web.archive.org/web/20070826052828/http://img153.imageshack.us/img153/3919/winglesgroupwy29om.jpg) and two.
2. Over the last 9 years, Wyvern has grown to 500,000 lines of Java code.
3. Steve realized that it is impossible for a single programmer to singlehandedly maintain and support half a million lines of code. Even if you’re Steve Yegge.


There’s much more, but I want to pause here for a moment. **It is absolutely true that any programmer who personally maintains half a million lines of code is automatically in a pretty rarified club.** Steve’s right about this. Most developers will never have the superhuman privilege of personally maintaining 500k LOC or more. On any rational software development project, you’d have a team of developers working on it, or you’d open source the thing entirely to spread the effort across a community.


But here’s what I don’t understand:


> I happen to hold a hard-won minority opinion about code bases. In particular I believe, quite staunchly I might add, that the worst thing that can happen to a code base is size.


So Steve believes the *majority* of developers, when encountering a code base approximately the size of the [Death Star](http://en.wikipedia.org/wiki/Death_Star), would think:


***I could totally build that.***


It’s a telling indicator of the [impressively bearded computer scientist crowd](http://www.mikepope.com/blog/AddComment.aspx?blogid=1875) that Steve runs with. They probably wear flip-flops to work, too. Amongst the programmers I know, the far more common – and certainly more rational – reaction to a code base that large would be to run away, screaming, as fast as they could. And I’d be right behind them.


I don’t think you necessarily have to spend ten years writing 500k worth of fairly complicated Java code to independently reach the same conclusion. **Size is the enemy**. Simply going from 1k to 10k LOC – assuming you’re sufficiently self-aware as a programmer – is *more* than enough of a glimpse into the maw of madness that lies beyond. Even if you’ve written zero lines of code, if you’ve ever read any [Steve McConnell books](http://www.amazon.com/s/ref=nb_ss_gw/102-0292990-3586571?url=search-alias%3Daps&field-keywords=steve+mcconnell), the [size rule is pounded home](https://blog.codinghorror.com/diseconomies-of-scale-and-lines-of-code/), time and time again:


> Project size is easily the most significant determinant of effort, cost and schedule [for a software project]. People naturally assume that a system that is 10 times as large as another system will require something like 10 times as much effort to build. But the effort for a 1,000,000 LOC system is *more* than 10 times as large as the effort for a 100,000 LOC system.


One of the most fundamental and truly effective pieces of advice you can give a software development team – *any* software development team – is to **write less code, by any means necessary**. Break the project into smaller subprojects. Deliver it in complementary fragments. Try iterative development. Stop writing everything in assembly language and APL. Hire better programmers who naturally write less code. Buy code from a third party. Do absolutely whatever it takes to write as little code as possible, because [the best code is no code at all](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/).


We’re not done yet. I warned you that this was a long post. Continuing from above:

1. Because Java is a statically typed language, it requires lots of tedious, repetitive boilerplate code to get things done.
2. That tedious, repetitive boilerplate code has been codified into Java faith as the seminal books “Design Patterns” and “Refactoring.”
3. Java developers fervently believe, almost to a man/woman, that IDEs can overcome the unavoidable LOC bloat of Java.
4. A rewrite of Wyvern from Java into a dynamic language that runs on the JVM could reduce the raw code size by 50% to 75%.


Here’s where Steve not-so-gently segues from “size is the problem” to “Java is the problem.”

kg-card-begin: html

> Bigger is just something you have to live with in Java. Growth is a fact of life. **Java is like a variant of the game of Tetris in which none of the pieces can fill gaps created by the other pieces, so all you can do is pile them up endlessly.**
>         Going back to our crazed Tetris game, imagine that you have a tool that lets you manage huge Tetris screens that are hundreds of stories high. In this scenario, stacking the pieces isn’t a problem, so there’s no need to be able to eliminate pieces. This is the cultural problem: [Java programmers] don’t realize they’re not actually playing the right game anymore.

kg-card-end: html

Steve singles out [Martin Fowler](http://martinfowler.com/), who recently “abandoned” the static-language Java fold in favor of the dynamically typed Ruby. Fowler quite literally [wrote the book on refactoring](http://www.amazon.com/exec/obidos/ASIN/0201485672), so perhaps there’s some truth to Steve’s claim that the rigid architecture of classic, statically typed languages ultimately prevent you from refactoring the code down as far as you need to go. If Fowler can’t refactor the Java pieces to fit, who can?


Bruce Eckel is another notable Java personality who apparently reached many of [the same conclusions about Java](https://web.archive.org/web/20071227151300/http://www.mindview.net/WebLog/log-0053) years ago.

kg-card-begin: html

> I can’t quantify [the cost of strong typing]. I haven’t been able to come up with a from-first- principles mathematical proof, probably because it depends on human factors, like how much time it takes to remember how to open a file and put the try block in the right places and remember how to read lines and then remember what you were really trying to accomplish by reading that file. In Python, I can process each line in a file by saying:
> for line in file(“FileName.txt”):
> # Process line
> I didn’t have to look that up, or to even think about it, because it’s so natural. I *always* have to look up the way to open files and read lines in Java. I suppose you could argue that Java wasn’t intended to do text processing and I’d agree with you, but unfortunately it seems like Java is mostly used on servers where a very common task is to process text.

kg-card-end: html

Lines of code are, and always have been, the enemy. More lines of code means more to read, more to understand, more to troubleshoot, more to debug. But it *is* possible to go too far in the other direction as well. If you’re not careful, you could end up playing yet another game entirely – yes, you’ve cleverly avoided the trap of Java’s infinitely tall Tetris, but have you slipped into [Perl’s Golf](http://en.wikipedia.org/wiki/Perl#Perl_golf) instead?

kg-card-begin: html

> Perl “golf” is the pastime of reducing the number of characters used in a Perl program to the bare minimum, much as how golf players seek to take as few shots as possible in a round.
>         It originally focused on the JAPHs used in signatures in Usenet postings and elsewhere, but the use of Perl to write a program which performed RSA encryption prompted a widespread and practical interest in this pastime. In subsequent years, code golf has been taken up as a pastime in other languages besides Perl.

kg-card-end: html

In our war on verbosity, there’s an inevitable [tradeoff between verbosity and understandability](http://weblog.raganwald.com/2007/12/golf-is-good-program-spoiled.html). Steve acknowledges this by hinging his JVM language choice on what is “syntactically mainstream”: JRuby, Groovy, Rhino (JavaScript), and Jython. I’ll spoil the not-so-surprise ending for you: Steve is rewriting Wyvern in Rhino, and in the process he’ll help bring Rhino up to spec with the forthcoming EcmaScript Edition 4 update to JavaScript. It’s no magic bullet, but it seems like a reasonable compromise based on his goals.


So ends the epic ten year tale of Stevey and his merry band of Wyverneers. But where does that leave us? I have my opinions, naturally:

- If you personally write 500,000 lines of code in any language, you are so totally screwed.
- If you personally rewrite 500,000 lines of static language code into 190,000 lines of dynamic language code, you are still pretty screwed. And you’ll be out a year of your life, too.
- If you’re starting a new project, consider using a dynamic language like Ruby, JavaScript, or Python. You may find you can write less code that means more. A lot of incredibly smart people like Steve present a compelling case that the grass really *is* greener on the dynamic side. At the very least, you’ll learn how the other half lives, and maybe remove some blinders you didn’t even know you were wearing.
- If you’re stuck using exclusively static languages, ask yourself this: why *do* we have to write so much damn code to get anything done – and how can this be changed? [Simple things should be simple, complex things should be possible](http://en.wikiquote.org/wiki/Alan_Kay). It’s healthy to question authority, *particularly* language authorities.


Remember: **size really *is* the enemy**. Right after ourselves, of course.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[code maintenance](https://blog.codinghorror.com/tag/code-maintenance/)
[java](https://blog.codinghorror.com/tag/java/)
[scalability](https://blog.codinghorror.com/tag/scalability/)
