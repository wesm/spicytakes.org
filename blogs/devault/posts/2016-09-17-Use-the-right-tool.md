---
title: "Using the right tool for the job"
date: 2016-09-17
url: https://drewdevault.com/2016/09/17/Use-the-right-tool.html
slug: Use-the-right-tool
word_count: 527
---

One of the most important choices you’ll make for the software you write is what
you write it in, what frameworks you use, the design methodologies to subscribe
to, and so on. This choice doesn’t seem to get the respect it’s due. These are
some of the only choices you’ll make that  *you cannot change* . Or, at least,
these choices are among the most difficult ones to change.

People often question why TrueCraft is written in C# next to projects like Sway
in C, alongside KnightOS in Assembly or sr.ht in Python. It would certainly be
easier from the outset if I made every project in a language I’m comfortable
with, using tools and libraries I’m comfortable with, and there’s certainly
something to be had for that. That’s far from being the only concern, though.

A new project is a  *great*  means of learning a new language or framework - the
only effective means, in fact. However, the inspiration and drive for new
projects doesn’t come often. I think that the opportunity for learning is more
important than the short term results of producing working code more quickly.
Making a choice that’s more well suited to the problem at the expense of comfort
will also help your codebase in the long run. Why squander the opportunity to
choose something unfamiliar when you have the rare opportunity to start working
on a new project?

I’m not advocating for you to use something new for every project, though. I’m
suggesting that you detatch your familiarity with your tools from the
decision-making process. I often reach for old tools when starting a new
project, but I have learned enough about new tools that I can judge what
projects are a good use-case for them. Sometimes this doesn’t work out, too - I
just threw away and rewrote a prototype in C after deciding that it wasn’t a
good candidate for Rust.

Often it does work out, though. I’m glad I chose to learn Python for MediaCrush
despite having no experience with it (thanks again for the help with that,
Jose!). Today I still know it was the correct choice and knowing it has hugely
expanded my programming skills, and without that choice there probably wouldn’t
have been a Kerbal Stuff or a sr.ht or likely even the new API we’re working on
at Linode. I’m glad I chose to learn C for z80e, though I had previously written
emulators in C#. Without it there wouldn’t be many other great tools in the
KnightOS ecosystem written in C, and there wouldn’t be a Sway or an aerc. I’m
glad I learned ES6 and React instead of falling back on the familiar Knockout.js
when building prototypes for the new Linode manager as well.

Today, I have a mental model of the benefits and drawbacks of a lot of
languages, frameworks, libraries, and platforms I don’t know how to use. I’m
sort of waiting for projects that would be well suited to things like Rust or
Django or Lisp or even Plan 9. Remember, the skills you already know make for a
great hammer, but you shouldn’t nail screws to the wall.
