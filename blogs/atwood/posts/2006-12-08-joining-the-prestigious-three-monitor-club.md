---
title: "Joining The Prestigious Three Monitor Club"
date: 2006-12-08
url: https://blog.codinghorror.com/joining-the-prestigious-three-monitor-club/
slug: joining-the-prestigious-three-monitor-club
word_count: 802
---

I have something in common with Bill Gates and Larry Page:


> [Larry Page](http://www.sfgate.com/cgi-bin/article.cgi?file=/chronicle/archive/2000/12/31/BU178263.DTL): I have a weird setup in my office. I have one computer with three monitors: one flat-screen monitor and two regular ones. I have my browser on one screen, my schedule on another and my e-mail on another. I can drag things to different screens. I also have a projector. So if I’m talking with everyone in my office, I can move stuff onto a big screen.
> [Bill Gates](http://money.cnn.com/2006/03/30/news/newsmakers/gates_howiwork_fortune/): If you look at this office, there isn’t much paper in it. On my desk I have three screens, synchronized to form a single desktop. I can drag items from one screen to the next. Once you have that large display area, you’ll never go back, because it has a direct impact on productivity.


We’re all members of the **three monitor club**.


If you’re only using one monitor, you are cheating yourself out of [potential productivity](https://blog.codinghorror.com/multiple-monitors-and-productivity/). Two monitors is a no-brainer. It’s so fundamental that I included it as a part of the [Programmer’s Bill of Rights](https://blog.codinghorror.com/the-programmers-bill-of-rights/).


But you can do better.


As good as two monitors is, **three monitors is **[**even better**](https://blog.codinghorror.com/multiple-lcds/). With three monitors, there’s a “center” to focus on. And 50% more display area. While there’s certainly a point of [diminishing returns for additional monitors](https://web.archive.org/web/20070118084944/http://blogs.vertigosoftware.com/jatwood/archive/2005/08/28/Multiple_Monitor_Madness.aspx), I think three is the sweet spot. Even Edward Tufte, in [the class I recently attended](https://blog.codinghorror.com/reading-with-edward-tufte/), explicitly mentioned multiple monitors. I don’t care how large a single display can be; you can *never* have enough desktop space.


Normally, to achieve three monitors, you have to either:

1. Buy an exotic video card that has more than 2 monitor connections.
2. Install a second video card.


The first option is difficult because video cards with 3+ monitor connections are quite rare and usually expensive to boot. The second option, adding an additional video card, is easier, but not without some compatibility pitfalls of its own. But there’s a third way that may be easiest of all. The Matrox [TripleHead2Go](https://web.archive.org/web/20061231175206/http://www.matrox.com/graphics/en/gxm/products/th2go/home.php) is a neat little external device that provides three display support from a single video output. And it’s now available in analog VGA and digital DVI editions.


![](https://blog.codinghorror.com/content/images/2025/05/image-436.png)


There is one big caveat, however. In a modern three monitor config, the operating system sees each monitor as an independently controllable desktop. You can set resolution, size, and position of the monitors independently, and windows can intelligently size themselves to each desktop on each monitor.


With the matrox Triplehead2Go, **you’re stuck with one mongo giant desktop that spans all your monitors**.


This is a very old-school way of implementing multiple monitors. Before Windows was properly aware of multiple displays (think NT 4.0 era), the “giant desktop” was the only way you could get more than one display to work at all. And “giant desktop” has a *lot* of downsides:

1. Maximizing a window becomes an exercise in futility.
2. You may not want your start menu on the leftmost monitor.
3. With two monitors, “centered” dialogs split the middle.


To avoid the many problems of “giant desktop” fakery, you really need the OS to know that you’re using two or three physical monitors, along with their resolutions, positions, and so forth.


But the Triplehead2Go has its charms. You don’t have to open your computer to install it, for one thing. And it works with computers that *can’t* be opened, such as laptops. The Triplehead2Go abstracts away the multiple monitors at a hardware level and presents itself to the operating system as a giant ultra widescreen monitor.


The Triplehead2Go also has one unexpected strength: **video games**. 3D acceleration across multiple video cards is tricky at best. And there’s no good way to tell a game to use multiple monitors unless it’s explicitly coded to do so. The Triplehead2Go device neatly sidesteps both of these limitations by externally simulating one ultra-ultra-wide monitor.


PCFormat UK experimented with the Triplehead2Go in a couple recent and upcoming game titles, such as [Armed Assault](https://web.archive.org/web/20070118051523/http://blog.pcformat.co.uk/page/pcformat?entry=armed_assault_holy_trinity):


![](https://blog.codinghorror.com/content/images/2025/05/image-435.png)


Armed Assault also takes advantage of an optional [TrackIR head-tracking device](http://www.naturalpoint.com/trackir/). The combination of a three-monitor setup with head tracking is incredibly immersive, and has to be seen to be believed. [Watch the video](https://web.archive.org/web/20071023221554/http://blog.pcformat.co.uk/resources/pcformat/trinity.wmv) and be amazed.


Three-monitor setups are particularly strong in “simulator” type games where peripheral vision is crucial to gameplay. PC Format UK tried it with the recently released [GTR2 racing game](https://web.archive.org/web/20061214031718/http://blog.pcformat.co.uk/page/pcformat/20060503), and the results are impressive.


![](https://blog.codinghorror.com/content/images/2025/05/image-434.png)


There are lots more screenshots of various games running in triple-head mode at [Tom’s Hardware](https://web.archive.org/web/20061216172244/http://www.tomshardware.com/2006/05/04/can_matroxs_triplehead2go_span_fun_across_three_displays/page8.html) and [Neoseeker](http://www.neoseeker.com/Articles/Hardware/Reviews/triplehead2go/5.html).


**The traditional “add another video card” method is still the preferred way to gain entry into the prestigious three monitor club.** But for laptop users and gamers, the Matrox Triplehead2Go is also a nice option with [a few caveats](https://web.archive.org/web/20061218072843/http://www.matrox.com/graphics/en/gxm/products/th2go/faq.php).

[multi-monitor setup](https://blog.codinghorror.com/tag/multi-monitor-setup/)
[productivity](https://blog.codinghorror.com/tag/productivity/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
