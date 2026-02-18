---
title: "When ‘Smart’ Cut/Copy/Paste Attacks"
date: 2006-04-26
url: https://daringfireball.net/2006/04/smart_cut_copy_paste
slug: smart_cut_copy_paste
word_count: 1394
---


If you’re young enough that your first computer was a Mac or a
Windows PC, you probably can’t fathom just how big a deal
Cut/Copy/Paste were when they were introduced as standard features
of all applications. Pre-Macintosh, it was generally quite tricky to
copy something from one program into another.1


C/C/P changed that. There were three great things about C/C/P, right
from the get-go:

1. It’s incredibly useful. Again, though, if you’re too young to
remember computing  before ubiquitous C/C/P, you probably can’t
help but take it for granted. It’s my generation trying to
appreciate color television.
2. It’s incredibly simple and obvious what it is and how it works.
Everyone “gets” C/C/P.
3. The three commands have perfect keyboard shortcuts (at least on
QWERTY keyboards.) Copy is the only one of the three that uses
the obvious mnemonic shortcut (⌘C on the Mac, Ctrl-C on
Windows and on open source Windows rip-offs). ⌘X for Cut
feels right, though — there’s something that feels *X*-y about
“cutting” something; plus, the X key is conveniently located
right next door to C.
So those two shortcuts were fairly obvious; the genius decision
was using ⌘V for Paste. There’s absolutely nothing *V*-y
about “pasting”. But the reason it works so well as a shortcut
is that the action of pasting is so strongly related to the
actions of cutting and copying that the shortcut seems to demand
an adjacent position on the keyboard. Apple even reinforced this
relationship with the commands’ order in the Edit menu: Cut,
Copy, Paste; X, C, V.
[**Update:** Over a dozen readers have already emailed me to
suggest that there *is* something *V*-y about pasting: that 
the shape of the letter V suggests the upside-down caret
editing mark used to indicate a place of insertion. That had
never occurred to me, but it’s a reasonable mnemonic.]
And that other brilliant “*you goddamn kids probably can’t
believe we ever got along without it*” standard Edit menu
command, Undo, fits right into this order. It’s the Z key’s
location on the keyboard that makes ⌘Z feel so natural for
“undo”.2


C/C/P has evolved a bit over the years, but in large part remains
the same as it was on the original Mac. These three commands really
are self-explanatory. They do exactly what you expect them to.


Except, now, when they don’t.


A few weeks ago I noticed that most NSTextView-based apps now use a
rather annoying “smart” C/C/P implementation.3 [NSTextView](http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/ObjC_classic/Classes/NSTextView.html) is the standard built-in
text-editing control in Cocoa, so this applies to most — but not
all — Cocoa applications that allow you to edit text. The app I
noticed it in is [MarsEdit](http://ranchero.com/marsedit/), but it’s also present in TextEdit, so
feel free to use TextEdit if you want to play along at home.


Here’s an example.


Start with this text:


```
<b></b> foo

```


Select the word “foo” by double-clicking on it, then invoke Cut.


The first bit of “smartness” here is that the trailing space after
the “</b>” is removed along with the word “foo”, even though it
wasn’t part of the selection.


Now place the insertion point between “<b>” and “</b>”. Paste.


What I expect is:


```
<b>foo</b>

```


But what I actually get is:


```
<b> foo </b>

```


I find this infuriating.


What’s worse though, is that if you go back to the beginning:


```
<b></b> foo

```


and select “foo” by clicking and dragging across the three letters
comprising the word, then you don’t get any of this “smart” C/C/P
behavior. The trailing space after the “</b>” isn’t removed when you
cut, and when you paste, it doesn’t add any unwanted spaces before
or after the pasted text.


## Technical Interpolation on the Word-Selection Techniques That Trigger ‘Smart’ C/C/P


I use a custom [DefaultKeyBinding.dict](http://hcs.harvard.edu/~jrus/Site/Cocoa%20Text%20System.html) file
that allows me to add and adjust the default editing shortcuts for
NSTextView and NSTextView-derived editing fields. One of my entries
in that file binds Ctrl-L to the `selectWord:` selector:


```
"^l"  =  "selectWord:";

```


This means that when I type Ctrl-L, it selects the current word,
where “current word” means whatever word the insertion point is
adjacent to or within — pretty much exactly as though I’d
double-clicked the mouse cursor on the exact spot where the
insertion point is.4


If I use this keyboard shortcut to select a word, I also get the
“smart” C/C/P behavior when I cut the selection and when pasting it
subsequently. If I use regular keyboard text-selection keystrokes,
such as Shift-Arrow or Shift-Option-Arrow, then I get the regular
old-fashioned “just cut the selection and don’t do anything fancy
regarding surrounding spaces” C/C/P behavior.


## Word to the Wise


So the point here is that you get very different C/C/P behavior
depending upon *how* you make your selection. Double-clicking with
your mouse (or using a shortcut based on NSTextView’s `selectWord:`
selector) puts you into a word-wise selection mode, and selections
made in this mode are treated differently than normal selections.


Is word-wise selection a shortcut, or is it an entirely different
action than regular click-and-drag selection? I say it’s a shortcut,
and I think that’s certainly how most users — especially the vast
non-technical majority — think.


But this Cocoa “smart” C/C/P behavior forces you, the user, to think
of them as different actions, and to think that, you have to
understand what’s going on. And because most users clearly have no
idea that “word-wise” selection is a different mode than normal
selection, the result is that from most users’ perspective, this
“smart” C/C/P behavior seemingly kicks in at random.


I.e. the worst part about this isn’t the “smart” C/C/P behavior
itself, which I find irritating but which let’s concede for the
moment might conceivably be deemed useful by some. (Obviously,
someone at Apple thinks it’s useful.) The worst part is that unless
you understand that word-wise selection puts you into a special
mode, the “smart” C/C/P behavior *seems to kick in at random*.
Sometimes spaces are removed and added automatically, sometimes they
aren’t.


Features that seem to kick in at random are bad features.


In this case, Apple has taken a very simple, completely obvious
feature — a feature that almost every user completely understood —
and turned it into something governed by a complicated and
undocumented set of rules that most users don’t even know exist.
They’ve exchanged the elegant simplicity of traditional C/C/P for
the very marginal benefit of sometimes having word-bordering spaces
taken care of for you automatically.


“Smart” editing features are often more trouble than they’re worth.
Many of the common complaints about Microsoft Word, for example,
revolve around the on-by-default features where it gets too smart
for its own good. (Remember [Clippy](http://www.microsoft.com/presspass/features/2001/apr01/04-11clippy.mspx) the “I see you’re trying to
write a business letter” animated paperclip from Office 97? Or just
try to enter a URL in Word without having it automatically turned
into a blue underlined hyperlink.)


Once software starts down this path of guessing what it is the user
is trying to do, and then doing something special based on that
guess, it must guess correctly nearly every time, because the times
when it guesses wrong are so annoying that they far outweigh the
extra convenience of the times when it guesses right.


Software that eschews the clever for the obvious — in this case,
using good old-fashioned “what you see selected is what you get”
C/C/P behavior — will always do exactly what the user expects.
That’s what people mean when they talk about *intuitive* software
design.


---

1. Unix command-line pipes count as “tricky”, you nerd. ↩︎
2. This also freed up ⌘P for Print and ⌘U for Underline. ↩︎
3. I’ve only noticed this “smart” C/C/P behavior recently, but for all I know, it’s been around for years, maybe even dating back to NextStep. If it has been around for a while, I suspect the reason I didn’t notice it until now is that I do most of my text editing in BBEdit and Mailsmith, which aren’t based on NSTextView, and even when I am using NSTextView-based text editing apps, ones like Xcode and SubEthaEdit [suppress this feature](http://developer.apple.com/documentation/Cocoa/Conceptual/TextEditing/Tasks/Subclassing.html#//apple_ref/doc/uid/20000937-85719). ↩︎
4. A while back I published a [“Select Word” AppleScript for BBEdit, TextWrangler, and Mailsmith](http://daringfireball.net/2003/09/select_word_script_for_bbedit) which implements this feature for those apps. ↩︎



| **Previous:** | [Cringely’s Machinations](https://daringfireball.net/2006/04/cringelys_machinations) |
| **Next:** | [More on NSTextView’s ‘Smart’ Cut/Copy/Paste](https://daringfireball.net/2006/04/more_smart_cut_copy_paste) |


PreviousNext