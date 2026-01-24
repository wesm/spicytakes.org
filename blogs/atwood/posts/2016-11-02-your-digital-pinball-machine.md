---
title: "Your Digital Pinball Machine"
date: 2016-11-02
url: https://blog.codinghorror.com/your-digital-pinball-machine/
slug: your-digital-pinball-machine
word_count: 1615
---

I’ve had something of an [obsession with digital pinball](https://blog.codinghorror.com/pc-pinball-sims/) for years now. That recently culminated in me buying a [Virtuapin Mini](http://virtuapin.net/index.php?main_page=product_info&products_id=92).


![](https://blog.codinghorror.com/content/images/2025/02/image-175.png)


OK, yes, it’s an extravagance. There’s no question. But in my defense, it is a minor extravagance relative to a real pinball machine.


![](https://blog.codinghorror.com/content/images/2025/02/image-176.png)


The mini is much smaller than a normal pinball machine, so it’s easier to move around, takes up less space, and is less expensive. Plus **you can emulate every pinball machine, ever!** The Virtuapin Mini is a custom $3k build centered around three screens:

- 27″ main playfield (HDMI)
- 23″ backglass (DVI)
- 8″ digital matrix (USB LCD)


Most of the magic is in those screens, and whether the pinball sim in question allows you to arrange the three screens in its advanced settings, usually by enabling a “cabinet” mode.


![](https://blog.codinghorror.com/content/images/2025/02/image-177.png)


Let me give you an internal tour. Open the front coin door and detach the two internal nuts for the front bolts, which are finger tight. Then remove the metal lockdown bar and slide the tempered glass out.


![](https://blog.codinghorror.com/content/images/2025/02/image-178.png)


The most uniquely pinball item in the case is right at the front. This [Digital Plunger Kit](http://virtuapin.net/index.php?main_page=product_info&cPath=8&products_id=105) connects the 8 buttons (2 on each side, 3 on the front, 1 on the bottom) and includes an **analog tilt sensor** and **analog plunger sensor**. All of which shows up as a standard game controller in Windows.


![](https://blog.codinghorror.com/content/images/2025/02/image-179.png)


On the left front side, the audio amplifier and left buttons.


![](https://blog.codinghorror.com/content/images/2025/02/image-180.png)


On the right front side, the digital plunger and right buttons.


![](https://blog.codinghorror.com/content/images/2025/02/image-181.png)


The 27″ playfield monitor is mounted using a clever rod assembly to the standard VESA mount on the back, so we can easily rotate it up to work on the inside as needed.


![](https://blog.codinghorror.com/content/images/2025/02/image-182.png)


To remove the playfield, disconnect the power cord and the HDMI connector. Then lift it up and out, and you now have complete access to the interior.


![](https://blog.codinghorror.com/content/images/2025/02/image-183.png)


Notice the large down-firing subwoofer mounted in the middle of the body, as well as the ventilation holes. The PC “case” is just a back panel, and the power strip is the [Smart Strip](https://www.amazon.com/dp/B000P1QJXQ/) kind where it auto-powers everything based on the PC being powered on or off. The actual power switch is on the bottom front right of the case.


![](https://blog.codinghorror.com/content/images/2025/02/image-184.png)


![](https://blog.codinghorror.com/content/images/2025/02/image-185.png)


Powering it up and getting all three screens configured in the pinball sim of your choice results in… *magic*.


It is a **thoroughly professional build**, as you’d expect from a company that has been building these pinball rigs for the last decade. It uses real wood (not MDF), tempered glass, and authentic metal pinball parts throughout.


I was truly impressed by the build quality of this machine. Paul of Virtuapin said they’re on roughly version four of the machine and it shows. It’s over 100 pounds fully assembled and arrives on a shipping pallet. I can only imagine how heavy the full size version would be!


That said, I do have some tweaks I recommend:

- **Make *absolutely sure* you get **[**an IPS panel**](https://blog.codinghorror.com/the-ips-lcd-revolution/)** as your 27″ playfield monitor**. As arrived, mine had a TN panel and while it was playable if you stood directly in front of the machine, playfield visibility was pretty dire outside that narrow range. I dropped in the [BenQ GW2765HT](https://www.amazon.com/dp/B00KYCSRSG/) to replace the GL2760H that was in there, and I was golden. If you plan to order, I would definitely talk to Paul at VirtuaPin and specify that you want this IPS display even if it costs a little more. The 23″ backglass monitor is also TN but the viewing angles are reasonable-ish in that orientation and the backglass is mostly for decoration anyway.
- The improved display has a 1440p resolution compared to the 1080p originally shipped, so you might want to upgrade from the GeForce 750 Ti video card to the [just-released 1050 Ti](https://www.amazon.com/dp/B01MF7EQJZ/). This is not strictly required, as I found the 750 Ti an excellent performer even at the higher resolution, but I plan to play only fully 3D pinball sims and the 1050 Ti gets [excellent reviews](http://www.pcworld.com/article/3134528/components-graphics/nvidia-geforce-gtx-1050-and-gtx-1050-ti-review-the-new-budget-gaming-champions.html) for $140, so I went for it.
- Internally everything is exceptionally well laid out, the only very minor improvement I’d recommend is connecting the rear exhaust fan to the motherboard header so its fan speed can be dynamically controlled by the computer rather than being at full power all the time.
- On the Virtuapin website order form, the PC they provide sounds quite outdated, but don’t sweat it: I picked the lowest options thinking I would have to replace it all, and they shipped me a Haswell based quad-core PC with 8GB RAM and a 256GB SSD, even though those options weren’t even on the order form.


I realize $3k (plus palletized shipping) is a lot of money, but I estimate it would cost you at *least* $1500 in parts to build this machine, plus a month of personal labor. Provided you get the IPS playfield monitor, this is a solidly constructed “real” pinball machine, and if you’re into digital pinball like I am, it’s an absolute *joy* to play and a good deal for what you actually get. As Ferris Bueller once said:


If you’d like to experiment with this and don’t have three grand burning a hole in your pocket, 90% of digital pinball simulation is **a widescreen display in portrait mode**. Rotate one of your monitors, add another monitor if you’re feeling extra fancy, and give it a go.


![](https://blog.codinghorror.com/content/images/2025/02/image-186.png)


As for software, most people talk about [Visual Pinball](https://en.wikipedia.org/wiki/Visual_Pinball) for these machines, and it works. But the combination of janky hacked-together 2D bitmap technology used in the gameplay, and the fact that all those designs are rip-offs that pay nothing in licensing back to the original pinball manufacturers really bothers me.


I prefer [Pinball Arcade](http://store.steampowered.com/app/238260/) in DirectX 11 mode, which is [downright beautiful](https://imgur.com/a/vPQvh), easily (and legally!) obtainable via Steam and offers a stable of 60+ incredible officially licensed classic pinball tables to choose from, all meticulously recreated in high resolution 3D with excellent physics.


![](https://blog.codinghorror.com/content/images/2025/02/image-187.png)


As for getting pinball simulations running on your three monitor setup, if you’re lucky the game will have a **cabinet mode** you can turn on. Unfortunately, this can be weird due to… licensing issues. Apparently building a pinball sim on the computer requires entirely different licensing than placing it inside a full-blown pinball cabinet.


**Pinball Arcade** has a nifty camera hack someone built that lets you position three cameras as needed to get the three displays. You will also need the excellent [x360ce program](http://www.x360ce.com/) to dynamically map joystick events and buttons to a simulated Xbox 360 controller.


[**Pinball FX2**](http://store.steampowered.com/app/226980/) added a cabinet mode about a year ago, but turning it on requires a special code and you have to send them a picture of your cabinet (!) to get that code. I did, and the cabinet mode works great; just enter your code, specify the coordinates of each screen in the settings and you are good to go. While these tables definitely have arcadey physics, I find them great fun and there are a ton to choose from.


![](https://blog.codinghorror.com/content/images/2025/02/image-188.png)


[**Pro Pinball Timeshock Ultra**](http://store.steampowered.com/app/287900/) is unique because it’s originally from 1997 and was one of the first “simulation” level pinball games. The current rebooted version is still pre-rendered graphics rather than 3D, but the client downloads the necessary gigabytes of pre-rendered content at your exact screen resolution and it looks amazing.


![](https://blog.codinghorror.com/content/images/2025/02/image-189.png)


Timeshock has explicit cabinet support in the settings and via command line tweaks. Also, in cabinet mode, when choosing table view, you want the bottom left one. Trust me on this! It supports maximum height for portrait cabinet mode.


![](https://blog.codinghorror.com/content/images/2025/02/image-190.png)


Position each window as necessary, then enable fullscreen for each one and it’ll snap to the monitor you placed it on. It’s “only” one table, but arguably the most classic of all pinball sims. I sincerely hope they continue to reboot the rest of the Pro Pinball series, including Big Race USA which is my favorite.


I’ve always loved pinball machines, even though they struggled to keep up with digital arcade games. In some ways I view my current project, [Discourse](https://discourse.org/), as a similarly analog experience attempting to bridge the gap to the modern digital world:


> The fantastic 60 minute documentary [Tilt: The Battle to Save Pinball](http://www.tilt-movie.com/) has so many parallels with what we’re trying to do for forum software.


> Pinball is threatened by Video Games, in the same way that Forums are threatened by Facebook and Twitter and Tumblr and Snapchat. They’re considered old and archaic technology. They’ve stopped being sexy and interesting relative to what else is available.
> Pinball was forced to reinvent itself several times throughout the years, from mechanical, to solid state, to computerized. And the defining characteristic of each “era” of pinball is that the new tables, once you played them, made all the previous pinball games seem immediately obsolete because of all the new technology.
> The [Pinball 2000](https://en.wikipedia.org/wiki/Pinball_2000) project was an attempt to invent the next generation of pinball machines:
> “It wasn’t a new feature, a new hardware set, it was everything new. We have to get everything right. We thought that we had reinvented the wheel. And in many respects, we had.”
> This is exactly what we want to do with Discourse – build a forum experience so advanced that playing will make all previous forum software seem immediately obsolete.
> Discourse aims to save forums and make them relevant and useful to a whole new generation.


So if I seem a little more nostalgic than most about pinball, perhaps a little *too* nostalgic at times, [maybe that’s why](https://blog.codinghorror.com/the-only-truly-failed-project/).

[pinball](https://blog.codinghorror.com/tag/pinball/)
[digital pinball](https://blog.codinghorror.com/tag/digital-pinball/)
