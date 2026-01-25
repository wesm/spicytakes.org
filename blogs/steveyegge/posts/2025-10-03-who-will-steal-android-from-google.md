---
title: "Untitled"
date: 2025-10-03
url: https://steve-yegge.medium.com/who-will-steal-android-from-google-af3622b6252e
word_count: 3208
source: medium
---


--


118


Listen


Share


Who will steal Android from Google?


Disclaimers: These are my own personal opinions. A lot of them are probably wrong. I do not speak for my employer (Grab!). Take all this with a healthy grain of salt. In fact, don’t even read it.


Here I am, writing a Medium post while on a plane to Jakarta again. This is getting to be a habit.


I’m still not 100% sure why my “Why I Left Google” post got so much attention. I basically said, “I’m some random dude changing jobs, blah blah blah”, more or less verbatim. Somehow it was translated into like 80 languages and was surpassed that day only by Natalie Portman’ssex column— which to be fair was a lot more interesting.


So it was a slow news week, I guess. Or maybe it took off because Medium reaches a lot of people? It’s a great platform. Back in my blogging days, I used to wish Google would create an innovative product just like this one, but… well, you know.


In any case, my post garnered some interesting responses. A guy somewhere in Pakistan offered to buy me a beer if I ever happened to be in town. Someone in London offered me a thousand bucks to talk on the phone for an hour about voice search markets or some such garbo, which I politely declined because I do not actually know any useful facts about anything. A Russian guy even came up to me at a party and told me, “You heff many enemies”. Fun times.


There also was alotof misunderstanding about the core message, with people asking “Hey, isn’t this just ride hailing?” I tried to paint a picture that was bigger than that, but it flew over a lot of heads, so I guess I didn’t do a very good job of it. I’ll try to revisit it at some point and see if I can do better.


But not today. No, today I’m going to talk a little about Android: Just my own personal take on it, as an outsider and hobbyist Android/iOS developer. And since everyone knows you can’t catch lightning in a bottle twice in a row, it’s safe to assume that this post won’t go viral. Today it’s just me and you.


Android has been on my mind because we’re trying to hire mobile developers, which you’d think would be a straightforward task. But it turns out they’re the hottest commodity on the market right now. Grab needs them, everyone needs them, and there aren’t enough to go around. It’s like trying to catch unicorns.


Why does everyone need mobile devs? Becausethe web is slowly dying. I have friends — well, probably ex-friends now — in just about every org at Google, who used to point me at their gloomy graphs, and it doesn’t matter how you slice it, the web’s in a steady decline as the whole world moves to mobile. Heck, you probably remember Facebook going through its transition from web-first to mobile-first, what, maybe 8 or 9 years ago? Facebook almost kicked the bucket. I mean not overnight, but the company went through an existential crisis when they realized that they had to become a mobile company or face oblivion.


They managed, but it sure as hell wasn’t easy, because Android’s dev stack is the world’s biggest poo sandwich.


Poo Cuisine


At Google, most engineers are too snooty to do mobile or web programming. “I don’t do frontend”, they proclaim with maximal snootiness. There’s a phenomenon there that I like to call the “DAG of Disdain”, wherein DAG means Directed Acyclic Graph, which is a bit like a flowchart. At the top of Snoot Mountain sit the lofty Search engineers writing in C++, which is considered cooler than Java, which is cooler than Python, which is cooler than JavaScript. And Search is cooler than Ads, which is cooler than Apps, which is cooler than Tools, which is cooler than Frontends. And so on. Programmers love to look down on each other. And if you’re unlucky enough to be a Google mobile engineer, you’re stuck scuffling around at the bottom of several totem poles with everyone looking down on you.


But having done it all myself at one time or another, from systems programming to large-scale data engineering to compiler design to service frameworks to game development to web development to mobile development, I can assure you thatfrontend programming is every bit as hard, if not harder. Everything in the backend is nice and clean and organized and distributed and parallelizable; it’sheavencompared to the yucky mess that web programming remains after 2.5 decades. And even web programming is like a nice trip to Bali compared to the poo sandwich of mobile programming, including iOS.


And Android? Yep. It’s the biggest poo sandwich of them all. Android devs areheroes, if you’ll pardon the pun. Programming Android for a huge app like Google Maps or Facebook or Snapchat is… just… I mean you wouldn’t believe me if I told you. Sitting there fortwenty minutesto wait to see what happens after you change one line of code. And every change you make, no matter how tiny, has an 80% chance of not working the first time you try it, because the feature interoperability matrix is bizarrely sparse. Sure you can use X, and you can use Y, but you can’t use X together with Y becausescrew you buddy.


And don’t even get me started about device compatibility. I have a bunch of angry 1-star reviews in the Google Play Store because my Wyvern game app randomly didn’t work on LG devices, so I had to go on eBay and buy a crummy $60 LG device (as opposed to a crummy $600 LG device) to repro the bug and discover that hey, there are two Android APIs for getting mouse-click events on a scrolling list, but one of those APIs doesn’t work on LG.


I meancome on.


So here’s what has happened: A bunch of competitors, big and small, have come out with their own replacement Android frameworks. I’m not just talking about support libraries for missing functionality, though those exist aplenty. No. I am talking about full-scale replacements for Google’sentireAndroid development stack. Microsoft has Xamarin, Adobe has Cordova, Facebook has React Native, I mean it’s crazy town. Seriously go look. Framework7, Appcelerator Titanium, Onsen, Sencha, Kendo, XDK, Ionic, Mobile Angular, Unity, I mean real talk here,what the hell is going on?


It’s like everyone who’s ever tried to do Android programming gave up and declared: “This is so bad that I will do my own startup to make it better.”


And Google, not to be outdone by their competitors, responded by saying, “Ohyeah? Well you can’t compete with us, becausewe’regoing to compete with us!” and they launched Flutter, which is — I am not making this up — a 100% serious Android development stack that competes with native Android, and whose existence the actual Android team simply refuses to acknowledge.


What a time to be alive.


Assaults on Android


The thing about these dev frameworks is that they make Googlevulnerable. Most of them are cross-platform, which means you write a single app and it runs on both iOS and Android. It doesn’t matter whether you’re a big company or a small shop, nobody likes having to pay for two engineering teams to write the exact same app on different platforms. So there is tremendous economic pressure to migrate to a cross-platform framework. The only thing stopping it from being a stampede is that the frameworks aren’t quite as good as “native” development yet.


But several of them (notably Facebook’sReact Native) are getting reeeeally close. And if one of them manages to snag a big enough market share, then Android basically becomes the plumbing for a developer ecosystem that’s no longer in Google’s control.


This might not seem like a big deal, because Google still has the Play Store and the OEMs and licensing and so on. To most folks, they probably appear to be comfortably in the driver’s seat. But consider: If all mobile developers were to start using a particular cross-platform framework X, then literally any other hardware/OS manufacturer or consortium could come along with their own competing hardware/OS platform (like, say, Windows) that supports that framework X directly, and all the apps would run on it (probably faster, to boot), which would cut Google out entirely. And believe you me, a lot of companies want to do just that. Sorry, my bad, not a lot of them. ALL of them. Who wouldn’t?


Google’s response to this situation has been to dig in their heels. They’re doubling down on “native” (traditional) Android programming, with official support for the Kotlin language, which was a big step up for native Android programmers. I love Kotlin; it’s the future of Java. But let’s face it: It’s not where the mobile market is headed. People are writing cross-platform frameworks for two big reasons: First, because they want their company’s app to work on two platforms without doing 2x the work. And second, because Android native programming is still so painful, even with Kotlin, many companies feel (justifiably) that they should just throw it all out and start from scratch with something easier.


If you are an Android or iOS developer, and you take some time to try React Native (which Facebook created to help address these problems), you’ll realize within about 30 seconds that it’s WAY better, assuming you’re not writing a game, in which case you’d probably use Unity anyway. For business and productivity apps, React Native offers reasonable performance, cross-platform compatibility, incredible tools (the best being from Microsoft. Hello, relevance! Welcome back!), andvastlyimproved development speed. Remember I said it could take 20 minutes to see a 1-line code change in the regular Android stack? That can happen in the biggest apps like Nest or Facebook, but even for medium-size apps it can be 2 or 3 minutes. Whereas with React Native it’sinstantaneous.You make a change, you see the change.


And that, folks, means you get to launch features 10x faster, which means faster time to market, which means first-mover advantage, which means you win win win. Abandoning native programming in favor of fast-cycle cross-platform frameworks like React Native is awinning strategy.


I suspect, without evidence, that the Android org at Google is not sure whether cross-platform is good for them or bad for them, but that they are leaning towards “bad” — otherwise they would get behind Flutter, which is cross-platform. I personally think it would be good for them, but what do I know.


Regardless, they are currently focusing on trying to stay on top by making the native experience less terrible. And since it’s worst for big apps like Snapchat and Instagram, they’re mostly trying to solve the big-app dev experience, which in turn is largely dominated by build times.


To fixthat, Google is doing a staggering amount of work on the “official” Android application build system, which is based on the already-complex Gradle system, but then Google piles on a bunch of hairy Android-specific stuff. It’s getting more complex month over month, to the point where even the build engineers don’t understand parts of it anymore. What’s the difference between a build type, a product flavor and a flavor dimension? Good luck with that. But they keep dialing up the complexity because they think these features are important for big shops with big apps.


The irony being that most of the big shops are aggressively dumping it in favor of Buck — Facebook’s Android build system. Google is chasing a dying strategy here.


So while Google seems to understand that there’s a problem, they are doubling down on the solutions that nobody likes: A native stack with an insanely complicated Gradle build system. And they are losing developers. The third-party stacks are gaining market share.


Flanking Attacks


To make matters worse, the development stack isn’t the only assault happening on Android. There are other ways that someone might “steal” Android from Google. One approach is to create a more successful store. One of Google’s biggest locks on Android is the Play Store, which has generated a ton of controversy (at the level of both companies and governments) because Android’s purportedly an open system, but the Play Store is 100% controlled by Google. Cyanogen was a big attempt at a coup, backed by Microsoft and Twitter. And though it failed due to internal political infighting, it was the first serious attempt at Play Store’s jugular.


But guess who else is making a big play with a competing store? You guessed it: Jeff Bezos, because you can’t become the world’s first trillionaire without stealing Android from Google. Well… I like to imagine it would help, anyway. Amazon’s app store is already pretty impressive, and in just about every head-to-head competition I’ve seen between Amazon and Google, Amazon has executed better over time. Watch out!


And as if that weren’t enough for Google to worry about, there is athirdassault on Android, and this one is hitting right where it hurts: In the Ads. Facebook’s Android app has become so large (there have been hundreds and hundreds of engineers working on it for years) that it has sprouted a bona-fide platform, and now you can serve your own ads directly into the Facebook app. For instance the New York Times can buy ad placements there, and all the money goes directly from NYT to Facebook without a dime going to Google. You can imagine how that makes them feel.


WeChat is doing exactly the same thing in China. The WeChat app has become a thriving platform for building and deploying other apps (and ads). It’s like a whole marketplace embedded inside the app itself. Facebook and WeChat mobile apps have become standalone advertising channels.


Let’s be clear: The only reason Google created Android was because it’s an ad channel. Google is an ads company, the biggest one in the world, and they are always always always under attack from companies who want to put your eyeballs intheirchannel instead of one of Google’s channels. That’s what the attack on Net Neutrality is all about, in the final analysis. Telecoms and ISPs want to serve you all the ads, or at least take a cut of what Google and Facebook are making.


Whenever you see a company like Facebook, Google, Amazon or Microsoft mysteriously get into a strange new business, you can bet it’s a channel play. Google Chrome is a channel play for controlling access to the Web. Microsoft’s XBox was a channel play against the PlayStation, which threatened to unseat the PC as the channel for getting online at home. YouTube was a channel play. Instagram and WhatsApp are channel plays. The HBO/Amazon/Netflix content war is a literal channel play. Amazon Echo is a channel play; your home is one of the biggest channel fights going on today. Even Google Maps is a channel play for local ads. Once you start looking, you see channels everywhere.


The bottom line is, companies want you viewing your favorite content (books, movies, games, Natalie Portman sex columns) thoughtheirchannel rather than someone else’s, so that they can get the ad revenue, or at least its little sister, subscription revenue.


Android is probably Google’s most important channel — if not today, then certainly over the next ten years. They can’t afford to lose control of it. But we’ve seen that there are at least three coordinated types of attack happening in different dimensions: The developer ecosystem (React Native and friends), the store (Amazon’s app store and Cyanogen’s rumored successor), and the lightweight in-app marketplaces (Facebook and WeChat, so far). Google’s reactions to each of these threats so far have been… well, let’s just say they’re still on top. For now.


Meanwhile, back at the ranch…


All this might seem like a bunch of useless high-flown speculation (well, I mean, because it is), but it actually affects us down on the ground here at Grab because we have to make important decisions about what technology stacks to use for our mobile apps, which are the windows to the world — channels, that is — for our passengers, drivers, merchants, agents and so on.


If you think there’sany risk at allthat Google might lose control of Android, then your best bet is to use a cross-platform framework, because it hedges your bet via improved portability. And if you’re locked in a fierce competitive race (which we are at Grab) and need to launch faster, you should probably go with something other than Android Native anyway. Android’s still chasing that Gradle train, and that is just never going to be fast, in large part due to legacy issues with Android’s design that are hard to paper over.


Among the cross-platform options, React Native is looking like a winner. It appeals to web developers, which is probably the biggest dev audience worldwide. Hard to compete with that. Grab has recently begun investing in React Native to see if it can live up to its promise, and so far it looks pretty good.


It’s going to be a long time before Grab retires our native Android and iOS apps, since these ports do take time. Which means that if you’re a mobile developer of just about any flavor, that’s great news, because we need you. We have React Native work, Android Kotlin work, and iOS Swift work, all of which are in super high demand worldwide. If your employer doesn’t appreciate you, I recommend looking around. A lot has changed in the past three years.


To summarize the main idea behind this post:Grab needs mobile devs just like everyone else, but those are hard to hire because Android programming is yucky, and everyone knows this except apparently Google, so now the ecosystem is proliferating with competitors trying to make their way the One True Way for programming mobile… which makes it evenharderto hire devs because it’s so fragmented. Whew!


But regardless of your flavor of choice, it’s a good time to be a mobile developer. If you’re a non-mobile dev, you should consider switching tracks for a while. Starting with backend experience and learning mobile development turns you into a “full stack developer”, which is an even rarer and more marketable unicorn.


It’s a good time to be competing to gain control of Android, if you’re into that sort of thing. Lots of companies are. Heck, even other teams at Google are doing it. Grab is not, though we are materially impacted by the outcomes. But there are a lot of big sharks circling the Android boat. Google needs to be careful.


And it’s agreattime to be at Grab. If you’re a professional programmer of any persuasion, particularly in the Seattle or Eastside area, and any of that stuff I said last time about GDP and emerging networks and raw golden opportunity resonated with youat all, then seriously: You should be thinking about heading over here as fast as your legs will carry you.


Heck, take a Lyft.


Closing thought: This is a highly nuanced space, and I’ve oversimplified in several ways. I look forward to the discussion threads.

