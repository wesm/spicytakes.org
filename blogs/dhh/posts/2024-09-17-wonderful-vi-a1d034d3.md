---
title: "Wonderful vi"
date: 2024-09-17
url: https://world.hey.com/dhh/wonderful-vi-a1d034d3
slug: wonderful-vi-a1d034d3
word_count: 1019
---

The speed of change in technology often appears to be the industry's defining characteristic. Nothing highlights that perception more than the recent and relentless march of AI advancements. But for as much as some things in technology change, many other things stay the same. Like vi!
vi is a programming text editor that was created by Bill Joy before computers even had real graphical interfaces,
[back in 1976](https://en.wikipedia.org/wiki/Vi_(text_editor))
. Just five years after the first microprocessor, the Intel 4004. In computing terms, we might as well be talking about ancient Egyptian hieroglyphs here. It's that old.
But it's fundamental design, splitting insert mode from command mode, remains unchanged in its modern successors, like
[Vim](https://www.vim.org/)
and
[Neovim](https://neovim.io/)
. In fact, the entire vi ethos of maximizing programmer productivity by minimizing keystrokes has carried forward all these years with remarkably little distortion. In 1976, most computers didn't even have a mouse. In 2024, most vi-successor users don't even need one when programming.
That's kinda incredible! That I can sit here, almost half a century after Bill Joy first gave birth to vi, and enjoy the same quirky style of text editing to make modern web apps in 2024. It's not
*why*
I use Neovim, but it sure does make it feel extra special.
The other reason it feels special is that vi makes turns manipulating text into a key-based form of Street Fighter. Sure, you can have fun just learning the basic buttons for punching and kicking, but the game unlocks an entirely new dimension the moment you pull off
[your first hadoken](https://www.youtube.com/watch?v=3ihrSG0j6l0)
— a fireball move done by making a half circle with the joystick followed by a punch. And now you're off to learn all the special moves followed by techniques for stringing them together into combos.
That's what pulling a "ciq" in Neovim feels like. It stands for "Change Inside Quotes". So say you're in the middle of a line of code like this: "puts 'Hello<cursor> World'". With that cursor placed after the "Hello", the "ciq" move will select all the text inside the quotes ("Hello World"), remove it, and place your cursor right after the opening quotes, ready to write something new. That's pretty magic!
And it just goes on and on from there. You can use "dab" to "Delete Around Brackets", which is great when you want to remove all the parameters used for a method at the end of a line in Ruby. Or what about "vii" to "(Visually) Select Inside [the current level of] Indention", so you have the entire body of a method highlighted, ready for overwriting with a paste or copying or cutting. Or just "yiw" which copies the current word your cursor is on, regardless of where in the word it is, and copies it to the clipboard.
There's an astounding number of combos like these available in Neovim (and the other vi flavors). But now you're probably thinking: how could anyone possibly remember all that? Which brings me to the real wonder of vi: It's not just an editor, it's a
*language*
for editing. Once you learn the basic grammar of vi text manipulation, and you learn a few actions, scopes, and objects, you can string it all together in any combination possible.
Here's the structure: [Action] [Scope] [Object]. I've already given you four actions in the examples above: change, select, delete, and copy. And there are only two primary scopes: inside and around. And we've looked at four different objects: quotes, brackets, indention, and word. There's your language.

```
yaq = Copy (yank) Around Quotesdiw = Delete Inside Wordvab = Select (visually) Around Brackets
```

See how it's starting to make sense? Now let's add one more move to the combo, which is a count. So you can also do:

```
3cw = Change Three Words
4dd = Delete Four Lines
10j = Jump Ten Lines
```

There's more to learning the vi command mode than just this, but to me, this is where the magic is. The language of text manipulation. The action-scope-object grammar. It's when that clicks that the combo stringing begins, and your dopamine starts flowing.
It's just uniquely satisfying to string a handful of these combos together and see the text beneath you radically manipulated. In a way you just know would have been a drag to do in any other editor. That's the game-like joy of vi's power moves.
Now all of this still comes with quite some learning curve, of course. On top of the text manipulation, there's a bunch of
[basic navigation keystrokes](https://manual.omakub.org/1/read/13/neovim)
to learn, but I think you ought to start with the basic grammar explained above. That's the fun bit, that's the addictive bit.
And if this appetizer has you hungry for more, I'd start by installing Neovim using
[the superb LazyVim distribution](https://www.lazyvim.org/)
. Neovim from scratch is like climbing Mount Everest without oxygen. If all you're interested in at first is a peek at the view, book that LazyVim helicopter tour before bothering the sherpas. Then checkout the excellent Vim and Neovim tutorials available on Youtube from the likes of
[ThePrimeagan](https://www.youtube.com/watch?v=X6AR2RMB5tE&list=PLm323Lc7iSW_wuxqmKx_xxNtJC_hJbQ7R)
and
[Typecraft](https://www.youtube.com/watch?v=zHTeCSVAFNY&list=PLsz00TDipIffreIaUNk64KxTIkQaGguqn)
, along with
[Elijah Manor's LazyVim introduction](https://www.youtube.com/watch?v=N93cTbtLCIM)
.
You can run Neovim on any operating system, but it works better if you're using a modern, fast terminal like
[Alacritty](https://alacritty.org/)
or Kitty. I personally use Alacritty and Neovim together with the multi-pane terminal enhancement
[Zellij](https://zellij.dev/)
. The entire package is configured out of the box in
[Omakub](https://omakub.org/)
, if your adventurous spirit should extend to a trip into Linux. But you absolutely don't need to run Linux to enjoy Neovim. It's great on both Mac and Windows too.
So that's it. That's my testimony to what a wonderful experience it's been adopting Neovim. It certainly wasn't without some frustration (like figuring out how to do my own snippets!!), and it's not without some sadness that I've given up on my beloved TextMate editor, but I can comfortably say,
[after running this stack since February](https://world.hey.com/dhh/finding-the-last-editor-dae701cc)
, that it feels like home now. A combo-smashing, hadoken-wielding home. And it's awesome.
May vi reign for another fifty years and beyond!
