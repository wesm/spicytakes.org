---
title: "Toolbox languages"
date: 2024-07-15
url: https://www.hillelwayne.com/post/toolbox-languages/
slug: toolbox-languages
word_count: 1703
---

A toolbox language is a programming language that’s good at solving problems without requiring third party packages. My default toolbox languages are Python and shell scripts, which you probably already know about. Here are some of my more obscure ones.


### [AutoHotKey](https://www.autohotkey.com/)


Had to show up! Autohotkey is basically “shell scripting for GUIs”. Just a fantastic tool to smooth over using unprogrammable applications. It’s Windows-only but similar things exist for Mac and Linux.


#### Useful features:

- You can configure shortcuts that are only active for certain programs, if a global flag is set, if certain text appears on screen, etc.
- Simple access to lots of basic win32 functionality. Opening the file selection dialog is just `f := FileSelect()`.
- The GUI framework is really, really good. Honestly the best of any language I’ve used, at least for small things.


#### Example problems:


[Audacity](https://www.audacityteam.org/) doesn’t let you configure mouse shortcuts, so I used AutoHotKey to map the middle-mouse to a keyboard shortcut anyway.


```
#HotIf WinActive("ahk_exe audacity.exe")
  MButton::Send "^l" ; silence selection
#HotIf

```


I made typing ``;iso`` fill in the current date.


```
:R:;iso:: 
{
    Send(FormatTime(,"yyyy-MM-dd"))
}

```


This is a tool I use to take timestamped notes.


```
; right-ctrl + d
>^d::
{
  TimeString := FormatTime(,"MM/dd hh:mm tt")
  t_msg := InputBox(,TimeString,"w200 h100")
  if t_msg.Result = "OK" {
    timestampfile := A_WorkingDir . "\Config\timestamps.txt"
    FileAppend(TimeString . "`t" . t_msg.Value . "`r`n", timestampfile)
  }
}

```


Other uses: launch REPLs for toolbox languages. Input the 100-keypress sequence required to beat one videogame (if you know, you know).


Further reading:

- [Learn AutoHotKey by stealing my scripts](https://www.hillelwayne.com/post/ahk-scripts-project/)
- [Somehow AutoHotKey is Kinda Good Now](https://www.hillelwayne.com/post/ahk-v2/)
- [In Praise of AutoHotKey](https://www.hillelwayne.com/post/ahk/)


### [J](https://code.jsoftware.com/wiki/Main_Page)


An array language, like [APL](https://en.wikipedia.org/wiki/APL_(programming_language)). Really good at doing arithmetic on arrays, hair-pullingly frustrating at doing anything with strings or structured data. I used to use it a lot but I’ve mostly switched to other tools, like [Excel](https://buttondown.email/hillelwayne/archive/excel-is-pretty-dang-cool/) and Raku. But it’s still amazing for its niches.


#### Useful features:

- It is *insanely* terse. Things that would take a several lines in most languages take a few characters in J, so I like it for quickly doing a bunch of math.
- First-class multidimensional arrays. `+` can add two numbers together, two arrays elementwise, a single number to every element of an array, or an array to every row (or column) of an higher-dimension array.
- There are lots of top-level primitives that do special case mathematical things, like decompose a number into its prime factors.


#### Example problems:


Get all of the prime factors of a number:


```
    q: 2520
2 2 2 3 3 5 7

```


Given two processes, each running a four step algorithm, [how many possible interleavings are there](https://buttondown.email/hillelwayne/archive/what-makes-concurrency-so-hard/)?


```
    ni =: !@:(+/) % */@:!
    ni 4 4
70

```


What if I wanted a table of interleavings for each value of 1 to 3 processors and 1 to 3 steps?


```
   (ni@:$)"0/~ >: i. 3
1  1    1
2  6   20
6 90 1680

```


Further reading:

- [J notation as a tool of thought](https://www.hillelwayne.com/post/j-notation/)
- [J as a desktop calculator](https://buttondown.email/hillelwayne/archive/j-as-a-desktop-calculator/)
- [How to solve sudoku](https://www.hillelwayne.com/post/sudoku/) (The appendix, mostly)


### [Frink](https://frinklang.org/)


Possibly the most obscure language on this list. Frink is designed for dimensional analysis (math with units), but it’s also got a bunch of features for covering whatever the developer thinks is interesting. Which is quite a lot of things! It’s probably the closest to “a better calculator” of any programming language I’ve seen: easy to get started with, powerful, and doesn’t have the unfamiliar syntax of J or Raku.


#### Useful features:

- Lots of builtin units and unit modifiers. `calendaryear` is exactly 365 days, `tropicalyear` is 365.24, and `half nanocentury` is about 1.6 seconds.
- Date literal notation: `# 2000-01-01 # - # 200 BC #` is 2199.01 years.
- There’s a builtin interval type for working with uncertainties. It’s a little clunky but it works.


#### Example problems:


If someone was born at midnight on Jan 1st 1970, when do they become a billion seconds old?


```
   # 1970 # + 1 billion seconds
AD 2001-09-09 AM 02:46:40.000 (Sun) Central Daylight Time

```


If I run a certain distance in a certain time, what’s my average pace?


```
   // In miles per hour
   2.5 miles / (27 minutes + 16 seconds) -> mph
5.5012224938875305623

   // In meters per hour
   2.5 miles / (27 minutes + 16 seconds) -> meters / hour
8853.3594132029339854

   // In (minutes, seconds) per mile
   1 / (4.5 miles / hour) -> [minutes/mile, seconds/mile, 0]
13, 19

```


What’s (6 ± 2) * (8 ± 1)?


```
   x = new interval [2, -2]
   (6 + x) * (8 + x/2)
[28, 72] // range is between 28 and 72

```


#### Further reading:

- [The Frink is Good, the Unit is Evil](https://www.hillelwayne.com/post/frink/)
- [A brief introduction to interval arithmetic](https://buttondown.email/hillelwayne/archive/a-brief-introduction-to-interval-arithmetic/)


### [Raku](https://raku.org/)


Raku (née Perl 6) is a *really* weird language filled to the brim with dark magic. It’s very powerful and also very easy to screw up. I’m not yet comfortable running it for a production program. But for personal scripting and toolkits, it’s incredible.


#### Useful features

- You can define your own [infix operators](https://docs.raku.org/language/functions#Defining_operators)! And postfix operators. And [*circumfix* operators](https://docs.raku.org/language/operators#Operator_classification).
- Lots and *lots* of syntactic sugar, to a level that worries me. Like instead of `[1, 2]` you can write `<1 2>`. And instead of `["a", "bc"]` you can write `<a bc>`. Raku Just Knows™ what to do.
- If you define a `MAIN` function then its parameters are turned into CLI arguments.
- Multimethods with multiple dispatch, based on runtime values. Combining this with `MAIN` makes small CLI tooling really easy.
- Many of the mathematical operators have unicode equivalents (like ∈ for ``(elem)``), which synergizes well with all of my AutoHotKey hotstrings.


#### Example problems


Generate three random 10-character lowercase strings.


```
> for ^3 {say ('a'..'z').roll(10).join}
fflqymxapa
znyxehaqvo
qwqxusudqw

```


Parse unusual structured data formats with [grammars](https://gist.github.com/hwayne/94ca3b23078234ca7e803c061b9338f3#file-format_picat-raku) (see link).


Copy a bunch of SVG ids over into inkscape labels.


```
use XML;

my $xml = from-xml-file("file.svg");

for $xml.elements(:NEST, :RECURSE<99>) -> $e {
  with $e<id> ~~ /k\w/ {
    say $_.target;
    $e.set("inkscape:label", $_.target);
  }
}
$xml.save()

```


Write a CLI with a few fiddly combinations of options ([example](https://www.hillelwayne.com/post/randomness/src/rng.raku)).


Further reading:

- [Raku, a Language for Gremlins](https://buttondown.email/hillelwayne/archive/raku-a-language-for-gremlins/)
- [An RNG that runs in your brain](https://www.hillelwayne.com/post/randomness/)
- [Raku is Surprisingly good for CLIs](https://buttondown.email/hillelwayne/archive/raku-is-surprisingly-good-for-clis/)


### [Picat](http://picat-lang.org/)


My newest toolbox language, and the language that got me thinking about toolboxes in general. A heady mix of logic programming, constraint solving, and imperative escape hatches. I first picked it up as a Better Constraint Solver and kept finding new uses for it.


#### Useful features:

- Assignment to variables. Shockingly useful in a logic language. Lots of problems felt *almost* right for logic programming, but there’d always be one small part of the algorithm I couldn’t figure out how to represent 100% logically. Imperative provided the escape hatch I needed.
- The `planner` module. I **love** the `planner` module. It is my best friend. Give it a goal and a list of possible actions, Picat will find a sequence of actions that reaches the goal. It is extremely cool.


#### Example problems:


If I run at 4.5 miles/hour for X minutes and 5.1 for Y minutes, what should X and Y be to run 3.1 miles in 38 minutes?


```
import cp.
[X, Y] :: 1..60, 45*X + 51*Y #= 31*60,  X+Y #= 38, solve([X,Y]).
X = 13
Y = 25
yes

```


Given a bunch of activities, time constraints, and incompatibilities, [figure out a vacation plan](https://gist.github.com/hwayne/c2e7d928d16de4ce3d117cf2e45d464d).


Checking if a logic puzzle has multiple solutions. Checking if the clues of a logic puzzle are redundant, or if one could be removed and preserve the unique solution.


Mocking up a quick Petri net [reachability solver](https://gist.github.com/hwayne/846faf9a841eb90a37221cebaba6d74b).


#### Further reading:

- [Planner programming blows my mind](https://www.hillelwayne.com/post/picat/)
- [Picat is my favorite new toolbox language](https://buttondown.email/hillelwayne/archive/picat-is-my-favorite-new-toolbox-language/)
- [Solving a math problem with planner programming](https://buttondown.email/hillelwayne/archive/solving-a-math-problem-with-planner-programming/)


## What makes a good toolbox language?


Most of the good toolbox languages I’ve seen are for computation and calculation. I think toolbox languages for effects and automation are possible (like AutoHotKey) but that space is less explored.


A toolbox language should be really, REALLY fast to write. At the very least, faster than Python. Compare “ten pairs of random numbers”:


```
# python

from random import randint
[(randint(10), randint(10)) for _ in range(10)]

# Raku
^10 .roll(2) xx 10

# J
10 2 ?@$ 10

```


A few things lead to this: a terse syntax means typing less. Lots of builtins means less writing basic stuff myself. Importing from a standard library is less than ideal, but acceptable. Having to install a third-party package bothers me. Raku does something cool here; the [Rakudo Star Bundle](https://rakudo.org/star) comes with a bunch of useful community packages preinstalled.


If you can do something in a single line, you can throw it in a REPL. So you want a good REPL. Most of the languages I use have good repls, though I imagine my lisp and Smalltalk readers will have words about what “good REPL” means.


Ideally the language has a smooth on-ramp. Raku has a lot of complexity but you can learn just a little bit and still be useful, while J’s learning curve is too steep to recommend to most people. This tends to conflict with being “fast to write”, though.


## Other tools I want in my toolbox

- [jq](https://github.com/jqlang/jq) for json processing
- Javascript, so I can modify other people’s websites via the dev console
- Some kind of APL that offers the benefits of J but without the same frustrations I keep having
- A concatenative PL if I ever find out what small problems a CPL is really good for
- Something that makes webscraping and parsing as easy as calculation. Requests and bs4 ain’t it.


*Thanks to [Saul Pwanson](https://saul.pw/) for feedback. If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*


*I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/).*


*My new book, [Logic for Programmers](https://leanpub.com/logic/), is now in early access! Find it [here](https://leanpub.com/logic/).*
