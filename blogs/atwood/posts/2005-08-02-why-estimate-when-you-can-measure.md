---
title: "Why Estimate When You Can Measure?"
date: 2005-08-02
url: https://blog.codinghorror.com/why-estimate-when-you-can-measure/
slug: why-estimate-when-you-can-measure
word_count: 580
---

> Wanna lower the noise of your computer? **Stop burning 450 WATTS of power to browse the web or send email.**
> Don’t see any moving parts on your Game Boy do you? Or your PDA for that matter. If desktop computers were made of APPROPRIATE parts instead of the “my computer has to be faster than yours” parts we’d have silent desktops that run in under 20 Watts of power that cost 150$ and run whatever OS you choose.
> Anything short of this and you’re doing to noise what we do to heat, moving the problem elsewhere. You could [for example] pump ice cold water over the heatsinks and keep the pump outside, in the basement, etc...
> But that’s just moving the problem elsewhere and not really solving it.
> The solution is more scalable computing or appropriate choices. There is no reason, for example, why the P4 idles at 400Mhz and the AMD64 at 1Ghz other than the design can only scale so far. This matters a bit more in laptops where every mW counts.
> – [slashdot poster](http://hardware.slashdot.org/article.pl?sid=05/07/25/1059231)


I don’t really read Slashdot, but someone forwarded this post to me, and I had to laugh. Pointing out the direct relationship between power consumption and noise is accurate enough, but... **450 watts?** I don’t think you can realistically build a desktop computer that uses 450 watts!


![](https://blog.codinghorror.com/content/images/2025/05/image-121.png)


We don’t need [back of the envelope](https://blog.codinghorror.com/gigabit-ethernet-and-back-of-the-envelope-calculations/) estimates to show how ridiculous that figure actually is. We can just measure the power usage with our trusty $30 [Kill-a-watt watt meter](http://www.amazon.com/exec/obidos/ASIN/B00009MDBU).


For my work PC, which currently contains the following items:

- Athlon X2 4800+
- GeForce 6600 video
- Maxtor 300gb SATA HDD
- GeForce 5200 PCI video (for 3rd display)
- 2gb PC3200 DDR RAM
- generic DVD-ROM


The Kill-a-Watt tells me I’m pulling this much power from the wall socket:

kg-card-begin: html


| Idle windows desktop | 118w |
| Defragmenting hard drive | 122w |
| 1 instance of Prime95 | 147w |
| 2 instances of Prime95 (affinity set) | 177w |
| Battlefield 2 demo | 172w |


kg-card-end: html

Now, that’s power draw at the wall socket. About 25 percent of this energy is lost in the power supply as it converts from wall power to something the PC can use. So **the** **actual peak power usage of my work PC is around 132 watts**. And that’s a fairly beefy PC, probably unrepresentative of the vast majority of current desktops.


It’s amazing how much you can infer from such simple, basic data collection:

- Each “core” of the X2 4800+ consumes **30 watts**
- The GeForce 6600 video card consumes **25 watts**
- The 300gb SATA hard drive consumes **4 watts**


We could go a lot farther, but the whole point is that we don’t have to. As estimates go, these are backed by supporting data. And that’s a lot more useful than the unsubstantiated wild guessing of random Slashdot posters.


Even outside Slashdot there are still plenty of people who will swear up and down that you absolutely *must* use a 500+ watt power supply for a new high-end computer. Why spread guesstimated misinformation when you can simply measure the power usage with a widely available $30 device?


Estimating is only necessary when you can’t easily measure. When you meet people like this, gently urge them to **stop estimating and start measuring**.

[scalable computing](https://blog.codinghorror.com/tag/scalable-computing/)
[power consumption](https://blog.codinghorror.com/tag/power-consumption/)
[hardware design](https://blog.codinghorror.com/tag/hardware-design/)
[computer noise](https://blog.codinghorror.com/tag/computer-noise/)
[energy efficiency](https://blog.codinghorror.com/tag/energy-efficiency/)
