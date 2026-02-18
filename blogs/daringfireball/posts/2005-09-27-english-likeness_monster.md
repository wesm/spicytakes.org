---
title: "The English-Likeness Monster"
date: 2005-09-27
url: https://daringfireball.net/2005/09/english-likeness_monster
slug: english-likeness_monster
word_count: 2662
---


So let’s revisit the AppleScript bug I [wrote about two weeks
ago](http://daringfireball.net/2005/09/path_to), where System Events returns the wrong folder in response
to a `path to` command asking for a special folder in the `user domain`.


Here’s the bug in a nutshell:


```
set p1 to path to application support folder from user domain
-- alias "Tycho HD:Users:gruber:Library:Application Support:"

tell application "Finder"
    set p2 to path to application support folder from user domain
    -- alias "Tycho HD:Users:gruber:Library:Application Support:"
end tell

tell application "System Events"
    set p3 to path to application support folder from user domain
    -- alias "Tycho HD:Library:Application Support:"
end tell

```


I.e. within a System Events tell block, a `path to <some magic folder
name> from user domain` command will return folders from the *local
domain* (the root-level Library folder) instead.


Thanks to dozens of helpful emails from various readers (and I thank
each of you), it’s clear why this is happening: it’s a good
old-fashioned scripting dictionary terminology conflict.


The StandardAdditions OSAX defines a `path to` command, which
takes an optional `from` parameter. When you use the `from`
parameter, you must choose from the following enumerated constants:

- `system domain`
- `local domain`
- `network domain`
- `user domain`
- `Classic domain`


So, StandardAdditions defines `user domain` as a constant, with the
four-character Apple Event code `fldu`.


The problem is that System Events *also* defines `user domain`, not
as a constant, but rather as a property of the System Events
application itself. It uses the same four-character Apple Event code,
`fldu`.


Bear with me here, because we need a little background on how
AppleScript works to truly fathom just how pernicious this particular
bug is.


Compiled AppleScripts are not stored as AppleScript source code;
instead, as the name of the format implies, they are stored in a
compiled format, which format consists of Apple Event codes. 
Scripting dictionaries are the go-between; they map the English-like
syntax of AppleScript to the underlying Apple events:


AppleScript source code  ⇄  scripting dictionaries  ⇄  Apple events


The translation works both ways. You type AppleScript syntax, then
when you compile the script, it gets translated to Apple events. When
you open a saved script, AppleScript uses the dictionaries to
translate the compiled Apple events back into English-like AppleScript
source code.


Our problem above is that when we use the StandardAdditions `path to`
command, we also want to use the StandardAdditions `user domain`
enumeration. However, when we put this statement in a System Events
tell block, System Events’s dictionary gets the first crack at the
terms, and because it has its own definition of `user domain`, that’s
the one AppleScript uses. Because it uses the same AppleScript syntax
*and* the same underlying Apple Event code, there is no indication to
you, the programmer, that AppleScript has resolved `user domain` to
something other than StandardAdditions’ `user domain`.


So it compiles successfully, and when it decompiles back into
AppleScript source code, the syntax looks correct. But when it
executes, it returns the wrong result.


## Workarounds


[Daniel Jalkut](http://www.red-sweater.com/blog/) was the first of several readers to suggest the
following workaround:


> A stupid, but functional workaround would be to define your own
> “user domain” key outside the scope of the System Events tell.
> For instance, if you were going to be doing a bunch of this
> stuff in a script, you could do something like this:
> `set myUserDomain to user domain
> tell application "System Events"
>    path to application support from myUserDomain
> end tell
> `


The idea here is that `myUserDomain` gives you a reference to
StandardAdditions’ `user domain` enumeration from within the context
of a System Events tell block.


Another workaround suggested by several readers is to use System
Events’s own means of getting references to special folders, rather
than StandardAdditions’ `path to` command. For example, to get a
reference to the Fonts folder in the user domain:


```
tell application "System Events"
    set ff to fonts folder of user domain
end tell

```


But that doesn’t return a path or an alias; instead it returns a
System Events `folder` object. System Events’ `folder` class contains
properties for the path (HFS-style) and POSIX path, so if what you
want is the path (rather than a folder object), you can say something
like this:


```
tell application "System Events"
    set ff to fonts folder of user domain
    set posix_path to POSIX path of ff
    set hfs_path to path of ff
end tell

```


`posix_path` will be something like “*/Users/gruber/Library/Fonts*”, and
hfs_path will be something like “*Tycho HD:Users:gruber:Library:Fonts:*”.


So, to get the HFS-style path, you can roll this up into a single line:


```
tell application "System Events"
    set ff1 to path of fonts folder of user domain
end tell

```


Compare and contrast to the StandardAdditions syntax:


```
set ff2 to path to fonts folder from user domain

```


paying particular regard to `path of` vs. `path to` and `of user
domain` versus `from user domain`.


## Interpolation on the Failed Experiment That Is AppleScript’s English-Like Syntax


This is AppleScript at its worst. It was a grand and noble idea to
create an English-like programming language, one that would seem
approachable and unintimidating to the common user. But in this
regard, AppleScript has proven to be a miserable and utter failure.


In English, these two statements ought to be considered synonymous:


```
path of fonts folder of user domain

path to fonts folder from user domain

```


But in AppleScript, they are not, and rather are brittlely dependent on the current context. In the global scope, the StandardAdditions OSAX wants `path to` and `from user domain`; in a System Events tell block, System Events wants `path of` and `of user domain`.


The idea was, and I suppose still is, that AppleScript’s English-like
facade frees you from worrying about computer-science-y jargon like
classes and objects and properties and commands, and allows you to
just say what you mean and have it just work.


But saying what you mean, in English, almost never “just works” and
compiles successfully as AppleScript, and so to be productive you
still have to understand all of the ways that AppleScript actually
works. But this is difficult, because the language syntax is optimized
for English-likeness, rather than being optimized for making it clear
just what the fuck is actually going on.


This is why Python and JavaScript, two other scripting language of
roughly the same vintage as AppleScript, are not only better languages
than AppleScript, but are *easier* than AppleScript, even though
neither is very English-like at all. Python and JavaScript’s syntaxes
are much more abstract than AppleScript’s, but they are also more
obvious. (Python, in particular, celebrates obviousness.)


In this regard, AppleScript syntax styling in your chosen script
editor can provide essential clues. Here’s what the above examples
look like on my machine in [Script Debugger](http://www.latenightsw.com/):


The gray words are language keywords, meaning they are part of the
AppleScript programming language; the blue words are application
keywords, meaning they are defined by a scripting dictionary.1


Note that in the first statement, inside the System Events tell block,
the `of` in `path of` is a language keyword. But in the second
statement, the `to` in `path to` is an application keyword. Even more
confusing is that `path to` is preceded by a `to`, which `to` *is*
a language keyword. So you’ve got `to path to`, and one of the
`to`’s is a language keyword, and the other is an application keyword.


How is this possible? Because the second `to` is not a standalone
keyword; it’s part of StandardAdditions’ `path to` command, which is
a single token that consists of multiple space-separated words. In most
languages, this command would have been called something like
`pathTo` or `path_to`; but in AppleScript, intra-token spaces are
considered a good thing, on the grounds that they greatly increase the
resemblence to English. In practice, however, I believe
intra-token spaces are one of the most common underlying causes of
AppleScript confusion.


Similarly, note that with the StandardAdditions `path to` syntax, the
`from` in `from user domain` is an application keyword; it’s the
name of a parameter defined by the `path to` command. Whereas in the
System Events syntax, it’s just another chained `of` to access a
property of an object.


These prepositional differences are even more exasperating when you
consider that `of` and `in` are interchangeable in AppleScript. If
you can say either of the following to mean the same thing within a System
Events tell block:


```
path of fonts folder of user domain

path in fonts folder in user domain

```


and you can say this using StandardAdditions:


```
path to fonts folder from user domain

```


then it seems rather natural to assume that the `to` and `from`
might be interchangeable with other prepositions as well. But you
can’t, and if you’re not aware that StandardAdditions’s `path to` is
a single token of two words, it seems rather arbitrary, if not
downright random, which prepositions are allowed where.


(The way AppleScript lets you throw in superfluous `the`’s and `a`’s — `get the path of the fonts folder` means the same thing as `get
path of fonts folder`, and in fact means the same thing as `get the
the the path of the the the fonts folder` — makes it seems as though
AppleScript just doesn’t care about “little words”, which is true in a
handful of cases, but completely untrue in others.)


In a “normal” programming language, the equivalent to `path to fonts
folder from user domain` might be something like:


```
path_to("fonts folder", "user domain")

```


And the equivalent to `path of fonts folder of user domain` might be:


```
user_domain.fonts_folder.path

```


The point being that in most languages, these two calls don’t look at
all similar. Which is a good thing, because they *aren’t* at all
similar: one is a global command taking two parameters, the other is a
property of a property of an object. AppleScript’s slavish devotion to
English-likeness, on the other hand, gives us two very different
syntax constructs that read, to humans, as though they’re semantically
similar.


One way to disambiguate the two syntaxes in these examples would be to
use AppleScript’s `'s` (apostrophe-s) “possessive” operator instead of
the `of` keyword. The two assignments in the following example are
more or less equivalent:


```
tell application "System Events"
    set ff1 to path of fonts folder of user domain
    set ff2 to user domain's fonts folder's path
end tell

```


Matt Neuburg, in his wonderful *[AppleScript: The Definitive
Guide](http://amazon.com/exec/obidos/asin/0596005571/ref=nosim/daringfirebal-20)*, devotes an entire section to what he calls
“The ‘English-Likeness’ Monster” (from which section I’ve taken the
title of this essay). He establishes numerous problems caused by
AppleScript’s attempts to resemble English, and concludes by pointing
out that even simple variable assignment in AppleScript suffers:


> Then there is the fact that English is verbose. In most
> computer languages, you would make a variable `x` take on the
> value 4 by saying something like this:
> `x = 4
> `
> In AppleScript, you must say something like one of these:
> `copy 4 to x
> set x to 4
> `
> Doubtless not everyone would agree, but I find such expressions
> tedious to write and hard to read. In my experience, the human
> mind and eye are very good at parsing simple symbol-based
> equations and quasi-mathematical expressions, and I can’t help
> feeling that AppleScript would be much faster to write and
> easier to read at a glance if it expressed itself in even a
> slightly more abstract notational style.


## Back to the Workarounds


So, back to this:


```
tell application "System Events"
    set ff1 to path of fonts folder of user domain
end tell

```


You might be tempted to say, “Well, there you go — when you’re inside
a System Events tell block, don’t use the StandardAdditions `path to`
command, use System Events’ own means of accessing special folders
instead.”


The problem here is that System Events doesn’t know about as many
special folders as does StandardAdditions. Or, more specifically, the
System Events dictionary doesn’t define names for as many special
folders as does the StandardAdditions dictionary.


And, unfortunately, one of the folders System Events doesn’t know
about is the one we’re interested in, the Application Support folder.
Changing the above reference to the Fonts folder to:


```
tell application "System Events"
    set appsup to path of application support folder of user domain
end tell

```


won’t even compile. As of Mac OS X 10.4.2, here is the full list of
special folder properties known to System Events `user domain` object:

- applications folder
- desktop pictures folder
- Folder Action scripts folder
- fonts folder
- preferences folder
- scripting additions folder
- scripts folder
- speakable items folder
- utilities folder
- desktop folder
- documents folder
- favorites folder
- home folder
- movies folder
- music folder
- pictures folder
- public folder
- sites folder
- temporary items folder2


StandardAdditions’ dictionary defines several dozen more,3 but even it doesn’t include every
special Mac OS folder.


The full list, in the form of four-character codes, [is available in
Apple’s Carbon developer documentation](http://developer.apple.com/documentation/Carbon/Reference/Folder_Manager/folder_manager_ref/chapter_1.4_section_7.html). The folder names defined
in System Events’ scripting dictionary are just wrappers around these
four-character codes, so, to address one of the folders that the
dictionary doesn’t define, you can simply use the raw code:


```
tell application "System Events"
    set appsup to path of folder id "asup" of user domain
end tell

```


Or, using the `'s` operator:


```
tell application "System Events"
    set appsup to user domain's folder id "asup"'s path
end tell

```


(You can see here why the `'s` operator isn’t popular.)


So, at last, we’ve arrived at a complete workaround, but it requires
(a) foreknowledge of the underlying `user domain` terminology
conflict; and (b) looking up the Application Support folder’s
four-character code in the Carbon developer documention.


## Conclusion and Advice


My advice is not to use scripting addition commands from within
application tell blocks if you can avoid it. Use tell blocks only to
group statements directly related to the app that is the target of the
tell block. You’re better off with multiple tell blocks for the same
app interspersed with calls to scripting addition commands than a
single tell block that contains calls to scripting additions.


The blame for my complaint here probably lies mostly with System
Events, because its dictionary should not define a `user domain`
object that conflicts with StandardAdditions’ `user domain`
enumeration in such a way that it doesn’t produce a compile- or
run-time error. Or, perhaps the blame lies mostly with the AppleScript
compiler for allowing this terminology conflict to proceed without
error.


But I’ll also point an accusatory finger in the direction of scripting
additions in general. The problem with scripting additions is that
they pollute the global namespace with their dictionary syntax. An
application can define whatever crazy terms it wants and it won’t
adversely affect the rest of your script, because an app’s terms are
only available within tell blocks targeting that app. (Or within
`using terms from application` blocks.)


AppleScript is actually a tiny language, with extraordinarily few
keywords, but the standard scripting additions turn it into a bigger
language, ripe for terminology conflicts.


---

1. “Application keywords” also include terms defined by scripting additions, but the point is, these are terms defined by dictionaries, not the AppleScript language itself.↩︎
2. **Interesting fact**: You can ask for the “`temporary items folder`” from the user domain using either StandardAdditions or System Events, and you’ll get the path to “~/Library/Caches/TemporaryItems” instead of a sub-folder within “/private/tmp” or “private/var/tmp” (which is where `temporary items folder` resolves to if you don’t tack on the `user domain` part).↩︎
3. See p. 341 of Neuburg’s *AppleScript: The Definitive Guide* for a full listing.↩︎



| **Previous:** | [Rhymes With Ditty](https://daringfireball.net/2005/09/ditty) |
| **Next:** | [Membership Renewal 2005](https://daringfireball.net/2005/10/membership_renewal) |


PreviousNext