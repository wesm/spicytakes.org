---
title: "Finding The Last Editor"
date: 2024-02-27
url: https://world.hey.com/dhh/finding-the-last-editor-dae701cc
slug: finding-the-last-editor-dae701cc
word_count: 881
---

Some programmers can code under any conditions. Open office? They'll bring headphones. Whatever editor is on their system? They'll make it work. Using a different framework or language every few years? No problem. I envy that level of versatility, but I've come to accept it just isn't me. I bond with a quiet room, an editor, and a programming environment far more deeply than that.
Case in point, I've been using the
[TextMate](https://macromates.com/)
programming editor since it was first created back in 2004. That's twenty years now. Almost as long as my time with Ruby working on Rails. TextMate has seen its popularity come and go in that time, and today, few people are still choosing it. But I don't care. It's damn near
[Finished Software](https://world.hey.com/dhh/finished-software-8ee43637)
as far as I'm concerned, and I love programming with TextMate.
It's all the little things. Like the algorithm for escape-completion of words within the current document. The macro recording and replay mechanism that I've used to setup the small handful of automations I use on a daily basis, like cmd-return to turn "method" into "def method/n  $cursor\n  end" or "doo<tab>" into "do |$cursor|\n  [tab $cursor]\n  end". It's the superb column mode. Oh, and it's the All Hallow's Eve color theme, and the perfection with which it renders Bitstream Vera Sans Mono.
It's not much, because I'm not looking for an IDE. I want to write my code in a plain text editor, and let that constraint force me to design programs and frameworks that require nothing more. It's amazing how sensitive you become to extraneous elements when you literally have to type all of them by hand. It's surely one of the reasons I never got on with explicitly-typed languages, which basically require an IDE to flow.
When I flatter myself, I think of it like climbing free solo. Minus the imminent risk of death. It's choosing for something to be harder, because the constraint has value.
So I'd long thought that TextMate might well be that forever editor for me. I've tried all of the major alternatives, but none of them has nailed the basics in the way TextMate does for me. Most of The New Stuff they brought to the party was stuff I'd pay to forgo.
But here's the problem. TextMate is tied to the Mac. And tying myself to the Mac seems like an increasingly bad idea. Apple has turned into the kind of company that I just don't want to have to rely on. That doesn't mean I can't use any of their products, but I absolutely do not want to feel like I have to. I want to have the independence where walking away is always an option, and it just isn't, as long as I'm committed to TextMate.
Thus began the search for The Last Editor. One that isn't tied to a specific platform, or preferably even a specific company, and that I trust will still be around until I'm done programming.
[VSCode](https://code.visualstudio.com/)
has become the obvious choice for most in the web world, but the longer I spend working with it, the more I realize that its heart is beating to become a full-fledged IDE, and all I want is a text editor.
I don't think we're going in the same direction, VSCode and I, and frankly, even with their latest redemption arc, I'm not keen to tie my editor commitment to Microsoft. Who knows what kind of villainy they may once again descent into, if you hope to still be writing code for another 20-30 years.
The suggestion I've heard a lot is
[Sublime](https://www.sublimetext.com/)
. They have clients on macOS, Windows, and Linux. I hear a lot of good things about it. The spiritual successor to TextMate.
But last time I gave it a shot, it felt like uncanny valley. Very similar to TextMate, but not quite, and all the little differences added up to a shimmer I just couldn't shake. That's why I'm thinking it might be better to try something radically different.
Enter vim. It's part of the ultimate neck-beard duo of editors together with emacs. It's an editor with a
[history that traces back to the late 1970s](https://en.wikipedia.org/wiki/Vi_(text_editor))
, and it's iconically quirky. The long-running joke is that nobody knows how to even quit it when they first start (the command is :q!). But talk about standing the test of time!
The modern interpretation of vim is called
[neovim](https://neovim.io/)
, and it's got a cult following, including people whose parents weren't even born when vi originally came about. It's still vi. It's still :q! to quit. It's still quirky. But it's also fast, modern, and integrates with the latest editor evolutions like language servers.
I actually spent a summer programming in vim prior to learning Ruby, and, remarkably, a good portion of all those quirky commands have stuck in my brain. Partly because the magic of vim is it's ubiquity. Every Linux system has some version of it installed, so whenever I'm editing files on a remote system, it's with vi mode.
So we'll see. I'm still of two minds of whether I'm going to allow Apple's villainy separate me from my beloved TextMate. But I'm willing to experiment and entertain the option now.
Let's go, neovim. SHOW ME WHAT YOU GOT!
