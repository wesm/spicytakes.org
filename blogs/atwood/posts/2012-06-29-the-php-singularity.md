---
title: "The PHP Singularity"
date: 2012-06-29
url: https://blog.codinghorror.com/the-php-singularity/
slug: the-php-singularity
word_count: 1294
---

Look at this incredible thing Ian Baker created. *Look at it!*


![](https://blog.codinghorror.com/content/images/2025/04/image-653.png)


What you’re seeing is not Photoshopped. This is an actual photo of a real world, honest to God *double-clawed hammer*. Such a thing exists. Isn’t that amazing? And also, perhaps, a little disturbing?


That wondrous hammer is a delightful real-world acknowledgement of the epic blog entry [PHP: A Fractal of Bad Design](https://web.archive.org/web/20120711143431/http://me.veekun.com/blog/2012/04/09/php-a-fractal-of-bad-design/).


> I can’t even say what’s wrong with [PHP](http://en.wikipedia.org/wiki/PHP), because – okay. Imagine you have uh, a toolbox. A set of tools. Looks okay, standard stuff in there.
> You pull out a screwdriver, and you see it’s one of those weird tri-headed things. Okay, well, that’s not very useful to you, but you guess it comes in handy sometimes.
> **You pull out the hammer, but to your dismay, it has the claw part on both sides.** Still serviceable though, I mean, you can hit nails with the middle of the head holding it sideways.
> You pull out the pliers, but they don’t have those serrated surfaces; it’s flat and smooth. That’s less useful, but it still turns bolts well enough, so whatever.
> And on you go. Everything in the box is kind of weird and quirky, but maybe not enough to make it completely worthless. And there’s no clear problem with the set as a whole; it still has all the tools.
> Now imagine you meet millions of carpenters using this toolbox who tell you “well hey what’s the problem with these tools? They’re all I’ve ever used and they work fine!” And the carpenters show you the houses they’ve built, where every room is a pentagon and the roof is upside-down. And you knock on the front door and it just collapses inwards and they all yell at you for breaking their door.
> That’s what’s wrong with PHP.


Remember the immediate visceral reaction you had to the double-clawed hammer? That’s exactly the reaction most sane programmers have to their first encounter with the web programming language PHP.


This has been going on for *years*. I published my contribution to the genre in 2008 with [PHP Sucks, But It Doesn’t Matter](https://blog.codinghorror.com/php-sucks-but-it-doesnt-matter/).


> I’m no language elitist, but **language design is hard**. There’s a reason that some of the most famous computer scientists in the world are also language designers. And it’s a crying shame none of them ever had the opportunity to work on PHP. From what I’ve seen of it, **PHP isn’t so much a *language* as a random collection of arbitrary stuff, a virtual explosion at the keyword and function factory.** Bear in mind this is coming from a guy who was [weaned on BASIC](https://blog.codinghorror.com/everything-i-needed-to-know-about-programming-i-learned-from-basic/), a language that gets about as much respect as [Rodney Dangerfield](http://en.wikipedia.org/wiki/Rodney_Dangerfield). So I am not unfamiliar with the genre.


Except now it’s 2012, and fellow programmers are *still* writing long screeds bemoaning the awfulness of PHP!


What’s depressing is not that PHP is horribly designed. Does anyone even dispute that PHP is the worst designed mainstream “language” to blight our craft in decades? What’s truly depressing is that **so little has changed**. Just one year ago, legendary hacker Jamie Zawinski had [this to say](http://www.jwz.org/blog/2011/05/computational-feces/) about PHP:


> I used to think that PHP was the biggest, stinkiest dump that the computer industry had taken on my life in a decade. Then I started needing to do things that could only be accomplished in AppleScript.


Is PHP so broken as to be unworkable? No. Clearly not. The great crime of PHP is its utter banality. Its continued popularity is living proof that quality is irrelevant; cheap and popular and *everywhere* always wins. PHP is the Nickelback of programming languages. And, yes, out of frustration with the status quo I may have recently referred to Rasmus Lerdorf, the father of PHP, as history’s greatest monster. I’ve told myself a *million times* to stop exaggerating.


The hammer metaphor is apt, because at its core, this is about proper tooling. As [presciently noted by Alex Papadimoulis](http://weblogs.asp.net/alex_papadimoulis/archive/2005/05/25/408925.aspx):

kg-card-begin: html

> *A client has asked me to build and install a custom shelving system. I’m at the point where I need to nail it, but I’m not sure what to use to pound the nails in. Should I use an old shoe or a glass bottle?*
> How would you answer the question?
> It depends. If you are looking to pound a small (20lb) nail in something like drywall, you’ll find it much easier to use the bottle, especially if the shoe is dirty. However, if you are trying to drive a heavy nail into some wood, go with the shoe: the bottle will shatter in your hand.
> There is something fundamentally wrong with the way you are building; you need to use real tools. Yes, it may involve a trip to the toolbox (or even to the hardware store), but doing it the right way is going to save a lot of time, money, and aggravation through the lifecycle of your product. You need to stop building things for money until you understand the basics of construction.

kg-card-end: html

What we ought to be talking about is not how terrible PHP is – although its *continued *terribleness is a particularly damning indictment – but how we programmers can culturally displace a deeply flawed tool with a better one. **How do we encourage new programmers to avoid picking up the double clawed hammer in favor of, well, a regular hammer?**


This is not an abstract, academic concern to me. I’m starting a new open source web project with the goal of making the code as freely and easily runnable to the world as possible. Despite the serious problems with PHP, **I was forced to consider it**. If you want to produce [free-as-in-whatever](https://blog.codinghorror.com/open-source-free-as-in-free/) code that runs on virtually every server in the world with zero friction or configuration hassles, PHP is damn near your only option. If that doesn’t scare you, then check your pulse, because you might be dead.


![](https://blog.codinghorror.com/content/images/2025/04/image-652.png)


Therefore, I’d like to submit a humble suggestion to my fellow programmers. The next time you feel the urge to write Yet Another Epic Critique of PHP, consider that:

1. We get it already. PHP is horrible, but it’s used everywhere. Guess what? It was just as horrible in 2008. And 2005. And 2002. There’s a pattern here, but it’s subtle. You have to look very closely to see it. On second thought, never mind. You’re probably not smart enough to figure it out.
2. The best way to combat something as pervasively and institutionally awful as PHP is not to point out all its (many, many, *many*) faults, but to **build compelling alternatives** and **make sure these alternatives are equally pervasive, as easy to set up and use as possible**.


We’ve got a long way to go. One of the *explicit* goals of my next project is to do whatever we can to buff up a… particular… open source language ecosystem such that it can truly compete with PHP in ease of installation and deployment.


From my perspective, the point of all these “PHP is broken” rants is not just to complain, but to help educate and potentially warn off *new* coders starting *new* codebases. Some fine, even historic work has been done in PHP despite the madness, unquestionably. But now we need to work together to *fix* what is broken. The best way to fix the PHP problem at this point is to **make the alternatives so outstanding that the choice of the better hammer becomes *obvious*.**


That’s the PHP Singularity I’m hoping for. I’m trying like hell to do my part to make it happen. How about you?

[php](https://blog.codinghorror.com/tag/php/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
