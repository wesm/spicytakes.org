---
title: "LCD Progress"
date: 2006-12-13
url: https://blog.codinghorror.com/lcd-progress/
slug: lcd-progress
word_count: 1467
---

After revisiting my [ongoing three monitor obsession](https://blog.codinghorror.com/joining-the-prestigious-three-monitor-club/) recently, I was compelled to upgrade my current mongrel mix of varying LCD monitor brands and sizes. I settled on three 20" [Samsung 204B](https://web.archive.org/web/20070106061354/http://review.zdnet.com/Samsung_SyncMaster_204B/4505-3174_16-31676719.html) panels.


Standardizing on a single type of monitor in a multiple monitor configuration has obvious advantages in color consistency and uniform sizing. But LCD technology has also advanced quite a bit since my last LCD purchase. Here’s a small chart outlining the relevant specs of every LCD panel I’ve ever owned:

kg-card-begin: html


|  | **Samsung 191T** | **Rosewill R910J** | **Samsung 213T** | **Samsung 204B** |
| Vintage | Mid 2003 | Early 2005 | Early 2005 | Late 2006 |
| Size | 19" | 19" | 21.3" | 20" |
| Price Paid | $660 | $320 | $840 | $350 |
| Resolution | 1280x1024 | 1280x1024 | 1600x1200 | 1600x1200 |
| Brightness | 250 cd/m2 | 250 cd/m2 | 250 cd/m2 | 300 cd/m2 |
| Contrast | 500:1 | 600:1 | 500:1 | 800:1 |
| Viewing Angle | 170 | 170 | 170 | 160 |
| Response time | 25 ms | 25ms | 25ms | 5ms |


kg-card-end: html

Yes, there are minor brightness and contrast bumps. But more importantly, there’s been **a huge improvement in response time**. This addresses one of the [key criticisms of LCD monitors](https://web.archive.org/web/20070610093813/http://techreport.com/reviews/2002q4/lcds/index.x?pg=1):


> The liquid crystals in an LCD have to change their molecular structure to manipulate light, and that’s not a speedy process. As a result, LCD pixels respond much slower than what you may be used to on a CRT monitor, and that can cause ghosting and streaking, especially at high frame rates. The pixel response time of LCDs has improved dramatically over the years, but CRTs still have the edge. What’s most worrying about pixel response times, however, is that LCDs with similar pixel response time specs don’t always show the same performance in the real world. It’s really something you have to check for yourself.


That was written in 2002. LCDs are larger and cheaper now, and getting larger and cheaper every day. The improvement in response time makes watching video and gaming on LCDs nearly equivalent to a CRT. Worries about dead pixels are generally a thing of the past, too. It’s fair to say that LCDs have won the hearts, minds, and wallets of the public in 2006. It’s difficult to find places that even *sell* CRTs these days.


I’m glad the era of the CRT is finally over. Not just because LCDs are more svelte and power efficient, but also because LCD monitors are much less finicky than CRT monitors. **Getting great image quality with an LCD is dead simple. **You only need to do three things:

1. **Always use the DVI port to connect your LCD.**
The DVI port is digital, so you get a perfect connection to the LCD every time. Using a VGA port with an LCD is downright pathological – it means you’re converting the digital bits inside your video card to an analog video signal, then converting the analog video signal *back* to digital bits inside the LCD. You open yourself up to a whole host of nasty analog conversion issues along the way. Don’t do this! Use the DVI port! If you own a video card that doesn’t have two DVI ports, it’s time for a new video card.


![](https://blog.codinghorror.com/content/images/2025/05/image-444.png)

1. **Set your monitor’s refresh rate to 60 Hertz.**
 [Refresh rate](http://en.wikipedia.org/wiki/Refresh_rate) has no real meaning to a LCD, but it can still cause problems if it’s set to anything higher than 60 hertz. This ought to be set automatically when you connect a LCD panel, but it never is in my experience. So go in and lock the refresh rate down to 60 hertz.


![](https://blog.codinghorror.com/content/images/2025/05/image-445.png)

1. **Set the display to the maximum native resolution. **
LCDs work best at their native resolution – when there is one pixel on the LCD for every pixel on the screen. If you run a 1600x1200 LCD panel with a 1280x1024 desktop, you’ll get a blurry, upsized image instead of the perfect digital clarity LCDs are capable of. The maximum native resolution is usually the maximum resolution available in the display dialog, but double check your monitor's manual if you’re unsure. LCDs should look *perfect*. If it looks blurry at all, either you’re using an analog VGA input, or you’re using the wrong resolution.


The digital connection between PC and LCD is about as good as it gets, right out of the box. Contrast this with the experience of hooking up a new CRT: to get the best image quality, you had to tweak the refresh rate, the image sizing, the pincushion adjustment, and a half-dozen other tedious, fiddly little analog settings.


But even with the refresh rate issue largely addressed, LCDs do have a few other display peculiarities that linger on:


> **Viewing angle. **When viewed from the side, above, or below, images on LCD monitors become noticeably darker, and colors start to get washed out. CRTs, on the other hand, can be viewed from extreme angles with little loss in actual picture quality. Admittedly, there are few areas where viewing angle makes a big difference for end users, but the limitation is worth noting. If, for example, you want to watch a DVD on your LCD with a group of friends, everyone is going to have to get real cozy with each other on the couch to see things properly. Limited viewing angles might not be a bad excuse to get a little closer to your date, but your buddy that’s just over to watch Office Space may object to you rubbing up against his leg like that.
> **Color reproduction. **Although LCD screens claim support for 32-bit color, the displays themselves often aren’t capable of accurately reproducing *all* 16.7 million colors common 32-bit graphics modes. With a properly calibrated LCD, a casual user probably won’t notice the difference, but the limitation will probably give graphics designers fits.
> **Contrast ratio.  **LCDs are back-lit whenever they’re on, which means that TFT panels have to orient the liquid crystals to block light if they want to display black. Some light inevitably manages to seep through the cracks, which limits a screen’s ability to display a true black.


Some of these peculiarities are only of interest to hardcore graphic designers. I’m assuming that most modern LCDs are capable of displaying the full 32-bit range of color by now. Regardless, color calibration remains as much [an art as a science](https://web.archive.org/web/20111019071024/http://reviews.cnet.com/4520-6501_7-5143365-1.html), and adjusting colors is difficult on LCDs. I’ve also noticed backlight problems on every LCD I’ve owned, including the new models that just arrived. Blacks are never quite as deep as they would be on a CRT. And the backlighting is never perfectly uniform. I tend to see gradations in color and brightness on LCDs where there shouldn’t be any. As for viewing angle, this is more of a problem for LCD televisions than monitors. In computing scenarios, we tend to sit much closer to the monitors, and in a fixed location. If you’re a hardcore graphic designer, you can buy extremely high end, extremely expensive LCD monitors which attempt to resolve the color and uniformity problems endemic to most LCDs. But these specialty monitors do nothing for viewing angle, and they tend to sacrifice response time, making the ghosting and streaking problems even worse.


**Is it possible to calibrate a LCD?** You can get some ideas of what you might want to calibrate in CNET’s description of their [LCD monitor testing methodology](https://web.archive.org/web/20061230013514/http://reviews.cnet.com/Labs/4520-6603_7-5098394-1.html). Software like [Displaymate](http://www.displaymate.com/enduser.html) or [MonitorTest](http://www.passmark.com/products/monitortest.htm) can even walk you through the process. But the earlier good news – that LCD displays generally don’t need to be adjusted to produce good image quality – is also the bad news here. There’s not much you *can* adjust on a digitally connected LCD, other than the brightness and color temperatures. But that’s generally enough to [calibrate the essentials](http://www.normankoren.com/makingfineprints1A.html): brightness and gamma.


After you’re done calibrating, it’s time to clean all that dust off your LCD. I’ve been wary of cleaning my LCD panels, because I’m afraid of damaging the anti-glare or glossy (laptop) coatings. Soap and water leaves massive streaks, and caustic window cleaners are clearly out. I was recently turned on to the [Monster ScreenClean display cleaning kit](http://www.amazon.com/exec/obidos/ASIN/B000068P8W/), which works wonderfully. It cleans almost effortlessly without streaks, and it’s a screen-friendly non-alcohol formulation. It’s almost like screen lube.


LCDs still have a way to go before they're *perfect* substitutes for CRTs. With the recent industry advances in refresh rate, at least LCDs no longer have any glaring weaknesses. Here's hoping that improvements continue to keep pace in in viewing angle and backlighting.

[lcd](https://blog.codinghorror.com/tag/lcd/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[monitor configuration](https://blog.codinghorror.com/tag/monitor-configuration/)
[color consistency](https://blog.codinghorror.com/tag/color-consistency/)
[display technology](https://blog.codinghorror.com/tag/display-technology/)
