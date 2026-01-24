---
title: "Welcome to The Internet of Compromised Things"
date: 2015-08-08
url: https://blog.codinghorror.com/welcome-to-the-internet-of-compromised-things/
slug: welcome-to-the-internet-of-compromised-things
word_count: 1842
---

This post is a bit of a public service announcement, so I’ll get right to the point:


> Every time you use WiFi, ask yourself: **could I be connecting to the Internet through a compromised router with malware?**


It’s becoming more and more common to see malware installed not at the server, desktop, laptop, or smartphone level, but at the *router* level. Routers have become quite capable, powerful little computers in their own right over the last 5 years, and that means they can, unfortunately, be harnessed to work against you.


I write about this because **it recently happened to two people I know.**


> @jchris A friend got hit by this on newly paved win8.1 computer. Downloaded Chrome, instantly infected with malware. Very spooky. 
> – not THE Damien Katz (@damienkatz) May 20, 2015


> @codinghorror *no* idea and there’s almost ZERO info out there. Essentially malicious JS adware embedded in every in-app browser 
> – John O’Nolan (@JohnONolan) August 7, 2015


In both cases, they eventually determined the source of the problem was that **the router they were connecting to the Internet through had been compromised**.


This is way more evil genius than infecting a mere *computer*. If you can manage to systematically infect common home and business routers, you can potentially compromise **every computer connected to them.**


![](https://blog.codinghorror.com/content/images/2015/08/muahahaha.jpg)


Hilarious meme images I am contractually obligated to add to each blog post aside, this is scary stuff and you should be scared.


Router malware is the ultimate man-in-the-middle attack. For all meaningful traffic sent through a compromised router [that isn’t HTTPS encrypted](https://blog.codinghorror.com/should-all-web-traffic-be-encrypted/), it is 100% game over. The attacker will certainly be sending all that traffic somewhere they can sniff it for anything important: logins, passwords, credit card info, other personal or financial information. And they can direct you to [phishing websites](https://blog.codinghorror.com/phishing-the-forever-hack/) at will – if you think you’re on the “real” login page for the banking site you use, think again.


Heck, even if you completely trust the person whose router you are using, they could be technically be doing this to you. But they probably aren’t.


*Probably.*


In John’s case, the attackers inserted annoying ads in all unencrypted web traffic, which is an obvious tell to a sophisticated user. But how exactly would the average user figure out where this junk is coming from (or worse, assume the regular web is just full of ad junk all the time), when even a technical guy like John – founder of the [open source Ghost blogging software](https://ghost.org/) used on this very blog – was flummoxed?


But that’s OK, we’re smart users who would *only* access public WiFi using HTTPS websites, right? Sadly, **even if the traffic *is* HTTPS encrypted, it can still be subverted!** There’s an extremely technical [blow-by-blow analysis](https://web.archive.org/web/20150826150835/https://cryptostorm.org/viewtopic.php?f=67&t=8713) at Cryptostorm, but the TL;DR is this:


> Compromised router answers DNS req for *.google.com to 3rd party with faked HTTPS cert, you download malware Chrome. Game over.


HTTPS certificate shenanigans. DNS and BGP manipulation. Very hairy stuff.


How is this possible? Let’s start with the weakest link, your router. Or more specifically, **the programmers responsible for coding the admin interface to your router**.


They must be terribly incompetent coders to let your router get compromised over the Internet, since one of the major selling points of a router is to act as a basic firewall layer between the Internet and you… right?


In their defense, that part of a router generally works as advertised. More commonly, you *aren’t* being attacked from the hardened outside. **You’re being attacked from the soft, creamy inside.**


![](https://blog.codinghorror.com/content/images/2025/02/image-103.png)


That’s right, *the calls are* [*coming from inside your house*](https://tvtropes.org/pmwiki/pmwiki.php/Main/TheCallsAreComingFromInsideTheHouse)*!*


By that I mean you’ll visit a malicious website that **scripts your own browser to access the web-based admin pages of your router, and reset (or use the default) admin passwords to reconfigure it.**


Nasty, isn’t it? They attack from the inside [using your own browser](https://arstechnica.com/information-technology/2014/03/hackers-hijack-300000-plus-wireless-routers-make-malicious-changes/). But that’s not the only way.

- Maybe you accidentally turned on remote administration, so your router can be modified from the outside.
- Maybe you left your router’s admin passwords at default.
- Maybe there is a legitimate external exploit for your router and you’re running a very old version of firmware.
- Maybe your ISP provided your router and made a security error in the configuration of the device.


In addition to being kind of terrifying, this does not bode well for the Internet of Things.


![](https://blog.codinghorror.com/content/images/2015/08/internet-of-compromised-things.png)


Internet of *Compromised* Things, more like.


OK, so what can we do about this? There’s no perfect answer; I think it has to be a defense in depth strategy.


### Inside Your Home


**Buy a new, quality router.** You don’t want a router that’s years old and hasn’t been updated. But on the other hand you also don’t want something *too* new that hasn’t been vetted for firmware and/or security issues in the real world.


Also, any router your ISP provides is going to be about as crappy and “recent” as the awful stereo system you get in a new car. So I say stick with well known consumer brands. There are some hardcore folks who think [all consumer routers are trash](https://routersecurity.org/), so YMMV.


I can recommend the Asus RT-AC87U – it did very well in the [SmallNetBuilder](https://www.smallnetbuilder.com/) tests, Asus is a respectable brand, it’s been out a year, and for most people, this is *probably* an upgrade over what you currently have without being totally bleeding edge overkill. I know it is an upgrade for me.


![](https://blog.codinghorror.com/content/images/2025/02/image-104.png)


(I am also eagerly awaiting [Eero](https://eero.com/) as a domestic best of breed device with amazing custom firmware, and have one pre-ordered, but it hasn’t shipped yet.)


**Download and install the latest firmware**. Ideally, do this before connecting the device to the Internet. But if you connect and then immediately use the firmware auto-update feature, who am I to judge you.


**Change the default admin passwords**. Don’t leave it at the documented defaults, because then it could be potentially scripted and accessed.


**Turn off WPS**. Turns out the Wi-Fi Protected Setup feature intended to make it “easy” to connect to a router by pressing a button or entering a PIN made it… a bit too easy. This is *always* on by default, so be sure to disable it.


**Turn off uPNP**. Since we’re talking about attacks that come from “inside your house,” uPNP offers zero protection as it has [no method of authentication](https://security.stackexchange.com/questions/38631/what-are-the-security-implications-of-enabling-upnp-in-my-home-router). If you need it for specific apps, you’ll find out, and you can forward those ports manually as needed.


**Make sure remote administration is turned off.** I’ve *never* owned a router that had this on by default, but check just to be double plus sure.


**For Wifi, turn on WPA2+AES and use a long, strong password.** Again, I feel most modern routers get the defaults right these days, but just check. The password is your responsibility, and [password strength matters tremendously](https://blog.codinghorror.com/open-wireless-and-the-illusion-of-security/) for wireless security, so be sure to make it a long one – at least 20 characters with all the variability you can muster.


**Pick a unique SSID.** Default SSIDs just scream *hack me, for I have all defaults and a clueless owner*. And no, don’t bother “hiding” your SSID, [it’s a waste of time](https://web.archive.org/web/20150820052745/http://www.howtogeek.com/howto/28653/debunking-myths-is-hiding-your-wireless-ssid-really-more-secure/).


**Optional: use less congested channels for WiFi.** The default is “auto,” but you can sometimes get better performance by picking less used frequencies at the ends of the spectrum. As summarized by official ASUS support reps:

- Set 2.4 GHz channel bandwidth to 40 MHz, and change the control channel to 1, 6 or 11.
- Set 5 GHz channel bandwidth to 80 MHz, and change the control channel to 165 or 161.


**Experts only: install an open source firmware.** I discussed this a fair bit in [Everyone Needs a Router](https://blog.codinghorror.com/because-everyone-still-needs-a-router/), but you have to be very careful which router model you buy, and you’ll probably need to stick with older models. There are several which are specifically sold to be friendly to open source firmware.


### Outside Your Home


Well, this one is simple. Assume everything you do outside your home, on a remote network or over WiFi is being monitored by **IBGs**: Internet Bad Guys.


![](https://blog.codinghorror.com/content/images/2015/08/internet-bad-guy.jpg)


I know, kind of an oppressive way to voyage out into the world, but it’s better to start out with a defensive mindset, because you could be connecting to anyone’s compromised router or network out there.


But, good news. There are only two key things you need to remember once you’re outside, facing down that fiery ball of hell in the sky and armies of IBGs.

1. **Never access anything but HTTPS websites. **If it isn’t available over HTTPS, *don’t go there! *You might be OK with HTTP if you are not logging in to the website, just browsing it, but even then IBGs could inject malware in the page and potentially compromise your device. And never, ever enter anything over HTTP you aren’t 100% comfortable with bad guys seeing and using against you somehow.We’ve made tremendous [progress in HTTPS](https://blog.codinghorror.com/should-all-web-traffic-be-encrypted/) everywhere over the lasrt 5 years, and these days most major websites offer (or even better, force) HTTPS access. So if you just want to quickly check your GMail or Facebook or Twitter, you will be fine, because those services all force HTTPS.
2. **If you must access non-HTTPS websites, or you are not sure, *always* use a VPN**.A VPN encrypts all your traffic, so you no longer have to worry about using HTTPS. You do have to worry about whether or not you [trust your VPN provider](https://torrentfreak.com/can-you-trust-your-vpn-provider-130929/), but that’s a much longer discussion than I want to get into right now.


It’s a good idea to pick a go-to VPN provider so you have one ready and get used to how it works over time. Initially it will feel like a bunch of extra work, and it kinda is, but if you care about your security an encrypt-everything VPN is bedrock. And if you don’t care about your security, well, why are you even reading this?


If it feels like these are both variants of the same rule, *always strongly encrypt everything*, you aren’t wrong. That’s [the way things are headed](https://letsencrypt.org/). The math is as sound as it ever was – but unfortunately the people and devices, less so.


### Be Safe Out There


Until I heard Damien’s story and John’s story, I had no idea router hardware could be such a huge point of compromise. I didn’t realize that you could be innocently visiting a friend’s house, and because he happens to be the parent of three teenage boys and the owner of an old, unsecured router that you connect to via WiFi… *your* life will suddenly get a lot more complicated.


As the amount of stuff we connect to the Internet grows, we have to understand that **the Internet of Things is a bunch of tiny, powerful computers, too** – and they need the same strong attention to security that our smartphones, laptops, and servers already enjoy.

[security](https://blog.codinghorror.com/tag/security/)
[internet of things](https://blog.codinghorror.com/tag/internet-of-things/)
[malware](https://blog.codinghorror.com/tag/malware/)
[router](https://blog.codinghorror.com/tag/router/)
[compromised](https://blog.codinghorror.com/tag/compromised/)
