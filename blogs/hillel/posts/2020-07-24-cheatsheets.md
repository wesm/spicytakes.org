---
title: "A Better Cheatsheet"
date: 2020-07-24
url: https://www.hillelwayne.com/post/cheatsheets/
slug: cheatsheets
word_count: 1328
---

Now that [teach workshops](https://www.hillelwayne.com/consulting/) for a living, I spend a lot of time on making better workshops. One improvement I made was creating **progressive cheatsheets**. I’ll discuss the motivation and implementation below, but this is the high level picture:


![](cs-1.png)

*Progressions #1 and #2 of the cheatsheet. Click for full size.*


I’m assuming you know “why cheatsheets”. You’d rather look at one page of essentials than an entire book. But they have problems and we can make them a lot better.


## Starting point


I currently run workshops for two languages, [TLA+](https://www.hillelwayne.com/talks/distributed-systems-tlaplus/) and [Alloy](https://www.hillelwayne.com/post/formally-modeling-migrations/), and need cheatsheets for both. Both already have public cheatsheets, but while I can use the [Alloy one](https://homepage.cs.uiowa.edu/~tinelli/classes/181/Fall17/Notes/alloy-cheatsheet.pdf) as-is, the [TLA+ cheatsheet](https://lamport.azurewebsites.net/tla/summary-standalone.pdf) is several pages long. Cheatsheets should be at most one page. Past two and nobody looks at them. Step one, make a one page version.


My tool of choice here is LaTeX, a typesetting DSL that grew wildly beyond its original niche. It’s the best tool for fine control over layouts. This is less because of its own intrinsic quality and more because everything else is far, far worse.


I found a cheatsheet template [here](https://github.com/tim-st/latex-cheatsheet). It divides the material into sections and the layout into columns.  LaTeX computes how to layout the content in the columns for me. This is nice because I didn’t know at the start how much content I needed or how to best group it. I could reorder sections and have the entire thing automatically reflow. Unfortunately, LaTeX is very finicky and I’d often end up with content overflowing the columns. But fixing weird LaTeX errors is still better than trying to lay everything out manually.


The basic cheatsheets got me going for a while, but then I started running into problems. Not ones that make cheatsheets useless, but ones that made them *slower*.


## Cheatsheet Theory


Cheatsheets need to be dense. The more information you pack into a single page, the more likely someone’s going to find what they need… if they already know *what* they need.


If a student don’t know what exactly they need, they might try to apply the wrong idea. Things like using `with` when they actually need `CHOOSE`, switching function and function-set notation, things like that.


This is a much bigger problem while they’re still learning the material. They don’t yet have a mental model, so they don’t know what material is relevant and what isn’t. Most of the cheatsheet is material we haven’t covered yet. This has two failures modes:

1. They don’t realize it’s future material and try to use it in the wrong place. Example: writing `set SUBSET set2` instead of `set1 \subseteq set2`.1
2. They know it’s not relevant, but it adds so much noise they have trouble *locating* the relevant things.


My workshops are long and cover challenging material. I’m already stuffing an entire discipline into my students’ brains, no need to add *more* difficulty on top of that. So I looked for ways to fix this problem.


## First Implementation


The most direct solution is to hide anything that I haven’t covered yet.  Instead of giving the students a single cheatsheet, I give them seven. After the first lesson, they get cheatsheet #1, which covers *only* the first lesson. After the second lesson, they get cheatsheet #2, which covers both the first and second lesson. I do this all the way to the final version of the cheatsheet, which has everything.


We can do this with the [etoolbox](https://ctan.org/pkg/etoolbox?lang=en) package in LaTeX. We define a switch with `newtoggle`, like `\newtoggle{temporal logic}`. Then we create a new `main.tex` file which we import into cheatsheet. In the root document, we do


```
\newtoggle{topic A}
\newtoggle{topic B}
\newtoggle{topic C}


% ...

\input{main}
\toggletrue{topic A}
\input{main}
\toggletrue{topic B}
\input{main}
\toggletrue{topic C}

```


This means that each instance of main will have all of the previous switches active. Now we can write:


```
\iftoggle{topic B}{content}{}

```


If the toggle is true, we process as normal. If the toggle is false, we skip rendering the entire section. Now I can be sure that the *only* things the student is seeing is stuff that we already covered.


This solves the problem nicely. No noise and no red herrings. But we can do better!


## Second Implementation


Topics in the cheatsheet are laid out in topic order, not *lesson* order. Think about something like Python functions: you’d put variadic argument syntax right after the regular syntax, even though one is a beginner topic and the other is an advanced topic.


So the final cheatsheet might look like this:



| column | column |
| A | C |
| B | D |



What should the cheatsheet that only covers A & D look like? If we remove C & B, LaTeX will recalculate the page layout as



| column | column |
| A |  |
| D |  |



In the earlier cheatsheet the student sees A in the top left and D in the bottom left. But in the cheatsheet with all four topics, the bottom left is now C. If the student got used to seeing D in the bottom left, they’ll have to break their habit and relearn the new location. The problem gets worse as we add more topics and progressions to the sheet.


This might seem like a minor problem, but I don’t like it. It’s extra mental overhead for the students that has nothing to do with the actual material. Accidental difficulty, not essential difficulty. I want it out. Every piece of content should be in the exact same place on every single cheatsheet.


I thought this would be pretty tough. I’d have to tell LaTeX to layout the doc as if all the content was there, but not actually render chunks of text. That seemed like expert-level LaTeX wizardry.


So I cheated.


```
\newenvironment{requires}[1]
{
 \iftoggle{#1}{
   % We've passed this point, show normal
 }{
   \color{white} % Hide text
   \rowcolors{2}{white}{white} % Hide tables
} 
}

```


Instead of using a “raw” `\iftoggle`, I created a new wrapping environment. If the toggle is true, we proceed as normal. If it’s false, though, I make all the text in the environment white. The text is still rendered, meaning the layout is consistent between sheets. But nobody can *see* it, so it’s not distracting. It gets the job done!


The main downside is this doesn’t work inside tables. Something about nested environments driving LaTeX crazy. But I can wrap the whole table in a `requires` block, so by splitting tables up I can sort of get the benefits here. The aesthetics are worse but eh.


If you want to make your own progressive cheatsheets, here’s a [sample template](progressive-cheat-sheet.zip) which produces [this sample output](cheat-sheet.pdf).


## Results


I first got to test this at a Facebook workshop back in November. It worked spectacularly. People who used the progressions from the start had a much easier time finding the right material than people who just used the final version of the cheatsheet. The first group also had fewer false negatives, where they tried to use the wrong concept. I consider this a big success. Three notes, though:

1. At first I gave the next progression out *before* the mid-lesson exercises. People would then try to use material from the *second* half of the module. I quickly switched to giving them out before the end-of-module exercises, after I had covered everything.
2. It’s really easy to forget to pass out progressions. I added new slides to the lecture notes at each new handout point.
3. Don’t collate.


Hope you enjoyed this peek into my design process! If you’re thinking “wow this person actually gives a crap about teaching” feel free to [reach out](https://www.hillelwayne.com/consulting/) if you’re interested in a corporate workshop, or join my newsletter [here](https://buttondown.email/hillelwayne/) for announcements about new public workshops!


*Thanks to Lito Nicolai and for [Greg Wilson](http://third-bit.com/) for feedback.*


---

1. In TLA+, `SUBSET P` is the power set of P. 
 [return]
