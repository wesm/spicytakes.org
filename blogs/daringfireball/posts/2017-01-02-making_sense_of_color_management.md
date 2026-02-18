---
title: "Craig Hockenberry’s ‘Making Sense of Color Management’"
date: 2017-01-02
url: https://daringfireball.net/2017/01/making_sense_of_color_management
slug: making_sense_of_color_management
word_count: 992
---


When I was an incoming freshman at Drexel University in 1991, the school had a program, in collaboration with Apple, that allowed students to buy Macintosh computers at a significant discount. I had narrowed my choices to two: a Mac LC and a Mac SE/30. The SE/30 was significantly faster. But I wound up choosing the LC for one reason: the LC came with a color display, and the SE/30’s display was black and white. Even today, I love the original Mac’s 9-inch black and white display, but even then, just seven years after the Mac debuted, that love was nostalgic.


A color display was, for me, an irresistible draw.


The display on that Mac LC now sounds quaint. It measured only 12 inches diagonally (common for notebooks today, but the LC was a desktop), with 512 × 384 pixel resolution. A retina display it was not. And it could only display 256 colors at a time. Today that sounds ludicrous. In 1991 it sounded luxurious — most Macs were black-and-white and many PCs with color support could only show 16 colors at a time. Macs that could display “thousands” of colors cost thousands of dollars more.1


For a while, I was obsessed with [a Mac golfing game](https://tcrf.net/PGA_Tour_Golf_(Mac_OS_Classic)). (Exciting, right?) As a computer nerd and budding designer, I noticed immediately that the game’s graphics seemed too good to be true — the scenery on the golf courses was clearly better looking than what was possible with the system’s 256 color palette. I delved into it and learned that while my LC indeed could not display more than 256 colors at a time, the OS provided APIs that allowed an app to specify *which* 256 colors to display.2 The golf game, for obvious reasons, used a custom palette with way more greens than the system’s standard palette. “That’s clever”, I remember thinking. I also remember thinking that 256 colors no longer seemed like “a lot”.


A few years later, after I’d immersed myself in the online indie Mac developer/power user community, I became aware of a design studio that specialized in a delightfully specific niche: software icons. Their name said it all: [The Iconfactory](http://iconfactory.com/home/history). Soon, The Iconfactory started making their own apps, too, the user interfaces for which were just as exquisitely pixel-perfect as their icons. The Iconfactory’s developer was a very tall fellow named Craig Hockenberry.


---


Craig’s long been a good friend. So, when he asked me last year if I’d consider writing the foreword to a book he was writing about color management, I was honored.


*[Making Sense of Color Management](https://abookapart.com/products/making-sense-of-color-management)* came out last month. It is an excellent book — useful for both designers and developers who are trying to, well, make sense of the state of the art in color management. Here’s an example. You specify a certain exact RGB color in your CSS for a web page. Then you make a graphic for that web page, with the exact same RGB value for the background color. But when you put the graphic on the web page, the background colors don’t match up. But only in some browsers, on some platforms. What the hell is going on?


In this book, Craig tells us not just *what* to do, but *why*. It’s not merely a checklist of steps to follow blindly, but rather a foundation of knowledge. The famed physicist Richard Feynman believed that if he couldn’t explain a complex subject to an audience of first-year students, that meant he himself didn’t truly understand the subject. This book is proof that Craig now truly understands how modern color management works.


A few salient facts:

- It’s an e-book, and it costs only $8.
- You can read it in iBooks, Kindle, and as a PDF. You only have to buy it once.
- It’s only 91 pages long. It contains everything you need to know, and nothing you don’t.
- It’s published by A Book Apart, so unsurprisingly it’s well-edited and exquisitely-designed.


Color graphics have *never* been easy. As our technical capabilities have expanded (e.g. wide color gamut displays), so has the complexity involved in understanding how it all works. If you work in design or graphics, you should read this book.


**See also:** Craig’s blog post [announcing the publication](http://furbo.org/2016/12/09/making-sense-of-color-management/) of the book, and [the mini-site he created to accompany it](http://furbo.org/color). Last but not least, Craig and I discussed the book [a few weeks ago on my podcast](http://daringfireball.net/thetalkshow/2016/12/16/ep-176).


---

1. Back in the System 7 era of the 1990s, you could change the number of colors used by your display in the Monitors control panel. There were options like “Black and White” and numbers like 4, 16, and 256. After that, though, [the system’s actual labels for how many colors to display were “Thousands” and “Millions”](http://tmp.gallopinginsanity.com/Intuit_Mac_Training/Mac_OS_Changing_Settings.html#-Monitors%20and%20Sound%20CP). It’s one of those little details that made me love the Mac. 256 is a manageable number. 65,536 is not.
This preference for humane descriptions over technical descriptions lives on today in MacOS 10.12 Sierra’s Displays System Preferences panel. You can’t change the number of colors, but you can change the scale of the interface. If you have a retina display, rather than a list of pixel resolutions (e.g. 2560 × 1440), [you simply see five](https://daringfireball.net/misc/2017/01/sierra-displays-panel.png) side-by-side example icons, with “Larger Text” on the left, “More Space” on the right, and “Default” [somewhere in between](https://twitter.com/bzamayo/status/816103532382289920). ↩︎︎
2. I even remember the 4-character code for the resource type that specified the custom color palettes: “clut”, for “color look up table”. I don’t think there’s any classic Mac app that I have stronger nostalgia for than ResEdit. I probably haven’t used ResEdit in 15 years, but I feel like I could sit down in front of it and be right at home. ↩︎



| **Previous:** | [Regarding Uber’s New ‘Always’ Location Tracking](https://daringfireball.net/2016/12/uber_location_privacy) |
| **Next:** | [On Chuq Von Rospach’s ‘Apple’s 2016 in Review’, and the AirPort and Mac Pro Lineups in Particular](https://daringfireball.net/2017/01/von_rospach_apple_airport_mac_pro) |


PreviousNext