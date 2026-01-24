---
title: "A Comparison of JPEG Compression Levels and Recompression"
date: 2006-07-06
url: https://blog.codinghorror.com/a-comparison-of-jpeg-compression-levels-and-recompression/
slug: a-comparison-of-jpeg-compression-levels-and-recompression
word_count: 423
---

Over the years, I’ve standardized on a **JPEG compression factor of 15**; I find that generally provides the best compromise between image quality and file size for most photographic images.


Although I’ve done some ad-hoc testing that pointed to compression factor 15 as the sweet spot before, I’ve never done a formal test. So I performed a JPEG compression series using the [Lena reference image](https://web.archive.org/web/20140115220741/http://www.ece.rice.edu/~wakin/images/).* Note that I resized the image slightly (from 512x512 to 384x384) to keep the file sizes relatively small. The original, uncompressed image size is 433 kilobytes.

kg-card-begin: html


| **compression factor 10** (39 kb) | **compression factor 15** (30 kb) |
|  |  |
| **compression factor 20** (26 KB) | **compression factor 30** (16 KB) |
|  |  |
| **compression factor 40** (11 KB) | **compression factor 50** (9 KB) |
|  |  |


kg-card-end: html

Beyond 50 percent compression factor, quality falls off a cliff, so I won’t bother displaying anything higher. Here’s a more complete breakdown of JPEG compression factor and file size for the 384x384 Lena image:


![](https://blog.codinghorror.com/content/images/2025/05/image-329.png)


I was also curious what the image quality and file size penalty was for **recompressing a JPEG image**. That is, opening a JPEG and re-saving it as a JPEG, including all the artifacts from the original compressed image in the recompression. I’ve been forced to do this when I couldn’t find an uncompressed or high quality version of the image I needed, and I always wondered how much worse it made the image when I recompressed it.


For the recompression test, I started with the uncompressed, resized 384x384 Lena reference image. For each new generation, I opened and saved the previous generation with my standard JPEG compression factor of 15.

kg-card-begin: html


| Generation 1 (30kb) | Generation 2 (30kb) |
|  |  |
| Generation 3 (30kb) | Generation 4 (30kb) |
|  |  |
| Generation 5 (30kb) | Generation 10 (30kb) |
|  |  |


kg-card-end: html

I was quite surprised to find that there’s **very little visual penalty for recompressing a JPEG once, twice, or even three times.** By generation five, you can see a few artifacts emerge in the image, and by generation ten, you’re definitely in trouble. There’s virtually no effect at all on file size, which stays constant at 30-31 kilobytes even through generation 15.


*An entire set of classic reference images is available from the USC-SIPI image database. I distinctly remember that [Mandrill image](https://web.archive.org/web/20060830004859/http://sipi.usc.edu/database/database.cgi?volume=misc&image=11#top) from my Amiga days.

[image compression](https://blog.codinghorror.com/tag/image-compression/)
[jpeg](https://blog.codinghorror.com/tag/jpeg/)
[file size](https://blog.codinghorror.com/tag/file-size/)
[image quality](https://blog.codinghorror.com/tag/image-quality/)
[compression levels](https://blog.codinghorror.com/tag/compression-levels/)
