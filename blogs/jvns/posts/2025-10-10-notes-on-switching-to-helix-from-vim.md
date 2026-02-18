---
title: "Notes on switching to Helix from vim"
date: 2025-10-10
url: https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/
slug: notes-on-switching-to-helix-from-vim
word_count: 1152
---


Hello! Earlier this summer I was talking to a friend about how much I
[love using fish](https://jvns.ca/blog/2024/09/12/reasons-i--still--love-fish/), and
how I love that I don’t have to configure it. They said that they feel the same
way about the [helix](https://helix-editor.com/) text editor, and so I decided
to give it a try.


I’ve been using it for 3 months now and here are a few notes.


### why helix: language servers


I think what motivated me to try Helix is that I’ve been trying to get a working
language server setup (so I can do things like “go to definition”) and getting
a setup that feels good in Vim or Neovim just felt like too much work.


After using Vim/Neovim for 20 years, I’ve tried both “build my own custom
configuration from scratch” and “use someone else’s pre-buld configuration
system” and even though I love Vim I was excited about having things just work
without having to work on my configuration at all.


Helix comes with built in language server support, and it feels nice
to be able to do things like “rename this symbol” in any language.


### the search is great


One of my favourite things about Helix is the search! If I’m searching all the
files in my repository for a string, it lets me scroll through the potential
matching files and see the full context of the match, like this:


![](https://jvns.ca/images/helix-search.png)


For comparison, here’s what the vim ripgrep plugin I’ve been using looks like:


![](https://jvns.ca/images/vim-ripgrep.png)


There’s no context for what else is around that line.


### the quick reference is nice


One thing I like about Helix is that when I press `g`, I get a little help popup
telling me places I can go. I really appreciate this because I don’t often use
the “go to definition” or “go to reference” feature and I often forget the
keyboard shortcut.


![](https://jvns.ca/images/goto.png)


### some vim -> helix translations

- Helix doesn’t have marks like `ma`, `'a`, instead I’ve been using `Ctrl+O` and
`Ctrl+I` to go back (or forward) to the last cursor location
- I think Helix does have macros, but I’ve been using multiple cursors in every
case that I would have previously used a macro. I like multiple cursors a lot
more than writing macros all the time. If I want to batch change something in
the document, my workflow is to press `%` (to highlight everything), then `s`
to select (with a regex) the things I want to change, then I can just edit
all of them as needed.
- Helix doesn’t have neovim-style tabs, instead it has a nice buffer switcher (`<space>b`)
I can use to switch to the buffer I want. There’s a
[pull request here](https://github.com/helix-editor/helix/pull/7109) to implement neovim-style tabs.
There’s also a setting `bufferline="multiple"` which can act a bit like tabs
with `gp`, `gn` for prev/next “tab” and `:bc` to close a “tab”.


### some helix annoyances


Here’s everything that’s annoyed me about Helix so far.

- I like the way Helix’s `:reflow` works much less than how
vim reflows text with `gq`. It doesn’t work as well with lists. ([github issue](https://github.com/helix-editor/helix/issues/3332))
- If I’m making a Markdown list, pressing “enter” at the end of a list item
won’t continue the list. There’s a [partial workaround](https://github.com/helix-editor/helix/wiki/Recipes#continue-markdown-lists--quotes)
for bulleted lists but I don’t know one for numbered lists.
- No persistent undo yet: in vim I could use an
[undofile](https://vimdoc.sourceforge.net/htmldoc/options.html#'undofile') so
that I could undo changes even after quitting. Helix doesn’t have that feature yet.
([github PR](https://github.com/helix-editor/helix/pull/9154))
- Helix doesn’t autoreload files after they change on disk, I have to run
`:reload-all` (`:ra<tab>`) to manually reload them. Not a big deal.
- Sometimes it crashes, maybe every week or so. I think it might be
[this issue](https://github.com/helix-editor/helix/issues/12582).


The “markdown list” and reflowing issues come up a lot for me because I spend
a lot of time editing Markdown lists, but I keep using Helix anyway so I guess
they can’t be making me that mad.


### switching was easier than I thought


I was worried that relearning 20 years of Vim muscle memory would be really hard.


It turned out to be easier than I expected, I started using Helix on a
vacation for a little low-stakes coding project I was doing on the side and
after a week or two it didn’t feel so disorienting anymore. I think it might be
hard to switch back and forth between Vim and Helix, but I haven’t needed to use
Vim recently so I don’t know if that’ll ever become an issue for me.


The first time I tried Helix I tried to force it to use keybindings that were
more similar to Vim and that did not work for me. Just learning the “Helix way”
was a lot easier.


There are still some things that throw me off: for example `w` in vim and `w` in
Helix don’t have the same idea of what a “word” is (the Helix one includes the
space after the word, the Vim one doesn’t).


### using a terminal-based text editor


For many years I’d mostly been using a GUI version of vim/neovim, so switching
to actually using an editor in the terminal was a bit of an adjustment.


I ended up deciding on:

1. Every project gets its own terminal window, and all of the tabs in that
window (mostly) have the same working directory
2. I make my Helix tab the first tab in the terminal window


It works pretty well, I might actually like it better than my previous workflow.


### my configuration


I appreciate that my configuration is really simple, compared to my neovim
configuration which is hundreds of lines. It’s mostly just 4 keyboard
shortcuts.


```
theme = "solarized_light"
[editor]
# Sync clipboard with system clipboard
default-yank-register = "+"

[keys.normal]
# I didn't like that Ctrl+C was the default "toggle comments" shortcut
"#" = "toggle_comments"

# I didn't feel like learning a different way
# to go to the beginning/end of a line so
# I remapped ^ and $
"^" = "goto_first_nonwhitespace"
"$" = "goto_line_end"

[keys.select]
"^" = "goto_first_nonwhitespace"
"$" = "goto_line_end"

[keys.normal.space]
# I write a lot of text so I need to constantly reflow,
# and missed vim's `gq` shortcut
l = ":reflow"

```


There’s a separate `languages.toml` configuration where I set some language
preferences, like turning off autoformatting.
For example, here’s my Python configuration:


```
[[language]]
name = "python"
formatter = { command = "black", args = ["--stdin-filename", "%{buffer_name}", "-"] }
language-servers = ["pyright"]
auto-format = false

```


### we’ll see how it goes


Three months is not that long, and it’s possible that I’ll decide to go back
to Vim at some point. For example, I wrote a [post about switching to
nix](https://jvns.ca/blog/2023/02/28/some-notes-on-using-nix/) a while back but
after maybe 8 months I switched back to Homebrew (though I’m still using NixOS
to manage one little server, and I’m still satisfied with that).
