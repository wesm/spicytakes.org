---
title: "What’s Wrong With Apple’s Font Rendering?"
date: 2007-06-11
url: https://blog.codinghorror.com/whats-wrong-with-apples-font-rendering/
slug: whats-wrong-with-apples-font-rendering
word_count: 372
---

I had read a few complaints that OS X font rendering was a little wonky, even from [Joel Spolsky himself](http://www.joelonsoftware.com/items/2006/09/11.html):


> OS X antialiasing, especially, it seems, with the monospaced fonts, just isn’t as good as Windows ClearType. Apple has some room to improve in this area; the fonts were blurry on the edges.


I didn’t believe it until I downloaded the first beta of Safari 3 for Windows and saw it for myself.


Font rendering in [Safari 3 Beta](http://www.apple.com/safari/):


![Font rendering in Safari 3 beta for Windows](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d908c970b-pi.png)


Font rendering in [Internet Explorer 7](http://www.microsoft.com/windows/ie/default.asp):


![Font rendering in IE7](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d90b0970b-pi.png)


All of these screenshots were taken under Windows Vista. It’s easier to see what’s happening if we zoom in a bit. These images are zoomed 200% with exact per-pixel resizing. Safari on the top, IE7 on the bottom:


![Font rendering in Safari, closeup](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b015392886717970b-pi.png)


![Font rendering in IE7, closeup](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0154365c1608970c-pi.png)


At first I wasn’t even sure if Apple was using [ClearType](https://web.archive.org/web/20070711100153/http://www.microsoft.com/typography/ClearTypeInfo.mspx)-alike RGB anti-aliasing, but it’s clear from the zoomed image that they are. **It looks like they’ve skewed the contrast of the fonts to an absurdly low level.** The [ClearType Tuner PowerToy](https://web.archive.org/web/20070703053310/http://www.microsoft.com/typography/ClearTypePowerToy.mspx) allows you to manually adjust the RGB font aliasing contrast level, as I documented in an [earlier blog post](https://blog.codinghorror.com/my-lovehate-relationship-with-cleartype/), but I don’t think it can go as low as Apple has it set.


**I am absolutely not trying to start an **[**OS X versus Windows flame war**](https://blog.codinghorror.com/because-they-all-suck/)** here**. I used the quote above for a reason: there really is no single best way to render fonts; results depend on your display, the particular font you’re using, and many other factors. That said, I’m curious why Apple’s default font rendering strategies, *to my eye* – and to the eyes of at least two other people – are visibly inferior to Microsoft’s on typical LCD displays. This is exactly the kind of graphic designer-ish detail I’d expect Cupertino to get right, so it’s all the more surprising to me that they apparently haven’t.

kg-card-begin: html

**Update:** I have a [followup post](https://blog.codinghorror.com/font-rendering-respecting-the-pixel-grid/) that explains the font rendering difference. It looks like neither Apple or Microsoft is wrong; it’s a question of whether you respect the pixel grid.

kg-card-end: html
[font rendering](https://blog.codinghorror.com/tag/font-rendering/)
[apple](https://blog.codinghorror.com/tag/apple/)
[os x](https://blog.codinghorror.com/tag/os-x/)
[safari](https://blog.codinghorror.com/tag/safari/)
[windows cleartype](https://blog.codinghorror.com/tag/windows-cleartype/)
