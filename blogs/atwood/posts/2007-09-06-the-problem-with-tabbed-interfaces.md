---
title: "The Problem With Tabbed Interfaces"
date: 2007-09-06
url: https://blog.codinghorror.com/the-problem-with-tabbed-interfaces/
slug: the-problem-with-tabbed-interfaces
word_count: 1041
---

Cyrus Najmabadi* [hates tabs in web browsers](https://web.archive.org/web/20071101083737/http://blogs.msdn.com/cyrusn/archive/2005/04/10/406971.aspx):


> Ok, I seriously don’t get tabs on Windows. Hell, I don’t get tabs on OSX either. In the latter there’s a great system called Expos, and in the former the taskbar does the job. Once I start using tabs, things go all to hell. On OSX, I can’t tell which FireFox/Safari window has the tab I want (since it’s too small). In Windows I find myself scanning the taskbar for a site I was looking at, but I can’t find it because the taskbar only lists the currently active tab. This makes it so difficult to actually find the site I want and it ends up being far slower than just having a window available for each site.


Initially I disagreed with Cyrus. However broken tabbed browsing may be, it’s still a better solution than any of the existing alternatives. For example, Microsoft’s own flagship Office suite, even today, suffers from some highly inconsistent, bizarre [pseudo-MDI behavior](https://blog.codinghorror.com/tabbed-browsing-and-mdi-sdi-wtf/) for multiple documents. I’ll take simple, reliable tabs over oddball MDI *any* day. No contest.


Lately I’m starting to come around to Cyrus’ way of thinking. I don’t hate tabbed interfaces – yet – but I definitely see what Cyrus was talking about. Tabs are increasingly the source of two aggravating mistakes for me:

1. **I inadvertently open multiple copies of a web site**, because I can’t see that I already had that web site open in an obscured tab of an existing browser window.
2. **I accidentally close a browser window containing information that I needed**, because the information was in an obscured tab of that particular browser window.


In a tabbed interface, it’s difficult to see anything except the active tab at any given time. **Tabbed interfaces obscure as much as they organize.** Tabs are great in moderation, but once they become a keystone navigational technique of your core applications, something peculiar happens. As Cyrus so aptly said, “once I start using tabs [extensively], things go all to hell.”


Allow me to illustrate with an example. Let’s say **I want to check my Gmail account**, which I do frequently throughout the day. It’s likely I already have Gmail running, somewhere, so job #1 is to find it.


First, I scan the text in the taskbars. I use [UltraMon](http://www.realtimesoft.com/ultramon/), so each of my three monitors has its own distinct taskbar, summarizing every window on that monitor.


![](https://blog.codinghorror.com/content/images/2025/05/image-521.png)


But I don’t see the word “Gmail” in any of the three taskbars.


Next, I press ALT+TAB – the poor man’s Expos – and scan through thumbnails of all the windows I have open. Do I see anything that looks like Gmail?


![](https://blog.codinghorror.com/content/images/2025/05/image-522.png)


No. I don’t see the distinctive look of the Gmail user interface in any of those thumbnails. I’ve actually [enlarged the Alt+Tab thumbnail size](https://web.archive.org/web/20070904010045/http://blogs.vertigo.com/personal/jatwood/Blog/Lists/Posts/Post.aspx?ID=31) via registry tweaks, so this is as good as it gets for visibility. Squinting doesn’t help.


The Alt+Tab dialog only uses the primary monitor, even though I have a three-monitor configuration. But we can harness the entire screen area of *all* the monitors if we install [the amazing Switcher](https://web.archive.org/web/20070914105226/http://insentient.net/). I have Switcher mapped to Windows+Tab, replacing the *incredibly* lame Flip3D. This is functionally identical to the OSX Expose that Cyrus mentioned. *Now* can I find Gmail?


![desktop-switcher-small](https://blog.codinghorror.com/content/images/uploads/2007/09/6a0120a85dcdae970b0120a86da527970b-pi.jpg)


No. Even with the additional resolution of Switcher across all three monitors, I don’t see Gmail in any of the windows. At this point I would usually launch the URL using [the keyboard entry area](https://blog.codinghorror.com/typing-trumps-pointing/) of the Vista Start Menu. I could use the fancy Start++ add-in to make this easier, but the vanilla Vista menu works well enough.


But wait! *I actually had Gmail open already.* I’ve made a mistake... again. I have *two* copies of Gmail running now. Did you see it? Here, let me show you:


![](https://blog.codinghorror.com/content/images/2025/05/image-523.png)


That muddy, tiny little morass of pixels is the *only* visual indication that I already had Gmail running as a tab in an existing browser instance. It’s not in the taskbar, it’s hardly visible at all in the small Alt+Tab screenshot, and you’d need the Six Million Dollar Man’s bionic eye to see that *barely* visible tab in Expose, I mean, Switcher.


The depressing thing is that it’s usually *faster* to mindlessly launch a new browser than it is to go through this tedious routine of playing [Where’s Waldo](http://en.wikipedia.org/wiki/Where's_Waldo) with (n) browsers and (n) tabs. And that’s what I often do. But it bothers me.


Let me be very clear – **I like tabs**. I think they’re a far better option than the terrible MDI-alike alternatives. But I also think tabbed interfaces present some pretty severe navigational problems of their own. In the above example, if Gmail had been in its own browser window, I could have found it instantly by looking in the taskbar, or at worst, by visually selecting it from even a smallish thumbnail image. Because Gmail was in a tab, I wasted my time trying to find it, and I wasted even more time needlessly launching another browser. And this isn’t an isolated incident. This happens to me *every day*. More times than I’d care to admit.


So how can we fix this? **How can we integrate tabs with the existing navigational features of the operating system, such as the taskbar, and Expose?** I keep coming back to search as the [dominant computing metaphor](https://blog.codinghorror.com/is-the-command-prompt-the-new-desktop/). The only thing I can think of is a plain-text search facility where I type “Gmail,” and the OS would automatically highlight that tab (or window) and bring it to the front. That presupposes a very high level of integration between the application tabs and the operating system, however.


Despite the undeniable convenience of tabs for grouping and organizing related topics together in a single browser instance, I feel like tabs create as many problems for me as they solve. I wish I could “tear off” tabs into standalone windows on demand, too. That might be a reasonable workaround in the meantime.


*Whatever happened to Cyrus? The last entry on his blog is two years old, and I can’t find hide nor hair of him via internet searches. It’s a shame, because I thoroughly enjoyed his blog.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[web browsers](https://blog.codinghorror.com/tag/web-browsers/)
[tabbed interfaces](https://blog.codinghorror.com/tag/tabbed-interfaces/)
[usability](https://blog.codinghorror.com/tag/usability/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
