---
title: "Open Wireless and the Illusion of Security"
date: 2008-06-29
url: https://blog.codinghorror.com/open-wireless-and-the-illusion-of-security/
slug: open-wireless-and-the-illusion-of-security
word_count: 997
---

[Bruce Schneier](http://en.wikipedia.org/wiki/Bruce_Schneier) is something of a legend in the computer security community. He’s the author of the classic, oft-cited 1994 book [Applied Cryptography](http://www.amazon.com/exec/obidos/ASIN/0471117099), as well as several well-known cryptography algorithms.


![](https://blog.codinghorror.com/content/images/2025/04/image-159.png)


The cheeky Norris-esque design above is a reference to the actor names commonly used in examples of [shared secret key exchange](http://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange#Description).


What I find most interesting about Bruce, however, is that he has moved beyond treating computer security as a problem that can be solved with increasingly clever cryptography algorithms:


> **Schneier now denounces his early success as a naïve, mathematical, and ivory tower view of what is inherently a people problem**. In Applied Cryptography, he implies that correctly implemented algorithms and technology promise safety and secrecy, and that following security protocol ensures security, regardless of the behavior of others. Schneier now argues that the incontrovertible mathematical guarantees miss the point. As he describes in [Secrets and Lies](http://www.amazon.com/exec/obidos/ASIN/0471453803), a business which uses RSA encryption to protect its data without considering how the cryptographic keys are handled by employees on “complex, unstable, buggy” computers has failed to properly protect the information. An actual security solution that includes technology must also take into account the vagaries of hardware, software, networks, people, economics, and business.


This is the programming equivalent of **realizing that **[**Peopleware**](https://blog.codinghorror.com/peopleware-revisited/)** is ultimately a much more important book than **[**The Art of Computer Programming**](https://blog.codinghorror.com/the-enduring-art-of-computer-programming/)**.** The shift in focus from algorithms to people is even more evident if you frequent [Bruce’s excellent blog](http://www.schneier.com/blog/), or read his newest books Practical Cryptography and [Beyond Fear](http://www.amazon.com/exec/obidos/ASIN/0387026207).


As much as I respect Bruce, I was surprised to read that he intentionally [keeps his wireless network open](http://www.schneier.com/blog/archives/2008/01/my_open_wireles.html).


> Whenever I talk or write about my own security setup, the one thing that surprises people – and attracts the most criticism – is the fact that I run an open wireless network at home. There’s no password. There’s no encryption. Anyone with wireless capability who can see my network can use it to access the internet.


I’ve advocated WiFi encryption from the day I owned my first wireless router. As I encountered fewer and fewer open WiFi access points over the years, I viewed it as tangible progress. Reading Bruce’s opinion is enough to make me question those long held beliefs.


It’s a strange position for a respected computer security expert to advocate. But I think I get it. Security is a tough problem. If you take the option of mindlessly flipping a [WPA](http://en.wikipedia.org/wiki/Wi-Fi_Protected_Access) or [WEP](http://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) switch off the table, you’re now forced to think more critically about the security of not only your network, but also the fundamental security of the data on your computers. By advocating the radical idea that your wireless network should be *intentionally* kept open, Bruce is attempting to **penetrate the veil of false algorithmic security**.


I may understand and even applaud this effort, but I don’t agree. Not because I’m worried about the security of my data, or any of the half-dozen other completely rational security arguments you could make against intentionally keeping an open wireless network. My concerns are more prosaic. **I desperately want to protect the thin sliver of upstream bandwidth my provider allows me**. Some major internet providers are also [talking about monthly download caps](http://tech.slashdot.org/article.pl?sid=08/05/08/1410231), too. Bruce’s position only makes sense if you have effectively unlimited bandwidth in both directions. Basically, I’m worried about the [tragedy of the bandwidth commons](http://en.wikipedia.org/wiki/Tragedy_of_the_commons). As much as I might like my neighbors, they can pay for their own private sliver of bandwidth, or knock on my door and ask to share if they *really* need it.


So, to me at least, enabling wireless security is my way of ensuring that I get every last byte of the bandwidth I paid for that month.


It’s worth realizing, however, that wireless security is no panacea, even in this limited role. Given a sufficiently motivated attacker, every wireless network is crackable.


![](https://blog.codinghorror.com/content/images/2025/04/image-158.png)


With that in mind, here are a few guidelines.

1. **WEP = Worthless Encryption Protocol**
WEP, the original encryption protocol for wireless networks, is so fundamentally flawed and so deeply compromised it should arguably be removed from the firmware of every wireless router in the world. It’s possible to crack WEP in [under a minute](http://www.practicallynetworked.com/security/041207wpa_vs_wep.htm) on any vaguely modern laptop. If you choose WEP, you have effectively chosen to run an open wireless network. There’s no difference.
2. **WPA *requires* a very strong password**
The common “personal” (PSK) variant of WPA is quite vulnerable to brute force dictionary attacks. It only takes a trivial amount of wireless sniffing to obtain enough data to attack your WPA password *offline* – which means an unlimited amount of computing power could potentially be marshalled against your password. While [brute force attacks are still for dummies](https://blog.codinghorror.com/hardware-assisted-brute-force-attacks-still-for-dummies/), most people are, statistically speaking, dummies. They [rarely pick good passwords](http://www.schneier.com/blog/archives/2006/12/realworld_passw.html). If ever there was a time to take my advice on [using long passphrases](https://blog.codinghorror.com/passphrase-evangelism/), this is it. Experts recommend you shoot for a [33 character passphrase](http://wifinetnews.com/archives/002452.html).
3. **Pick a unique SSID (name) for your wireless network**
[Default wireless network names](http://www.wigle.net/gps/gps/main/ssidstats) just scream *I have all default settings!* and attract hackers like flies to honey. Also, [pre-generated rainbow tables](http://www.renderlab.net/projects/WPA-tables/) exist for common SSIDs.
4. **Use WPA2 if available**
As of 2006, WPA2 is required on any router that bears the WiFi certification. WPA2, as the name might suggest, is designed to replace WPA. It has stronger and more robust security. There’s no reason to use anything less, unless your hardware doesn’t support it. And if that’s the case, *get new hardware*.


In the end, perhaps wireless security is more of a deterrent than anything else, another element of defense in depth. It’s important to consider the underlying message Bruce was sending: if you’ve enabled WEP, or WPA with anything less than a truly random passphrase of 33 characters, you don’t have security.


You have the *illusion* of security.


And that is far more dangerous than no security at all.

[security](https://blog.codinghorror.com/tag/security/)
[cryptography](https://blog.codinghorror.com/tag/cryptography/)
[bruce schneier](https://blog.codinghorror.com/tag/bruce-schneier/)
[network security](https://blog.codinghorror.com/tag/network-security/)
[open wireless](https://blog.codinghorror.com/tag/open-wireless/)
