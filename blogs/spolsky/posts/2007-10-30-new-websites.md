---
title: "New websites"
date: 2007-10-30
url: https://www.joelonsoftware.com/2007/10/30/new-websites/
word_count: 1133
---


Those of you who develop custom software for clients have probably been burned more than once by clients who are disappointed with what you thought was going to be the “final” version, and start demanding countless changes. You’ve probably built pretty good defenses against this: I’ve seen contrators ask their clients to sign every single page of the spec so that there can be no question that the client got *exactly* what they were promised.


It doesn’t help. The client is still unhappy. They knew what you were going to build, intellectually, but as soon as they saw it in real life, they started finding lots of problems:


> Custom development is that murky world where a customer tells you what to build, and you say, “are you sure?” and they say yes, and you make an absolutely beautiful spec, and say, “is this what you want?” and they say yes, and you make them sign the spec in indelible ink, nay, *blood*, and they do, and then you build that thing they signed off on, promptly, precisely and exactly, and they see it and they are horrified and shocked, and you spend the rest of the week reading up on whether your E&O insurance is going to cover the legal fees for the lawsuit you’ve gotten yourself into or merely the settlement cost. Or, if you’re really lucky, the customer will smile wanly and put your code in a drawer and never use it again and never call you back.
> (from [Set Your Priorities](https://www.joelonsoftware.com/articles/SetYourPriorities.html))


That’s just how the world works. A spec can’t reveal everything. Clients can’t use the spec for their real work, and they’ll never notice just how many keystrokes it takes to do basic operations until you get, at least, a UI prototype working.


A good way to defend yourself against this is to deliver lots and lots of interim versions to the client: real, working interim versions, and get them using it so you can build feedback into future iterations. Rather than going off in a cave and building something for a year, only to find out that 9 months of that work is wasted, you show the client something every month, say, and get instant feedback and then you adjust directions if needed. That’s one thing that many people waving the “agile” flag are talking about. The first delivery should be the minimum thing that could possibly be useful.


This should not be seen as an excuse to write code without designing it, first. All code is going to be designed eventually. But if you try to design it first in a programming language, the designing process is vastly slower than if you were designing it with pencil and paper and descriptive paragraphs in the English language, so you’re wasting time.


Anyway. Where was I going with this? Oh yes. For the first time, I had the honor of being the “client” in that client/developer relationship, when we hired [Happy Cog Studios](http://www.happycog.com/) to build our new website.


We gave them a relatively precise, unambiguous spec. Basically, we wanted the same website as we already had, only we wanted it to be prettier.


Here’s what our original website, designed by [Dave Shea](http://www.mezzoblue.com/), looked like (click to enlarge:)


It was a great design, but several years old, and it felt dated.


Happy Cog gave us a couple of design options to use as starting points:


Or:


Both were quite good, I think, but had showstoppers. The first design put the most important paragraph in a spot where people were very likely to miss it. The second design required 1024 pixels. Even when people have 1024×768 (or larger) monitors, they don’t keep their browsers that wide. And about 30% of the people we asked hated the orange.


Which led us into several rounds of iteration by “a committee of tasteless slobs,” that committee being mostly me, and somehow we ended up with a design that just got worse and worse and worse the more we tweaked it. This is what we started to build:


That’s when [I knew we had to start over](https://www.joelonsoftware.com/items/2007/09/11.html), and when I suddenly knew what it felt like when you told the barber to give you an “en brosse” haircut because you thought you would look like Tom Cruise, and that’s not what happened.


Anyway, at that point I realized the design was suffering because it was trying to stuff a FogBugz identity (with the kiwi and the FogBugz logotype) into a Fog Creek website (with the Fog Creek wave logo). This both ate a lot of space at the top of the page, where real estate was scarce, and made the page a confusing bundle of links.


Fortunately, Happy Cog was very patient with us. We asked them to start fresh, with a new design concept and a new designer. Second, we decided that the FogBugz website doesn’t have to look anything like the Fog Creek website. It should be a showcase for FogBugz, with a tiny link to Fog Creek at the bottom. Happy Cog would design the FogBugz website. The Fog Creek website, which far fewer people ever visit, is about *the company itself*. It links to our products but doesn’t have to have the same graphic design. I designed that myself, with a very minimalist design that captured the essense of the company:


[Larger picture](https://www.joelonsoftware.com/wp-content/uploads/2007/10/30-fogcreek-large.png) | [Go to fogcreek.com](http://www.fogcreek.com/)


My favorite part is the slideshow, with a set of pictures that captures life at Fog Creek perfectly. It’s plain, it’s minimalist, it reflects the company personality, and it harks back to the very first website design from when we started the company seven years ago:


Happy Cog assigned [Dan Mall](http://danielmall.com/) to the redesign of the FogBugz page. His first design was really good, and I knew that it would be better to just shut up and give him artistic license to do whatever he thought was best. I thought that we could try and meddle in his design, tweaking things left and right, and get another bad design-by-committee, or we could just tell him we trusted him and whatever he delivered would be exactly what went live.


Which it was.


[Larger picture](https://www.joelonsoftware.com/wp-content/uploads/2007/10/30-fogbugz-large.png) | [Go to fogbugz.com](http://www.fogcreek.com/FogBugz/)


So that’s where we stand. Babak and I spent a week creating a [video FogBugz demo](http://media.fogcreek.com/fogcreek.com/FogBugz/60movie/60movie.html) for the site using my favorite screen-recording program, [TechSmith Camtasia](http://www.techsmith.com/camtasia.asp). The sound we could get in the office was just not good enough, so we rented studio time to record the soundtrack.


It took a lot of editing, but we got the video down to about 13 minutes. Probably too long for a web video, but what can ya do. And I already talk to fast.


Anyway, that’s the saga of the new websites. How do you like them?
