---
title: "Choosing Anti-Anti-Virus Software"
date: 2007-02-28
url: https://blog.codinghorror.com/choosing-anti-anti-virus-software/
slug: choosing-anti-anti-virus-software
word_count: 1508
---

Now that Windows Vista has been available for almost a month, the comparative performance benchmarks are in.

- [Windows XP vs. Vista: The Benchmark Rundown](https://web.archive.org/web/20070302132220/http://www.tomshardware.com/2007/01/29/xp-vs-vista/page11.html#conclusion_ko_for_windows_vista) (Tom’s Hardware)
- [Windows Vista Performance Guide](https://web.archive.org/web/20070303113333/http://www.anandtech.com/systems/showdoc.aspx?i=2917&p=20) (Anandtech)


It’s about what I expected; rough parity with the performance of Windows XP. Vista’s a bit slower in some areas, and a bit faster in others. **But shouldn’t new operating systems perform *better* than old ones? There are plenty of low-level improvements under the hood. Why does Vista only *break even* in performance?**


To be fair, Vista does a lot more than XP. I don’t want to get into the whole XP vs. Vista argument here, but suffice it to say that the list of new [features in Vista](http://en.wikipedia.org/wiki/Features_new_to_Windows_Vista) is quite extensive – although perhaps not as extensive as some would like. [Vista’s integrated search](https://blog.codinghorror.com/typing-trumps-pointing/) alone is enough for me to banish XP from my life forever.


Microsoft has gotten a giant security shiner from Windows XP over the last five years. That’s why Windows Vista goes out of its way to radically improve security, with new features like User Account Control (UAC) and Windows Defender. The existing security features in XP, such as Windows Firewall and System Protection (aka restore points) were significantly overhauled and improved for Vista, too. Enhanced security is a good thing, but it’s never free. **In fact, Vista’s new security features will slow your PC down more than almost any other kind of software you can install**.


For best performance, the first thing I do on any new Vista install is this:

1. Turn off Windows Defender
2. Turn off Windows Firewall
3. Disable System Protection
4. Disable UAC


I’ve had friends remark how “slow” Vista feels compared to XP, but when I ask them whether they’ve disabled Defender or UAC, the answer is typically no. Of course your system is going to be slower with all these added security checks. Security is expensive, and [there ain’t no such thing as a free lunch](http://en.wikipedia.org/wiki/TANSTAAFL).


You might argue that three out of these four security features wouldn’t even be necessary in the first place **if Windows had originally followed the well-worn UNIX convention of separating standard users from privileged administrators**. I won’t disagree with you. But Windows’ long historical precedent of setting user accounts up by default as privileged administrators is Microsoft’s cross to bear. I can’t rewrite history, and neither can Microsoft. That’s why they came up with these painful, performance-sapping workarounds.


But this doesn’t mean you have to give up on security entirely in the name of performance. If you’re really serious about security, then **create a new user account with non-Administrator privileges, and log in as that user**. This isn’t the default behavior in Vista, sadly. Post install, you get an Administrator-But-Not-Really-Just-Kidding account which triggers UAC on any action that requires administrator privileges. I’m sure this torturous hack was conceived in the name of backwards compatibility, but that doesn’t mean *we* need to perpetuate it. The good news is that Vista is probably the first Microsoft operating system ever where you can actually work effectively as a standard, non-privileged user. As a standard user, you get all the benefits of UAC, Defender, and System Protection.. without all the performance drain.


Let me be clear here. I’m not against security. I’m against retrograde, band-aid, *destroy all my computer’s performance* security.


Speaking of retrograde, band-aid, *destroy all my computer’s performance *security, the one security feature Vista doesn’t bundle is anti-virus software. **And nothing cripples your PC’s performance quite like anti-virus software.** This isn’t terribly surprising if you consider what anti-virus software has to do: examine every single byte of data that passes through your computer for evidence of malicious activity. But who needs theory when we have Oli at The PC Spy. Oli conducted a remarkably thorough investigation of the real world performance impact of [security software on the PC](https://web.archive.org/web/20070225181141/http://www.thepcspy.com/articles/other/what_really_slows_windows_down/5). The results are truly eye-opening:

kg-card-begin: html


|  | Percent slower |
|  | Boot | CPU | Disk |
| Norton Internet Security 2006 | 46% | 20% | 2369% |
| McAfee VirusScan Enterprise 8 | 7% | 20% | 2246% |
| Norton Internet Security 2007 | 45% | 8% | 1515% |
| Trend Micro PC-cillin AV 2006 | 2% | 0% | 1288% |
| ZoneAlarm ISS | 16% | 0% | 992% |
| Norton Antivirus 2002 | 11% | 8% | 658% |
| Windows Live OneCare | 11% | 8% | 512% |
| Webroot Spy Sweeper | 6% | 8% | 369% |
| Nod32 v2.5 | 7% | 8% | 177% |
| avast! 4.7 Home | 4% | 8% | 115% |
| Windows Defender | 5% | 8% | 54% |
| Panda Antivirus 2007 | 20% | 4% | 15% |
| AVG 7.1 Free | 15% | 0% | 19% |


kg-card-end: html

The worst offenders are the anti-virus suites with real-time protection. According to these results, **the latest Norton Internet Security degrades boot time by nearly 50 percent. And no, that isn’t a typo in the disk column. It also makes all disk access *sixteen times slower!*** Even the better performers in this table would have a profoundly negative impact on your PC’s performance. Windows Defender, for example, “only” makes hard drive access 54 percent slower.


And yet, despite the crushing performance penalty, anti-virus software is *de rigeur* in the PC world. Most PC vendors would no sooner ship a PC without preinstalled anti-virus software than they would ship a PC without an operating system (yeah, you wish). The very thought of running a PC naked, vulnerable, unprotected from viruses sends system administrators screaming from the room in a panic. When you tell a sysadmin you dislike running anti-virus software, they’ll look at you mouth agape, as if you’ve just told them that you hate puppies and flowers.


I don’t see why they’re so shocked. anti-virus software itself, while not self-propagating like a virus, certainly fits the definition of a Trojan Horse. Once installed on your system, it has a hidden, unadvertised payload: it decimates your computer’s performance and your productivity. In my opinion, **what we really need is Anti-Anti-Virus software to keep us safe from the ongoing Anti-Virus software pandemic.**


I’ve never run any anti-virus software. And Mac or Linux (aka UNIX) users almost never run anti-virus software, either. Am I irresponsible to run all my computers without anti-virus software? Are Mac and Linux users irresponsible for not participating in the culture of fear that Windows anti-virus software vendors propagate? I think it’s braver and more responsible to recognize that anti-virus software vendors are not only telling us to be afraid, they are selling us fear. The entire anti-virus software industry is predicated on a bad architectural decision made by Microsoft fifteen years ago. And why, exactly, would any of these vendors want to solve the virus problem and put themselves out of business?


I’ll certainly agree that you can’t stop users from [clicking on dancing bunnies](https://blog.codinghorror.com/the-dancing-bunnies-problem/) if they have their mind set on it. You should have a few different security layers in any modern operating system. But we should also be treating the disease first – *too many damn users running as administrators –* instead of the symptoms.


As for remediation strategies, I’m a fan of [the virtual machine future](https://blog.codinghorror.com/our-virtual-machine-future/). We should treat our operating system like a roll of paper towels. If you get something on it you don’t like, you ball it up and throw it away, and rip off a new, fresh one. But if that’s too radical for you, I think Jan Goyvaerts is on to something with good old plain [common sense backups](https://web.archive.org/web/20070306101255/http://www.shareware-beach.com/2007/02/the-value-of-os-disk-images/):


> In fact, with a proper backup system in place, you don’t have to be afraid of messing up your system. **I don’t use any anti-virus or anti-spyware software.** If my system starts acting up, I’ll restore the backup, and have a guaranteed clean system. No spyware remover can beat that. If I want to play with beta software, I don’t have to inconvenience myself by running it in a virtual machine. I do use VMware for testing my applications on clean installs of Windows. But when beta testing new versions of tools I use for development, I want to test them in my actual development environment rather. When the beta expires, I wipe it off by restoring the OS backup.


It’s not terribly different from my virtual machine solution. Either way, you go back to a known good checkpoint. And I’ll take a backup strategy over a computer with hobbled performance any day.


This also begs the question of what safety really means. No matter how much security software you install, nagging users with dozens of security dialogs clearly [doesn’t make users any safer](https://blog.codinghorror.com/windows-vista-security-through-endless-warning-dialogs/). We should give users a basic level of protection as standard non-administrator users. But beyond that, let users make mistakes, and **provide automatic, unlimited undo.** That’s the ultimate safety blanket.

[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[performance benchmarks](https://blog.codinghorror.com/tag/performance-benchmarks/)
[security](https://blog.codinghorror.com/tag/security/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
