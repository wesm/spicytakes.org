---
title: "Single Minute Exchange of Dies"
date: 2006-08-03
url: https://www.kalzumeus.com/2006/08/04/single-minute-exchange-of-dies/
slug: single-minute-exchange-of-dies
word_count: 1222
---


I studed Toyota way back during my study-abroad year in Kyoto as a college student, but hadn’t heard about [Single Minute Exchange of Dies](http://profitdesk.com/content/2006/07/21/switching-out-the-dies/). The idea is very relevant to uISVs, but we might understand it better as “implementing scaleable systems”.


Briefly, a die is a big nasty piece of manufacturing equipment. As with all equipment, they have faults and failures. As with all equipment on an assembly line, when they are down the assembly line gets held up. As a result, there is a strong temptation to let the faults go to avoid killing the line, which results in slightly malformed components, which results in lower quality of output. Toyota had (and, to my knowledge, has) a corporate culture which was absolutely intolerant of defects, and they invented a system for system improvement. The system improvements they got from their system let them change dies in minutes instead of in days, which gave them the flexibility to yank them any time they performed sub-optimally, which lead to Toyota cars being some of the highest-quality in the world, which helped lead to US politicians campaigning in Michigan being the only people who really enjoy American cars. (OK, I suppose Japanese mobsters count, too.)


This is very relevent to the article which I posted yesterday regarding support and scalability. That is the beautiful thing about systems: systems scale. If you sell a car and the car breaks down, you get to have somebody fix it, and every additional break-down costs you additional fixing. Or, you could just sell cars which don’t break down. If you sell a piece of software that crashes, you have to answer an email “Why did my software crash?” Or, you could stop your software from crashing. Do you have systems in place which make this easy for you? Because you should: work on your system once and you keep getting value out of it for an extended period of time, without inputting more work. Here’s some systems you should probably have working for you (the 3rd one is directly responsive to “Uh oh, I spend too much time on support”, and its something that I could use some serious improve on myself):


1) **Order management**: For a B2C company I cannot imagine a reason why you would not totally automate the order process. Customer pays you, customer gets license key, you wake up in the morning a little richer. I use [e-junkie](http://www.e-junkie.com) for this and the service is brilliant: for $5 a month and Paypal fees they take care of the entire problem for me. Setting up e-junkie took an initial investment (about an hour of my time, plus time to research the tradeoffs & etc) and pays me dividends for every order: customers get instantaneous service, which is a selling point, and when my order volume (hopefully) increases from the current one-per-week I won’t be wasting my time checking that Paypal payments were received properly and manually mailing out CD keys.


2) **Systems to support marketing**: How easy is it for you to get a link to the most linkable page on your website? You’ve probably gotten most of yours from hustling for them — find 5 pages in a related niche, pitch your idea to 5 webmasters, get maybe one link from a PR2 site? Well, thats certainly one way to do things, and when you’re bootstrapping you’ll need to do it. But you can implement a system to get yourself links in 5 seconds. Watch:


> Hiya, I hope you like my blog about uISVs. If you do, please feel free to share it with your friends! If you have a web page, blog, or want to send a link via email, just copy and paste the following: <a href=”http://microisvjournal.wordpress.com”>MicroISV on a Shoestring</a> . That will create a clickable link which your friends can follow back to my site. Thanks much for your interest!


One page on my product’s site offers some information of interest to elementary school teachers. It has an exhortation very similar to the one above. 20% of the people who land on that page convert so I rather like it when people see it. Roughly one out of every 200 visitors sends the link out. Multiply that by 1000 visitors per week and I get 5 links, some of them from decently influential sites, for free. Did I have to hustle and write 25 emails? No, the day I got a link from a PR5 ESL site I was busy doing the important things for my uISV’s success: drinking cocoa and reading the [best series of books about the Napoleonic Wars fought with dragons ever written](http://www.temeraire.org/).


If you’re willing to spend more than 5 seconds, you can incorporate scripts to mail a friend, buttons which submit your site to digg or one of the other social-bookmarkers, Javascript buttons to bookmark a site automagically, etc etc. I lack the technical skill to do some of these and my target audience does not quite live in the Valley’s Web 2.0-induced echo chamber, but my two sentence HTML tutorial worked wonders.


3) **Build systems**: Here’s one place where I’m woefully inadequate. Suppose I get it in my head to change the text in a single dialog box in my program. I hit Ctrl-S to save the resource file. Now here’s what I have to do:


1) Run my program and verify that the dialog has not broken (5 clicks).


2) Export the JAR from Eclipse (roughly 6 clicks).


3) Run my obfuscation program on the exported JAR. (4 clicks)


4) Run my wrapper program to turn the JAR into an exe (4 clicks)


5) Copy the exe into the distribution directory (4 clicks).


6) Run my installer build script (2 clicks).


7) Install my program (4 clicks).


8) Visually inspect that nothing has broken (~10 clicks).


9) Copy the new installer to my web server (4 clicks).


10) Delete one file from the webserver and copy two. (6 clicks).


Thats in the vicinity of **fifty** mouse clicks, taking 15-30 minutes, to make a one-character change to my published executable. As you can reasonably expect, this forces me to make my changes in bunches, where there’s even more likelihood that something goes wrong, and where neat new features which are tested and done sit on my local machine for a week (3 at the moment and counting, include one which fixes the poor architecture choice which caused my first return and which is continuing to spoil customer experiences) because I can’t spare the time at the moment.


What I really need to do is break down and learn how to actually use an ANT build script and unit tests to do this whole thing in one-tenth the time. Build in one click, observe unit-tests function, give it a visual inspection myself, deploy in one click. Then I won’t be producing the computer equivalent of overly-expensive breakdown-prone cars with the fuel efficiency and aerodynamics of aircraft carriers*.


*This metaphor has been brought to you by Dave Barry, in his seminal work [Dave Barry Does Japan](http://www.amazon.com/gp/product/0449908100/sr=8-1/qid=1154676764/ref=pd_bbs_1/102-9668698-6052133?ie=UTF8), which won’t teach you very much about Japan but will cause you to bust a gut laughing.


[Edit: I tweaked a paragraph to make the connection between SMED and the software support scenario more explicit, and linked Dave Barry Does Japan.]
