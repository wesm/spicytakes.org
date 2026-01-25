---
title: "The Monkey and the Apple"
date: 2016-11-16
url: https://steve-yegge.blogspot.com/2016/11/the-monkey-and-apple.html
word_count: 4588
---

It's been a while!
I took a couple of years off blogging because I felt I didn't have much left in the way of interesting things to say.  So I've been just been programming, and studying, and learning this and that.  I've been doing a bit of Cloud development, and I taught myself iOS development, and after years in the Google cocoon I poked my head out and learned how people do things in the real world with open source technologies.
And lo at long last, after some five years of tinkering, I finally have something kind of interesting to share.  I wrote a game!  Well, to be more precise, I took an old game that I wrote, which I've perhaps mentioned once or twice before, and I turned it into a mobile game, with a Cloud backend.
It has been waaaay more work than I expected. Starting with a more-or-less working game, and tweaking it to work on Cloud and mobile -- I mean, come on, how hard can it be, really?  Turns out, yeah, yep, very hard. Stupidly hard. Especially since out of brand loyalty I chose Google's cloud platform, which 3 or 4 years ago was pretty raw.  And let's face it, iOS APIs have evolved a ton in that timeframe as well.  So even as "recently" as 2013 I was working with some pretty immature technology stacks, all of which have come leaps and bounds since then.
And now I have all
*sorts*
of stuff to share.  Definitely enough for a series of blog posts.  But I also have less time than before, because it's all happening in my non-copious spare time, all late nights and weekends.  And running an MMORPG is a fearsome task in its own right.
Incidentally, I've just opened the game up for
.  So if you want to try it out while you read along, visit
[http://ghosttrack.com](http://ghosttrack.com/)
to request an invite.
**(Edit, 12/13/16 -- BETA IS NOW CLOSED.)**
You'll need an iPhone, iPad, or iPod running iOS
*(Edit: 9.2!)*
or later.  I'd love to do Android and PC, but there's only one of me.  For now.
So where do I start?  I guess the logical thing to do would be to start at the beginning, but screw all that, I'm starting with the monkey.

## The Monkey

I had the following conversation with my wife the other day. It went something like:
**Wifey**
: Baby, I lost all my stuff!
*(A lot of our conversations have started this way since April, give or take, when she started playing the game.)*
**Me**
:  What stuff baby?
**Wifey**
: (
*wailing*
) All the stuff I had in my house!!  I dropped it all there and them boom, it disappeared, right in front of my eyes.  I was watching it and then five seconds later it was gone.  This happened before, and I didn't want to tell you because I wasn't sure, but I just saw it!  It happened!
**Me**
:  OK baby I'll come look.
**Wifey**
:  See?  It was right there!  I had a lot of good stuff there and it's gone!
**Me**
:  (
*looking around)*
I believe you baby.
**Me**
:  (
*looking around some more*
)  I think... I think the Monkey did it.
**Wifey**
:  What monkey?  What!?  That monkey took my stuff?
**Me**
:  (
*checking*
)  Yep.  It picked it all up and it's carrying it now.
Sure enough, her pet monkey had picked up all her precious loot and valuables.  But while she stared in disbelief at this unexpected betrayal, I was worrying about how I was going to get her stuff back.  Because there were two problems.
First, the monkey wasn't killable via combat, since I had marked pet creatures in your personal home as non-attackable.  I don't know if that was the best decision ever, but it seemed reasonable at the time.  And second, there was a chance that if I pulled out the big guns and killed it myself, for instance by invoking its
kill()
method directly at runtime, its inventory (her loot) would be replaced with the default monkey inventory of bananas and fur, or whatever I'd given them.
I'm pretty sure that in most states, accidentally replacing your wife's hard-earned treasure with bananas and bits of fur is legal grounds for divorce.  So I was in a bit of a pickle.
**Wifey**
: How are you going to get it back?  I can't believe that monkey!  Can you just make it drop it?
**Me**
:  Well I could, but the AI will just immediately pick everything up again.
**Wifey**
: I worked hard for that stuff!  I can't even remember what I had!  An amulet, a sword, a girdle, all kinds of stuff!
**Me**
: Don't worry, baby.  Tap on the monkey, you can see it carrying everything.  Just give me a second to figure it out.
The picture below shows the predicament.  Wifey is the naga warrior, I'm the old guy in the blue pajamas, just like in real life, and the monkey is barely visible 2 squares below her, by the Japanese shoji screen.
Every creature in the game has an event queue and a command processor, and can respond to generally the same set of commands as players.  Normally the AI decides what commands to give a monster, but you can inject your own commands under the right circumstances, or even take control for a while (e.g. with the Charm Monster spell).  So I decided I'd try to command the monkey to give me the items, one at a time.
The game is written mostly in Java, but a good portion (maybe 25%) is written in Jython, which is an implementation of the Python language on the Java virtual machine.  And, usefully, Jython has eval and exec functions for interactive code evaluation.  So I opened up my command interpreter and went to work.
> exec monsters = me().map.monsterList
Ok
> eval monsters
[monkey]
> exec monkey = monsters.iterator().next()
Ok
> eval monkey
Monkey
> eval monkey.inventory
The MonsterInventory contains:
- bit of fur (0.06 lb)
- bone (1.5 lb)
- Amulet of Acid Resistance (0.12 lb)
- bag (0.5 lb)
...
So far, so good.  I had a reference to the monkey in my interpreter, and I was seeing Wifey's stolen valuables, plus the expected monkey inventory.  Now for the coup de grace.
> eval monkey.commandNow("give amulet to rhialto")
> None
> Monkey gives you Amulet of Acid Resistance.
Woot!  Success.  I had to keep chasing the monkey around, since offhand I couldn't think of a way to make it stand still.  In retrospect I could have paralyzed it, or set its AI to the stationary AI used for immobile monsters.  But I couldn't be bothered to look up how right then, since I hadn't ever been in a situation quite like this before, and my wife was alternating between indignation, amused disbelief, and near panic over her stolen stuff.
I had a mechanism for getting the items back, so I just followed the monkey and issued those
commandNow()
instructions.
Unfortunately, and to my lasting surprise, the monkey started ignoring me after the fourth or fifth item.  It continued about its business, but it would not give me any more items.  I still don't know exactly why, since this was such an edge case scenario.  I have a large toolchest of utilities and commands for manipulating player inventories and map contents.  But it's rare that you need to command a monster to give you stuff.  Normally you get a monster's inventory the old-fashioned way. You pay the iron price.
I was irked by the monkey's emergent nonchalance, so I pulled out the hammer:
> eval monkey.kill(me())
> Ok
> You killed monkey.
Where
me()
in this case is the attacker.
As I feared, the corpse's inventory was completely empty, because I clear out the inventory for pet monsters, to prevent abuses where you just create them in builder mode, take their stuff, and make infinite cash.
So I busted out the
clone()
command and manually recreated the rest of the missing items as best I could, and gave them all back to Wifey.  I'm pleased to report that this story had a happy ending.

## How to Make a Game

You look at a game like Wyvern, which is at its heart just a tiles game like the old roguelikes, and maybe a bit of a MUD, and you think, gosh, I could do that.  And you can!
Off the top of my head, you will need:
* A cloud computing platform such as AWS, Azure or GCP.
* Xcode and a Mac, or else Android Studio and a whatever-you-want.
* A programming language and a compiler. These days, I would go with Kotlin.
* A service for browsing and licensing music and sound effects. They have those now.
* A service for hiring contractors for artwork and maybe level design. They have those too!
* A hosted datastore, because seriously it's 2016, don't administer your own.
* A source hosting and bug tracking service, such as Bitbucket.
* A good lawyer and a good accountant.
* About twenty years.
Ha!  I kid.  I've only put about ten years into it, spread over the past twenty years.  I started in 1996; my character Rhialto will turn 20 on March 1st.  But in terms of total person-years, it's in the hundreds, largely due to area design contributed by dozens of passionate volunteers.
It's amazing how much stuff we have access to since I started this project back in 1996.  Back then, I had Java, and we're not talking about Java 8 with fancy lambdas and streams.  We're talking Java 1.0.2, with that O'Reilly book with the referees on the the front.  You had to roll everything yourself back then.  Uphill both ways, in the snow.
*(Actually the game started in C++ in 1995, but I migrated to Java and never looked back.)*
I went through something of a life crisis in 2004, after 8 years of working on the game, because my productivity had tanked as the code base grew, and I wanted it back.  So I stopped working on the game, for the most part, and went on a Grail-like quest to find a good language -- one that was ultimately unsuccessful, although I learned a lot and got some good rants out of it all.
Nowadays, though, sheesh.  Between GitHub and its infinite supply of high-quality libraries, cloud providers and their hosted services, Stack Overflow and its infinite supply of answers to just about every question you'll ever encounter, and all the services available for payments and contractors and everything else you could want -- I mean, it's a startup's dream come true.  I am
*way*
more productive than I was in 2003.  All I needed was a time machine.
Even so, a game like this -- which, despite its simple appearance, is a true MMORPG with surprising depth -- is basically an infinite amount of work.  Lifetimes of work.  So you have to practice triage, time management, and stress management.
But really, anyone can do it.  You just gotta
*_want_*
it bad enough.

## Apple vs. Android

I have enough material for lots of blog posts now, and I'd love to spend some time exploring Google's Cloud Platform (GCP) in future articles.  I've learned a thing or two about Android as well.  And Kotlin is absolutely entrancing.  I haven't used it yet for anything serious, but it's one of the best new languages to emerge in a long, long time.  Would love to talk more about Kotlin at some point.
For today, though, I thought I'd offer a few musings on Apple, iOS, and their store ecosystem.  I'm still no expert, and I don't do anything iOS-related at work.  This is just some very personal impressions I've collected while making the game.
A lot of people have asked me why I did my first mobile client in iOS rather than Android.  The answer is monetization.  iOS is straight-up easier to monetize.  Android has cultivated a frugal audience, through both marketing and hardware choices, and that cultivation has been a success.  Android users tend to be frugal.  That doesn't mean they don't spend money, but it does mean they are more cautious about it.  I have friends who've done simultaneous iOS/Android releases for their apps, and invariably the iOS users outspend the Android users by anywhere from 4:1 to 10:1 -- anecdotally, to be sure, but a little Googling is enough to support just about any confirmation bias you like.  So I picked iOS.
When I started, I didn't know Objective-C, and I started
*just*
before Swift came out, just a couple of months.  But by then I was far enough into development, and wary enough from prior experiences with new languages, that I opted to continue in Obj-C.  Obviously today I'd do it in Swift, and if I weren't always so time-constrained, I could even start introducing Swift class-by-class.  Swift is cool.  It actually reminds me a lot of Kotlin.  I think language designers must have some sort of clique these days, whether they know it or not.
What about iOS?  Well, there's not much to it.  And that's a
*good thing*
.  It feels familiar, at least if you've done any sort of UI programming at all in your career.  I've done some Java AWT and Swing, some Microsoft MFC and whatnot, some X-windows work, some web programming, whatever -- rarely anything major, but I've tinkered with UI throughout my career.  Frontend UI is a skill every engineer should have, even if it's just one framework that you know well.
Coming from all those frameworks, I had certain expectations, and they were 100% met by iOS.  It has an MVC framework, and you add views and subviews, and you have all the hooks and lifecycle events you'd expect -- after learning Objective-C, I'd say it was only about four days (thanks to the excellent Big Nerd Ranch book) before I was able to start cranking out reams of code by copying it all directly from Stack Overflow, as is tradition.
Why am I making such a big deal about iOS's almost boring familiarity?  Because Android is the exact opposite of intuitive and familiar.  I've gotta be a little careful here, since I recently joined the Android tools team at Google, and I don't want to throw anyone under the bus.  They did the best they could with the environment and situation they had when they started back in the early 2000s, which featured phones that didn't even have memory -- they just had "address/contact slots".  It was awful.  They did fine.
But now, thanks to Moore's Law, even your wearable Android or iOS watch has gigs of storage and a phat CPU, so all the decisions they made turned out in retrospect to be overly conservative.  And as a result, the Android APIs and frameworks are far, far, FAR from what you would expect if you've come from literally any other UI framework on the planet.  They feel alien.  This
[reddit thread](https://www.reddit.com/r/androiddev/comments/2hlw20/am_i_retarded_or_android_development_is_a_mess/)
pretty well sums up my early experiences with Android development.
So as much as I'd love to make an Android client for my game, it's not going to happen for a while.  Plus I'm still iterating heavily on the iOS UI, so I might as well wait until it stabilizes a bit.
That's enough about Android for today.  I always gauge how edgy my blog posts are by how likely I am to get fired over them, and my little indicator is redlining, so let's move back to Apple and iOS.

## Apple:  The Good, the Bad, and the Ugly

Objective C isn't so bad.  They have continued iterating on it, so even though its string handling is comically verbose, and it has no namespacing, and there are tons of other modern features missing, the language is pretty capable overall.  It has generics, literal syntax for sets/dictionaries/arrays, try/catch/finally macros, extremely well-implemented lambdas with proper closure capturing (unlike nearly every other non-functional language out there), properties, and many other modern conveniences.  The syntax is awful, and it can get pretty weird when you're bridging to the C APIs, but on the whole you wind up writing less code than you'd think.
In fact, various bloggers have measured it, and if I recall correctly, the consensus is that Android Java is about 30% more verbose than Objective-C.  Which is pretty counterintuitive, because the Java language itself, verbose as it may be, is
*clearly*
less verbose than Objective-C.  What's happening here is that iOS has such good APIs, you wind up needing to write a lot less code to get your job done.
So Obj-C isn't bad, and Swift looks really good.  The APIs are good, the documentation is solid, and Apple is aggressively deprecating crummy old APIs (like
UIAlertView
) in favor of better-designed ones.  Everything is still there in the system, and you can see generations of whole layers of API access dating all the way back to the old NeXT computers from the late '80s (heck, everything in iOS starts with NS, for NeXTStep)
But you don't have to use most of that stuff, because Apple has been constantly layering on new APIs that modernize it all.  Unlike, you know... some other, uh, people. >.>
Xcode is pretty good. It used to be bad, but now it's not bad at all.  Yes, it crashes more than I'd like, and yes, its refactoring support is abysmal.  It's no Visual Studio.  But "pretty good" is good enough.  Because all I'm doing is copying code from Stack Overflow, really I have no shame whatsoever, and Xcode works great for that.  It even formats it for me.  Who am I to complain?  Besides, I use Emacs for any serious editing.
So for the Good, we have the languages, the APIs, and the tools.  What about the Bad?
Well, Apple's review process is really, really,
**really**
long and convoluted.  Sure, I can totally understand why.  They have millions of developers trying to shoehorn crap into their store, and they are trying to make a strong quality stand.  But it means you're in for a wild ride if you're making anything more complicated than a flashlight app.
First you have to go through their checklist of roughly seventeen thousand rules, and make sure you have addressed each of them, since all of them can result a veto.  And wouldn't you know it, I checked
*exactly*
sixteen thousand, nine hundred and ninety-nine of those rules very carefully, so my app was rejected.  Because they don't mess about.  You have to follow all of them.
The story of my app's rejection is epic enough for an opera, but in a nutshell, Apple requires that all apps support ipv6-only networks.  But none of the major Cloud providers supported ipv6 at the time of my submission, in late September.  You're pretty well covered if you're just doing HTTP(S), but if you use sockets you're hosed.  My game uses direct TCP/TLS connections to my cloud instances, so it didn't work on an ipv6-only network, and my app was kicked to the curb like so much garbage.  At least they did it quickly.
After some technical consideration, I did the only logical thing, and got on my knees and begged them for an exception, because what am I gonna do?  Some cheesy hack with an ipv6 tunnel provider to a fixed IP address on a single instance?  Well, yeah, that's exactly what I was going to do, if push came to shove, just to get through the review. Even though it's completely non-scalable.  Desperate times.
Fortunately, after a mere six weeks, and me finally sending them an angry-ish (but still cravenly and begging) note asking WTH, they granted me the exception for 1 year, backdated so it was really only 11 months, but whatevs.  I was approved!
**The Ugly**
Just kidding, haha joke's on me, I was NOT approved.  Because when they gave me the exception, they also threw in a major feature request.  Lordy.  It's almost like they're a monopoly or something.  They didn't like that my game required you to sign in via a social network -- Facebook, Google, or Twitter for now, since those are the sign-in SDKs that I've managed to wire up so far.  So they asked me to implement Wyvern Accounts.
Sigh.  I was so relieved that I got the exception, I didn't fight it.  I called back to ask if it was OK to require an email address, for account/password recovery functionality (but also because I use the email address to tie your characters together), and they said that was fine.
So I went to work, even though my game had already been in Alpha for six weeks too long, and I implemented Wyvern accounts.  New database table, new web service, new API service, new UI screens for registration and account creation and password resetting, new plumbing for passing credentials to the server, blah blah blah.  God dammit, the nerve of them to ask for such a big feature.
A week later when it was all finished, I realized FB/Google/Twitter all have minimum age requirements (all 13 years minimum because of COPPA), so I had been protected until Apple threw their curveball at me.  Now I need underage reporting and god knows what else.  Still working through it with the lawyers.
I'd go back to Plan B (in iOS-land, B is for Begging), except that I actually sort of agree with Apple that I need this feature.  Not everyone is on a social network.  For example, there is an uncontacted tribe deep in the South American rainforest who are not on Facebook yet, although I believe they are still eligible for Amazon Prime.  And also some of my alpha testers were struggling with it.  I guess there are a lot of people who not only don't have GMail, but they prefer not to sign up for a free account.  I can only assume the NSA is responsible for this phenomenon.  But it means I most likely need Wyvern accounts.
Another reason I sort of need Wyvern accounts is that Facebook, Google and Twitter all have very different philosophies about email-verification APIs.
Facebook's philosophy is, roughly: "What's a few API calls between friends?"  They have quotas, but they're so high that I won't have to worry about them for years.
Google's philosophy is, roughly: "Our APIs should scale with your business."  They have quotas, but they're so high that I won't have to worry about them for years.
Twitter's philosophy is, roughly: "Go fuck yourself."  I exhaust their tiny quotas every day, even after adding credential caching so that players only re-validate once every 8 hours or so.  Even though I only have a few dozen, maybe fifty regular players right now, only a handful of which use Twitter.  Their quotas are comically, absurdly low.
So I'm probably going to have to yank Twitter out before launch, which would limit people to FB and Google sign-in.  And that seems like... not enough options.  I don't like having to maintain my own accounts, but I think I'm pretty well stuck with it.
The takeaway (well, other than "don't use Twitter APIs"), is that Apple can jerk you around pretty much all they want, and you'd better like it.  You should basically prepare for a long review.
**Back to The Good**
Despite the bumps in the (long) road so far, some stuff has been great.  TestFlight, which is Apple's beta testing system, is working nicely for me.  It provides me with crash reports which have identified half a dozen real issues so far.  The sign-up is a snap, and they'll let me have up to 2000 testers, which will help me make sure my stuff scales, if I can get that many.
And their review turnaround time has been pretty good.  It generally takes about a day, in my experience.  I'm not sure why they require a manual review for my Beta builds, after they've already approved me for the actual store launch.  And every build requires another 1-3 day review.  But I've got a pipeline going, and I'm pleased overall with how straightforward it has been.
I'm really worried about In-App Purchases.  I offer them in my game (though it's definitely not pay-to-play), but Apple's testing for IAP leaves a lot to be desired.  You have to sandbox it, and this requires setting up separate accounts.  It's not possible to enable production IAP (with real money) before the actual launch.  But their sandbox environment makes it really easy to screw up a transaction, after which your device will prompt you for a store login every 5 minutes for the rest of your miserable life, and likely into the hereafter.  It's a mess.
You can sort of enable IAP in Beta/TestFlight, but it's *free*, which means players would be able to acquire millions of coins for free, and it would require me to perform a full reset of everyone back to level 1 before launch.  I'm trying to avoid that.
So I have no idea if my IAP really works.  I got it working in the sandbox at one point, and I'm hoping it works in prod, but until I'm confident that it's working, I'm going to have to charge for my app, to forestall the possibility of a massive meltdown from casual players (tourists, basically) eating up my server resources.  I don't want to get a gigantic bill from Google.  So I need to limit the growth as best I can for a while.

## Going Forward

Building this game has been a lot of fun.  I've learned more from doing this project than from anything I've ever done that was work-related, at any job I've had.  Something about having to do a big project yourself forces you to pay attention to everything in a way that you rarely have to do at a corporation.
I don't know if it's going to be a hit.  Statistically, probably not.  But I have some pretty darn loyal players.  The game was down for
*five years*
(2011-2016), and when I brought it back up, a hundred or so old timers appeared out of nowhere.  Many of them had to purchase iOS devices just to play, but they splurged.  And they started playing insane hours.  The ratio of 7-day-active to concurrent players has been crazy.  In the old days it was about 100:1, so on a server that could comfortably support 100 concurrent players, I'd typically have about 10k 7-day actives.  It was self-limiting because I only had one server back then.
With these alpha testers, the ratio has been about 4:1.  They're playing upwards of 8 hours a day, around the clock.  And they're all over the world -- I have testers in Japan, England, New Zealand, Spain, Nigeria, Toronto, east coast, west coast, I forget where they're all from.  But we're talking about a group of only about 60-70 regulars, so the diversity is quite remarkable.
This
[letter they wrote me back in 2012](http://wyvernsource.com/2016/10/06/remembering-players-letter-to-rhialto/)
, when the game went down so I could port it to Cloud, gives a pretty good sense of how much people like it.
I'll report back in a few months and let you know how the launch went.  Meantime, if you want to play, visit
[http://ghosttrack.com](http://ghosttrack.com/)
.  Hope to see you online!
Rhialto