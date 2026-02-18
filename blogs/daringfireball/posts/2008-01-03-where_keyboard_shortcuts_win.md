---
title: "Where Keyboard Shortcuts Win"
date: 2008-01-03
url: https://daringfireball.net/2008/01/where_keyboard_shortcuts_win
slug: where_keyboard_shortcuts_win
word_count: 766
---


In an off-hand remark [here](http://www.tbray.org/ongoing/When/200x/2007/12/31/Year-Sweep-Tech), Tim Bray writes:


> The famous Tog explains in parts [1](http://www.asktog.com/TOI/toi06KeyboardVMouse1.html), [2](http://www.asktog.com/TOI/toi22KeyboardVMouse2.html), and [3](http://www.asktog.com/SunWorldColumns/S02KeyboardVMouse3.html), why the mouse is
> always faster than the keyboard. He’s wrong. Why is left as an
> exercise for the reader.


Here’s the crux of Tog’s [original analysis](http://www.asktog.com/TOI/toi06KeyboardVMouse1.html):


> We’ve done a cool $50 million of R&D on the Apple Human
> Interface. We discovered, among other things, two pertinent facts:
> Test subjects consistently report that keyboarding is faster than mousing.
> The stopwatch consistently proves mousing is faster than keyboarding.
> […] It takes two seconds to decide upon which special-function
> key to press. Deciding among abstract symbols is a high-level
> cognitive function. Not only is this decision not boring, the user
> actually experiences amnesia! Real amnesia! The time-slice spent
> making the decision simply ceases to exist.
> While the keyboard users in this case feels as though they have
> gained two seconds over the mouse users, the opposite is really
> the case. Because while the keyboard users have been engaged in a
> process so fascinating that they have experienced amnesia, the
> mouse users have been so disengaged that they have been able to
> continue thinking about the task they are trying to accomplish.
> They have not had to set their task aside to think about or
> remember abstract symbols.
> Hence, users achieve a significant productivity increase with the
> mouse in spite of their subjective experience.


The main point here is that according to Apple’s late-80s user testing, it takes longer to use keyboard shortcuts than to use the mouse for most tasks, but it *feels* like the opposite is true, because for some reason people don’t notice the (significant) time that it takes to recall just which keys to press to invoke a keyboard shortcut.


This nugget has been controversial ever since Tog first published it in 1989, mainly, I think, because it’s just so hard to accept that our perception could be so wrong.1 I’ve also heard the argument that 20-year-old research may no longer be relevant. Someone would have to conduct actual user testing to prove it, but my money says it still holds true. If anything, I’d guess that today’s mousing times would improve — in the 1980s many people had little or no experience using a mouse; today, everyone knows how to use one.


But I don’t think it’s fair to summarize Tog’s argument as claiming “the mouse is always faster than the keyboard”; clearly there are exceptions. Tog himself mentions one:


> Not that any of the above True Facts will stop the religious wars.
> And, in fact, I find myself on the opposite side in at least one
> instance, namely editing. By using Command X, C, and V, the user can
> select with one hand and act with the other. Two-handed input.
> Two-handed input can result in solid productivity gains (Buxton
> 1986).


Another exception where keyboard shortcuts should win, and win big, in a stopwatch test: repetitive actions.


When you’re doing the same thing over and over — not even necessarily right after each other (e.g. Paste, Paste, Paste, Paste…) but just several times in close proximity — it’s a huge win to have a keyboard shortcut. E.g. “Find Next”, or deleting several non-adjacent items in a list. The key to understanding Tog’s argument about why the mouse is faster is that there’s a hidden delay where you stop to recall the actual keys to press for a shortcut. But with repetitive actions, you only suffer that penalty the first time. Even if you waste two seconds remembering that the shortcut for Find Next is Command-G, you save time (versus using the mouse) if you invoke it several times in a row.2


I’ve always thought this was a good rule of thumb for developers when deciding which menu item commands should get keyboard shortcuts. It’s obvious that commands that are used frequently should get shortcuts, but so too should commands that, even if they’re used infrequently, are likely to be invoked several times in short order when they are used.


---

1. Keyboard shortcut aficionados also get upset about this because they mistakenly conclude that Tog was “against” keyboard shortcuts. Not so. ↩︎
2. Especially with most Cocoa apps, where the Find commands are in a sub-menu, and thus take even longer to target using the mouse. ↩︎



| **Previous:** | [The Way the Camera Follows Us in Slo-Mo](https://daringfireball.net/2008/01/follows_us_in_slo-mo) |
| **Next:** | [Advertising on Daring Fireball](https://daringfireball.net/2008/01/advertising_on_df) |


PreviousNext