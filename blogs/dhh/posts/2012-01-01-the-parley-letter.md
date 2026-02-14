---
title: "The Parley Letter"
date: 2012-01-01
url: https://dhh.dk/2012/the-parley-letter.html
slug: the-parley-letter
word_count: 2579
---


My [appearance on the Ruby Rogues podcast](http://rubyrogues.com/056-rr-david-heinemeier-hansson/) recently came up for discussion again on the private Parley mailing list. A long list of topics were raised and I took a time to ramble at large about all of them at once. Apologies for not taking the time to be more succinct, but at least each topic has a header so you can skip stuff you don't care about.


### Maintainability


It's simply not true to say that I don't care about maintainability. I still work on the oldest Rails app in the world. The original Basecamp code base is going to be ten years in a few months. It's still our biggest product and a multi-million dollar business. We still maintain it, fix things, and even occasionally introduce minor features. Until last year, when the new Basecamp premiered, we were introducing major features on a regular basis.


This code base has been working on by probably around 25-30 people, if you count the few developers who've left 37signals. We would throw new developers at the code base whenever they joined with little else but a feature request and a smile. They all picked it up, committed to the code base, and deployed changes within a few days.


On top of Basecamp, we have multiple other products that have been around for a very long time (at least in software years). Campfire is from 2005, Highrise is from 2007. Again, two code bases still being maintained and developed.


Anyway, that's just the anecdote to support what I ultimately believe about maintainability: That it's indistinguishable from good design. There's not good design that then suddenly rots and becomes horrible and unmaintainable. There is not bad design that suddenly blossoms and becomes a peach to extend years after.


So I tend to find that people pull out the maintainability card as a last resort when all other rational arguments for a design have failed in the plain sight of looking at the code.


I know this is a bit harsh, but I also find it to be a variant of "but does it scale?". It's so hard to argue against something like that when it's based on future unknowns. Who knows how it's going to be maintainable when you get new business requirements, new people with "other ideas" join, and so forth. But there's a reason we try not to worry too much about The Future and that's because predicting it is hard. YAGNI and all that.


Given that, I think the responsible thing is to make the best damn piece of software facing CURRENT DAY constraints and let tomorrow worry about tomorrow. When the actual changed requirements or new people with "new ideas" roll around, they'll have less baggage to move around. The predictions for what the app is going to look like a decade from now are pretty likely to be wrong anyway.


This last part I know all too well because I, like all programmers, have occasionally succumbed to future coding. Only to learn later that what I thought I needed in the future wasn't it at all. And then my task was double because I had to rip out the predicted crap before I could implement the actual work.


### The Traveling Consultant Problem (TCP)


The most fierce debates about software design I've had has been with traveling consultants. People who visit other software shops and try to teach them better techniques. It presents what I like to call The Traveling Consultant Problem.


Consultants are invariably called in whenever there's a crisis of some sort. Usually it's because the team has created such a horrid mess of a code base that they're no longer able to make progress at a reasonable pace. So you call in the rescue team.


What do you expect to see when you're called in as the rescue team? Fucking mayhem! Otherwise they wouldn't have called you in the first place! So if you base your view of the world and the design qualities of a framework like Rails off this mayhem, of course you're going to think shit is broken. People misusing features, people hanging themselves with all the rope that Ruby and Rails gives them.


This is like a doctor diagnosing the health of a nation by extrapolating from all the sick people who come to see him. Yes, you're going to see a lot of ills. You're not going to see a lot of healthy people because they don't come to you!


(On a tangent, this is exactly what's wrong with drug policy in general. Yes, you can find cases of people going crazy from dropping acid, but if you only look at those, you're going to miss the transformations that created the Steve Jobs that brought the world so much good. And, on a less evangelical scale, people having a better time partying out in the world with an acceptable downer to show for it afterwards).


Now this doesn't mean that there is no value to be gained from the observations of the traveling consultant. Far from it. But it is to say that the observations are skewed from a sample group of the broken.


Often times the best tools and techniques, the ones that make you most productive, can be sharp things that can cut you. Like one my favorite feature of Ruby, the beloved monkey patching. It's a sharp tool, and you can hurt yourself, but oh what a tool.


So here's my perspective: I try to make simple, sharp tools. I'm OK with the fact that some people will cut themselves because that risk is the flip side of the productivity reward. I encourage people to live up to my high expectations of them. I expect everyone working with Rails to be interested in improving their craft and creating beautiful code. If you don't give a shit, if you're not interested in living up to what Rails has to teach you, or you're happy writing shitty code, then Rails is not going to save you. It's not its mission. The plate is already full trying to be the best that it can be for people who care.


### Arguing OO technique


It is also not true that I don't like to argue OO technique. I fucking LOVE to argue coding techniques of all kind. What I don't like to do, though, is to argue technique outside the realm of looking at real code. Let's have an argument alright, but let's base it off code examples. Before/after and all that jazz.


I've found that's the only way to keep a calibrated bullshit meter. There is so much WANKERY (I know you guys love that term ;)) in the world of software when people are left to just talk technique in the abstract. We're overburdened and, frankly, oppressed by the pontifications of "architects".


So that's why I love software. It's not like modern art. You can't just keep spouting intellectual nonsense forever. At the end of the day, you have to translate your prescriptions into running code and that's when the bullshit meter activates. It may sound nice, but is the code better? If not, call bullshit.


Which brings me to another point about calling bullshit. The state of the art in the Rails world is full of hard-won simplifications. It's incredibly easy to devolve and regress from that. While Java certainly isn't a pinnacle of language design, it took quite a few years of devolution to go from something relatively simple like servlets to the steaming pile of shit that is J2EE. And every tiny step of the way probably seemed somewhat reasonable at the time to reasonable people.


If we don't call bullshit loud and often against what's perceived as putting us on this path of devolution, which imo is the standard trajectory of software, then we will end up exactly where they did. In Kompleksistan with no map to find our way back.


### Judging code on gut


I like to say that when reasonable people look at a piece of actual code, their differences tend to dissipate. It's much easier to maintain an illusion of disagreement until there's actual code in front of you. I know this from almost every single debate I've had in the Ruby world with people I've disagreed with. When we actually sit down in front of a piece of real code and try to improve it, we tend to converge on the same solution.


This observation was the most obvious in the Merb->Rails 3 merger. When Yehuda and I and others actually sat down to talk about what we care about, we found that it was completely complementary. And when we then went to work on making it so, these furious debates lost a lot of their heat but retained all the light.


So yes, judging code on gut is mostly the concept of judging code by reading it. Not by debating it in the abstract. You can talk to authors all day long who know everything there is to know about writing a novel, but still can't crank out a compelling story. At the end of the day the only way you can tell the good from the bad, in code or literature, is by reading it.


That doesn't mean that gut reactions to code aren't based on something more rigorous. I formed my gut reading the works previously described here. Smalltalk Best Practices, Enterprise App Architecture, Refactoring, and so forth. What did all those books have in common? Lots and lots of code! Lots and lots of before/after! They swayed my opinion on good design by show, don't tell.


### Hypermedia


Another part of the necessary art of calling bullshit is to take down good ideas when they become inflated beyond what they can bear. Using URLs instead of IDs in your json responses is a reasonable idea that I support. But there's just not enough there there to dress it up in HATEOAS, HAL, custom mime types, and all the other -- here's that word again! -- wankery that passes for muster in the hypermedia orthodoxy.


When I introduced REST as a concept for Rails in 2006, it wasn't because of the intellectual purity of the prophet Fielding. It was because the pattern provided real, practical advances for the code it was applied to. Unweilding controllers gained a perfect straight jacket in the softest silk to keep them under control. It made the connection between CRUD and the web in such a way that we could just take the convention for granted and start worrying about other things.


So I felt there was a lot there there. Granted, lots of others didn't at the time, but today I don't see a lot of people arguing against the progress we gained from that. That's not the same as declaring a blood alliance with all things Roy Fielding, though. I evaluate every design principle on the merits of WHAT HAVE YOU DONE FOR MY CODE LATELY! I've implemented a hypermedia API (to varying degree of scripture compliance) for the new Basecamp (minus the custom mimetype) and it just didn't do much for me.


Again, there's a sliver of a good idea there buried under ten feet of academic hypermedia orthodoxy with little connection to real world benefits.


### Context for Rails


There absolutely is a design context for Rails. I know this might be controversial to some, but I have no problem saying that Basecamp is the single most important application for Rails. (I can already imagine the shocked and horrified faces for stating such an overt priority!). I evaluate every design technique or feature in Rails first against what it would do for Basecamp. It's by no means the ONLY evaluation, but it is the first.


So yes, the closer your application is to an application like Basecamp -- and I make that net extremely wide, I consider, say, 500px, Github, Shopify, and others to fall into "close enough" -- the closer you are to the primary use case that guides the development of Rails.


Again, it's not the only use case. There are many uses of Rails that are very unlike that of Basecamp. Yehuda and others are building things with a combo of Rails + Ember.js that's distinctly unlike the architecture used in Basecamp and doing so to good effect.


But it does mean that anything that's obviously a good idea for applications like Basecamp gets on a fast track for inclusion. Anything that's not obviously a good idea has to travel through a longer, more rigorous proving path to find its way in. That is simply the nature of design. If we want to do good work, we first have to know -- really know -- the problem. When it's your own problem, you know it by instinct. When it's somebody else's problem, you first have to take the time to learn it.


### Focusing on "ease of getting started"


Rails wasn't created with any particular focus on "the ease of getting started". In the grand scheme of things, I start new applications fairly rarely. The most important code bases in my life (Rails, Basecamp, Highrise, etc) are all old men in rocking chairs. I consider this, like maintainability, to be a side effect of good, simple design.


The more wrapping paper you reject, the easier it is to open the package and enjoy your toys. I work so very, very hard to keep needless wrapping paper out of the design of Rails and the popular design principles that are associated with it.


### Defending your right to rspec and other terrible ideas


With all this being said, I have no illusion that I'll successfully convince everyone of everything that I consider a good idea. Or dissuade them of what I consider a bad idea. The popularity of rspec stands as a stark reminder that there are limits to my successful advocacy. I consider rspec to have the worst DSL of any major piece of Ruby software, yet lots of people seems to take no offense at all.


Here's the perverse thing: That's great. I want Rails to be a big tent. In a big tent, there has to be room for different dialects. You cannot keep a perfect mono-culture for a community the size of Rails. And you shouldn't.


My mission is to clearly state what I consider good and what I consider bad. Rails is an expression of my taste in software development, so of course that taste is going to be expressed around the techniques we employ in the use of Rails. I want to make sure that fresh recruits are at least well aware of where I stand on most issues. So they can, if they please, choose to follow a carefully curated set of opinions on how best to develop web applications with Rails and trust that it'll be good. Just like Rails itself is a carefully curated collection of APIs and DSLs.


But one of my key guiding principles in life is that of "consenting adults". You can do whatever the fuck you want with Rails, pervert it in ways that make me gag, and use rspec to test it. I will defend that right. As long as you've read the warning labels, you are free to get high as a kite on whatever meth-ODOLOGY of choice and flavor of the month.


Just expect that I will weigh in.

