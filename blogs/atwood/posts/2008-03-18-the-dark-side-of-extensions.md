---
title: "The Dark Side of Extensions"
date: 2008-03-18
url: https://blog.codinghorror.com/the-dark-side-of-extensions/
slug: the-dark-side-of-extensions
word_count: 996
---

One of the best things – if not *the* best thing – about [Firefox](http://en.wikipedia.org/wiki/Mozilla_Firefox) is the rich, vibrant ecosystem of [add-ons](https://addons.mozilla.org/en-US/firefox/) that has grown up around it. Almost anything you could possibly want to do with a web browser can be done with Firefox... *if* you’re willing to hunt down the necessary extension. In [Buy the Community, not the Product](https://blog.codinghorror.com/buy-the-community-not-the-product/), I argued that this made Firefox the better browser. That’s still true today.


But relying on extensions and add-ins isn’t the whole story. Not by a long shot. Consider the average user who has no clue how fabulous those Firefox extensions may be, much less where to find them or how to install them. I’m not saying it’s complicated, but **any installation at all is too much work** for a sizable percentage of the audience. They’ll use the browser as it was supplied to them, forever. That’s [the power of defaults](https://blog.codinghorror.com/the-power-of-defaults/).


In [9 things Firefox should steal from Safari](https://web.archive.org/web/20080410001424/http://destraynor.com/serendipity/index.php?/archives/151-9-things-Firefox-should-steal-from-Safari.html), Des highlighted some of the unique and innovative features in the Safari web browser:

- Improved current field highlighting
- Alternate [font rendering](https://blog.codinghorror.com/whats-wrong-with-apples-font-rendering/)
- Cleaner downloads dialog
- Faster HTML rendering
- Simple, painless bug reporting
- Visual incremental find
- Detachable tabs
- Draggable images
- Resizable text areas


All of these features are well worth copying and including in the core Firefox browser. Despite Des’ thoughtful analysis, the avalanche of comments across Digg, Reddit, and Des’ own site had one universal, monotonous response:


> It seems the author simply hasn’t really tried to use Firefox. 5 points can be changed by extensions, two are non existent, one is a Windows issue, and one is disputable.


**Extensions, extensions, extensions.** Indeed, why bother improving the core browser when you can force the user to install five extensions to duplicate that same functionality? This approach doesn’t make any sense to me, and [I think Des agrees](https://web.archive.org/web/20100510145349/http://www.destraynor.com/serendipity/index.php?/archives/2007/08.html):


> Every day I see little things in Safari that could and should be copied. In Safari if I type destraynor.cmo into my url bar, it realizes that there is no .cmo, and looks at previous sites I’ve visited, and sends me to destraynor.com. Firefox doesn’t do that. Not without installing extensions. The majority of internet users, surprisingly, do not feel the need to install custom browser components. When they see Safari do something clever like this they don’t think “Hey, that’s cool, I better check mozilla.org to see if anyone has written an extension to spell check urls,” they just think “Hey that’s cool,” or maybe “Hey that’s cool, I wish Firefox could do that.” That’s why you have to [fight for every inch](http://www.scripting.com/2002/01/12.html).


Since Des’ initial post, [Safari 3.1](http://www.apple.com/safari/download/) was released with even more features. Firefox 3 isn’t quite out yet, but [Firefox 3.0 beta 4](http://www.mozilla.com/en-US/firefox/all-beta.html) offers a fairly complete picture of what the final version of Firefox 3 will look like later this year. The only feature that is no longer an issue on Des’ original list is HTML rendering speed. All the others remain.


Extensions, as a solution to general software and productivity problems, have both dark and light sides.


![](https://blog.codinghorror.com/content/images/2025/04/image-26.png)


Extensions offer wonderful enhancements to Firefox. It’s a huge credit to the Firefox development team that **they made extensions both easy to create and incredibly powerful**. This is something that the Safari and IE teams appear incapable of doing. We can’t even have this discussion about those browsers because their add-on ecosystems are pale shadows of the massive Firefox extension community. The Firefox team absolutely deserves all the market share they’ve earned from that one crucial decision.


But extensions are also an indictment of Firefox. If an extension is wildly popular and everyone urges you to install some “crucial” or “essential” extension in Firefox – **shouldn’t that extension have been baked into the browser in the first place?** If I ran the Firefox development team, every new development cycle, I’d take the list of [top 5 Firefox add-ins](https://web.archive.org/web/20090630214655/https://addons.mozilla.org/en-US/firefox/browse/type:1/cat:all/sort:popular) and *demand that we fold that functionality into the core product*.


Half the value of a robust add-in ecosystem lies in product guidance – users are taking it upon themselves to fill the gaps and holes in your product, and audience metrics tell you exactly which holes truly *needed* filling. Sure, there are some oddball extensions that only a few users might care about – but when extensions reach critical download mass and the same extensions appear repeatedly on best Firefox extension lists, they’re filling a universal need. Ignoring that is just irresponsible software development, pure and simple.


If software developers were doing their jobs properly, an extension ecosystem wouldn’t be necessary – 99% of the features users want and need would be already baked into the shipping software. And yet without a robust, powerful extension ecosystem, I suspect developers have a terrible idea of what features users actually *do* use and want. They’re guessing.


It’s sort of a [Catch-22](http://en.wikipedia.org/wiki/Catch-22).


So when I see a user post an enormous list of Firefox extensions they’ve installed, as in the comments of [this lifehacker post](http://lifehacker.com/355973/make-your-extensions-work-with-the-firefox-3-beta):

kg-card-begin: html


| AdBlockPlus 0.7.5.3
All-In-One Sidebar 0.6.1
Always Remember Password 0.6
BlockSite 0.6
ColorfulTabs 3.0
CustomizeGoogle 0.69
CuteMenus - Crystal SVG 1.9.2
Forcecastfox I10n
Furl Tools 0.8
GMail Notifier 0.6.3.2
Greasemonkey 0.6.8.20070314.0
Image Zoom 0.2.6
Japanese English Dictionary for rikaichan 1.05
No Squint 1.0.1 | PDF Download 1.0.10
PeraPera-kun 0.5.22
Places’ Full Titles 3rc3
PrefButtons 0.3.3
QuickJava 0.4.2.1
Redirect Remover 2.5.3
Remove It permanently 1.0.6.3
Secure Login 0.9.0.6
Session Manager 0.6.1.9
SmoothWheel 0.44.10.20071026
StopAutoplay 0.7.2
Stylish 0.5.1
Temporary Inbox 2.1
User Agent Switcher 0.6.10
XHTML Ruby Support 1.4.20061000801
Xinha Here! 0.12 |


kg-card-end: html

Or when I hear, as I often do, how someone **couldn’t possibly imagine using Firefox without the three or four extensions that they absolutely *must* have**... I’m torn. How many of those nifty extensions are specialized functionality – and how many are crude spackle over missing features that really should have shipped in the box?

[extensions](https://blog.codinghorror.com/tag/extensions/)
[web browser](https://blog.codinghorror.com/tag/web-browser/)
[firefox](https://blog.codinghorror.com/tag/firefox/)
[add-ons](https://blog.codinghorror.com/tag/add-ons/)
[safari](https://blog.codinghorror.com/tag/safari/)
