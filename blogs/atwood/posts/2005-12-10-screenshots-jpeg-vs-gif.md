---
title: "Screenshots: JPEG vs. GIF (and PNG)"
date: 2005-12-10
url: https://blog.codinghorror.com/screenshots-jpeg-vs-gif/
slug: screenshots-jpeg-vs-gif
word_count: 533
---

It constantly amazes me how many times I **encounter pages where screenshots are inappropriately stored as JPEGs**. Not to single Mike Gunderloy out, but there’s yet another example in his recent article on [configuring an ASP.NET 2.0 website](https://web.archive.org/web/20051231034602/http://developer.com/net/asp/article.php/3569166):


![](https://blog.codinghorror.com/content/images/2025/03/image-370.png)


That is just nasty. As in, [Miss Jackson if you’re nasty](http://www.everything2.com/index.pl?node_id=743607).


Haven’t the two most common image encoding formats on the web – [GIF](http://en.wikipedia.org/wiki/GIF) and [JPEG](http://en.wikipedia.org/wiki/JPEG) – been around long enough for editors to figure out which one is appropriate for a screenshot?


Evidently not. For those hapless editors, here’s the handy Cliff’s Notes version of which encoding algorithm to choose for your screenshots:

kg-card-begin: html


|  |  |
| Use JPEG | Use GIF (or PNG) |


kg-card-end: html

**Most GUI screenshots lean more towards the picture on the right than the picture on the left**. When all else fails, try all three commonly supported image formats (GIF, [PNG](http://en.wikipedia.org/wiki/PNG), and JPEG) and use your common sense to manage the quality and size tradeoffs. I know bandwidth can be expensive. *Just don’t make our eyeballs bleed.*


Unfortunately, capturing decent looking screenshots in a reasonable file size gets more difficult with each successive OS release. Windows XP’s default “Luna” theme was just colorful enough to make it difficult to capture using lossless algorithms like PNG and GIF. That’s one reason I prefer the older “classic” Windows 2000 style GUI skin in XP. But later versions of Windows use color blending and color transitions even more extensively. **This means you’re effectively stuck with lossy JPEG for screenshots in any modern OS.**

kg-card-begin: html


| Great for GIF and PNG! | Not so much. Use JPG. |


kg-card-end: html

At least JPEG images have selectable quality levels. Here’s an example of the various JPEG quality levels and the resulting image sizes using the reference 512x512 Lenna image:

kg-card-begin: html


| [
5% JPEG, 104 kb](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b017616f64bf7970c-800wi.jpg) | [
10% JPEG, 66 kb](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b017616f64d40970c-800wi.jpg) |
| [
20% JPEG, 43 kb](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b016769017677970b-pi.jpg) | [
30% JPEG, 26 kb](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b017616f65612970c-pi.jpg) |
| [
40% JPEG, 17 kb](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b017616f6570d970c-pi.jpg) | [
50% JPEG, 12 kb](https://blog.codinghorror.com/content/images/uploads/2005/12/6a0120a85dcdae970b017743dc6fda970d-pi.jpg) |


kg-card-end: html

For comparison, the **lossless PNG version of this image is 541 kb** – that’s more than 5 times the size of the very high quality 5% JPEG!


Personally, I can’t tell the Lenna reference image from the 10% JPEG without zooming in excessively. That’s a nearly 10:1 file size savings for an image that will be identical to most casual viewers.


But the Lenna image doesn’t have any black on white text embedded in it, like a desktop screenshot would. And these harsh color transitions are particularly difficult for JPEG to encode, as illustrated so painfully in the first screenshot. So **let’s try a 1024x768 screenshot of a typical Windows Vista desktop **with an explorer window, icons, desktop background, etcetera:

kg-card-begin: html


| Lossless PNG (noninterlaced) | 476 kb |
| Lossless JPEG | 821 kb |
| 1% JPEG | 289 kb |


kg-card-end: html

Unfortunately, the 1% JPEG still has quite a bit of noise around the black text to my eye. Check it out yourself and compare it with the lossless PNG. Is this acceptable?

[image compression](https://blog.codinghorror.com/tag/image-compression/)
[file formats](https://blog.codinghorror.com/tag/file-formats/)
[screenshots](https://blog.codinghorror.com/tag/screenshots/)
[image encoding](https://blog.codinghorror.com/tag/image-encoding/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
