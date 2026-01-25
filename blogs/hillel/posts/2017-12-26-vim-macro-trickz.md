---
title: "Vim Macro Trickz"
date: 2017-12-26
url: https://www.hillelwayne.com/post/vim-macro-trickz/
slug: vim-macro-trickz
word_count: 1339
---

Vim has one of the best macro systems of any text editor out there.


Here’s why: **Macros are just stored keystrokes**. When you record a macro, it’s saved to the appropriate register, and it can be pasted and appended like any other saved string. When you run the macro, Vim simulates you typing every single character in the register. There are a couple of quirks to this (you can’t have a macro record another macro), but for the most part, macros have complete access to everything in vim. You can open new windows, save and quit, trigger Ex commands, whatever. This makes macros one of the most powerful tools in your Vim toolkit.


> Found an old video where I wrote a Vim Brainfuck interpreter. No Vimscript, just keystrokes and macros. [pic.twitter.com/2rBNhBMpk4](https://t.co/2rBNhBMpk4)— Inactive; Bluesky is @hillelwayne(dot)com (@hillelogram) [November 5, 2017](https://twitter.com/hillelogram/status/927239094937292800?ref_src=twsrc%5Etfw)


Kind of a shame they’re so neglected. The vim doc has what, fifty lines devoted to macros? For comparison, the docs on the various forms of `:echo` are like a hundred lines. So let’s talk macros. I’m assuming you already know how to record and run a macro. If not, `:h q` will teach you the basics. The rest of this guide is going to be assorted macro trickz. In all cases, we’ll be recording the macro with `qq` and replaying it with `@q`.


### Helpful Settings


Stuff worth adding to your vimrc:

- `nnoremap Q @@`. In normal Vim `Q` switches you to Ex mode, which is almost never what you want. Instead, we’ll have it repeat the last macro you used, which makes using macros a lot more pleasant.
- `set lazyredraw`. Normally Vim rerenders the screen after every step of the macro, which looks weird and slows the execution down. With this change it only rerenders at the end of the macro.
- `nnoremap Y y$`. This isn’t necessary but helps when you’re debugging macros.


### Undoing mistakes


If you’re recording a macro and make a mistake, don’t start over. Instead, undo it and keep going normally. Once you’re finished with the macro, press `"qp` to paste it to an empty line, remove the mistaken keystrokes and the undo, and copy it back in with `"qy$`. Since macros are just keystrokes in a register, this is sufficient the fix whatever you broke.


**Warning:** Don’t leave undos in your macro. If you undo in a macro to correct a mistake, always be sure to manually remove the mistake **and** the undo from the macro. In replay mode, an undo will undo the *entire* macro up until that point, erasing all of your hard work and bleeding the macro out into the rest of your text.


### Manually adjusting macros


If after rerunning a macro you discover it has a small mistake, make the adjustments on the stored macro string. F.ex if you wrote `dw` when you actually meant `dW`, no reason to rerecord the entire macro.


Sometimes you want to add a special character or a chord. Maybe you need to add a return or switch windows with `c_W` or something, there are plenty of different reasons. If you inspect a register with a chord, you might see something like `^M` for `<CR>`. But manually adding in `^M` won’t work: Vim will interpret that as `^` (beginning of line) followed by `M` (go to middle of screen).


To add special characters, switch to insert mode and press `c_V` followed by the chord or character. This inserts the terminal code instead of the actual code. If `c_V` is used for pasting, you can usually use `c_Q` instead.


**Warning:** If you have your own maps, the macro will replay them. Normally this is good, *except* that it will skip any timeouts you have. For example, I have `inoremap jk <esc>` to quickly exit insert mode. If I do `qqij<wait a second>k<esc>q`, I’d expect `@q` to insert the string `jk` into my code. But since it didn’t record the wait, it will instead exit insert mode.


### Start with a guard prefix


The more deterministic the macro, the better. If possible we always want to start in the same relative position with respect to what we’re modifying. Usually that means starting the macro off with a `^` so you’re at the beginning of the line.


### End with a setup suffix


If you plan to run the macro a lot, end with a suffix that places the cursor where you want the next macro to begin. A common one here is `j` to go to the next line.


## Useful macro commands


A lot of stuff that isn’t too useful in everyday vimming becomes really handy when you’re embedding it in a macro.


### Marks


`m[a-z]` sets a mark in a given file, `'[a-z]` jumps to the line, and ``[a-z]` jumps to the exact position in the line you set the mark. You can use this to set up macros, or track state in the middle of a macro. These marks are local to the file.


**Warning:** If you’re manipulating marks or registers in a macro, this will override your existing setup. Either use dedicated “state” markisters or do what I do and be apathetic.


**Example:** ``adiw`bviwp`aP`. Swaps the words under marks `a` and `b`.


**Example:** `o**Warning:** <esc>'add''pkJ` Grab a bullet point in your “Gotchas” section you created and move it to a different section as a warning. I probably should have done it the other way around (putting the mark where I wanted to place the warning instead of on the warning it self), but too late for that now!


### File Marks


This is the same as `[a-z]` except it’s global: if you’re in a different file, `'A` will switch to the file with the given mark. Unsurprisingly, it’s useful for macros spanning multiple files or keeping a slush buffer.


**Example:** `yy'AGp<c_o><c_o>`. Copy to the line to your ‘A file and return to the original position.


### Registers


You can save and load from registers in the middle of a macro, which gives you the same stateful benefits as file marks. You can also assign to new registers with `:let @[a-z]= ...`. In insert mode, you can paste a register with `<c_R>[a-z]`.


**Example:** `:let @a=@a+1<CR>iconsole.log(<c_R>a);<esc>` Adds a console.log with increasing numbers.


**Example:** `mayyp`aDjv^r<space>`. Split on column.


```
abcd =>  ab
           cd

```


### Visuals


Most commands in visual mode exit to normal/insert, so you lose your selection. You can get it back with `gv`. You can also switch between ends of a selection with `o`.


**Example:** `A|<esc>gvohA|<esc>`. Add pipes around a selection like a poor man’s vim-surround. You could also do `c||<esc>""P` instead, but that doesn’t demonstrate visual reselection.


### Conditionals


If you need a conditional in your macro you should probably be writing a function instead. For very simple conditionals, though, you can probably get away with a “fail fast”. If one of the commands in a macro would cause an error, execution of the macro stops. Possible errors are `dy` (`y` isn’t a valid movement) or `f`, followed by a character not on the line.


**Example:** `]}k$hf,x`. removes a trailing comma of the last entry in a json object. If there is no trailing comma, does nothing. An alternative is `]}k:s/,$/<cr>` if you don’t want to have a fail-fast.


### Recursive Macros


Macros are best for simple ad-hoc repetitive edits. If you need something more sophisticated, consider using

- A function (`:h 41`), or
- An external filter (`:h !`), or
- A regex-based global/substitute (`:h :[sgv]`, `:h regex`), or
- A snippet plugin, or
- …


Look Vim has a lot of cool techniques for mass edits, and while macros are powerful, writing recursive macros *usually* means you picked the wrong tool for the job. But if you want to try recursive macros, [this](https://robots.thoughtbot.com/recursive-macros-in-vim) is a pretty decent guide. Although I think they chose the wrong tool. I probably would have done `:s!\v(\d\d)/(\d\d)/(\d+)!& : \1-\2\-\3` instead.


### Saving Macros


Just write a function dangit


*If you found this useful, please [share your own](https://twitter.com/hillelogram) vim trickz!*
