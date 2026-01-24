---
title: "Building Tiny, Ultra Low Power PCs"
date: 2008-07-22
url: https://blog.codinghorror.com/building-tiny-ultra-low-power-pcs/
slug: building-tiny-ultra-low-power-pcs
word_count: 658
---

In previous posts, I’ve talked about [building your own desktop PC](https://blog.codinghorror.com/building-a-pc-part-i/), and [building your own home theater PC](https://blog.codinghorror.com/building-your-own-home-theater-pc/). I’m still very much in love with that little HTPC I built. Not only does it have a modern dual-core CPU, and fantastic high-definition capable integrated video – it’s an outstanding general purpose media sharing server, too. But the real punchline is that I eventually got that box down to **an insanely low 44 watts at idle**. That’s [in the ballpark](https://blog.codinghorror.com/revisiting-how-much-power-does-my-laptop-really-use/) for a powerful laptop, and far better than your garden variety desktop PC, which will draw [somewhere between](https://blog.codinghorror.com/why-estimate-when-you-can-measure/) 100 to 200 watts of power.


44 watts is impressive, but what if you want to build a PC that uses even less power – radically less?


That’s when you turn to something like AMD’s Geode platform in [the Nano-ITX form factor](https://blog.codinghorror.com/the-impossibly-small-pc-nano-itx/). It uses **five watts of power at idle**. That’s almost *ten times less *than my HTPC build I was so proud of!


![](https://blog.codinghorror.com/content/images/2025/04/image-185.png)


This is the JetWay J8F9 AMD Geode LX800 motherboard. I can’t say “this is actual size” with a straight face without knowing the size and aspect ratio of your monitor, but it’s probably darn close. The actual dimensions are just under five inches on each side. It may not look like much, but consider the specs:

- 500 Mhz [AMD x86 Geode](http://en.wikipedia.org/wiki/Geode_(processor)) LX 800 CPU
- 200 pin SO-DIMM memory slot, 1 GB DDR-400 max
- Two ATA-100 drive connections
- mini-PCI expansion slot
- CompactFlash memory card slot
- onboard audio / VGA / fast ethernet / USB


This thing is, for all intents and purposes, **a complete, standalone x86 PC that fits in the palm of your hand and sips five watts of power**. Well, assuming you have an enormous hand.


You will need memory and a storage device, of course. You could pick up a laptop hard drive, but another clever thing about this board is that it allows you to use a cheap CompactFlash card as your storage medium – for the optimal low power, no moving parts install.

1. AMD Geode LX 800 Nano ITX Motherboard/CPU Combo $154
2. 512MB 200-pin SO-DIMM DDR-400 $20
3. 4GB compact flash card $14
4. [12vdc AC/DC external wall wart](https://web.archive.org/web/20080727113650/http://www.trcelectronics.com/Phihong/psa-15r-120p.shtml) $18


So we can put together our own tiny utility PC for right at 200 bucks. Not bad. Unbox it, snap in the memory and CF card, plug in the wall wart, and you’re ready to install and boot your operating system of choice. It’s that simple.


Naturally, **you won’t get barn-burning performance**, but if you remember the Pentium II 300 Mhz systems of yesteryear, you’ll know what to expect. You may recall those now-ancient boxes were still able to do some pretty amazing things in their day. I would not build an ultra-lower power PC assuming it will be tolerable for day-to-day web browsing and email reading, unless you’re comfortable using text mode or command-line interfaces exclusively.


This must be a market segment JetWay specializes in; they have a surprisingly large number of Mini-ITX motherboards to choose from. I don’t think you’ll find anything more power-efficient than the Geode LX 800 model, though, but there are some lesser expensive choices that get close. Lots of variety!


If the 5" x 5" profile of the Nano-ITX is far too large for your tastes, how do you [feel about Pico-ITX?](http://www.mini-itx.com/reviews/pico-itx/default.asp?page=4) It’s even smaller at 10cm x 7.2cm.


![](https://blog.codinghorror.com/content/images/2025/04/image-184.png)


I’ve been following the ultra low power, tiny form factor PC segment for quite a few years now. With the emergence of [Intel’s Atom](http://en.wikipedia.org/wiki/Silverthorne_(CPU)) and “[netbooks](http://en.wikipedia.org/wiki/Netbook)” like the ASUS Eee, it’s a segment that is dangerously close to becoming mainstream. If you’re interested, [mini-itx.com](http://www.mini-itx.com/) is still one of the best sources of hands-on reviews, information, and community projects. It’s fun stuff.


What could *you* do with a tiny, highly efficient x86 PC that boots up in under a minute?

[hardware](https://blog.codinghorror.com/tag/hardware/)
[low power consumption](https://blog.codinghorror.com/tag/low-power-consumption/)
[mini pcs](https://blog.codinghorror.com/tag/mini-pcs/)
[amd geode](https://blog.codinghorror.com/tag/amd-geode/)
[nano-itx](https://blog.codinghorror.com/tag/nano-itx/)
