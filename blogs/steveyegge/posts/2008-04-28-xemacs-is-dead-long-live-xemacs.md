---
title: "XEmacs is Dead.  Long Live XEmacs!"
date: 2008-04-28
url: https://steve-yegge.blogspot.com/2008/04/xemacs-is-dead-long-live-xemacs.html
word_count: 5095
---



|  | "We're going to get lynched, aren't we?" — *Phouchg* |


And you thought I'd given up on controversial blogs.  Hah!
**Preamble**
This must be said:  Jamie Zawinski is a hero.  A living legend.  A major powerhouse programmer who, among his many other accomplishments, wrote the original Netscape Navigator and the original
[XEmacs](http://en.wikipedia.org/wiki/XEmacs)
. A guy who can use the term "
[downward funargs](http://www.jwz.org/doc/java.html)
" and then glare at you just daring you to ask him to explain it, you cretin.  A dude with arguably the best
[cat-picture blog](http://jwz.livejournal.com/)
ever created.
I've never met him, but I've been in awe of his work since 1993-ish, a time when I was still wearing programming diapers and needing them changed about every 3 hours.
Let's see... that would be 15 years ago.  I've been slaving away to become a better programmer for fifteen years, and I'm still not as good — nowhere
*near*
as good, mind you — as he was then.  I still marvel at his work, and his shocking writing style, when I'm grubbing around in the guts of the Emacs-Lisp byte-compiler.
It makes you wonder how many of him there are out there.  You know, programmers at that level.  He can't be the only one.  What do you suppose they're all working on?  Or do they all eventually make 25th level and opt for
[divine ascension](http://www.dnalounge.com/)
?
In any case, I'm sad that I have to write the obit on one of his greater achievements.  Sorry, man.  Keep up the cat blog.
**Forking XEmacs**
I have to include a teeny history lesson.  Bear with me.  It's short.
[XEmacs](http://www.xemacs.org)
was a fork of the GNU Emacs codebase, created about 17 years ago by a famous-ish startup called
[Lucid Inc.](http://en.wikipedia.org/wiki/Lucid_Inc.)
, which, alas, went Tango Uniform circa 1994.  As far as I know, their two big software legacies still extant are a Lisp environment now sold by
[LispWorks](http://www.lispworks.com/products/lispworks.html)
, and XEmacs.
I'd also count among their legacies an absolutely outstanding collection of software essays called
, by Lucid's founder,
[Richard P. Gabriel](http://en.wikipedia.org/wiki/Richard_p_gabriel)
.  I go back and re-read them every year or so.  They're that good.
Back when XEmacs was forked, there were some fireworks.  Nothing we haven't seen many times before or since.  Software as usual.  But there was a Great Schism.  Nowadays it's more like competing football teams.  Tempers have cooled.  At least, I think they have.
As for the whole sordid history of the FSF-Emacs/XEmacs schism, you can read about it online.  I'm sure it was a difficult decision to make.  There are pros and cons to forking a huge open-source project.  But I think it was the right decision at the time, just as decomissioning it is the right decision today, seventeen years later.
XEmacs dragged Emacs kicking and screaming into the modern era.  Among many other things, XEmacs introduced GUI widgets, inline images, colors in terminal sessions, variable-size fonts, and internationalization.  It also brought a host of technical innovations under the hood.  And XEmacs has always shipped with a great many more packages than GNU Emacs, making it more of a turnkey solution for new users.
XEmacs was clearly an important force helping to motivate the evolution of GNU Emacs during the mid- to late-1990s.  GNU Emacs was always playing catch-up, and the dev team led by
[RMS](http://en.wikipedia.org/wiki/Richard_stallman)
(an even more legendary hacker-hero) complained that XEmacs wasn't really playing on a level field.  The observation was correct, since XEmacs was using a
[Bazaar](http://catb.org/~esr/writings/cathedral-bazaar/)
-style development model, and could move faster as a direct consequence.
A lot of people were switching over to XEmacs by the mid-1990s:  the fancy widgets and pretty colors attracted GNU Emacs users like moths to a bug-zapper.
Problem was, it could actually zap you.
**The downside of the Bazaar**
I personally tried to use XEmacs many times over a period of many years.  I was jealous of its features.
However, I never managed to use XEmacs for very long, because it crashed a lot.  I tried it on every platform I used between ~1996 and 2001, including HP/UX, SunOS, Solaris, Ultrix, Linux, Windows NT and Windows XP.  XEmacs would never run for more than about a day under moderate use without crashing.
I've argued previously that one of the most important survival traits of a software system is that it
[should never reboot](http://steve-yegge.blogspot.com/2007/01/pinocchio-problem.html)
.  Emacs and XEmacs are at the leading edge of living software systems, but XEmacs has never been able to take advantage of this property because even though it can live virtually forever, it's always tripping and falling down manholes.
Clumsy XEmacs.  Clumsy!
I assume its propensity for inopportune heart attacks is a function of several things, including (a) old-school development without unit tests, (b) the need to port it to a gazillion platforms, including many that nobody actually uses, (c) a culture of rapid addition of new features.  There are probably other factors as well.
I'm just speculating though.  All I know is that it's always been very, very crashy.  It doesn't actually matter what the reasons are, since there's no excuse for it.
Interestingly, most XEmacs users I've talked to say they don't notice the crashing.  I'm sure this is because it's all relative.  XEmacs doesn't crash any more often than Firefox, for instance.  Probably less often.  When Firefox crashes I make a joke about it and restart it, because the crashing rarely has an impact.  It even restores your state properly most of the time, so it's just a minor blip, an almost trivial inconvenience, so long as whatever text field you happen to be editing has an auto-save feature.  And most of the good ones do.
XEmacs may crash even less than Eclipse and IntelliJ.  Crashing editors usually aren't a big problem.  Programmers all learn the hard way to save their buffers frequently.  For me, saving is like punctuation; I save whenever my typing pauses, out of reflex.  Doesn't matter whether it's Emacs or NeoOffice or GMail or... do I use any other apps?  Oh yeah, or the Gimp.  When I pause, I save, and if you're a programmer I bet you do too.  So occasional crashes may seem OK.
Another reason the crashes aren't called out more often is that most Emacs and XEmacs users are at best casual users.  They open up an {X}Emacs session whenever they need to edit a file, and close it when they're done.  It's just Notepad with colors and multi-level Undo.
If your average session length is shorter than the editor's MTBF, then yeah, you're not going to notice much crashing.
In contrast, your more... ah,
*seasoned*
(read: fanatical) Emacs users gradually come to live in it.  Anything you can't do from within Emacs is an annoyance.  It's like having to drive to a government building downtown to take care of some random paperwork they should have been offering as an online service a decade ago.  You can live with it, but you're annoyed.
Even Firefox, the other big place I live, really wants to be Emacs.  Tabs don't scale.  Tabbed browsing was revolutionary in the same way adding more tellers to a bank was revolutionary: it's, like, 4x better.  w00t.  Emacs offers the unique ability to manage its open buffers in another first-class buffer, as a
*list*
.  Imagine what your filesystem life would be like if the only view of a directory was one tab per file.  Go to your pictures directory and watch it start vomiting tabs out like it tried to swallow a box of chiclets.  Fun!
I feel sad when I see Eclipse users with fifty open tabs, an army of helpful termites eating away at their screen real-estate and their time.
I have a feeling I've veered off course somewhere... where was I?  Oh yeah.  Crashing.
So XEmacs has never been a particularly good tool for serious Emacs users because even though it's written in C, it crashes like a mature C++ application.  You know the drill:  major faceplants, all the fugging time.
Your ability to become an inhabitant of Emacs is gated by how stable it is.  GNU Emacs has always been famously stable.  Sure, the releases happen less frequently than presidential inaugurations.  Sure, for a long time it always lacked some XEmacs feature or other.  But it's really, really stable.  Its MTBF is measurable in weeks (or even months, depending on what you're doing with it) as opposed to hours or days.
Emacs, like Firefox, can be configured to back up your state periodically, so that in theory it can recover after a crash.  That's part of the problem: you didn't actually have to configure Firefox to get that behavior.  It does it automatically.  And to be honest, I've never had much luck with the Emacs save-state facilities.  I'm a pretty competent elisp hacker these days, but the
has never worked reliably for me.  I could probably get it to work, but I've always found it easier to write specialized startup "scripts" (lisp functions) that load up particular favorite configurations.
If I can't get desktop-save working, I'd guess that fewer than 1/10th of 1 percent of Emacs users use that feature.  So crashes blow everything away.
If the state isn't being auto-saved, the next best thing is for it not to crash.
XEmacs never got that right.
**Don't get me wrong...**
I just realized I'm going to get screamed at by people who think I'm just an XEmacs-hater slash GNU-fanboy.
Make no mistake: I'm a fan of XEmacs.  I think it was a great (or at least, necessary) idea in 1991.  I think the execution, aside from the stability issue, was top-notch.  I think it had a good architecture, by and large, at least within the rather severe constraints imposed by Emacs Lisp.  I think it spurred competition in a healthy way.
I think the XEmacs development team, over the years, has consisted of engineers who are ALL better than I am, with no exceptions.  And I even like certain aspects of the interface better, even today now that GNU Emacs has caught and surpassed XEmacs in features.  For instance, I like the XEmacs "apropos" system better.
If you're going to scream at me for irrational reasons, it really ought to be for the
*right*
irrational reasons.  Legitimate dumb reasons for screaming at me include: you're lazy and don't want to learn anything new; you invested a lot of time in XEmacs and don't see why you should be forced to switch; you are a very slow reader, causing you to skip three out of every five words I write, resulting in your receipt of a random approximation of my blog content, with a high error bar; you're still mad about my OS X blog.  All good bad reasons.
Heck, you could even scream for rational reasons.  Perhaps you have a philosophical beef with the FSF or GPL3.  Perhaps XEmacs still has some vestiges of feature support that do not yet exist in GNU Emacs, and you truly can't live without them.  I would think you're being a teeny bit uptight, but I would respect your opinion.
Whatever you do, just don't yell at me for thinking I'm dissing XEmacs or taking some sort of religious stance.  Far from it.  I just want a unified Emacs-o-cratic party.
**XEmacs vs. GNU Emacs today**
GNU Emacs pulled into the lead in, oh... I'd say somewhere around maybe 2002?  2003?  I wasn't really keeping track, but one day I noticed Emacs had caught up.
Even today I maintain XEmacs/FSF-Emacs compatibility for my elisp files – some 50k lines of stuff I've written and maybe 400k lines of stuff I've pilfered from
[EmacsWiki](http://www.emacswiki.org/cgi-bin/wiki)
, friends, and other sources.  I still fire up XEmacs whenever I need to help someone get un-stuck, or to figure out whether some package I've written can be coerced to run, possibly in restricted-feature mode, under XEmacs.
For years I chose stability over features.  And then one day GNU Emacs had... well, everything.  Toolbars, widgets, inline images, variable fonts, internationalization, drag-and-drop in and out of the OS clipboard (even on Windows), multi-tty, and a long laundry-list of stuff I'd written off as XEmacs-only.
And it was still stable.  Go figure.
I don't have the full feature-compatibility list.  Does it even exist?  You know, those tables that have little red X's if the Evil Competitor product is missing some feature your product offers, and little green checkmarks, and so on.  We ought to make one of those.  It would be useful to know what (if any) XEmacs features are preventing the last holdouts from migrating to FSF Emacs.
But for the past five years or so, just about every time an XEmacs user on a mailing list has mentioned a feature that's keeping them from switching, it's been solved.
If GNU Emacs isn't a perfect superset of XEmacs yet, I'm sure we could get it there if we had the big unified-platform carrot dangling in front of us.  And I bet it's pretty close already.
Features and stability aside, XEmacs is looking pretty shabby in the performance department.  Its font-lock support has never been very fast, and a few years back GNU Emacs took a giant leap forward.  XEmacs can take 4 or 5 seconds or longer to fontify a medium-sized source file.  Sure, it shows that big progress bar in the middle of the screen, so you know it's not dead, but when you're used to it being almost instantaneous, coming back to XEmacs is a real shocker.
And XEmacs has bugs.  Man, it has a lot of bugs.  I can't begin to tell you how many times I've had to work around some horrible XEmacs problem.  It has bugs (e.g. in its fontification engine and cc-engine) that have been open for years, and they can be really painful to work around.  I've had to take entire mode definitions and
them, using an ancient version of the mode for XEmacs because nothing even remotely recent will run.
You may not notice the bugs, but as elisp developers, we feel the pain keenly.
**Fundamental incompatibilities**
As if issues with stability, performance and bugs weren't enough, XEmacs has
*yet another*
problem, which is that its APIs for dealing with UI elements (widgets and input events, but also including things like text properties, overlays, backgrounds and other in-buffer markup) are basically completely different from their GNU-Emacs counterparts.  The two Emacsen share a great deal of common infrastructure at the Lisp level: they have mostly compatible APIs for dealing with files, buffers, windows, subprocesses, errors and signals, streams, timers, hooks and other primitives.
But their APIs range from mildly to completely different for keyboard and mouse handling, menus, scrollbars, foreground and background highlighting, dialogs, images, fonts, and just about everything else that interfaces with the window system.
The GUI and display code for any given package can be a significant fraction of the total effort, and it essentially has to be rewritten from scratch when porting from GNU Emacs to XEmacs or vice-versa.  Unsurprisingly, many package authors just don't do it.  The most famous example I can think of is James Clark's nxml-mode, which claims it'll never support XEmacs.  I found that pretty shocking, since I thought it was basic Emacs etiquette to try to support XEmacs, and here James was cutting all ties, all public about it and everything.  Wow.
But I totally understand, since I really don't want to rewrite all the display logic for my stuff either.
I'll be the first to admit: the API discrepancies are not XEmacs's fault.  I can't see how they could be, given that for nearly all these features, XEmacs had them first.
For a developer trying to release a productivity package, it doesn't really matter whose fault it is.  You target the platform that will have the most users.  I don't know what XEmacs's market share is these days, but I'd be very surprised if it's more than 30%.  That's a big number, but when you're an elisp hacker creating an open-source project in your limited spare time, that number can start looking awfully small.  Teeny, even.
**XEmacs should drop out of the race**
At this point it's becoming painful to watch.  GNU Emacs is getting all the superdelegates.  That warmonger VIM is sitting back and laughing at us.  But XEmacs just won't quit!
I'm sure there are a few old-timers out there who still care about the bad blood that originally existed between the two projects.  To everyone else it's ancient history.  As far as I can tell, there has been an atmosphere of polite (if subdued) cooperation between the two projects.  Each of them has incorporated some compatibility fixes for the other, although it's still mostly up to package authors to do the heavy lifting of ensuring compatibility, especially for display code.
I haven't seen any XEmacs/GNU-Emacs flamewars in a long time, either.  We're all just *Emacs users, keeping our community alive in the face of monster IDEs that vomit tabs, consume gigabytes of RAM, and attract robotic users who will probably never understand the critical importance of customizing and writing one's own tools.
When the Coke/Pepsi discussion comes up these days, it's usually an XEmacs user asking, in all seriousness, whether they should transition to GNU Emacs, and if so, would someone volunteer to help migrate their files and emulate their favorite behaviors.
Yes, someone will volunteer.  I promise.
**The dubious future of Emacs**
I've got good news and bad news.
The good news is:  Emacs is a revolutionary, almost indescribably QWAN-infused software system.  Non-Emacs users and casual users simply can't appreciate how rich and rewarding it is, because they have nothing else to compare it to.  There are other scriptable applications and systems out there — AppleScript, Firefox, things like that.  They're fun and useful.  But Emacs is
*self-hosting*
: writing things in it makes the environment itself more powerful.  It's a feedback loop: a recursive, self-reinforcing, multiplicative effect that happens because you're enhancing the environment you're using to create enhancements.
When you write Emacs extensions, sometimes you're automating drudgery (always a good thing), sometimes you're writing new utilities or apps, and sometimes you're customizing the behavior of existing utilities.  This isn't too much different from any well-designed scriptable environment.  But unlike in other environments, sometimes you're improving your editing tools and/or your programming tools for Emacs itself.  This notion of self-hosting software is something I've been wanting to blog more about, someday when I understand it better.
Eclipse and similar environments
*want*
to be self-hosting, but they're not, because Java is not self-hosting.  In spite of Java's smattering of dynamic facilities, Java remains as fundamentally incapable of self-hosting as C++.  Self-hosting only works if the code can "fold" on itself and become more powerful while making itself smaller and cleaner.  I'm not really talking about macros here, even though that's probably the first thing you thought of.  I'm thinking more along the lines of implementing JITs and supercompilers in the hosted runtime, rather than in the C++ or Java "hardware" substrate, which is where everyone puts them today.
I suspect (without proof) that in self-hosted environments, you can eventually cross a threshold where your performance gains from features implemented in the hosted environment outpace the gains from features in the substrate, because of this self-reinforcing effect: if code can make _itself_ faster and smarter, then it will be faster and smarter at making itself faster and smarter.  In C++ and Java, making this jump to the self-reinforcing level is essentially intractable because, ironically, they have so many features (or feature omissions) for the sake of performance that they get in their own way.
To be sure, Emacs, the current crop of popular scripting languages, and other modestly self-hosting environments are all pretty far from achieving self-reinforcing
*performance*
.  But Emacs has achieved it for
*productivity*
– at least, for the relatively small percentage of Emacs users who learn enough elisp to take advantage of it.  There are just enough of us doing it to generate a steady supply of new elisp hackers, and the general-purpose artifacts we produce are usually enough to keep the current crop of casual users happy.
**The bad news:  the competition isn't the IDEs**
I've argued that Emacs is in a special self-reinforcing software category.  For productivity gains, that category can
*only*
be occupied by editors, by definition, and Emacs is currently way ahead of any competition in most respects.  So most Emacs users have felt safe in the assumption that IDEs aren't going to replace Emacs.
Unfortunately, Emacs isn't immunized against obsolescence.  It still needs to evolve, and evolve fast, if it's going to stay relevant.  The same could be said of any piece of software, so this shouldn't be news.  But it's particularly true for Emacs, because increasing numbers of programmers are being lured by the false productivity promises of IDEs.
They really are false promises: writing an Eclipse or IntelliJ (or God help you, Visual Studio) plugin is a monumental effort, so almost nobody does it.  This means there's no community of building and customizing your own tools, which has long been the hallmark of great programmers.  Moreover, the effort to create a plugin is high enough that people only do it for really significant applications, whereas in Emacs a "plugin" can be any size at all, from a single line of code up through enormous systems and frameworks.
Emacs has the same learning-curve benefit that HTML had: you can start simple and gradually work your way up, with no sudden step-functions in complexity.  The IDEs start you off with monumental API guides, tutorials, boilerplate generators, and full-fledged manuals, at which point your brain switches off and you go over to see what's new on reddit.  ("PLEASE UPMOD THIS PIC ITS FUNNY!")
And let's not even get into the Million Refactorings yet.  It's a blog I've been working on for years, and may never finish, but at some point I'd like to try to show IDE users, probably through dozens or even hundreds of hands-on examples I've been collecting, that "refactoring" is an infinite spectrum of symbol manipulation, and they have, um, twelve of them.  Maybe it's thirteen.  Thirteen out of infinity – it's a start!
Programmers are being lured to IDEs, but the current crop of IDEs lacks the necessary elements to achieve self-hosting.  So the only damage to Emacs (and to programmers in general) is that the bar is gradually going down:  programmers are no longer being taught to create their own tools.
IDEs are draining users away, but it's not the classic fat-client IDEs that are ultimately going to kill Emacs.  It's the browsers.  They have all the power of a fat-client platform and all the flexibility of a dynamic system.  I said earlier that Firefox wants to be Emacs.  It should be obvious that Emacs also wants to be Firefox.  Each has what the other lacks, and together they're pretty damn close to the ultimate software package.
If Emacs can't find a way to evolve into (or merge with) Firefox, then Firefox or some other extensible browser is going to eclipse Emacs.  It's just a matter of time.  This wouldn't be a bad thing, per se, but there's a good chance it would be done poorly, take forever, and wind up being less satisfying than if Emacs were to sprout browser-like facilities.
**Emacs as a CLR**
So Emacs needs to light a fire and hurry up and get a better rendering engine.  Port to XUL, maybe?  I don't know, but it's currently too limited in the application domains it can tackle.  I realize this is a very hard problem to solve, but it needs to happen, or at some point a rendering engine will emerge with just enough editing power to drain the life from Emacs.
Emacs also needs to take a page from the JVM/CLR/Parrot efforts and treat itself as a VM (that's what it is, for all intents) and start offering first-class support for other languages.  It's not that there's anything wrong with Lisp; the problem is
*X programmers*
.  They only want to use X, so you have to offer a wide range of options for X.  Emacs could be written in any language at all, take your pick, and it wouldn't be good enough.
RMS had this idea a long, long time ago (when he was making the rather controversial point that Tcl isn't a valid option for X), and it eventually led to Guile, which led more or less nowhere.  Not surprising; it's a phenomenally difficult challenge.  There are really only two VMs out there that have achieved even modest success with hosting multiple languages: the CLR and the JVM.  CLR's winning that race, although it's happening in a dimension (Windows-land) that most of us don't inhabit.  Parrot is... trying really hard.  Actually, I should probably mention LLVM, which (like Parrot) was designed from the ground up for multi-language support, but took a lighter-weight approach.  So let's call it four.
In any case, it's a small very group of VMs, and they still haven't quite figured out how to do it: how to get the languages to interoperate, how to get languages other than the first to perform decently, and so on.
This is clearly one of the hardest technical challenges facing our industry for the next 10 years, but it's also one of the most obviously necessary.  And Emacs is going to have to play that game.  I'm not talking about hacked-together process bridges like PyMacs or el4r, either — I mean first-class support and all that it entails.
I've mentioned the rendering engine and the multi-language support; the last major hurdle is concurrency.  I don't know the answer here, either, but it needs an answer.  Threads may be too difficult to support with the current architecture, but there are other options, and someone needs to start thinking hard about them.  Editing is becoming a complicated business — too complicated for hand-rolling state machines.
**Compete or die**
So Emacs has some very serious changes ahead.
Let's face it:  we're not going to see real change unless ALL the Emacs developers out there – today's crop of JWZs – band together to make it happen.  But today we're divided.  Two groups of brilliant C hackers working on separate, forked code bases?  That's bad.  Two groups of maniacal elisp hackers working on incompatible packages, or at best wasting time trying to achieve compatibility?  Also bad.
Developers are starting to wake up and realize that the best "mainstream" extensible platform (which excludes Emacs, on account of the Lisp) is Firefox or any other non-dead browser (which excludes IE).  Dynamic typing wins again, as it always will.  Dynamic typing, property-based modeling and non-strict text protocols won the day for the web, and have resisted all incursions from heavyweight static replacements.  And somehow the web keeps growing, against all the predictions and lamentations of the static camp, and it still works.  And now the browsers are starting to sprout desktop-quality apps and productivity tools.  It won't be long, I think, before the best Java development environment on the planet is written in JavaScript.
Emacs has to compete or die.  If Firefox ever "tips" and achieves even a tenth of the out-of-the-box editing power of Emacs, not just for a specific application but for all web pages, widgets, text fields and system resources, Emacs is going to be toast.  I may be the last rat on the ship, but I'm sure not going down with it; even _I_ will abandon Emacs if Firefox becomes a minimally acceptable extensible programmer's editor.  This is a higher bar than you probably think, but it could happen.
We no longer need XEmacs to spur healthy competition.  The competition is coming in hard from entirely new sources.  What we need now is unity.
**Then why not unify behind XEmacs?**
I threw this in just in case you blew through the article, which I'd find perfectly understandable.  To summarize, I've argued that XEmacs has a much lower market share, poorer performance, more bugs, much lower stability, and at this point probably fewer features than GNU Emacs.  When you add it all up, it's the weaker candidate by a large margin.
Hence there's only one reasonable strategy:  Hill, er, I mean XEmacs has to drop out of the race.
I'm really sorry about this.  I'm a close personal friend of XEmacs, but I just can't endorse it anymore.  I used to be a laissez-faire kinda guy, as long as you were using
*some*
flavor of Emacs.  But at this point, if you're using XEmacs you're actively damaging not only your long-term productivity, but mine as well.  So I'd like to ask you to think long and hard about switching.  Soon.
If you're a local Emacs-Lisp guru, please offer your services to XEmacs users who would like to switch over.  The more pain-free the migration is, the faster it will happen.
If you're a graphic artist, consider making a nice, tasteful "Euthanize XEmacs!" logo.  Not that message, precisely, but something along those lines.  Make sure it's tasteful.  Perhaps "XEmacs is dead – long live XEmacs"?  Yes, I think that would do nicely.
If you happen to know someone on the XEmacs development team, send them some chocolates, or movie tickets, or something.  A thank-you, even.  We should honor their service.  But those guys are the most qualified on the planet to step in and start helping drive GNU Emacs forward, assuming the FSF team will have them.  Emacs is in very bad shape indeed if they will not.
If you're a local system administrator, consider
.  Sorry, I mean consider politely asking your emacs-users mailing list if they might be willing to set a timeline for deprecating XEmacs, thereby starting the most massive flamewar in your company's history.  Can't hurt!
If you're seeing red, and you skipped most of this article so you could comment on how amazingly lame this idea is, I recommend taking a little walk and getting some fresh air first.
If you're RMS, thank you for making Emacs and all that other stuff, and for keeping it free.  Please be nice to those who wish to help.  You're scary to the point of unapproachability, just 'cuz you're you.
XEmacs team, JWZ, and XEmacs package authors: thank you all for helping drive progress in the greatest piece of software of all time.  I can only hope that someday I may have chops like that.
Now how about we turn this into the most famous reverse-
[fork](http://en.wikipedia.org/wiki/Category:Software_forks)
in history?