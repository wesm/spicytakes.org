---
title: "Scuttlebutt Regarding Apple’s Cross-Platform UI Project"
date: 2018-04-30
url: https://daringfireball.net/2018/04/scuttlebutt_regarding_ui_project
slug: scuttlebutt_regarding_ui_project
word_count: 603
---


Back in late December, Mark Gurman published an intriguing report at Bloomberg [regarding a secret cross-platform project at Apple](https://www.bloomberg.com/news/articles/2017-12-20/apple-is-said-to-have-plan-to-combine-iphone-ipad-and-mac-apps):


> Starting as early as next year, software developers will be able
> to design a single application that works with a touchscreen or
> mouse and trackpad depending on whether it’s running on the iPhone
> and iPad operating system or on Mac hardware, according to people
> familiar with the matter. […]
> Apple is developing the strategy as part of the next major iOS and
> macOS updates, said the people, who requested anonymity to discuss
> an internal matter. Codenamed “Marzipan,” the secret project is
> planned as a multiyear effort that will start rolling out as early
> as next year and may be announced at the company’s annual
> developers conference in the summer. The plans are still fluid,
> the people said, so the implementation could change or the project
> could still be canceled.


I wrote [an extensive piece speculating on what it might really mean](https://daringfireball.net/2017/12/marzipan).


This “Marzipan” rumor got a lot of people excited. But Gurman’s report is so light on technical details that the excitement is based mostly on what developers hope it could mean, not what’s actually been reported. The less specific the rumor, the easier it is to project your own wishes upon it. And, oddly perhaps, we haven’t seen any additional rumors or details about this project in the four months since Gurman’s original report.


I’ve heard a few things, from first- and second-hand sources. Mostly second-hand, to be honest, but they’re all consistent with each other.


**The Name:** There is indeed an active cross-platform UI project at Apple for iOS and MacOS. It may have been codenamed “Marzipan” at one point, but if so only in its earliest days. My various little birdies only know of the project under a different name, which [hasn’t leaked publicly yet](https://twitter.com/gruber/status/991122089557004288). There are people at Apple who know about this project who first heard the name “Marzipan” when Gurman’s story was published.


**What Is It?** I don’t have extensive details, but basically it sounds like a declarative control API. The general idea is that rather than writing classic procedural code to, say, make a button, then configure the button, then position the button inside a view, you instead declare the button and its attributes using some other form. HTML is probably the most easily understood example. In HTML you don’t procedurally create elements like paragraphs, images, and tables — you declare them with tags and attributes in markup. There’s an industry-wide trend toward declaration, perhaps best exemplified by [React](https://reactjs.org/), that could be influencing Apple in this direction.


There’s nothing inherently cross-platform about a declarative control API. But it makes sense that if Apple believes that (a) iOS and MacOS should have declarative control APIs, and (b) they should address the problem of abstracting the API differences between UIKit (iOS) and AppKit (MacOS), they would tackle them at the same time. Or perhaps the logic is simply that if they’re going to create a cross-platform UI framework, the basis for that framework should be a declarative user interface.


**When:** I’m nearly certain this project is not debuting at WWDC 2018 in June, and I doubt that 2018 was on the table in December. It’s a 2019 thing, for MacOS 10.15 and iOS 13.1 I would set your expectations accordingly for this year’s WWDC.


---

1. My guess is this is all part of the updated UI for iOS 13 coming next year. ↩︎



| **Previous:** | [Design Plagiarism](https://daringfireball.net/2018/04/design_plagiarism) |
| **Next:** | [Lobe](https://daringfireball.net/2018/05/lobe) |


PreviousNext