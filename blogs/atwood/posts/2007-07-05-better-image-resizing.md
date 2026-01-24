---
title: "Better Image Resizing"
date: 2007-07-05
url: https://blog.codinghorror.com/better-image-resizing/
slug: better-image-resizing
word_count: 730
---

In a previous post, I examined the difference between [bilinear and bicubic image resizing](https://blog.codinghorror.com/the-myth-of-infinite-detail-bilinear-vs-bicubic/) techniques. Those are the two options available in most graphics programs for resizing an image.


![](https://blog.codinghorror.com/content/images/2025/05/image-504.png)


After some experimentation, I came up with these rules of thumb:

- When making an image **smaller, use bicubic**, which has a natural *sharpening* effect. You want to emphasize the data that remains in the new, smaller image after discarding all that extra detail from the original image.
- When making an image **larger, use bilinear**, which has a natural *smoothing *effect. You want to blend over the interpolated fake detail in the new, larger image that never existed in the original image.


Of course, there are plenty of conditions that might make you want to choose one method over the other, but I think these are reasonable guidelines to start with.


What I didn’t realize when I wrote the original article is that **there are other, more advanced resizing algorithms available**. Some are specific to particular kinds of images, such as the [2xSAI](http://en.wikipedia.org/wiki/2xSaI) algorithm which works on pixel art. Compare this shot of [Mario vs. Wario using pixel resizing](https://web.archive.org/web/20071019225507if_/http://www.codinghorror.com/blog/images/mario_wario_pixel.gif), and the [same shot using 2xSAI resizing](https://web.archive.org/web/20071019225600if_/http://www.codinghorror.com/blog/images/mario_wario_2xsal.png). It’s a dramatic difference, especially since traditional bilinear and bicubic upsizing methods degenerate into a giant blur on pixel art.


Supposedly, one of the best image resizing algorithms on the market is [Genuine Fractals](http://www.ononesoftware.com/detail.php?prodLine_id=2). The web site boasts that you can use its **fractal-based resizing algorithm** to *“enlarge your images over 1000% with no loss in image quality.”* It’s probably pure marketing hyperbole, but I was still intrigued. Bilinear and Bicubic are decent, but there has to be room for improvement in there somewhere. I downloaded a trial version of the tool (which requires Photoshop Elements, or Photoshop CS) and gave it a shot.


I took the [the reference Lena image](http://en.wikipedia.org/wiki/Lenna) and blew it up 500%.


Here’s a closeup of the results using **Bicubic Sharper**:


![Lena 512 color reference image, bicubic sharp 5x resize](https://blog.codinghorror.com/content/images/uploads/2007/07/6a0120a85dcdae970b0120a86d97b3970b-pi.jpg)


Here’s the same closeup using **Genuine Fractals**:


![Lena 512 color reference image, fractal 5x resize](https://blog.codinghorror.com/content/images/uploads/2007/07/6a0120a85dcdae970b0120a86d97f0970b-pi.jpg)


Bicubic wouldn’t normally be my choice here, but I chose it because it’s technically the most advanced method, and it produces the results closest to the effect that the fractal resizing delivers. Still, **the fractal algorithm comes out way ahead**; you can’t see any pixel resize artifacts in the enlarged image, and the edges are sharp and well defined. It does start to bear an unfortunate resemblance to a watercolor drawing filter, but arbitrarily resizing images to 5 times their original size will always involve tradeoffs of some kind.


Bicubic and bilinear are well understood image resizing algorithms, and they’re “good enough” for most image resizing chores. That’s why they are provided out of the box in almost all graphics applications and graphics libraries. There’s an [outstanding article on CodeProject](https://web.archive.org/web/20070809135508/http://www.codeproject.com/csharp/imgresizoutperfgdiplus.asp) which digs into advanced image resizing algorithms with actual C# code for some spline and fractal resizing algorithms. But before you begin resizing images, consider whether you *need* those advanced algorithms.


**Reducing images** is a completely safe and rational operation. You’re simply reducing precision and resolution by discarding information. Make the image as small as you want, and you have complete fidelity – within the bounds of the number of pixels you’ve allowed. You’ll get good results no matter which algorithm you pick. (Well, unless you pick the naïve Pixel Resize or Nearest Neighbor algorithms.)


**Enlarging images** is risky. Beyond a certain point, enlarging images is a fool’s errand; you can’t magically synthesize an infinite number of new pixels out of thin air. And interpolated pixels are never as good as real pixels. That’s why it’s more than a little artificial to upsize the 512x512 Lena image by 500%. It’d be smarter to find a higher resolution scan or picture of whatever you need* than it would be to upsize it in software.


But **when you can’t avoid enlarging an image**, that’s when it pays to know the tradeoffs between bicubic, bilinear, and more advanced resizing algorithms. At least arm yourself with enough knowledge to pick the best of the bad options you have.


*E.g., if I really needed the Lena image that large, I’m better off hunting down old copies of Playboy and scanning them myself. Or at least that’s what I tell my wife...

[image processing](https://blog.codinghorror.com/tag/image-processing/)
[image resizing](https://blog.codinghorror.com/tag/image-resizing/)
[digital imagery](https://blog.codinghorror.com/tag/digital-imagery/)
[scaling technique](https://blog.codinghorror.com/tag/scaling-technique/)
