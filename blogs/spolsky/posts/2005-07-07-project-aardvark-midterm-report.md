---
title: "Project Aardvark Midterm Report"
date: 2005-07-07
url: https://www.joelonsoftware.com/2005/07/07/project-aardvark-midterm-report/
word_count: 2005
---


Project Aardvark, if you’ve been following along with [the blog](http://www.projectaardvark.com/), is our summer interns’ new product. We’ve got four interns here (three in development, one in marketing) putting together a complete product from beginning to end. Now that they’ve officially announced what it’s all about and we’re about to start the first beta, I can bring you up to date on the project, which is more or less halfway done.


**The Idea**


If you’ve ever tried to help your technologically-challenged uncle fix his computer problems over the phone, you know what a pain in the butt it can be to try to walk him through the fix.


“Click START”


“What?”


“Start. Click Start. It’s in the bottom left.”


“I have C – T – R – L in the bottom left.”


“The bottom left of your *screen*.”


“Oh. OK, I clicked it.”


“OK, now click RUN.”


“What?”


“On the menu that came up. Click RUN.”


“It’s not there.”


“What do you mean it’s not there?”


“It’s not there. I don’t have a RUN.”


“What *do* you see? Read me everything you see”


“Recycle Bin… My Computer… Anna Navratilova J P G…”


“No, on the menu.”


“What *menu?*“


“The menu that came up when you clicked start.”


“When I what?”


This is when you give up and realize that something that could take you 10 seconds to fix in person is about to become a two hour nightmare during which you’ll alienate your family, lose sleep, tie up the phone line while your Auntie Marge is stuck on the turnpike with no gas and can’t get through to your uncle to come rescue her, and curse your lot in life. Just because you’re a programmer doesn’t mean you have to be the help desk for a dozen friends, relatives, and the people in the apartment next door. Does it?


That’s the general idea behind the new Fog Creek CopilotSM service. In a nutshell, you go to copilot.com and get an invitation code. You tell your uncle to go to copilot.com and type in that same invitation code. You each get a little program to download and run. When you run the program, your uncle’s computer screen shows up in a window. When you move your mouse, his mouse moves. When you type something, it appears on his computer. Etc. And now you fix the problem and log off, and peace is restored and your aunt gets home safely and your uncle dances at your wedding instead of boycotting it and holding up unpleasant signs across from the hotel where said wedding is taking place.


**But but but…**


Yes, similar services already exist. That never stopped me before. I’d like to point out that Fog Creek has been doubling in revenues every year mostly thanks to *bug tracking software*, and it’s not like we invented bug tracking software. There are a few things our product will do better than the competition, but mostly we just want the Fog Creek Copilot experience to be shockingly *seamless*. It’ll be totally secure, it’ll be cheap, it’ll be painless, it will work through firewalls *on either side *so you can help mom at home on her firewalled DSL from behind your NAT at work without a hiccup. We even made it so that the little software program you download is totally self-contained, totally pre-configured, and *deletes itself* when you’re done so you can feel more secure about the whole episode. There’s no commitment; you don’t have to sign up or create an account and remember a password; you can even make your uncle pay since, after all, he’s getting the benefit.


For the geeks in the audience, the service uses a highly customized and optimized version of VNC, but it also requires a customized “reflector” service that we’re building which sits outside of any firewalls. The idea is, since you can’t connect *into* mom’s computer which is behind a firewall, she’ll connect *out* to our server, you’ll connect *out* to our server too, and the reflector will forward data back and forth between the two of you.


**How’d you get the idea?**


For the last few years we’ve been supporting FogBugz customers using a similar scheme, although it’s a bit of a pain to set up. Our customers have to follow 7 steps to allow us to control their computers, and we’ve found that walking people through these steps on the phone takes an average of 5 minutes. With the Fog Creek Copilot service we’ll just tell them to check their email and click on a link and *hey presto!* we’re fixing their computer.


So the original idea was to use this for tech support. But when I told the idea to the interns, two out of four said, “yeah, I could use something like that to help my mom.” That’s when we realized there’s a huge world out there of Informal Tech Support… lots of people trying to help Uncle Leo who can’t use products like VNC because of the firewall problem. So we changed the focus of release 1 to be the casual and home user instead of tech support departments.


**The Name**


We had a list of important criteria for the name, but the most important one was that when someone read the name to someone else over the phone, it would be extremely likely that they would get it right. This ruled out names that are weirdly spelled, names which could be easily confused over the phone (for example “m” and “n” are almost impossible to distinguish), and names that have different possible spellings. We went rather too far along the process of investigating the name “Fixant” (complete with a very cool drawing of an ant holding an ethernet cable) before I just got everyone together in a room for a half hour of brainstorming, when we finally hit upon the idea of “Copilot.” I can’t even remember who thought of it. The idea of brainstorming is just that you shout out ideas, which stimulate other people to have ideas, and you put them all up on a whiteboard.


Well, there are a couple of dozen products named Copilot, many with registered trademarks, so our trademark lawyer advised us to use Fog Creek Copilot which would eliminate any possibility of confusion with those other Copilot brand products. The point of trademark laws is that what you’re not allowed to do is create any confusion or potential confusion as to the origin of your product, and sticking “Fog Creek” in front guarantees that, but we have to be religious about always using the full name. I didn’t really mind, having started my career working on products like Microsoft Excel, Microsoft Visual Basic for Applications for Microsoft Excel, etc. etc. After a few weeks on the Microsoft Excel team if you ever saw the word “Excel” without a “Microsoft” in front of it, it looked nekkid.


We bought the domain name for more money than we spent developing the first version of FogBugz, oy gevalt, but it *is* a really good name — easy to spell, pronounce, and it even sort of suggests what the product does, which makes it more memorable.


**The Conference**


For some reason, a long long time ago, I had agreed to give the keynote speech for CFUNITED, a conference about ColdFusion.


“I never used ColdFusion!” I protested.


“Don’t worry. Nobody has. The biggest sponsor of this conference is Microsoft, who have a huge presence trying to get the ColdFusion developers to switch to VB.NET,” the organizers told me.


As luck would have it, the conference timing was perfect for the first feature-complete version of the interns’ code. It gave the team a deadline to work to. At the conference itself, we set up a Fog Creek booth and the interns gave demos to several hundred attendees who wandered by.


This was the first trade show Fog Creek had ever attended. The truth is, a trade show is not a very cost-effective way to reach potential customers. Given the cost of travel, hotels, the booth, a thousand bucks for nice brochures, and everybody taking a week off of work, it’s a really expensive way to get in front of prospects, especially since I can write an article on my website and get in front of 1000 times as many people.


But that’s not really the point: the point is to have *interactive* experiences with your customers. You can try out lots of different pitches and really listen to how people respond to them, which is something you can’t do in non-interactive marketing like web sites and magazine ads. I learned this from Eric Sink, who wrote a great article on the topic, [Going to a Trade Show](http://software.ericsink.com/bos/Trade_Shows.html).


We went down to Washington in two big SUVs with all four interns, one of the FogBugz developers, Brett, who gave demos of FogBugz, and me. Our booth probably looked just a little bit too much like a science-fair exhibit, but, whatever, it was our first attempt. Next time we’ll know to make backdrop posters that stretch right out to the edge of the backdrop which looks a bit more professional, and I’ll remember to bring a lucite brochure dispenser instead of arranging the trifold brochures artfully in the shape of an Aardvark.


But that’s not really a big deal. What was a big deal is that we got to talk to hundreds of potential customers, and, *wow!* the response was just incredible. At the very best, the response we got was, “I need a thousand of these yesterday for my whole team.” Almost everyone was impressed by the product and knew that they wanted to use it. A very small number of people were aware of other competitors and other solutions to the problem, but mostly people gave us very positive feedback. More importantly, after spending two days pitching the product again and again to lots of different people we learned the most effective ways to present it. We learned that the best way to present it was not to start with, “You know VNC?” This drew glassy stares. The best way was to start with a typical remote support scenario. “Your mom calls you up. She says her screen is half grey. You have no idea what the heck she’s talking about.”


**The Beta**


We got back last Friday and immediately started working on the beta. The goal of this summer internship is to be *shipping to paying customers* by the end of the summer, and I didn’t want our interns to go home after “mostly” finishing the code, leaving us permanent employees to debug until next February, so we’re working on a really compressed schedule. Over the next few weeks, we’ve got to:

- Deploy the site and service on our web farm
- Launch a controlled, private beta so a few people can start trying the service and we can figure out if it works in the real world. [Yaron is taking beta applications now](http://www.projectaardvark.com/posts/guez/july/06.html).
- Launch a wider public beta
- Do a round of usability tests in the lab. The nice folks at [TechSmith](http://www.techsmith.com/) have a product for usability testing called [Morae](http://www.techsmith.com/products/morae/default.asp), and they’ll be coming out to New York and helping us organize and run the usability tests. Morae lets you set up a complete usability lab using nothing more than their software and a little webcam
- Start serious QA.


So far we’ve really been hitting the schedule so I’m pretty confident. In the meantime, you can:

- Follow along with the [Project Aardvark blog](http://www.projectaardvark.com/)!
- [Apply for the beta](http://www.projectaardvark.com/posts/guez/july/06.html)! If you’re accepted, you can try the Fog Creek Copilot service yourself!
- If you’re in New York, come to the Project Aardvark Open House! You’ll get free wine and cheese and you can pepper the interns with questions about sockets programming in person. The open house is **Thursday, July 14, 2005, from 5:30 PM – 7:00 PM, **at **Fog Creek Software, 535 8th Ave., 18th Floor, New York.**


****
