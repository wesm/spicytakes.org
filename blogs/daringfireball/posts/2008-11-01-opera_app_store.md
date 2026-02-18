---
title: "Regarding Opera Mini and the App Store"
date: 2008-11-01
url: https://daringfireball.net/2008/11/opera_app_store
slug: opera_app_store
word_count: 1210
---


[**Update:** Addendum regarding iPhone SDK guideline 3.3.2 appended.]


I’ve done some digging on this “Opera Mini was rejected from the App Store” story, and the truth appears to be very different than what has been reported and assumed.


It all started with this paragraph [from Saul Hansell on the NY Times Bits weblog](http://bits.blogs.nytimes.com/2008/10/27/opera-sings-an-ode-to-browsers-everywhere/), regarding Opera CEO Jon Stephenson von Tetzchner:


> Mr. von Tetzchner said that Opera’s engineers have developed a
> version of Opera Mini that can run on an Apple iPhone, but Apple
> won’t let the company release it because it competes with Apple’s
> own Safari browser.


Note, though, that this is not a quote from von Tetzchner — he’s being paraphrased by Hansell.


My understanding, based on information from informed sources who do not wish to be identified because they were not authorized by their employers, is that Opera has developed an iPhone version of Opera Mini, but they *haven’t even submitted* it to Apple, let alone had it be rejected.


One thing I hadn’t realized before is that Opera has two different mobile browsers: [Opera Mini](http://www.operamini.com/) and [Opera Mobile](http://www.opera.com/products/mobile/). Opera Mobile is pretty much a traditional, regular web browser. It’s Opera, but stripped down and optimized for mobile platforms. Opera Mini, though, is something else. Rather than a web browser that interacts with web sites directly, Opera Mini goes through proxy servers run by Opera.


In a nut, it works like this: You request a URL in Opera Mini. Opera Mini makes the request to a proxy server run by Opera. Opera’s proxy server connects to the web server hosting the requested URL, and renders the page into an image. This image is then transmitted (in a proprietary format called OBML — Opera Binary Markup Language) to the Opera Mini client. Opera Mini displays the rendered image on screen. This may sound convoluted, but apparently the result is very effective — it’s faster to transmit, because only OBML (a compressed binary format) is transmitted to the mobile device over the phone network, and far faster to render on slow mobile processors.


It is Opera Mini, not Opera Mobile, that Hansell indicated that Apple rejected. So, [my speculation](http://daringfireball.net/linked/2008/10/30/opera-iphone) that it was rejected from the App Store for running its own JavaScript interpreter was wrong — Opera Mini is really only a thin client that knows how to display OBML. It doesn’t even render HTML, let alone contain a full JavaScript interpreter. (Chris Mills wrote a piece on the Opera developer weblog last year [regarding Opera Mini and JavaScript](http://dev.opera.com/articles/view/javascript-support-in-opera-mini-4/).) OBML is more like PDF than HTML. So in theory, I think a version of Opera Mini that complies with the iPhone SDK Agreement could be developed.


However, the version that Opera *has* developed for the iPhone is problematic in other ways. The cross-platform code base for the Opera Mini client software is written in Java. The assumption being that it should run on any mobile phone with a Java ME virtual machine. The iPhone, of course, doesn’t support Java in any form.


On the Opera Labs web site in April, Chris Mills [described how they ported Opera Mini to Android](http://labs.opera.com/news/2008/04/10/). Android uses the Java programming language for development, but doesn’t use a standard Java virtual machine; instead, for Android, Google has developed [their own virtual machine called Dalvik](http://code.google.com/android/what-is-android.html). Here’s Mills’s description of how Opera ported it for Android:


> We decided to use the existing Opera Mini code base (even the
> binary package) instead of creating a separate port, to save on
> resources. We created a special wrapper that translates Java ME
> (mostly MIDP) API calls into Android API calls. The tool used was
> [MicroEmulator](http://www.microemu.org/) — this is an open source (LGPL) implementation of
> Java ME that runs on top of Java SE. The lead Opera Mini Android
> developer is also the lead developer of MicroEmulator, so it was
> an inspired choice! The Android platform is similar to Java SE,
> with the exception of several libraries normally included in Java
> SE (like AWT/Swing — these are excluded because they would likely
> be too heavy to fit into the embedded environment.) It is
> therefore fairly simple to port MicroEmulator to run inside
> Android environment. The only major task was to replace the
> AWT/Swing graphics backend of MicroEmulator with Android specific
> APIs.


So in short, they’ve written their own bridge to run Java ME bytecode on Android.


If what they’ve done for the iPhone is along the same lines — that they’ve gotten a Java ME runtime running on the iPhone — it’s clearly outside the bounds of the iPhone SDK Agreement. The guideline in question is rule 3.3.2, which reads:


> 3.3.2 — An Application may not itself install or launch other
> executable code by any means, including without limitation through
> the use of a plug-in architecture, calling other frameworks, other
> APIs or otherwise. No interpreted code may be downloaded and used
> in an Application except for code that is interpreted and run by
> Apple’s Published APIs and built-in interpreter(s).


My somewhat informed hunch is that the iPhone version of Opera Mini that von Tetzchner alluded to in his interview with Hansell is running only on jailbroken iPhones. If it’s using APIs only available on jailbroken iPhones, it might not even *run* as it stands today on a standard iPhone using only the official APIs.


What Opera would need to do to have a version of Opera Mini they could submit to the App Store would be to port the entire client software to the C and Objective-C APIs officially supported on the iPhone. It could well be that even then, Apple would reject it from the App Store on anti-competitive grounds — but contrary to this week’s speculation, that has not happened.


And I hope it wouldn’t, because Opera Mini sounds like a very cool app.


## Addendum


Several readers dispute my interpretation of rule 3.3.2, arguing that it does not forbid interpreters in general. The key word in the clause is “downloaded” — that you cannot ship an iPhone app containing an interpreter which allows you to download additional executable content, circumventing the App Store. For example, a generic “Flash Player” app which allowed you to download directly to your iPhone games and utilities written in Flash — that’s the sort of thing 3.3.2 forbids.


An app which contains an interpreter that only executes scripts or bytecode that is self-contained within the app bundle, however, should be permissible under this guideline. And there are, apparently, apps that are shipping through the App Store today using just such technologies.


There are even commercial developer projects like Innnaworks’s [AlcheMo](http://www.innaworks.com/alcheMo-for-iPhone.html), which translate J2ME Java apps to native iPhone apps, and [Unity3D](http://unity3d.com/), a game development framework based on Mono, using JavaScript, C#, and Python, but which outputs native ARM assembly code and, thus, native iPhone apps.


So there may well be nothing in the iPhone SDK Agreement that would forbid Opera Mini from appearing in the App Store. Again, though, just because an app doesn’t violate the rules doesn’t mean Apple will accept it.



| **Previous:** | [The Richard Solo iPhone/iPod Backup Battery](https://daringfireball.net/2008/10/richard_solo_battery) |
| **Next:** | [iPhone-Likeness](https://daringfireball.net/2008/11/iphone_likeness) |


PreviousNext