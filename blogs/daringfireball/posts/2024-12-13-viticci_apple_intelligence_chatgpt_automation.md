---
title: "Federico Viticci on Apple Intelligence, With ChatGPT, as a Breakthrough Automation Tool"
date: 2024-12-13
url: https://daringfireball.net/2024/12/viticci_apple_intelligence_chatgpt_automation
slug: viticci_apple_intelligence_chatgpt_automation
word_count: 1225
---


Federico Viticci, writing at MacStories “[Apple Intelligence in iOS 18.2: A Deep Dive into Working with Siri and ChatGPT, Together](https://www.macstories.net/stories/apple-intelligence-and-chatgpt-in-18-2/)”:


> In testing the updated Writing Tools with ChatGPT integration,
> I’ve run into some limitations that I will cover below, but I also
> had two *very* positive experiences with the Notes app that I want
> to mention here since they should give you an idea of what’s
> possible.
> In my first test, I was working with a note that contained a list
> of payments for my work at MacStories and Relay FM, plus the
> amount of taxes I was setting aside each month. The note
> originated in [Obsidian](https://obsidian.md/), and after I pasted it into Apple
> Notes, it lost all its formatting.
> There were no proper section headings, the formatting was
> inconsistent between paragraphs, and the monetary amounts had been
> entered with different currency symbols for EUR. I wanted to make
> the note look prettier with consistent formatting, so I opened the
> “Compose” field of Writing Tools and sent ChatGPT the following
> request:
> This is a document that describes payments I sent to myself each
> month from two sources: Relay FM and MacStories. The currency is
> always EUR. When I mention “set aside”, it means I set aside a
> percentage of those combined payments for tax purposes. Can you
> reformat this note in a way that makes more sense?
> I hit Return, and after a few seconds, ChatGPT reworked my text
> with a consistent structure organized into sections with bullet
> points and proper currency formatting. I was immediately
> impressed, so I accepted the suggested result, and I ended up with
> the same note, elegantly formatted just like I asked.


The other day a friend pointed out that using ChatGPT (and the like) for automation purposes is making real the original promise of AppleScript — being able to describe automation tasks using natural language. [As I wrote long ago](https://daringfireball.net/2005/09/englishlikeness_monster), the *idea* behind AppleScript was noble, but the truth is that it *is* a programming language, and in practice it has ultimately frustrated everyone. Programmers find it weird and clumsy compared to scripting languages that don’t attempt to hide that they’re programming languages, and non-programmers find it confusing because it doesn’t really parse natural language at all — it only parses a very specific syntax that happens to look like natural language, but isn’t at all like the way natural language is used or understood.


Here’s the nut of my aforementioned 2005 piece, “[The English-Likeness Monster](https://daringfireball.net/2005/09/englishlikeness_monster)”:


> In English, these two statements ought to be considered
> synonymous:
> `path of fonts folder of user domain
> path to fonts folder from user domain
> `
> But in AppleScript, they are not, and rather are brittlely
> dependent on the current context. In the global scope, the
> StandardAdditions OSAX wants `path to` and `from user
> domain`; in a System Events tell block, System Events wants `path
> of` and `of user domain`.
> The idea was, and I suppose still is, that AppleScript’s
> English-like facade frees you from worrying about
> computer-science-y jargon like classes and objects and properties
> and commands, and allows you to just say what you mean and have it
> just work.
> But saying what you mean, in English, almost never “just works”
> and compiles successfully as AppleScript, and so to be productive
> you still have to understand all of the ways that AppleScript
> actually works. But this is difficult, because the language syntax
> is optimized for English-likeness, rather than being optimized for
> making it clear just what the fuck is actually going on. [...]
> These prepositional differences are even more exasperating when
> you consider that `of` and `in` are interchangeable in
> AppleScript. If you can say either of the following to mean the
> same thing within a System Events tell block:
> `path of fonts folder of user domain
> path in fonts folder in user domain
> `
> and you can say this using StandardAdditions:
> `path to fonts folder from user domain
> `
> then it seems rather natural to assume that the “to” and “from”
> might be interchangeable with other prepositions as well. But you
> can’t, and if you’re not aware that StandardAdditions’s “path to”
> is a single token of two words, it seems rather arbitrary, if not
> downright random, which prepositions are allowed where.


But LLMs really do just parse natural language. None of that seeming nonsense with some common prepositions working in some contexts, but other common prepositions being required in others. That doesn’t mean LLM agents are always capable of doing what you want — far from it — but the best way to *try* to get them to do what you want is the same, whether you have a computer science degree or have never written a program in your life: describe what you want as clearly as possible in plain natural language. Just try to ask in the most obvious way possible, and that’s the most likely way that it will work, if it can work. That’s remarkable.


Here’s Viticci’s second example:


> The second example of ChatGPT and Writing Tools applied to regular
> MacStories work involves our annual [MacStories Selects
> awards](https://www.macstories.net/tag/macstories-selects/). Before getting together with the MacStories team
> on a Zoom call to discuss our nominees and pick winners, we
> created a shared note in Apple Notes where different writers
> entered their picks. When I opened the note, I realized that I was
> behind others and forgot to enter the different categories of
> awards in my section of the document. So I invoked ChatGPT’s
> Compose menu under a section heading with my name and asked:
> Can you add a section with the names of the same categories that
> John used? Just the names of those categories.


That worked too, leading Viticci to observe:


> Years ago, I would have had to do a lot of copying and pasting,
> type it all out manually, or write a shortcut with regular
> expressions to automate this process. Now, the “automation” takes
> place as a natural language command that has access to the
> contents of a note and can reformat it accordingly.


Like Viticci, I remain largely skeptical and uncomfortable with AI for purposes of generating original new stuff — writing, imagery, whatever. But as an assistive agent, it’s quite remarkable today and improving at a fast clip.


Not only is using Apple Intelligence for automation more accessible (in every sense) than writing a programming script or creating a Shortcut, it’s also something we’re all much more likely to do for a one-time task. I often create scripts, shortcuts, and macros to automate tasks that recur with some frequency; I seldom do for tasks that I’m only going to do once. But why not use Apple Intelligence and ChatGPT to save a few minutes of tedium?



| **Previous:** | [The Information Suggests, in an Aside, That Apple Scrapped Work on a Quad-Max/Double-Ultra M-Series Chip](https://daringfireball.net/2024/12/information_aside_double_ultra_scrapped) |
| **Next:** | [On the Accountability of Unnamed Public Relations Spokespeople](https://daringfireball.net/2024/12/on_the_accountability_of_unnamed_public_relations_spokespeople) |


PreviousNext