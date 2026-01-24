---
title: "Please Don’t Steal My Focus"
date: 2007-12-04
url: https://blog.codinghorror.com/please-dont-steal-my-focus/
slug: please-dont-steal-my-focus
word_count: 816
---

Has this ever happened to you? You’re merrily typing away in some application, minding your own business, when – suddenly – **a dialog pops up and steals the focus from you**.


![](https://blog.codinghorror.com/content/images/2025/03/image-167.png)


At best, your flow is interrupted. You’ll have to switch back to the window that you were using, figure out where you were, and resume your work.


But it can be worse. So, so much worse. If you happen to be typing something that can be interpreted as an action by that dialog – and remember, pressing the space bar is the same as clicking a button when it happens to have the focus – you could suddenly and very much accidentally be in a world of pain. Like this poor, unfortunate soul, who recently posted a plaintive comment to my [XP Automatic Update Nagging post](https://blog.codinghorror.com/xp-automatic-update-nagging/).


> Great news! Microsoft developed a solution to this problem! Microsoft’s most talented programmer figured out how to make “Reboot later” mean “Reboot when user says reboot.” It only took some tweaking to 1 line of code, 180 days for approvals from 80 managers, 80 resource files for different languages, and 18 days for testing in one of the languages. It worked.
> The programmer opened a SourceSafe^H^H^H^H^H^H^H^H^H^H^H Team Foundation window in order to check in the fix. An expert programmer, she was used to using the keyboard. She didn’t click her mouse on the “OK” button, she just hit the Enter key.
> **The “Reboot now” / “Reboot later” prompt flashed so briefly, she didn’t even notice it. She thought she hadn’t pounded the Enter key hard enough.** Looking at Team Foundation’s “OK” button still waiting there for her to hit the Enter key to check in her work, she hit the Enter key again.
> The check in started. The check in got killed while her workstation rebooted. There we remain today, with the check in half-in and half-out, unusable, with no good copy of the code. So that’s why the fix was never released.


It’s a perfect example of how **stealing the user’s focus can lead to catastrophic results** if the user is particularly unlucky. Unfortunately, this burden falls heaviest on us keyboarders.


Another classic example is the IE download notification window, which loves to pop up, steal the focus, and tell you the great news: your download is complete! Oh, and your newly downloaded file is copying to its destination! Hooray! Unfortunately, this very same download notification dialog *also* contains a “Cancel” button. Guess which button just so happens to have the focus when this pops up? Why you’d want to cancel a download after it is complete is a mystery to me, but I’ve inadvertently pressed the space bar on this dialog more than once.


**Stealing focus from the user is never acceptable**. I can’t imagine any circumstance where this would be desirable or even defensible behavior. Modal dialogs [are bad enough](https://blog.codinghorror.com/death-to-the-dialog-box/), but this is even worse – it’s almost a system modal dialog, so self-important that all work must cease as the user is forced to pay attention to whatever earth-shattering message it urgently has to deliver. It's an extreme form of [stopping the proceedings with idiocy](https://blog.codinghorror.com/unnecessary-dialogs-stopping-the-proceedings-with-idiocy/). I’m not the first person to complain about this, of course. Fellow members of the “Don’t Steal My Focus” club [wrote about this back in 2002](https://web.archive.org/web/20080108055639/http://radio.weblogs.com/0103807/stories/2002/06/07/dontStealMyFocus.html), [again in 2005](https://web.archive.org/web/20071213005200/http://useful-sounds.de/pivot/entry.php?id=102), and [a few months ago](https://web.archive.org/web/20071210191637/http://www.rafb.net/cohen/blog/2007/08/30/stealing-focus/). It’s not exactly an unknown or new problem. So why do we have to keep talking about it and dealing with it? What gives?


The strange thing is, there are provisions built into the operating system to protect us from badly written, focus stealing applications. The ForegroundLockTimeout registry setting is *expressly designed* to prevent applications from stealing focus from the user. The OS silently converts that inappropriate focus stealing behavior into friendlier, less invasive taskbar button flashing, which is the subject of the ForegroundFlashCount registry setting.


I’ve seen this work. Most of the time, it *does* work. This setting is enabled by default in Windows XP and Vista. And yet, applications are occasionally able to steal the focus from me and screw up my flow. I’d say it happens a few times a week on average. It’s perplexing. I’m wondering if it’s because badly behaved programmers abuse the “Always on Top” window flag in a misguided attempt to [get the user’s attention](https://web.archive.org/web/20071213051525/http://blogs.msdn.com/oldnewthing/archive/2006/12/19/1325024.aspx). I suppose as long as there are bad programmers, there will be some unorthodox way they can devise to steal the focus from the user. At some level, sufficiently advanced incompetence is indistinguishable from malice. Maybe we’d have better luck educating programmers on the evils of focus stealing and, more generally, the futility of [unnecessary notifications](https://web.archive.org/web/20080108015705/http://jcooney.net/archive/2007/09/12/54550.aspx) the user isn’t going to read anyway.


But in the meantime, **please don’t steal my focus**. I’m using it right now. Really. I am.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
[focus stealing](https://blog.codinghorror.com/tag/focus-stealing/)
