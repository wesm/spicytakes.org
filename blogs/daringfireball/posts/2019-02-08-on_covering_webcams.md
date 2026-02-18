---
title: "On Covering Webcams"
date: 2019-02-08
url: https://daringfireball.net/2019/02/on_covering_webcams
slug: on_covering_webcams
word_count: 1375
---


I’m a big fan of Joanna Stern — she was in fact [just on my podcast](https://daringfireball.net/thetalkshow/2019/01/23/ep-241) and it was one of my favorite episodes in a while. At the end of the episode, she mentioned that she was working on a piece about webcam security for her Personal Tech column at The Wall Street Journal. [That column dropped yesterday](https://www.wsj.com/articles/what-i-learned-from-the-hacker-who-spied-on-me-11549559728), and I found it half enlightening, half maddening.


> How secure are these tiny eyes into our private lives? The bad
> news is, it was possible for Mr. Heid to get into my Windows 10
> laptop’s webcam and, from there, my entire home network. He also
> eventually cracked my MacBook Air. The good news is that both
> operating systems were initially able to thwart the hacker. It
> took me performing some intentionally careless things for him to
> “succeed.”


Key words there: *intentionally careless*.


Here’s how he got into her Windows 10 laptop — admittedly using only “off-the-shelf hacking tools”:


> When I opened the attached Word doc, Microsoft ’s built-in, free
> anti-virus software, Windows Defender, immediately flagged it.
> When I clicked the link to the “reel,” the file that began
> downloading was identified as a virus and deleted. The system
> worked, but I wanted to see what would happen if I were someone
> who didn’t have anti-virus turned on in the first place, or who
> turned it off because it got annoying.


Here’s how the security expert got into her MacBook (again, using only “off-the-shelf hacking tools”):


> Hacking a 2015 MacBook Air running the latest MacOS version,
> Mojave, also required a multistep process (and some missteps by
> the “victim”). This time the malware was embedded in an .odt
> document, an open-source file format.
> To open it, I downloaded LibreOffice. The free version of the
> popular open-source office suite isn’t in the Mac App Store,
> however, so I had to disable the Mac security setting that
> prevents unverified developer software installation. […]
> Once I installed LibreOffice, I turned off its macro security
> setting, per the hacker’s instructions. There are scenarios where
> you might do this — say, for instance, because your company used
> a specially designed inventory spreadsheet or sales form — but
> for most people, it’s a bad idea. […]
> I did get a pop-up asking for camera access, and I clicked OK,
> like we might do when we’re in a rush. Because Mr. Heid was only
> snapping stills, the webcam LED only lit up for a second.


So she had to download LibreOffice (weird), disable LibreOffice’s macro security (really weird), and then *still* had to grant explicit permission for LibreOffice to access the camera. If you open a document that prompts you for access to the camera, aren’t you expecting it to be able to access your camera?


Stern’s advice to Mac users:


> Installing those nagging security and OS updates are a must —
> on your phone, laptop, router, thermostat, really anything
> that connects to the internet. They include the latest
> attempts to patch the holes that hackers use to get in. Mac
> users should install Malwarebytes or other malware-fighting
> software — and don’t turn off any security features just
> because someone asks you to.


I’ve long argued that third-party anti-malware software on the Mac causes more problems than it solves. If someone is willing to ignore the warning from MacOS that an app isn’t from a verified developer, and is willing to disable the security settings in that app at the behest of a social engineering hacker, why wouldn’t that same person be gullible enough to also disable their anti-malware software?


Stern also claims she’s now using a physical stick-on camera cover. But why? In both cases — Mac and PC — the built-in system software did its job and issued clear warnings that she had to ignore for the attack to proceed. And even then — on both Mac and PC — the light next to the camera went on when it was in use.


There’s nothing in Stern’s story that makes me worry in the least bit about the security of my Mac webcams, and I don’t see anything that should worry someone running Windows 10 with Windows Defender (Microsoft’s built-in security software). The path to compromising Stern’s cameras was like a test of your home security that starts with a request that you leave your door unlocked and turn off your alarm system.


I have never understood the mass paranoia over laptop webcams — which have in-use indicator lights, which I’ve seen no evidence can be circumvented on Macs from the last decade — and the complete lack of similar paranoia over microphones, which cannot be blocked by a piece of tape and which have no in-use indicator lights. And I don’t see anyone taping over the cameras on their phones. This story is only going to feed that paranoia, because the takeaway is going to be “*The Wall Street Journal says you should cover up your webcam.*”


---


[Security researchers at Johns Hopkins released a paper in 2013](http://arstechnica.com/security/2013/12/perv-utopia-light-on-macbook-webcams-can-be-bypassed/) revealing that the indicator lights on Macs released prior to 2008 could be circumvented by software. I linked to this in 2016, wondering if the same exploit was possible on more recent Macs. Here’s an answer I received from a former engineer at Apple who was intimately familiar with the software drivers for Mac webcams:


> The original cameras had the problem that the JHU researchers
> detailed in the article that your linked to. Problem was that the
> firmware was downloaded on every boot and there was no
> security/encryption mechanism for verifying it. The part used was
> fairly common and the firmware was just in RAM (hence the loading
> after a cold boot), as oppose to flashed.
> All cameras after that one were different: The hardware team
> tied the LED to a hardware signal from the sensor: If the (I
> believe) vertical sync was active, the LED would light up. There
> is NO firmware control to disable/enable the LED. The actual
> firmware is indeed flashable, but the part is not a generic part
> and there are mechanisms in place to verify the image being
> flashed. […]
> So, no, I don’t believe that malware could be installed to enable
> the camera without lighting the LED. My concern would be a
> situation where a frame is captured so the LED is lit only for a
> very brief period of time.


The still photo problem — where the light only turns on for the instant the image is being captured — is interesting. But I would wager real money that the camera indicator light cannot be circumvented by software on any Mac released this decade.


[As I wrote back in 2016 about taping over your webcam](https://daringfireball.net/linked/2016/06/23/):


> I think this is nonsense. Malware that can surreptitiously engage
> your camera can do all sort of other nefarious things. If you
> can’t trust your camera, you can’t trust your keyboard either.
> Follow best practices to avoid malware in the first place — don’t
> install Flash Player, and don’t install software from sketchy
> sources — and you’ll almost certainly be fine.


The problem isn’t your camera, it’s malware. Don’t install any software from unknown or sketchy sources, keep your OS up to date1, and you should be fine. And if you do have malware on your Mac, the webcam is likely the least of your problems.


---

1. MacOS 10.14 Mojave, in particular, has made some significant improvements to identifying and disabling malware automatically. I got a fascinating email from a Genius Bar tech recently, who said that his time the last few years had been consumed more and more by Mac malware problems. Then Mojave shipped, and malware problems dropped noticeably, and when he does see a malware problem these days, it’s almost always on a Mac that isn’t running Mojave. ↩︎



| **Previous:** | [25 Years Ago: RAM Doubler](https://daringfireball.net/2019/01/ram_double_engst) |
| **Next:** | [My 2018 Apple Report Card](https://daringfireball.net/2019/02/my_2018_apple_report_card) |


PreviousNext