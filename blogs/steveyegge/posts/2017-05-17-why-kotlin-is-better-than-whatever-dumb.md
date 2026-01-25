---
title: "Why Kotlin Is Better Than Whatever Dumb Language You're Using"
date: 2017-05-17
url: https://steve-yegge.blogspot.com/2017/05/why-kotlin-is-better-than-whatever-dumb.html
word_count: 3019
---

Ah, clickbait.  Where would the internet be without it?  The answer will shock you!
But seriously, I didn't mean to insult your favorite language… much.  After all, your language of choice is probably getting better at a glacial pace.  Right?  If your language isn't dead, then it's gradually getting better as they release updates to it.
How slowly, though?  Well... If the language you're using happens to be Java, then you've no doubt realized that by the time Java becomes a really good language, you'll be dead.  Loooong dead.  I know we don't like to contemplate our own mortality, but when you plot the trajectory of Java from its birth 20+ years ago to its full knee and hip replacement with Java 8, you can't help but wonder, "Am I going to be stuck with this for literally the rest of my life? What if this is as good as it gets?"
Anyhoo, I ran across the old language question again because I finally tried my hand at Android development.  I have an iOS client for my old game
[Wyvern](http://reddit.com/r/wyvernrpg)
, and I decided somewhat recently to take the plunge and write an Android version.  I didn't realize that it would turn into a language question (as in, "What the hell am I doing with my life?")  But then, if you've done any Android programming at all, you'll know that this is in fact a
burning
question in Android-land.
My first attempt at doing Android was last summer, and my god it sucked.  I mean, they warned me.  Everyone warned me. "The APIs are terrible", they all said.  I can't say I wasn't warned.
How terrible could they
be
, though?  It's just Java, right?
Legacy Yuck
Unfortunately -- for long complicated legacy reasons that nobody cares about -- some of Android's core APIs really are bad.  I mean baaaaad bad.  Shut the book, take a deep breath, and go out for coffee bad.  The warnings were spot on.
It's a mixed bag, though.  A lot of their APIs are just ducky. I found plenty of things that are hard in iOS and easy in Android.  Product flavors, the Downloads service, findViewById(), the Preferences activity, etc.  There is a ton of stuff in Android that has no equivalent at all in iOS, so in iOS you wind up writing gross hacky code or building elaborate libraries to work around it.
But!  There's a big "But".
When you're learning and writing for Android, everyone focuses on the bad APIs
, for the same reason that when you're in traffic you focus on the red lights, not the green lights. You tend to judge your commute by how many red lights it has.
And Android has some pretty big red-light APIs.  Fragments, for example, are a well-known Flagship Bad API in Android.  In fact the entire lifecycle is maddeningly awful, for both Activities and Fragments.  iOS is living proof that it didn't have to be that bad.  There's no defending it.  It's so bad that when I tried it for the first time last summer, I just gave up.  Threw in the towel.  Screw it, I said to myself -- I'll hire someone to do this port, someday.
And I didn't look at Android programming again for another half a year.
Rescued by Russians
I kept hearing about this new-ish programming language for the JVM and Android called Kotlin.  From Russia, of all places.  More specifically, from JetBrains, the makers of the world-famous IntelliJ IDEA IDE, whose primary claim to fame is its lovely orange, green, purple and black 'Darcula' theme.

![](https://lh6.googleusercontent.com/eNcWzzfFCrHOrcZXnPRuCJbET7RgsnMzTyFNDtgrCdvrKoW5nbZUbcAScGVPi7Cp1rLG4HcsH4BH2kC6vDCQ237A8-VVBSy97PWQKhMjuiOuf3ogNSpsc8QnnDYO_FIEoiPkVlVI)

Figure 1:  A thousand-year-old vampire expressing his excitement over Java 8.
So why is it called Kotlin?  Well, there's a clear play on incrementing the 'J' in Java.  Beyond that, one can only assume that 'Kremlin', 'Khrushchev' and 'KGB' were already taken, probably by UC Berkeley.  So they did the next best thing and named it after a Russian military base.  It's not a bad name, though.  You get used to it.
Last year I noticed that Kotlin had a fair amount of buzz.  Not hype, just... buzz.  People were low-key buzzing about it.  So, sure, whatever, I took a look, just like I've done for fifty or a hundred other languages in the past 15 years, on my Quest to Replace Java with Anything Reasonable.
Kotlin first impressions
When I first looked at Kotlin, I honestly didn't think there was any chance I'd use it in real life, not even the remotest possibility.  I was just window shopping.  First glance?  Nothing immediately wrong with it. It's clean and modern. If anything it felt almost hipsterish in its adoption of all the latest new trends in language design.  But there are oodles of languages like that.  Just look at Rust.  Another solid, appropriately-named language that almost nobody uses.  How "good" a language is doesn't really matter from an adoption standpoint.
Kotlin came across as strangely
*familiar*
, though, and eventually I realized it's because it looks like Swift -- which I was slow to notice because my iOS app is in Objective C for irritating legacy reasons.  And of course now I know that's backwards:  Kotlin predates Swift by several years, so it's more accurate to say that
[Swift is like Kotlin](http://nilhcem.com/swift-is-like-kotlin/)
.
But none of this made me want to sit down and
*use*
it.  Kotlin was just another decent-looking language, and as a working stiff, I didn't really feel like putting in the effort to learn it well enough to do anything real.
From Kotlin Experiment to Java Expatriate
I don't remember exactly when or how I fell in love with Kotlin.  I can tell you I sure as hell wasn't expecting it.
As best I can remember, my players had been begging me to do an Android version of my game. It launched to the Apple App Store in December, and within a few weeks, tons of old fans emerged to tell me that they couldn't play unless it was on Android.  So, despite my swearing off Android "forever", I decided I'd better give it one more try.  But
something
had to change -- I wasn't going to be able to stomach the vanilla Android Java programming language experience.  I needed a framework or whatever, to ease the pain.
In mid-January I did a quick-and-dirty evaluation and decided to try Kotlin, which also targets the Android Dalvik and Art runtimes. I think my evaluation was equal parts (a) Kotlin buzz, (b) wishing I'd written my iOS app in Swift, and (c) Kotlin had some sort of clever Android DSL called Anko, which I never wound up using, but which initially piqued my interest.
So I took it for a test drive. And within maybe four or five weeks, just like that, I was rewriting my 20-year-old game
server platform
in Kotlin.  One month of using Kotlin and I was
sold
.  I mean, I'm not knocking Scala or any of those other languages, but for an ordinary working clod like me, Kotlin is
perfect
.  I just want street food, you know?  Scala is nice but it's just too fancy for me, all frog legs and calf brains and truffled snails.  I'm too blue-collar to use Clojure or Scala or any of those guys.
It only took maybe 3 days to learn Kotlin well enough to start busting out code, fully aware that I didn't know what the hell I was doing, but knowing the language and IDE were doing a great job of keeping me out of trouble anyway.
And once I was a bit fluent, well, wow.  I'm so jaded that I didn't think it was possible to love a language ever again, but Kotlin is just gorgeous.  Everything you write in it feels like you made something cool.  I've certainly felt that way with other languages before.  But most of them had
*really*
steep learning curves.  Kotlin is just butter: Tailor-made for us Java programmers who are still sort of scratching our heads over Java 8's parallel streaming filterable collecting scheduled completable callbacking futuring listening forking executor noun kingdom.  Kotlin gives you all the same power -- substantially more, actually, with its coroutines support -- but makes it way easier to
*say stuff.*
Java 8 lets you say interesting things, but you have to do it with a mouthful of sand.
I think a fair share of why Kotlin is so easy to pick up, though, owes to its IDE support.  The IDE support for pretty much every other JVM or Android language (besides Java) tends to be bolted on by a couple of community volunteers.  Whereas Kotlin is made by world-class IDE vendors, so right from the start it has the best tooling support
ever
.  How many languages can you name that were built with IDE support from the ground up?  Languages don't usually evolve like that; in fact many language designers outright eschew IDEs. (Hi Rob!) The only other one I can think of offhand is C# -- and C# is easily one of the best languages on earth, hands-down.
The upshot of being an IDE-first language is that you can type pretty much anything even
*approximately*
correct in a Kotlin buffer, and the IDE will gently tell you what you meant to type.  Heck, you can even paste in Java code and it'll convert it for you automatically. If you like Java's IDE support, well, I'm pleased to report that Kotlin has pushed that experience to unprecedented levels.  Even ex-Microsoft engineers tell me, "I used to think Visual Studio was the unbeatable flagship IDE, but IntelliJ is actually better!"  I mean, I don't know Visual Studio, so I'm just relating what they say.  But I'm betting IDEA is at least on par with VS.
Of course, I always need to switch over to Emacs to get real work done.  IntelliJ doesn't like it when you type fast.  Its completions can't keep up and you wind up with half-identifiers everywhere.  And it's just as awful for raw text manipulation as every other IDE out there.  So you need to use both.  The Emacs Kotlin support is unfortunately only so-so right now, but presumably it'll improve over time.  I constantly switch back and forth between Emacs and IntelliJ and I'm getting by.  Good enough for now.
And there you have it.  I spent over a decade searching for a language to replace Java.  I mean I looked
*hard.*
Ironically,
it was only after I gave up that it finally came along.  Go figure.  Kudos to JetBrains for an amazing achievement.
Android:  Kotlin's Killer App
It's nigh-impossible for any new language to get traction these days.  That's not to say there are no new languages.  There are neat new ones almost every year!
But nobody will ever,
*ever*
use them.  It's hard bordering on impossible.  The language market is fully saturated.  The
only
way a new language can make a big splash -- and I think this has been true for at least ten, maybe twenty years -- is for it to have a "killer app". It needs a platform that everyone wants to use so badly that they're willing to put up with learning a new language in order to program on that platform.
It turns out the perfect killer app here -- and this brings us full circle -- is Android's crappy Red Light APIs.  When you're zooming along the road in Android-land, every time you hit an API that stops you in your tracks, you curse the platform.  It doesn't actually matter how many
good
APIs Android has, as long as there are sufficiently many bad ones to make you pause and look around for big solutions.
And boyo, do big "solutions" ever abound in Android.  For starters, there are a bunch of Java annotation processors, which are a sure sign there's a language problem afoot.  And there are a bunch of mini-frameworks like (say) Lyft's Scoop.  There are even full-on departures from Android:  React Native, Cordova, Xamarin, Flutter and so on.  Make no mistake -- people are looking for alternatives.
When you have a big gap like that, there's an opportunity for a language-based solution.  And unsurprisingly, the full-on departures are all based around specific languages that aren't Java.
Kotlin's competitive advantage, though, is that it's
not
a full-on departure.  It's completely 100% interoperable and even interminglable with Java, almost (though not quite) to the extent that C++ was to C.  Kotlin feels like an evolutionary step.  You can just start mixing it right into your existing Android project, right there in the same directories, and call back and forth without batting an eyelash.
All the other big Android platform contenders force you to learn and use a completely different language and platform, each with its own paradigms and idioms and quirks.  Kotlin just lets you program Android like regular old working-class Android programmers do.  It's all the same APIs, but they're somehow
better
now.  It feels an order of magnitude better.
I was first in line to throw the Android book at the wall and give up last summer, but now with Kotlin I'm finding Android programming is, dare I say it -- enjoyable?  I think this suggests that Android's "bad" APIs weren't all that bad to begin with, but rather that Java has been masking Android's neat functionality with a bunch of Java-y cruft.
Kotlin manages to help you route around just about all of Android's Red Lights, and turns the experience into something that on the whole I now find superior to iOS development.  Well, at least for Objective-C -- I'm sure Swift is awesome.  Because it's like Kotlin!
What I specifically like about Kotlin
Well now, the
specifics
will be another large write-up, so I'll have to do a separate post.  Here I'll just mention a few high-level generalities.
- It works like Java.  It's not "weird" like Clojure or Scala (and let's face it, they're both pretty weird.)  You can learn it quickly.  It was obviously designed to be accessible to Java developers.
- It's safer than Java.  It provides built-in support for many things that are handled in Java these days with annotation processors -- override checking, nullability analysis, etc.  It also has safer numeric conversion rules, and although I'm not sure I like them, I have to appreciate how they force me to think about all my number representations.
- It's interoperable with Java.  And I mean their interop is flawless.  I've seen too many JVM languages go down in flames because you couldn't subclass, I dunno, a static inner class of a nonstatic inner class, or whatever weird-ass edge case you needed at the time.  Kotlin has made Java interop a top priority, which means migration to Kotlin can be done incrementally, one file at a time.
- It's succinct.  I'm a bit of a golfer, I'll be honest.  All else being equal, I like shorter programs that do the same thing, if they're clear enough.  Kotlin makes for a great round of golf.  On average I find it to be about 5-10% shorter than the equivalent Jython code (which is sort of my gold standard), while remaining more readable and *far* more typesafe.
- It's practical.  Kotlin allows multiple classes per file, top-level functions, operator overloading, extension methods, type aliasing, string templating, and a whole bunch of other bog-standard language features that for whatever reason Java just never adopted even though everyone wanted them.
- It's evolving fast.  For instance they just launched coroutine support, which is going to provide the foundation for async/await, generators and all your other favorite non-threaded concurrency features.
- It's unashamed.  Kotlin often borrows great ideas from other languages, and doesn't try to hide it.  They'll say, "We liked C#'s generics, so we did it that way."  I like that.
- It's got DSLs.  No DSL should ever be created without serious consideration of the alternatives -- but a DSL done well can be a powerful tool.  Look at Gradle's DSL, for instance, in comparison to the thousands of lines of XML in a typical Maven project.  Kotlin makes that kind of thing easy.
- It's got one hell of an IDE.  Lately I've taken to writing new files in Emacs, which lets me bust out a ton of code very quickly, code which just happens to be full of horrible errors.  And then I open it in IntelliJ and hit Alt-Enter like 50 times while the IDE fixes everything for me.  It's a great symbiosis.
- It's fun.  Kotlin is just plain fun.  Maybe it's subliminal advertising, since their keyword for declaring methods is fun.  But it's somehow turned me from a surly professional programmer into a hobbyist again.

Anyhoo, you get the idea.  I'm packed up and moving into a new neighborhood called Kotlin
.  I've raved about other languages plenty of times before, but never once, not
ever
, did I rewrite any of my precious Java game server code in any of them.  But here I am, busily rewriting everything in Kotlin as fast as I can.
I know a few other programmers who've also full-on converted to Kotlin. Most of them beat me to it by at least a year or two.  We buzz about it sometimes.  "Kotlin makes programming fun again," we tell each other.  The funny thing is, we hadn't fully grasped that programming had become
*non-fun*
until we tried Kotlin.  It takes you back to when you were first learning programming and everything seemed achievable.
Once again, big kudos to JetBrains.  They've done an amazing job with this language.  I am hats-off impressed.
Is Kotlin better than whatever dumb language you're using?  I think so.  Certainly so, if the language you're using happens to be Java.  If your daily routine involves coding in Java, I think you'll find Kotlin is an unexpected breath of fresh air.  Let me know what you think!
Disclaimer:  These are my own personal opinions based on personal Android development, and are not endorsed in any way by my employer nor JetBrains.