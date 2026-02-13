---
title: "The Road to FogBugz 4.0: Part IV"
date: 2005-03-31
url: https://www.joelonsoftware.com/2005/03/31/the-road-to-fogbugz-40-part-iv/
word_count: 1792
---


A ridiculously small portion of the energy it takes to make a commercial software product actually goes into the writing of lines of code. I would estimate that out of every 100 calories expended by the Fog Creek team:


> 25 calories are spent on customer service
> 55 calories are spent on debugging, beta testing, and minor tweaks
> 8 calories are spent on marketing, including the Fog Creek website
> 5 calories are spent reading college kids’ resumes and interviewing said college kids
> 5 calories are spent on code that never ships, such as the online demo and the online store
> Leaving just:
> 2 calories spent on actually writing new lines of code that ship to a customer.


This, I think, helps explain why so many software companies started by programmers fail: programmers are really good at writing news line of code, they might be good at debugging, but nobody ever taught them how to do marketing or customer service, and they are probably horrible at graphic design.


Before a consumer will buy your software product, they’ll evaluate all kinds of things to decide if it’s a real product that will meet their needs:

- They’ll evaluate the quality of your website.
- They’ll look for discussion groups to see if people are actually using the product, and if the people who have problems are getting prompt resolutions.
- They’ll look to see if there is a third-party support infrastructure, like books.
- They’ll evaluate your reputation.
- They’ll search the web to see if you have positive buzz.
- They’ll see how long you’ve been around, and they’ll try to evaluate whether you’re profitable and successful and likely to stay around to continue supporting the product.
- Oh, and if they have a few minutes left over, they *might* actually look at your product itself to see if it works.


And *that* explains why people buy overpriced but useless shelfware that costs $millions and doesn’t really work. They rationalize that if they install it, they’ll be shielded from criticism and other mercurial notes of anger.


Anyway, before we could launch FogBugz, even after the final shipping bits were perfect and ready to go, we had a list of things we wanted to have ready to make the product experience complete. For FogBugz 4.0 the big things were:

1. Professional-quality graphic design in the user interface
2. An online demo that included *every* feature of the product
3. An online movie that introduced the product for couch potatoes
4. A great marketing website
5. Getting at least one book about FogBugz into bookstores
6. Making a real physical product available on CD-ROM


**Graphic Design**


Human emotions can be really, really superficial. In particular people ridiculously overvalue aesthetics and beauty when evaluating products. It’s one of the reasons iPods, and, for that matter, Keanu Reeves, are so successful. If you have a product that is functional but not beautiful you have a really, really, really, really, really, really, really, really, really, really big handicap to overcome against the product that is beautiful but maybe not so functional.


Given the importance of this I spent days looking at portfolios of web designers. I happened upon [CSS Zen Garden](http://www.csszengarden.com/), which was new at the time, the effort of Vancouver-based graphic designer [Dave Shea](http://www.mezzoblue.com/) who wanted to prove that CSS did not imply ugly boxy design. In those days there were only a few designs available on Zen Garden and a lot of them were done by Dave himself, but they were all stunning. ([Here’s one](http://www.csszengarden.com/?cssfile=003%2F003%2Ecss) I particularly liked).


So we hired Dave to do a redesign of FogBugz.


Before:


After:


OK, now all the programmers in the audience are saying, “what? I don’t get it?!” I know. I don’t either. But the new user interface looks and feels, well, 5% more “quality,” whatever the heck that means, and it’s all very nebulous and vague but I can tell ya everyone has been saying it’s the cat’s pajamas, so I’m happy.


**Online Demo**


The [online demo](http://try4.fogbugz.com/) speaks for itself, but we had to do a lot of work to make it possible to host hundreds or thousands of instances of FogBugz in one directory.


In particular we were afraid that one spark of good publicity would result in hundreds or thousands of people setting up new trial accounts simultaneously, which would whack the poor servers and result in a lot of potential customers thinking FogBugz was slow simply because they were trying it on an overloaded server. So we changed the trial signup procedure to include a throttle that, under peak load, allows us to slow down the creation of new trials. Occasionally, it may mean that a potential customer has to wait a few hours to try out the software, but it’s better than everybody having a bad experience.


**The Online Movie**


One product I just can’t stop singing the praises of is [Camtasia Studio](http://www.techsmith.com/products/studio/default.asp), by the folks at TechSmith in Okemos, Michigan. It lets you “film” your computer screen, all in software of course, then edit the film, add narration, then squeeze it down to a very compact flash movie you can put on the web. This is a beautiful piece of software. It does exactly what you need, works the first time, and comes with great documentation you’ll never need.


I used Camtasia Studio to record [an introduction to FogBugz 4.0 in movie form](http://www.fogcreek.com/FogBugz/40movie/40movie.html). The whole project took me about one day. If I had to make another movie, it would only take a couple of hours, as I learned many tricks along the way. For example the first recordings I made sounded terrible. Our offices are in New York City and a lot of street noise drifts up to us here on the 18th floor. It’s not enough to notice during the day but when you’re trying to record something, the muted sirens in the background are shockingly unprofessional! To make things worse, we have hardwood floors throughout the office and don’t have those yucky acoustic tiles on the ceiling, so the office is acoustically live in a way which made the movie sound like I was in a big abandoned warehouse, down by the river, waiting for Kojak to arrive with a lollypop.


I gathered up all the rugs and pillows I could find at Fog Creek and moved them all into my office. With a big rug on the floor and giant sofa pillows lining every wall, the sound quality was *vastly* improved. In fact my office was so pleasant with all the sound-absorbing stuff that I realized it’s not enough to have quiet offices; you want to have acoustically dead offices as well. For our next office space I think I’ll specify thick carpeting for the private offices, even if it’s not as cool as wood floors. We’re seriously considering hiring [Aviva Stanoff](http://www.avivastanoff.com/) to come up with some kind of framed pillow arty thing to put on the walls to deaden the sound even more.


**The Website**


Um, [yeah](http://www.fogcreek.com/FogBugz/index.html). We threw this together at the last minute. We did manage to find a few good-looking FogBugz customers to give us testimonials so we could replace the crappy stock photography with pictures of actual humans, and Dmitri found a great old picture of some craftsmen making violins. I spent a lot of time putting together a [screenshot tour](http://www.fogcreek.com/FogBugz/40tour/01.html) because a lot of people look for the screenshots first when they’re learning about a new product.


**FogBugz, The Book**


Different people learn different ways. I always want to dive in and start using a product, but some people prefer learning about a product in a classroom, and others prefer to read a book. I’ve even heard people say they won’t use any development tool until there’s a genuine book about it in bookstores. A real book from a real publishing house is one of those things that makes a product “feel” real.


I had been incredibly impressed by Mike Gunderloy’s classic book [Coder to Developer](http://www.codertodeveloper.com/), about all the things that a full-fledged software developer needs to do above and beyond the basic work of writing lines of code, and Mike has been working with FogBugz since version 1.0, so I persuaded him to write a book, which [Apress](http://www.apress.com/) published.


The reason I like [Mike’s book](http://www.fogcreek.com/FogBugz/40PainlessProjectManageme.html) so much is that it’s not just a rehash of the online documentation, which is pretty detailed to begin with, and it’s not just a big wasted list of steps for filling out dialog boxes. Instead Mike’s book focuses on how to manage software projects using FogBugz effectively, so it adds a lot of useful material. In fact I liked the book so much I ordered a thousand copies, which we’re selling along with FogBugz. Probably 20% of new FogBugz customers buy a copy or two of the book, and it’s also good to have around as a handout for potential large customers.


(By the way, if you’re a Mike Gunderloy fan like me, you’ll be delighted to see that he has recently relaunched his website [Larkware](http://www.larkware.com/) as a daily source of news about programming technologies.)


**FogBugz, The CD-ROM**


One of the nicest things about selling software is that there *is* no physical product, but I’m kind of old fashioned, and whenever I buy software online, if there’s an option to receive a physical disk, I usually take it, just so I can have something physical up on the shelf that I can find if I ever need to reinstall the software. I can’t tell why but somehow having the option of a physical product makes the software feel more tangible and therefore worth more money. It’s a great mystery to me why this is the case but I’m sure anthopologists would not be surprised.


Since we already decided to sell physical products, i.e., the book, we needed to get set up for shipping physical products anyway, which meant inventory, postage meters, UPS accounts, and all that stuff, so I figured, against my better judgement, that it couldn’t hurt to make CD-ROMs available as well.


The FogBugz CD-ROM is entirely manufactured at Fog Creek, using a robotic combination CD-ROM recorder/inkjet printer which records and prints the CD-ROM without human intervention. We put them in DVD boxes, which are a little bit classier than CD-ROM Jewel Boxes. So far it looks like we’re shipping two or three a week to customers who opt to pay an extra ten bucks for physical media. It’s hard to tell if it’s worth it. Somehow I think that having a real packaged product makes FogBugz “seem” more real even if almost nobody orders it, but again, maybe that’s just me being old fashioned.


Tomorrow, the aftermath!
