---
title: "Will Mouse Gestures Ever Be Mainstream?"
date: 2006-02-20
url: https://blog.codinghorror.com/will-mouse-gestures-ever-be-mainstream/
slug: will-mouse-gestures-ever-be-mainstream
word_count: 680
---

[Darwinia](https://blog.codinghorror.com/darwinia/) is the third game I’ve played with [mouse gesture](http://en.wikipedia.org/wiki/Mouse_gestures) support:

1. Bungie’s classic 1998 game [Myth](http://projectmagma.net/what/index.php) used gestures in a limited way to indicate squad facing post-movement.
2. Lionhead’s 2001 game [Black and White](https://web.archive.org/web/20060324155635/http://www.lionhead.com/bw/index.html) used gestures to invoke various spells.
3. Introversion Software’s 2005 game [Darwinia](https://web.archive.org/web/20060219163804/http://www.darwinia.co.uk/) offers gestures as an alternative control scheme.


I’ve never been comfortable with mouse gestures in any of these games. It seems like a great idea in concept, but it breaks down in execution, at least for me. I distinctly remember the awkwardness of getting my squads to face the right direction in Myth. And although there was a certain element of mysticism in scrawling spells on the screen in Black and White, the game sometimes had difficulty recognizing what I had drawn. It ultimately ended up feeling like extra work when I could have simply clicked an icon or pressed a key to cast the very same spell. Perhaps problems like these are why mouse gesture control mode is not the default control mode in Darwinia.


Games tend to be experimental when it comes to UI. But mouse gestures are slowly – *very* slowly – making their way into mainstream operating systems and applications:

- There’s a [plugin](https://web.archive.org/web/20060405001445/http://optimoz.mozdev.org/gestures/defaultmappings.html) to add gesture support to Firefox
- [Strokeit](https://web.archive.org/web/20060508090428/http://www.tcbmi.com/strokeit/actions.shtml?app=./files/actions/Default.cfg) offers system-wide gesture support in Windows
- The Opera browser [natively supports gestures](http://www.opera.com/features/mouse/)
- [Sensiva](https://web.archive.org/web/20060426071646/http://www.sensiva.com/symbolcommander/index.html) provides system-wide gestures for Tablet PCs
- There’s a [plugin](https://web.archive.org/web/20060414134053/http://www.codeproject.com/atl/MouseGestures.asp) that brings gestures to Internet Explorer
- Here’s [sample code](http://www.vbaccelerator.com/home/NET/Code/Libraries/Windows_Messages/Mouse_Gestures/article.asp) that demonstrates how to add gesture support to a .NET app


Even without any of this software installed, you can use one very familiar mouse gesture: **dragging and dropping**.


I’ve experimented with several of the above utilities at various times, and I’m still ambivalent about mouse gestures for a few reasons:

- **Gestures have the **[**one-button mouse problem**](https://blog.codinghorror.com/double-click-must-die/). There are zero visual cues that any of these fancy gestures are possible. Additional buttons on a mouse, or toolbar buttons on the screen, can prompt a “I wonder what this does?” reaction from a new user. There is no such discoverability for mouse gestures.
- **Gestures are extremely mouse-centric.** Have you ever tried “writing” your name with the mouse? Very few users have that kind of fine motor control. But the mouse isn’t your only option. Left-hand keyboard accelerator keys can be just as effective – without requiring you to take your other hand off the mouse.
- **There are only so many gestures you can draw.** Once you get beyond a dozen simple strokes in the cardinal directions (up, down, diagonal, etc.), you’re in trouble. It’s a slippery slope to something overwhelming like [Graffiti](https://web.archive.org/web/20060405003223/http://palm.vanbrayne.com/graffiti.html).
- **Gestures require a dedicated accelerator key.** There’s no way to automatically detect a mouse gesture; they have to be manually initiated via a button or keypress. In most apps, you hold down the right mouse button to begin your gesture, then release it when you’re done. It’s one more accelerator to remember. And it’s now possible to accidentally trigger a gesture when all you wanted was the right-click menu.


In short, *gestures are for extremely advanced users only*, perhaps even more so than traditional keyboard shortcuts. But they do have some specific uses that are interesting:


> *“The motion of performing a gesture is more natural than sliding the mouse over to a button or menu,” he said. “And because it works anywhere in the window (not just on the button), it saves a bit of time and effort, especially as screens get bigger and you have to move farther to reach a button.”*


Rather than mousing over and clicking on the relatively small minimize, maximize, or close buttons, it’s faster to invoke a gesture right where your mouse is to perform the same action. This is particularly nice when the gesture has some conceptual mapping to the activity: drawing a diagonal slash to close, down to minimize, up to maximize/restore, etcetera.


![](https://blog.codinghorror.com/content/images/2025/05/image-208.png)


For mouse gestures to become mainstream, they need to be simple, discoverable, and most definitely system-wide.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user interface design](https://blog.codinghorror.com/tag/user-interface-design/)
