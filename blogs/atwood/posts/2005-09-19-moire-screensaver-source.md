---
title: "Moire Screensaver Source"
date: 2005-09-19
url: https://blog.codinghorror.com/moire-screensaver-source/
slug: moire-screensaver-source
word_count: 241
---

I’m not a big screensaver enthusiast per se, but one of my all time favorite screensavers is definitely [Moire](http://www.realtimesoft.com/multimon/products.asp#ScreenSavers) from the DirectX 8.1 SDK. It’s simple yet visually striking, and **it works seamlessly on multiple monitors**. It’s also hardware accelerated on each monitor without requiring a lot of video card horsepower or CPU time.


![](https://blog.codinghorror.com/content/images/2025/05/image-139.png)


One thing that always bugged me about Moire, though, was that **it chose the same colors over and over**. Every time it ran, it would cycle through the same exact color sequences, in the same order.


Well, after digging around (a lot) to find the DX 8.1 SDK that this sample is specific to, I came up with the C++ source for Moire. With the assistance of a coworker more versed in C++ than I, we managed to bundle Moire into a VS.NET 2003 C++ solution. Then I was able to hack in a **more sophisticated random color algorithm** with my completely negligible C++ coding skillz.


This solution compiles fine on any machine with VS.NET 2003 installed; no DirectX SDK is required. I’ve attached both the original, unmodified Moire from the SDK and our modified random color version. And if you don’t feel like hacking on the source code, I put a binary up as well.

- [Moire screensaver](https://web.archive.org/web/20060901075900/http://www.codinghorror.com/blog/files/Moire.zip) binary (173kb)
- [Original Moire VS.NET 2003 C++ solution](https://web.archive.org/web/20060910124429/http://www.codinghorror.com/blog/files/Moire_vsnet2003_solution.zip) (70kb)
- [Modified Moire VS.NET 2003 C++ solution](https://web.archive.org/web/20060909130021/http://www.codinghorror.com/blog/files/Moire_vsnet2003_solution_randomcolors.zip) (71kb)

[c++](https://blog.codinghorror.com/tag/c/)
[directx 8.1](https://blog.codinghorror.com/tag/directx-8-1/)
[screensaver](https://blog.codinghorror.com/tag/screensaver/)
[vs.net 2003](https://blog.codinghorror.com/tag/vs-net-2003/)
[random color algorithm](https://blog.codinghorror.com/tag/random-color-algorithm/)
