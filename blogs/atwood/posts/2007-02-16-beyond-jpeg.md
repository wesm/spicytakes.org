---
title: "Beyond JPEG"
date: 2007-02-16
url: https://blog.codinghorror.com/beyond-jpeg/
slug: beyond-jpeg
word_count: 501
---

It’s surprising that the venerable [JPEG image compression standard](http://en.wikipedia.org/wiki/JPEG), which dates back to 1986, is **still the best we can do for photographic image compression**. I can’t remember when I encountered my first JPEG image, but JPEG didn’t appear to enter practical use [until the early 90’s](http://www.vias.org/pngguide/chapter07_01.html).


There’s nothing *wrong* with JPEG. I’'s a perfectly serviceable image compression format. But there are newer, more modern choices these days. There’s even a sequel of sorts to JPEG known as [JPEG 2000](http://en.wikipedia.org/wiki/JPEG_2000). It’s the logical heir to the JPEG throne.


The promise of JPEG 2000 is **higher image quality in much smaller file sizes**, at the minor cost of additional CPU time. And since we always seem to have a lot [more CPU time than bandwidth](https://blog.codinghorror.com/the-popularity-tax/), this is a perfect tradeoff. You may remember my [comparison of JPEG compression levels](https://blog.codinghorror.com/a-comparison-of-jpeg-compression-levels-and-recompression/) entry from last year. Let’s see what happens when we take the two worst-looking images from that comparison – the ones with JPEG compression factor 40 and 50 – and use JPEG 2000 to produce images of (nearly) the exact same size:

kg-card-begin: html


| JPEG, ~8,200 bytes | JPEG 2000, ~8,200 bytes |
|  |  |
| JPEG, ~10,700 bytes | JPEG 2000, ~10,700 bytes |
|  |  |


kg-card-end: html

No current web browsers can render JPEG 2000 (.jp2) images, so what you’re seeing are extremely high quality JPEG versions of the JPEG 2000 images. Click on the images to download the actual JPEG 2000 files; most modern photo editing software can view them natively.


JPEG 2000 not only compresses more efficiently, it also does a better job of hiding its compression artifacts, too. It takes a lot more bits per pixel to create a JPEG image that looks as good as a JPEG 2000 image. But if you’re willing to pump up the file size, you aren’t losing any fidelity by presenting JPEG images.


Microsoft, as Microsoft is wont to do, offers a closed-source alternative to JPEG 2000 known as [HD Photo or Windows Media Photo](http://en.wikipedia.org/wiki/HD_Photo). As of late 2006, Microsoft made the format 100% royalty free, and support for HD Photo is included in Windows Vista and .NET Framework 3.0. According to [this Russian study](http://www.compression.ru/video/codec_comparison/wmp_codecs_comparison_en.html), Files in Microsoft’s HD Photo format (.hdp, .wdp) are comparable to – but *not better than –* JPEG 2000. The [study PDF](http://www.compression.ru/video/codec_comparison/pdf/wmp_codec_comparison_en.pdf) has lots of comparison images, so you can decide for yourself.


Unfortunately, it doesn’t really matter which next-generation image compression format is better, since *nobody uses them*. Microsoft neglected to include support for HD Photo in Internet Explorer 7. And Firefox doesn’t currently support JPEG 2000, either. It’s a bit of a mystery, because there’s an seven year-old [open bug on JPEG 2000](http://bugzilla.mozilla.org/show_bug.cgi?id=36351), and the [OpenJPEG library](https://web.archive.org/web/20071014224104/http://www.openjpeg.org/index.php?menu=main) seems like a logical fit.


Until a commonly used web browser supports JPEG 2000 or HD Photo, there’s no traction. I hope the next browser releases can **move us beyond the ancient JPEG image compression format**.

[image compression](https://blog.codinghorror.com/tag/image-compression/)
[jpeg](https://blog.codinghorror.com/tag/jpeg/)
[jpeg 2000](https://blog.codinghorror.com/tag/jpeg-2000/)
[compression standards](https://blog.codinghorror.com/tag/compression-standards/)
[file formats](https://blog.codinghorror.com/tag/file-formats/)
