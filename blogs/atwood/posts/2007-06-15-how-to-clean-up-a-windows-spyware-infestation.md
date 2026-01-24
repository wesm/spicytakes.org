---
title: "How to Clean Up a Windows Spyware Infestation"
date: 2007-06-15
url: https://blog.codinghorror.com/how-to-clean-up-a-windows-spyware-infestation/
slug: how-to-clean-up-a-windows-spyware-infestation
word_count: 1655
---

I recently upgraded my dedicated racing simulation PC, so I was forced to re-install Windows XP SP2, along with all the games. As I was downloading the no-cd patches for the [various racing sims](https://blog.codinghorror.com/pc-racing-sims/) I own, I was suddenly and inexplicably deluged with popups, icons, and unwanted software installations. I got that sinking feeling: I had become the unfortunate victim of a **spyware infestation**.


Of course, this is *completely my own fault* for browsing the web using the 2004-era web browser included with a default install of Windows XP Service Pack 2. If I was thinking rationally, I would have downloaded [Firefox](http://www.mozilla.com/en-US/firefox/) first, or at least connected to Windows Update to get the latest patches, *before* venturing on to the open internet. But I figured I’d save myself that work, and just pop into a few specific web sites for a few quick downloads. Couldn’t hurt, right? Let my mistake be a lesson to everyone reading this: ***never* browse the web without the very latest version of your preferred web browser**. Intentionally choosing to browse the web with a three year old browser, as I did, is an incredibly dangerous thing to do.


The consequences in this case are fairly minimal since this isn’t even my secondary machine – it’s a special-purpose PC dedicated to gaming. Reinstalling the operating system is no big deal. But it’s still an inconvenient time sink, and in any case, the spyware infestation has to be dealt with because it causes serious performance problems and will even interrupt gameplay with incessant popups.


The two most common sites for no-cd patches are [MegaGames](http://www.megagames.com/) and GameCopyWorld. In case you’re wondering, yes, I do own all my games. I download no-cd patches for convenience’s sake; I consider them a privilege of ownership for knowledgeable, ethical PC gamers. I figured the infection came from one of these sites. So I set up a [honeypot virtual machine](http://en.wikipedia.org/wiki/Honeypot_%28computing%29) under Virtual PC 2007, using the ancient, original 2001 release of Windows XP and the classic [Devil’s Own key](http://www.everything2.com/index.pl?node_id=1374161), and began testing.


Here’s a shot of Task Manager at the desktop, after installing the necessary virtual machine additions. This is a completely plain vanilla, clean Windows XP installation: no service packs, no updates, no nothing. This system is connected to the internet, but it’s not as dangerous as it sounds. Because it’s behind a NAT router that blocks all incoming connections, there’s no way it can get* passively *infected. I let it connect to the internet and quiesce at the desktop for about an hour, just to prove my point. **No passive infections occurred behind a NAT router**, even for this woefully out of date September 2001 era install of Windows XP.


![](https://blog.codinghorror.com/content/images/2025/05/image-492.png)


Now we’re leaving passivity behind, and unwisely **browsing the open internet with the unpatched, six year old original version of Internet Explorer 6.0**. [Danger, Will Robinson!](http://en.wikipedia.org/wiki/Danger,_Will_Robinson) I left Task Manager running as I browsed to MegaGames, downloaded a no-cd patch, and... nothing. I then visited GameCopyWorld, downloaded a no-cd patch, and... all of a sudden, it’s crystal clear who the culprit is. Check out Task Manager now:


![spyware: taskman after](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d8ea5970b-pi.png)


This comes as a shock to me, because GameCopyWorld is recommended often in gaming forums. I consider(ed) it a reputable web site. I’ve never had a problem with the site before, because I usually surf with the latest updates. But the unpatched browser spyware infestation from visiting GCW – **just from visiting the web pages, even if you don’t download a single thing –** is nearly immediate and completely devastating. The virtual machine desktop, after a few scant minutes, tells the story:


![](https://blog.codinghorror.com/content/images/2025/05/image-493.png)


It isn’t pretty, and let me tell you, **I have a new degree of sympathy for the poor users who become the unfortunate victims of spyware infestations**. The machine becomes borderline unusable, between...

- new icons that magically appear on your desktop
- full-screen popups that occur every two minutes
- dialog boxes that offer to “install antivirus software” with only an OK button
- system performance degradation from all those spyware background processes


... it’s a wonder people don’t just give up on computing altogether. Once the door is open, it seems the entire neighborhood of malware, spyware, and adware vendors take up residence in your machine. There should be a special circle of hell reserved for companies who make money doing this to people.


At first, I was mad at myself for letting this happen. I should know better, and I *do* know better. Then I channeled that anger into action: **this is my machine, and I’ll be damned if I will stand for any slimy, unwanted malware, adware, or spyware that takes up residence on it.** I resolved to clean up my own machine and fix the mess I made. It’s easier than you might think, and I’ll show you exactly how I did it.


Our first order of business is to **stop any spyware that’s currently running**. You’ll need something a bit more heavy-duty than mere Task Manager – get Sysinternals’ [Process Explorer](https://web.archive.org/web/20070630194502/http://www.microsoft.com/technet/sysinternals/utilities/processExplorer.mspx). Download it, run it, and sort the process list by Company Name.


![](https://blog.codinghorror.com/content/images/2025/05/image-499.png)


**Kill any processes that don’t have a Company Name** (with the exception of DPCs, Interrupts, System, and System Idle Process). Right-click the processes and select Kill, or select them and press the Delete key. You can use my initial screenshot of Task Manager, at the top of this post, as a reference for what *should* be running in a clean Windows XP installation. But there’s usually no need to be that specific; unless it has a Company Name you recognize, it’s highly likely to be a rogue application and should be terminated.


Stopping the running spyware is only half the battle. Now we need to **stop the spyware from restarting the next time we boot the system**. [Msconfig](http://www.netsquirrel.com/msconfig/) is a partial solution, but again we need something more powerful than what is provided out of the box. Namely, SysInternals’ [AutoRuns utility](https://web.archive.org/web/20070622153641/http://www.microsoft.com/technet/sysinternals/utilities/Autoruns.mspx). Download it, run it, and start browsing through the list that appears:


![](https://blog.codinghorror.com/content/images/2025/05/image-498.png)


As you can see, there’s a bunch of spyware, malware, adware, and god knows what else gunking up the works – all from visiting a *single* website! **Scroll through the list, all the way to the bottom, scanning for blank Publishers, or any Publisher you don’t recognize. If you see anything that’s suspect, delete it!** In a default Windows install, 99.5% of the entries will have “Microsoft Corporation” as the Publisher. Any *reputable* vendor will have no problem attaching their name to their work, so it’s generally only the blank entries you need to worry about.


Now **reboot the system**. We’ve removed most of the spyware infestation, but there’s a certain much more virulent class of spyware that can survive this treatment. We’ll deal with them next.


After rebooting, check Process Explorer and Autoruns for anything suspicious, exactly as we did before. The first thing I noticed that “came back” in Autoruns was a suspicious driver, core.sys, that didn’t have a Publisher. I used **the powerful Find | Find Handle or DLL menu in Process Explorer** to locate any active references to this file.


![](https://blog.codinghorror.com/content/images/2025/05/image-497.png)


Unfortunately I didn’t capture the right screenshot at the time, so I’m showing a generic search result above. Anyway, there was exactly one open handle to the core.sys file. I selected the result, which highlights the corresponding handle in the lower pane of the Process Explorer view. Right-click the handle entry in the lower pane and click “Close Handle.”


![](https://blog.codinghorror.com/content/images/2025/05/image-496.png)


After I closed the handle, I could physically delete the rogue core.sys file from the filesystem, along with the Autoruns entry for it. Problem solved!


The other item that reappeared in Autoruns after the reboot was an **oddly named DLL file with hooks into Winlogon and Explorer**. In addition to the suspicious name, each entry carries the tell-tale sign of the missing Publisher value:


![](https://blog.codinghorror.com/content/images/2025/05/image-495.png)


Delete the entries in Autoruns all you want; they’ll keep coming back when you press F5 to refresh. This rogue, randomly named DLL continually monitors to make sure its ugly little hooks are in place. The nasty thing about processes attached to [Winlogon](http://en.wikipedia.org/wiki/Winlogon) is that they’re very difficult to kill or remove. We can kill Explorer, but **killing Winlogon is not an option**; it’s the root process of Windows, so shutting it down causes the OS to restart. It’s a difficult [catch-22](http://en.wikipedia.org/wiki/Catch-22_(logic)).


But we’re smarter than the malware vendors. Fire up Process Explorer and use the Find | Find Handle or DLL menu to locate all the instances of this DLL by name. (See, I told you this option was powerful.) Kill any open handles to this file that you find, exactly as we did before. But you’ll need to go one step further. We know from the Autoruns that this DLL is likely to be attached to the Explorer and Winlogon processes, but let the find results be your guide. Double-click on any processes you found that reference this DLL. **In the process properties dialog, select the Threads tab. Scroll through the threads and kill every one that has the rogue DLL loaded.**


![](https://blog.codinghorror.com/content/images/2025/05/image-494.png)


Once you’ve killed all the threads, you can finally delete the entries in Autoruns without them coming back. Reboot, and your machine is now completely free of spyware. **I count 17 entries in Task Manager, exactly the same number as when I originally started.**


Of course, the smartest thing to do is **not to get infected with spyware, malware, or adware in the first place**. I can’t emphasize this enough: *always browse with the latest patches for your preferred web browser*. But if you do happen to get infected, at least now you have the tools and knowledge to banish these evildoers from your machine forever.


Update: If you’re worried about spyware, malware, and adware, you should strongly consider [not running as an Administrator](https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/).

[security](https://blog.codinghorror.com/tag/security/)
[spyware removal](https://blog.codinghorror.com/tag/spyware-removal/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[web browsing](https://blog.codinghorror.com/tag/web-browsing/)
[malware detection](https://blog.codinghorror.com/tag/malware-detection/)
