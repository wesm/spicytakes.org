---
title: "I Happen to Like Heroic Coding"
date: 2009-04-04
url: https://blog.codinghorror.com/i-happen-to-like-heroic-coding/
slug: i-happen-to-like-heroic-coding
word_count: 1061
---

I’ve been following Michael Abrash for more than 10 years now; he’s one of [my programming heroes](https://blog.codinghorror.com/there-aint-no-such-thing-as-the-fastest-code/). So I was fascinated to discover that Mr. Abrash wrote an article extolling the [virtues of Intel’s upcoming Larrabee](http://www.ddj.com/hpc-high-performance-computing/216402188?pgno=1). What’s Larrabee? It’s a weird little unreleased beast that sits somewhere in the vague no man’s land [between CPU and GPU](http://www.anandtech.com/cpuchipsets/intel/showdoc.aspx?i=3367):


> [Larrabee] is first and foremost NOT a GPU. It’s a CPU. A many-core CPU that is optimized for data-parallel processing. What’s the difference? Well, there is very little fixed function hardware, and the hardware is targeted to run general purpose code as easily as possible. The bottom lines is that Intel can make this very wide many-core CPU look like a GPU by implementing software libraries to handle DirectX and OpenGL.


We know that GPUs generally deliver one or two more orders of magnitude more performance than a general purpose CPUs at the [things they are good at](https://blog.codinghorror.com/cpu-vs-gpu/). That’s what I would expect for dedicated hardware devoted to a specific and highly paralizable task.


Michael Abrash has already attempted what most people said was impossible – to build **a full software 3D renderer that runs modern games at reasonable framerates**. In other words, to make a general purpose CPU compete in a completely unfair fight against a highly specialized GPU. He’s effectively accomplished that, and his company sells it as a product called [Pixomatic](https://web.archive.org/web/20100102132202/http://www.radgametools.com/pixomain.htm):


> In this three-part article, I discuss the process of optimizing Pixomatic, an x86 3D software rasterizer for Windows and Linux written by Mike Sartain and myself. Pixomatic was **perhaps the greatest performance challenge I’ve ever encountered**, certainly right up there with [Quake](http://en.wikipedia.org/wiki/Quake). When we started on Pixomatic, we weren’t even sure we’d be able to get DirectX 6 features and performance, the minimum for a viable rasterizer. I’m pleased to report that we succeeded. On a 3 GHz Pentium 4, Pixomatic can run Unreal Tournament 2004 at 640x480, with bilinear filtering enabled. On slower processors, performance is of course lower, but by rendering at 320x240 and stretching up to 640x480, Unreal Tournament 2004 runs adequately well – even on a 733-MHz Pentium III.


Pixomatic is documented in an excellent [series of Dr. Dobbs articles](http://www.google.com/search?q=Optimizing+Pixomatic+for+x86+Processors). It’s fascinating reading; even though I know zero about assembly language, Michael’s language of choice, he’s a fantastic writer. That old adage about the subject not mattering when you have a great teacher has never been truer.


I remember [trying out Pixomatic](https://blog.codinghorror.com/on-managed-code-performance/) briefly four years ago. Those CPUs he’s talking about seem awfully quaint now, and that made me curious: how fast is the Pixomatic software renderer on *today’s* CPUs? My current box is a **Core 2 Duo (wolfdale) running at 3.8 GHz**. So I downloaded the [Unreal Tournament 2004 demo](http://download.cnet.com/Unreal-Tournament-2004-demo/3000-7441_4-10262824.html) (still fun, by the way!), and followed the brief, easy instructions provided to [enable the Pixomatic software renderer](http://www.radgametools.com/pixo/PixoWithUnreal2004.txt). It’s not complicated:

kg-card-begin: html

```

ut2004.exe -software

```

kg-card-end: html

One word of warning. Be sure you have an appropriate resolution set before doing this! I was playing at 1920x1200 initially, and that’s what the software renderer defaulted to. And here’s the shocker: *it was actually playable!* I couldn’t believe it. It wasn’t great, mind you, but it was hardly a slideshow. I tweaked the resolution down to something I felt was realistic: 1024x768. I turned on framerate display by pressing...

kg-card-begin: html

```

~
stat fps

```

kg-card-end: html

... from within the game. **This Pixomatic software rendered version of the game delivered a solid 40-60 fps experience in capture the flag mode**. It ran so well, in fact, that I decided to bump up the detail – I enabled 32-bit color and bilinear filtering by editing the `ut2004.ini` file:

kg-card-begin: html

```

[PixoDrv.PixoRenderDevice]
FogEnabled=True
Zoom2X=False
SimpleMaterials=True
LimitTextureSize=True
LowQualityTerrain=False
TerrainLOD=10
SkyboxHack=True
FilterQuality3D=3
FilterQualityHUD=1
HighDetailActors=False
SuperHighDetailActors=False
ReduceMouseLag=True
DesiredRefreshRate=0
DetailTexMipBias=0.000000
Use16bitTextures=False
Use16bit=False
UseStencil=False
UseCompressedLightmaps=False
DetailTextures=False
UsePrecaching=True

```

kg-card-end: html

Once I did this, the game looked totally respectable. Eerily reminiscent in visuals and performance to the classic, early Voodoo and Voodoo 2 cards, actually.


![](https://blog.codinghorror.com/content/images/2025/04/image-343.png)


(If you think this looks bad, check out Doom 3 running on [an ancient Voodoo 2 setup](https://web.archive.org/web/20090411230512/http://www.firingsquad.com/media/gallery_index.asp/244). It’s certainly better than that!)


The frame rate took a big hit, **dropping to 30fps**, but I found it was an uncanilly *stable* 30fps. The only Achilles heel of the Pixomatic software renderer is places with lots of alpha blending, such as when you fire a sniper rifle, obscuring the entire screen with a puff of muzzle smoke, or if you're standing near a teleportation portal.


Pretty amazing, right? It is!


## And **utterly pointless**.


My [current video card](https://blog.codinghorror.com/feeding-my-graphics-card-addiction/) renders Unreal Tournament 2004 at the highest possible resolution with every possible quality option set to maximum, at somewhere between **200 and 300 frames per second**. Despite the miraculously efficient assembly Abrash and Sartain created to make this possible *at all*, it’s at best a carnival oddity; even the crappiest onboard laptop 3D (assuming a laptop of recent vintage) could outperform Pixomatic [without even breaking a sweat](http://www.anandtech.com/video/showdoc.aspx?i=2427&p=5).


We know that the game is far more enjoyable to play with a real GPU, on a real video card. And we’re hip deep in real GPUs on every platform; even the iPhone has one. Perhaps Pixomatic made some business sense back in 2003, but it didn’t take a genius analyst back then to see that it would make no business sense at *all* today. At the same time, I can’t help admiring the engineering effort that went into building a viable 3D software renderer, something that seemed virtually *impossible* bordering on foolish.


> In short, it will be possible to get major speedups from [Larrabee] without heroic programming, and that surely is A Good Thing. Of course, nothing’s ever that easy; as with any new technology, only time will tell exactly how well automatic vectorization will work, and at the least it will take time for the tools to come fully up to speed. Regardless, it will equally surely be possible to get even greater speedups by getting your hands dirty with intrinsics and assembly language; besides, **I happen to like heroic coding**.


Ditto.


We’ll have to wait and see if Intel’s efforts to push GPU functionality into their x86 architecture makes any of this heroic coding more relevant in the future. Either way, it remains impressive.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
