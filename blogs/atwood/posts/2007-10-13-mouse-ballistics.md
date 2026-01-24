---
title: "Mouse Ballistics"
date: 2007-10-13
url: https://blog.codinghorror.com/mouse-ballistics/
slug: mouse-ballistics
word_count: 1718
---

Let me be completely honest with you. I have a [full-blown mouse fetish](https://blog.codinghorror.com/my-mouse-fetish/). I’ve owned every single major mouse model from Microsoft and Logitech since the bad old days of the original Microsoft “Dove bar” mouse, and the Logitech MouseMan. I remember quite clearly bringing home my first mouse, an add-on for my Apple //c, and demonstrating this novel method of input to friends. I’ve been obsessing over these essential input devices since way before the days when USB was just a glint in Intel’s collective eye; I have more than my share of mousing experience.


These days, I can’t claim experience with every mouse under the sun; there are too many models out there. Mice have long since split into two distinct family trees: premium “performance” mice for gamers and enthusiasts; less expensive vanilla models for everyone else. As an enthusiast and a gamer, I’ve followed the enthusiast mouse family tree with great gusto. My current mouse of choice is the [Microsoft Habu](http://www.amazon.com/exec/obidos/ASIN/B000H16G3W). But that was way back in March. Since then two very interesting new models have emerged.


The [Microsoft Sidewinder Mouse](http://www.amazon.com/exec/obidos/ASIN/B000TTQFIS):


![](https://blog.codinghorror.com/content/images/2025/03/image-231.png)


The [Logitech G9 Mouse](http://www.amazon.com/exec/obidos/ASIN/B000UHE8Y2):


![](https://blog.codinghorror.com/content/images/2025/03/image-232.png)


I’ve now used both models for a few days, long enough to generate some informed opinions. They do have a quite a few things in common, things I’d consider relatively standard for current generation enthusiast mice:

- Five buttons (left, center, right, back, forward)
- Weight cartridges for adjustable “heft”
- Textured aluminum scroll wheels
- Hardware DPI adjustable “on the fly” with visual indicators
- Oversize glide pads on the bottom
- Mouse settings are permanently stored in on-board firmware


Each model also has a few unique features of its own:

kg-card-begin: html


| Microsoft Sidewinder | Logitech G9 |
| LED display that shows the current DPI setting
Glide pads can be swapped out; includes three sets, of varying slickness
Accessory box is weighted and doubles as cable anchor
Record macro button in front of the thumb buttons
Quick launch button on body
Vertical side button arrangement | Grip body can be swapped out; two different bodies are provided
DPI indicator LED color can be changed in software
Wheel can be switched between gear and frictionless modes
Offers one more DPI setting (4 total) |


kg-card-end: html

I noticed that neither of the [mouse wheels](https://blog.codinghorror.com/meet-the-inventor-of-the-mouse-wheel/) allow horizontal (left-right) scrolling. This is a good thing, because horizontal scrolling has always struck me as a dubious sort of feature at best. I think you’d need something other than a wheel to do it justice, more like a mini-trackball, and even then I’m not sure the complexity is worth it. How often do you *need* to scroll horizontally? I’d rather have a firm, bi-directional mouse wheel that’s locked to up-down, anyway.


So which one do I prefer? [My old Habu](https://blog.codinghorror.com/mouse-dpi-and-usb-polling-rate/) wasn’t exactly chopped liver – nor was the Logitech MX 518 I used before that – but on the whole, **I prefer the Logitech G9**. The Sidewider is arguably the more innovative model, but I have a few concerns with it:

1. It is a large mouse. The shape, while unusual, is plenty comfortable – but bulky. I prefer smaller mice in general.
2. The thumb buttons are in an unusual location. I’ve trained my thumb to move up, not forward. Every time I hit the “back” thumb button, I have to think and stretch a bit to reach it.
3. It’s a bit more awkward in general. Even with equivalent DPI and mouse speed/acceleration settings, I miss small click targets that I had no problem hitting with the G9 or the Habu. I don’t think it’s a technical limitation; it might be a consequence of the fit.


The G9, on the other hand, is a flawless mouse upgrade. I have no complaints whatsoever – it’s a solid step forward in every respect. Well, there is one minor niggle worth mentioning: the body, because it’s designed to be interchangeable, is a tiny bit loose when you pick up the mouse. If you frequently pick up the mouse to adjust the position, you might find that annoying. Also, the frictionless mouse wheel option is fun – it reminds me of the spinner control in classic arcade games like [Tempest](http://en.wikipedia.org/wiki/Tempest_(game)) – but useless in practice. It is an option, not a requirement, so I don’t deduct anything for that. I’ll stick with the Sidewinder at work for a while longer and see if I can adapt. I admire all the innovation at a relatively low price (for this type of enthusiast mouse, at least), but I am sorely tempted to [buy another G9](http://www.amazon.com/exec/obidos/ASIN/B000UHE8Y2).


During all this mouse testing, I spent a lot of time normalizing the pointer speed between the control panel mouse options and the DPI settings in the mouse’s hardware. I don’t think I realized until now **how essential it is to enable mouse pointer acceleration** for best pointer “feel” with *any* mouse. I strongly recommend that you double check to make sure this this feature is enabled. It’s available in Control Panel, Mouse, Pointer Options under “Enhance Pointer Precision.”


![](https://blog.codinghorror.com/content/images/2025/03/image-233.png)


What does Enhance Pointer Precision do? It’s a simple concept. When enabled, **the pointer moves more precisely when you move the mouse slowly, and more nimbly when you move the mouse quickly**. It decouples pointer movement ever so slightly from a basic 1:1 relationship with mouse movement, and introduces something called the mouse acceleration curve.


The translation from physical mouse movement to pointer movement is more sophisticated and more subtle than you might think. It’s all documented in an excellent [Microsoft article on mouse ballistics](https://web.archive.org/web/20071023210409/http://www.microsoft.com/whdc/device/input/pointer-bal.mspx). It introduced me to the amusing concept of the *mickey*: the smallest unit of measurement that the mouse’s hardware can produce.


Let’s think about this like programmers. If it was our job to translate mouse mickeys into pointer movements, how would we do it? Our first order of business is to figure out how fast the mouse is moving on the table or mousepad – the mouse *velocity*.


![](https://blog.codinghorror.com/content/images/2025/03/image-234.png)


The accuracy of the mickeys coming from our mouse is strongly influenced by the bus update rate. The math proves it. I talked about this in an earlier post on [Mouse DPI and USB Polling Rate](https://blog.codinghorror.com/mouse-dpi-and-usb-polling-rate/). The good news is that fancy enthusiast mice always override the default 125 Hz USB update rate. Both of these mice bump it up to 500 Hz as soon as they’re plugged in, which I verified using the Direct Input Mouse Rate tool.


The number of mickeys/inch is similarly influenced by the capabilities of the mouse’s sensor hardware, also known as DPI. It should more accurately be called MPI, **mickeys per inch**. A “dot” isn’t a dot at all; it’s a completely arbitrary unit, nothing more than the smallest unit of movement that the hardware can measure. The Sidewinder ranges from 200 DPI to 2000 DPI; the G9 from 200 DPI to 3200 DPI. This is dynamically switchable via the buttons on the mouse, and configurable in software as well. Don’t get hung up on the fact that the Sidewinder “only” goes up to 2000 DPI; the packets going over the wire only allow a mickey size between 0 and +127, so there’s a practical limit on how precise you can be.


Now that we have mouse velocity in the physical world, let’s determine how that will map to *pointer* velocity on the virtual world of our screen.


![](https://blog.codinghorror.com/content/images/2025/03/image-235.png)


Screens are bounded by obvious, concrete physical limitations. Refresh rate is typically fixed at 60 Hz for modern LCD displays. Screen resolution varies from 800 x 600 to astronomically huge for those that can afford 30" displays, but [the DPI ranges](https://blog.codinghorror.com/where-are-the-high-resolution-displays/) are fairly similar for most monitors.


Let’s try plugging in some typical values into our formulas:


Vmouse = 3 mickeys * 500 Hz / 1600 DPI = 0.9375 inches/sec
Vpointer = 3 mickeys * 60 Hz / 80 DPI = 2.25 inches/sec


You can immediately see the disconnect – **1 inch of physical mouse movement resulted in 2.25 inches of screen pointer movement**. There’s a physical to virtual gain of 2.4x. Without the mouse acceleration curve, this is as sophisticated as it gets. We might use a simple multiplier based on the pointer speed slider, but that’s about it. The relationship is linear. We’re doing a basic one to one mapping.


But with “Enhance Pointer Precision,” we use a variable curve to determine how far the pointer moves for any given mouse speed. The different colored curves shown here represent different values of the pointer speed slider with acceleration enabled.


![](https://blog.codinghorror.com/content/images/2025/03/image-236.png)


It is possible to edit these curves via the `SmoothMouseXCurve` and `SmoothMouseYCurve` registry settings, but there’s absolutely no documentation I could find on these settings, so be careful. Getting the curve right is crucial. According to the article, the mouse acceleration curves in Windows were determined by a usability study. For example, many people dislike the default [mouse acceleration curve in OS X](http://db.tidbits.com/article/8893):


> So what’s wrong with Mac OS X’s mouse acceleration curve? Simply put, it’s the wrong shape. For mouse motion to feel natural (at least for most people), the curve has to start by moving upward fairly moderately, then gradually flattening out as the value of X increases. Mac OS X’s, curve, however, starts off by being too steep, staying too steep for too long, and then flattening out too abruptly. In practical terms this means that, frequently, as a user tries to use the mouse to move the pointer from point A to point B, the pointer motion feels sluggish. The user then tries to compensate for the sluggishness by moving the mouse faster, and the pointer suddenly goes flying across the screen and overshoots point B. A comfortable and useful curve is actually shaped like a curve. Mac OS X’s curve, however, is shaped more like a cliff.


Windows may have better curves, as long as that “Enhance Pointer Precision” checkbox is ticked.


Who knew mouse ballistics could be this sophisticated? Heck, who knew that mouse ballistics even *existed* until now? Experiment with the “Enhance Pointer Precision” setting for yourself, but **I believe it should always be enabled –** it results in mouse pointer movement most people will find both easier to control and more accurate.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[peripherals](https://blog.codinghorror.com/tag/peripherals/)
[mice](https://blog.codinghorror.com/tag/mice/)
[gaming](https://blog.codinghorror.com/tag/gaming/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
