---
title: "‘Web Kit’ vs. ‘WebKit’"
date: 2006-05-15
url: https://daringfireball.net/2006/05/web_kit_vs_webkit
slug: web_kit_vs_webkit
word_count: 526
---


Question for Apple: Is it “Web Kit” or “WebKit”?


As a stickler for detail and consistency, this has been driving me
nuts ever since the framework was announced. Apple’s inconsistency
regarding whether there’s a space in the name is borderline
comical. I mean, just look at the [Apple Developer Connection
page for “Internet & Web”](http://developer.apple.com/internet/safari/) technologies, where both spellings
appear nearly side by side:


A year or so ago, I checked with someone in Apple’s documentation
group, and he stated categorically that the official spelling was
“Web Kit”, with the space. Not surprisingly, the [Web Kit
Objective-C Reference](http://developer.apple.com/documentation/Cocoa/Reference/WebKit/ObjC_classic/index.html), which is produced by Apple’s
documentation group, consistently uses “Web Kit”. And, on the schizo
ADC web page referenced above, “Web Kit” appears seven times;
“WebKit” only twice.


However, on [this page](http://developer.apple.com/opensource/internet/webkit.html), “WebKit” beats “Web Kit” eight to *zero*.
Plus, the [WebKit Open Source Project](http://webkit.opendarwin.org/)’s web site is mostly
consistent with its use of the “WebKit” spelling, and judging from
their [Surfin’ Safari weblog entries](http://webkit.opendarwin.org/blog/) and their [posts](http://opendarwin.org/pipermail/webkit-dev/2006-April/000896.html) to
the mailing list, the developers working on the code have settled
upon the closed-up “WebKit”.


As near as I can tell, the official names for each of the Cocoa kits
include a space:

- [I/O Kit](http://developer.apple.com/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/chapter_1_section_1.html)
- [PDF Kit](http://developer.apple.com/cocoa/pdfkit.html)
- [QuickTime Kit](http://developer.apple.com/documentation/QuickTime/Conceptual/QTKitProgrammingGuide/Chapter01/chapter_1_section_1.html)
- [Search Kit](http://developer.apple.com/documentation/UserExperience/Conceptual/SearchKitConcepts/searchKit_intro/chapter_1_section_1.html)


But then there’s the granddaddy of all Cocoa kits, the [Application
Kit, a.k.a. AppKit](http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/ObjC_classic/Intro/IntroAppKit.html). “Application Kit” is the official name of
the framework, but “AppKit” is an accepted and frequently-used
abbreviation — for example, the title of the aforelinked document
is “AppKit The Application Kit”.


So I think what has happened with Web Kit is that the framework’s
name does (and should, for the sake of consistency) have a space,
but that because the closed-up “AppKit” is both accepted and
commonly used, the closed-up “WebKit” is what comes naturally to
Cocoa programmers. I.e. that in the same way that Application Kit is
commonly abbreviated “AppKit”, Web Kit is commonly abbreviated
“WebKit”.1


We don’t frequently see this erroneous closing-up of kit names with
I/O Kit or PDF Kit because closing up their names looks bad.
(All-capital words seldom read well in CamelCase.) “SearchKit”, on
the other hand, looks reasonable, and judging by [Google results](http://www.google.com/search?client=safari&rls=en&q=searchkit+cocoa&ie=UTF-8&oe=UTF-8),
it does in fact get used.


But unlike Application Kit/AppKit, which feels like a legitimate and
useful abbreviation in that the short form is both easier to
pronounce and to type, Web Kit/WebKit just looks like inconsistent
spelling. They’re pronounced the same, and unless you have two
broken thumbs, it’d be hard to argue that “WebKit” is easier to type.


[Plug them into GoogleFight](http://www.googlefight.com/index.php?lang=en_GB&word1=%22web+kit%22&word2=webkit) and “WebKit” absolutely kicks “Web
Kit”’s ass; but that doesn’t make it right. My gut feeling is thus
that “WebKit” is a mistake. But I don’t really care which spelling
Apple settles on, I just want it settled.


---

1. The fact that WebCore, the lower-level HTML rendering
engine at the heart of Web Kit, is universally spelled with no
breaking space probably contributes to the use of “WebKit” as well. Not to mention the whole “web site” vs. “website” can of worms.↩︎



| **Previous:** | [The Last Pixel](https://daringfireball.net/2006/05/the_last_pixel) |
| **Next:** | [Confidence Game](https://daringfireball.net/2006/05/confidence_game) |


PreviousNext