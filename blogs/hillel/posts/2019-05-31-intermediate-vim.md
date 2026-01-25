---
title: "At least one Vim trick you might not know"
date: 2019-05-31
url: https://www.hillelwayne.com/post/intermediate-vim/
slug: intermediate-vim
word_count: 2283
---

I’ve been using Vim for eight years and am still discovering new things. This is usually seen as a Good Thing About Vim. In my head, though, it’s a failing of discoverability: I keep discovering new things because Vim makes it so hard to know what’s available.


While people often talk about the beauty of modal editing or text objects, I don’t think that gets at the essence of Vim. Vim is a patchwork of subsystems crammed together with every crag of space stuffed with extra special-purpose tooling. There’s over a hundred different keystroke commands in Normal mode alone. That density is a big part of what makes Vim so useful. When “show all matching tags for keyword” is just `g]` then you’re much more likely to actually use it.


In nondiscoverable systems we have to rely on guides to find useful stuff. There aren’t that many for Vim, though. You have beginning articles, like `ciw` and such.1 And you have expert articles that dive into subsystems. But nobody really talks about those special purpose tricks, leading people to stumble into stuff they needed for the past six years.


This article is about some of the little tricks that I use in Vim. None of them are deep dives, and I encourage you to learn more about whatever’s interesting. They also aren’t connected to each other. But that’s fine. In total, they’re more than enough to help a lot.


### Organization


There are- very roughly- two categories of Vim users. **Purists** value Vim’s small size and ubiquitousness. They tend to keep configuration to a minimum in case they need to use it on an unfamiliar computer (such as during `ssh`). **Exobrains**, on the other hand, stuff Vim full of plugins, functions, and homebrew mappings in a vain attempt to pretend they’re using Emacs. If you took away an exobrain’s vimrc they’d be completely helpless.


As you can probably tell, I’m much more exobrain than purist. I’ve divided the tricks into two sections based on whether or not it involves adding mappings or settings to base Vim.


## Purist Vim


I used the standard Vim help representations for modal commands, ie `<cr>` means pressing the enter key. In cases where you have to `:h` a specific string to get help, like `:h E676`, I put the help string in parenthesis.


### Misc Normal Commands


### Macros


See [this post](https://www.hillelwayne.com/post/vim-macro-trickz/) for a deep dive into using macros.


### Visual Mode


#### g ctrl-A / ctrl-X


In visual mode, ctrl-A just increments the first number on every line. `g ctrl-A`, on the other hand, will bump the increment by one for each matching line. This is much easier to explain with a table:



| **selected** | `ctrl-A` | `g ctrl-A` | `2 g ctrl-A` |
| `a 0
b 0
c
d 0 ` | `a 1
b 1
c
d 1 ` | `a 1
b 2
c
d 3 ` | `a 2
b 4
c
d 6 ` |



#### operators: v, V, c-v (`:h o_v`)


You probably know about visual mode: v is character-wise, V is line-wise, ctrl-V is blockwise. But the three can also be used as motion operators, making the motion the corresponding -wise. For example, if you have


```
abc
abc
abc

```


If you place your cursor on the top `b` and press `d2j`, it will delete all three lines. That’s because `j` is a linewise motion. If you instead pressed `d<c-V>2j`, it would convert the motion to blockwise and delete just the middle column of `b`s.


One way I used to use this was with deleting to a search. Normally `d/` is an exclusive character motion. So I’ll use `dV/` to make it linewise and include the search-line in the deletion. There’s another way to do that, though:


### Ex Commands


Ex commands are the stuff you write from the command mode, such as `:s`. Beyond substitution, there are a lot of other useful ways to use ex. All of these examples need a range, such as `%`.


#### `:g/regex/ex`


Runs the `Ex` command only on the lines that match `regex`. So for example you can use `g/regex/d` to delete all the lines matching the regex. `v` is like `g` except it runs `ex` on all of the lines that *don’t* match `regex`.


This becomes more powerful with norm and friends.


#### `:norm {Vim}`


Acts as if you ran `{Vim}` on every single line in the range. For example, `g/regex/norm f dw` will delete the first word after the first space on every line matching `regex`. This is often much easier than using a macro.


`norm` obeys all of your mappings. For example, if you mapped `jk` to `<esc>` in insert mode, `norm I jk$diw` will prepend a space to the beginning of the line, *leave insert-mode*, and then delete the last word on the line. I like this functionality a lot, but if you’d prefer it not to use your mappings, you can use `norm!` instead.


#### `:co .`


Copies the range to the current line. You can also do arbitrary points instead of `.`, such as `+3` or `'a`. `mv` moves it instead.


#### `:y {reg}`


Copies the range to the register `{reg}`. If `{reg}` is a capital register, this appends to the existing register. ie if we do


```
let @a = '' | %g/regex/y A

```


It will copy all lines matching `regex` in the entire file to `a`. This can help with extracting broken-up text from a file and copying it to the system clipboard (with `let @+ = @a`.)


#### `:windo {ex}`


Runs `ex` on all windows. `:windo $` will scroll all windows to the bottom. There’s also `bufdo`, `cdo`, `tabdo`, etc.


This works really well with `g` and `s`. If you want to replace every instance of `AA` with `BB` but want to check each substitution first, you can use `vimgrep AA` to load all matches into a quickfix, then `cdo s/AA/BB/cge` to find/replace all the matches.


## Exobrain Vim


These are the stuff that requires persistent storage or you modifying your Vim session. Hypothetically you could use them as a purist by typing them in, but some of these are significant enough changes that go against the purist spirit.


I’m only including uncommon things here. Like a lot of people map `H` to `^`, so I don’t need to talk about that too. I also don’t need to talk about `vim-sensible` or `vim-surround`, and included only the more obscure plugins.


If you’re constantly tweaking your vimrc, do yourself a favor and add a command for that:


```
command! Vimrc :vs $MYVIMRC

```


### Settings


I put all my settings, maps, and functions into a single vimrc file. Breaking it up into many files makes it harder to find what I’m looking for.


Most of the settings aren’t really Vim “tricks”. Best bet is to look at [vim-sensible](https://github.com/tpope/vim-sensible): almost everything there is good for your vimrc.


#### `set statusline` (`:h statusline`)


Specifies what appears in the bar at the bottom of each window. The formatting here is a lot more complicated and finicky than other settings, and explaining it would take a post of its own. In terms of *simple* tricks, there’s a couple of things we can do. First, Vim’s default statusline is


```
:set statusline=%<%f\ %h%m%r%=%-14.(%l,%c%V%)\ %P

```


The easiest thing to replace here is the `%P`, which shows the percentage you’re through the file. The statusline format reads `%{exp()}` as writing the result of `exp()`. So for markdown files, we can do things like


```
:set statusline=%<%f\ %h%m%r%=%-14.(%l,%c%V%)\ %{wordcount()[\"words\"]}

```


To replace the percentage with the document wordcount.


You can also `set tabline`. If you don’t use tabs you can probably hack this to be a “global statusline”. Like you could do


```
set tabline=%{strftime('%c')}

```


To always show the date on top.


### Maps


I have a *lot* of maps.


A lot of Vim’s prime real-estate is taken up by cruft. `s` saves one whole keystroke over doing just `cl`. `U` is the same as `u` except it does the undo as a new change, which is functionally useless. `Q` is identical to `gQ` and is a colossal trap, anyway. `Z` is only used for `ZZ` and `ZQ`. Heck, the Vim manual recommends rebinding things like `_` and `,` to custom maps as “you probably never use them.” I’d much rather add completely new tasks to my keyboard vs saving a couple keystrokes. Some of the maps I have:


#### Special Arguments (`:h map-arguments`)


Writing `map <buffer> lhs rhs` makes the mapping only for that buffer. This is really handy when combined with autocommands, as a short-term shortcut, or when defining maps through a function. Buffer maps have priority over global maps, meaning you can override a general command with a more specifically-useful one.


On every use `map <expr> {lhs} {expr}` evaluates `{expr}` and uses the return value as the end mapping. One simple use-case is conditional maps. I have


```
nnoremap <expr> k (v:count == 0 ? 'gk' : 'k')
nnoremap <expr> j (v:count == 0 ? 'gj' : 'j')

```


Which makes `j` and `k` move by wrapped line *unless* I had a count, in which case it behaves normally. So I can navigate long paragraphs of prose without breaking things like `10j`.


`<silent>` is good if you are having mappings launch ex commands.


#### inoremaps


You can make maps in insert-mode with `inoremap`. Maps start in insert-mode, so `inoremap ;a aaaa` will type in ‘aaaa’ instead of ‘;a’. If you want to do something in normal mode, use `<c-O>`. IE if we have


```
inoremap ;1 <c-o>ma

```


then `;1` will set the `'a` mark at the point you are typing.


I tend to use semicolons as my leader key for imaps, because I almost never need to follow a `;` with anything other than a space or a newline.


### autocmd


Autocommands are great for configuration. You usually configure them in the form


```
augroup {name}
  autocmd! " Prevents duplicate autocommands
  au {events} {file regex} {command}
augroup END

```


Then whenever any of `{events}` happen in a file matching `{file regex}`, `{command}` fires. Events are listed under `:h event`. For example, if you do


```
augroup every
  autocmd!
  au InsertEnter * set norelativenumber
  au InsertLeave * set relativenumber
augroup END

```


Then Vim will turn off relativenumber only for insert mode.


Writing `au {event} <buffer> {ex}` only applies the autocommand to the buffer you are in. I sometimes use this for adding short-term event handlers to a specific file.


#### `BufNewFile,BufRead`


`BufNewFile` triggers when you create a new file, `BufRead` when you open the buffer for the first time. These are commonly used to add filetype-specific settings and mappings. One I have is


```
augroup md
  autocmd!
  au BufNewFile,BufRead *.md syntax keyword todo TODO
  au BufNewFile,BufRead *.md inoremap <buffer> ;` ```<cr><cr>```<Up><Up>
augroup END

```


This means for markdown files only, the string TODO is highlighted and typing `;`` in insert mode will add code fences.


You can do much more complex things with autocommands. For example, adding an `au` for `BufWriteCmd` will override the standard save, letting you put in custom logic. That’s moving beyond the realm of “Vim tricks” and into the realm of “dark magic”.


### Plugins


Most people know about popular plugins like `vim-surround` and `NERDtree`. This is a list of some of the more obscure ones that I think are very useful.


#### [Undotree](https://github.com/mbbill/undotree)


Most text editors have linear undo. If you make change A, undo it, and then make change B, then A is lost forever. Vim, on the other hand, stores the entire undo tree. `u` only undoes to a previous state in your current branch. `g-` moves to the previous *chronological* version of the code. You can see the list of undo leafs with `:undolist`.


That format is hard to read, though, and we’re better off seeing the actual tree. That’s what `Undotree` does: it laets you pop open a nice ascii representation of the undo tree for easy navigation.


#### [vim.swap](https://github.com/machakann/vim-swap)


Gives you commands to swap arguments around, so you can replace `(a, f(b, c))` with `(f(b, c), a)` in a couple keystrokes. I regularly have to do edits like that, so this is a huge quality of life improvement for me.


#### [Neoterm](https://github.com/kassio/neoterm)


Puts a higher-level API around the neo/vim embedded terminal. Like `:T {text}` will send `{text}` to the terminal. Makes for nice REPLs.


## `" TODO {{{`


There’s a lot that isn’t covered here because they’re too dense or long, like writing functions or the syntax system. There’s also a lot I don’t know yet. Here are some things that I plan on learning next:


### Preview, Quickfix, and List Windows


I’ll occasionally use tools that use these, but I don’t know how to manipulate them myself. I want to add quickfix errors to my [TLA+ plugin](https://github.com/hwayne/tla.vim/). I also like the idea of putting auxilary information and callback commands into a preview window. I see some possibilities that would be hard to replicate in an IDE.


### The Neovim API


Neovim has an extensive API for composing Vim with external programs. So you can have a Python script send commands to a Neovim instance, or control it through a server. I’ve seen some cool concept demos with this, where people autocomplete based on what’s in their browser. It just seems like a lot of fun!


### Text Objects


Never defined my own.


---


Anyway, that’s a brief tour of some slightly-more-obscure Vim features. Hope you learned something useful!


---

1. This used to say `cia` instead of `ciw`. That was a typo, not a reference to the [CIA Vim tipsheet](https://wikileaks.org/ciav7p1/cms/page_3375350.html).
 [return]
