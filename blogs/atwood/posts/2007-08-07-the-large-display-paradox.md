---
title: "The Large Display Paradox"
date: 2007-08-07
url: https://blog.codinghorror.com/the-large-display-paradox/
slug: the-large-display-paradox
word_count: 877
---

As displays increase in size and prices drop, **more and more users will end up with relatively large displays by default**. Nobody buys 15 or 17 inch displays any more; soon, it won’t make financial sense to buy a display smaller than 20 inches. Eventually, if this trend continues, everyone will have 30-inch displays on their desktops. This is clearly a good thing. You can never have enough display space. But there is one unintended consequence of large displays.


One of the *advantages* of small monitors, ironically, is that **because they’re small, they nudge users into a simpler, windowless method of working**. Instead of wasting time sizing, moving, and z-ordering windows, users only need to deal with one maximized window at a time. They can flip between maximized applications in much the same way they change channels on the television. But once your display gets to 1600 x 1200 or beyond, this easy one-app-per-display model isn’t feasible any more. Dan recently ran into this problem when he [upgraded to a 30" LCD](http://www.dansdata.com/3007wfp-hc.htm):


> Users of 30-inch monitors face the terrible, *terrible* problem of how to effectively use all of that space. You don’t often want to maximize a folder or document window on a screen this big; either you’ll end up with a lot of [white space and important program buttons](https://blog.codinghorror.com/the-non-maximizing-maximize-button/) separated by a vast expanse of nothing, or you’ll get lines of text 300 or more characters long, which are [difficult to read](https://blog.codinghorror.com/text-columns-how-long-is-too-long/).


That’s the **large display paradox**. Having all that space can make you *less *productive due to all the window manipulation excise you have to deal with to make effective use of it.


Personally, I’m a card-carrying member of [the prestigious three monitor club](https://blog.codinghorror.com/joining-the-prestigious-three-monitor-club/), which means I’m one step ahead of Dan. At least until he doubles or triples down:


![Al Gore using three 30 inch monitors](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d9539970b-pi.jpg)


Although my displays are only 20 inches in size, [I have three of them](https://blog.codinghorror.com/multiple-lcds/). Maximizing a window to a 20 inch, 1600 x 1200 display area is a reasonable thing to do most of the time. I also use [UltraMon](http://www.realtimesoft.com/ultramon/), which gives me **the indispensable ability to drag maximized windows between monitors**. I’m constantly grabbing maximized windows and “throwing” them from monitor to monitor, ala [Minority Report](http://www.imdb.com/title/tt0181689/).


![Minority Report user interface](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d955c970b-pi.jpg)


With my triple monitor setup, I have a very large display surface with a primary area of focus and secondary areas that I can “snap” items to when I want them available for reference, but out of the way. **I have a natural snapping grid because I use three physical monitors.** It’s a side-effect of the hardware, but a crucial one that I’ve absolutely come to rely on.


Dan only has a single large 30 inch monitor, so he has no natural grid to snap windows to. He needs a software solution:


> I’ve been using [WinSplit Revolution](https://maxto.net/compare/winsplit_revolution/) to manage this problem. It’s a neat little Windows utility that makes it easy to bounce (most) windows around the screen and quickly resize them to take up the amounts of screen you probably want them to occupy. Two panes, each 1280 by 1600, give you a couple of twenty inch portrait-aspect-ratio “screens” that work great for many tasks.


I run into this problem a little bit on my three 20 inch displays, but it’s only a minor nuisance. I’m in *serious* trouble if I ever get a multiple monitor setup with displays larger than 20 inches. (I’d also need a much, much [larger desk](https://blog.codinghorror.com/the-ideal-computer-desk/).) There’s no question that **maximized windows aren’t effective on large displays**. For larger displays, I’d need to extend the “snap grid” effect of my three monitors to each individual monitor.


That’s exactly what the WinSplit Revolution app does. It’s quite intuitive; you use CTRL+ALT+(numpad) to push the currently selected window towards the quadrant of the screen represented by the number. Pressing the key sequence multiple times iterates through the two or three possible sizes at that particular position. This diagram explains it better than I can in text:


![window grids possible using WinSplit Revolution](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d956e970b-pi.png)


As you can see, you end up with a few dozen possible grid arrangements just using the simple numpad direction metaphor. But it’s still quite a bit of work; I have to select each window and then use the numeric keypad (or the popup window equivalent) to push it over where [I want it to go](http://reptils.free.fr/help.htm). As of version 1.8, WinSplit Revolution is perfectly multiple monitor aware, and even offers a convenient key combo to move windows from monitor to monitor, too.


Fortunately, there’s [GridMove](https://web.archive.org/web/20070811102039/http://www.donationcoders.com/jgpaiva/gridmove.html), which supports multiple monitors. Just use the middle mouse button to drag a window, and you invoke the current grid template, which provides automatic snappable drop targets for that window.


![GridMove animation](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d9595970b-pi.gif)


In the not-too-distant future, **every user will have a monitor so large that maximizing a window no longer makes sense for most applications**. It’s too bad some kind of automatic snap grid support can’t be embedded into the operating system to help users deal with large display areas. Like Dan, we’re all going to need it sooner or later. Until then, these applications – or ones like them – can fill the gap.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[display technology](https://blog.codinghorror.com/tag/display-technology/)
[screen size](https://blog.codinghorror.com/tag/screen-size/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
[multitasking](https://blog.codinghorror.com/tag/multitasking/)
