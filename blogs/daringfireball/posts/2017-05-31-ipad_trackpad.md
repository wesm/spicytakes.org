---
title: "What If the iPad Smart Keyboard Had a Trackpad?"
date: 2017-05-31
url: https://daringfireball.net/2017/05/ipad_trackpad
slug: ipad_trackpad
word_count: 1458
---


Here’s an idea I tossed out [on the latest episode of The Talk Show](https://daringfireball.net/thetalkshow/2017/05/27/ep-191), while talking with Jim Dalrymple about what Apple might do with the iPad Pro: what if they added a trackpad to the Smart Keyboard? [David Chapman took the idea and made a quick mockup of what it might look like](https://twitter.com/DaveChap/status/869192781960499200). (I think the trackpad should be smaller than in his mockup — more like an older MacBook than a new MacBook, but his image conveys the general idea.)


I’m *not* talking about adding an on-screen mouse cursor to iOS for clicking and dragging. That’s a terrible idea. My loose idea for an iPad trackpad is based on a few things:

1. iOS’s trackpad-like mode for using the on-screen keyboard to move the insertion point around like a mouse cursor while editing text. A lot of people don’t know about this feature, and some who do misunderstand it, but it’s one of my favorite additions to iOS in recent years. If your iPhone has 3D Touch, while editing text you can hard press on the keyboard to turn it into a trackpad for moving the insertion point around in the text editing area. While in that mode, you can hard press again to change from moving the insertion point to selecting words (like double-click-then-drag on MacOS). iPads don’t (yet?) have 3D Touch, but you can access the same mode by putting two fingers on the on-screen keyboard and dragging. Two-finger touch on the keyboard and drag right away: move the insertion point. Two-finger touch on the keyboard, wait a moment for the insertion point to change to a barbell, and then drag: select words.
2. tvOS’s UIFocusEngine. That’s the interface framework that allows Apple TV to be controlled by a trackpad or game controller *without* an on-screen mouse cursor. On Apple TV, you don’t move a cursor around, you move the selection around. [Two years ago Steven Troughton-Smith discovered that an incomplete version of UIFocusEngine was built into iOS 9](https://daringfireball.net/linked/2015/11/13/uifocusengine-ios).
3. As things stand today while using an iPad with any hardware keyboard, selecting text and moving the insertion point around stinks. Yes, you can use the arrow keys on the keyboard (along with shortcuts like Option to move word-by-word instead of character-by-character, and Shift to select as you go), but it seems like a regression to 1983 to encourage an entirely keyboard-based routine for text editing. [The original Mac didn’t even have arrow keys on the keyboard](http://geekfun.com/2010/04/21/the-ipad-and-why-the-original-mac-didnt-have-arrow-keys/), to force users to use the mouse for moving the insertion point.


In short, when you’re using the iPad’s on-screen keyboard, you have a crummy (or at the very least sub-par) keyboard for typing but a nice interface for moving the insertion point around. When you’re using the Smart Keyboard (or any other hardware keyboard) you have a decent keyboard for typing but no good way to move the insertion point or select text. Using your finger to touch the screen is imprecise, and, when an iPad is propped up laptop-style, ergonomically undesirable.


A hardware keyboard with a trackpad could have just as good an interface for moving the insertion point and selecting text as the software keyboard. Even better, really, since you wouldn’t have to use two fingers or start it with a 3D Touch force press. And, a trackpad would make this feature discoverable. An awful lot of iPad owners — most of them, probably — don’t know about the two-finger drag feature on the on-screen keyboard.


When you’re *not* editing text, the trackpad might not do much on an iPad. But the entire point of the smart keyboard is that you’re writing and editing text while it’s connected, or you’re just using it to prop up the iPad for watching video or something. But I think the trackpad could be used for selecting things or changing input focus. On the home screen you could use the trackpad to select an app to launch, just like on Apple TV. In split-screen multitasking mode, you could use a multitouch gesture on the trackpad to switch which pane has focus. Two-finger drags on the trackpad could scroll the current view, much like on the Mac.


I fully admit this is not a perfect idea. But I do think it would greatly improve the efficiency of text editing on an iPad, and if text editing isn’t an essential task for iPad users, I don’t understand why Apple bothered making the Smart Keyboard in the first place. And, unlike adding touchscreen support to MacOS, adding trackpad support to iOS would not harm anything that is good about the way things already are.


The biggest problem with this entire notion is that the way the Smart Keyboard folds from a cover to a keyboard would have to be redesigned, because the current design leaves no room at all for a trackpad. What I’m proposing might only be possible with a hard (non-folding) keyboard cover.


---


[Stephen Coyle came up with a different idea](http://stephencoyle.net/ipad-trackpad/):


> The keys on the Smart Keyboard are very low profile, so it’s easy
> for one’s fingers to glide over them. With this in mind, why not
> make the entire top surface of the keyboard touch sensitive, then
> use it in the same way as the software keyboard? All that’s needed
> is a way to toggle trackpad mode, and I think this is a perfect
> opportunity to ditch the “caps lock” key, and replace it with a
> “trackpad mode” key, which can be held down while using one’s
> other finger to move the cursor.
> There are a few reasons why I think this approach would be better
> than a discrete trackpad. First, it requires no extra space, nor
> any major changes to the current design. Second, as mentioned
> above, it maintains gesture parity with the current trackpad mode
> on iOS. Third, it removes the expectation of a system-wide,
> mouse-style pointer, which I think a laptop-style trackpad would
> create. I think this is a significant consideration; a more
> precise pointing device would be really useful on iOS for more
> than just text entry, but I don’t expect this to come in the form
> of a mouse pointer. Thus, I think avoiding the suggestion of one
> altogether would lead to less confusion. With my proposed method,
> pro users who need this functionality won’t take long to become
> aware of it, and users who don’t need it won’t have what they may
> perceive as a half-broken laptop trackpad present at all times.


Coyle very nicely summarizes the most common objection I’ve heard to the idea of adding a trackpad to iPad keyboards: that adding a mouse pointer to iOS is a bad idea because when users see the trackpad they’ll expect a mouse cursor system-wide, not just while editing text.


Maybe!


But my gut tells me this concern is overblown. Even if users expect a mouse cursor when they first see the trackpad, they’ll adjust quickly when they realize it isn’t there. If they wanted a MacBook they’d be using a MacBook. By definition anyone using an iPad is not expecting it to act like a Mac. I do think *something* should happen when you move your finger(s) around the trackpad even when you’re not editing text, but tvOS shows that that *something* doesn’t need to be a mouse cursor moving around the screen.


I have three objections to Coyle’s alternative solution. First, I think it would prove to be a technical challenge to create a touch-sensitive surface with Apple-quality latency and responsiveness that also doubles as a good surface for typing. The existing Smart Keyboard is rubbery for several reasons, but I don’t think rubbery can be used for a touchpad, and I think the gaps between keys would result in stuttery cursor movement. Second, making it a two-handed operation is clunky (and it would be two-handed for people who want to move the insertion point using their right hand). Third, making it a mode — even an easily toggle-able mode — feels like a bad idea. Modes aren’t always bad in UI design — the iOS software keyboard’s “move the cursor” feature is a mode — but it’s almost always better to avoid modality if you can. With a discrete trackpad, the keyboard is always the keyboard and the trackpad is always the trackpad. That’s better than a keyboard that is usually a keyboard but sometimes a trackpad.


I say don’t overthink it. Just put a small trackpad under the keyboard for moving the insertion point around and Apple TV-style navigation. Simple.



| **Previous:** | [Halide](https://daringfireball.net/2017/05/halide) |
| **Next:** | [When the Scoops Run Dry](https://daringfireball.net/2017/05/when_the_scoops_run_dry) |


PreviousNext