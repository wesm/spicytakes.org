---
title: "Foreword to Painless Project Management with FogBugz, by Mike Gunderloy"
date: 2005-02-11
url: https://www.joelonsoftware.com/2005/02/11/foreword-to-painless-project-management-with-fogbugz-by-mike-gunderloy/
word_count: 1206
---


There’s a restaurant in my New York City neighborhood called Isabella’s that’s always packed.


Downstairs, upstairs, at the sidewalk cafe, it’s mobbed. And there are large crowds of happy yuppies out front, waiting 45 minutes for a table when they can clearly see other *perfectly good* restaurants right across the street which have plenty of tables.


It doesn’t matter when you go there. For Sunday brunch, it’s packed. Friday night? Packed, of course. But go on a quiet Wednesday night at 11:00 PM. You’ll get a table fairly quickly, but the restaurant is still, basically, packed.


Is it the food? Nah. Ruth Reichl, restaurant reviewer extraordinaire from the New York Times, [dismissed it thusly](http://travel2.nytimes.com/top/features/travel/destinations/unitedstates/newyork/newyorkcity/restaurant_details.html?vid=1002207988079): “The food is not very good.”


The prices? I doubt anyone cares. This is the neighborhood where Jerry Seinfeld bought Isaac Stern’s apartment with views over *two* parks.


Lack of competition? What, are you serious? This is Manhattan!


Here’s a clue as to why Isabella’s works. In ten years living in this neighborhood, I still go back there. All the time. Because they’ve never given me a single reason not to.


That actually says a lot.


I never go to a certain fake-Italian art-themed restaurant, because once I ate there and the waiter, who had gone beyond rude well into the realm of actual cruelty, mocking our entree choices, literally chased us down the street complaining about the small tip we left him.


I stopped going to another hole-in-the-wall pizza-pasta-bistro because the owner would come sit down at our table while we ate and ask for computer help.


I really, really loved the food at a local curry restaurant with headache-inducing red banquettes and zebra-striped decor. The katori chat was *to die for*. I was even willing to overlook the noxious smell of ammonia wafting up from the subterranean bathrooms. But the food inevitably took an hour to arrive, even when the place was empty, so I just never went back.


But in ten years I can’t think of a single bad thing that ever happened to me at Isabella’s.


Nothing.


So that’s why it’s so packed. People keep coming back, again and again, because when you dine at Isabella’s, nothing will ever go wrong.


Isabella’s is thoroughly and completely debugged.


It takes you ten years to notice this, because most of the time when you eat at a restaurant, nothing goes wrong. It took a couple of years of going to the curry place before we realized they were always going to make us miss our movie, no matter how early we arrived, and we finally had to write them off.


And so, on the Upper West Side of Manhattan, if you’re a restaurant, and you want to thrive, you have to carefully debug everything.


You have to make sure that there’s always someone waiting to greet guests. This person must learn never to leave the maitre d’ desk to show someone to their table, because otherwise the next person will come in and there will be nobody there to greet them. Instead, someone else needs to show patrons to their tables. And give them their menus, right away. And take their coats and drink orders.


You have to figure out who your best customers are—the locals who come on weekday nights when the restaurant is relatively quiet—and give them tables quickly on Friday night, even if the out-of-towners have to wait a little longer.


You need a procedure so that every water glass is always full.


Every time somebody is unhappy, that’s a bug. Write it down. Figure out what you’re going to do about it. Add it to the training manual. Never make the same mistake twice.


Eventually, Isabella’s became a fabulously profitable and successful restaurant, not because of its food, but because it was *debugged*. Just getting what we programmers call “the edge cases” right was sufficient to keep people coming back, and telling their friends, and that’s enough to overcome a review where the New York Times calls your food “not very good.”


Great products are great because they’re *deeply debugged*. Restaurants, software, it’s all the same.


Great software doesn’t crash when you do weird, rare things, because everybody does something weird.


Microsoft developer Larry Osterman, working on DOS 4, once thought he had found a rare bug. “But if that were the case,” he told DOS architect Gordon Letwin, “it’d take a one in a million chance for it to happen.”


Letwin’s [reply](http://blogs.msdn.com/larryosterman/archive/2004/03/30/104165.aspx)? “In our business, one in a million is next Tuesday.”


Great software helps you out when you misunderstand it. If you try to drag a file to a button in the taskbar, Windows pops up a message that says, essentially, “You can’t do that!” but then it goes on to tell you how you can accomplish what you’re obviously trying to do (try it!)


Great software pops up messages that show that the designers have thought about the problem you’re working on, probably more than you have. In FogBugz, for example, if you try to reply to an email message but someone else tries to reply to that same email at the same time, you get a warning and your response is not sent until you can check out what’s going on.


Great software works the way *everybody* expects it to. I’m probably one of the few people left who still closes windows by double clicking in the top left corner instead of clicking on the [x] button. I don’t know why I do that, but it always works, with great software. Some software that I have is not so great. It doesn’t close if you double click in the top left corner. That makes me a little bit frustrated. It probably made a lot of people frustrated, and a lot of those people probably complained, but I’ll bet you that the software developers just didn’t do bug tracking, because they have never fixed that bug and probably never will.


What great software has in common is being *deeply debugged* and the only way to get software that’s deeply debugged is to *keep track of your bugs*.


A bug tracking database is not just a memory aid, or a scheduling tool. It doesn’t make it easier to produce great software, it makes it *possible* to create great software.


With bug tracking, every idea gets into the system. Every flaw gets into the system. Every tester’s possible misinterpretation of the user interface gets into the system. Every possible improvement that anybody thinks about gets into the system.


Bug tracking software captures the cosmic rays that cause the genetic mutations that make your software evolve into something superior.


And as you constantly evaluate, reprioritize, triage, punt, and assign these flaws, the software evolves. It gets better and better. It learns to deal with more and more weird situations, more and more misunderstanding users, and more and more scenarios.


That’s when something magical happens, and your software becomes better than just the sum of its features. Suddenly it becomes *reliable*. Reliable, meaning, it never screws up. It never makes its users angry. It never makes its customers wish they had purchased something else.


And that magic is the key to success. In restaurants as in software.
