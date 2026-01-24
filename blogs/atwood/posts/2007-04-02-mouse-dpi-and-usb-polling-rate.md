---
title: "Mouse DPI and USB Polling Rate"
date: 2007-04-02
url: https://blog.codinghorror.com/mouse-dpi-and-usb-polling-rate/
slug: mouse-dpi-and-usb-polling-rate
word_count: 699
---

Despite my heavy computer use, I rarely [experience hand or wrist pain](https://blog.codinghorror.com/programming-your-hands/). I consider myself fortunate. However, my mouse hand has been aching a bit lately. In light of my this, I decided it was time to change things up on the mouse front. I currently use the [Logitech MX518](https://blog.codinghorror.com/my-mouse-fetish/) mouse at work and the Logitech G5 mouse at home. Both have the same roughly egg-like shape. I’ve never been completely satisfied with this shape, but it was the best of the available options at the time.


A little research turned up an excellent new alternative: the [Microsoft Habu mouse](http://www.amazon.com/exec/obidos/ASIN/B000H16G3W/). The Habu is roughly the same size and shape as [the classic Intellimouse Explorer](http://www.amazon.com/exec/obidos/ASIN/B000GOUE7O/), which is one of my all-time favorites.


![](https://blog.codinghorror.com/content/images/2025/03/image-88.png)


The Habu is a collaboration between Microsoft and Razer. Razer is best known for their freakishly shaped high-end gaming mice, which I’ve never been a fan of. Fortunately, the Habu seems to have inherited the best traits from its parents: the classic *body* of the Intellimouse Explorer, with the sophisticated *brains* of a Razer gaming mouse. I thought I’d disable the blue LEDs straight away, but as a kid who grew up with the movie [TRON](http://www.imdb.com/title/tt0084827/), the retro blue outline look is growing on me.


![](https://blog.codinghorror.com/content/images/2025/03/image-89.png)


The Habu has all the key features I personally look for in a mouse:

- Wired
- High resolution LED or laser
- Conveniently placed forward and back thumb buttons
- On-the-fly adjustable DPI in hardware


The Habu delivers resolution in spades; it offers four levels selectable via the small buttons behind the mouse wheel: 400, 800, 1600 or 2000 DPI. On top of that, the Habu has one truly unique feature: **it stores all of its settings in onboard flash memory**. It’s the first mouse I’ve ever owned with firmware. Once you’ve configured the settings to taste, you can unplug the mouse, bring it to another computer, and those settings will be retained.


If, like me, you’ve invested in a high resolution mouse, there’s one additional trick you should know to get the most out of it. The default USB polling rate is 125 Hz, which means the mouse cursor can only be updated every 8 milliseconds. But it is possible to **increase the USB polling rate via software or hardware**.

kg-card-begin: html


| Polling rate | Response time |
| 125 Hz | 8 ms |
| 250 Hz | 4 ms |
| 500 Hz | 2 ms |
| 1000 Hz | 1 ms |


kg-card-end: html

It’s no coincidence that the Razer Habu and the latest Logitech mice automatically increase the USB polling rate in hardware. Whenever you plug them in, you’ll benefit from the higher polling rate. Here’s a screenshot of the Habu driver settings; you can select both your preferred DPI and polling rate, and write that into the mouse firmware permanently.


![](https://blog.codinghorror.com/content/images/2025/03/image-90.png)


You can check your current mouse’s USB polling rate via a utility like the Direct Input mouse rate tool.


![](https://blog.codinghorror.com/content/images/2025/03/image-91.png)


Low-end mice and wireless interfaces may not be able to exceed the default 125 Hz USB polling rate, but you won’t know until you try. To change your USB polling rate in software, refer to the following guides.

- [How to change the USB polling rate in Windows Vista](https://web.archive.org/web/20070615200626/http://forum.overclock3d.net/showthread.php?s=e327793189712e82bdacc9c4ffc99950&t=8561)
- [How to change the USB polling rate in Windows XP or Windows 2003](https://web.archive.org/web/20070513233123/http://www.overclock.net/faqs/73418-how-improve-mouse-response-accuracy-changing.html)
- [How to change the USB polling rate in Linux](https://web.archive.org/web/20070911102741/http://www.linux-gamers.net/modules/wiwimod/index.php?page=HOWTO+USBPolling)


If you own a reasonably nice mouse, and the mouse rate tool reports 125 Hz movement, I recommend bumping up the USB polling rate in software. Turning the polling rate all the way up to 1000 Hz probably isn’t necessary. But **if you’re sensitive to cursor smoothness at all, I can practically guarantee you will feel the difference between 125 Hz and 500 Hz.**


If you think all this talk of high DPI mice and USB polling rates is obsessive, trust me, it’s merely the tip of the iceberg. ESReaily developed an entire test rig for [scientifically benchmarking mice](http://www.esreality.com/?a=post&id=1265679), and legions of twitch game players [pore over every minute detail](http://www.overclock.net/computer-peripherals/173255-cs-s-mouse-optimization-guide.html) of their mouse settings.

[gaming mice](https://blog.codinghorror.com/tag/gaming-mice/)
[high-end](https://blog.codinghorror.com/tag/high-end/)
[mouse dpi](https://blog.codinghorror.com/tag/mouse-dpi/)
[usb polling rate](https://blog.codinghorror.com/tag/usb-polling-rate/)
[microsoft habu](https://blog.codinghorror.com/tag/microsoft-habu/)
[logitech mx518](https://blog.codinghorror.com/tag/logitech-mx518/)
[logitech g5](https://blog.codinghorror.com/tag/logitech-g5/)
