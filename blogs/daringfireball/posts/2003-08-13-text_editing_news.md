---
title: "Text Editing News"
date: 2003-08-13
url: https://daringfireball.net/2003/08/text_editing_news
slug: text_editing_news
word_count: 675
---


## Scriptable TextWrangler


Bare Bones yesterday released version 1.5 of [TextWrangler](http://www.barebones.com/products/textwrangler/), the $49 younger sibling of BBEdit. When I wrote about TextWrangler 1.0, [this](http://daringfireball.net/2003/02/wrangly.html) was my summary of what BBEdit offered beyond TextWrangler:

- AppleScript support; TextWrangler has no scripting dictionary.
- HTML Markup tools.
- Syntax coloring for dozens of languages.
- Glossary.
- Support for Perl and Unix shell scripting.
- File filters for multi-file search-and-replace.


That was then. This is now: TextWrangler 1.5 includes full support for AppleScript, and includes syntax coloring for numerous additional programming languages, most notably Perl, Python, Java, and TeX.


The addition of AppleScript support is huge. Many people mistakenly felt that TextWrangler 1.0 was little more than a renamed commercial version of the free BBEdit Lite; the addition of full scriptability clearly moves TextWrangler’s capabilities much closer to BBEdit’s.


Using a scriptable text editor can be incredibly useful — even if you never write a single script yourself. Most obviously, you can simply take advantage of scripts written by others. For example, almost all the BBEdit AppleScripts I post here at Daring Fireball now work in TextWrangler as well, simply by changing:


```

tell application "BBEdit"

```


to:


```

tell application "TextWrangler"

```


The only BBEdit scripts that won’t work in TextWrangler are those which pertain to BBEdit-only features, most notably the HTML tools. TextWrangler’s scriptability isn’t at all crippled — every TextWrangler feature that is scriptable in BBEdit is equally scriptable in TextWrangler.


## BBAutoComplete


Scriptability also opens up TextWrangler to third-party Apple event communication. (AppleScript is just a language wrapped around Apple event communication.) Most notably, TextWrangler now works with [Michael Tsai’s very cool BBAutoComplete](http://www.c-command.com/bbautocomplete/), which he just updated to version 1.2.


BBAutoComplete is just what it sounds like — an auto-completion tool for BBEdit. Except it doesn’t just work with BBEdit — in addition to TextWrangler, it also works with Mailsmith, Trans-Tex Software’s [Tex-Edit Plus](http://www.tex-edit.com/), and Late Night Software’s [Script Debugger](http://www.latenightsw.com/sd3.0/index.html).
It’s fast, convenient, addictive — and free.


BBAutoComplete is not a plug-in. It’s simply an application that is invoked via AppleScript, and communicates with editors via Apple events. This means that it can work with any editor that fully supports the standard Text suite of Apple events.


Tsai’s succinct description of how it works:


> You type the start of a word, press a key, and BBAutoComplete types
> 	the letters to complete the word. If BBAutoComplete guessed wrong, you
> 	can keep pressing the key to cycle through other possible completions.
> 	Other auto-completion utilities need to be taught the abbreviations and
> 	expansions that you use; BBAutoComplete avoids this hassle by
> 	automatically looking for expansions in the program’s open documents.
> 	This means that it always suggests completions that are relevant to
> 	your current task.


What I like most about BBAutoComplete is that it doesn’t kick in until and unless you invoke it. I despise auto-completing editors which automatically pop-up or flash suggested completions on-the-fly as you type. It’s like trying to write while someone else is typing in the same window. This is, of course, subject to personal taste. Regardless if you like BBAutoComplete’s style of auto-completion, you can’t argue with the fact that it wouldn’t be possible if the aforementioned editors didn’t offer terrific AppleScript support.


## Hydra


And of course if you really *do* want multiple authors typing in the same window simultaneously, [Hydra](http://hydra.globalse.org/) has been updated to version 1.1.2.


As a single-user text editor, I don’t find Hydra very interesting. But its claim to fame is multi-user shared editing via Rendezvous, which is very cool — sort of like a free-form chat session. The latest version adds another cutting-edge trick: live previews of HTML documents, powered by the [Web Kit](http://developer.apple.com/documentation/Cocoa/Reference/WebKit/ObjC_classic/Intro/IntroWK.html) renderer.


Or I suppose I should say, *the editor formerly known as Hydra*, because a [legal dispute has apparently forced a name change](http://hydra.globalse.org/news.html). That’s too bad, because *Hydra* was both catchy and very apt.



| **Previous:** | [The One and Only Mac OS X Extensions Folder](https://daringfireball.net/2003/08/the_one_and_only_mac_os_x_extensions_folder) |
| **Next:** | [On Newsstands Now](https://daringfireball.net/2003/08/on_newsstands_now) |


PreviousNext