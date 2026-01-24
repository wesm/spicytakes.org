---
title: "Fast Approximate Anti-Aliasing (FXAA)"
date: 2011-12-07
url: https://blog.codinghorror.com/fast-approximate-anti-aliasing-fxaa/
slug: fast-approximate-anti-aliasing-fxaa
word_count: 1059
---

Anti-aliasing has an intimidating name, but what it does for our computer displays is rather fundamental. **Think of it this way – a line has infinite resolution, but our digital displays do not.** So when we “snap” a line to the pixel grid on our display, we can compensate by imagineering partial pixels along the line, *pretending* we have a much higher resolution display than we actually do. Like so:


![](https://blog.codinghorror.com/content/images/2025/03/image-17.png)


As you can see on these little squiggly black lines I drew, anti-aliasing produces a superior image by using grey pixels to simulate partial pixels along the edges of the line. It is a hack, but as hacks go, it’s pretty darn effective. Of course, the *proper* solution to this problem is to have extremely high resolution displays in the first place. But other than tiny handheld devices, [I wouldn’t hold your breath](https://blog.codinghorror.com/where-are-the-high-resolution-displays/) for that to happen anytime soon.


This also applies to much more complex 3D graphics scenes. Perhaps even more so, since **adding motion amplifies the aliasing effects of all those crawling lines that make up the edges of the scene**.


![](https://blog.codinghorror.com/content/images/2025/03/image-18.png)


But anti-aliasing, particularly at 30 or 60 frames per second in a complex state of the art game, with millions of polygons and effects active, is not cheap. [Per my answer here](http://gaming.stackexchange.com/a/31849), you can generally expect a **performance cost of at least 25% for proper 4X anti-aliasing**. And that is for [the most optimized version of anti-aliasing](http://hacksoflife.blogspot.com/2011/04/so-many-aa-techniques-so-little-time.html) we’ve been able to come up with:

kg-card-begin: html

> **Super-Sampled Anti-Aliasing (SSAA).** The oldest trick in the book – I list it as universal because you can use it pretty much anywhere: forward or deferred rendering, it also anti-aliases alpha cutouts, and it gives you better texture sampling at high anisotropy too. Basically, you render the image at a higher resolution and down-sample with a filter when done. Sharp edges become anti-aliased as they are down-sized. Of course, there’s a reason why people don’t use SSAA: it costs a fortune. Whatever your fill rate bill, it’s 4x for even minimal SSAA.
> **Multi-Sampled Anti-Aliasing (MSAA).** This is what you typically have in hardware on a modern graphics card. The graphics card renders to a surface that is larger than the final image, but in shading each “cluster” of samples (that will end up in a single pixel on the final screen) the pixel shader is run only once. We save a ton of fill rate, but we still burn memory bandwidth. This technique does not anti-alias any effects coming out of the shader, because the shader runs at 1x, so alpha cutouts are jagged. This is the most common way to run a forward-rendering game. MSAA does not work for a deferred renderer because lighting decisions are made after the MSAA is “resolved” (down-sized) to its final image size.
> **Coverage Sample Anti-Aliasing (CSAA).** A further optimization on MSAA from NVidia [ed: ATI has an equivalent]. Besides running the shader at 1x and the framebuffer at 4x, the GPU’s rasterizer is run at 16x. So while the depth buffer produces better anti-aliasing, the intermediate shades of blending produced are even better.

kg-card-end: html

Pretty much all “modern” anti-aliasing is some variant of the MSAA hack, and even *that* costs a quarter of your framerate. That’s prohibitively expensive, unless you have so much performance you don’t even care, which will rarely be true for any recent game. While the crawling lines of aliasing do bother me, I don’t feel anti-aliasing alone is worth giving up a quarter of my framerate and/or turning down other details to pay for it.


But that was before I learned that there are some [emerging alternatives to MSAA](http://gamedev.stackexchange.com/questions/18777/full-screen-anti-aliasing-in-opengl). And then, much to my surprise, these alternatives started showing up as actual graphics options in this season’s PC games – Battlefield 3, Skyrim, Batman: Arkham City, and so on. **What is this FXAA thing, and how does it work?** Let’ see it in action:

kg-card-begin: html


| No AA | 4x MSAA | FXAA |
|  |  |  |


kg-card-end: html

(this is a zoomed fragment; click through to see the full screen)


FXAA stands for Fast Approximate Anti-Aliasing, and it’s an *even more clever hack than MSAA*, because it ignores polygons and line edges, and simply **analyzes the pixels on the screen**. It is a pixel shader program [documented in this PDF](http://developer.download.nvidia.com/assets/gamedev/files/sdk/11/FXAA_WhitePaper.pdf) that runs every frame in a scant millisecond or two. Where it sees pixels that create an artificial edge, it smooths them. It is, [in the words of the author](https://web.archive.org/web/20111217001533/http://timothylottes.blogspot.com/2011/03/nvidia-fxaa.html), “the simplest and easiest thing to integrate and use.”


![](https://blog.codinghorror.com/content/images/2025/03/image-19.png)


FXAA has two major advantages:

1. FXAA smooths edges in *all* pixels on the screen, including those inside alpha-blended textures and those resulting from pixel shader effects, which were previously immune to the effects of MSAA without oddball workarounds.
2. It’s fast. Very, very fast. [Version 3](https://web.archive.org/web/20111217001521/http://timothylottes.blogspot.com/2011/07/nvidia-fxaa-39-released.html) of the FXAA algorithm takes about 1.3 milliseconds per frame on a $100 video card. Earlier versions were found to be [double the speed of 4x MSAA](https://web.archive.org/web/20111217001527/http://www.hardocp.com/article/2011/07/18/nvidias_new_fxaa_antialiasing_technology/5), so you’re looking at a modest 12 or 13 percent cost in framerate to enable FXAA – and in return you get a *considerable* reduction in aliasing.


The only downside, and it is minor, is that you may see a bit of unwanted edge “reduction” inside textures or in other places. I’m not sure if it’s fair to call this a downside, but FXAA can’t directly be applied to older games; **games have to be specifically coded to call the FXAA pixel shader** *before* they draw the game’s user interface, otherwise it will happily smooth the edges of on-screen HUD elements, too.


The FXAA method is *so* good, in fact, it makes all other forms of full-screen anti-aliasing pretty much obsolete overnight. **If you have an FXAA option in your game, you should enable it immediately** and ignore any other AA options.


FXAA is an excellent example of the power of simple hacks and heuristics. But it’s also **a great demonstration of how attacking programming problems from a different angle** – that is, rather than thinking of the screen as a collection of polygons and lines, think of it as a collection of pixels – can enable you to solve computationally difficult problems faster and arguably *better* than anyone thought possible.

[graphics](https://blog.codinghorror.com/tag/graphics/)
[anti-aliasing](https://blog.codinghorror.com/tag/anti-aliasing/)
[display](https://blog.codinghorror.com/tag/display/)
[resolution](https://blog.codinghorror.com/tag/resolution/)
[3d.](https://blog.codinghorror.com/tag/3d/)
