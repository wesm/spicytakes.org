---
title: "Remote Desktop Tips and Tricks"
date: 2006-04-18
url: https://blog.codinghorror.com/remote-desktop-tips-and-tricks/
slug: remote-desktop-tips-and-tricks
word_count: 655
---

I’m with K. Scott Allen: the pervasiveness of Remote Desktop functionality in Windows has fundamentally changed the way I work.


The fact that it shipped in the Windows XP box – and as a default component of all the server operating systems since Windows 2000 – has done wonders for its adoption. It’s truly ubiquitous. And it doesn’t hurt that it’s actually the best performing remote control tool I’ve ever used; I have yet to try [any other remote control tool](https://blog.codinghorror.com/vnc-vs-remote-desktop/) that performs as well. It’s so responsive that it almost makes the idea of physically sitting in front of a computer seem quaint.


Almost.


One thing you quickly learn with Remote Desktop is that **not all the windows shortcut keys work as you would expect them to**. The “Apply Windows key combinations” setting defaults to “full screen only,” so you may see different behavior depending on whether or not you’re running full-screen; use the Ctrl+Alt+Pause shortcut to switch back and forth.


The help file contains a list of the **special Remote Desktop key combinations**:


![](https://blog.codinghorror.com/content/images/2025/05/image-267.png)


Switches between programs from left to right.


![](https://blog.codinghorror.com/content/images/2025/05/image-268.png)


Switches between programs from right to left.


![](https://blog.codinghorror.com/content/images/2025/03/image-77.png)


Cycles through the programs in the order they were started.


![](https://blog.codinghorror.com/content/images/2025/03/image-78.png)


Displays the Start menu.


![](https://blog.codinghorror.com/content/images/2025/03/image-81.png)


Switches the client between a window and full screen.


![](https://blog.codinghorror.com/content/images/2025/03/image-80.png)


Brings up the Windows Security dialog box.


![](https://blog.codinghorror.com/content/images/2025/03/image-82.png)


Toggles between full screen and windowed mode
(note that this does not set the client desktop to the correct size)


![](https://blog.codinghorror.com/content/images/2025/03/image-83.png)


Displays the Windows menu


![](https://blog.codinghorror.com/content/images/2025/03/image-84.png)


Places a snapshot of the client’s active window on the clipboard


![](https://blog.codinghorror.com/content/images/2025/03/image-85.png)


Places a snapshot of the client’s entire desktop area on the clipboard


To **shut down or restart the remote computer**, either bring up the Windows Security dialog, or use Task Manager.


Scott also provides a great list of additional resources for hacking Remote Desktop:

- [Shadowing the current login session with Windows Server 2003](https://web.archive.org/web/20060426045939/http://support.microsoft.com/default.aspx?scid=kb;en-us;278845)
- [Shadowing the current login session with Windows XP](https://web.archive.org/web/20060426050847/http://support.microsoft.com/default.aspx?scid=kb;en-us;279656&sd=tech) (aka Remote Assistance)
- [A description of the .RDP file format](https://web.archive.org/web/20060424125116/http://dev.remotenetworktechnology.com/ts/rdpfile.htm)
- [Managing Desktop Sessions Remotely](https://web.archive.org/web/20060424173631/http://weblogs.asp.net/owscott/archive/2003/12/30/46776.aspx) (or use [the GUI tool](https://blog.codinghorror.com/remotely-managing-remote-desktop/))
- [Connect to Remote Desktop via Linux](http://www.rdesktop.org/)
- [Change the default Remote Desktop listening port](https://web.archive.org/web/20060426050334/http://support.microsoft.com/?kbid=306759)


I have two tips of my own. The first has to do with multiple monitors. Both my work and home computers have [three monitors](https://blog.codinghorror.com/multiple-lcds/). Before you laugh, guess who else was on the three monitor tip back in the day? Google’s Larry Page. And Bill Gates. At any rate, I’ve gotten at least one email on this, so I know it’s not easy to figure out. **Here’s how you run a remote desktop session maximized to a particular monitor**:

1. Start a windowed (non-full screen) remote desktop session
2. Drag the windowed session to the monitor you want
3. Close the remote desktop session
4. Set the properties for the connection to “full screen.” It must be “full screen,” *not* the actual resolution of your monitor (1280x1024, etc.)
5. Start a remote desktop connection; it’ll be full screen on the target monitor


I know it’s convoluted. But at least it remembers which monitor it is full screen to. It’d be simpler if we had a way to change the client desktop size without closing and re-opening the connection, say via the display properties dialog. But we don’t.


Here’s my second tip: **if you’re not on a fast LAN, drop the color depth down to either 256 or 15-bit color**, and **select “Modem” on the Experience tab**. Color depth is the single biggest contributor to performance over a slow connection. You may be tempted to go to 16-bit color or even 24-bit color to make things look prettier, but remember all those additional bits have to be transmitted across the wire. I know 256 colors can look desperately bad with most of todays websites and applications – but 15-bit color is a good compromise.

[remote desktop](https://blog.codinghorror.com/tag/remote-desktop/)
[windows](https://blog.codinghorror.com/tag/windows/)
[remote control](https://blog.codinghorror.com/tag/remote-control/)
[shortcut keys](https://blog.codinghorror.com/tag/shortcut-keys/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
