---
title: "More on the Snow Leopard/Old Version of Flash Brouhaha"
date: 2009-09-05
url: https://daringfireball.net/2009/09/more_snow_leopard_flash
slug: more_snow_leopard_flash
word_count: 1559
---


(**9:30pm ET:** See updates one and two, inline below.)


[Jeffrey Czerniak answers](http://geekable.com/blog/2009/09/04/dont_call_it_a_comeback.html) my “What should Apple have done differently?” question:


> John Gruber’s latest piece of Apple apologetics concerns the fact
> that Apple shipped a known-vulnerable version of Adobe Flash Player
> on the Snow Leopard DVD. He has the gall to ask those of us who
> consider this a bad thing,
> But what exactly should Apple have done differently?
> Gruber apparently considers the possibility of postponing the
> release of Snow Leopard in order to coordinate with Adobe to be
> unreasonable. If postponing Snow Leopard is out-of-bounds, then I
> have another suggestion:
> *Apple could have posted a security advisory.*


Is it possible in the run-up to going GM that a serious issue could be discovered that would warrant postponing the release of a major OS update? Sure. That’s exactly why GM releases aren’t rushed. Is this Flash situation such an issue? I believe not — and have seen no evidence that it is.


As for Apple issuing a security advisory, sure. That would be nice. But that’s not how Apple rolls. Apple’s policy regarding security issues is not to publicize them until after they’ve been addressed by software updates. It’s not unreasonable at all to disagree with this policy, but I think Apple is pretty happy with how it’s worked out for them so far, so don’t hold your breath waiting for it to change.


## Why Doesn’t the Snow Leopard Installer Do the Right Thing if You’ve Already Installed the Latest Version of Flash?


Mike Ash — on Twitter [here](http://twitter.com/mikeash/status/3773694196), [here](http://twitter.com/mikeash/status/3773919411), [here](http://twitter.com/mikeash/status/3773924484), and etc. — argues that the problem is specifically the issue of the installer downgrading the version of Flash for users who manually upgraded to the latest version of Flash while they were on 10.5. (Forgive him for his brevity, given the constraints of Twitter.)


I have no sympathy for the argument that Apple should have included an eight-day-old version of Flash in the Snow Leopard installer, or that they should have delayed the release of Snow Leopard to include it. I do have sympathy for the argument, like Ash’s, that the installer [ought not *replace*](http://twitter.com/mikeash/status/3779879894) a newer version with an older one.


And there’s a good — but, alas, in my research, unanswered — technical question as to why this did not in fact work as Ash and others expected. The Mac OS X Installer system relies on “bill of materials” *bom* files. From the [bom man page](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man5/bom.5.html):


> The Mac OS X Installer uses a file system “bill of materials” to
> determine which files to install, remove, or upgrade. A bill of
> materials, bom, contains all the files within a directory, along
> with some information about each file. File information includes:
> the file’s UNIX permissions, its owner and group, its size, its time
> of last modification, and so on.  Also included are a checksum of
> each file and information about hard links.
> The bill of materials for installed packages are found within the
> package receipts located in /Library/Receipts.


In theory, the Snow Leopard installer could look at the bom for Flash and, if the installed version is greater than the version in the installer, leave it. I do not know why it doesn’t work this way. Perhaps the bom file left by Adobe’s Flash installer is malformed. Perhaps (and this is my guess) the installer for major OS versions does not check for such things for components in the “Essentials” and “BaseSystem” installer packages. (Flash, and all other default items in the */Library/Internet Plug-Ins/* folder, are part of the Essentials package.)


Yesterday, as a hypothetical example, [I wrote](http://daringfireball.net/2009/09/flash_snow_leopard):


> That’s just how the installer works. The same is true for any
> component you manually upgrade. Like, say, if you overwrote the
> system version of Python with version 2.6.2 — when you upgrade to
> Snow Leopard, the installer will give you the system standard
> version (2.6.1).


Ends up I chose a bad example, because this is not true. DF reader Jonathan Lundell emailed me to report that he had in fact upgraded his system version of Python to version 2.6.2 while on Mac OS X 10.5.8, and, after upgrading to Snow Leopard, he still had version 2.6.2 installed, not the Snow Leopard default version 2.6.1.


**Update 1:** Correction, ends up I was right in the first place. Lundell’s personally updated version of Python 2.6.2 was, and remains, in */usr/local/bin/*. The system version of Python (version 2.6.1) is right where it should be in */usr/bin/*. The confusion arose because he checked the version by typing just “`python -V`”, rather than specifying the full path to `/usr/bin/python` at the command prompt.


(As for why the Mac OS X Installer might be designed to overwrite components like Flash in this regard, consider the following hypothetical. What if the very latest version of Flash worked just fine on Leopard but did not work on Snow Leopard? That is apparently not the case, but, what if it were? (And don’t tell me it’s not possible.) In that case, if the OS installer worked as Ash and others desire, after upgrading to Snow Leopard you’d have a system where Flash did not work at all. Some people may reasonably argue that they’d prefer a broken version of Flash than a potentially vulnerable version, but the point of the components in the Essentials package is that Apple deems them, well, *essential*. The installer logic for these “essential” components may reasonably be that it’s going to install its own known versions no matter what’s already on the disk being upgraded. Why Flash is deemed essential is a good question, though.)


## Which Vulnerabilities Apply to Flash Version 10.0.23.1?


Lastly, I’ve been attempting to research exactly what the vulnerabilities are in Snow Leopard 10.6.0’s version of Flash, but have come up empty. There are three versions of Flash to keep in mind:

- 10.0.32.18 — The current version of Flash 10 from Adobe.
- 10.0.23.1 — The version that ships with Snow Leopard 10.6.0.
- 10.0.22.87 — The version of Flash Adobe identifies as having “critical vulnerabilities”.1


[Adobe’s security bulletins and advisories page](http://www.adobe.com/support/security/#flashplayer) lists just four advisories for Flash Player 10. One dates back to February and is no longer relevant; the other three were from late July. One of the advisories from July [is specific to Windows Internet Explorer](http://www.adobe.com/support/security/advisories/apsa09-04.html). The other two apply to Windows, Mac OS X, and Linux.


[Advisory APSA09-03](http://www.adobe.com/support/security/advisories/apsa09-03.html), dated 22 July 2009, states:


> A critical vulnerability exists in the current versions of Flash
> Player (v9.0.159.0 and v10.0.22.87) for Windows, Macintosh, Linux
> and Solaris operating systems, and the authplay.dll component that
> ships with Adobe Reader and Acrobat v9.x for Windows, Macintosh and
> UNIX operating systems. This vulnerability (CVE-2009-1862) could
> cause a crash and potentially allow an attacker to take control of
> the affected system. There are reports that this vulnerability is
> being actively exploited in the wild via limited, targeted attacks
> against Adobe Reader v9 on Windows. […]


[Advisory APSB09-10](http://www.adobe.com/support/security/bulletins/apsb09-10.html), dated 30 July 2009, states:


> Critical vulnerabilities have been identified in the current
> versions of Adobe Flash Player (v9.0.159.0 and v10.0.22.87) for
> Windows, Macintosh, Linux and Solaris operating systems, and the
> authplay.dll component that ships with Adobe Reader and Acrobat v9.x
> for Windows, Macintosh and UNIX operating systems. These
> vulnerabilities could cause the application to crash and could
> potentially allow an attacker to take control of the affected
> system.
> Adobe recommends users of Adobe Flash Player 9.x and 10.x and
> earlier versions update to Adobe Flash Player 9.0.246.0 and
> 10.0.32.18.


In both advisories, the “affected software versions” are listed as “Adobe Flash Player 9.0.159.0 and 10.0.22.87 and earlier 9.x and 10.x versions”. So both of these bulletins mention version 10.0.22.87 as being vulnerable and recommend updating to version 10.0.32.18. But neither mention version 10.0.23.1 at all.


Is version 10.0.23.1 susceptible to the same “critical vulnerabilities” as version 10.0.22.87? I can’t find any version information about Flash 10.0.23.1 whatsoever. It could be that 10.0.23.1 has all, some, or none of the vulnerabilities in version 10.0.22.87. I do not know.


The only mention from Adobe regarding Snow Leopard’s version of Flash is this post on the Adobe Flash Platform Blog by Tom Barclay, which reads in its entirety:


> The initial release of Mac OS X 10.6 (Snow Leopard) includes an
> earlier version of Adobe Flash Player than what is available from
> Adobe.com. We recommend all users update to the latest, most secure
> version of Flash Player (10.0.32.18) — which supports Snow Leopard
> and is available for download from
> http://www.adobe.com/go/getflashplayer.


So, yes, Adobe clearly recommends upgrading to 10.0.32.18, but doesn’t mention any specific problems with 10.0.23.1.


**Update 2:**  Via Twitter, [Dj Walker-Morgan reports](http://twitter.com/Codepope/status/3783367229) that version 10.0.23.1 is the same version of Flash from the June WWDC seed of Snow Leopard, so it almost certainly doesn’t contain the fixes for the issues Adobe publicized in July.


---

1. 10.0.22.87 is, in fact, still the standard version of Flash in Mac OS X 10.5.8. ↩︎



| **Previous:** | [Regarding the Brouhaha Over the Version of Flash in Snow Leopard](https://daringfireball.net/2009/09/flash_snow_leopard) |
| **Next:** | [Regarding WordPress and Security](https://daringfireball.net/2009/09/regarding_wordpress_and_security) |


PreviousNext