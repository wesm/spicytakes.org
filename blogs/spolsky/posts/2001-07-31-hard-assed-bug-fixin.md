---
title: "Hard-assed Bug Fixin’"
date: 2001-07-31
url: https://www.joelonsoftware.com/2001/07/31/hard-assed-bug-fixin/
word_count: 1989
---


Software quality, or the lack thereof, is something everybody loves to gripe about. Now that I have my own company I finally decided to do something about it. Over the last two weeks we stopped everything at [Fog Creek](http://www.fogcreek.com/) to ship a new incremental version of [FogBUGZ](http://www.fogcreek.com/FogBUGZ) with the goal of eliminating all known bugs (there were about 30).


As a software developer, fixing bugs is a good thing. Right? Isn’t it always a good thing?


No!


Fixing bugs is only important when the value of having the bug fixed exceeds the cost of the fixing it.


These things are hard, but not impossible, to measure. Let me give you an example. Suppose you operate a peanut-butter-and-jelly sandwich factory. Your factory produces 100,000 sandwiches a day. Recently, due to the introduction of some new flavors (garlic peanut butter with spicy Habanero jam), demand for your product has gone through the roof. The factory is operating full-out at 100,000 sandwiches, but the demand is probably closer to 200,000. You just can’t make any more. And each sandwich earns you a profit of 15 cents. So you’re losing $15,000 a day in potential earnings because you don’t have enough capacity.


Building a new factory would cost way too much. You don’t have the capital, and you’re afraid that spicy/garlicky sandwiches are just a fad which will pass, anyway. But you’re still losing that $15,000 a day.


It’s a good thing you hired Jason. Jason is a fourteen year old programmer who hacked into the computers that run the factory, and believes that he has come up with a way to speed up the assembly line by a factor of 2. Something about overclocking that he heard on slashdot. And it seemed to work in a test run.


There’s only one thing stopping you from rolling it out. There’s a teeny tiny *wee* little bug that causes a sandwich to be mushed once an hour or so. Jason wants to fix the wee bug. He thinks he can fix it in three days. Do you let him fix it, or do you roll out the software in its bug-addled state?


Rolling out the software three days later will cost you $45,000 in lost profits. And it will save you, um, the cost of raw materials for 72 sandwiches. (In either case Jason will get the bug fixed three days later). Well, I don’t know how much sandwiches cost on *your* planet, but here on Earth, they’re a lot less than $625.


Where was I. Oh yeah. Sometimes it is *not worth fixing a bug.* Here’s another bug that’s not worth fixing: if you have a bug that totally crashes your program when you open gigantic files, but it only happens to your single user who has OS/2 and who, for all you know, doesn’t even use large files. Well, don’t fix it. Worse things have happened at sea. Similarly I’ve generally given up caring about people with 16 color screens or people running off-the-shelf Windows 95 with no upgrades in 7 years. People like that don’t spend much money on packaged software products. Trust me.


But mostly, it’s worth fixing bugs. Even if they are “harmless” bugs, they may reduce the reputation of your company and your product, which, in the long run, will have a significant impact on your earnings. It’s hard to overcome the reputation of having a buggy product. When you do want to do that .01 release, here are some ideas for finding and fixing the *right* bugs: the ones that it is economically worth fixing.


**Step One: Make Sure You Find Out About The Bugs.**


In the case of FogBUGZ, we have two ways of doing that. First, we trap all bugs on our free demo server, capture as much information as we can, and email the whole thing to the development team. That found an awful lot of bugs, which was very cool. For example, we discovered a bunch of people who didn’t enter dates where they were supposed to in the “Fix For” screen. We didn’t even have an error message in that case, we just “crashed” (which, in a web app, just means you got an ugly IIS error instead of what you expected). Oops.


When I worked at Juno, we had an even cooler system in place to collect bugs “from the field” automatically. We installed a handler using TOOLHELP.DLL so that every time Juno crashed, it stayed alive just long enough to dump the stack into a log file before going to its grave. The next time the program connected to the Internet to send mail, it uploaded the log file. During betas, we gathered these log files, collated all the crashes, and entered them into the bug tracking database. This found literally hundreds of crashing bugs. When you have a million users, it is *amazing* what will crash, often because of severe low memory conditions or severely crappy computers (can you spell Packard Bell?) You could have code like this:


> int foo( object& r )
> {
>     r.Blah();
>     return 1;
> }


and you would get crashes there because the r reference was NULL, even though that’s completely impossible, there’s no such *thing* as a NULL reference, C++ guarantees it, and you don’t have to believe me but when you wait long enough and have millions of users and religiously collect their stack dumps, you will find crashes in places like that and you won’t believe your eyes. (And you won’t fix them. Cosmic rays, man. Get a new computer and this time *don’t* install every cool shareware taskbar lint gizmo you find. *Sheesh.*)


The other thing we do is consider each and every tech support call to be evidence of a bug. When we take the call, we try to figure out what we could have done to eliminate it. For example, the old FogBUGZ Setup used to assume that FogBUGZ would run under the anonymous Internet user account. That was a good assumption 95% of the time, and a bad assumption 5% of the time, but every one of those 5% cases ended up in a call to our support line. So we modified Setup to prompt for an account.


**Step Two: Make Sure You Get Economic Feedback**


You may not be able to figure out *exactly* how much it’s worth to fix each bug, but there’s something you *can* do: charge the “cost” of tech support back to the business unit. In the early nineties there was a financial reorganization at Microsoft under which each product unit was charged for the full cost of all tech support calls. So the product units started insisting that PSS (Microsoft’s tech support) provide lists of Top Ten Bugs regularly. When the development team concentrated on those, product support costs plummeted.


This is a bit in contradiction with the new trend of letting the tech support department pay for its own operation, something that most large companies do. At Juno tech support was expected to break even by charging people for tech support. By moving the economic burden of bugs onto the users themselves, you lose what limited ability you might have had to detect the damage they were causing. (Instead you get irate users who resent having to pay for *your* bug, who tell their friends, and you can’t even measure how much that costs you. To be fair to Juno, the product itself was free, so stop yer bitchin.)


One way of resolving the two is to *not *charge the user when the support call was caused by a bug in your own product. Microsoft does this, and it’s quite nice, and I’ve never paid for a call to Microsoft  Instead, charge the $245 or whatever one developer incident costs these days back to the product unit. That blows away their profit completely for the product they sold you (several times over), and creates exactly the right economic incentives. Which reminds me of one reason DOS games were a *terrible* business… to get them to look good and run fast, you usually  needed strange video drivers, and a single tech support call about the video drivers would blow away the profit you could make from *20* copies of your product, assuming Egghead and Ingram and the ad on MTV hadn’t already guzzled away *all* your earnings.


**Step Three: Figure Out What It’s Worth To You To Fix Them All.**


At Fog Creek Software, well, we’re a tiny company (except in our own minds), and the development team just takes the tech support calls. The cost was running about 1 hour per day, which, based on our consulting rates, is somewhere around $75000 a year. We were pretty confident that we could get that down to 15 minutes a day by fixing all known bugs.


Using very sloppy numbers, here, that means that the net present value of the savings would be about $150,000. That justifies 62 days of work: if you can do it in less than 62 person-days, it’s worth doing.


Using the handy estimation feature built into FogBUGZ, we calculated that it would take 20 person-days (two people two weeks) to fix everything – that’s $48,000 “spent” for a return of $150,000, which is a great return on investment *just on the basis of the tech support savings*. (Observe that you could substitute the cost of programmer’s salaries and overhead instead of our consulting rate and get the same 3:1 result, since it cancels out).


I haven’t even begun to count the value from having a better product, but I can start doing that, too. We had 55 crashes on the demo server during the month of July with the old code, representing 17 distinct users. You have to imagine that at least *one* of those people decided not to buy FogBUGZ because they thought it was buggy when they ran the demo (although I don’t have real statistics for that.) In any case the lost sales was probably costing us somewhere between $7,000 and $100,000 in present value. (If you were serious enough, it wouldn’t be too hard to get a real number).


Next question. Can you charge more for a less buggy product? That would add a whole bunch of value to debugging. I suspect that at the extremes, bug count does affect price, but I am hard pressed to think of an example from the world of packaged software where this has been the case.


**Please Don’t Beat Me Up!**


Inevitably people read essays like this and come to silly conclusions, like, Joel doesn’t think you should fix bugs. In fact I think that for most of the kinds of bugs that most people fix, there’s a clear return on investment. But there may be an even higher monetary value to doing something *other* than fixing every last bug. If you have to decide between fixing the bug for OS/2 guy and adding a new feature that will sell 20,000 copies of your software to General Electric, well, sorry, OS/2 guy. And if you’re dumb enough to think that it’s *still* more important to fix OS/2 than to add the GE feature, maybe your competitors won’t be and you’ll be out of business.


With all that said, I’m optimistic at heart, and I believe that there is a lot of hidden value to producing very high quality products that is not very easy to capture. Your employees will be prouder. Fewer of your customers will send you back your CD in the mail after microwaving it and chopping it to bits with an ax. So I tend to err on the side of quality (indeed, we fixed *every known bug* in FogBUGZ, not just the big bang ones) and take pride in that, and feel confident, by the complete elimination of errors from the demo server, that we have a rock-solid product.
