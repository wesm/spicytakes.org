---
title: "Some Assembly Required"
date: 2006-10-05
url: https://daringfireball.net/2006/10/some_assembly_required
slug: some_assembly_required
word_count: 863
---


Wil Shipley posted [an interesting essay](http://wilshipley.com/blog/2006/10/pimp-my-code-part-12-frozen-in.html), wherein he complains about Mac OS X APIs that are only available using Carbon. At the heart of his argument is the real difference between Carbon and Cocoa — Cocoa APIs make things a lot easier for developers, and require a lot fewer lines of code. I think Shipley loses track of this main point, though.


For one thing, he starts by calling Carbon a “compatibility library” for “older applications”, and Cocoa a “new application environment”, even though *both* date from the 1980s. Yes, the original Mac OS Toolbox APIs are a bit older than the original NextStep object system, but only by a few years. (In fact, it’s fair to argue that Cocoa, today in 2006, is older than Carbon was back in 2000, when the whole “Carbon is old, Cocoa is new” meme got started in earnest.) “Carbon” is humongous; it’s an umbrella label for a huge number of APIs. Some of these APIs do exist for compatibility with the old Mac OS; but some of them are brand new and *only* exist on Mac OS X. If you count [CoreFoundation](http://developer.apple.com/documentation/CoreFoundation/index.html) as part of Carbon, then in a very real sense it’s fair to say that most of Cocoa sits on top of Carbon. And even if you want to argue that CoreFoundation sits below both Carbon and Cocoa, it’s still the case that [Cocoa’s AppKit framework uses the Carbon HIToolbox](http://www.red-sweater.com/blog/181/the-cocoa-carbon-advantage#comment-13937), etc.


So the argument here shouldn’t be that Carbon is old and Cocoa is new, or that Carbon is bad and Cocoa is good; no, the argument is that Carbon is lower-level and Cocoa is higher-level, and programmers are almost always more productive, write fewer bugs, and have more fun when working with higher-level APIs.


Shipley writes:


> What’s distressing to Cocoa programmers is that there are
> still critically important Apple APIs that are only available
> through the incredibly byzantine and ill-documented Carbon
> libraries, and some groups at Apple are still generating
> Carbon code, under the guise of “Core”.


For examples, he cites (with source code) using QuickTime to manually control a USB video camera, and building a list of FTP sites from items in the user’s keychain.


As Shipley himself points out, nowadays programmers can call Carbon APIs from Cocoa (and Cocoa APIs from Carbon), so it’s not a matter of “*you can’t do that in Cocoa*”. The problem is that you can’t do it in Cocoa *using Cocoa*; you have to use Carbon, and compared to how it might be done if it *were* possible using Cocoa, it’s a pain in the ass.


Using Cocoa, at its best, is like opening a box and getting a toy. Using Carbon is like opening a box and getting a fistful of tiny pieces that you need to assemble into a toy.


The whole Carbon-vs.-Cocoa propaganda thing has, thankfully, died down a bit at the user level in the last few years. It really is, for the most part, not something users ought to be worried about. But it’s definitely still a touchy subject for some Mac developers.


Daniel Jalkut wrote about this last month, in [an essay on calling Carbon from Cocoa and vice-versa](http://www.red-sweater.com/blog/181/the-cocoa-carbon-advantage):


> The saddest thing in all of Macdom is the sight of Cocoa and
> Carbon purists crying in their mailing list beers because a
> given task is “impossible” in the API of their preference. Often
> a fearless API-hopper like Jim Correia or John Stiles will pop
> up and cheerfully announce a one-line solution to their woes. In
> the opposite API than the original poster had hoped, of course.
> “Thanks for the response, but I’d like to keep this as pure as
> possible.”
> Excuse me, I thought you wanted a solution. You idiot! What they
> really mean to say is “I learned this framework 10 years ago and
> I’ll be damned if I have to learn anything new now.”


Shipley’s argument isn’t like that, though. He did slip a wee bit of anti-Carbon FUD into his essay, but he’s not saying that he doesn’t want to use Carbon because he can’t, or because he’s opposed to it for religious or political reasons. He’s saying, *Look, here’s some example Carbon code, and it’d be a whole lot easier to do these things if there were APIs for them in Cocoa.*


One of my favorite programming slogans is [from Larry Wall](http://interviews.slashdot.org/interviews/02/09/06/1343222.shtml), regarding his goals for Perl: “Easy things should be easy, and hard things should be possible.”1


That motto certainly describes the appeal of Cocoa. It’s why Objective-C 2.0 — unveiled at WWDC in August and [coming with Mac OS X 10.5](http://www.apple.com/macosx/leopard/xcode.html) — is gaining things like garbage collection and `foreach`-style `for` loops: they make code that should be easy even easier.


So I think Shipley’s argument could be summarized thusly: Making hard things possible is good, but making hard things easy is even better.


---

1. Which is apparently a reformulation of [Alan Kay’s](http://en.wikiquote.org/wiki/Alan_Kay) “Simple things should be simple, complex things should be possible.” ↩︎



| **Previous:** | [Brand New](https://daringfireball.net/2006/10/brand_new) |
| **Next:** | [BBColors 1.0](https://daringfireball.net/2006/10/bbcolors_1-0) |


PreviousNext