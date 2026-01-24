---
title: "The Windows Security Epidemic: Don’t Run as an Administrator"
date: 2007-06-20
url: https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/
slug: the-windows-security-epidemic-dont-run-as-an-administrator
word_count: 1165
---

In [How to Clean Up a Windows Spyware Infestation](https://blog.codinghorror.com/how-to-clean-up-a-windows-spyware-infestation/), I documented how **spyware can do a drive-by infection of your machine through your web browser**. To be absolutely clear, I never clicked on any advertisements, or downloaded and executed any files. All I did was open a GameCopyWorld web page in an unpatched, original circa-2001 version of Internet Explorer 6.0.


Yes, I know this is a spectacularly stupid thing to do. But I’m glad I did it. I got a small taste of the experience awaiting casual users when they browse the web without the latest patches and updates. I think *every* technical computer user should have this experience, so they can see first hand, on their own machine, the profound evil that we’re up against. Sure, we can recover, but we do this stuff for a living. I’m trying to imagine what my mother or father would do if this happened to them. They’d probably have to [buy a new computer](http://www.nytimes.com/2005/07/17/technology/17spy.html?ex=1279252800&en=5b2b6783f66a7422&ei=5090).


When the only viable solution to sickness is to *kill the patient*, you have a problem of epidemic proportions.


Adam McNeil, of [Webroot Software](http://www.webroot.com/), was kind enough to lend an investigative hand and duplicate the GameCopyWorld scenario. His findings are exhaustive and eye-opening:

kg-card-begin: html

> After researching the GameCopyWorld.com website I can confirm that the site is utilizing 3rd party exploits in order to deliver malware. The exploits in question appear to be delivered through a series of advertisements within the gamecopyworld.com website.
> GameCopyWorld displays a “Find Your Love at Bride.Ru” advertisement.  That advertisement “refers” to linktarget.com in order to display an advertisement for the DVD software produced by Slysoft.com.  That advertisement “refers” to 39m.net which in turn creates an <iframe> to buyhitscheap.com.  Buyhitscheap.com in turn calls fkdomain.info who attempts to deliver a series of exploits to a users system in hopes of installing a trojan dropper.  The fkdomain.info site attempts to exploit the following: (there could be more but these were the exploits I picked out of the code) 
> [Apple QuickTime with an RTSP Buffer Overflow error](https://web.archive.org/web/20070910184543/http://www.us-cert.gov/cas/techalerts/TA07-005A.html)
> WinZip FileView ActiveX CreateNewFolderFromName Method
> [Microsoft Windows Shell Code Execution Vulnerability](http://secunia.com/advisories/22159/)
> [Byte Verify Exploit](https://web.archive.org/web/20070614013047/http://www.microsoft.com:80/technet/security/bulletin/ms03-011.mspx)
> The dropper creates files that in turn download additional files as well as create threads within the Internet Explorer browser. 
> [Webroot SpySweeper](http://www.webroot.com/consumer/products/spysweeper/) detected the following spies after allowing the installer to run over night. 
> Virtumonde
> Visfx
> ZenoSearchAssistant
> PurityScan
> Trojan Downloader Matcash
> Trojan-Downloader-Zlob
> BookedSpace
> Trojan-Downloader-WaveRevenue
> Trojan.Gen
> Trojan-Downloader-Prez
> MaxiFiles
> TargetSaver
> Trojan-Poolsv
> Trojan-Dropper-Zomavis
> Webhancer
> Web Buying
> Command
> Core Adware (CoreAdware is known to use Rootkits {core.sys} to mask its presence.)
> In addition to the above listed spies, I have also recorded a large number of unclassified (not for long) files and registry entires that were added to the box as well. 
> Seeing as how these exploit files were delivered via 3rd party advertisements I’m not sure it is entirely accurate to place all of the blame for this Drive-by with GameCopyWorld.com.  It’s possible that they allowed a third party to attempt exploits on a users machine, but then again it’s also entirely possible that one of these advertisers has slipped in these exploits without their knowledge or consent.  It’s impossible to know if this exploit was delivered intentionally or accidentally.

kg-card-end: html

I’ve never used any Webroot products, but when an employee takes his own personal time to investigate a public scenario so thoroughly, that speaks very highly of the company. They’re clearly one of the good guys. But the fact that I *have* to maintain a mental “safe list” of software companies – these are OK, these are questionable – is itself disturbing and unhealthy. It’s symptomatic of just how sick the Windows software ecosystem has become. **It’s nearly impossible to tell the good guys from the bad guys**. Do a web search for “spyware” and you’ll get dozens of results, some of which are for companies that installed the spyware in the first place. Can you tell them apart? Could your parents?


Tracing this massive security epidemic all the way back to [patient zero](http://en.wikipedia.org/wiki/Patient_Zero) doesn’t take much detective work. It originates with Windows NT 3.0, when **Microsoft chose to set up default users as Administrators**.


This infection was **only possible because I was logged in as an administrator**. Choosing *not* to run as an Administrator is easily the single most important security tip for a Windows machine, whether you’re running XP or Vista. Worried about your parents getting infected? Need to create an account for a teenager? **Set them up as regular users**. It’s not a panacea, but it goes an awful long way towards solving the problem. As a test, I logged in as a normal user, and I was unable to duplicate the GameCopyWorld infection in any way – even with a completely unpatched, circa 2001 version of Windows XP. Running as a normal user *really works*.


[Aaron Margosis’ blog](http://blogs.msdn.com/aaron_margosis/archive/2004/06/17/157962.aspx) is the best source of information on running as a non-administrator. His list of reasons why you [shouldn’t run as an Administrator](https://web.archive.org/web/20071006030128/http://blogs.msdn.com/aaron_margosis/archive/2004/06/17/157962.aspx) is hair-raising stuff:

kg-card-begin: html

> If you’re running as admin, an exploit can:
> install kernel-mode rootkits and/or keyloggers (which can be close to impossible to detect)
> install and start services
> install ActiveX controls, including IE and shell add-ins (common with spyware and adware)
> access data belonging to other users
> cause code to run whenever anybody else logs on (including capturing passwords entered into the Ctrl-Alt-Del logon dialog)
> replace OS and other program files with trojan horses
> access LSA Secrets, including other sensitive account information, possibly including account info for domain accounts
> disable/uninstall anti-virus
> cover its tracks in the event log
> render your machine unbootable
> if your account is an administrator on other computers on the network, the malware gains admin control over those computers as well
> ... and lots more

kg-card-end: html

I’ll admit I am not the best role model on this count. Personally, I lost my enthusiasm for limited user accounts when **Microsoft didn’t have the guts to make standard users the default – as they absolutely should have – in Windows Vista**. I [swore they would](https://blog.codinghorror.com/the-dancing-bunnies-problem/). Instead, we got got hybrid administrator weirdness and “Cancel or Allow” oddities.


I guess that’s yet another thing we can sacrifice at the [dark altar of backwards compatibility](http://www.joelonsoftware.com/articles/APIWar.html).


I understand the pressure to be backwards compatible. There’s no end of Vista blowback based on minor driver compatibility issues. The *“if it doesn’t work, it’s automatically Microsoft’s fault, even if the software or hardware vendor is clearly to blame”* mentality is sadly all too common. But given the **massive ongoing Windows security epidemic**, was defaulting regular users to Administrator accounts – exactly like Windows XP, Windows 2000, and Windows NT before it – *really* the right decision to make?


I’m not so sure.

[security](https://blog.codinghorror.com/tag/security/)
[windows](https://blog.codinghorror.com/tag/windows/)
[administrator](https://blog.codinghorror.com/tag/administrator/)
[spyware](https://blog.codinghorror.com/tag/spyware/)
[web browsing](https://blog.codinghorror.com/tag/web-browsing/)
