---
title: "More on NSTextView’s ‘Smart’ Cut/Copy/Paste"
date: 2006-04-27
url: https://daringfireball.net/2006/04/more_smart_cut_copy_paste
slug: more_smart_cut_copy_paste
word_count: 642
---


So with the [smart Cut/Copy/Paste thing](http://daringfireball.net/2006/04/smart_cut_copy_paste) yesterday, I
definitely did not mean to imply that I thought the general concept
of “smart” C/C/P was new. In a footnote, I wrote:


> I’ve only noticed this “smart” C/C/P behavior recently, but for
> all I know, it’s been around for years, maybe even dating back to
> NextStep. If it has been around for a while, I suspect the reason
> I didn’t notice it until now is that I do most of my text editing
> in BBEdit and Mailsmith, which aren’t based on NSTextView, and
> even when I am using NSTextView-based text editing apps, ones like
> Xcode and SubEthaEdit [suppress this feature](http://daringfireball.net/2006/04/smart_cut_copy_paste#fn3-2006-04-26).


What I meant here is that I wasn’t sure whether NSTextView had been
doing this dating back to NextStep, not that I wasn’t sure whether
NextStep originated the idea of trying to do something clever with
word-bordering spaces when you C/C/P.


A bunch of Mac apps have offered similar functionality over the
years,1 and the HIG has contained
a [section on “Intelligent Copy and Paste”](http://developer.apple.com/documentation/UserExperience/Conceptual/OSXHIGuidelines/XHIGUserInput/chapter_11_section_5.html#//apple_ref/doc/uid/TP30000361-TPXREF36) dating back at
least to 1992. The behavior prescribed by the HIG is sensible
enough, and for prose editing probably does do what the user wants
almost every time:


> If your application supports intelligent cut and paste, follow these
> guidelines:
> If the user selects a word or a range of words, the selection
> itself is highlighted, but spaces adjacent to the selection are
> not highlighted.
> When the user chooses Cut, if the character preceding the
> selection is a space, cut that space along with the selection.
> If the character preceding the selection is not a space, but the
> character following the selection is a space, cut that space
> along with the selection.
> When the user chooses Paste, if the character to the left or
> right of the current selection is part of a word (but not inside
> a word), insert a space before pasting.


Note, though, that the NSTextView implementation clearly contradicts
these guidelines. There’s nothing in the HIG regarding *how* you
make your selection — a selected word is a selected word, no matter
whether you selected it by double-clicking or by clicking and
dragging.


And as noted yesterday, my primary complaint isn’t with “smart”
C/C/P in general, but rather with NSTextView’s “*sometimes you get
it, sometimes you don’t, depending on how you made your selection*”
rules which govern when the feature kicks in.


Think of it this way. If while editing text you see this:


You ought to be able to know exactly what’s going to happen if you
hit ⌘X, but in Cocoa apps that use NSTextView’s smart C/C/P, you
can’t, because you have to know how the word “uncomfortable” was
selected. I.e instead of “what you *see* is what you get”, it’s
“what you *did* is what you get”, and the whole point of a GUI is
about what you see.


The point of “smart” C/C/P is, ostensibly, to free you from thinking
about word-bordering spaces before and after C/C/P. With
old-fashioned “non-smart” C/C/P, sure, you have to deal with
word-bordering spaces manually, but I think in practice, you get
used to doing so without even thinking about it, because you know
you have to do it every time. Cut a word, delete the extra space;
paste a word, hit the space bar.


With NSTextView’s implementation, however, you do have to think
about it — or at least most users do — because sometimes you get
the “smart” behavior, and other times you don’t.


---

1. Including BBEdit, which offered it as a preference for many years. It was consigned to the dustbin of history a few versions ago. ↩︎



| **Previous:** | [When ‘Smart’ Cut/Copy/Paste Attacks](https://daringfireball.net/2006/04/smart_cut_copy_paste) |
| **Next:** | [Aperture Dirt](https://daringfireball.net/2006/04/aperture_dirt) |


PreviousNext