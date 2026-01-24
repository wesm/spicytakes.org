---
title: "I Repeat: Do Not Listen to Your Users"
date: 2008-02-25
url: https://blog.codinghorror.com/i-repeat-do-not-listen-to-your-users/
slug: i-repeat-do-not-listen-to-your-users
word_count: 1167
---

Paul Buchheit on [listening to users](http://paulbuchheit.blogspot.com/2008/02/most-import-thing-to-understand-about.html):


> I wrote the first version of Gmail in one day. It was not very impressive. All I did was stuff my own email into the Google Groups (Usenet) indexing engine. I sent it out to a few people for feedback, and they said that it was somewhat useful, but it would be better if it searched over their email instead of mine. That was version two. After I released that people started wanting the ability to respond to email as well. That was version three. That process went on for a couple of years inside of Google before we released to the world.
> Startups don’t have hundreds of internal users, so it’s important to release to the world much sooner. When FriendFeed was semi-released (private beta) in October, the product was only about two months old (and 99.9% written by two people, Bret and Jim). We’ve made a lot of improvements since then, and the product that we have today is much better than what we would have built had we not launched. The reason? **We have users, and we listen to them, and we see which things work and which don’t.**


Listening to users is a tricky thing. Users often don’t know what they want, and even if they did, the communication is [likely to get garbled](https://blog.codinghorror.com/every-user-lies/) somewhere between them and you. By no means should you *ignore* your users, though. Most people will silently and forever walk away if your software or website doesn’t meet their needs. The users who care enough to give you feedback deserve your attention and respect. They’re essentially taking it upon themselves to design your product. If you don’t listen attentively and politely respond to all customer feedback, you’re setting yourself up for eventual failure.


It’s rude not to listen to your users. So how do we reconcile this with the first rule of usability – [**Don’t Listen to Users**?](https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/)

kg-card-begin: html

> To discover which designs work best, watch users as they attempt to perform tasks with the user interface. This method is so simple that many people overlook it, assuming that there must be something more to usability testing. [It] boils down to the basic rules of usability:
> Watch what people actually do.
> Do not believe what people *say* they do.
> Definitely don’t believe what people predict they *may* do in the future.

kg-card-end: html

I think Paul had it right, but it’s easy to miss. The relevant phrase in Paul’s post is **we see which things work**, which implies measurement and *correlation*. There’s no need to directly watch users (although it never hurts) when you have detailed logs showing what they actually did. Collect user feedback, then correlate it with data on what those [users are actually doing](https://www.nngroup.com/articles/top-10-application-design-mistakes/):


> Don’t just implement feature requests from “user representatives” or “business analysts.” The most common way to get usability wrong is to **listen to what users say rather than actually watching what they do.** Requirement specifications are always wrong. You must prototype the requirements quickly and show users something concrete to find out what they really need.


Acting on user feedback alone is questionable. No matter how well intentioned, you’re guessing. Why guess when you can take actions based on cold, hard data? Acting on user feedback *and* detailed usage metrics for your application or website – that’s the gold standard.


Consider Valve software’s [hardware survey](http://www.steampowered.com/status/survey.html). A particularly vocal set of gamers might demand support for extremely high widescreen resolutions such as 1920 x 1200 or 2560 x 1600. Understandable, since they’ve spent a lot of money on high-end gaming rigs. But what resolutions do most people actually play at?


![](https://blog.codinghorror.com/content/images/2025/04/image-5.png)


Based on this survey of 1.3 million Steam users, about 10% of gamers have high resolution, widescreen displays. There are other reasons you might want to satisfy this request, of course. Those 10% tend to be the most dedicated, influential gamers. But having actual data behind your user feedback lets you vet the actions you take, to ensure that you’re spending your development budget wisely. The last thing you want to do is fritter away valuable engineering time on features that almost nobody is using, and having usage data is how you tell the difference.


Valve also collects an exhaustive set of gameplay statistics for their games, such as [Team Fortress 2](http://en.wikipedia.org/wiki/Team_Fortress_2).


> We’ve traditionally relied on things like written feedback from players to help decide which improvements to focus on. More recently, Steam has allowed us to collect more information than was previously possible. TF2 includes a reporting mechanism which tells us details about how people are playing the game. We’re [sharing the data we collect](http://steampowered.com/status/tf2/tf2_stats.php) because we think people will find it interesting, and because we expect to spot emergent problems earlier, and ultimately build better products and experiences as a result.


The very first graph, of **time played per class**, illustrates one problem with Team Fortress 2 in a way that I don’t think any amount of player feedback ever could.

kg-card-begin: html


| Scout | 17.5% |
| Engineer | 17.3% |
| Soldier | 15% |
| Demoman | 10.5% |
| Sniper | 10.1% |
| Heavy | 8.5% |
| Spy | 8% |
| Pyro | 7% |
| Medic | 5.5% |


kg-card-end: html

The medic class is severely underrepresented in actual gameplay. I suppose this is because Medics don’t engage in much direct combat, so they’re not as exciting to play as, say, a Demoman or Soldier. That’s unfortunate, because the healing abilities of the medic class are frequently critical to winning a round. So what did Valve do? They released a giant set of [medic-specific achievements](https://web.archive.org/web/20080229021058/http://www.ubercharged.net/2008/01/29/new-medic-achievements-already-hidden-on-your-pc/) to encourage players to choose the Medic class more often. That’s iterative game design based on actual, real world gameplay data.


Using detailed gameplay metrics to refine game design isn’t new; Bungie ran both Halo 2 and 3 through [comprehensive usability lab tests](https://web.archive.org/web/20081016215545/http://www.wired.com/gaming/virtualworlds/magazine/15-09/ff_halo?currentPage=all).


![](https://blog.codinghorror.com/content/images/2025/04/image-4.png)


> In April, Bungie found a nagging problem with Valhalla, one of Halo 3’s multiplayer levels: Player deaths (represented in dark red on this “heat map” of the level) were skewing toward the base on the left, indicating that forces invading from the right had a slight advantage. After reviewing this image, designers tweaked the terrain to give both armies an even chance.


Again – try to imagine how you’d figure out this fundamental map imbalance based on player feedback. I’m not sure if it’s even possible.


**Make sure your application or website is capturing user activity in a useful, meaningful way**. User feedback is important. Don’t get me wrong. But never take action *solely* based on user feedback. Always have some kind of user activity data to corroborate and support the valuable user feedback you’re getting. Ignoring your user feedback may be setting yourself up for eventual failure, but blindly acting on every user request is *certain* failure.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user feedback](https://blog.codinghorror.com/tag/user-feedback/)
[product iteration](https://blog.codinghorror.com/tag/product-iteration/)
