---
title: "Rub a dub dub"
date: 2002-01-23
url: https://www.joelonsoftware.com/2002/01/23/rub-a-dub-dub/
word_count: 1674
---


One reason people are tempted to rewrite their entire code base from scratch is that the original code base wasn’t designed for what it’s doing. It was designed as a prototype, an experiment, a learning exercise, a way to go from zero to IPO in nine months, or a one-off demo. And now it has grown into a big mess that’s fragile and impossible to add code to, and everybody’s whiny, and the old programmers quit in despair and the new ones that are brought in can’t make head or tail of the code so they somehow convince management to give up and start over while Microsoft takes over their business. Today let me tell you a story about what they could have done instead.


[FogBUGZ](http://www.fogcreek.com/FogBUGZ) started out six years ago as an experiment to teach myself ASP programming. Pretty soon it became an in-house bug tracking system. It got embellished almost daily with features that people needed until it was *good enough *that it no longer justified any more work.


Various friends asked me if they could use FogBUGZ at *their* companies. The trouble was, it had too many hardcoded things that made it a pain to run anywhere other than on the original computer where it was deployed. I had used a bunch of SQL Server stored procedures, which meant that you needed SQL Server to run FogBUGZ, which was expensive and overkill for some of the two person teams that wanted to run it. And so on. So I would tell my friends, “gosh, for $5000 in consulting fees, I’ll spend a couple of days and clean up the code so you can run it on your server using Access instead of SQL Server.” Generally, my friends thought this was too expensive.


After this happened a few times I had a revelation — if I could sell the same program to, say, three people, I could charge $2000 and come out *ahead*. Or thirty people for $200. Software is neat like that. So in late 2000, Michael sat down, ported the code so that it worked on Access or SQL Server, pulled all the site-specific stuff out into a header file, and we started selling the thing. I didn’t really expect much to come of it.


In those days, I thought, golly, there are zillions of bug tracking packages out there. Every programmer has written a dinky bug tracking package. Why would anyone buy ours? I knew one thing: programmers who start businesses often have the bad habit of thinking everybody *else* is a programmer *just like them *and wants the same stuff as them, and so they have an unhealthy tendency to start businesses that sell programming tools. That’s why you see so many scrawny companies hawking source-code-generating geegaws, error catching and emailing geegaws, debugging geegaws, syntax-coloring editing tchotchkes, ftping baubles, and, ahem, bug tracking packages. All kinds of stuff that only a programmer could love. I had no intention of falling into *that* trap!


Of course, nothing ever works out exactly as planned. FogBUGZ was popular. Really popular. It accounts for a significant chunk of Fog Creek’s revenue and sales are growing steadily. The People won’t stop buying it.


So we did version 2.0. This was an attempt to add some of the most obviously needed features. While David worked on version 2.0 we honestly didn’t think it was worth that much effort, so he tended to do things in what you might call an “expedient” fashion rather than, say, an “elegant” fashion. Certain, ahem, *design issues* in the original code were allowed to fester. There were two complete sets of nearly *identical *code for drawing the main bug-editing page. SQL statements were scattered throughout the HTML hither and yon, to and fro, pho and ton. Our HTML was creaky and designed for those ancient browsers that were so buggy they could crash loading about:blank.


Yeah, it worked brilliantly, we’ve been at zero known bugs for a while now. But inside, the code was, to use the technical term, a “big mess.” Adding new features was a hemorrhoid. To add one field to the central bug table would probably require 50 modifications, and you’d still be finding places you forgot to modify long after you bought your first family carplane for those weekend trips to your beach house on Mars.


A lesser company, perhaps one run by an executive from the express-package-delivery business, might have decided to [scrap the code](https://www.joelonsoftware.com/articles/fog0000000069.html) and start over.


Did I mention that I don’t believe in starting from scratch? I guess I talk about that a lot.


Anyway, instead of starting from scratch, I decided it was worth three weeks of my life to completely scrub the code. Rub a dub dub. In the spirit of [refactoring](http://www.amazon.com/exec/obidos/ASIN/0201485672/ref=nosim/joelonsoftware), I set out a few rules for this exercise.

1. No New Features, not even small ones, would be added.
At any time, with any check in, the code would still work perfectly.
All I would do is [logical transformations](http://www.refactoring.com/catalog/index.html) — the kinds of things that are almost mechanical and which you can convince yourself immediately will not change the behavior of the code.


I went through each source file, one at a time, top to bottom, looking at code, thinking about how it could be better structured, and making simple changes. Here are some of the kinds of things I did during these three weeks:

- Changed all HTML to xhtml. For example, <BR> became <br />, all attributes were quoted, all nested tags were matched up, and all pages were [validated](http://www.htmlhelp.com/tools/validator/).
Removed all formatting (<FONT> tags etc.) and put everything in a CSS style sheet.
Removed all SQL statements from the presentation code and indeed all program logic (what the marketing types like to call “business rules”). This stuff went into classes which were not really designed — I simply added methods lazily as I discovered a need for them. (Somewhere, someone with a big stack of 4×6 cards is sharpening their pencil to poke my eyes out. What do you mean you didn’t design your classes?)
Found repeated blocks of code and created classes, functions, or methods to eliminate the repetition. Broke up large functions into multiple smaller ones.
Removed all remaining English language text from the main code and isolated that in a single file for easy internationalization.
Restructured the ASP site so there is a single entry point instead of lots of different files. This makes it very easy to do things that used to be hard, for example, now we can display input error messages in the very form where the invalid input occurred, something which *should* be easy if you lay things out right, but I hadn’t laid things out right when I was learning ASP programming way back when.


Over three weeks the code got better and better internally. To the end user, not too much changed. Some fonts are a little nicer thanks to CSS. I could have stopped at any point, because at any given time I had 100% working code (and I uploaded every checkin to our live internal FogBUGZ server to make sure). And in fact I never really had to think very hard, and I never had to design a thing, because all I was doing was simple, logical transformations. Occassionally I would encounter a weird nugget in the code. These nuggets were usually bug fixes that had been implemented over the years. Luckily I could keep the bug fix intact. In many of these cases, I realized that had I started from scratch, I would have made the same bug all over again, and may not have noticed it for months or years.


I’m basically done now. It took, as planned, three weeks. *Almost every line of code is different now*. Yep, I looked at every line of code, and changed *most* of them. The structure is completely different. All the bug-tracking functionality is completely separate from the HTML UI functionality.


Here are all the good things about my code scrubbing activity:

- It took vastly less time than a complete rewrite. Let’s assume (based on how long it took us to get this far with FogBUGZ) that a complete rewrite would have taken a year. Well, that means I saved 49 weeks of work. Those 49 weeks represent knowledge in the *design* of the code that I preserved intact. I never had to think, “oh, I need a new line here.” I just had to change <BR> to <br /> mindlessly and move on. I didn’t have to figure out how to get multipart working for file uploads. It works. Just tidy it up a bit.
I didn’t introduce any new bugs. A couple of tiny ones, of course, probably got through. But I was never doing the types of things that cause bugs.
I could have stopped and shipped at any time if necessary.
The schedule was entirely predictable. After a week of this, you can calculate exactly how many lines of code you clean in an hour, and get a darn good estimate for the rest of the project. Try that, Mozilla river-drawing people.
The code is now much more amenable to new features. We’ll probably earn back the three weeks with the first new major feature we implement.


Much of the literature on refactoring is attributable to [Martin Fowler](http://www.martinfowler.com/), although of course the principles of code cleanups have been well known to programmers for years. An interesting new area is refactoring tools, which is just a fancy word for programs that do some of this stuff automatically. We’re a long way from having all the good tools we need — in most programming environments you can’t even do a simple transformation like changing the name of a variable (and having all the references to it change automatically). But [it’s getting better](http://www.refactoring.com/#tools), and if you want to start one of those scrawny companies hawking programming tool geegaws, or make a useful contribution to open source, the field is wide open.
