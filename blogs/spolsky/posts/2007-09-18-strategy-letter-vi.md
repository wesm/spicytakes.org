---
title: "Strategy Letter VI"
date: 2007-09-18
url: https://www.joelonsoftware.com/2007/09/18/strategy-letter-vi/
word_count: 2121
---


IBM just released an open-source office suite called [IBM Lotus Symphony](http://symphony.lotus.com/software/lotus/symphony/home.jspa). Sounds like Yet Another StarOffice distribution. But I suspect they’re probably trying to wipe out the memory of the original Lotus Symphony, which had been hyped as the Second Coming and which fell totally flat. It was the software equivalent of Gigli.


In the late 80s, Lotus was trying very hard to figure out what to do next with their flagship spreadsheet and graphics product, Lotus 1-2-3. There were two obvious ideas: first, they could add more features. Word processing, say. This product was called Symphony. Another idea which seemed obvious was to make a 3-D spreadsheet. That became 1-2-3 version 3.0.


Both ideas ran head-first into a serious problem: the old DOS 640K memory limitation. IBM was starting to ship a few computers with 80286 chips, which could address more memory, but Lotus didn’t think there was a big enough market for software that needed a $10,000 computer to run. So they squeezed and squeezed. They spent 18 months cramming 1-2-3 for DOS into 640K, and eventually, after a lot of wasted time, had to give up the 3D feature to get it to fit. In the case of Symphony, they just chopped features left and right.


Neither strategy was right. By the time 123 3.0 was shipping, everybody had 80386s with 2M or 4M of RAM. And Symphony had an inadequate spreadsheet, an inadequate word processor, and some other inadequate bits.


“That’s nice, old man,” you say. “Who gives a fart about some old character mode software?”


Humor me for a minute, because history is repeating itself, in three different ways, and the smart strategy is to bet on the same results.


## Limited-memory, limited-CPU environments


From the beginning of time until about, say, 1989, programmers were extremely concerned with efficiency. There just wasn’t that much memory and there just weren’t that many CPU cycles.


In the late 90s a couple of companies, including Microsoft and Apple, noticed (just a little bit sooner than anyone else) that Moore’s Law meant that they shouldn’t think too hard about performance and memory usage… just build cool stuff, and wait for the hardware to catch up. Microsoft first shipped Excel for Windows when 80386s were too expensive to buy, but they were patient. Within a couple of years, the 80386SX came out, and anybody who could afford a $1500 clone could run Excel.


As a programmer, thanks to plummeting memory prices, and CPU speeds doubling every year, you had a choice. You could spend six months rewriting your inner loops in Assembler, or take six months off to play drums in a rock and roll band, and in either case, your program would run faster. Assembler programmers don’t have groupies.


So, we don’t care about performance or optimization much anymore.


Except in one place: JavaScript running on browsers in AJAX applications. And since that’s the direction almost all software development is moving, that’s a big deal.


A lot of today’s AJAX applications have a meg or more of client side code. This time, it’s not the RAM or CPU cycles that are scarce: it’s the download bandwidth and the compile time. Either way, you really have to squeeze to get complex AJAX apps to perform well.


History, though, is repeating itself. Bandwidth is getting cheaper. People are figuring out how to precompile JavaScript.


The developers who put a lot of effort into optimizing things and making them tight and fast will wake up to discover that effort was, more or less, wasted, or, at the very least, you could say that it “conferred no long term competitive advantage,” if you’re the kind of person who talks like an economist.


The developers who ignored performance and blasted ahead adding cool features to their applications will, in the long run, have better applications.


## A portable programming language


The C programming language was invented with the explicit goal of making it easy to port applications from one instruction set to another. And it did a fine job, but wasn’t really 100% portable, so we got Java, which was even more portable than C. Mmmhmm.


Right now the big hole in the portability story is — tada! — client-side JavaScript, and especially the DOM in web browsers. Writing applications that work in all different browsers is a friggin’ nightmare. There is simply no alternative but to test exhaustively on Firefox, IE6, IE7, Safari, and Opera, and guess what? I don’t have time to test on Opera. Sucks to be Opera. Startup web browsers don’t stand a chance.


What’s going to happen? Well, you can try begging Microsoft and Firefox to be more compatible. Good luck with that. You can follow the p-code/Java model and build a little sandbox on top of the underlying system. But sandboxes are penalty boxes; they’re slow and they suck, which is why Java Applets are dead, dead, dead. To build a sandbox you pretty much doom yourself to running at 1/10th the speed of the underlying platform, and you doom yourself to never supporting any of the cool features that show up on one of the platforms but not the others. (I’m still waiting for someone to show me a Java applet for phones that can access *any* of the phone’s features, like the camera, the contacts list, the SMS messages, or the GPS receiver.)


Sandboxes didn’t work then and they’re not working now.


What’s going to happen? The winners are going to do what worked at Bell Labs in 1978: build a programming language, like C, that’s portable and efficient. It should compile down to “native” code (native code being JavaScript and DOMs) with different backends for different target platforms, where the compiler writers obsess about performance so you don’t have to. It’ll have all the same performance as native JavaScript with full access to the DOM in a consistent fashion, and it’ll compile down to IE native and Firefox native portably and automatically. And, yes, it’ll go into your CSS and muck around with it in some frightening but provably-correct way so you never have to think about CSS incompatibilities ever again. Ever. Oh joyous day that will be.


## High interactivity and UI standards


The IBM 360 mainframe computer system used a user interface called CICS, which you can still see at the airport if you lean over the checkin counter. There’s an 80 character by 24 character green screen, character mode only, of course. The mainframe sends down a form to the “client” (the client being a 3270 smart terminal). The terminal is smart; it knows how to present the form to you and let you input data into the form without talking to the mainframe at all. This was one reason mainframes were so much more powerful than Unix: the CPU didn’t have to handle your line editing; it was offloaded to a smart terminal. (If you couldn’t afford smart terminals for everyone, you bought a System/1 minicomputer to sit between the dumb terminals and the mainframe and handle the form editing for you).


Anyhoo, after you filled out your form, you pressed SEND, and all your answers were sent back to the server to process. Then it sent you another form. And on and on.


Awful. How do you make a word processor in that kind of environment? (You really can’t. There never was a decent word processor for mainframes).


That was the first stage. It corresponds precisely to the HTML phase of the Internet. HTML is CICS with fonts.


In the second stage, everybody bought PCs for their desks, and suddenly, programmers could poke text anywhere on the screen wily-nily, anywhere they wanted, any time they wanted, and you could actually read every keystroke from the users as they typed, so you could make a nice fast application that didn’t have to wait for you to hit SEND before the CPU could get involved. So, for example, you could make a word processor that automatically wrapped, moving a word down to the next line when the current line filled up. Right away. Oh my god. You can do that?


The trouble with the second stage was that there were no clear UI standards… the programmers almost had too much flexibility, so everybody did things in different ways, which made it hard, if you knew how to use program X, to also use program Y. WordPerfect and Lotus 1-2-3 had completely different menu systems, keyboard interfaces, and command structures. And copying data between them was out of the question.


And that’s exactly where we are with Ajax development today. Sure, yeah, the usability is much better than the first generation DOS apps, because we’ve learned some things since then. But Ajax apps can be inconsistent, and have a lot of trouble working together — you can’t really cut and paste objects from one Ajax app to another, for example, so I’m not sure how you get a picture from Gmail to Flickr. Come on guys, Cut and Paste was invented 25 years ago.


The third phase with PCs was Macintosh and Windows. A standard, consistent user interface with features like multiple windows and the Clipboard designed so that applications could work together. The increased usability and power we got out of the new GUIs made personal computing explode.


So if history repeats itself, we can expect some standardization of Ajax user interfaces to happen in the same way we got Microsoft Windows. Somebody is going to write a compelling SDK that you can use to make powerful Ajax applications with common user interface elements that work together. And whichever SDK wins the most developer mindshare will have the same kind of competitive stronghold as [Microsoft had with their Windows API](https://www.joelonsoftware.com/articles/APIWar.html).


If you’re a web app developer, and you don’t want to support the SDK everybody else is supporting, you’ll increasingly find that people won’t use your web app, because it doesn’t, you know, cut and paste and support address book synchronization and whatever weird new interop features we’ll want in 2010.


Imagine, for example, that you’re Google with GMail, and you’re feeling rather smug. But then somebody you’ve never heard of, some bratty Y Combinator startup, maybe, is gaining ridiculous traction selling NewSDK, which combines a great portable programming language that compiles to JavaScript, and even better, a huge Ajaxy library that includes all kinds of clever interop features. Not just cut ‘n’ paste: cool mashup features like synchronization and single-point identity management (so you don’t have to tell Facebook and Twitter what you’re doing, you can just enter it in one place). And you laugh at them, for their NewSDK is a honking 232 megabytes … 232 megabytes! … of JavaScript, and it takes 76 seconds to load a page. And your app, GMail, doesn’t lose any customers.


But then, while you’re sitting on your googlechair in the googleplex sipping googleccinos and feeling smuggy smug smug smug, new versions of the browsers come out that support cached, compiled JavaScript. And suddenly NewSDK is really fast. And Paul Graham gives them another 6000 boxes of instant noodles to eat, so they stay in business another three years perfecting things.


And your programmers are like, jeez louise, GMail is huge, we can’t port GMail to this stupid NewSDK. We’d have to change every line of code. Heck it’d be a complete rewrite; the whole programming model is upside down and recursive and the portable programming language has more parentheses than even Google can buy. The last line of almost every function consists of a string of 3,296 right parentheses. You have to buy a special editor to count them.


And the NewSDK people ship a pretty decent word processor and a pretty decent email app and a killer Facebook/Twitter event publisher that synchronizes with everything, so people start using it.


And while you’re not paying attention, everybody starts writing NewSDK apps, and they’re really good, and suddenly businesses ONLY want NewSDK apps, and all those old-school Plain Ajax apps look pathetic and won’t cut and paste and mash and sync and play drums nicely with one another. And Gmail becomes a legacy. The WordPerfect of Email. And you’ll tell your children how excited you were to get 2GB to store email, and they’ll laugh at you. Their *nail polish* has more than 2GB.


Crazy story? Substitute “Google Gmail” with “Lotus 1-2-3”. The NewSDK will be the second coming of Microsoft Windows; this is exactly how Lotus lost control of the spreadsheet market. And it’s going to happen again on the web because all the same dynamics and forces are in place. The only thing we don’t know yet are the particulars, but it’ll happen.
