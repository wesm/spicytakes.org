---
title: "Looney Tunes"
date: 2003-06-02
url: https://daringfireball.net/2003/06/looney_tunes
slug: looney_tunes
word_count: 2096
---


Apple’s disabling of Internet sharing in last week’s iTunes 4.0.1 update caused quite a stir. I’m baffled — not by Apple’s decision, but by much of the reaction to it. It is simply beyond me to understand how so many people could express such venomous disdain toward Apple for disabling a capability that was so obviously turning into a huge problem.


But while I don’t think Apple deserves criticism for their decision to prevent Internet sharing in iTunes 4.0.1, let’s be clear that Internet sharing via iTunes 4.0 was not an accident, as some defenders of Apple have claimed by pointing to passages in iTunes 4.0’s help, such as the following:


> If your computer is connected to any other computers over a local network and you’re using Mac OS X version 10.2.4 or later, you can share the music in your library and playlists with up to five of those computers (in the same subnet as your computer). Sharing is intended for personal use only.


But other passages in the 4.0 help clearly indicate that sharing was also intended to work across wide area networks, provided you knew the host’s IP address. For example, from `iTunes.app/Contents/Resources/English.lproj/iTunes Help/pgs/696.html`:


> You can also set your sharing preferences to look for shared music. Any shared music that’s available on your network appears in your iTunes Source list. You can also see the shared music on a specific computer that isn’t in the same subnet, if you know the computer’s IP address.


Note also that Internet sharing is not Rendezvous sharing. *Rendezvous* is a local networking protocol, and so quite obviously Rendezvous sharing could only ever work locally. “Rendezvous sharing” is just a marketing term — at a technical level, sharing music in iTunes 4.0 worked the same way locally as it did over the entire Internet — it’s just that when sharing locally, you got auto-discovery and therefore didn’t need to know any IP addresses.


What iTunes 4.0 allowed, and 4.0.1 does not, is Internet-wide sharing. This had nothing to do with Rendezvous, and Apple did not promote this capability, nor give the capability a marketing name. But it wasn’t an accident.


I think it was more of a social experiment. Rendezvous networking is built on top of IP networking, so once the programming work was done to support sharing locally, it was likely very little extra work to allow it to work between any two IP addresses. The potential for abuse was obvious, but so was the potential utility. And so I think Apple tried giving everyone the benefit of the doubt with iTunes 4.0’s sharing capabilities.


The problem is that third-party software sprung up that effectively turned iTunes 4.0 into a Napster-style P2P music distribution application. [iLeech](http://ileech.sourceforge.net/) and [iSlurp](http://www.oatbit.com/iSlurp/), for example — these guys weren’t even subtle.


Note that I’m not passing moral or legal judgment on these apps or the people who used them. The point is only that these applications turned iTunes 4 into something Apple never intended it to be. Streaming is one thing; copying is another.


You’ll get no argument from me that the RIAA has its collective head up its ass with regard to online music distribution. Any industry that expresses outright hostility toward its most enthusiastic customers is in trouble. So if you want to be angry at the RIAA, fine. But Apple is not the RIAA, nor is Apple in any position whatsoever to dictate to the RIAA. The RIAA is vehemently opposed to software that allows you to freely copy arbitrary MP3 files from servers on the Internet. Software like iLeech and iSlurp effectively turned iTunes into just that.


Thus, Apple’s only possible options were to disable Internet sharing in iTunes, or to wage a costly legal battle with the RIAA. It’s absolutely unreasonable to expect Apple to have chosen the latter. *Choose your battles wisely*, the saying goes, and regardless of righteousness, a P2P battle against the RIAA would be just about the most foolish thing Apple could do.


Knee-jerk critics of Apple’s iTunes decision accuse Apple both of fellating the RIAA, and disrespecting iTunes users by yanking a useful feature. Neither is true.


The major new features in iTunes 4 address two disparate needs. First is that people want to download new music online, cheaply. Napster, famously, blazed this particular trail — so cheap that it was free, and quite successful at providing access to a large library of music. But the Napster party didn’t last long, and its successors — Gnutella, et al — have been forced to decentralize in order to avoid the wrath of the RIAA. This decentralization has been successful in terms of staying afloat, but it hasn’t made the process of finding and downloading songs either easy or reliable. Your mileage may vary, of course, but in my experience, none of the current bootlegging services work nearly as well as Napster did. And Napster wasn’t exactly smooth sailing.


And so Apple has attacked this problem by creating the iTunes Music Store. At 99 cents a song, it is infinitely more expensive than the bootlegging services — but it offers vastly superior reliability and ease-of-use, and still falls in the category of “cheap”.


The second problem iTunes 4 addresses is that people want remote access to the music they’ve already obtained. If you’ve built a large iTunes library on one Mac, it’d be nice to have access to those songs and playlists from other machines. iTunes 4 attempts to solve this problem with its music sharing features.


So the problem is that by allowing streamed music sharing over the Internet, iTunes 4.0 also opened the door for *copying* music over the Internet. Once this happened, iTunes’s Internet-wide music sharing was in conflict with the iTunes Music Store. There is no logical way you can claim that iTunes could act, simultaneously, as (1) an RIAA-sanctioned front end to the ITMS, and (2) as bootlegging software the RIAA deems illegal. That it was only a minority of iTunes users who abused Internet sharing makes no difference.


Apple’s decision was not about preventing bootlegging; it was about preventing the use of *iTunes* as a bootlegging tool. There is a huge difference. You can still stream music from your Mac over the Internet — you just can’t do it using iTunes. [iCommune](http://icommune.sourceforge.net/) comes to mind as the best option out there.


## Rebuttals to Certain of the Aforementioned Knee-Jerk Critics


Cory Doctorow posted his frothing take on the situation, “[Apple force-feeds customers shit, calls it sunshine](http://boingboing.net/2003_05_01_archive.html#200349509)”, within hours of iTunes 4.0.1’s release. He wrote:


> So, in other words, Apple has “enhanced” iTunes so that it can’t be used to play music from one computer on another if they’re on different subnets (i.e., if you have a computer at home that you stream to from work).


Doctorow claims the iTunes 4.0.1 release notes describe the disabling of Internet sharing as an “enhancement”. Curse those slick corporate marketers. Too bad it’s not true. The iTunes 4.0.1 release notes, as displayed in Software Update, state: *iTunes 4.0.1 includes a number of performance and network access enhancements, and only allows music sharing between computers using iTunes 4.0.1 or later on a local network (in the same subnet).*


So Apple claims (1) there are enhancements; *and* (2) Internet sharing has been disabled, as is the ability to share music between iTunes 4.0 and iTunes 4.0.1. “And” joins two separate clauses, last time I checked. So in fact Apple was forthright about the sharing changes in version 4.0.1, and the update is in no way mandatory.


And by the way, there really are legitimate enhancements in version 4.0.1, including fixes for (1) the AppleScript bug I complained about [here](http://daringfireball.net/2003/04/observations_regarding_itunes_4.html), wherein you couldn’t use AppleScript to obtain references to tracks in shared music libraries; and (2) a highly annoying [volume fluctuation bug](http://docs.info.apple.com/article.html?artnum=93051).


Back to Doctorow:


> Apple’s apologists say that this is to prevent “stealing,” but there are many legitimate uses for the feature (imagine if Paul Frank “enhanced” his jackets by sewing the pockets shut to make them less useful for shoplifters).


There is no dispute that there are legitimate uses for the feature. That’s why it was there in the first place. The problem is that those who abused it put the feature in direct conflict with the iTunes Music Store. It’s not that Apple is forcing us to use the ITMS, or preventing us from using P2P software to share music — they simply don’t want to enable the use of *iTunes itself* as an Internet-wide sharing server.


> Apple has removed a useful feature from its software, and its customers are out in the cold. I paid $50 or so for downloadable iTunes tracks, with the understanding that Apple had sold me something that would stream over the Internet. Yesterday, they had. Today, they took it away. And they called it an “enhancement.”
> Sure, I could just skip the update, but how long will that work for? When 10.3 ships next year, will I be able to run an unupdated iTunes on it? Will I have to pickle a computer and keep from updating it in order to continue to use my iTunes music in  the way I was promised I could?


First, as stated earlier, they didn’t call it an “enhancement”. Second, I’m not aware of any “promise” made by Apple with regard to ITMS songs being streamable over the Internet. Yes, you could do it with iTunes 4.0, but as far as I can see, this was never touted as a feature of ITMS AAC files. I can this how this might be disappointing, but it certainly isn’t a broken promise.


> Apple wants to be the leader of the Digital Lifestyle pack.


Clearly, Apple *is* the leader of this particular pack.


> But Apple is choosing to screw its customers and kowtow to the entertainment interests who have, at various times, tried to ban the piano roll, the radio, the VCR, and the Internet. They’re putting the desires of the companies that tried to ban firewalls ahead of the legitimate expectations of their customers. A digital lifestyle designed by Hilary Rosen and Jack Valenti is a world of “consumers” (us) and “producers” (them). It’s the opposite of the iApps philosophy.


Apple’s decision does not prevent P2P music sharing. It only prevents music sharing using iTunes as the server.


> It’s a world I don’t want to live in.


Terrific. Might I suggest starting [here](http://www.dell.com/)?


Next on the rebuttal list is [Steve Mallett, who wrote on his O’Reilly weblog](http://www.oreillynet.com/pub/wlg/3238):


> One of my fears of buying an Apple came true yesterday.


Looks like somebody needs to start reading [Crazy Apple Rumors](http://crazyapplerumors.com/2003_05_18_archive.htm#200329733).


> [Apple crippled iTunes](http://rss.com.com/2100-1027_3-1010541.html?tag=fd_top) in a somewhat sneaky, under the radar kind of way.  With the newest update, some of iTunes ‘sharing’ capabilities were dismantled.


What was sneaky about it?


> Let’s just say this isn’t something you see happening to the Linux kernel OK, but this is a proprietary application […]


Which is why so many Linux MP3 players have something similar to the ITMS.


> I don’t think this would have happened in the pre Apple Music store era.  Now it looks like the Music store, which iTunes is integral in, is a major revenue stream for Apple.


Define “major”. In their [most recent quarterly statement](http://www.apple.com/pr/library/2003/apr/16earnings.html), Apple reported revenue of $1.475 *billion*. That’s three months. Now at a million songs a week, that’s only around $15 *million* a quarter in additional revenue. I’m rounding up here, not to mention that an estimate of one million songs a week is probably way high. Admittedly, the *potential* for significant revenue in the future is there, but Mallett is speculating on the present, not the future.


> I’m going to reserve total judgement on this, other than to say I’m feeling a little discouraged, to see how this plays out over the next week.  It will be interesting to see how much your interests are discussed.


OK, let’s discuss our interests. In what way are iTunes users worse off than the users of any other digital music software, for any platform? That iTunes could potentially be even better — by allowing Internet-wide sharing as did version 4.0 — is indeed unfortunate. But Apple is still providing its customers with the best personal music software in the world, by far.


> Let’s all remember that people can continue to share their legally purchased music without iTunes at all.


At least we agree on something.



| **Previous:** | [Waferbaby Interview](https://daringfireball.net/2003/05/waferbaby_interview) |
| **Next:** | [Noted](https://daringfireball.net/2003/06/noted) |


PreviousNext