---
title: "Widescreen and FOV"
date: 2007-08-23
url: https://blog.codinghorror.com/widescreen-and-fov/
slug: widescreen-and-fov
word_count: 482
---

As far as I’m concerned, you can [never have enough pixels](https://blog.codinghorror.com/joining-the-prestigious-three-monitor-club/) on your desktop. Until a few years ago, buying a larger display meant buying a larger display in the same, standard 4:3 screen layout – 640 x 480, 800 x 600, 1024 x 768, 1600 x 1200, and so forth. **But widescreen monitors are increasingly popular**. It’s difficult to buy a larger monitor today without changing your aspect ratio to widescreen.


As the new owner of my very first non-4:3 widescreen monitor, I’m learning first hand that widescreen displays can be problematic in certain rendering contexts. The issue of **scaling pre-rendered content** to a widescreen display is a well-understood problem at this point; [non-linear stretching techniques](https://blog.codinghorror.com/media-center-2005-adds-non-linear-stretch/) work reasonably well.


But when **rendering dynamic 3D content**, things are a bit more problematic. I just purchased [the game Bioshock](http://en.wikipedia.org/wiki/Bioshock), which “supports” widescreen displays – but, in fact, it doesn’t. Here’s a screenshot of the same scene displayed in 1600 x 1200 (4:3), and in widescreen 1920 x 1200 (16:10).


![bioshock 1600x1200 overlaid with 1920x1200](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d948b970b-pi.jpg)


It’s wider, technically, but you actually *see less*. The sides are the same, but the top and bottom of the display is clipped away in widescreen. In effect, the viewport is zoomed in. This is what you *have* to do to get static, pre-rendered content to fit a widescreen format, because that content is immutable. But this is a terrible solution for dynamically rendered content in a 3D world. Instead, the developers should **increase the **[**field of view**](http://en.wikipedia.org/wiki/Field_of_view).


![fov (field of view) diagram](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d9495970b-pi.png)


If we turn down the FOV in Bioshock to something like 0.84 to accommodate our widescreen 16:10 aspect ratio, we **can see more of the world, not less**:


![Bioshock FOV comparison, 4:3 vs 16:10](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d94a0970b-pi.jpg)


With the adjusted FOV, the wider screen is used to display more of the scene on the left and right edges. Makes sense, doesn’t it? But this is not something you get for free – the [rendering engine *must* be programmed](https://learn.microsoft.com/en-us/windows/win32/dxtecharts/introduction-to-the-10-foot-experience-for-windows-game-developers?redirectedfrom=MSDN#aspect-ratio-and-widescreen) to allow and support changing the FOV.


**In multiplayer circles, a wider FOV is considered cheating.** If you can view more of the world than your opponent, then you might be able to see them coming before they see you. But this is a moot point for Bioshock; it’s a single-player game. It’s definitely possible to [go a little crazy with FOV](http://strlen.com/gfxengine/fisheyequake/compare.html) if you don’t have enough physical display size to justify the field of view you’ve chosen:


![Quake with a large FOV](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d94b5970b-pi.jpg)


It’s a tricky balancing act, and not many rendering engines get it right. That’s probably why there’s a [Widescreen Gaming Forum](https://web.archive.org/web/20071016040815/http://www.widescreengamingforum.com/wiki/index.php?title=Main_Page) dedicated to dealing with FOV and widescreen issues, along with at least one other website, [Widescreen Gamer](http://www.widescreengamer.com/). As the widescreen display format becomes increasingly popular, you can expect to run into this little rendering quirk eventually.

[aspect ratio](https://blog.codinghorror.com/tag/aspect-ratio/)
[widescreen monitors](https://blog.codinghorror.com/tag/widescreen-monitors/)
[display resolution](https://blog.codinghorror.com/tag/display-resolution/)
[screen layout](https://blog.codinghorror.com/tag/screen-layout/)
[dynamic 3d rendering](https://blog.codinghorror.com/tag/dynamic-3d-rendering/)
