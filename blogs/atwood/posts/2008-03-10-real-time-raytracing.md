---
title: "Real-Time Raytracing"
date: 2008-03-10
url: https://blog.codinghorror.com/real-time-raytracing/
slug: real-time-raytracing
word_count: 1146
---

Like many programmers, my first exposure to [ray tracing](http://en.wikipedia.org/wiki/Ray_tracing) was on my venerable [Commodore Amiga](http://en.wikipedia.org/wiki/Amiga). It’s an iconic system demo every Amiga user has seen at some point: behold the [robot juggling silver spheres!](https://web.archive.org/web/20081208155931/http://home.comcast.net/~erniew/juggler.html)

kg-card-begin: html

> Thus begins the article in the May/June 1987 AmigaWorld in which Eric Graham explains how the Juggler was created. The program (“with full Intuition interface”) promised at the end of the article was [Sculpt 3D](http://en.wikipedia.org/wiki/Sculpt_3D) for the Amiga, released in the fall of 1987. Byte by Byte sold Amiga and then Macintosh and Windows variants of Sculpt for more than a decade.
> Eric rendered the frames in a raytracer he wrote called ssg, a Sculpt precursor. The rendered images were encoded in the Amiga’s HAM display mode and then assembled into a single data file using a lossless delta compression scheme similar to the method that would later be adopted as the standard in the Amiga’s ANIM file format.
> Eric and his wife Cathryn actively promoted raytracing on the Amiga. Cathryn wrote the Amiga Sculpt 3D user manual and compiled an electronic newsletter distributed on a series of disks. Raytracing 1.0, the earliest of these, contains both ssg and the static geometry of the juggler object, along with the Juggler image data and the player program.
> [
> ](http://home.comcast.net/~erniew/getstuff/juggler.avi)
> Juggler was an astounding demo in its time. I personally remember staring at it for several minutes through the front window of a local Amiga dealer, wondering how it “worked.” Many people were inspired by Juggler, and by the Amiga animations that followed, to pursue a career in 3D graphics. Nothing like it could have run on any other stock personal computer in 1986.
> In fact, Eric recalled recently, the Commodore legal department initially “thought it was a hoax, and that I’d done the animation on a mainframe.” He sent them his renderer so that they could generate and compile the frames themselves.

kg-card-end: html

The juggler may seem primitive by today’s standards. Maybe it is. I’ve been subjected to forum signature images with more frames of animation. But it was revelatory back in 1986. **The Amiga brought 3D raytracing graphics to the masses for the first time**. Ray tracing is extremely computation intensive, but hyper-realistic. It’s essentially calculating the result of every individual ray of light in a scene.


![](https://blog.codinghorror.com/content/images/2025/04/image-18.png)


Given the [explosion of computing power](https://blog.codinghorror.com/moores-law-in-practical-terms/) in the 22 years since Juggler was released, you might think all 3D graphics would be rendered via ray tracing by now. To a certain extent, that *is* true; [many computer animated films](http://en.wikipedia.org/wiki/List_of_films_made_involving_PhotoRealistic_RenderMan) are rendered through ray tracing techniques, such as Pixar’s [PhotoRealistic RenderMan](http://en.wikipedia.org/wiki/PhotoRealistic_RenderMan).


![](https://blog.codinghorror.com/content/images/2025/04/image-17.png)


Pixar has done some [incredible work](http://graphics.pixar.com/) on 3D rendering, but it’s not exactly what I’d call *real time*. Courtesy of Chris Anderson, here’s [a little Pixar quiz](http://www.longtail.com/the_long_tail/2006/12/pixar_quiz.html):

kg-card-begin: html

> On 1995 computer hardware, the average frame of Toy Story took two hours to render. A decade later on 2005 hardware, how long did it take the average frame of Cars to render?
> 30 minutes
> 1 hour
> 2 hours
> 15 hours
> Answer: D. **The average Cars frame took 15 hours, despite a 300x overall increase in compute power.** The artists have an essentially infinite appetite for detail and realism, and Pixar’s resources have grown over the decade so it can afford to allocate more computers to the task, allowing each to run longer to achieve the artist’s and animator’s ambitions for the scenes.

kg-card-end: html

Surprisingly, [Cars](http://www.imdb.com/title/tt0317219/) was the first Pixar movie to be rendered with the slower, more accurate ray tracing techniques; previous movies used mostly scanline rendering. There’s an excellent presentation from [Pixar’s Per Christensen](https://web.archive.org/web/20161001174628/http://www.cs.ucy.ac.cy/ayia-napa06/presentations/ayianapa06per.ppt) (ppt) describing the differences in some detail, if you’re curious. And if you want to experiment with ray tracing yourself, there’s always [POV-Ray](http://www.povray.org/), which produces some [impressive results](http://hof.povray.org/) as well.


Movies, of course, don’t have to be rendered in real time. But even with the freedom to take as much time as necessary per frame, ray tracing is often too expensive. Imagine the difficulty, then, of **shoehorning ray tracing into real time 3D engines**. [Modern GPUs are impressive](https://blog.codinghorror.com/cpu-vs-gpu/) pieces of silicon, but they cheat *mightily* when it comes to rendering a 3D scene. They have to, otherwise they’d never be able to generate the 30 or 60 frames per second necessary to provide the illusion of an interactive world.


Of course, this doesn’t stop people from trying. The most impressive real time ray tracing attempt I’ve seen is from Daniel Pohl and his [OpenRT real-time ray tracing project](https://web.archive.org/web/20081103084938/http://www.openrt.de/). Daniel has done some fascinating proof of concept work with Quake 3 and Quake 4.


![](https://blog.codinghorror.com/content/images/2025/04/image-16.png)


But performance remains a problem, even on the latest and greatest hardware:

kg-card-begin: html

> So why don’t we see raytracing right now in games? The problem is still performance. Rendering all these effects through the CPU is not as fast as using special purpose hardware like current graphic cards for the rasterization algorithm. But the evolution of CPUs is fast. Q3RT speed has increased by more than a factor of 4 since 2004. Intel’s new quad core is out and the efficiency using the same CPU clock rate is about 30% higher.
> One big advantage of raytracing is that it is perfect for parallelization. As explained in the introduction, a ray is shot through the 3D scene for every pixel. If you render an image with 640x480 pixels, you have about 300,000 rays. Each of them can be calculated independently of the others. This means the image could be split up into four parts and every core of a quad-core CPU can calculate the color values of the image without waiting on any of the other cores for intermediate results. Therefore the scaling of performance with the number of cores in Quake 4: Ray traced with OpenRT on Intel’s quad-core CPU is great. The following benchmarks were taken at a resolution of 256x256 pixels on the Quake 4 map “Over the Edge (Q4DM7)”.
> 4 cores16.9 fps3.84x scaling
> 2 cores8.6 fps1.96x scaling
> 1 core4.4 fps1x scaling

kg-card-end: html

It’s difficult to find much software that [scales beyond two cores](https://blog.codinghorror.com/choosing-dual-or-quad-core/). So the emergence of a many-core future is a boon to ray tracing algorithms, which scale nearly *perfectly*.


The dimensions of the original juggler are 320 x 200. That’s roughly the same number of pixels as the 256 x 256 Quake 4 benchmark presented above. **It’s possible we could render the ray traced Amiga juggler today in real time at close to 30 fps – but *barely*. **Despite many hyperbolic marketing claims of “rendering Toy Story in real time,” real time ray tracing remains something of a holy grail in practice – considering Toy Story was [rendered at 1536 x 922](http://en.wikipedia.org/wiki/Computer-generated_imagery). Who knows what we’ll be able to render in the next 20 years?
