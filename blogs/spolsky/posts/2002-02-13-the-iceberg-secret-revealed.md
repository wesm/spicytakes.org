---
title: "The Iceberg Secret, Revealed"
date: 2002-02-13
url: https://www.joelonsoftware.com/2002/02/13/the-iceberg-secret-revealed/
word_count: 2013
---


“I don’t know what’s wrong with my development team,” the CEO thinks to himself. “Things were going so well when we started this project. For the first couple of weeks, the team cranked like crazy and got a great prototype working. But since then, things seem to have slowed to a crawl. They’re just not working hard any more.” He chooses a Callaway Titanium Driver and sends the caddy to fetch an ice-cold lemonade. “Maybe if I fire a couple of laggards that’ll light a fire under them!”


Meanwhile, of course, the development team has *no idea *that anything’s wrong. In fact, nothing is wrong. They’re right on schedule.


Don’t let this happen to you! I’m going to let you in on a little secret about those non-technical management types that will make your life a million times easier. It’s real simple. Once you know my secret, you’ll never have trouble working with non-technical managers again (unless you get into an argument over the coefficient of restitution of their golf clubs).


It’s pretty clear that programmers think in one language, and MBAs think in another. I’ve been thinking about the problem of communication in software management for a while, because it’s pretty clear to me that the power and rewards accrue to those rare individuals who know how to translate between Programmerese and MBAese.


Since I started working in the software industry, almost all the software I’ve worked on has been what might be called “speculative” software. That is, the software is not being built for a particular customer — it’s being built in hopes that *zillions* of people will buy it. But many software developers don’t have that luxury. They may be consultants developing a project for a single client, or they may be in-house programmers working on a complicated corporate whatsit for Accounting (or whatever it is you in-house programmers do; it’s rather mysterious to me).


Have you ever noticed that on these custom projects, the single most common cause of overruns, failures, and general miserableness always boils down to, basically, “the (insert expletive here) customer didn’t know what they wanted?”


Here are three versions of the same pathology:

1. “The damn customer kept changing his mind. First he wanted Client/Server. Then he read about XML in Delta Airlines Inflight Magazine and decided he had to have XML. Now we’re rewriting the thing to use fleets of small Lego Mindstorms Robots.”
“We built it *exactly the way they wanted*. The contract specified the whole thing down to the smallest detail. We delivered exactly what the contract said. But when we delivered it, they were crestfallen.”
“Our miserable sales person agreed to a *fixed price contract* to build what was basically unspecified, and the customer’s lawyers were sharp enough to get a clause in the contract that they don’t have to pay us until ‘acceptance by customer,’ so we had to put a team of nine developers on their project for two years and only got paid $800.”


If there’s one thing every junior consultant needs to have injected into their head with a heavy duty 2500 RPM DeWalt Drill, it’s this: **Customers Don’t Know What They Want. Stop Expecting Customers to Know What They Want.** It’s just never going to happen. Get over it.


Instead, assume that you’re going to have to build something *anyway*, and the customer is going to have to like it, but they’re going to be a little bit surprised. YOU have to do the research. YOU have to figure out a design that solves the problem that the customer has in a pleasing way.


Put yourself in their shoes. Imagine that you’ve just made $100,000,000 selling your company to Yahoo!, and you’ve decided that it’s about time to renovate your kitchen. So you hire an expert architect with instructions to make it “as cool as Will and Grace’s Kitchen.” You have no idea how to accomplish this. You don’t know that you want a Viking stove and a Subzero refrigerator — these are not words in your vocabulary. You want the architect to do something good, that’s why you hired him.


The Extreme Programming folks say that the solution to this is to get the customer *in the room* and involve them in the design process every step of the way, as a member of the development team. This is, I think, a bit *too* “extreme.” It’s as if my architect made me show up while they were designing the kitchen and asked me to provide input on every little detail. It’s boring for me, if I wanted to be an architect I would have become an architect.


Anyway, you don’t really *want* a customer on your team, do you? The customer-nominee is just as likely to wind up being some poor dweeb from Accounts Payable who got sent to work with the programmers because he was the slowest worker over there and they would barely notice his absence. And you’re just going to spend all your design time explaining things in words of one syllable.


Assume that your customers don’t know what they want. Design it yourself, based on your understanding of the domain. If you need to spend some time learning about the domain or if you need a domain expert to help you, that’s fine, but the design of the software is your job. If you do your domain homework and create a good UI, the customer will be pleased.


Now, I promised to tell you a secret about translating between the language of the customers (or nontechnical managers) of your software and the language of programmers.


You know how an iceberg is 90% underwater? Well, most software is like that too — there’s a pretty user interface that takes about 10% of the work, and then 90% of the programming work is under the covers. And if you take into account the fact that about half of your time is spent fixing bugs, the UI only takes 5% of the work. And if you limit yourself to the *visual *part of the UI, the pixels, what you would see in PowerPoint, now we’re talking less than 1%.


That’s not the secret. The secret is that *People Who Aren’t Programmers Do Not Understand This*.


There are some very, very important corollaries to the Iceberg Secret.


**Important Corollary One.** If you show a nonprogrammer a screen which has a user interface that is 90% worse, they will think that the program is 90% worse.


> I learned this lesson as a consultant, when I did a demo of a major web-based project for a client’s executive team. The project was almost 100% code complete. We were still waiting for the graphic designer to choose fonts and colors and draw the cool 3-D tabs. In the meantime, we just used plain fonts and black and white, there was a bunch of ugly wasted space on the screen, basically it didn’t look very good at all. But 100% of the functionality was there and was doing some pretty amazing stuff.
> What happened during the demo? The clients spent the *entire meeting *griping about the graphical appearance of the screen. They weren’t even talking about the UI. Just the graphical appearance. *“It just doesn’t look slick,”* complained their project manager. That’s all they could think about. We couldn’t get them to think about the actual functionality. Obviously fixing the graphic design took about one day. It was almost as if they thought they had hired *painters.*


**Important Corollary Two.** If you show a nonprogrammer a screen which has a user interface which is 100% beautiful, they will think the program is almost done.


> People who aren’t programmers are just looking at the screen and seeing some pixels. And if the pixels look like they make up a program which does something, they think “oh, gosh, how much harder could it be to make it *actually work?*“
> The big risk here is that if you mock up the UI first, presumably so you can get some conversations going with the customer, then everybody’s going to think you’re almost done. And then when you spend the next year working “under the covers,” so to speak, nobody will really see what you’re doing and they’ll think it’s nothing.


**Important Corollary Three.** The dotcom that has the cool, polished looking web site and about four web pages will get a higher valuation than the highly functional dotcom with 3700 years of archives and a default grey background.


> Oh, wait, dotcoms aren’t worth anything any more. Never mind.


**Important Corollary Four.** When politics demands that various nontechnical managers or customers “sign off” on a project, give them several versions of the graphic design to choose from.


> Vary the placement of some things, change the look and feel and fonts, move the logo and make it bigger or smaller. Let them feel important by giving them non-crucial lipstick-on-a-chicken stuff to muck around with. They can’t do much damage to your schedule here. A good interior decorator is constantly bringing their client swatches and samples and stuff to choose from. But they would never discuss dishwasher placement with the client. It goes next to the sink, no matter what the client wants. There’s no sense wasting time arguing about where the dishwasher goes, it has to go next to the sink, don’t even *bring it up; *let the clients get their design kicks doing some harmless thing like changing their mind 200 times about whether to use Italian Granite or Mexican Tiles or Norwegian wood butcher-block for the countertops.


**Important Corollary Five.** When you’re showing off, the only thing that matters is the screen shot. Make it 100% beautiful.


> Don’t, for a minute, think that you can get away with asking *anybody* to *imagine how cool this would be*. Don’t think that they’re looking at the functionality. They’re not. They want to see pretty pixels.
> Steve Jobs understands this. Oh **boy** does he understand this. Engineers at Apple have learned to do things that make for great screen shots, like the gorgeous new 1024×1024 icons in the dock, even if they waste valuable real estate. And the Linux desktop crowd goes crazy about semitransparent xterms, which make for good screenshots but are usually annoying to use. Every time Gnome or KDE announces a new release I go straight to the screenshots and say, “oh, they changed the planet from Jupiter to Saturn. Cool.” Never mind what they really did.


Remember the CEO at the beginning of this article? He was unhappy because his team had showed him great PowerPoints at the beginning — mockups, created in *Photoshop*, not even VB. And now that they’re actually getting stuff done under the covers, it looks like they’re not doing anything.


What can you do about this? Once you understand the Iceberg Secret, it’s easy to work with it. Understand that any demos you do in a darkened room with a projector are going to be *all about pixels*. If you can, build your UI in such a way that unfinished parts *look* unfinished. For example, use scrawls for the icons on the toolbar until the functionality is there. As you’re building your web service, you may want to consider actually leaving out features from the home page until those features are built. That way people can watch the home page go from 3 commands to 20 commands as more things get built.


More importantly, make sure you control what people think about the schedule. Provide a [detailed schedule](https://www.joelonsoftware.com/articles/fog0000000245.html) in Excel format. Every week, send out self-congratulatory email talking about how you’ve moved from 32% complete to 35% complete and are *on track* to ship on December 25th. Make sure that the actual facts dominate any thinking about whether the project is moving forward at the right speed. And don’t let your boss use Callaway Titanium Drivers, I don’t care how much you want him to win, the USGA has banned them and it’s just not fair.


[ ](http://discuss.fogcreek.com/joelonsoftware/default.asp?cmd=show&ixPost=3676)


Discuss
