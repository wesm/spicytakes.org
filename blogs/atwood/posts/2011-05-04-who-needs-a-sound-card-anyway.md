---
title: "Who Needs a Sound Card, Anyway?"
date: 2011-05-04
url: https://blog.codinghorror.com/who-needs-a-sound-card-anyway/
slug: who-needs-a-sound-card-anyway
word_count: 994
---

The last sound card I purchased was in 2006, and that’s only because I’m (occasionally) a bleeding edge PC gamer. The very same card was still in my current PC until a few days ago. It’s perhaps too generous to describe PC sound hardware as stagnant; it’s borderline *irrelevant*.


**The default, built-in sound chips on most motherboards have evolved from “totally crap” to “surprisingly decent” in the last 5 years.** But besides that, in this era of ubiquitous quad core CPUs nearing 4 GHz, it’d be difficult to make a plausible case that you *need* a discrete set of silicon to handle sound processing, even for the very fanciest of [3D sound algorithms and HRTFs](https://blog.codinghorror.com/3d-positional-audio-and-hrtfs/).


That said, if you enjoy music even a *little*, I still strongly recommend investing in a quality set of headphones. As I wrote in 2005’s [Headphone Snobbery](https://blog.codinghorror.com/headphone-snobbery/):

kg-card-begin: html

> **Am I really advocating spending two hundred dollars on a set of headphones?** *Yes. Yes I am.* Now, you could spend a lot more. This is about extracting the maximum bang for your buck:
> Unlike your computer, or your car, your headphones will never wear out or become obsolete. I hesitate to say lifetime, but they’re multiple decade investments at the very least.
> The number one item that affects the music you hear is the speakers. Without a good set of headphones, everything else is irrelevant.
> The right headphones can deliver sound equivalent to extremely high-end floorstanding speakers worth thousands of dollars.
> If you’re the type of person who is perfectly happy listening to 64 kilobit MP3s through a $5 set of beige headphones, that’s fine. There’s nothing wrong with that. Keep on scrolling; this post is not for you.

kg-card-end: html

I realize that there’s a fine line between audiophile and bats**t insane – *and that line better not be near any sources of interference!* But nice headphones require powerful, reasonably clean output to deliver the best listening experience. This isn’t high end audio crackpot snake oil, it’s actual physics.


I’ll let the guys at headroom [explain](http://www.headphone.com/learning-center/how-do-i-know-if-my-headphones-need-an-amp.php):


> You may have heard of a headphone’s “impedance.” Impedance is the combined resistance and reactivity the headphones present to the amplifier as an electrical load. High impedance cans will usually need more voltage to get up to a solid listening level, so they will often benefit from an amp, especially with portable players that have limited voltage available from their internal batteries. But low impedance cans may require more current, and will lower the damping factor between the amp and headphones. So while low impedance headphones may be driven loud enough from a portable player, the quality of sound may be dramatically improved with an amp.
> The size of your headphone will give you some clues to whether an amp may be warranted. Most earbud and in ear headphones are typically very efficient and are less likely to benefit strongly from an amp. Many larger headphones will benefit, or even require, a headphone amp to reach listenable volume levels with portable players.


Thus, once you have a set of nice headphones, you *do* need some kind of amplified output for them. Something like the [Boostaroo](http://boostaroo.com/), or a [Total BitHead](http://www.amazon.com/exec/obidos/ASIN/B003WXBFS8). And if you’re on a laptop these outboard solutions might be your only options.


![](https://blog.codinghorror.com/content/images/2025/04/image-520.png)


But desktops offer the option of adding a sound card. The good news is that **arguably the best sound card on the planet, the Xonar DG, is all of 30 measly bucks.** It’s a big step up in fundamental sound quality from even the best current integrated HD audio motherboard sound chips, per [this Tech Report review](https://web.archive.org/web/20110902054309/http://techreport.com/articles.x/19997/1).

kg-card-begin: html


|  | [RightMark Audio Analyzer](http://audio.rightmark.org) audio quality, 16-bit/44.1kHz |
|  | freq response | noise level | range | THD | THD + Noise | IMD + Noise | crosstalk | IMD at 10kHz | overall |
| Realtek ALC892 HD | 5 | 4 | 4 | 3 | 1 | 3 | 5 | 3 | 4 |
| Xonar DG | 5 | 6 | 6 | 5 | 4 | 6 | 6 | 6 | 5 |


kg-card-end: html

It also includes a little something extra of particular interest to us music loving programmers with nice headphones:


> **Built-in headphone amplification** is something you won’t find on a motherboard, but it’s featured in both Xonars. On the DG, Asus has gone with Texas Instruments’ DRV601RTJR, which is optimized for headphone impedances of 32-150 Ω according to the card’s spec sheet. The Xense gets something considerably fancier: a TI amp capable of pushing headphones with impedances up to 600 Ω. Of course, the headphones bundled with the card are rated for an impedance of only 150 Ω. Mid-range stereo cans like Sennheiser’s excellent HD 555s, which we use for listening tests, have a rated impedance of just 50 Ω. You don’t need big numbers for high-quality sound.


The headphone amplification options are a bit buried in the Xonar driver user interface. To get there, select headphone mode, then click the little hammer icon to bring up the headphone amp gain settings.


![Xonar-dg-audio-center-headphones](https://blog.codinghorror.com/content/images/uploads/2011/05/6a0120a85dcdae970b0154321f2ec1970c-800wi.png)


After my last upgrade, I was truly hoping I could get away with just the on-board Realtek HD audio my motherboard provides. I resisted mightily – but the drop in headphone output quality with the onboard stuff was noticeable. Not to mention that I had to absolutely *crank* the volume to get even moderate loudness with my fancy-ish Sennheiser HD 600 headphones. The Xonar DG neatly solves both of these problems.


As you probably expected, the answer to the question “Who needs a sound card?” is “Almost nobody.” *Except those of us who invested in quality headphones.* Rather than spending $30 or $150 on an outboard headphone amp, spend $30 on the Xonar DG to get a substantial sound quality upgrade *and* a respectable headphone amp to boot.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[sound card](https://blog.codinghorror.com/tag/sound-card/)
[pc gaming](https://blog.codinghorror.com/tag/pc-gaming/)
[cpu](https://blog.codinghorror.com/tag/cpu/)
[sound chips](https://blog.codinghorror.com/tag/sound-chips/)
