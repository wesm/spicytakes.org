---
title: "Physics Based Games"
date: 2008-06-16
url: https://blog.codinghorror.com/physics-based-games/
slug: physics-based-games
word_count: 654
---

I’ve always been fascinated by physics-based gameplay. Even going back to the primeval days of classic arcade gaming, I found vector-based games, with their vastly simplified 2D approximations of physics and motion, more compelling than their raster brethren. I’m thinking of games like [Asteroids](http://en.wikipedia.org/wiki/Asteroids_(computer_game)), [Battlezone](http://en.wikipedia.org/wiki/Battlezone_(1980_video_game)), and [Lunar Lander](http://en.wikipedia.org/wiki/Lunar_Lander_(arcade_game)).


Accurately simulating the physics of the real world has been the domain of supercomputers for decades. The simulation of even “simple” physical phenomena like fire, smoke, and water requires a staggering amount of math. Now that we almost have multicore supercomputers on every desktop, it’s only natural that aspect of computing would trickle down to us.


This topic is particularly relevant in light of today’s introduction of NVIDIA’s newest video card, [the GTX 280](https://web.archive.org/web/20080620012953/http://www.techreport.com/articles.x/14934/2), which contains **a whopping 1.4 *billion* transistors**. That’s a lot. For context and scale, here’s a shot of the 280 GPU next to a modern Intel dual-core CPU.


![](https://blog.codinghorror.com/content/images/2025/04/image-144.png)


I’ve talked about this before in [CPU vs. GPU](https://blog.codinghorror.com/cpu-vs-gpu/), but it bears repeating: **some of the highest performing hardware in your PC lies on your video card**. At least for a certain [highly parallelizable set of tasks](https://web.archive.org/web/20081201074104/http://www.tomshardware.co.uk/nvidia-gtx-280,review-30971-24.html).


> We were able to compress our test video (400 MB) in iPhone format (640*365) at maximum quality in 56.5 seconds on the 260 GTX and 49 seconds on the 280 GTX (15% faster). For comparison purposes, the iTunes H.264 encoder took eight minutes using the CPU (consuming more power overall but significantly less on peaks).


While one of the [primary benefits of manycore CPUs](https://blog.codinghorror.com/re-encoding-your-dvds/) is radically faster video encoding, let’s put this in context – compared to the newest, speediest quad core CPU, you can encode video **ten times faster** using a modern video card GPU. It’s my hope that [CUDA](http://www.nvidia.com/object/cuda_home.html), Microsoft’s Accelerator, and Apple’s Grand Central/[OpenCL](http://en.wikipedia.org/wiki/OpenCL) will make this more accessible to a wide range of software developers.


All this physics horsepower, whether it’s coming from yet another manycore x86 CPU, or a massively parallel GPU, is there for the taking. There are quite a few [physics engines](http://en.wikipedia.org/wiki/Physics_engine) available to programmers:

- [Havok](https://web.archive.org/web/20080623061125/http://tryhavok.intel.com/)
- [Newton](http://www.newtondynamics.com/downloads.html)
- [Open Dynamics Engine](http://www.ode.org/)
- [Actionscript Physics Engine](https://web.archive.org/web/20081216010619/http://www.cove.org/ape/index.htm)
- [Farseer Physics Engine](https://web.archive.org/web/20080702113601/http://www.codeplex.com/FarseerPhysics)
- [NVIDIA PhysX](https://developer.nvidia.com/tools-downloads#?tx=$physx_sdk,3.3.0,3.3.1,3.3.2,3.3.3,3.3.4,3.4.0)
- [Bullet Physics](http://bulletphysics.com/)


There are no shortage of physics games and sandboxes to play with this stuff, too. Here are a few of my favorites.


Perhaps the most archetypal physics based game is Chronic Logic’s [Bridge Construction Set](http://www.chroniclogic.com/index.htm?pontifex2.htm), the original version of which dates way back to 1999. I’m showing a picture of their fancy NVIDIA branded version below, but it’s hardly about the graphics. This is pure physics simulation at its most entertaining. Who knew civil engineering could be so much *fun?* Highly recommended.


![](https://blog.codinghorror.com/content/images/2025/04/image-143.png)


Oh, and small hint: after playing this game, you will learn to love the power and beauty of the simple triangle. You’ll also marvel at the longer bridges you manage to drive across without plunging into the watery abyss underneath.


I’ve professed my love for The Incredible Machine and other [Rube Goldberg devices before](https://blog.codinghorror.com/rube-goldberg-software-devices/). The physics based game [Armadillo Run](http://www.armadillorun.com/) is a modern iteration of same. Get the armadillo from point A to point B using whatever gizmos and gadgets you find in your sandbox – rendered in glorious 3D with a full-blown 2D physics engine in the background.


![](https://blog.codinghorror.com/content/images/2025/04/image-142.png)


The latest physics based game to generate a lot of buzz is Trials 2: Second Edition. I haven’t had a chance to try it yet, but the [gameplay movie](http://www.youtube.com/watch?v=25DbdzrU8R4) is extremely impressive. Like Armadillo run, the action is all on a 2D plane, but the physics are impeccable.


![](https://blog.codinghorror.com/content/images/2025/04/image-141.png)


I’m sure I’ve forgotten a few physics based games here; peruse this [giant list of physics games](http://www.fun-motion.com/list-of-physics-games/) to see if your favorite is already included.


See, physics *can* be fun – and **increasingly complex physics engines** are an outstanding way to harness the massive computational horsepower that lies dormant in most modern PCs.

[physics](https://blog.codinghorror.com/tag/physics/)
[games](https://blog.codinghorror.com/tag/games/)
[simulation](https://blog.codinghorror.com/tag/simulation/)
[video card](https://blog.codinghorror.com/tag/video-card/)
[gpu](https://blog.codinghorror.com/tag/gpu/)
