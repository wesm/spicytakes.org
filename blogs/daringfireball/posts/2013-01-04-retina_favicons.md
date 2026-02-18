---
title: "How to Create Retina-Caliber Favicons"
date: 2013-01-04
url: https://daringfireball.net/2013/01/retina_favicons
slug: retina_favicons
word_count: 550
---


A few months ago I decided to recreate this website’s [favicon](http://en.wikipedia.org/wiki/Favicon) to support retina-caliber displays. I found this trickier to accomplish than I anticipated, mainly due to a dearth of good ICO-savvy icon creation tools.


Old (non-retina) favicons are 16 × 16 px; a retina favicon is thus 32 × 32 px. The lazy way to support retina is to replace your old 16 px favicon.ico file with a 32 px file, and allow non-retina browsers to scale the image. The proper solution, however, is to create a single favicon.ico file containing two icon resources: one 16 × 16, the other 32 × 32. ICO files support other resolutions as well, but I see no practical utility in doing so.1


The app I found that works best is [Icon Slate](http://www.kodlian.com/apps), by Kodlian. It costs $5 in the Mac App Store and is worth every penny. It’s very simple. First, create your 16 × 16 and 32 × 32 px icons in the image editing application of your choice — Acorn, Pixelmator, or Photoshop probably. Export each icon size to its own PNG file. It doesn’t matter what you name them.


Next, create a new project in Icon Slate. Change the build settings to output only ICO (it defaults to outputting both ICO and ICNS). Drag the PNG files for your 16 and 32 px icons into the corresponding image wells in the project window. Ignore the other various icon sizes. Build. That’s it — you should now have a favicon.ico containing two icon resources, one for non-retina and one for retina.


---


I found no other tool that suited my needs. Apple has a free developer tool named [Icon Composer](http://www.google.com/search?q=apple+icon+composer) that seemingly does what we want (pretty much the same thing as Icon Slate — with drag-and-drop targets for images edited elsewhere), but the resulting ICO files don’t render in Chrome and apparently don’t render properly on Windows.


[iConvertIcons](http://iconverticons.com/) doesn’t do multi-resource ICOs. Neither does [Image2Icon](https://itunes.apple.com/us/app/image2icon/id403202957?mt=12). There’s a command line tool named [png2ico](http://www.winterdrache.de/freeware/png2ico/) but it doesn’t handle alpha channel transparency, apparently by design, so it’s only suitable for full-frame icons.


[X-Icon Editor](http://www.xiconeditor.com/) is a free web app recommended by Thomas Fuchs in his otherwise excellent [Retinafy Your Website flowchart](http://mir.aculo.us/2012/06/26/flowchart-how-to-retinafy-your-website/), but the problem I found with it (other than the inherent clunkiness of a web app in general) is that it did awful things to colors — the colors in the ICO files it generated did not match the colors in my source PNG files.


---

1. Most websites with retina-caliber favicons do exactly what I recommend here: a single ICO file with two icon resources, 16 and 32 px. [Apple’s](http://apple.com/favicon.ico), though, is a weird duck. Theirs has *four* resources: two each at 16 and 32 px dimensions. Opening it in Preview shows all four resources; I’m not aware of any other icon display app that isn’t confused by multiple resources of the same pixel dimensions. The first two icons in Apple’s file use alpha channels, but the second two seem to have hard-coded anti-aliasing artifacts. Not sure how they made this or what the extra resources are for, compatibility-wise. I presume ancient versions of Internet Explorer. ↩︎



| **Previous:** | [A Big Misunderstanding](https://daringfireball.net/2012/12/big_misunderstanding) |
| **Next:** | [The Trend Against Skeuomorphic Textures and Effects in User Interface Design](https://daringfireball.net/2013/01/the_trend_against_skeuomorphism) |


PreviousNext