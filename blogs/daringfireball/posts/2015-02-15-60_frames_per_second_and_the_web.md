---
title: "60 Frames Per Second and the Web"
date: 2015-02-15
url: https://daringfireball.net/2015/02/60_frames_per_second_and_the_web
slug: 60_frames_per_second_and_the_web
word_count: 668
---


Faruk Ateş, in [a thoughtful piece regarding the new Flipboard website](http://farukat.es/journal/2015/02/708-how-flipboard-chose-form-over-function-their-web-version), which, because it eschews the DOM and builds the entire layout using the HTML5 `<canvas>` element, is not accessible:


> I’m also hopeful that Accessibility is the next big project to
> tackle for the engineering team. A 2.0 release, if you will.
> But more than anything, I am dismayed.
> I am dismayed that Accessibility was treated not even as a mere
> afterthought, but as something worth sacrificing *completely* for
> the sake of flashiness.
> I am dismayed that Flipboard’s leadership chose fancy but
> ultimately irrelevant animations over function, over purpose.
> And I am dismayed that people like John Gruber now think this
> solution by Flipboard is somehow “[a scathing condemnation of the
> DOM/CSS web standards stack](http://daringfireball.net/linked/2015/02/10/flipboard-web).”


When you build a website with traditional standard DOM techniques, you get accessibility “for free” more or less, and this is without question a good thing. I’ve been a proponent of accessibility for as long as I can remember. It does not follow, however, that what Flipboard chose to do is wrong.


It is true that Flipboard’s engineering decisions prioritize animation and scrolling performance above accessibility. That’s no secret — the title of their how-we-build-this post was “[60 FPS on the Mobile Web](http://engineering.flipboard.com/2015/02/mobile-web/)”. It does not mean they don’t care about accessibility. My understanding is that accessibility is coming — they’re working on it, but it isn’t ready yet.


As I see it, the only things Flipboard could have done differently:

1. Launch now, lack of accessibility be damned.
2. Wait some number of additional months to unveil this web version, so that it could debut with better accessibility.
3. Build the whole thing with standard DOM techniques.


Launching today (#1) does not postpone the eventual release of an accessible Flipboard.com (#2). Shipping is a feature.


If they had gone with choice #3, [by their own admission](http://engineering.flipboard.com/2015/02/mobile-web/), Flipboard never would have achieved 60 FPS animation and scrolling across all the devices they were targeting. You may disagree with their technical argument. Go ahead and build a Flipboard-esque website using the DOM to prove them wrong.


You may disagree that 60 FPS animation and scrolling is important. That’s a perfectly valid opinion — but it’s an opinion that is falling into antiquity. iOS raised the bar. We expect not just smooth scrolling and animation, but *perfect* animation and scrolling. A janky platform is now perceived by many as a junky platform. And complex animations and scrolling via the DOM are [janky](http://jankfree.org/).


I stand by my remark that Flipboard being unable to use the DOM to achieve this design is “a scathing condemnation of the DOM/CSS web standards stack”. The standard DOM/CSS stack is great for many things. Going forward, though, it needs to be great for building designs with iOS-caliber animation, scrolling, and touch responsiveness. Not only is the DOM/HTML/CSS stack not great at that, it’s incapable of it.


Blinded by ideology, oblivious to the practical concerns of *60-FPS-or-bust*-minded developers and designers, the W3C has allowed standard DOM development to fall into seemingly permanent second-class status. I almost tacked “on mobile” to the end of the previous sentence, but that shouldn’t be necessary. Mobile is all that matters going forward. The DOM has always been slow and cumbersome. CSS has always been an over-engineered, over-complicated academic exercise that largely ignores the practical needs and processes of working designers.


60 frames per second is not “would be nice”. It’s “must have”. And the DOM doesn’t have it. It’s not surprising that Flipboard’s workaround — the `<canvas>` element — [was invented by Apple](https://en.wikipedia.org/wiki/Canvas_element), as the basis for Dashboard widgets and potentially as the backdrop for the iPhone. But it’s damning that something Apple decided was too slow to serve as the basis for native iPhone apps is the best-performing backdrop for the mobile web.



| **Previous:** | [Dazzling Results](https://daringfireball.net/2015/02/dazzling_results) |
| **Next:** | [Thinking About the Split in Apple Watch Sales by Model](https://daringfireball.net/2015/02/apple_watch_split) |


PreviousNext