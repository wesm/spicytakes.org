---
title: "How I wish I could organize my thoughts"
date: 2022-08-10
url: https://drewdevault.com/2022/08/10/Organizing-my-thoughts.html
slug: Organizing-my-thoughts
word_count: 698
---

I keep a pen & notebook on my desk, which I make liberal use of to jot down my
thoughts. It works pretty well: ad-hoc todo lists, notes on problems I’m working
on, tables, flowcharts, etc. It has some limitations, though. Sharing anything
out of my notebook online is an awful pain in the ass. I can’t draw a straight
line to save my life, so tables and flowcharts are a challenge. No edits,
either, so lots of crossed-out words and redrawn or rewritten pages. And of
course, my handwriting sucks and I can type much more efficiently than I can
write. I wish this was a digital medium, but there are not any applications
available which can support the note-taking paradigm that I wish I could have.
What would that look like?

Well, like this (click for full size):

I don’t have the bandwidth to take on a new project of this scope, so I’ll
describe what I think this should look like in the hopes that it will inspire
another team to work on something like this. Who knows!

The essential interface would be an infinite grid on which various kinds of
objects can be placed by the user. The most important of these objects would be
pages, at a page size configurable by the user (A4 by default). You can zoom in
on a page (double click it or something) to make it your main focus, zooming in
automatically to an appropriate level for editing, then type away. A simple
WYSIWYG paradigm would be supported here, perhaps supporting only headings,
bold/italic text, and ordered and unordered lists — enough to express your
thoughts but not a full blown document editor/typesetter. 1  When you run out
of page, another is generated next to the current page, either to the right or
below — configurable.

Other objects would include flowcharts, tables, images, hand-written text and
drawings, and so on. These objects can be placed free form on the grid, or
embedded in a page, or moved between each mode.

The user input paradigm should embrace as many modes of input as the user wants
to provide. Mouse and keyboard: middle click to pan, scroll to zoom in or out,
left click and drag to move objects around, shift+click to select objects, etc.
A multi-point trackpad should support pinch to zoom, two finger pan, etc. Touch
support is fairly obvious.  [Drawing tablet](https://en.wikipedia.org/wiki/Graphics_tablet)  support is also important: the
user should be able to use one to draw and write free-form. I’d love to be able
to make flowcharts by drawing boxes and arrows and having the software recognize
them and align them to the grid as first-class vector objects. Some drawing
tablets support trackpad and touch-screen-like features as well — so all
of those interaction options should just werk.

Performance is important here. I should be able to zoom in and out and pan
around while all of the objects rasterize themselves in real-time, never making
the user suffer through stuttery interactions. There should also be various ways
to export this content. A PDF exporter should let me arrange the pages in the
desired linear order. SVG exporters should be able to export objects like
flowcharts and diagrams. Other potential features includes real-time
collaboration or separate templates for presentations.

Naturally this application should be free software and should run on Linux.
However, I would be willing to pay a premium price for this tool — a
one-time fee of as much as $1000, or subscriptions on the order of $100/month if
real-time collaboration or cloud synchronization are included. If you’d like
some ideas for how to monetize free software projects like this, feel free to
swing by  [my talk on the subject](https://hackmeeting.org/hackit22/schedule.html#talk-a2eb7aa1-90ac-48b9-8ac9-b16235eb2daf)  in Italy early this September to talk about
it.

Well, that’s enough dreaming for now. I hope this inspired you, and in the
meantime it’s back to pen and paper for me.

1. Though perhaps you could import pages from an external PDF, so you can
typeset stuff in LaTeX or whatever and then work with those documents inside
of this tool. Auto-reload from the source PDFs and so on would be a bonus for
sure. ↩︎
