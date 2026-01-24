---
title: "Anisotropic Filtering"
date: 2006-01-08
url: https://blog.codinghorror.com/anisotropic-filtering/
slug: anisotropic-filtering
word_count: 416
---

I’ve talked about [Bilinear vs. Bicubic filtering](https://blog.codinghorror.com/the-myth-of-infinite-detail-bilinear-vs-bicubic/) before in the context of 2D images, but bilinear filtering is a key ingredient in 3D graphics, too. When a texture is applied to a polygon, the texture may be scaled up or down to fit, depending on your screen resolution. This is done via bilinear filtering.


A full discussion of 3D graphics is way outside the scope of this post – plus I don’t want to bore you to death with concepts like trilinear filtering and mip-mapping. But I do want to highlight one particular peculiarity of bitmap scaling in 3D graphics. **As you rotate a texture-mapped polygon away from the viewer, simple bilinear filtering and mip-mapping cause the texture to lose detail as the angle increases:**


![](https://blog.codinghorror.com/content/images/2025/05/image-154.png)


Now, **some detail loss with distance is intentional**. That’s essentially what [mip-mapping](http://www.gamedev.net/reference/articles/article1233.asp) is. if we didn’t mip-map into the distance, the image would look extremely noisy:

kg-card-begin: html


| No mip-mapping | Mip-mapping |
|  |  |


kg-card-end: html

The problem with simple mip-mapping and bilinear filtering is that they’re *too simple*. Much more detail should be retained into the distance. And **that’s what anisotropic filtering does**:


![](https://blog.codinghorror.com/content/images/2025/05/image-155.png)


Because you’re typically viewing most of the polygons in the world at an angle at any given time, **anisotropic filtering has a profound impact on image quality**. Here are some screenshots I took from the PC game [FlatOut](http://www.flatoutgame.com/) which illustrate the dramatic difference between standard filtering and anisotropic filtering:

kg-card-begin: html


| Standard filtering | 16x Anisotropic filtering |
|  |  |
|  |  |


kg-card-end: html

These are detail elements cropped from the full-size 1024x768 screenshots: [standard](https://web.archive.org/web/20060822001704/http://www.codinghorror.com/blog/images/flatout-no-aniso-full.jpg), [anisotropic](https://web.archive.org/web/20060822001537/http://www.codinghorror.com/blog/images/flatout-aniso-full.jpg).


Proper anisotropic filtering is computationally expensive, even on dedicated 3D hardware. And the performance penalty increases with resolution. ATI was the first 3d hardware vendor to introduce some [anisotropic filtering optimizations](http://www.3dcenter.org/artikel/2003/11-21_a_english.php) – some would say shortcuts – in their cards which allowed much higher performance. There is one small caveat, however: at some angles, textures don’t get fully filtered. ATI effectively optimized for common angles you’d see in 3D level geometry (floor, walls, ceiling) at the cost of the others.


For better or worse, these optimizations are now relatively standard now even on [nVidia cards](https://web.archive.org/web/20070302061333/http://www.xbitlabs.com/articles/video/display/geforce6600g-games_3.html). I think it’s a reasonable tradeoff for the increased image quality and performance.


In my opinion, **anisotropic filtering is the most important single image quality setting available on today’s 3D hardware**. It’s like [Freedom Rock](http://www.urbandictionary.com/define.php?term=Freedom+Rock&defid=1564108): make sure you’ve turned it up, man!

[graphics](https://blog.codinghorror.com/tag/graphics/)
[3d](https://blog.codinghorror.com/tag/3d-2/)
[filtering](https://blog.codinghorror.com/tag/filtering/)
[mip-mapping](https://blog.codinghorror.com/tag/mip-mapping/)
[bilinear filtering](https://blog.codinghorror.com/tag/bilinear-filtering/)
