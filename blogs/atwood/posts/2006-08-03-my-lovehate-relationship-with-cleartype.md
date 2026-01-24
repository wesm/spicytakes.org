---
title: "My Love/Hate relationship with ClearType"
date: 2006-08-03
url: https://blog.codinghorror.com/my-lovehate-relationship-with-cleartype/
slug: my-lovehate-relationship-with-cleartype
word_count: 386
---

I’ve been vacillating a bit on [ClearType](https://web.archive.org/web/20071221082752/http://www.microsoft.com/typography/ClearTypeInfo.mspx) recently. I love ClearType in theory. A threefold improvement in horizontal resolution on LCDs is an incredible step forward for computer displays. Internet Explorer 7 forces the issue a bit by always defaulting to ClearType for web content, even if you haven’t enabled ClearType in Windows XP.


To sweeten the pot even further, [Consolas](https://web.archive.org/web/20061223092933/http://www.microsoft.com/downloads/details.aspx?familyid=22e69ae4-7e40-4807-8a86-b3d36fab68d3&displaylang=en), one of the best (if not the best) fixed-width fonts [I’ve ever seen](https://blog.codinghorror.com/progamming-fonts/), is [only usable with ClearType enabled](https://blog.codinghorror.com/consolas-and-cleartype/).


But in practice, **I keep running into problems with ClearType enabled that drive me absolutely bonkers.** Check out this shot of Hex Workshop, using the Consolas font, with ClearType enabled:


![](https://blog.codinghorror.com/content/images/2025/04/image-735.png)


What’s up with the hideous halation effects around the selected characters? It’s unbearable! The obvious RGB noise around the characters is not helping readability at all.


Fortunately, the [ClearType Tuner PowerToy](https://web.archive.org/web/20061117142124/http://www.microsoft.com/typography/ClearTypePowerToy.mspx) lets us tweak this for the better. Switch to the advanced tab so you can use the ClearType Contrast Setting slider. The slider has a range of 1.0 to 2.2, and the changes take effect in real time.


Here’s a shot of the same window with 2.2 contrast, the lightest possible.


![](https://blog.codinghorror.com/content/images/2025/04/image-736.png)


The effect is exacerbated by reducing the contrast, so **clearly we have a contrast problem**. Let’s try turning it all the way up.


Here’s a shot of the same window with 1.0 contrast, the darkest possible.


![](https://blog.codinghorror.com/content/images/2025/04/image-737.png)


Maximum contrast looks good, but it has an unwanted side effect as well – now **bold** text looks terrible! Compare for yourself. Minimum contrast at the top, standard in the middle, and maximum at the bottom.


![](https://blog.codinghorror.com/content/images/2025/04/image-739.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-738.png)


Bold text looks best with contrast set to *minimum*. I just can’t win.


I’m currently compromising by sliding the contrast slider over a few notches toward the darker side – a setting of 1.4 versus the default of 1.6. But no matter how I tweak the slider, there are always places where the text is less legible with ClearType on. Sometimes pathologically so.


I guess it’s back to standard greyscale font smoothing for me. It’s too bad, because I love Consolas, and I think ClearType is genius – if they could get it to look good in *all* situations, and not just for black text on a white background.

[font rendering](https://blog.codinghorror.com/tag/font-rendering/)
[cleartype](https://blog.codinghorror.com/tag/cleartype/)
[consolas](https://blog.codinghorror.com/tag/consolas/)
[display technology](https://blog.codinghorror.com/tag/display-technology/)
[web content](https://blog.codinghorror.com/tag/web-content/)
