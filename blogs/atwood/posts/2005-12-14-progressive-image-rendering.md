---
title: "Progressive Image Rendering"
date: 2005-12-14
url: https://blog.codinghorror.com/progressive-image-rendering/
slug: progressive-image-rendering
word_count: 480
---

I’m a big fan of showing the user visual feedback as soon as possible, whether you’re [downloading a web page](https://blog.codinghorror.com/the-lost-art-of-progressive-html-rendering/) or [rendering a windows form](https://blog.codinghorror.com/perceived-performance-and-formpaint/).


Images already render progressively in a web browser – but you can do even better. **Simply save your GIF or PNG images with the “interlaced” option, or your JPEG images with the “progressive” option.**


Stephan Lavavej has a [great page outlining the difference](http://nuwen.net/png.html) between fancy interlacing and plain old progressive rendering:

kg-card-begin: html

> There are four ways to transmit an image over the Internet. Over a fast connection there won’t be any apparent difference, but over a modem connection the difference is stunningly obvious. Choosing the right way can make your connection seem much faster than it really is.
> **Wait until every bit of image data has been sucked through the modem before displaying the whole image**. So blindingly dumb that not even Internet Explorer does it.
> **Display image data as it is received, resulting in a top-down filling in of the image**. One variant – the one that everyone has seen – of JPEG does this. This is noninterlaced display, and both GIF and PNG are capable of it as well. Non-interlaced images are smaller than interlaced images.
> **Use a one-dimensional interlacing scheme**. This is how GIF interlacing works. Every eighth horizontal line is transmitted in the first “pass,” filling up the dimensions of the image in 1/8th of the time that the entire image will take to download. The next pass transmits every fourth line, making the image less distorted. The next pass transmits every second line, making the image even less distorted, and the fourth and final pass transmits the remaining lines.
> **Use a two-dimensional interlacing scheme**. This is how PNG interlacing works. Instead of four passes through the image, PNG makes seven passes. In 1/64 of the time that the whole image will take to display, one pass is already completed, showing the image in a very rough manner. Successive passes fill in more information, never distorting the pixels by more than a factor of two to one.

kg-card-end: html

Here’s a demo of simple progressive as-received rendering:


![Hello Kitty, standard progressive rendering](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b0128776fcab6970c-pi.gif)


And here’s a demo of the superior PNG style two-dimensional interlaced rendering:


![Hello Kitty, PNG style two-dimensional interlaced rendering](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b0128776fcadb970c-pi.gif)


You don’t get this for free, of course – **turning this feature on adds about 20% to the size of PNG images, and about 10% to the size of JPEG and GIF images.** Whether this improved rendering behavior is worth the bandwidth cost I leave as an exercise to the reader.


I am not aware of any browsers that actually bilinearly interpolate the low-resolution incremental images, as shown in the sample screenshots on Stefan’s page. But that would be really cool! Why doesn’t Firefox add this?

[html](https://blog.codinghorror.com/tag/html/)
[css](https://blog.codinghorror.com/tag/css/)
[image rendering](https://blog.codinghorror.com/tag/image-rendering/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
