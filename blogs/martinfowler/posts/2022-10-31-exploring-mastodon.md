---
title: "Exploring Mastodon"
description: "With the current uncertainty over Twitter, I'm starting to explore using Mastodon"
date: 2022-10-31T00:00:00
tags: ["writing", "internet culture"]
url: https://martinfowler.com/articles/exploring-mastodon.html
slug: exploring-mastodon
word_count: 6687
---


I've been a heavy user of Twitter over the last decade, and while Musk's
    purchase of Twitter hasn't got me running for the exit, it has prompted me
    to take a look at possible alternatives should Twitter change into something
    no longer worthwhile for me. The obvious alternative is for me to explore
    the Fediverse with **[my new
    Mastodon account](https://toot.thoughtworks.com/@mfowler)**. As I explore using Mastodon, I'll make some notes here so
    that others can learn from my explorations.


I'm currently cross-posting all my tweets to my Mastodon feed, so you can
    follow on whichever system you prefer.


For an introduction to Mastodon and the Fediverse, my current favorite
    starting point is by [Jeff
    Jarvis](https://medium.com/whither-news/on-joining-mastodon-d539eed5e41a), and for a bit more depth [Danielle
    Navarro](https://blog.djnavarro.net/posts/2022-11-03_what-i-know-about-mastodon). For tips on how to do common tasks, I turn to [Fedi.Tips](https://fedi.tips/). Read Julien's compelling argument on why
    [your organization should run its own Mastodon server](https://martinfowler.com/articles/your-org-run-mastodon.html)


## Earlier Memos 
▶


### Starting out by following some folks (01 November 2022) 
▶


I spent a bit of time yesterday taking my first steps into the world of Mastodon.


Unlike Twitter, Mastodon is a federated system. So for most people, the first step in using Mastodon is to choose which server to use. In my case, I donât need to make this decision since my colleagues in Thoughtworks have set up our own mastodon instance. An admin for this, [Julien Deswaef](https://toot.thoughtworks.com/@judeswae) set me up with an account back in April, when the first rumblings of the Muskover occurred.


My intention at this point is to set up my Mastodon account as an automatic cross-post from my twitter account. That way any Mastodon user can follow me on Mastodon to see my twitter feed rather than do it via Twitter. My thinking is that Iâll then monitor my Mastodon followers and if enough followers appear, Iâll think about doing something more sophisticated.


One of my first challenges was to figure out how following works, to understand this I needed to get a handle on the nature of Mastodonâs federated nature. If I look at an account like Julienâs, which is on the same instance as me, then following is easy, I just navigate to his account page and hit the âFollowâ button.


But if I do that on an account on mastodon.social, I get this complicated response


I need to copy that URL, and then paste it into the Search box on my page. I tried that this morning and got no response, which was rather frustrating. Eventually, after asking for help from Julien, I did get it working. We suspect that mastodon.social was under heavy load and just responding too slowly. Iâve also noticed some times I try searching for a URL of the form `https://mastodon.social/@RonJeffries` and get no response, but then try to search for `@RonJeffries@mastodon.social` and it does work.


Once the remote user showed up, I could just hit the button to follow, but there was still an issue. My new mastodon-friend didnât show up in the list of Follows and Followers, so I tried to follow again and saw this


On reading around I figured out (and Julien confirmed) that this means Ron has set his account up so that he has to approve followers. The hourglass like icon indicates that a follower request has been sent to him, but he hasnât approved it yet. I havenât set that, so if you try to follow me you should get an immediate response.


## Local and Federated timelines


When I look at the default UI, I see things that make sense from a Twitter background, such as Notifications and Direct Messages. But I also see two odd things: Local and Federated.


The **Local timeline** shows every post made by anyone on my own instance. This makes some sense in my case as my local instance has a natural community - weâre all employees of Thoughtworks. It  makes much less sense if youâre on a big instance like mastodon.social. This feature encourages the idea of using lots of small instances rather than a few giant ones. Itâs a reason for users to look for a smaller community instance rather than just going to a big one, which is why some Mastodon users suggest new people should avoid mastodon.social.


The **Federated timeline** takes this a step further, it includes all posts on the local timeline and adds all posts by anyone that the local instance follows. Again this may be handy for people with a small community instance, but is less useful for bigger servers.


## Reading more documentation


There isnât a huge amount of stuff to act as a guide to Mastodon, and much of what is out there is rather old (as always, check the date when reading about a technology that is rapidly changing). The [official documentation](https://docs.joinmastodon.org) is pretty decent. I enjoyed Scott Feeneyâs discussion of [4 Twitter features Mastodon is better for not having](https://scott.mn/2022/10/29/twitter_features_mastodon_is_better_without/). It provided some insight into the thinking behind some of the differences between how it works compared to twitter.


### Verification on Mastodon (01 November 2022) 
▶


Twitter has a facility for verifying that well-known people (for Twitterâs value of âwell-knownâ) can have their account verified. Such accounts are shown with a blue check mark.


I got my blue check mark several years ago, and donât remember much about it. I donât think I asked for it, I think Twitter approached me. I donât pay anything for it, and I donât remember what they did to verify me. They donât verify everyone, I suppose they did me partly due to having hundreds of thousands of followers, and partly because of being well-known in the software development world.


Due to this rather opaque way of choosing who to give out the blue check marks, Twitter verification has become somewhat fraught. Itâs often seen as a status symbol. But people who donât have it may have genuine problems with others spoofing them on Twitter.


Mastodonâs approach to verification is rather different. Since itâs a decentralized system, thereâs no single mechanism for verification. The way I see it, verification is up to each Mastodon instance. Iâm pretty well verified on toot.thoughtworks.com because Thoughtworks is essentially verifying me by allowing me to have an account there. (As it happens, the only way to access an account at toot.thoughtworks.com is to use your corporate login.)


If Mastodon takes off, we could imagine this approach spreading widely. If a journalist at The Economist needed a verified account, then The Economist could run their own Mastodon instance, where anyone on it would be effectively verified by that newspaper. Unlike Twitter, which needs to scale to a vast amount of users, a Mastodon instance can be small enough for the organization running it to verify its members.


On the other hand, big instances like mastodon.social may not do any verification at all, because itâs just too complicated for their membership model, or they want to support anonymous accounts. That then becomes part of the choice of an instance - some folks would prefer to join an instance that can give them a viable identity.


Thereâs another approach to verification, which is cross-association with other parts of your web presence. On my home page I have a link to my twitter page, which is a form of verification. It indicates that the web page and the twitter account are controlled by the same user. I verify my email address in a similar way, by mentioning it on my website.


I can do this with Mastodon, of course, but can go a step further. If I include a bit of metadata on my web page, and link to that page on my Mastodon profile, then Mastodon checks for metadata, and marks my link as verified, like this:


Mastodon suggests doing this by adding this link into the body of the page


```
<a rel="me" href="https://toot.thoughtworks.com/@mfowler">Mastodon</a>

```


I did it slightly differently, adding this element to the <head> of the page


```
<link rel="me" href="https://toot.thoughtworks.com/@mfowler">

```


This mechanism allows me to tie together different bits of my online identity, helping them verify each other


### Twitter feed to Mastodon is now working (02 November 2022) 
▶


One of the main things I wanted to do with Mastodon was to replicate my twitter feed there, so that folks who would rather follow me on Mastodon could get everything. To do this, I used [moa.party](https://moa.party). You have to give it credentials to access both your Twitter and Mastodon feeds, which is a little worrisome, but my Mastodon-aware colleagues have used it without problems. It allows cross-posting in either or both directions, but Iâve set it up to just go from Twitter to Mastodon. Itâs pretty simple and seems to be working. So if youâd like to follow my twitter feed from Mastodon, you can now do so.


Iâll be monitoring the follower count for the Mastodon account. If lots of people follow me on Mastodon, Iâll probably do more with it. So following my Mastodon feed is vote for me to put more effort into it. But for the moment, I expect it to be a simple copy of what I post on Twitter.


### Choosing a first instance (02 November 2022) 
▶


An immediate reason why Mastodon is difficult to get into is the choice of instance. With a centralized system like Twitter, there is no choice, you just join the single service. But Mastodon is a federated system, so before you can begin to explore the Fediverse, youâre faced with having to choose a server. This is a tricky decision, as without any experience in the Fediverse, you donât have enough information to make a decent choice. The good news is that your initial choice doesnât really matter that much, because Mastodon makes it easy to change servers once you find a better fit.


Youâll notice I used the term âFediverseâ a couple of times there. Fediverse is the name given to the federated universe of servers that communicate using the [ActivityPub](https://activitypub.rocks) protocol, essentially an open standard for social media interoperability. (One that is backed by the W3C.) Mastodon is one kind of server that communicates using ActivityPub, and is the one Iâm currently exploring - I may look into the others later.


Mastodon servers contain facilities that make it easy to [transfer your presence to another Mastodon account](https://fedi.tips/how-to-use-mastodon-and-the-Fediverse-basic-tips/#TransferringYourMastodonAccountToAnotherServer). All you need to do is create a new account, connect the old and new accounts together, download a bunch of files from your old account, and upload them to the new one. This will redirect the old account to the new one and transfer most of data, including your follower lists and blocking information. Old posts stay on the old server, but will indicate the redirection to the new one. My long-time Mastodon colleagues have several transfers under their belts, and it works quite well.


As Iâve been exploring whatâs written about Mastodon, Iâve read several articles that suggest that joining a large instance, such as mastodon.social, is a bad idea. There are certainly good reasons why many people would find they get more value out of a smaller, more focused, server. But as my colleague [Julien Deswaef](https://toot.thoughtworks.com/@judeswae) explained, you shouldnât worry about that at the beginning. Pick one that looks vaguely right and dive in. Once youâve spent some time with Mastodon, youâll have a better appreciation for whatâs valuable to you. This flexibility is all the more important because if Mastodon takes off, I expect there to be lots more servers. In this scenario, most companies and other organizations will set up Mastodon instances - or other nodes in the Fediverse. If then you want to migrate to a smaller server, then itâs easy to do so.


As an advocate of agile software design, I recognize this as an example of the principle that making decisions easy to change [reduces complexity](https://www.martinfowler.com/articles/designDead.html#Reversibility).


### What if Twitter goes MySpace (06 November 2022) 
▶


Now Iâm starting to get a feel for using Mastodon, itâs hard not to speculate on the future. What happens if Twitter goes MySpace and there truly is a mass migration to Mastodon? Iâve always avoided playing the role of futurist. I prefer to describe things that have been done in the past to speculations about possible futures. Such speculations usually end up being wrong, and I expect the same with this one. Still, Iâm enjoying a beautiful fall weekend with friends in New York, so Iâm in the mood for some frivolous entertainment.


The most obvious shift in such a future is that there wonât be one big, central system. Instead of everyone posting on The Single Twitter, there will be lots of servers for people to post from. Iâd expect most companies, government agencies, churches, and ad-hoc organizations will [have their own server](https://martinfowler.com/articles/your-org-run-mastodon.html). This will create not just the global community, but also a collection of smaller groups. The local feed on Mastodon encourages this, as this shows all posts by people on your server - a nice feature if you share server with a bunch of people with a similar interest.


But one lesson we can draw from the history of the internet is that despite this appearance of decentralization, it will still be a centralized world, because centralization tends to bring convenience. There may be a host of instances out there, but the organizations they serve wonât be running them directly. Instead I expect a few service providers will run instances, just as they do for email now.


Indeed Iâd expect that most people wonât use Mastodon. The essence of this federated social future isnât the software the instances run on, but the protocol they use to communicate (ActivityPub). Hosting services will run different kinds of software, designed more with the needs of a hosting service in mind. The Fediverse equivalent of gmail will appear and it will be a proprietary single entity, in many ways not that different from the entity that is Twitter now. (It would be amusing if in this future Twitter ends up having to support the ActivityPub protocol itself, and just be another node in the Fediverse.) But this form of centralization will still be a step forward if the open protocol is the key to tying everything together, just like the open protocols of email allow different hosting services to communicate. That way if I do want to run my own service, I can still plug into the wider social world. (Although the open interconnections of email are often truer in theory than [in practice](https://cfenollosa.com/blog/after-self-hosting-my-email-for-twenty-three-years-i-have-thrown-in-the-towel-the-oligopoly-has-won.html).)


Itâs been said, with some justification, that content management is the product of a social network. How will that look in the federated future? In many ways it becomes easier. Itâs hard for Twitter to control its content when the only relationship it has with its posters is a sign-up over the web. But a companyâs relationship with its employees is much deeper, and the consequences for offensive posts are more than a ban. Posters will be constrained by the expectations of whoever runs their instance. To some degree these expectations go two ways, especially with a social organization.


The most important arbiter of content moderation is the reader. My decisions on who I follow should indicate what content I want to see. That control is undermined by commercial services that maximize engagement to sell attention to advertisers. So if I care about that, I look for instances that wonât hijack my feed with content I donât like. That, however, isnât enough. Thereâs too many ways for bad stuff to slide into peopleâs timeline, so we need robust tools to control it. Mastodon offers a range of blocking measures, allowing me to block both individual users and entire instances if they give bad posters free rein. Instance admins can block other instances that encourage bad behavior. Iâll be fascinated to see how this federated content management will play out in practice.


### Multiple Mastodon Accounts (09 November 2022) 
▶


One of the conventions of Twitter (and Facebook) was a person would have a single Twitter account, following that person would follow âthe whole personâ, mixing posts on different topics that the person was interested. The Fediverse doesnât have such a strong push towards a single person, so  instead we see a growing convention for people having multiple Fediverse accounts.  I know some long-term Mastodon people who already do this. Would my followers prefer it if I posted software posts from one account, and board game posts from a different account?


Mastodon often likes to draw parallels with email, and many people have separate work and personal emails. Iâve lived for decades with separate Thoughtworks and martinfowler.com email accounts. The separation is often messy, while I try to keep my Thoughtworks email to company business, thereâs many things that get misplaced or on a fuzzy line. But the separation can still have value. As my colleague [Julien](https://toot.thoughtworks.com/@judeswae) put it about his pair: âI donât follow the same people (although thereâs overlap), Iâm not followed by the same people (with overlap). I say things on one that I would not say on the other, or not the same way, and vice versa.â


If organizations run their own Fediverse servers, the local timeline is more valuable if the posts are more focused on that organizationâs activity. That encourages users on such a server to use that account to post only about that activity, with perhaps the occasional boost from a personâs other timelines when some cross-fertilization is appealing.


Having separate accounts reduces the risk of problems when someone leaves an organization. While the convention is to use Mastodonâs migration feature to move followers, that may not happen if the separation isnât amicable. In this case separate presences on the Fediverse will help direct people to any new account, as well as not disrupting activity thatâs separate to that organization.


Years ago I separated my social media activity by using Twitter for my professional social network, and Facebook for my personal network. Iâve let the latter lapse in the last few years (becauseâ¦ wellâ¦ Facebook). On Mastodon I could recreate the kind of setup I had from Facebook with an account where I had to approve followers and where my posts go only to followers. Groups of friends could go further, having their own instance if service providers had plans that are cheap enough. (For this it would be nice if Mastodon sent posts by email for people who donât have a Fediverse presence.)


Even without these desires to separate Mastodon accounts, thereâs a broader need for separate presence on the Fediverse. Even now, there are other social media software present, such as [Peertube](https://joinpeertube.org) for video and [Pixelfed](https://pixelfed.org) for photos. Each of these need separate accounts. This effect would swell in the future if ActivityPub is seen as plug-in for other kinds of software. My project tracking software and my travel booking software could end up collaborating with other tools through ActivityPub, and each would have its own accounts. Iâve long been part of the venerable [BoardGameGeek](https://boardgamegeek.com/) community, it would be interesting to see how it might interact with the Fediverse.


There will be times when I need to tie my different presences together. Boosting is one mechanism,  if I need to share my flight information with my team,  my work presence can boost a post from my travel account. But we may need something more permanent and explicit, just as I need to tie together my website, twitter (and now Mastodon) feeds now.


Itâs a different model to the singular presence that Twitter and Facebook have trained us to use, and it will be interesting to see how it shake out as the Fediverse grows.


### Using CWs (16 November 2022) 
▶


One of the new features on Mastodon for a recovering twitterer is the CW field for new posts. CW stands for Content Warning. When Iâm composing a post, if I press the CW button, I have the option of putting a short phrase into a dialog. Readers will initially only see that short phrase, and need to click a button to see more.


CW stands for Content Warning, and the name suggests it can be used to hide potentially offensive material. However itâs a general purpose tool thatâs handy whenever we feel a reader would benefit from only seeing a short phrase with the ability to click for more, such as a post including spoilers for a TV show. One person I saw used it to say âCourse Promotionâ - which I thought was a thoughtful way to reduce the impact of advertising.


Adding a CW adds friction to reading the post, as you have to click the button to see the full contents. This friction is good if youâd rather not see the content, but irritating if you do want to see the content, particularly if youâre clicking on a lot of buttons. (A reader can turn off hiding for all CWs [in your settings](https://fedi.tips/staying-safe-on-mastodon#UsingContentWarnings), if you wish.)


The issue of how to use CWs has become a very emotive issue in recent weeks.  Communities had formed on the Fediverse who had felt bullied on other internet locales, including Twitter, and created norms for thriving here, norms which include when to use CWs. The [musk-to-tusk](https://journa.host/@mckenziefunk/109319233262061809) migration has led to a [massive influx](https://twitter.com/joinmastodon/status/1591519312338210816) of new accounts on the Fediverse (from 0.5 to 1.6 million), with the result that many long-time Mastodonians fear that their carefully built set of norms will be swept away. Newcomers, on the other hand, argue that the context for those norms has now changed. In any case,  a federated network means that there will be different sets of norms in different communities, and those communities will have to figure out how to coexist.


So as a new poster in this neighborhood, how should I react, specifically to the conundrum of when to use this CW feature?


The phrase I use to anchor my approach in matters like this is âI canât choose whether someone is offended by my actions. I can choose whether I care.â So I donât try to judge whether anyone ought to be upset with my decisions, thatâs up to them. Instead I think about how much concern I have for their reactions, and a large part of that is a judgment on how widespread the distress would be.


Mastodon is a federated network, so I have to accept that different parts of the community will have different standards. I presume the expectations about CWs will be a feature of a particular publisher, either that of an individual writer or a publication. My publisher is Thoughtworks, as that company controls the  Mastodon server I post from. So anything I post must fit in with expectations of Thoughtworks - but as an employee, thatâs nothing different from what Iâve been doing for two decades, on any platform.


Fundamentally, Iâm responsible for the contents of my Mastodon feed, and my readers will choose to follow me or not depending on how I use it.


One thing I read early on was to put any cross-posts from Twitter behind a CW. I did this when I started up my cross-post feed, but I also [created a poll](https://toot.thoughtworks.com/@mfowler/109275885334079676) to ask my readers what they preferred. They voted overwhelmingly against the CW, so I removed it. Readers indicated they didnât like the friction of clicking the button when they wanted to quickly glance through the feed.


Mastodon allows longer posts than Twitter, and Iâve seen even longer posts that I assume came from other Fediverse software. The longer a post is, the more useful it is to use a CW to summarize it so the reader wonât spend time reading it only to find they arenât interested. I use Twitter mostly to publish links that I think my readers will find interesting. In this case the post itself is a CW for that linked material.


My feed is mostly about software development, so thereâs an argument to use CWs for posts that are about other topics. As I expressed above, if the post is short with a link, its acting as a CW itself. But beyond that, a reason to not apply a CW is that I can give more visibility to something that I think is important for my readers to see, even if itâs not something they may want. As with software feature requests, often people will find it valuable to receive something that they never thought they wanted. Part of my role as an author is to figure out what my readers need, which isnât the same thing as what they want.


Politics is a regular topic for disputes about CWs. Many Mastodon guides state that all political posts should be behind CWs. But if Iâm following a political journalist, I would expect to see political posts, and the CWâs friction is an irritation. As a mostly-non-political poster, thereâs a greater argument for me to use a CW. But I only post on a political issue when I think itâs important to highlight it to my readers, and a CW defeats that purpose.


All in all, I see CWs as another tool for me, as a writer to help my readers by helping them find material useful to them. My suggestion to other posters is to experiment, use it when you think it helps your readers, but expect your understanding to change as you learn more. Weâll also see how the people we interact with use CWs, and use our experiences as readers to guide our decisions when we post.


### Volunteer moderation means lots of work (22 November 2022) 
▶


One of the things new people find most frustrating about Mastodon is the difficulty in [choosing a first server](https://martinfowler.com/articles/exploring-mastodon.html#choosing-a-first-instance). People are often told, with good reason, that a smaller server, focused on a particular community, is a better place to be, as the local feed will be more interesting. But then I hear a different frustration, that the moderators of such servers make it hard to join such servers, creating an air of cliquish exclusivity. This is particularly fraught when servers are based on a profession, since then the moderators are acting as gatekeepers, deciding who is or isnât a true professional.


I understand this frustration. If you are trying to build a career, itâs annoying when people set themselves up to judge your worthiness. But one of the things to remember is that Mastodon moderators are volunteers, and moderating an online community is a lot of work, particularly when  that community is a public one, whose posts can be passed widely across the Fediverse and wider internet.


Any community, however friendly, will run into disputes between its members. These can get ugly very quickly, spoiling the dialogue for everyone in it. Such disputes tend to heat up even more on a public forum like these, where thereâs a greater loss of face for backing down. Moderators have to spend time stepping into these disputes, trying to find some form of resolution that doesnât damage the broader community. Often this requires one-on-one conversations which are both time-consuming and emotionally draining. Their intervention will often lead to an outbreak of their own disputes, sucking up yet more time and energy. (This is a reason for Mastodon instances to be based around broader organizational membership. That way disputes can be handled by that broader organization, and not be a Mastodon moderatorâs responsibility alone.)


Whenever you allow other people to post content thereâs also the lurking risk that somebody will post something bad. It could be something awful, like Child Sexual Abuse Material, or copyrighted material, which will suck moderators into ugly hassles with DMCA takedowns and the like. If this happens the best case scenario is more time and energy lost.


Given all this, itâs understandable that moderators should want to be selective about who they have posting on their instance. Partly this is about scale, the more people you have posting, the exponentially more hassle it is to keep a healthy community. Itâs also why many moderators will prefer to have people with more connection than just signing up on a form. Thereâs a difficult trade-off here between being welcoming to people without connections and being an exclusive club. But volunteers need to be wary of signing up to more than they should handle, and applicants need to be understanding of the challenges that volunteer moderators face - especially since volunteers usually only realize they have taken on too much when itâs too late.


### Thoughts on (almost) a month of cross-posting (28 November 2022) 
▶


Iâve now been cross-posting from Twitter to Mastodon for almost a month. On the whole, I think itâs working well. I compose my posts on Twitter, fire them off, and shortly afterwards they appear on my Mastodon feed.


Many times, I can leave them on the feed as they are, but sometimes itâs worth doing some work to make them read better on Mastodon. A couple of times Iâve re/quote-tweeted a Twitter Thread. That doesnât show up very well on the Mastodon side, so for those cases Iâve deleted the Mastodon post and edited it to give the full Twitter URL (eg [https://toot.thoughtworks.com/@mfowler/109354209959165277](https://toot.thoughtworks.com/@mfowler/109354209959165277)). I sometimes do that when I mention Twitter user names too, switching them to their Mastodon accounts (if I know them), or using only their names or the @user@twitter.com convention. I donât adjust all the Mastodon cross-posts that mention Twitter handles, just the ones where I think itâs more valuable.


Delete and repost is somewhat awkward. It sometimes takes a few minutes for the Mastodon post to  show up, as I assume the cross-posting software only runs at intervals. So I have to wait for the cross-post to show, and then edit it before others notice, and either boost or reply. A couple of times Iâve been too late, which has led me to effectively repeat the post, or reply to the Mastodon post with proper URLs. At some point our team will upgrade the Thoughtworks Mastodon instance to the latest version, and Iâll be able to edit the posts. That will make editing cross-posts easier.


Iâm still inclined to stay on Twitter for the near future. Iâve seen a number of people I follow move off Twitter. (Please donât delete your account if you do this, in order to preserve URLs to old posts.) But I still have around 340,000 followers on Twitter versus 9000 on Mastodon, and I donât want to abandon them. Itâs still not clear to me what the future of Twitter looks like, although thereâs no shortage of worrying indications. Since I only use Twitter (and Mastodon) to post announcements, Iâm not worried about losing access to content. Anything longer than a tweet sits on [martinfowler.com](https://martinfowler.com) - I continue to feel that any active writer should own their own domain and post all significant writing on that domain.


Other than some departures, my reading experience on Twitter hasnât changed since the Muskover, which I suspect is mostly due to me only ever using the chronological view or lists, where I only see tweets from people I deliberately follow. Iâm lucky enough not to get many unpleasant characters in my mentions. At this point Iâm still seeing valuable stuff there that doesnât appear on Mastodon, so I still read it.


### Frustrations with lists (01 December 2022) 
▶


One of the most useful, and most frustrating, features of Twitter is lists. I like lists because they allow me to divide up my timeline to topics I want to read about at different times. They are frustrating because the tools to manage them in Twitter are very limited, so itâs more hassle to set up the kind of environment Iâd like. Mastodon also has lists, sadly its current management tools are equally bad.


The problem lists can solve for me is my cluttered timeline. On Twitter I use only the reverse-chronological flow of accounts I specifically follow. I like this approach, and seem to avoid a lot of problems that I hear about from those that use Twitterâs engagement algorithm (Mastodon only has reverse-chronological). But the problem with this is that there a lot of accounts I follow, and my interest to them varies at different times. Some accounts Iâd like to know about whenever they post during the day, others Iâd prefer to catch up with only when I feel I have some time to graze, some I only want to look at in the evening when Iâm âdoneâ with work, and some I want to avoid while Iâm in my comfy chair with a whiskey in hand.


Lists allow me to divide things up like this. I have separate lists for tech, current-affairs, covid, and boardgames to reflect different topics that Iâd like to peruse at different times. I have another feed for voluble posters who would otherwise flood a timeline with their frequent posts but I occasionally like to read when Iâm in the mood. Iâd like to have a hot list for people I always want to monitor. But this is where the management tools have been awkward for me.


To manage these lists, I really need a display that shows every account that I follow in a table with its lists. That way I can easily see which list each account is on, and spot any accounts that arenât on a list. Such a display should also be the point where Iâd change the list assignment. For my usage each account would be on a single list (although Iâd need some way to deal with any exceptions that might crop up).


On Twitter, this scheme was defeated because I had no way to easily find which accounts I follow that were not on any list. (I tried cobbling together something using the Twitter API, but wasnât able to get it to work.) Consequently I treated my follows as the hot list, and most accounts I âfollowâ were just on a list and not officially followed. Of course, this leads to the impression that I donât follow certain accounts that I actually do via the lists.


On Mastodon, I can only put accounts I follow onto lists, so I wonât be able to repeat that hack. The controls for assigning accounts to lists are sufficiently onerous that I havenât yet tried to go through and assign them all yet. My hope here is that the APIs are sufficiently open that someone else with a similar desire will scratch that itch. (Yes, I could do it myself, but I have too many higher-priority things to do.)


### Finding accounts to follow (16 December 2022) 
▶


A common question Iâve seen is: how to find people to follow on Mastodon. One of the reasons this is a big question for people is that there is no algorithm to introduce readers to new writers, unlike Twitterâs Top Tweets view. I find this rather odd, because Iâve been very determined to stick to the reverse-chronological view on Twitter (latest tweets), which means I only see tweets from people I explicitly follow. Indeed I think this has done a great deal to keep my Twitter experience to be generally positive. However I recall a Mastodon post by an ex-Twitter employee who said that 97% or so of Twitter users preferred the Top Tweets feed - another sign that Iâm not a usual user. (Sadly I canât find that post, partly due to Mastodonâs decision to make searching difficult.)


So how do I go about finding people to follow? Mostly itâs because people I already follow on Twitter have said they have opened up a Mastodon account. As soon as I see that, I add them to my list. But this just shifts the question, because I had to find them on Twitter first. Most of them came from two paths. One is that I ran into their writing from another source, such as a web article,  and looked to see if they have a social media handle. Thatâs why I have my Twitter and Mastodon icons on the top of my web page banner (and listed on my [about page](https://martinfowler.com/aboutMe.html)). The other source is when someone else who I follow retweets (boosts) a tweet from them that looks interesting. Iâll then take a look at their stream, and if they look interesting, start following them. (Remember that on Twitter, I follow mostly via lists, so they donât show up as an official follow.)


Another route that I used in my early days on Twitter was to look at  people I liked and see who they followed. You can go to my Mastodon accountâs [following page](https://toot.thoughtworks.com/@mfowler/following) to see who I follow. This will be a mix of writers on software, current affairs, and board games. Take a look at their streams and you should be able to figure out if they would be interesting to you.


Another useful route on Twitter is through public lists, but sadly Mastodon only has private lists - at least for the moment. I hope that will change as I think curated lists can be a great way to find good material.


(When following someone on social media, itâs wise to ensure the account is genuine. I wrote earlier on what that means for Mastodon.)


### Status - February 2023 (03 February 2023) 
▶


I havenât posted much on my Mastodon usage in the this year, and thatâs because the situation has settled down for me. Reading-wise I check both my Twitter and my Mastodon accounts. Most of my lists seem equally active between the channels, the one exception being the board game one, which is almost all on Twitter only.


Iâve set my Mastodon account up to use lists. I wrote a rough and ready script to list out all my follows using the API (too rough to share, Iâm afraid). I then manually assigned everyone to one of my lists. Since then, whenever I follow a new account, I add it to one of the lists. Itâs not the smoothest method in the world, but itâs worked well enough. I now pretty much ignore the built-in feeds and use my lists all the time.


I still have *far* more followers on Twitter: 344,000 compared to 18,000 on Mastodon. Iâm still not inclined to abandon those Twitter followers, so continue to cross-post. I suspect the tool I use for cross-posting will stop when Twitter starts charging for its API access. My current plan is to then cross-post manually. At some point Iâll do some analysis on the response to my article announcements, but I want to have a few more published before I spend time on that.


## Latest Memo: Comparing Engagement on Twitter and the Fediverse


07 February 2023


My colleague [Julien Deswaef](https://toot.thoughtworks.com/web/@judeswae) recently compared engagement data for my Twitter and Mastodon posts. Hereâs how they compare.


(If youâre not familiar with the type of chart Iâm using above, see my article explaining why you [shouldnât use averages](https://martinfowler.com/articles/dont-compare-averages.html) to compare things like this.)


For this he compared the boosts (retweets), comments (replies), and likes for my recent cross-posted Twitter and Mastodon posts for the last month. He selected only original posts, not retweets or replies - 40 posts in all. (I excluded 4 outlier points from 3 posts.)


From this we can see that boosts and comments are very similar. Twitter does get significantly more likes, but considering I have nearly 20 times more Twitter followers than Mastodon, itâs a remarkably small difference.


Based on these engagement figures, Iâd say that the Fediverse is now just as important to me as Twitter. That makes me feel more comfortable should the bird be suddenly killed by the debt kitty.


We should remember, of course, that my audience is very tech-savvy, and other writers on Twitter may not get a similar engagement pattern. But tech is often a leading indicator in these things, suggesting that thereâs a considerable evidence for optimism in the Fediverseâs future (and perhaps rather less optimism for Twitterâs).


---
