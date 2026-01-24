---
title: "Power, Surge Protection, PCs, and You"
date: 2006-07-11
url: https://blog.codinghorror.com/power-surge-protection-pcs-and-you/
slug: power-surge-protection-pcs-and-you
word_count: 1420
---

A question recently came up on the internal Vertigo mailing list about **surge protection for home equipment and computers**:

- Do you know if the cheap outlet strips work? I’m not sure if they are a good deal (work as good as more expensive strips) or a waste of money.
- Do UPS provide better surge protection, or are you just paying more for the battery backup?
- Do you know of any studies that show how well different devices work?


The best source of information on this is Dan of the eponymously named [Dan’s Data](http://www.dansdata.com/). Let’s start with his essential article on [power conditioning](http://www.dansdata.com/sbs9.htm):


> Mains irregularities come in four flavors – surges, sags, spikes and outages.
> A **surge** is a lengthy (2.5 second or longer) increase in the supply voltage. A **sag** is a similarly lengthy decrease. By and large, computer power supplies deal with both of these quite well, though it of course depends on the severity of the irregularity, not to mention the quality of the power supply, and how much of its capacity is being used by the computer. The closer to maximum capacity a power supply is, the less likely it is to handle a given surge or sag. For this reason, a computer with a 300 watt (W) Power Supply Unit (PSU) is likely to deal better with line irregularities than one with a 235W PSU, although it may not ever need more than 200W of the PSU’s possible output.
> **Outages** are plain old blackouts, which are the Russian roulette of computing – you’ll probably get away with no damage or only minor system corruption if the power drops out, but if you’re writing to the only copy of an important file at the magic moment, you can kiss it goodbye.
> **Spikes** are the real nasties. A spike is a brief increase in the supply voltage – less than 2.5 seconds, often a lot less. For a fraction of a second, a spike can easily subject your equipment to several hundred volts. If this doesn’t blow something up outright, it can progressively damage power supply and other components. So, after a few (or a few hundred) more spikes and surges, your PC dies, for no obvious reason. You may lose a power supply or modem; you may lose your motherboard; you may even lose your hard drive and everything on it.
> If lightning directly strikes the power lines near your house, you will have a very exciting time and probably lose some gear, unless everything is unplugged. Fortunately, direct strikes to power lines are rare, because, by definition, a power line is well isolated from earth, and the lightning is looking for an earth. Buried power and telephone lines are a different story, though; lightning strikes a long way away can result in large induced spikes on these sorts of cables.


Dan goes on to describe the risks of garden variety cheap, generic surge protectors:


![](https://blog.codinghorror.com/content/images/2025/05/image-332.png)


> The plain surge/spike filter powerboards you can buy at various electronics, electrical and hardware stores are, arguably, worse than nothing. This is because they give you the impression you’re protected, when you probably aren’t - well, not for long, anyway.
> The chief surge-clamping component in a basic filter-board is a **Metal-Oxide Varistor (MOV)**.
> MOVs pass current only when the voltage across them is above a set value, and they react very quickly (in a matter of microseconds, against the tens of milliseconds a circuit breaker takes). That’s the good news. The bad news is that MOVs wear out - they’re only good for a few uses, and the bigger the spike, the more damage is done.
> Cheap power filters seldom give you any indication whether your MOV is alive or not. If the powerboard has an illuminated power switch, the switch light often goes off when the MOV has died. The switch lights generally last for decades, so no light almost definitely means no MOV - but since the light only shows the status of a fuse, and the fuse won’t blow if the MOV has been killed by lots of smaller surges, the light can keep glowing merrily when the MOV has long since kicked the bucket.


The key thing to take away from this article is that **surge protectors wear out**. They aren’t good forever.


Personally, I recommend the [Tripp Lite ISOBAR Ultra](http://www.amazon.com/dp/B0000513US) series of surge protectors. And yes, it has to be the Ultra, because of the little green **“protection present” LED** the Ultra adds. It lets you know that the MOV inside your power strip is still functioning.


![](https://blog.codinghorror.com/content/images/2025/05/image-333.png)


The 6-outlet ISOBAR ultra is about $50 online, so they skew to the expensive side of the surge protection spectrum. But at least you won’t get a false sense of security from a cheap power strip with a MOV that blew out three years ago. The [howstuffworks article on surge protectors](http://computer.howstuffworks.com/surge-protector7.htm) mentions that you should look for power strips with a **UL 1449 certification**, but I think it’s more important to look for one with that “protection present” LED.


If you’re really serious about protecting that bit of equipment, you won’t bother with a surge protector. A surge protector can only protect you from spikes and surges, after all. What about sags and outages? **To get full protection from the entire gamut of power problems, you need an Uninterruptible Power Supply.**


And that’s why, although I own and use many Tripp Lite Ultra power strips, **all my home PCs are plugged into UPSes**.


![](https://blog.codinghorror.com/content/images/2025/05/image-334.png)


I don’t have enough experience to recommend a specific *brand* of UPS, other than a [general trust of Tripp Lite](http://www.amazon.com/gp/search?ie=UTF8&keywords=tripp%20lite%20ups&tag), but this excellent [Computer Power User article](https://web.archive.org/web/20060715060642/http://www.computerpoweruser.com/editorial/article.asp?article=articles/archive/c0305/07c05/07c05.asp) (may be behind paywall after first visit) has a few general recommendations for us:

- **Pick a UPS with USB support.** Once the UPS is plugged into your PC’s USB port, it’ll enable those built-in Windows OS power functions you usually see on laptop computers, related to batteries and battery life. It also enables your computer to do a controlled shutdown when power runs out, exactly like a laptop. Note that you do *not* need to install the software that comes with the device to achieve this basic level of functionality!
- **Think about battery runtime.** You’ll want to scale the size of the battery to how much runtime you need, and the power draw of what you’re plugging into it. For a typical 2003 vintage desktop PC, ~800VA watts provided at least 10 minutes of runtime under fully-loaded conditions. That should be more than enough for a brief power outage.
- **Is it a UPS or a SPS?** If the device is a true UPS, the inverter is running all the time, translating the wall power into clean output. If it’s a SPS (standby power supply), the inverter only kicks in when the power is actually out or unstable; at all other times, it’s passing the “OK” power signal directly through, as-is. If you get a true UPS, look for “sine wave output.” This is the ideal, pure form of power; cheaper devices use “square wave” or “modified square wave” which are harsher on sensitive equipment over time. On a SPS, it doesn’t matter so much since the inverter will only be running when the power is actually out.
- **Consider form factor and weight.** The more battery power you have, the larger and heavier the unit will be. I have a 1200VA unit at home I inherited through a garage sale, and I can barely lift the thing. Given the choice, I’d opt for something with less power/runtime that is easier to move and less bulky. My home theater PC, for example, is on a modest UPS that’s more analogous to [a giant power strip](http://www.amazon.com/dp/B000B8MFI6).


Once you hook your device up to a true UPS, you’ve basically removed it from the power grid and hooked it into a custom electricity provider. The only use the UPS has for wall power is to charge its batteries. And be sure *not* to plug your UPS into any surge protection strip! Plug it directly into the wall. I’ve seen some truly bizarre PC behavior resulting from daisy-chaining UPSes or surge protection strips.


So, in summary: **if it’s something you *really* care about, put it on a decent UPS. If it’s something you want to protect, put it behind a decent surge protector with a “protection OK” indicator**.

[power conditioning](https://blog.codinghorror.com/tag/power-conditioning/)
[surge protection](https://blog.codinghorror.com/tag/surge-protection/)
[ups](https://blog.codinghorror.com/tag/ups/)
[power supply](https://blog.codinghorror.com/tag/power-supply/)
[voltage fluctuations](https://blog.codinghorror.com/tag/voltage-fluctuations/)
