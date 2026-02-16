---
title: "The Plain Text Workflow: How Vim and Markdown Became My Backbone"
date: 2023-12-10
url: https://www.ssp.sh/blog/my-vimverse/
slug: my-vimverse
word_count: 1672
---

![The Plain Text Workflow: How Vim and Markdown Became My Backbone](https://www.ssp.sh/blog/my-vimverse/featured-image.png)

Contents

In my journey, detailed in [why Vim is more than an editor](https://www.ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/), I’ve discovered the profound impact of integrating Vim and its motions into my entire computer workflow. This evolution, from using familiar tools like Notepad++ and SQL Server Management Studio to embracing Vim, represents a significant shift in how I approach tasks in data engineering and writing.


This blog post delves into how this transition to Vim, coupled with a step-by-step adoption of Markdown, has streamlined my process. Moving away from the limitations of WYSIWYG editors, I’ve embraced the simplicity and power of Markdown, as explored in my piece on [Markdown vs Rich Text](https://www.ssp.sh/brain/markdown-vs-rich-text/).


From the early days of learning editor shortcuts in VS Code to the moment I discovered the efficiency of Vim’s modal editing, my journey has been about finding [clarity](https://ssp.sh/brain/clarity) in my work. This path has led to significant changes in my writing process, including the adoption of [Obsidian](https://ssp.sh/brain/obsidian) for my Second Brain, and expanding Vim’s use to other applications, enhancing my productivity and creativity.


I share insights from my transition, showcasing how Vim’s [motions](https://ssp.sh/brain/vim-language-and-motions) and Markdown can revolutionize your workflow, just as they have mine.


## Where I came from


I started with procedural database instructions with PL- or T-SQL. Editors such as Notepad++, UltraEdit, or SQL Server Management Studio (SSMS) were my friends. Later, I discovered many more, such as Sublime, Eclipse, Netbeans, Sublime, TextMate, and VS Code.


### OS-wide Shortcuts


I was pretty efficient; I learned how to `ctrl+shift+end` and use arrow keys to select lines or jump with `shift+option+->` or `shift+option+<-` to select by words, both on Mac and Windows. Other shortcuts I only used a little as I wasn’t a proficient programmer.


However, I learned advanced features that I used and discovered constantly. These were features such as the column-edit feature in Notepad++ to extract columns, remove/add commas, or do another batch kind of work.


### Editor Shortcuts


Once VS Code became famous, I loved the `cmd+shift+p` shortcut to fuzzy find all commands. I felt way more productive in everyday tasks. Afterward, I added separate hotkeys for each command I used often, skipping the cmd+shift+p. Also, `cmd+p` to open and fuzzy find files was a big game-changer quickly.


At some point, I couldn’t get any faster. I was much faster than most of my co-workers, or so I thought. The problem was that I lost my productivity whenever I switched to another editor, program, or app. I had to do a lot of copy-pasting. Whenever I switched editors to a newer, better one, I had to re-learn all shortcuts and mappings. They were different on every tool. Sure, I tried to align them, but it was a lot of work, and I couldn’t recreate my old habits a hundred percent.


## Entering Writing. WordPress.


At the same time, I started to write more publicly on my [Blog](https://ssp.sh), and I had to constantly copy my text from something my Google Docs or editor I used to the WordPress editors. I also wrote directly in WordPress but didn’t do it anymore after losing some of my text or limited functionality.


I mostly wrote the text in my Second Brain, which at that time was Microsoft OneNote. But every time I wanted to publish, I had to ensure all my formatting was copied and the images looked okay. It was always a hassle. I had maintained two versions of the same, one locally and one on WordPress.


The worst part was that it was a pain if I wanted to fix errors or update my content. And I generally didn’t do it, even though I fancied the idea of constantly updating content back then, too.


## How I discovered Vim


At some random point, I discovered something called Vim. I saw it from a co-worker before, but I thought he needed to include more features from VS Code I used back then, and as he didn’t customize anything, it looked awful and not something I could ever work with.


But I was impressed with the macros and how he would temper the CSV or batch-fix files from the cmd line. Or how he instantly created Python scripts and ran them without leaving the terminal. You know, that hacker feeling we all want, I saw there.


But I was not into it yet. It was much later when I saw another co-worker who used Linux only and had great [Dotfiles](https://ssp.sh/brain/dotfiles) set up.


### Why it sticked


What grew over time on me was editing philosophy, also called [Vim Language (and Motions)](https://ssp.sh/brain/vim-language-and-motions). Instead of clicking with the mouse to a specific part to fix grammar or change a variable, in Vim motions, you jump there with a critical command and have another one to change after/before/surround a word. For each different edit, there was a command. I was hooked to learn more. That’s how a surgeon would work: fine-grained and filigree, but with words.


As I worked on a computer all day, I went in rabbit holes with custom keyboards, different keyboard layouts such as [Halmak](https://ssp.sh/brain/halmak), and fancied custom color themes. I have custom shortcuts for each edit I want.


Instead of only having to jump to the end of a line or jump by word, all of a sudden, I could do so many more. I have yet to learn the edit modes that you had. Besides the `insert-mode` that every editor had by default, you also had `normal`, `visual`, and `command` modes. You can learn more about the edit modes in my previous article [Why Vim Is More than Just an Editor â Vim Language, Motions, and Modes Explained](https://ssp.sh/blog/why-using-neovim-data-engineer-and-writer-2023/#how-to-use-vim-modes-normal-insert-visual-and-command).


But this was when I started to research Vim and what it was. I watched tons of videos by [ThePrimeagen](https://www.youtube.com/@theprimeagen) and other great videos. The possibilities blew me away.


## Writing


I never thought I would use it for writing, too. But it came naturally. The more I learned Vim, which initially takes a long time to get used to. But as I enjoyed the process, it was fun. It was like learning a game, adding a new superpower (shortcut) every weekâstarting to use `hjkl` instead of arrow keys for navigation or `o` to append under the current line and the whole palette.


To this day, I’m constantly learning more efficient ways to edit text, which helps me become a better writer. I can edit my second brain, and text I write everywhere with the speed of thought. It sounds cliche but valid for me.


### Entering Markdown.


Over time, [I moved away from WordPress](https://www.ssp.sh/blog/why-i-moved-away-from-wordpress/), to a [statistically generated site](https://www.ssp.sh/brain/static-site-generators-ssg/), the source being [Plaintext Files](https://ssp.sh/brain/plaintext-files), for transparent [Markdown](https://ssp.sh/brain/markdown) files with plain text with a sugar-coded syntax.


It felt powerful. I had one version of the truth. No more formatting battles, no more fear I’d lose a bolding text or a code formatting. I could write and publish them with a single script to see them locally or on my website.


I didn’t realize the power of Markdown back then, but with all of this, with the **power of modal editing** and **Vim motions**, I just started flying to take notes, capture an idea, write a short blog post, code or to this day, writing a [full-blown book](https://dedp.online) in plain text.


### Obsidian


Another key to this progress was [Obsidian](https://ssp.sh/brain/obsidian). Obsidian being a faithful [Second Brain](https://ssp.sh/brain/), owning your content as Markdown, I switched from my [10 years of OneNote to Obsidian](https://www.ssp.sh/blog/how-to-take-notes-in-2021/). A key element was the out-of-the-box Vim support in Obsidian.


![/blog/my-vimverse/img/setting-vim-mode-on-obsidian.png](https://www.ssp.sh/blog/my-vimverse/img/setting-vim-mode-on-obsidian.png)

*Setting to turn on vim keybinding.*


Instantly I had the superpowers from Vim I used everywhere for my note-taking app.

Why I do not use Neovim for notes

You might wonder why I don’t use Neovim for notes. I tried a couple of times, and sometimes, when writing my book, I use Neovim. But for the most part, Obsidian is optimized for notes specifically, and Neovim is optimized for programming.


With Obsidian based on Markdown, I have access to my [Second Brain](https://brain.sspaeti.com/) with forward/backlinks to any note or article. Better integration with images, text-based diagrams with [Mermaid](https://ssp.sh/brain/mermaid), and text-based images with [Exaclidraw](https://excalidraw.com/), and [Canvas](https://obsidian.md/canvas).


Integration with Plugins such as [ReadWise](https://ssp.sh/brain/readwise) syncing my highlights and notes I read, [Obsidian Dataview](https://github.com/blacksmithgu/obsidian-dataview) to use Notes as databases, [Admonition (Call-outs)](https://www.ssp.sh/brain/admonition-call-outs/) to write lovely in-side comments without distracting the reading flow, Templates, Mobile support, and many [more](https://obsidian.md/plugins). I write more about that in [Obsidian in Rich Text vs Markdown](https://www.ssp.sh/brain/markdown-vs-rich-text#obsidian).


## Other Vim-supported Apps I use


Today, I use everything as plain text wherever I can. With that, I learned that I can simplify my whole workflow.


Firstly, I can edit with the speed of thought, as if something is plain text; I can use Neovim and use all my muscle memory to edit it, with all the benefits of Markdown (if supported).


I’m trying to set up [Neomutt](https://neomutt.org/), another text-based editor, to read and write emails. I even built my favorite feature from [HEY.com](https://www.hey.com), the [HEY-Screener in (Neo)Mutt](https://www.ssp.sh/brain/hey-screener-in-neomutt/).


I also use [Vimium](https://chromewebstore.google.com/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb), a Chrome/Brave extension to navigate the browser without the mouse, inspired by Vim motions and navigation.


I’m excited about what else I can switch to Vim modes and commands. But so far, it makes me really happy that I can write everything from a single place and share it with a single script to either my public [Second Brain](https://brain.ssp.sh), my [Blog Website](https://ssp.sh), or my [Data Engineering Book](https://www.dedp.online/).


This is it for this blog. I wrote this more to reflect on how much Vim, its motions, and Markdown have significantly impacted my business life lately. And I just got introduced to Vim a couple of years back. I’m curious to follow that journey and hope to learn from your workflow and Vim journeys. Maybe I could inspire some of you to give Vim, and especially its motions, a try. That would make my day, as it could also heavily and positively influence your professional life.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/my-vimverse/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Vim](https://www.ssp.sh/tags/vim/)
[Obsidian](https://www.ssp.sh/tags/obsidian/)
[Writing](https://www.ssp.sh/tags/writing/)
[Neovim](https://www.ssp.sh/tags/neovim/)
