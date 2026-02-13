---
title: "Fruity treats, customization, and supersonics: FogBugz 7 is here"
date: 2009-07-20
url: https://www.joelonsoftware.com/2009/07/20/fruity-treats-customization-and-supersonics-fogbugz-7-is-here/
word_count: 1479
---


A year ago today, FogBugz development was in disarray.


The original roadmap was too complicatedWe had done this big offsite at a beach house in the Hamptons and came up with a complicated roadmap that involved splitting FogBugz into two separate products and two separate teams. We had done a lot of work on the architecture that made the product much more modular, but we had this goofy plan to do a major release containing virtually no new features, just to let the new architecture shake out, a plan which nobody was very excited about.


So, on July 31, 2008, we reset our plans. We gave up on the idea of shipping a standalone Wiki product, and merged the Wiki team with the FogBugz team. And we nailed down a new vision for FogBugz 7 that’s a lot easier to understand and a much better product: something we could ship in one year.


Then the development team shipped it. Exactly on schedule. Well, maybe a week or two early. They used [Evidence Based Scheduling](https://www.joelonsoftware.com/items/2007/10/26.html) religiously on this large one year project and it worked amazingly well. Yes, they had to cut and trim features as they went along, but the accuracy of the estimates also gave them the confidence to add a couple of major features (like Scrum support) that you’ll love.


One of the best things we did as a development team was to write a short, concise, comprehensible vision statement that got everybody exactly on the same page about what we were going to do over the course of a year. The vision statement made it easy to prioritize. Instead of just telling us what was in the product, it also gave us a way to know what was *out*.


Here’s the vision statement, in its entirety, which is a pretty good description of what we are actually shipping today. Please excuse the tone of voice; remember that this was an internal document to galvanize the team.

Fog Creek Confidential

## FogBugz 7


As of August, 2008, the entire FogBugz and Weeble teams are working towards a single major new release of FogBugz that will blow away our customers (real and imaginary). When they see it they will grow weak in the knees. Competitors will shiver in fear at the monumental amount of win in this release. As customers evaluate the software, they will simply never find a reason **not** to use FogBugz to run their software teams. No matter what the grumpy people on their team come up with, they’ll find that not only have we implemented it in FogBugz, we’ve done it in a FULL-ASSED way. No more HALF-ASSED features (I’m looking at you, logo customization in FogBugz 6.1).


This release has **three important focus areas** with friendly catchnames.

1. fruity treats
2. customization
3. supersonics


If it’s NOT ON THAT LIST it’s NOT IN THE PRODUCT. Get used to it.


## fruity treats


FogBugz 7.0 will include a long list of simple improvements that will make life dramatically easier for people trying to get things done, especially when they want to do things just a wee bit differently than we do here in the Land of the Fog. Every little feature will be a delight for *somebody,* especially that person who keeps emailing us because he can’t believe that the feature he wants which is *obviously* only *six lines of code* hasn’t been implemented in FogBugz 1.0, 2.0, 3.0, 4.0, “4.5”, or 6.0, and if we don’t get it soon he JUST MIGHT HAVE TO GO OVER TO THE AUSTRALIANS.


Collectively, though, **fruity treats** will make FogBugz friggin’ amazing, and they’ll help us *win more sales *because we won’t have so many showstopper reasons why people choose another so-called bug “tracker.”


What’s a fruity treat? It must fit these three rules to get into the 7.0 orchard:

1. It must be something **customers **and potential customers are** asking about all the time**
2. There must **not be a trivial, easy workaround **in 6.1
3. It must be **relatively easy for us to implement**. No big earth-shaking new features will sneak in.
4. “Three rules,” I said. Not *four*. Why is there a 4 here?


Visit the shared filter *FogBugz 7 Fruity Treats* to see what’s coming up.


### customization


FogBugz 7.0 will include our smashingly powerful new **plug-in archicture**, which, combined with the FogBugz API, will give people **complete confidence** that if there’s anything FogBugz *can’t* do out of the FogBox, you can write it yourself. No more will we tell customers “you get the source code, so you can modify it!” That’s BS. They know perfectly well that if they modify our source code, terribobble tragedies will occur the minute we release a service pack. From now on, we can say, “there’s a great plug in architecture and a whole online cornucopia of righteous plug-ins available for download.”


So you can trick out your FogBugz installation like a lowrider or an off-road dune buggy. You can make it into a Cadillac or a space shuttle. It’s up to you.


## supersonics


Thanks to the newfangled, all-electronic compilation machine (“Wasabi”) that we had installed at great expense, FogBugz will be running on the CLR and Mono for greatly improved performance and compatibility. Whiz zip blip! bleep! You’ll be able to run 1000s of users on one server. Long queries will finish faster. Laundry will be brighter.


## and that is it.


Nothing else. Go fix yourself an icy lemonade.


The team got pretty excited. Having a sharp focused vision statement like that, and having the whole team working towards a single shared goal, really helped us get our house in order. We scrubbed through thousands of backlogged ideas, feature requests, and comments, and came up with a set of fruity treats that will eliminate virtually every customer objection that we hear during the sales process. We developed a comprehensive plug-in architecture that’s pretty amazing, and had interns develop a slew of slick plug-ins. And the fact that Wasabi is now a genuine .NET language made for substantial performance improvements over running on the VBScript “runtime.”


I’ll let the team give you a comprehensive look at [what’s new in FogBugz 7](http://www.fogcreek.com/FogBugz/WhatsNew.html), but here are some of the highlights:

- Subcases: organize your work hierarchically
- EBS can track the schedule of developers who work on multiple projects
- EBS also now has dependencies (work on X can’t start until Y is complete)
- Scrum is fully supported, with project backlogs and EBS-powered burndown charts
- Just about the slickest implementation of tags you’ve ever seen
- Plug-ins, with comprehensive support throughout the product
- Customizable workflow
- Lots of visual improvements and small usability enhancements
- A context menu in the grid saves steps
- Easier case entry right from the grid
- Auto complete in case fields, so you don’t have to remember case numbers
- Custom fields (Yes. They tied me up in a closet.)
- URL triggers (FogBugz will hit a URL you specify when certain events happen)
- Easier administration, through an administrator dashboard, and a feature for cloning users and creating a list of new users all at once
- Much better performance, including substantial caching that speeds up display of email, EBS calculations, and more


Those are just the big-ticket items. FogBugz 7 is rife with little areas where the development team put a ridiculous amount of attention to detail. For example, the signup process, which is actually very complicated on the backend, became much simpler on the front end, due to a heroic amount of work that every user will only see once. If you do nothing else, [check out the signup process](http://www.fogcreek.com/FogBugz/) to see the effort that went into making signup just a tiny bit faster. Another example: we completely replaced the entire email processing infrastructure, just because there were tiny corner case bugs that simply could not be solved with the commercial class library we had been using.


Tyler Griffin Hicks-WrightI wish I could take more credit for it, but the truth is, Fog Creek has grown. We have a very professional team with testers, program managers, and developers, and I just sort of sit here agog at what a brilliant job they’re doing. All of the credit for this fantastic new product goes to them. I’m just the Michael Scott character who wastes everybody’s time whenever I venture out of my office.


FogBugz 7 is shipping today for Windows servers and on our own, hosted infrastructure. The Mono version (for Macintosh and Linux) will be in beta soon. To try it, go to [try.fogbugz.com](http://try.fogbugz.com/).


If you’re currently using FogBugz on Demand, you’re already using 7.0.


If you run FogBugz on your own server and have an up-to-date support contract, the [upgrade is free](https://shop.fogcreek.com/FogBugz/status.asp), otherwise, [bring your support contract up-to-date](https://shop.fogcreek.com/FogBugz/status.asp) and you’ll be good to go.
