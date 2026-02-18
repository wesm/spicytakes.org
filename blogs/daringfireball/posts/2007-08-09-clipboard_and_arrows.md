---
title: "Clipboard and Text Selection : iPhone :: Arrow Keys : Original Macintosh"
date: 2007-08-09
url: https://daringfireball.net/2007/08/clipboard_and_arrows
slug: clipboard_and_arrows
word_count: 1558
---


## 1.


Clearly, the single most vexing shortcoming of the iPhone is its lack of text selection and clipboard features. (I group them together because neither would be very useful without the other.)


I am not alone in thinking this. It’s hard to find an iPhone review that doesn’t mention this. The need is so obvious that I don’t just hope that Apple adds these features in a future iPhone software update, I pretty much expect them to.


But, I not only understand why they’re absent today, I can even see the argument that — while they’re essential — it’s *good* that the 1.0 iPhone shipped without them. And therefore, alas, why it might be a while before they appear.


The analogy that comes to mind is to [the keyboard](http://www.aresluna.org/attached/computerhistory/articles/macintoshbytereview/pics/photo3) on the [original Macintosh](http://en.wikipedia.org/wiki/Macintosh_128K), which had no arrow keys. The most commonly cited reason for this omission was that Apple wanted to force users to use the mouse, and not allow them to fall back on keyboard-centric habits forged on pre-Mac computers. But another reason was to force developers — *including themselves* — to design a system and apps that could be accessed entirely by mouse. Pre-Macintosh, how did you move up and down in a list? With arrow keys. How did you move the insertion point in a text editor? With arrow keys. By not even having arrow keys, there was no option but to design software meant to be used with a mouse.


I doubt there was any dispute that arrow keys were potentially useful and convenient. (Likewise for other prominent missing keys on the original Mac keyboard, like Esc and Forward Delete.) But sometimes if you *can* do without something, even something potentially useful, it’s worth it to try. Necessity is the mother of invention; constraints lead to creative solutions.


By giving users and developers only a mouse for movement, it forced them to learn the Mac way. The lack of cut/copy/paste on the iPhone likewise forces users, along with Apple’s iPhone development team, to do things the iPhone way, rather than the Mac way.1 If you have something in app A that you want to use in app B, the Mac way is to copy it from A and paste it into B. (Or, to drag it from A to B, but drag-and-drop is really just a shortcut for copy-and-paste.)


The iPhone way is different. For anything you might want to use in another app, Apple has tried to anticipate the common cases and make them directly available. You don’t copy a picture you took in the Camera app, switch to MobileMail, and paste it into a message; you tap the photo to bring up the toolbar, tap the “do something with this picture” button, and then tap the Email Photo button. You don’t copy a URL from MobileSafari, switch to Mail, and paste it into a message; you tap the URL, then click the Share button that appears. (Which button really should be labeled “Email”, unless and until it offers sharing options other than sending an email.)


All of the above examples are more convenient and more obvious than using copy-and-paste would be, even if it were available. The lack of copy-and-paste on iPhone is only a frustrating irritation, not a fatal flaw. But these direct shortcuts only scale so far; copy-and-paste can be used in infinite different ways.


The analogy between the iPhone’s missing clipboard and the original Mac’s missing arrow keys isn’t perfect, however. When Apple decided the Mac did indeed need arrow keys (with [the Mac Plus](http://en.wikipedia.org/wiki/Macintosh_Plus) in 1986), the solution was obvious: make the keyboard bigger and add arrow keys.


Adding text selection and clipboard commands to the iPhone, on the other hand, poses some very tricky UI design problems.


## 2.


One problem with any touch screen is that your fingers, while convenient and direct, are not precise. Instead of the single-pixel precision of a mouse or trackpad pointer (really — just one pixel of the cursor acts as the hot spot for clicking), you’ve got a (relatively) huge circle of “hot spot” pixels when you tap or drag with a fingertip.


The two main pointer tasks in a scrolling view of items — text, icons, pictures, whatever — are selecting items and scrolling the view. The most obvious pointer gesture for both tasks is the same: click/tap-and-drag. Alas, one gesture can only mean one thing at a time. The most obvious solution the iPhone designers could have chosen would have been to mimic the Mac paradigm: tap-and-drag in the content area to select a range of items, and display scroll bars at the edges of the screen for tap-and-drag scrolling.


There are two problems with the idea of using scroll bars on the iPhone. First, screen real estate is precious on a 3.5-inch display; persistent scroll bars would consume screen space that would be better used for displaying content. Second, it’s easier to use a scroll bar with a pixel-precise pointer like a mouse than it is with a finger — unless you make the scroll bar really wide. Making the scroll bars extra wide would help eliminate ambiguous taps where part of your fingertip is on the scroller and part is in the content area — but that would only exacerbate the screen real estate problem.2


Apple’s clever idea, solving both problems, was to eliminate scroll bars entirely, and instead use the tap-and-drag gesture for scrolling from anywhere in the content area of the screen. This makes scrolling easy, convenient — and, I swear, fun. It is, in fact, easier to scroll on an iPhone than on a Mac. You can do it with your thumb while holding the iPhone in either hand. It’s a huge [Fitts’s Law](http://www.asktog.com/columns/022DesignedToGiveFitts.html) win, yet leaves the entire screen available for the display of content.


The trade-off is that tap-and-drag is not available for selecting a range of text. I’m convinced this trade-off is worth it, if for no other reason than that I primarily use my iPhone for *consuming* — reading, viewing, listening, looking — far more than I use it for *creating*. Scrolling is important for reading; selecting is important for writing. Better for the iPhone to optimize for reading.


This is very similar to the trade-off Apple made regarding the keyboard: sure, a dedicated hardware keyboard would be better for typing than the iPhone’s soft keyboard, but take away the physical keyboard and give the extra space to screen, and you have a much better device for *consuming*. The iPhone keyboard is good enough, and the extra screen space is used to great effect for reading and watching video.


But unlike the keyboard trade-off, text selection on the iPhone isn’t just a little worse off, it’s non-existent. I’ve seen [dozens of ideas](http://kottke.org/07/07/new-iphone-features) regarding how it *could* be added, but still not one that jumps out for how it *should*. Best I can think of is some way to modify the tap-hold-then-drag gesture that currently brings up the magnifier for placing the insertion point. The other thought that’s occurred to me is that I’d be perfectly happy with word-wise, rather than character-wise, text selection on the iPhone. Even with the magnifier, character-level specificity is tricky with an imprecise finger for a pointer. Selecting words at a time — like you get with double-click-and-drag on the Mac — would solve most of my needs and would work much better with a finger.


And but then once you have a range of selected text, how would you invoke cut/copy/paste? On-screen [squiggle gestures](http://www.37signals.com/svn/posts/195-iphone-trails)? Possible, but it strikes me as too pie-in-the-sky, and, if I dare say so just five weeks in, un-iPhone-like. My best idea is a dedicated clipboard button on the keyboard; tap it and it displays a panel with Cut/Copy/Paste buttons, as applicable to the current context. (I’d gladly accept slightly smaller space bar and Return buttons in the bottom row to make room.) There would also have to be a Copy button that appears when you select text in a read-only view with no keyboard; a simple inline button attached to the bottom of the selection, sort of like the tooltip-style button that you use for rejecting auto-correct suggestions, would do.


Whatever Apple comes up with, it doesn’t have to be spectacularly clever. It could even be an off-by-default preference, like the [caps lock](http://www.ipodobserver.com/story/32479) feature, so as not to clutter up the screen for typical users. The 80/20 rule says you spend 80 percent of your time using 20 percent of the features. The genius of the iPhone design is that they’ve already covered the common side of the 80/20 rule. But without text selection and a clipboard, the uncommon side remains out of bounds.


---

1. I’ve never been one to yammer about Windows being a “rip-off” of the Mac, but insofar as the fundamentals of selecting text and invoking clipboard commands, the “Windows way” is the Mac way that debuted in 1984. ↩︎
2. The Palm OS uses Mac-style tap-and-drag selection and persistent scroll bars, but (a) a stylus is far more precise than a fingertip, so their scroll bars are thinner, not thicker; and (b) no one has raved about how cool the Palm OS is since the ’90s. ↩︎



| **Previous:** | [Fake Steve, Unmasked](https://daringfireball.net/2007/08/fake_steve_unmasked) |
| **Next:** | [C4[1] in a Nut](https://daringfireball.net/2007/08/c4_1_in_a_nut) |


PreviousNext