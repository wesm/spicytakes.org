---
title: "I’ma Set It Straight, This Watergate"
date: 2012-01-24
url: https://daringfireball.net/2012/01/ima_set_it_straight_this_watergate
slug: ima_set_it_straight_this_watergate
word_count: 2248
---


Ed Bott, “[How Apple Is Sabotaging an Open Standard for Digital Books](http://www.zdnet.com/blog/bott/how-apple-is-sabotaging-an-open-standard-for-digital-books/4378)”:


> Apple’s behavior is a modern, sophisticated version of the
> “[embrace, extend, and extinguish](http://en.wikipedia.org/wiki/Embrace,_extend_and_extinguish)” behavior that got
> Microsoft in so much trouble in the 1990s: Enter a product
> category supporting a widely used standard, extend that standard
> with proprietary capabilities, and then use those differences to
> disadvantage competitors. (The strategy is even more effective if
> you have a dominant market position in another, related category
> that you can use for leverage. Think Windows in the 1990s, iPad
> in 2012.)


I agree with Bott that Apple is being competitive here, but disagree that it’s an example of embrace/extend/extinguish. Put another way, over the weekend [Bott called the iBooks Author  EULA “mind-bogglingly greedy and evil”](http://www.zdnet.com/blog/bott/apples-mind-bogglingly-greedy-and-evil-license-agreement/4360); I agree with the *greedy*, but not the *evil* or the mind-bogglingliness.


> So Apple, which claims to use the ePub format exclusively, has now
> created an incompatible, proprietary version of that format. And
> with iBooks Author they’ve added licensing terms that restrict
> what an author can do with the generated content.


This is why I disagree with the comparison to Microsoft’s embrace/extend/extinguish strategy: Apple isn’t calling the new iBooks Author format “ePub”. They never mentioned “ePub” during last week’s event. iBooks Author doesn’t use “ePub” anywhere in the user interface or documentation. The filename extension is ‘.ibooks’, not ‘.epub’. Arguing that Apple is following the embrace/extend/extinguish strategy implies that Apple was attempting to redefine “ePub” to mean “ePub plus Apple proprietary extensions”. Apple isn’t doing that. They’re very clearly presenting the output of iBooks Author as something new and proprietary to the iBooks Author.


Bott points to [this iBooks FAQ from Apple](http://support.apple.com/kb/HT4059), which states that the only formats supported by iBooks are industry-standard ePub and PDF. Given that the modification date on this FAQ is 22 December 2011, it seems clear that this is simply an outdated FAQ, not an attempt to describe the new iBooks format as ePub.


I’m not trying to be cute here. I understand that technically, under the hood, the iBooks Author output is standard ePub plus Apple proprietary extensions. But I don’t think it’s fair to say that Apple is attempting to confuse anyone in this regard. The under-the-hood similarities to ePub are an implementation detail. No casual user creating a work in iBooks Author should have any reason to believe they are creating an ePub file, or something that can be used anywhere other than in the iBooks app on an iPad.


I don’t disagree that Apple’s goal is for the proprietary iBooks format to become a de facto standard — for it to become popular and widely used and thus, because it only works on the iPad, further cement the iPad as the leading next-generation personal computing platform. I simply disagree that Apple is being in any way disingenuous or misleading about it. The only people who seem to be confused about iBooks Author’s relationship to ePub are technically-minded people who know exactly what ePub is and who have a vested interest in seeing the open standard become the de facto industry standard.


Bott writes:


> They also could have included the option to import ePub files. As
> a publisher and author myself, I would have welcomed that option.
> I could create a book using the industry-leading standard ePub
> format, for sale in any outlet, then import it into iBooks Author,
> add interactive elements, and sell an enhanced version in the
> iTunes Store for the same price.


What Bott is asking for here, to me, would have been a *more* embrace/extend/extinguish sort of move — to allow iBooks Author to open a cross-platform ePub book, make changes, and then save it in a proprietary format that can only be read in iBooks. It might have been a convenience to authors and publishers who already have ePub source files, but by not even allowing iBooks Author to import ePub, it only serves to emphasize that iBooks Author is not a general-purpose ePub or e-book tool. It is an iBooks tool.


> Apple, which uses the ePub standard as the core for iBooks, could
> easily have produced their free authoring tool so that it
> continues to support what they acknowledge is the
> “industry-leading standard.” The program could offer users a
> choice of output formats: a standard ePub file or a fully
> interactive iBooks file.


They could have, but they didn’t. And if they had, when exporting to standard ePub, the books would lose all of the formatting and interactive features that are exclusive to the iBooks format. Apple wants authors and publishers to use those features, because those features are what differentiates iBooks on the iPad from all other e-readers.


---


Bott’s on firmer ground with this follow-up piece: “[Some Standards Are More Open Than Others](http://www.zdnet.com/blog/bott/some-standards-are-more-open-than-others/4394)”, wherein he makes the case that Apple is a hypocrite for developing and promoting its own proprietary e-book format while serving as a member of the International Digital Publishing Forum, the trade group behind the ePub standard:


> OK, everyone, you got that? It’s just capitalism! Why should Apple
> care about other companies in the digital publishing industry? Let
> them go build their own tools and design their own formats!
> Except for one little thing. Apple is a [member in good standing of
> the International Digital Publishing Forum](http://idpf.org/membership/members), which identifies
> itself as the “Trade and Standards Organization for the Digital
> Publishing Industry.”
> As a member of the IDPF, Apple most certainly is on record as
> agreeing to do what Gruber thinks they don’t have to do: reduce
> the cross-platform burdens of the entire digital publishing
> industry.


There are an awful lot of companies on the IDPF members list, including at least a few that produce tools that generate digital publications in proprietary formats (e.g. Adobe and Quark, to name two that compete directly against iBooks Author).


On the one hand, iBooks, since its inception, has had best-of-breed support for the ePub standard, and all the regular books available for download and purchase through the iBookstore (i.e. every book other than the dozen or so made using iBooks Author which appeared in the store last week) are in standard ePub format. (Apple even requires books submitted to the store to pass ePub standard validation tests.) And Apple has made no mention of moving away from this support for ePub.


The question is, what does it mean to be a “good” member of IDPF: supporting ePub alongside any proprietary formats, or supporting ePub to the exclusion of any proprietary formats? Bott clearly sees it as the latter.


Put another way, if you’re a producer of ePub-formatted books and wish to remain so, your books are just as welcome in the iBookstore and just as well-rendered in iBooks as they were prior to Apple’s announcements last week.


To me, again, it’s like mobile web apps versus native apps on the iPhone. When the iPhone debuted in 2007, Apple declared that [the only way for third-party developers to write software for it](http://daringfireball.net/2007/06/wwdc_2007_keynote) was to write mobile web apps. Such mobile web apps were far more capable than mobile web apps on any other platform — but they were far *less* capable than the native Cocoa Touch apps Apple provided with the iPhone. In 2008, when Apple unveiled the App Store and native Cocoa Touch SDK, it didn’t drop support for mobile web apps. Indeed, mobile web app support in iOS has continued to improve, and today still exceeds the mobile web app support in any other OS. But the fact that mobile web apps on iOS remain far less capable than native App Store apps paints Apple as “anti-web” in the eyes of some critics.


I believe the new iBooks Author format is to iBooks as native App Store apps are to the iPhone, and that ePub is to iBooks as mobile web apps are to the iPhone: closed/proprietary/technically-superior/better-looking on one side, open/standard/cross-platform on the other side. I expect Apple to continue to support ePub the same way it has continued to support mobile web apps — as a second-class citizen compared to its own proprietary format, but still just as good as, if not better than, anyone else in the industry.


I don’t know enough about the collective politics of the IDPF to say whether this stance is contrary to the group’s goals or mores. If you see the goal of ePub as serving as an expressive, standard, cross-platform format for e-books, Apple remains fully on board with that. If you see the goal of ePub as serving as the *only* commercial e-book format — i.e. that all e-books should be cross-platform — I don’t see how you can argue that Apple was ever on board with that. There’s a big difference between arguing “*There should be a good standard for cross-platform books*” and “*All books should be based on a good cross-platform standard*”.


---


Lastly, Bott thinks I’ve slowly changed my mind over the last few days:


> The top defender is ace Apple-watcher John Gruber, who has been
> slowly and publicly changing his mind on the new iBooks format and
> accompanying license agreement over the past few days. First he
> said it was “[Apple at its worst](http://daringfireball.net/linked/2012/01/19/ibooks-author-eula).” And then he began backtracking.
> [First](http://daringfireball.net/linked/2012/01/19/unprecedented):
> The output of iBooks Author is, as far as I can tell, HTML5 —
> pretty much ePub 3 with whatever nonstandard liberties Apple saw
> fit to take in order to achieve the results they wanted. It’s
> not a standard format in the sense of following a spec from a
> standards body like the W3C…
> [Next](http://daringfireball.net/2012/01/ibooks_author_file_format):
> Apple’s concern is not what’s best for the publishing industry,
> and it certainly isn’t about what’s best for the makers of (and
> users of) rival e-book reading devices.
> [And most recently](http://daringfireball.net/linked/2012/01/23/glazman-responds):
> But again, Apple’s not in this game to reduce the cross-platform
> burdens of the publishing industry. If the publishing industry
> wants to reduce the number of formats it supports and the hassles
> of converting from one format to another, Apple’s pitch would be
> to go exclusive to the iBookstore.


There are two separate issues in play. First is the iBooks Author EULA, and its requirement that if you sell a book generated by the app, you must do so exclusively through the iBookstore. Second is the proprietary file format of the new iBooks Author and its relationship to ePub 3.


My “this is Apple at its worst” remark was regarding the EULA. That criticism still stands. I believe Apple should treat the output of iBooks Author as it does Mac apps: allow authors and publishers to choose to sell them through the iBookstore and/or to sell them on their own. I could even see Apple requiring books made with iBooks Author to be submitted to the iBookstore if they’re going to be made available for sale anywhere — just remove the exclusivity clause. I see no reason why the iBookstore would not succeed in the same way the Mac App Store has. I say this is Apple at its worst because Apple has chosen the path of exerting the most control.1 A little more flexibility on Apple’s part would do well for everyone, even Apple itself, as it would only further encourage the use of iBooks Author.


The other remarks of mine that Bott quotes are regarding the second issue — the *proprietary file format versus ePub* one — and my stance on that is largely unchanged. The only thing I believe I was wrong about is my initial conjecture that the output of iBooks Author is mostly or entirely expressed in HTML5. It is indeed largely based on ePub (and thus HTML5), [but significant aspects are not](http://daringfireball.net/linked/2012/01/23/ibooks-bjarnason). Here’s another snippet from my first piece Bott quotes from above:


> It’s not a standard format in the sense of following a spec from a
> standards body like the W3C, but it’s just HTML5 rendered by
> WebKit — not a binary blob tied to iOS or Cocoa. It may not be
> easy, but I don’t think it would be *that* much work for anyone
> else with an ePub reader that’s based on WebKit to add support for
> these iBooks textbooks.


I no longer believe that to be true. I think it would take significant effort for a competitor to render the output of iBooks Author with full or even near-full fidelity. All the more reason for Apple to remove or loosen the exclusivity clause of the EULA.


---

1. Actually, I take that back. Exerting the most control, they would disallow the free distribution of books generated with iBooks Author, and make it more like the iOS App Store. But such a restriction would completely contradict the role iBooks Author is intended to play with the new iTunes U, where individual teachers and professors are encouraged to use iBooks Author to produce their own courseware. What Apple has chosen is the path of exerting the most control while still supporting the new iTunes U. ↩︎



| **Previous:** | [On the Proprietary Nature of the iBooks Author File Format](https://daringfireball.net/2012/01/ibooks_author_file_format) |
| **Next:** | [The ‘Apple Should Be Worried If Anyone Else Has Any Success Whatsoever’ School of Thought](https://daringfireball.net/2012/02/apple_should_be_worried) |


PreviousNext