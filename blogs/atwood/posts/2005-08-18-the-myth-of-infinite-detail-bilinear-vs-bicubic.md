---
title: "The myth of infinite detail: Bilinear vs. Bicubic"
date: 2005-08-18
url: https://blog.codinghorror.com/the-myth-of-infinite-detail-bilinear-vs-bicubic/
slug: the-myth-of-infinite-detail-bilinear-vs-bicubic
word_count: 366
---

Have you ever noticed how, in movies and television, actors can take a crappy, grainy low-res traffic camera picture of a distant automobile and somehow “enhance” the image until they can read the license plate perfectly?


Yeah.


I don’t know what kind of crazy infinite-detail fractal images these scriptwriters think we have. Here in the real world, [bitmaps don’t scale](https://blog.codinghorror.com/trapped-in-a-bitmapped-world/) worth a damn. Take this bitmap, for example:


![Hello Kitty, biatch!](https://blog.codinghorror.com/content/images/uploads/2005/08/6a0120a85dcdae970b0120a86d4c46970b-pi.gif)


If we blow that up 300% using the simplest possible algorithm ‐ a naïve nearest neighbor (aka pixel resize) approach – we get this:


![](https://blog.codinghorror.com/content/images/2025/03/image-223.png)


Pixel-tastic! But there’s a well known way of interpolating the pixels in the image so it doesn’t look *quite* so bad when upsized – something called **bilinear filtering**. Bilinear filtering samples nearby pixels in an effort to guesstimate what the missing pixels would look like in a larger image. Let’s enlarge the image 300% using bilinear filtering and see what happens:


![](https://blog.codinghorror.com/content/images/2025/03/image-222.png)


A bit blurry, yes, but clearly superior to giant chunky pixels.


There’s also something called **bicubic filtering** which is supposed to be an improvement over bilinear filtering. Video cards have offered bilinear filtering for years, but they don’t bother with bicubic filtering to this day. And that’s with millions of transistors to burn. If bicubic is only offered by paint programs, you have to wonder, is it really worth it? Here’s the same image enlarged 300% using bicubic filtering:


![](https://blog.codinghorror.com/content/images/2025/03/image-221.png)


Interesting. It’s sharper, but I’m not sure it’s all that much better. And there’s a bit of an over sharpening or halation effect at some color borders, too.


There’s [another image sample](https://web.archive.org/web/20050913135519/http://www.interpolatethis.com/closeups/nearestCU.html) at Interpolate This with a writeup that implies that bicubic is flat-out superior, but I’m not sure that’s the case. Either way you’re interpolating,* it’s just a question of how sharp you like your simulated pixels to be.


The best solution of all is to move to a vector representation and give up on bitmaps – and interpolation – entirely.


*A reader pointed out an interesting algorithm for interpolating low-res images called [2xSAI](http://en.wikipedia.org/wiki/2xSaI). Here’s a [screenshot](http://www.codinghorror.com/.a/6a0120a85dcdae970b017743dceefa970d-pi) I generated of a SNES game with 2xSAI interpolation enabled. Compare to the [original screenshot](http://www.codinghorror.com/.a/6a0120a85dcdae970b01676901f3ab970b-pi).

[image processing](https://blog.codinghorror.com/tag/image-processing/)
[interpolation](https://blog.codinghorror.com/tag/interpolation/)
[bilinear filtering](https://blog.codinghorror.com/tag/bilinear-filtering/)
