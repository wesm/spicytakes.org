---
title: "Distributed Version Control is here to stay, baby"
date: 2010-03-17
url: https://www.joelonsoftware.com/2010/03/17/distributed-version-control-is-here-to-stay-baby/
word_count: 1176
---


A while ago Jeff and I had [Eric Sink on the Stack Overflow Podcast](http://blog.stackoverflow.com/2009/01/podcast-36/), and we were yammering on about version control, especially the trendy new distributed version control systems, like [Mercurial](http://mercurial.selenic.com/) and [Git](http://git-scm.com/).


In that podcast, I said, “To me, the fact that they make branching and merging easier just means that your coworkers are more likely to branch and merge, and you’re more likely to be confused.”


This is what Taco looks like nowWell, you know, that podcast is not prepared carefully in advance; it’s just a couple of people shooting the breeze. So what usually happens is that we say things that are, to use the technical term, *wrong*. Usually they are wrong either in details or in spirit, or in details *and* in spirit, but this time, I was just plain *wrong*. Like strawberry pizza. Or jalapeño bagels. *WRONG*.


Long before this podcast occurred, my team had switched to Mercurial, and the switch *really* confused me, so I hired someone to check in code for me (just kidding). I did struggle along for a while by memorizing a few key commands, imagining that they were working just like Subversion, but when something didn’t go the way it would have with Subversion, I got confused, and would pretty much just have to run down the hall to get Benjamin or Jacob to help.


And then my team said, hey you know what? This Mercurial bug-juice is really amazing, we want to actually make a code review product that works with it, and, and, what’s more, we think that there’s a big market providing commercial support and hosting for it (Mercurial itself is freely available under GPL, but a lot of corporations want some kind of support before they’ll use something).


And I thought, what do I know? But as you know I don’t really make the decisions around here, because “management is a support function,” so they took *all* the interns, all *six* of them, and set off to build a [product](http://www.fogcreek.com/kiln/) around Mercurial.


I decided I better figure out what the heck is going on with this “distributed version control” stuff before somebody asks me a question about the products that my company allegedly sells, and I don’t have an answer, and somebody in the blogo-“sphere” writes another article about me junking the sharp.


And I studied, and studied, and finally figured something out. Which I want to share with you.


With distributed version control, the *distributed* part is actually not the most interesting part.


The interesting part is that these systems think in terms of *changes*, not in terms of *versions*.


That’s a very zen-like thing to say, I know. Traditional version control thinks: OK, I have version 1. And now I have version 2. And now I have version 3.


And distributed version control thinks, I had nothing. And then I got these changes. And then I got these other changes.


It’s a different [Program Model](https://www.joelonsoftware.com/uibook/chapters/fog0000000058.html), so the user model has to change.


In Subversion, you might think, “bring my version up to date with the main version” or “go back to the previous version.”


In Mercurial, you think, “get me Jacob’s change set” or “let’s just forget that change set.”


If you come at Mercurial with a Subversion mindset, things will *almost* work, but when they don’t, you’ll be confused, unhappy, and unsuccessful, and you’ll hate Mercurial.


Whereas if you free your mind and reimagine version control, and grok the zen of the difference between thinking about managing the *versions *vs. thinking about managing the *changes*, you’ll become enlightened and happy and realize that this is the way version control was meant to work.


I know, it’s strange… since [1972](http://en.wikipedia.org/wiki/Source_Code_Control_System) everyone was thinking that we were manipulating versions, but, it turned out, surprisingly, that thinking about the *changes themselves *as first class solved a very important problem: the problem of merging branched code.


And here is the most important point, indeed, *the* most important thing that we’ve learned about developer productivity in a decade. It’s so important that it merits a place as the very last opinion piece that I write, so if you only remember one thing, remember this:


When you manage *changes* instead of managing *versions*, merging works better, and therefore, you can branch any time your organizational goals require it, because merging back will be a piece of cake.


I can’t tell you how many Subversion users have told me the following story: “We tried to branch our code, and that worked fine. But when it came time to merge *back*, it was a complete nightmare and we had to practically reapply every change by hand, and we swore *never again* and we developed a new way of developing software using **if** statements instead of branches.”


Sometimes they’re even kind of proud of this new, single-trunk invention of theirs. As if it’s a virtue to work around the fact that your version control tool is not doing what it’s meant to do.


With distributed version control, *merges are easy* and work *fine*. So you can actually have a stable branch and a development branch, or create long-lived branches for your QA team where they test things before deployment, or you can create short-lived branches to try out new ideas and see how they work.


This is too important to miss out on. This is possibly the biggest advance in software development technology in the ten years I’ve been writing articles here.


Or, to put it another way, I’d go back to C++ before I gave up on Mercurial.


If you are using Subversion, stop it. Just stop. Subversion = Leeches. Mercurial and Git = Antibiotics. *We have better technology now.*


Because so many people dive into Mercurial without fully understanding the new program model, which can leave them thinking that it’s broken and malicious, I wrote a Mercurial tutorial, [HgInit](http://hginit.com/).


Today, when people ask me about that podcast where I dissed DVCS, I tell them that it was just a very carefully planned fake-out of my long time friend and competitor Eric Sink, who makes a *non*-distributed version control system. Like that time he started selling bug-tracking software, and, to punish him, we sent him a very expensive Fog Creek backpack with a fake form letter that made it look like we were doing so well that expensive backpacks were the standard Christmas gift we were sending *every* FogBugz customer.


I seem to have run out the clock on this site. It has been an extreme honor to have you reading my essays over the last ten years. I couldn’t ask for a greater group of readers. Whether you’re one of the hundreds of people who volunteered their time to translate articles into over 40 languages, or the 22,894 people who has taken the time to send me an email, or the 50,838 people who subscribed to the email newsletter, or the 2,262,348 people per year who visited the website and read some of the 1067 articles I’ve written, I sincerely thank you for your attention.
