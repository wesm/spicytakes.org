---
title: "Why Vim Is More than Just an Editor – Vim Language, Motions, and Modes Explained"
date: 2023-01-04
url: https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/
slug: why-using-neovim-data-engineer-and-writer-2023
word_count: 3075
---

![Why Vim Is More than Just an Editor – Vim Language, Motions, and Modes Explained](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/using-neo-vim-feature.jpg)

Contents
ð¶
Featured on Hacker News.
[Read the comments](https://news.ycombinator.com/item?id=43780682)

Throughout my time as a developer, I’ve used VS Code, Sublime, Notepad++, TextMate, and others. But shortcuts like `cmd(+shift)+end` and jumping with `option+arrow-keys` from word to word needed to be faster at some point.


I was hitting my limits. Everything I was doing I did decently fast, but I didn’t get any faster.


I’ve since learned that Vim is the only editor that you get faster using with time.


[Vim](https://www.vim.org/) is based solely on shortcuts. When I discovered that and played around a bit, I felt numb and a little stupid, having not learned the shortcuts (called Vim language) much earlier in my career.


I realized there was a keystroke to get to any specific position I wanted to jump. It was like a game, seeing if I could use fewer shortcuts to accomplish a particular edit. It’s where many Vim users get a lot of pleasure from coding and writing. It felt liberating, moving my cursor with the precision of a surgeon.


Although speed is a smaller benefit, it got me started when I saw [others](https://youtu.be/1UXHsCT18wE) navigating in Vim. After climbing the steep learning curve, it’s still one of the most powerful skills I’ve ever learned in my career, working for a living on a computer.


Let’s debunk the myth of Vim and learn how it’s possible to remember all the shortcuts using the specific Vim language. We’ll see how to move with vim motions, and I’ll share what I’ve learned so far, and why you might give Vim a try as well.


## Learning the Vim Language


Lots of things have been said about Vim – how fast it is, how only Linux nerds use it, and that it’s impossible to [exit Vim](https://stackoverflow.com/q/11828270).


For myself, I fell in love with the “Vim language”. You see, I’m bad at remembering anything and thought that Vim was not for me. But this wasn’t the case for one specific reason: Vim **motions** and its language.


I learned that there’s a grammar behind the editor. With it, you express what you want to do first, how many times, and then what you want it to apply.


Let’s get deeper into Vim and the language behind it.


### How the Vim Language and Motions Work


Vim has a terrific language or grammar behind its shortcuts. Instead of remembering a thousand shortcuts, you can learn a couple and combine them.


These are often called the Vim language or Vim motions for moving around. This has nothing to do with the editor yet – these are universal and available in other editors as well.


For example, there’s [VSVim](https://marketplace.visualstudio.com/items?itemName=JaredParMSFT.VsVim) for VSCode, [IdeaVim](https://plugins.jetbrains.com/plugin/164-ideavim) for the JetBrains products, [Vintage Mode](https://www.sublimetext.com/docs/vintage.html) for Sublime, and so on. But there are also Browser extensions like [Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en) or [Firenvim](https://chrome.google.com/webstore/detail/firenvim/egpjdkipkomnmjhjmdamaniclmdlobbo?hl=en), and Gmail even adapted some of Vim’s [shortcuts](https://support.google.com/mail/answer/6594?hl=en&co=GENIE.Platform%3DDesktop#zippy=%2Cjumping%2Cnavigation) for navigation (`j`, `k` for moving, `g` for jumping).


Everyone who types on a computer eight hours a day should learn the Vim language. Yes, it’s hard in the beginning, but that’s the case with everything new and different. But getting better every day and having more fun coding or writing should be motivation enough. You’re not too busy to learn - you’ll learn as you go.


![/blog/why-using-neovim-data-engineer-and-writer-2023/weel-too-busy.png](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/weel-too-busy.png)

*Are you too busy to improve | Image fromsteenschledermann*


#### Vim Grammar


Just as spoken language ****grammar**** has verbs, subjects, and objects, so does the Vim language. The grammar has different ****verbs**** to begin with. Copying (or yanking) in Vim with `y`, deleting with `d`, pasting with `p`, changing with `c`, and so on.


For example, the easiest shortcut is copying a line with `yy`. In this case, yank is the verb and the second `y` is a synonym for `y_`. The `y` is doubled up which makes it easier to type since it’s a joint operation.


Next, we can add movements. Each verb takes a ****subject**** for their movements. There are lots of movements (more in the next section) – the easiest is with numbers.


For example, to copy three lines, you add a 3 in front, such as `3yy`. You can do that with all verbs, like deleting three lines is `3dd`. Another would be `{` and `}` to move to the beginning or end of the paragraph, respectively.


In addition to verbs and subjects, the Vim language also has ****objects****. For example, we can save text into different clipboards (called a register in Vim) with `"ay`. Here, we copy it into register a, which would be the object. We can paste it again by doing the same but using the verb paste instead of yank `"ap`.


There are even ****adjectives**** and ****adverbs**** with prefixes. Usually, you use a verb and an object. But instead of going down three lines with `3J`, which joins the following three lines, you could add `d5}`, which means “delete from the current line through the end of the fifth paragraph down from here.”


For me, the most magical thing about Vim is how you navigate and edit text – and it still has nothing to do with the editor.


Sure Vim was the one that introduced and perfected these actions, but again – you can get them anywhere else. This goes deep into the Vim language, yet we still need to touch on the editor. This is important to know.


I hope you’ve started seeing the power of such patterns, though. With a couple of verbs and objects, you can already know hundreds of combinations without memorizing each one individually.


You can watch a video on [Mastering the Vim Language](https://youtu.be/wlR5gYd6um0) or read a full exposition of the Vim language on this terrific [StackOverflow](https://stackoverflow.com/a/1220118) comment.


### Vim Motions


Vim motions are how you navigate, whether you navigate to the end of the word or back to the start of the document – these are all motions.


These are the first things you start learning (and hating) when learning Vim. They’re extra hard to figure out initially, but they’re something you’ll want to use everywhere when you get used to them.


Instead of using arrow keys, Vim uses `jk` to move down and up and `hl` to move left and right. The main idea is to use the keys your right hand naturally rests on. You do not need to move your hands or even fingers for navigation.


Again, this seems like a small thing, but once you’ve learned it, you know why everyone is telling you about it.


Some common motions are:



| `1
2
3
4
5
6
` | `h,j,k,l - left, down, up, right
w - to start of next word
b - to start of previous word
e - to end of word
$ - to end of line
^ - to start of line
` |



You can find the most important motions to start with in this cheatsheet:


[

](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/vim-language-cheetsheet.png)Vim Command Cheat Sheet from [Cloud Guru](https://acloudguru.com/blog/engineering/a-vim-cheat-sheet-reference-guide)

<div class="details admonition note open">
        <div class="details-summary admonition-title "><i class="icon admonition-icon icon-note"></i>My Vim Cheatsheet<i class="details-icon  admonition-icon admonition-icon-arrow-right"></i></div>
        <div class="details-content">
            <div class="admonition-content"><p>&ndash;&gt;</p>
<!-- [My own Vim Cheatsheet](https://brain.sspaeti.com/cheatsheet-vim)
</div>
        </div>
    </div>

## How to Use Vim Modes (normal, insert, visual, and command)


Modes are another thing that might get you confused at the beginning.


When you launch Vim, you are not typing what you click on your keyboard as you are not in the “insert” mode that you’re likely familiar with from other editors. Instead, the normal mode you are in lets you do the commands explained in the above Vim language and motions.


Vim is the only editor that **optimizes editing text** instead of writing from a blank page.


![/blog/why-using-neovim-data-engineer-and-writer-2023/vim-modes.png](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/vim-modes.png)

*Three modes illustrated (escape mode being the command mode) | Image fromGeekforgeeks*


That’s another reason Vim makes you so efficient: you have different modes for each phase of your current work or task.

- Normal mode is for reading code and navigating quickly.
- Insert mode is for when you want to add some code or text.
- Visual mode is unique, the same as highlighting text with the mouse, but with the above Vim motions.
- And command mode is the powerhouse, where you can type Linux commands such as formatting a JSON file with `:%!jq` (whereas [jq](https://stedolan.github.io/jq/) is a command line tool installed on your machine) and execute them within Vim. This is also where you can use Vim commands such as `:sort` for sorting your files.


I could go on here, but I want to dive into the editor itself now and explore why I learned it initially and how to get started.


## Introduction to Vim the Editor (Neovim, Lunarvim, and Helix)


So what is Vim the editor, then? It started with the simple vi editor, a basic editor that implements the Vim language and can edit text. It’s a little like Notepad++, which you might use on Windows, but without a mouse and context menu.


Vim is simply an improved version of Vi with more features.


![/blog/why-using-neovim-data-engineer-and-writer-2023/vi-vs-vim.png](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/vi-vs-vim.png)

*Differences between Vi and Vim | Image byLinuxiac*


Today there is even a newer version of Vim called [Neovim](https://neovim.io/). This version is super popular, and I’ve started using Neovim as well. Compared to Vim, Neovim uses [Lua](https://www.lua.org/), an actual programming language, to configure and extend the editor. This makes writing plugins and configuring Neovim easier compared to Vim’s native [Vimscript](https://learnvimscriptthehardway.stevelosh.com/).


Neovim is a great place to start learning Vim today, as it has so many awesome [plugins](https://github.com/rockerBOO/awesome-neovim). Neovim also won the most [loved IDE](https://survey.stackoverflow.co/2022/#integrated-development-environment) on the StackOverflow survey a couple of times, last in 2022.


There is also an editor called [Helix](https://github.com/helix-editor/helix) built in Rust, but it has minor deviations from the Vim language, which make it a less optimal place to start.


If you want to get started without needing to know anything about Neovim and spending hours on configurations, you can begin with [LunarVim](https://www.lunarvim.org/). It’s a distro with all the features you know from VS Code already included.


Suppose you are comfortable with the terminal and realize you want to change the editor to your liking. In that case, you can kickstart your journey with a [simple single-file configuration](https://github.com/nvim-lua/kickstart.nvim) with many explanations that will work out of the box. You can also learn each config by opening the single config file.


## Why I Learned Vim


Using the standard input method we use in our editors daily, we will eventually stagnate at a certain level. Sure, you can use `cmd+arrow-keys` (on a Mac) to jump to the beginning of a line or `option+arrow-keys` to jump between words instead of characters.


But what happens once you’ve mastered that? What if you need to change something in the middle of a sentence? There is no other way to jump several times with this option, or you move your hands away each time to reach the mouse to click on the exact spot.


One day, I saw a coworker work in Vim, and everything clicked. The Vim language and motions were the things I needed all along. So I installed the VS Code plugin, watched a couple of YouTube videos, and started my journey to learn the basic movements.


I also love learning new things and, even better, I’m always looking for ways to make me more productive ð.


But as many of you might have experienced, the hardest part of learning Vim is getting started. The initial learning curve is very steep. Below is an illustration that shows this :).


![/blog/why-using-neovim-data-engineer-and-writer-2023/vim-learning-curve.png](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/vim-learning-curve.png)

*The learning curve for text editors. Although funny, very accurate | Image fromWhy I Love Using Vim To Write Code*


It took me also two or three times trying to start learning Vim until I fully grasped it. I switched back and forth. As well as having to get work done, it is sometimes hard to switch entirely from one day to another. But I just loved learning all the movements, and I knew it would make me faster after a short time.


## Why I Love Vim


I have been using Vim for only eight months, and coding with Python for around six years. I’ve been using other code editors since my career started in 2003. Each editor I used had its strengths and its appeal. But I never experienced such efficiency gains as I have with Vim.


In the end, use the editor that works best for you. Personally, I want my editor to help me work as fast as possible, especially since I use it daily. Investing a bunch of time learning Vim is necessary, but it pays off over time. That’s the whole point with Vim and especially the Vim language.


An underrated skill in general among programmers is using the ****terminal****. By learning your editor, especially with Vim, you will naturally learn more about the terminal and improve your Linux skills (reverse search, lazy git, Tmux, and many more).


Before Vim, I only used the terminal if I had to. I googled everything, and today, I use the terminal with its helpful manuals whenever I can.


Sometimes I’m surprised by myself as well, and it’s super nerdy – but it’s so effective. I’ve become a much better developer since starting to get comfortable with Vim.


Tweaking and optimizing Vim can take hours and days, and it’s unavoidable in the beginning. But after a while, your [dotfiles](https://github.com/sspaeti/dotfiles) mature, and you start changing things less. You will also get much faster at trying out a new plugin or adding a remap.


Also, Vim is ****fun****! Working in Neovim is one of the highlights of my everyday work. Improving your text editor and making it your own – maybe in ways no one else has optimized – is awesome.


For example, I write a lot, so I optimized for writing markdown and programming in Python. That’s what adds a lot to my happiness as a coder.

PDE (Personalized Development Environment
Because of all this,
[TJ DeVries](https://github.com/tjdevries)
calls Neovim a
[PDE](https://brain.sspaeti.com/pde-personalized-development-environment)
(Personalized Development Environment), not “just” an IDE. You can learn more about this in
[ThePrimeagen](https://www.youtube.com/c/ThePrimeagen)
’s truly inspiring
[Vim videos](https://youtube.com/playlist?list=PLm323Lc7iSW_wuxqmKx_xxNtJC_hJbQ7R)
and learn why he used
[Vim in 2022](https://youtu.be/D4YTJ2W5q4Y)
.

Vim also manifested ****minimalism**** more in me. I used the terminal instead of fancy GUIs and plain text files for clarity, freedom, blazingly fast shortcuts, no vendor lock-in, and staying in the [Flow](https://brain.sspaeti.com/deep-work) with the content in front.


Vim changed not only my [workflow](https://www.ssp.sh/blog/my-vimverse/) but how I was able to ****edit at the speed of thought****. Instead of thinking, “I want to edit that word”, my fingers jump to that word and change it with a few keystrokes.


## Vim for Data Engineering


My data engineering workflow uses Neovim with the [LSP](https://microsoft.github.io/language-server-protocol/) (Language Server Protocol) [pyright](https://github.com/microsoft/pyright) installed with [mason](https://github.com/williamboman/mason.nvim). There’s much more with [Tmux](https://github.com/sspaeti/dotfiles/tree/master/tmux), but you can find all the details on [dotfiles/nvim](https://github.com/sspaeti/dotfiles/tree/master/nvim).


![/blog/why-using-neovim-data-engineer-and-writer-2023/vim-mason-install.png](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/vim-mason-install.png)

*Installing Pyright with Mason*


## Vim for Writing


I’m still using [Obsidian](https://brain.sspaeti.com/obsidian) a lot more for writing (see more on my [PKM workflow](https://sspaeti.com/blog/pkm-workflow-for-a-deeper-life/)) due to its additional features of supported images, backlinks, graphs, and plugins specified for note-taking, such as [ReadWise](https://brain.sspaeti.com/readwise) (syncing my highlight from books, and tweets), [Dataview](https://github.com/blacksmithgu/obsidian-dataview) (using notes as a database), [Excalidraw](https://excalidraw.com/) (drawing with Markdown format), Templates, and so on.


Nevertheless, I write more and more in Neovim. For now, I use [ZenMode](https://github.com/folke/zen-mode.nvim) (for centering the text), Grammarly (for linting grammar), [write-good](https://github.com/btford/write-good) (linting grammar), and specifically [Obsidian.nvim](https://github.com/epwalsh/obsidian.nvim) (follow backlinks, and so on.). You find all details in my [dotfiles](https://github.com/sspaeti/dotfiles).


In Obsidian, I use the [Vim mode](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/for+Vim+users) Obsidian [.vimrc](https://github.com/sspaeti/dotfiles/blob/master/obsidian/.vimrc) and map most [hotkeys](https://github.com/sspaeti/dotfiles/tree/master/obsidian) to my Vim settings. At the same time, I’ve been writing more and more in Neovim and have been progressively moving over to full Neovim.


Plugins such as [Telescope](https://github.com/nvim-telescope/telescope.nvim) and simple grep features that I use for coding work very well with Markdown. Here are some clips showing what is possible in an excellent talk about [Writing, Editing, and World-Building at the speed of thought with Vim](https://youtu.be/2ORWaIqyj7k).


## Why You Should Learn Vim, Too


When I heard about Vim, I thought that it was only for software engineers and Linux nerds ð. I never thought I was going to use it as well. But how did I get into it?


I’ve already shared some reasons why I love Vim. But it really changed all my workflows, not only as a developer but also how I surf the internet, write, navigate, and use tools. I search for a Vim mode in any application I use.


But if you don’t enjoy fiddling and optimizing your workflow, and if you don’t write or code for a living, Vim might not be for you. Start with your current editor and activate the Vim mode before you do anything with Vim. It will save you [a lot of frustration](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/), trust me ð.


## How to Get Started Using Vim


There are many good resources that’ll help you get started with Vim. The easiest is to type `vimtutor` into your terminal, which is an interactive tutorial for Vim.


I’ve already linked a few YouTube videos above – especially check out ThePrimagen starting with [Vim As Your Editor](https://youtu.be/X6AR2RMB5tE) or [Why even bother with Vim or Neovim in 2022](https://youtu.be/84qoMxS-iqQ).


I started with Ben Awads’s [Vim tutorial](https://youtu.be/IiwGbcd8S7I) back then. An excellent [Lecture: Editors (Vim) (2020)](https://youtu.be/a6Q8Na575qc). [Mastering the Vim Language](https://youtu.be/wlR5gYd6um0). I also collect a small [playlist](https://www.youtube.com/playlist?list=PLxGd5Sk9B7IZfFOxGWgg8XswEKZ6lEzmh) on YouTube with Vim content. A big inspiration also [dev workflow using Tmux and Vim](https://youtu.be/sSOfr2MtRU8) from [Takuya](https://twitter.com/inkdrop_app?lang=en).


## Wrapping Up


We have learned that Vim is a powerful text editor popular among developers. It’s based on shortcuts, called the Vim language, which can make coding and writing faster and more efficient.


With Vim, you can jump to any specific text position and rapidly make precise edits. While learning Vim can be challenging, it is well worth the effort in the long run as it will improve your productivity and bring joy to your coding experience.


If you want to go further, read my follow-up on [My Vim-Verse](https://www.ssp.sh/blog/my-vimverse/), or try [Tmux](https://github.com/tmux/tmux/wiki), which plays well with Vim. You could even go one level deeper, which is a dedicated keyboard layout such as [Dvorak](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout) or [Halmak](https://brain.sspaeti.com/halmak) (which I started learning at some point). Or buy a fancy [ergonomic keyboard](https://www.reddit.com/r/kinesisadvantage/comments/yplirr/im_also_part_of_the_team_kinesis_now/?utm_source=share&utm_medium=web2x&context=3) or [build one yourself](https://bit.ly/sspaeti_keyboard).


Thanks for reading this far. I hope you enjoyed this article. I’m looking forward to hearing your comments and experiences.


---


```
Republished on FreeCodeCamp.
```

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Vim](https://www.ssp.sh/tags/vim/)
[Neovim](https://www.ssp.sh/tags/neovim/)
[IDE](https://www.ssp.sh/tags/ide/)
[Writing](https://www.ssp.sh/tags/writing/)
