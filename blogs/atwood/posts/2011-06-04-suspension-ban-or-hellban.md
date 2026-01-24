---
title: "Suspension, Ban or Hellban?"
date: 2011-06-04
url: https://blog.codinghorror.com/suspension-ban-or-hellban/
slug: suspension-ban-or-hellban
word_count: 1117
---

For almost eight months after launching Stack Overflow to the public, we had no concept of banning or blocking users. Like any new frontier town in the wilderness of the internet, I suppose it was inevitable that we’d be obliged to build a jail at some point. But first we had to come up with some form of *government*.


Stack Overflow was always intended to be a democracy. With the [Stack Exchange Q&A network](http://stackexchange.com/sites), we’ve come a long way towards that goal:

- We create new communities through the open, democratic process defined at [Area 51](http://area51.stackexchange.com/).
- Our communities are maintained and operated by the most avid citizens within that community. The more reputation you have, the more [privileges you earn](http://blog.stackoverflow.com/2010/10/membership-has-its-privileges/).
- We hold [yearly moderator elections](http://blog.stackoverflow.com/2010/12/stack-exchange-moderator-elections-begin/) once each community is large enough to support them.


We strive mightily to build self organizing, self governing communities of people who are passionate about a topic, whether it be [motor vehicles](http://mechanics.stackexchange.com/) or [homebrewing](http://homebrew.stackexchange.com/) or [musical instruments](http://music.stackexchange.com/), or… *whatever*. Our general philosophy is *power to the people*.


![](https://blog.codinghorror.com/content/images/2025/04/image-527.png)


But in the absence of *some* system of law, the tiny minority of users out to do harm – intentionally or not – eventually drive out all the civil community members, leaving behind a lawless, chaotic badland.


Our method of dealing with disruptive or destructive community members is simple: **their accounts are placed in timed suspension.** Initial suspension periods range from 1 to 7 days, and increase exponentially with each subsequent suspension. We prefer the term “timed suspension” to “ban” to emphasize that we *do* want users to come back to their accounts, *if* they can learn to refrain from engaging in those disruptive or problematic behaviors. It’s not so much a punishment as a time for the user to cool down and reflect on the nature of their participation in our community. (Well, at least in theory.)


Timed suspension works, but much like democracy itself, it is a highly imperfect, noisy system. The transparency provides ample evidence that moderators aren’t secretly whisking people away in the middle of the night. But it can also be a bit too... *entertaining* for some members of the community, leading to hours and hours of meta-discussion about who is suspended, why they are suspended, whether it was *fair*, what the *evidence* is, how we are *censoring* people, and on and on and on. While a certain amount of introspection is important and necessary, it can also become a [substitute for getting stuff done](https://blog.codinghorror.com/meta-is-murder/). This might naturally lead one to wonder – **what if we could suspend problematic users without anyone knowing they had been suspended?**


There are three primary forms of secretly suspending users that I know of:

1. A **hellbanned** user is invisible to all other users, but crucially, not himself. From their perspective, they are participating normally in the community but *nobody ever responds to them*. They can no longer disrupt the community because they are effectively a ghost. It’s a clever way of enforcing the “don’t feed the troll” rule in the community. When nothing they post ever gets a response, a hellbanned user is likely to get bored or frustrated and leave. I believe it, too; if I learned anything from reading [The Great Brain](http://www.amazon.com/dp/0803725906) as a child, it’s that the silent treatment is the cruelest punishment of them all.

I’ve always associated hellbanning with the Something Awful Forums. Per [this amazing MetaFilter discussion](http://ask.metafilter.com/117775/What-was-the-first-website-to-hide-trolls-activity-to-everyone-but-the-troll-himself), it turns out the roots of hellbanning go much deeper – all the way back to an early Telnet BBS system called [Citadel](http://anticlimactic.retrovertigo.com/), where the “problem user bit” was introduced around 1986. Like so many other things in social software, it keeps getting reinvented over and over again by [clueless software developers](https://web.archive.org/web/20110707035014/http://www.wired.com/techbiz/people/magazine/17-04/st_thompson) who believe they’re the first programmer smart enough to figure out how people work. It’s supported in most popular forum and blog software, as documented in the [Drupal Cave module](http://drupal.org/project/cave).(There is one additional form of hellbanning that I feel compelled to mention because it is particularly cruel – when hellbanned users can see only themselves *and other hellbanned users*. Brrr. I’m pretty sure Dante wrote a chapter about that, [somewhere](http://en.wikipedia.org/wiki/Inferno_(Dante)).)
2. A **slowbanned** user has delays forcibly introduced into every page they visit. From their perspective, your site has just gotten terribly, horribly slow. And stays that way. They can hardly disrupt the community when they’re struggling to get web pages to load. There’s also science behind this one, because per [research from Google and Amazon](https://blog.codinghorror.com/speed-still-matters/), every page load delay directly reduces participation. Get slow enough, for long enough, and a slowbanned user is likely to seek out greener and speedier pastures elsewhere on the internet.
3. An **errorbanned** user has errors inserted at random into pages they visit. You might consider this a more severe extension of slowbanning – instead of pages loading slowly, they might not load at all, return cryptic HTTP errors, return the wrong page altogether, fail to load key dependencies like JavaScript and images and CSS, and so forth. I’m sure your devious little brains can imagine dozens of ways things could go “wrong” for an errorbanned user. This one is a bit more esoteric, but it isn’t theoretical; an existing implementation exists in the form of the [Drupal Misery module](http://drupal.org/project/misery).


Because we try to hew so closely to the real world model of democracy with Stack Exchange, I’m not quite sure how I feel about these sorts of reality-altering tricks that are impossible in the world of atoms. On some level, they feel disingenuous to me. And it’s a bit like [wishing users into the cornfield](http://en.wikipedia.org/wiki/It's_a_Good_Life_(The_Twilight_Zone)) with superhuman powers far beyond the ken of normal people. But I’ve also spent many painful hours trapped in public dialog about users who were, *at best*, just wasting everyone’s time. Democracy is a wonderful thing, but efficient, it ain’t.


That said, every community is different. I’ve personally talked to people in charge of large online communities – ones you probably participate in every day – and part of the reason those communities *haven’t* broken down into utter chaos by now is because they secretly **hellban** and **slowban** their most problematic users. These solutions do neatly solve the problem of getting troublesome users to “voluntarily” decide to leave a community with a minimum of drama. It’s hard to argue with techniques that are proven to work.


I think everyone has a right to know what sort of jail their community uses, even these secret, invisible ones. But keep in mind that whether it’s timed suspensions, traditional bans, or exotic hellbans and beyond, the goal is the same: civil, sane, and safe online communities for everyone.

[community management](https://blog.codinghorror.com/tag/community-management/)
[stack overflow](https://blog.codinghorror.com/tag/stack-overflow/)
[moderation](https://blog.codinghorror.com/tag/moderation/)
[user privileges](https://blog.codinghorror.com/tag/user-privileges/)
[self-governing](https://blog.codinghorror.com/tag/self-governing/)
