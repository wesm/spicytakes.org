---
title: "Building a PC, Part IX: Downsizing"
date: 2020-04-19
url: https://blog.codinghorror.com/building-a-pc-part-ix-downsizing/
slug: building-a-pc-part-ix-downsizing
word_count: 982
---

Hard to believe that I’ve had the same PC case since 2011, and my last serious upgrade was in 2015. I guess that’s yet another sign that [the PC is over](https://blog.codinghorror.com/the-pc-is-over/), because PC upgrades have gotten *really boring*. It took 5 years for me to muster up the initiative to get my system fully upgraded! 🥱


I’ve been slogging away at this for quite some time now. My PC build blog entry series spans 13 glorious years:

- [Building a PC, Part VIII: Iterating](https://blog.codinghorror.com/building-a-pc-part-viii-iterating/) (2015)
- [Building a PC, Part VII: Rebooting](https://blog.codinghorror.com/building-a-pc-part-vii-rebooting/) (2011)
- [Building a PC, Part VI: Rebuilding](https://blog.codinghorror.com/building-a-pc-part-vi-rebuilding/) (2009)
- [Building a PC, Part V: Upgrading](https://blog.codinghorror.com/building-a-pc-part-v-upgrading/) (2008)
- [Building a PC, Part IV: Now It’s Your Turn](https://blog.codinghorror.com/building-a-pc-part-iv-now-its-your-turn/) (2007)
- [Building a PC, Part III: Overclocking](https://blog.codinghorror.com/building-a-pc-part-iii-overclocking/) (2007)
- [Building a PC, Part II: Burn in](https://blog.codinghorror.com/building-a-pc-part-ii/) (2007)
- [Building a PC, Part I: Minimal boot](https://blog.codinghorror.com/building-a-pc-part-i/) (2007)


The future of PCs may not necessarily be **more speed** (though there is some of that, if you read on), but in **smaller builds**. For this iteration, my go-to cases are the [Dan A4 SFX](https://www.dan-cases.com/dana4.php)...


![](https://blog.codinghorror.com/content/images/2025/02/image-156.png)


![](https://blog.codinghorror.com/content/images/2025/02/image-157.png)


And the Streacom DA2...


![](https://blog.codinghorror.com/content/images/2025/02/image-158.png)


![](https://blog.codinghorror.com/content/images/2025/02/image-159.png)


The attraction here is **maximum power in minimum size**. Note that each of these cases are *just *large enough to fit...

- a standard mini-ITX system
- SFX power supply
- full sized GPU
- reasonable CPU cooler


...though the DA2 offers substantially more room for cooling the CPU and adding fans.


![](https://blog.codinghorror.com/content/images/2025/02/image-261.png)


I’m not sure you can physically build a smaller standard mini-ITX system than the DAN A4 SFX, at least not without custom parts!


> DAN A4-SFX
> 200mm × 115mm × 317mm = 7.3 liters
> Silverstone RVZ02 / ML08
> 380mm × 87mm × 370mm = 12.2 liters
> [nCase M1](https://ncases.com/products/m1)
> 240mm × 160mm × 328 mm = 12.6 liters
> Streacom DA2
> 180mm × 286mm × 340mm = 17.5 liters


(For comparison with [The Golden Age of x86 Gaming](https://blog.codinghorror.com/the-golden-age-of-x86-gaming/) consoles, a PS4 Pro occupies 5.3 liters and an Xbox One S 4.3 liters. About 50% more volume for considerably more than 2× the power isn’t a bad deal!)


I chose the Streacom DA2 as my personal build, because after experimenting heavily with the DAN A4 SFX, I realized you need more room to deal with extremely powerful CPUs and GPUs in this form factor, and I wanted a truly powerful system:

- Intel [i9-9900KS](https://www.intel.com/content/www/us/en/products/processors/core/i9-processors/i9-9900ks.html) (8 core, 16 thread, 5.0 GHz) CPU
- Samsung 970 PRO 1TB / Samsung 970 EVO 2TB / Samsung 860 QVO 4TB SATA
- 64GB DDR4-3000
- [Cryorig H7](http://www.cryorig.com/h7.php) cooler (exact fit)
- NVIDIA GeForce RTX 2080 Ti GPU


Compared to my old 2015-2017 system, a slightly overclocked i7-7700k, that at least gives me 2× the cores (and faster cores, both in clock rate and IPC), 2× the memory, and 2× the M.2 slots (two versus one).


![](https://blog.codinghorror.com/content/images/2025/02/image-161.png)


The DA2 is a clever case though less perfect than the A4-SFX. What’s neat about it is the hybrid open-air design (on the top and bottom) plus the versatile horizontal and vertical bracket system interior. Per the manual (PDF):


![](https://blog.codinghorror.com/content/images/2025/02/image-162.png)


Check out all the bracket mounting options. Incredibly versatile, and easy to manipulate with the captured nut and bolt design:


![](https://blog.codinghorror.com/content/images/2025/02/image-163.png)


Note that you can (and really *should*) pop out the top and bottom acrylic pieces with the mesh dust net.


![](https://blog.codinghorror.com/content/images/2025/02/image-164.png)


I had **dramatically better temperatures** after I did this, and it also made the build easier since the case can fully “breathe” through the top and bottom. You’ll note that the front of the DA2 is totally solid, no air holes, so you do need that extra airflow.


I only have a few criticisms of this Streacom DA2 case:

- The side panels are tool free, which is excellent, but the pressure fit makes them fairly difficult to remove. Feels like this could be tweaked?
- (Don’t even think about using a full sized ATX power supply. In theory it is supported, but the build becomes so much more difficult. Use a SFX power supply, which you’d expect to do for a mini-ITX build anyway.)
- My primary complaint is that the **power extension cable gets in the way**. I had to remove it and re-attach it during my build. They should custom route the power cable upwards so it blocks less stuff.
- Less of a criticism and more of an observation: if your build uses a powerful GPU and CPU, you’ll need two case fans. There’s mounting points for a 92mm fan in the rear, and the bracket system makes it easy to mount a 140mm fan blowing inward. You will definitely need both fans!


Here’s the configuration I recommend, open on both the top and bottom for maximum airflow, with three fans total:


![](https://blog.codinghorror.com/content/images/2025/02/image-165.png)


If you are a water cooling kind of person – I am definitely not, I experienced one too many traumatic cooling fluid leaks in the early 2000s – then you will use that 140mm space for the radiator.


I have definitely [burn-in tested](https://blog.codinghorror.com/is-your-computer-stable/) this machine, as I do all systems I build, and it passed with flying colors. But to be honest, if you expect to be under full CPU and GPU loads for extended periods of time you *might* need to switch to water cooling due to the space constraints. (Or pick slightly less powerful components.)


If you haven’t built a PC system recently, it’s easier than it has ever been. Heck by the time you install the M.2 drives, memory, CPU, and cooler on the motherboard you’re almost done, these days!


![](https://blog.codinghorror.com/content/images/2025/02/image-166.png)


There are a lot of interesting [compact mini-itx builds](https://yuel-beast-designs.myshopify.com/products/motif-monument) out there. Perhaps that’s the primary innovation in PC building for 2020 and beyond – **packing all that power into less than 20 liters of space! **


Read a [Spanish translation of this article](https://www.ibidemgroup.com/edu/traduccion-como-construir-minipc/) here.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[pc building](https://blog.codinghorror.com/tag/pc-building/)
[system upgrades](https://blog.codinghorror.com/tag/system-upgrades/)
[pc cases](https://blog.codinghorror.com/tag/pc-cases/)
