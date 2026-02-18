---
title: "The \"shut up and get back to work\" coding style guide"
date: 2019-04-29
url: https://drewdevault.com/2019/04/29/Shut-up-and-get-back-to-work-style.html
slug: Shut-up-and-get-back-to-work-style
word_count: 423
---

So you’re starting a new website, and you open the first CSS file. What style do
you use? Well, you hate indenting with spaces passionately. You know tabs are
right because they’re literally made for this, and they’re only one byte, and
these god damn spaces people with their bloody spacebars…

Shut up and use spaces. That’s how CSS is written 1 . And you, mister web
programmer, coming out of your shell and dipping your toes into the world of
Real Programming, writing your first Golang program: use tabs, jerk. There’s
only one principle that matters in coding style: don’t rock the boat. Just do
whatever the most common thing is in the language you’re working in. Write your
commit messages the same way as everyone else, too. Then shut up and get back to
work. This hill isn’t worth dying on.

If you’re working on someone else’s project, this goes double. Don’t get snippy
about their coding style. Just follow their style guide, and if there isn’t one,
just make your code look like the code around it. It’s none of your goddamn
business how they choose to style their code.

Shut up and get back to work.

Ranting aside, seriously - which style guide you use doesn’t matter nearly as
much as using one. Just pick the one which is most popular or which is already
in use by your peers and roll with it.

…though since I’m talking about style anyway, take a look at this:

```
struct wlr_surface *wlr_surface_surface_at(struct wlr_surface *surface,
                                           double sx, double sy,
                                           double *sub_x, double *sub_y) {
    // Do stuff
}
```

There’s a lot of stupid crap which ends up in style guides, but this is by far
the worst. Look at all that wasted whitespace! There’s no room to write your
parameters on the right, and you end up with 3 lines where you could have two.
And you have to mix spaces and tabs! God dammit! This is how you should do it:

```
struct wlr_surface *wlr_surface_surface_at(struct wlr_surface *surface,
        double sx, double sy, double *sub_x, double *sub_y) {
    // Do stuff
}
```

Note the extra indent to distinguish the parameters from the body and the
missing garish hellscape of whitespace. If you do this in your codebase, I’m not
going to argue with you about it, but I am going to have to talk to my therapist
about it.

1. For the record, tabs are objectively better. Does that mean I’m going to write my JavaScript with tabs? Hell no! ↩︎
