---
title: "Spatial Navigation and Opera"
date: 2008-02-13
url: https://blog.codinghorror.com/spatial-navigation-and-opera/
slug: spatial-navigation-and-opera
word_count: 984
---

In [Where the Heck is My Focus](https://blog.codinghorror.com/where-the-heck-is-my-focus/), I wondered why web developers don’t pay attention to basic keyboard accessibility issues. I don’t want to navigate the entire web with my keyboard. That’s unrealistic. I was specifically referring to **login pages**, which tend to be quite spartan and minimal. On a simple login web page, the standard keyboard tab, enter, focus order navigation scheme is quite useful and [much more efficient](https://blog.codinghorror.com/logging-in-with-the-keyboard/) than using the mouse.


But why is keyboard navigation so unrealistic for the rest of the web? Probably because **the existing keyboard navigation paradigm was developed for the earliest GUIs**, where forms had at most *dozens* of selectable items.


![](https://blog.codinghorror.com/content/images/2025/03/image-461.png)


Compare with the modern web, where **pages regularly have *hundreds* of selectable items.**


![](https://blog.codinghorror.com/content/images/2025/03/image-460.png)


Presented with a 20-fold increase in selectable items, it’s not too difficult to see why **traditional keyboard navigation techniques completely break down**. They were never designed to handle such complex navigation scenarios. Jan Miksovsky [explains](http://miksovsky.blogs.com/flowstate/2007/11/directional-key.html):


> The first issue is one of scale: the page above has twenty times the number of focusable controls as the simple dialog. A user trying to use the keyboard to reach a link in the middle of the page might have to press the Tab key 125 times to reach it. (Or, if they were exceptionally efficient, they could tab around the other direction and only have to press Shift+Tab 75 times.) The second issue is that the page has a much more complex two-dimensional columnar layout that the dialog, but that layout cannot be captured in the one-dimensional tab order. To the user, the behavior of the Tab key is therefore quite unpredictable.
> The other standard keyboard navigation technique – explicit keyboard shortcuts – are also inadequate for complex user interfaces. Microsoft Windows allows users to move the focus directly to a control on the dialog by pressing a keyboard shortcut, generally the Alt key plus a single letter in the control’s label. (OS/X does this too, although I find it less discoverable and generally weaker in execution.) This system is workable for dialogs with a small number of controls and a reasonable distribution of letter frequencies in control labels, but is obviously unable to scale well beyond a handful of controls.


[Incremental search](https://blog.codinghorror.com/search-if-it-isnt-incremental-its-excremental/) is one way to find what you’re looking for on a complex web page. [Safari does incremental searching](https://web.archive.org/web/20080217100119/http://sarathc.wordpress.com/2007/06/16/incremental-search-of-safari-really-makes-sense/) extraordinarily well, Firefox reasonably well, and IE not at all unless you install a third-party plugin. As useful as incremental search is, it can be a jarring navigational technique.


Jan describes an alternate navigational technique that *can* scale to hundreds of selectable items. It’s not even new. You’ve probably used it before, but not on your desktop or laptop PC. That technique is spatial navigation.


> A much better user interface for navigating screens with lots of elements is already ubiquitous – but not on PCs. It’s found on mobile phone web browsers, which of necessity do a good job at keyboard navigation. **They support two-dimensional directional navigation by using Left, Right, Up and Down arrow keys (or a joystick) to move to the “nearest” element in the corresponding direction.** For example, if you press the Right key, heuristics determine whether there’s an element you might be trying to reach towards the right, and if there are multiple elements, which element you probably want.
> Significantly, **these heuristics respect the rendered visual representation of the page**, not the structure of the document’s object model or the original location of elements at design time. This is necessary to account for the fact that the user may be viewing the page at a different width than the designer used, with different fonts, at different sizes, etc. Directional navigation UIs also tightly connect keyboard focus and scroll position, allowing someone to continually press the Up and Down keys to move through focusable controls and to page over large blocks of text.


Jan said “*directional navigation works so well on mobile devices, I’m hoping it will get built into a browser someday.”* What he apparently didn’t realize is that at least one browser already implements spatial navigation. That browser is [Opera](http://www.opera.com/). In Opera, you can press shift+arrow to move the focus to the next logical selection in that direction.


![](https://blog.codinghorror.com/content/images/2025/03/image-459.png)


Opera’s spatial navigation is fun to play with. Combined with the space bar and arrow keys to scroll the page, it’s a surprisingly effective navigation technique even outside the constraints of mobile browsers where you usually see it. But there are some quirks. It isn’t always obvious what selectable item is next in any particular direction. Also, heavy use of JavaScript page manipulation appears to interfere with spatial navigation in some cases.


Try it yourself. Despite the quirks, **spatial navigation is worlds better than the insanity of pressing tab 125 times**.


It’s too bad Opera doesn’t get more respect. I’m as guilty as anyone; when I’m testing something, I’ll use IE, Firefox, and Safari in that order. Opera isn’t even on my radar. That’s a shame, because as you can see, it’s quite innovative in some areas. It’s also historically [one of the fastest browsers](https://blog.codinghorror.com/a-need-for-speed-and-silence/) on the market. Opera is the default browser on the Nintendo DS and Wii, and I’ve heard nothing but raves for [Opera Mini](http://en.wikipedia.org/wiki/Opera_Mini) and [Opera Mobile](http://en.wikipedia.org/wiki/Opera_Mobile) on mobile phones. Yet Opera’s PC market share remains [vanishingly small](http://www.w3schools.com/browsers/browsers_stats.asp), on the order of 1 percent – a very distant fourth behind the big three. I suppose part of that is Opera’s fault; Opera was sold as a product long after browsers were given away for free. That certainly didn’t help their market share.


Regardless, it’s worth checking out Opera for spatial navigation and other innovations it brings to the table. Now that [the browser wars](https://blog.codinghorror.com/what-if-they-gave-a-browser-war-and-microsoft-never-came/) have heated up again, I hope there will be more cross-pollination of innovative features so *everyone* can benefit.

[accessibility](https://blog.codinghorror.com/tag/accessibility/)
[keyboard navigation](https://blog.codinghorror.com/tag/keyboard-navigation/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[gui设计](https://blog.codinghorror.com/tag/guishe-ji/)
