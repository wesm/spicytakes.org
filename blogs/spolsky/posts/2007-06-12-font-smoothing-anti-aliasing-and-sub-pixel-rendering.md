---
title: "Font smoothing, anti-aliasing, and sub-pixel rendering"
date: 2007-06-12
url: https://www.joelonsoftware.com/2007/06/12/font-smoothing-anti-aliasing-and-sub-pixel-rendering/
word_count: 668
---


Apple and Microsoft have always disagreed in how to display fonts on computer displays. Today, both companies are using [sub-pixel rendering](http://www.grc.com/ctwhat.html) to coax sharper-looking fonts out of typical low resolution screens. Where they differ is in philosophy.

- Apple generally believes that the goal of the algorithm should be to preserve the design of the typeface as much as possible, even at the cost of a little bit of blurriness.
- Microsoft generally believes that the shape of each letter should be hammered into pixel boundaries to prevent blur and improve readability, even at the cost of not being true to the typeface.


Now that Safari for Windows is available, which goes to great trouble to use Apple’s rendering algorithms, you can actually compare the philosophies side-by-side on the very same monitor and see what I mean. I think you’ll notice the difference. Apple’s fonts are indeed fuzzy, with blurry edges, but at small font sizes, there seems to be much more variation between different font families, because their rendering is truer to what the font would look like if it were printed at high resolution.


(Note: To see the following illustration correctly, you need to have an LCD monitor with pixels arranged in R,G,B order, like mine. Otherwise it’s going to look different and wrong.)


The difference originates from Apple’s legacy in desktop publishing and graphic design. The nice thing about the Apple algorithm is that you can lay out a page of text for print, and on screen, you get a nice approximation of the finished product. This is especially significant when you consider how dark a block of text looks. Microsoft’s mechanism of hammering fonts into pixels means that they don’t really mind using thinner lines to eliminate blurry edges, even though this makes the entire paragraph lighter than it would be in print.


The advantage of Microsoft’s method is that it works better for on-screen reading. Microsoft pragmatically decided that the design of the typeface is not so holy, and that sharp on-screen text that’s comfortable to read is more important than the typeface designer’s idea of how light or dark an entire block of text should feel. Indeed Microsoft actually designed font faces for on-screen reading, like Georgia and Verdana, around the pixel boundaries; these are beautiful on screen but don’t have much character in print.


Typically, Apple chose the stylish route, putting art above practicality, because Steve Jobs has taste, while Microsoft chose the comfortable route, the measurably pragmatic way of doing things that completely lacks in panache. To put it another way, if Apple was Target, Microsoft would be Wal-Mart.


Now, on to the question of what people prefer. Jeff Atwood’s [post](http://www.codinghorror.com/blog/archives/000884.html) from yesterday comparing the two font technologies side-by-side generated rather predictable heat: Apple users liked Apple’s system, while Windows users liked Microsoft’s system. This is not just standard fanboyism; it reflects the fact that when you ask people to choose a style or design that they prefer, unless they are trained, they will generally choose the one that looks most familiar. In most matters of taste, when you do preference surveys, you’ll find that most people don’t really know what to choose, and will opt for the one that seems most familiar. This goes for anything from silverware (people pick out the patterns that match the silverware they had growing up) to typefaces to graphic design: unless people are trained to know what to look for, they’re going to pick the one that is most familiar.


Which is why Apple engineers probably feel like they’re doing a huge service to the Windows community, bringing their “superior” font rendering technology to the heathens, and it explains why Windows users are generally going to think that Safari’s font rendering is blurry and strange and they don’t know why, they just don’t like it. Actually they’re thinking… “Whoa! That’s different. I don’t like different. Why don’t I like these fonts? Oh, when I look closer, they look blurry. *That must be why.*“
