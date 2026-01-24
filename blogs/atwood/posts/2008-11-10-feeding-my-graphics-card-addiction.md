---
title: "Feeding My Graphics Card Addiction"
date: 2008-11-10
url: https://blog.codinghorror.com/feeding-my-graphics-card-addiction/
slug: feeding-my-graphics-card-addiction
word_count: 1736
---

Hello, my name is Jeff Atwood, and I’m an addict.


**I’m addicted... to video cards.**


In fact, I’ve been addicted since 1996. Well, maybe a few years earlier than that if you count some of the classic 2D accelerators. But the true fascination didn’t start until 1996, when the first consumer hardware 3D accelerators came to market. I followed their development avidly in newsgroups, and tried desperately to be the first kid on my block to own the first one. And boy did I ever succeed. Here’s a partial list of what I remember owning in those early days:

- Rendition Verite V1000
- 3dfx Voodoo
- 3dfx Voodoo 2
- ATI Rage Pro
- NVIDIA Riva 128
- Matrox G400
- NVIDIA Riva TNT
- NVIDIA GeForce 256


(This is only a partial list, ranging from about 1996 to 2001 – I don’t want to bore you. And believe me, I could. I mean more than I already am.)


These were heady times indeed for 3D graphics enthusiasts (read: PC gamers). I distinctly remember playing **the first DOS-based Tomb Raider on my 3dfx Voodoo** using the proprietary [GLIDE API](http://en.wikipedia.org/wiki/Glide_API). Sure, it’s pathetic by today’s standards, but the leap from software 3D to fast hardware 3D was quite dramatic from the trenches – and far more graphically powerful than any console available.


This was a time when you could post a thread on a usenet newsgroup about a brand new 3D card, and one of the creators of the hardware would respond to you, as [Gary Tarolli did to me](http://groups.google.com/group/comp.sys.ibm.pc.hardware.video/browse_thread/thread/e5e1b52b75dc4921?hl=en&ie=UTF-8):


> I first want to say how rewarding it is to read all your reviews after having worked on the design of Voodoo Graphics (the chipset on the Orchid Righteous 3D board) for over two years. **I am one of the founders of 3Dfx** and one of our goals was to deliver the highest quality graphics possible to the PC gamer. It was and still is a very risky proposition because of the cost sensitivity of the marketplace. But your reviews help convince me that we did the right thing.
> I thought I would share with you a little bit about what is inside the 3Dfx Voodoo Graphics chipset. There are 2 chips on the graphics board. Each is a custom designed ASIC containing approximately 1 million transistors. Although this number of transistors is on the order of a 486, it is a lot more powerful. Why? Because the logic is dedicated to graphics and there’s a lot of logic to boot. For example, bilinear filtering of texture maps requires reading four 16-bit texels per pixel (that’s 400 Mbytes/sec at 50 Mpixels/sec) and then computing the equation `red_result =r0*w0+r1*w1+r2*w2+r3*w3` where `r0:3` are the four red values and `w0:3` are the four weights based on the where the pixel center lies with respect to the four texels. This is performed for each color channel (red, green, blue, alpha) resulting in 16 multiples and 12 additions or 28 operations per pixel. At 50 Mpixels per second that is 1,400 Mops/sec. The way this is designed in hardware is you literally place 16 multipliers and 12 adders on the chip and hook them together. And this is only a small part of one chip. There are literally dozens of multipliers and dozens of adders on each of the two chips dedicated only to graphics. Each chip performs around 4,000 million actual operations per second, of which around one third are integer multiplies. These are real operations performed – if you were to try to do these on a CPU (or a DSP) you must also do things like load/store instructions and conditions. In my estimation it would take about a 10,000 Mip computer (peak) to do the same thing that one of our chips does. This is about 20 of the fastest P5-200 or P6-200 chips per one of our chips. Not exactly cost-effective. **So if you want to brag, you can say your graphics card has approximately the same compute power as 40 P5-200 chips.** Of course, these numbers are more fun than they are meaningful. What is meaningful in graphics is what you see on the screen.
> Now of course, if you were [writing a software renderer](https://blog.codinghorror.com/on-managed-code-performance/) for a game, you wouldn’t attempt to perform the same calculations we perform on our chip on a general purpose CPU. You would take shortcuts, like using 8-bit color with lookup tables for blending, or performing perspective correction every (n) pixels. The image quality will depend on how many shortcuts you take and how clever you are. Voodoo Graphics takes no shortcuts and was designed to give you the highest quality image possible within the constraint of 2 chips. As your reviews have shown, it is evident that you can see the difference in quality and performance.


There’s nothing quite like having a little chat on usenet with the founder of the company who created the 3D accelerator you just bought. Like I said, it was a simpler time.


Just *imagine* something with the power of forty Pentium-200 chips! Well, you don’t have to. There’s probably a CPU more powerful than that in your PC right now. But the relative *scale* of difference in computational power between the CPU and a GPU hasn’t changed – special purpose GPUs really are [that much more powerful](https://blog.codinghorror.com/cpu-vs-gpu/) than general purpose CPUs.


After that first taste of hot, sweet GPU power, I was hooked. Every year since then I’ve made a regular pilgrimage to the temple of the GPU Gods, paying my tithe and bringing home whatever the latest, greatest, state-of-the art in 3D accelerators happens to be. What’s amazing is how often, even now, performance doubles yearly.


This year, I chose the NVIDIA GTX 280. Specifically, the MSI NVIDIA GTX 280 OC, with 1 GB of memory, overclocked out of the box. I hate myself for succumbing to mail-in rebates, but they get me every time – this card was $375 after rebate.


![](https://blog.codinghorror.com/content/images/2025/04/image-225.png)


$375 is expensive, but this is still the fastest single card configuration available at the moment. It’s also one heck of a lot cheaper than the comically expensive $650 MSRP these cards were introduced at in June. Pity the poor rubes who bought these cards at launch! Hey, wait a second – I’ve been one of those rubes for 10 years now. Never mind.


This is the perfect time to buy a new video card – before Thanksgiving and running up to Christmas is prime game release season. All the biggest games hit right about now. Courtesy of my new video card and the [outstanding Fallout 3](https://www.amazon.com/s?k=fallout+3), my productivity last week hit an all-time low. But oh, was it ever worth it. I’m a long time Fallout fan, even to the point that our wedding pre-invites had secret geek Fallout art on them. Yes, that was approved by my wife, because *she is awesome*.


I must say that experiencing the wasteland at 60 frames per second, 1920 x 1200, in [high dynamic range lighting](https://blog.codinghorror.com/high-dynamic-range-lighting/), with every single bit of eye candy set to maximum, was *so* worth it. I dreamt of the wastelands.


![](https://blog.codinghorror.com/content/images/2025/04/image-224.png)


In fact, even after reaching the end of the game, I’m still dreaming of them. I’ve heard some claim Fallout 3 is just Oblivion with guns. To those people, I say this: *you say that like it’s a bad thing*. The game is incredibly true to the Fallout mythos. It’s harsh, gritty, almost oppressive in its presentation of the unforgiving post-apocalyptic wasteland – and yet there’s always an undercurrent of dark humor. There are legitimate good and evil paths to every quest, and an entirely open-ended world to discover.


No need to take my word for it, though. I later found some [hardware benchmark roundups](http://www.techspot.com/article/125-fallout3-performance/page4.html) that confirmed my experience: the GTX 280 is *crazy* fast in Fallout 3.


![](https://blog.codinghorror.com/content/images/2025/04/image-223.png)


Of course, we wouldn’t be responsible PC owners if we didn’t like to mod our hardware a bit. That’s what separates us from those knuckle-dragging Mac users: [skill](https://blog.codinghorror.com/the-diy-pc/). (I kid, I kid!) First, you’ll want to download a copy of the [amazing little GPU-Z application](http://www.techpowerup.com/gpuz/), which will show you in real time what your video card is doing.


A little load testing is always a good idea, particularly since I got a bum card with my first order – it would immediately shoot up to 105 C and throttle within a minute or two of doing anything remotely stressful in 3D. It *worked*, but the resulting stuttering was intolerable, and the fan noise was unpleasant as the card worked overtime to cool itself down. I’m not sure how I would have figured that out without the real time data and graphs that GPU-Z provides. I returned it for a replacement, and the replacement’s behavior is much more sane; compare GPU-Z results at idle (left) and under [RTHDRIBL](http://www.daionet.gr.jp/~masa/rthdribl/) load (right):

kg-card-begin: html


|  |  |


kg-card-end: html

Fortunately, there’s not much we need to do to improve things. The Nvidia 8800 and GTX series are equipped with outstanding integrated coolers which directly exhaust the GPU heat from the back of the PC. I’d much rather these high powered GPUs exhaust their heat outward instead of blowing it around inside the PC, so this is the preferred configuration out of the box. However, the default exhaust grille is *incredibly* restrictive. I cut half of the rear plate away with a Dremel, which **immediately reduced fan speeds 20% (and thus, noise 20%)** due to the improvement in airflow.


![](https://blog.codinghorror.com/content/images/2025/04/image-222.png)


Just whip out your trusty Dremel (you *do* own a Dremel, right?) and cut along the red line. It’s easy. If you’re a completionist, you can apply better thermal paste to the rest of the card to eke out a few more points of efficiency with the cooler.


Extreme? Maybe. But I like my [PCs powerful and quiet](https://blog.codinghorror.com/building-a-quiet-pc/). That’s another thing that attracted me to the GTX 280 – for a top of the line video card, it’s [amazingly efficient at idle](https://web.archive.org/web/20090109072444/http://techreport.com/articles.x/14934/16). And despite my gaming proclivities, it will be idle 98% of the time.


![](https://blog.codinghorror.com/content/images/2025/04/image-221.png)


I do love this new video card, but I say that every year. I try not to grow too attached. I’m sure this video card will be replaced in a year with something even better.


What else would you expect from an addict?

[graphics cards](https://blog.codinghorror.com/tag/graphics-cards/)
[video cards](https://blog.codinghorror.com/tag/video-cards/)
[3d accelerators](https://blog.codinghorror.com/tag/3d-accelerators/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
