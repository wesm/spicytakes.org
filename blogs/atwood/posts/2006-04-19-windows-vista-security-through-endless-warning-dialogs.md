---
title: "Windows Vista: Security Through Endless Warning Dialogs"
date: 2006-04-19
url: https://blog.codinghorror.com/windows-vista-security-through-endless-warning-dialogs/
slug: windows-vista-security-through-endless-warning-dialogs
word_count: 788
---

Paul Thurrott’s scathing article [Where Vista Fails](https://web.archive.org/web/20060422010620/http://www.winsupersite.com/reviews/winvista_5308_05.asp) highlights my biggest concern with Windows Vista:


> Modern operating systems like Linux and Mac OS X operate under a security model where even administrative users don’t get full access to certain features unless they provide an in-place logon before performing any task that might harm the system. This type of security model protects users from themselves, and it is something that Microsoft should have added to Windows years and years ago.
> Here’s the good news. In Windows Vista, Microsoft is indeed moving to this kind of security model. The feature is called User Account Protection (UAP) and, as you might expect, it prevents even administrative users from performing potentially dangerous tasks without first providing security credentials, thus ensuring that the user understands what they’re doing before making a critical mistake. It sounds like a good system. But this is Microsoft, we’re talking about here. They completely botched UAP.
> **The bad news, then, is that UAP is a sad, sad joke. It’s the most annoying feature that Microsoft has ever added to any software product**, and yes, that includes that ridiculous Clippy character from older Office versions. The problem with UAP is that it throws up an unbelievable number of warning dialogs for even the simplest of tasks. That these dialogs pop up repeatedly for the same action would be comical if it weren’t so amazingly frustrating. It would be hilarious if it weren’t going to affect hundreds of millions of people in a few short months. It is, in fact, almost criminal in its insidiousness.


![](https://blog.codinghorror.com/content/images/2025/05/image-269.png)


We have fairly recent internal builds of Vista for a project we’re working on at Vertigo, and we’ve run into this problem too. Even though you’re ostensibly logged in as an “Administrator,” you’re inundated with a sea of security dialogs if you try to do anything even remotely, well, Administrator-y.


The problem with the **Security Through Endless Warning Dialogs** school of thought is that *it doesn’t work*. All those earnest warning dialogs eventually blend together into a giant “click here to get work done” button that nobody bothers to read any more. The operating system cries wolf so much that when a real wolf – in the form of a virus or malware – rolls around, you’ll mindlessly allow it access to whatever it wants, just out of habit. As Rick Strahl notes, this is the ultimate form of [nagware](https://web.archive.org/web/20070928021122/http://west-wind.com/weblog/posts/4678.aspx):


> Then there are the security dialogs. Ah yes, now we’re making progress: Ask users on EVERY program you launch that isn’t signed whether they want to elevate permissions. Uh huh, this is going to work REAL WELL. We know how well that worked with unsigned ActiveX controls in Internet Explorer – so well that even Microsoft isn’t signing most of its own ActiveX controls. Give too many warnings that are not quite reasonable and people will never read the dialogs and just click them anyway... I know I started doing that in the short use I’ve had on Vista.


But there’s an even deeper problem lurking under the surface. **Why doesn’t Vista respect my choice to be an Administrator?** Who is really in control here: me, or my operating system? There’s something awfully paternalistic about an operating system that lets me log in as an Administrator, but treats me like a regular User. If you’re going to treat me like a User, at least have the decency to create a regular User account for me. That would certainly make more sense.


Rick Strahl confirmed that, indeed, Vista downgrades Administrators to regular Users by default, in a misguided attempt to enhance security. He also posted a workaround that applied only to the Vista Beta. But the good news is that in the final, released version of Vista, it’s quite easy to disable UAC:

1. Launch Control Panel
2. Type “UAC” in the search box at the upper-right hand corner of the window
3. The option to disable UAC is the first search result.


Then log off and log back on.


I seriously hope Microsoft reconsiders these bizarre policies before Vista is released, but sadly they did not.

1. Let administrators really be Administrators!
2. Create all new users by default as plain Users. If a user opts to upgrade to an Administrator, that’s the appropriate time to pop the scary warning dialog.
3. If a user tries to do something that requires Administrator rights, show a dialog telling them so, and offering links to a) log in temporarily as an Admin, or b) enter the Admin credentials in-place for a quick one time operation.


It could be so much simpler if Microsoft just followed the established conventions.

[security](https://blog.codinghorror.com/tag/security/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
