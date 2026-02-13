---
title: "The infinite music collection"
date: 2006-11-09
url: https://www.joelonsoftware.com/2006/11/09/the-infinite-music-collection/
word_count: 1170
---


Every Sunday morning when I was 12, I would listen to [Casey Kasem](http://en.wikipedia.org/wiki/American_Top_40) on KQEO and write down a list of any new or upcoming songs. Then I would take my weekly allowance of $5 straight to the record store and spend it on 45s. They were a dollar each. Eventually I had a pretty good collection of, um, maybe 100 records, which my mother is now begging me to throw out.


What I never imagined is that when I grew up, I’d be able to expand my record collection to about 2,500,000 songs for just under $10 a month. I’ve been subscribing to [Rhapsody](http://www.rhapsody.com/) (formerly Listen.com, now owned by Real) for the last four years or so, and it’s a great way to listen to music at the computer.


But laptops have lousy speakers, and I had been looking for a way to pump the music from the computer into other rooms of the house, so last January I finally got a [Sonos](http://www.sonos.com/) system, which is probably the coolest piece of technology I’ve ever bought. Ever.


It’s kind of a confusing system–a combination between a stereo and a computer and a wifi network–so let me explain a bit how it works.


First, you get some ZonePlayers: one for each room where you want music. There are two kinds of ZonePlayers. The big one has its own amplifier. You just plug speakers into it. The little one doesn’t have an amplifier. You plug it in as an aux input on an existing stereo system.


You can get up to 32 of these. I bought three: one in the living room, one in the kitchen, and one in a bathroom. Usually, you put one of the ZonePlayers near your computer and connect it with an ethernet connection to your network; all the other ZonePlayers magically find each other using WiFi, so you don’t have to connect *anything*. It really is magical. The ease of configuration and setup is astonishing. It’s about ten times easier than installing a printer. It’s fifty times easier than getting Bluetooth to work. The Sonos developers obviously put a huge amount of work into making setup and configuration completely painless.


Next, you get one (or more) handheld controllers. These also use WiFi, and they also find the rest of the system pretty much automatically. They have a terrific user interface, an iPod-like thumbwheel, a big bright LCD color screen, and all kinds of brilliant UI touches. For example, to save batteries, the screen dims when you put it down, but if you pick it up again, a motion detector lights up the screen.


Finally, you can install the controller software on any home computers you have: Windows or Mac. This is a desktop application that more or less behaves exactly like the handheld controllers.


Now you pick up any of the controllers anywhere in the house, tell it what rooms you want to control, and browse through your music collection. You can play any music files stored on any attached computer: MP3s, WMAs, AACs, OGGs, etc. You can play internet radio stations–I use this to listen to Seattle’s NPR station to hear All Things Considered three hours later than I can get it in New York. If you want to play music from an iPod, an old vinyl turntable, or an eight track tape player, just plug it into the back of any ZonePlayer.


And, in the ultimate coolness, if you get a subscription to Rhapsody Unlimited, you can browse and play any of Rhapsody’s 2,500,000 songs anywhere in your house.


So now if one of my guests is complaining about the music, I hand them the controller, and they browse around for something they like and play that instead.


The one thing I can’t stop talking about is what a nice job Sonos has done with the user interface. This really is a zero-configuration system. Everything is easy. A long time ago [I wrote](https://www.joelonsoftware.com/uibook/chapters/fog0000000059.html): “Every time you provide an option, you’re asking the user to make a decision. That means they will have to think about something and decide about it.” Users don’t want to decide if the WiFi network should use WEP or WPA. They *do* want to decide whether to listen to the Big Mountain version of *Baby, I Love Your Way* or the Peter Frampton version. Or one of the ten other versions Rhapsody has online (check out Mig Ayesa’s). No extra charge.


**Geek Stuff**


I asked Nick Millington, the Director of Software Engineering at Sonos, to tell me a little bit about the software development environment. It turns out the controller and the ZonePlayers are running Linux. “We started with a standard Linux kernel,” he told me, “then added some of our own device drivers for audio, our buttons, scroll wheel, and other controls, and networking (the latter employing strict Office Hungarian in its source code I might add, in possibly a ‘first’ for Linux kernel modules).”


More from Nick: “All of our applications use a shared code layer written in C++ for their basic network communications protocol stack. The controller applications share a ‘household’ data model that manages knowledge of the set of ZonePlayers that you own, how they are linked together, what music is playing, and so forth. Finally, there is a platform specific UI layer for each controller: a custom-built UI layer on the CR100, a Win32 UI based on WTL (Windows Template Library) on Windows, and a Cocoa/Objective C UI layer on the Macintosh. WTL and Cocoa have both worked out well for us. WTL succeeds in taking away a lot of the drudgery of programming directly against the metal without hiding how Windows actually works to the point of being dangerous because developers forget how to fly without the autopilot. Cocoa has been nice as well–I’m sure everyone in the Mac world knows about this, but coming from Windows I found its approach to memory management (where each pump of the message loop gets you effectively a fresh ‘heap’ that is automatically cleared when returning to the message loop) pretty cool. It allows you to actually write code that returns something like a string, without putting in place the overhead of a garbage collection scheme.


“We use the de facto ‘native’ compilers for the platform we are building on (gcc for Linux, MSVC for Windows, and the gcc that comes with Xcode on the Mac). It has been relatively easy to keep our code portable across these 3 compilers, which we enforce by doing daily builds on all the platforms. The build is all wrapped up into one nightly cron job that checks everything out of source control, kicks off the Linux builds, contacts the Windows and Mac build machines to do their part of the work, and waits for everything to finish up. Then end product is an ‘online update’ package that gets posted directly to our intranet upgrade server and allows testers to install our daily builds on all the hardware in their test systems.”
