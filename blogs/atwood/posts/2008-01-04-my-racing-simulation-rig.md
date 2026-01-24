---
title: "My Racing Simulation Rig"
date: 2008-01-04
url: https://blog.codinghorror.com/my-racing-simulation-rig/
slug: my-racing-simulation-rig
word_count: 996
---

One advantage of being a geek is that our habits – as such habits go – are not terribly expensive. I’ve written before about [my interest in auto racing](https://blog.codinghorror.com/pc-racing-sims/). Instead of spending $100,000 on a sports car, I’ve **built a nifty racing simulation rig that delivers many of the same thrills at a tiny fraction of the price**. It’s one of my few indulgences, and I’d like to share how I built it with you.


![](https://blog.codinghorror.com/content/images/2025/03/image-414.png)


Here are the ingredients:

kg-card-begin: html


| [Playseats Evolution (black)](http://www.amazon.com/exec/obidos/ASIN/B000K9Q5UK) | $299 |
| Playseats Evolution shifter add-on | $39 |
| [Logitech G25 racing wheel](http://www.amazon.com/exec/obidos/ASIN/B000GP8448) | $229 |
| 50 watt Aura bass shaker x 2 | $80 |
| Generic 100 watt subwoofer amp | $100 |


kg-card-end: html

It’s worth noting that **the Playseat Evolution is designed to mate with the G25 wheels, pedal, and shifter**. The mounting holes match up *perfectly*. That was a pleasant surprise, as I had to do quite a bit of drilling on the older, original Playseat to get things mounted in [the first version of this rig](https://web.archive.org/web/20080302102018/http://blogs.vertigosoftware.com/jatwood/archive/2006/01/13/1861.aspx). With the Evolution and G25 combo, it’s almost plug and play, although you still have to do some drilling to get the shifter add-on mounted properly.


The premium leather-and-metal (well, mostly) G25 kit includes some fairly esoteric features from a major brand vendor like Logitech, notably **a clutch pedal and full shifter kit**.


![](https://blog.codinghorror.com/content/images/2025/03/image-412.png)


![](https://blog.codinghorror.com/content/images/2025/03/image-411.png)


I know $229 may seem like a lot, but it’s actually a *great* deal considering what you’d have to pay for an aftermarket shifter or clutch. You don’t *have* to use these advanced realism features, of course. You can always ignore the clutch pedal, and the shifter can be switched between simple up/down mode and a full 6 speed + reverse layout.


The other item of interest here is the **bass shakers**. I split the PC audio between the PC and the 100 watt subwoofer amplifier, which is strategically mounted under the seat via bungee cords. I also tuck most of the wires under there.


![](https://blog.codinghorror.com/content/images/2025/03/image-410.png)


The amp is dedicated to driving the two 50 watt Aura shakers, which I’ve drilled and mounted on each side of the seat platform. The bottom of the aura has a cork backing, so there’s no metal-to-metal contact.


![](https://blog.codinghorror.com/content/images/2025/03/image-409.png)


The wiring is quite basic, but if you’d like more detail there’s a great walkthrough on [hooking up bass shakers](https://web.archive.org/web/20080516080740/http://home.comcast.net/~davemats/hooking_up_bass_shakers.html) on Dave’s site. The net effect of the bass shakers is pretty wonderful – all the low-end bass is converted to tactile rumbling you feel in the driver’s seat. You’ll instantly know when you hit a rumble strip, and when revving a powerful engine you can  *feel* the roar. Bass shakers are a clever, if decidedly low-tech, way to extend the sophisticated force feedback effects of the wheel to the rest of your body. It’s no [force dynamics simulator](http://youtube.com/results?search_query=force-dynamics), but the bang for the buck is off the charts.


The “brains” behind this simulator is a franken-machine of parts left over from various PC upgrades I’ve made over the last year or so. PCs are so cheap these days, it’s hardly worth listing the hardware specs. Any vaguely modern dual core CPU with 2 GB of memory will do fine. There are only two bits worth worrying about:

- **Video card**. Don’t skimp here. I’d recommend the NVIDIA 8800GT or better, as games tend to be heavily video card dependent these days.
- **Sound card**. Get a discrete sound card with enough outputs to drive a 5.1 surround system. I need three analog outputs to drive the necessary 6 channels on the old Logitech Z-680 surround system I used in this room. A simple stereo plug isn’t enough.


For the display, I opted for an inexpensive projection system.


![](https://blog.codinghorror.com/content/images/2025/03/image-408.png)


I used a typical 4:3 business class projector, mounted on a shelf at the rear top of the room. The screen is the largest that would fit in the space. I’ve also mounted the 5.1 speakers on the wall, as you can see. The two rear speakers are on the opposite wall behind us, and the subwoofer sits in a rear corner.

kg-card-begin: html


| Business class projector (1024x768) | ~$800 |
| 8 foot projector screen | ~$150 |
| [Logitech 5.1 surround speaker system](http://www.amazon.com/exec/obidos/ASIN/B0002WPSBC/codihorr-20) | $220 |


kg-card-end: html

Between the booming sound, the huge eight foot screen, the realistic racing “cockpit,” and the force feedback of the leather-wrapped wheel and rumbling bass shakers, it’s an impressive driving experience.


![](https://blog.codinghorror.com/content/images/2025/03/image-407.png)


I’ve always loved racing simulations, and now I’ve assembled a rig that does them justice. Some of my current favorite racing sims are:

- [Dirt](http://www.amazon.com/exec/obidos/ASIN/B000OPPR72)
- Richard Burns Rally
- [Race 07: The official WTCC Game](http://www.amazon.com/exec/obidos/ASIN/B000U5RRX8)
- [GTR 2](http://www.amazon.com/exec/obidos/ASIN/B000PIK1G0)
- [rFactor](http://www.amazon.com/exec/obidos/ASIN/B000VOSQ0Q)
- [Live for Speed](http://www.lfs.net/)


There’s something about the programmer in me that [delights in the physics playground](https://web.archive.org/web/20080225103918/http://channel9.msdn.com/Showpost.aspx?postid=314874) afforded by these simulations:


> Simulation, by definition, needs to be accurate. Otherwise, well, it’s not simulating reality, really, which is of course the idea of simulation. Games like Forza simulate [the real physics of racing](https://web.archive.org/web/20080222062731/http://phors.locost7.info/contents.htm) in a predictable and mathematically precise manner.
> The past, present and future of computer simulation of real-time physical events, or simply computer-based simulations that involve highly accurate representations of things moving/changing in space and time that are precisely affected by multiple variables like wind, rain, gravity, mud, oil, planets, waves, etc. are fascinating topics for gamers (many may not realize this explicitly, but they sure experience it!), mathematicians, programmers and physicists alike.


I know this racing simulation rig probably barely scratches the surface of what it would *actually* be like to drive a $100k sports car on a race track. It certainly won’t get you as much attention from the opposite sex as a real sports car would. But it’s still a heck of a lot of fun, nonetheless – and it can be built by mere mortals like you and I.

[simulation](https://blog.codinghorror.com/tag/simulation/)
[gaming](https://blog.codinghorror.com/tag/gaming/)
[racing](https://blog.codinghorror.com/tag/racing/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[diy](https://blog.codinghorror.com/tag/diy/)
