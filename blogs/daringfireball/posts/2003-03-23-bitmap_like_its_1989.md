---
title: "Bitmap Like It’s 1989"
date: 2003-03-23
url: https://daringfireball.net/2003/03/bitmap_like_its_1989
slug: bitmap_like_its_1989
word_count: 509
---


Follow-ups and corrections regarding “[Anti-Anti-Aliasing](http://daringfireball.net/2003/03/antiantialiasing.html)”.


Dave Hyatt: [Fonts in Safari](http://www.mozillazine.org/weblogs/hyatt/archives/2003_03.html#002925):


> Safari *is* using the wrong fonts for rendering to the
> 	screen. Because of our use of lower-level APIs, we missed out on a font
> 	substitution step that happens when rendering to the screen where the
> 	bitmap font ends up getting chosen for rendering. This is a bug in Safari,
> 	and we’re looking into fixing it.


See also: [An Education in Anti-Aliasing](http://www.mozillazine.org/weblogs/mt/mt-comments.cgi?entry_id=2921), which prompted me to tell Amy “I can’t believe Hyatt has already responded to my article,” which prompted Amy to respond, “I can’t believe he called that ‘an interesting read’.”


## Dot Matrix


One clear mistake I made was my claim that the ImageWriter’s resolution
was only 72 DPI. [Nicholas Riley](http://web.sabi.net/log/) wrote via email:


> The ImageWriter had 144 dpi resolution, not 72 dpi.  If you picked
> 	“Best” quality (as opposed to “Faster”, which was 72 dpi, or “Draft”
> 	which was text only), then the ImageWriter driver would draw a 2× font
> 	at full printer resolution if it could — you’d get half-size 24 point
> 	Geneva where you specified 12 point Geneva, for example.
> 	In even more obscure trivia, the ImageWriter LQ was 216 dpi and used
> 	3× screen fonts.  I really loved the gigantic 72 point screen fonts
> 	that came on my LQ installation disks, prior to ATM and TrueType...


Riley also pointed out that in the screenshots showing how Camino renders Hivelogic’s navigation menu, Camino is displaying 10-point Geneva, not 9-point Geneva. Which is slightly odd, since the Hivelogic [CSS stylesheet](http://www.hivelogic.com/style/master.css) specifies 9 pixels as the size for that font. (Internet Explorer correctly uses 9-point Geneva, if you’re interested in seeing the difference.)


## Hinting


Several people wrote to point out that it wasn’t accurate to describe TrueType hinting as simply embedding bitmaps in the TrueType font. I knew this, that hinting is actually much more powerful than just bitmaps, but it’s also much more complicated, and the article was already long enough, so I only mentioned it in passing. It is hinting that allows Microsoft fonts like Verdana and Georgia to looks so good on-screen without anti-aliasing. From a type designer’s standpoint, hinting is much more than a bitmapping technique, but from a user’s standpoint, the result is the same: hinting allows the designer to precisely control which pixels are used to render each letterform. Microsoft.com’s typography section has more [information on TrueType hinting](http://www.microsoft.com/typography/hinting/hinting.htm).


It’s also worth noting that well-hinted fonts seem to look better than unhinted fonts, even when anti-aliased. This would explain why ProFont — whose TrueType version is well-hinted — looks good when anti-aliased in Safari. If Monaco looked that good in Safari, I probably wouldn’t have bothered writing about this in the first place.


## Two Bits


Lastly, I described black-and-white displays as “2-bit”, when of course, a black-and-white display is just 1-bit. Two colors, but just one bit. A 2-bit display would be four colors.



| **Previous:** | [Anti-Anti-Aliasing](https://daringfireball.net/2003/03/anti-anti-aliasing) |
| **Next:** | [The Party’s Over](https://daringfireball.net/2003/03/the_partys_over) |


PreviousNext