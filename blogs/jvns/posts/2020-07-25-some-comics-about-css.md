---
title: "Some CSS comics"
date: 2020-07-25
url: https://jvns.ca/blog/2020/07/25/some-comics-about-css/
slug: some-comics-about-css
word_count: 559
---


Hello! I’ve been writing some comics about CSS this past week, and I thought as
an experiment I’d post them to my blog instead of only putting them on Twitter.


I’m going to ramble about CSS at the beginning a bit but you can skip to the
end if you just want to read the comics :)


### why write about CSS?


I’ve been writing a tiny bit more CSS recently, and I’ve decided to [actually
take some time to learn CSS](https://jvns.ca/blog/debugging-attitude-matters/)
instead of just flailing around and deciding “oh no, this is impossible”.


CSS feels a little like systems programming / Linux to me – there are a lot of
counterintuitive facts that you need to learn to be effective with it, but I
think once you learn those facts it gets a lot easier.


So I’m writing down some facts that I found counterintuitive when learning CSS,
like the fact that `position: absolute` isn’t absolute!


### why try to read the specs?


I’ve been having a lot of fun reading
through the [CSS2 spec](https://www.w3.org/TR/CSS2/css2.pdf) and finding out
that some things about CSS that I was intimidated by (like selector specificity) aren’t as complicated as I thought.


I think reading (parts of) the CSS specs is fun because I’m so used to
learning CSS by reading a lot of websites which sometimes have conflicting
information. ([MDN](https://developer.mozilla.org) is an incredible resource
but I don’t think it’s 100% always correct either.)


So it’s fun to read a more authoritative source! Of course, it’s not always
true that the CSS specs correspond to reality – browser implementations of the
specs are inconsistent.


But expecially for parts of CSS that are older & better-established (like the
basics of how `position: absolute` works) I like reading the specs.


### how are the CSS specs organized?


CSS used to be defined by a single specification (CSS2), but as of CSS 3 each
part of CSS has its own specification. For example, there’s a CSS 3 specification
[for colours](https://www.w3.org/TR/css-color-3/).


Here are the links I’ve been using:

- there’s a PDF of the [CSS2 spec here](https://www.w3.org/TR/CSS2/css2.pdf)
- [CSS Snapshot 2018](https://www.w3.org/TR/CSS/) lists all the CSS specifications as of 2018, which is where I’ve been looking for links to the CSS 3 specifications
- [Understanding the CSS Specifications](https://www.w3.org/Style/CSS/read.en.html) is an explanation of how to approach reading the CSS specs. For example, it recommends reading [CSS sizing](https://www.w3.org/TR/css-sizing-3/) which I haven’t tried reading yet.


I’ve been kind of alternating between the CSS 2 spec and the CSS 3 specs –
because the CSS 2 spec is smaller, I find it easier to digest and understand
the big picture of how things are supposed to work without getting lost in a
lot of details.


### a few comics


Okay, here are the comics! As always when I start working on a set of comics /
a potential zine, there’s no specific order or organization.


### the box model


Permalink: [[https://wizardzines.com/comics/box-model](https://wizardzines.com/comics/box-model)](https://wizardzines.com/comics/box-model)


### CSS units


Permalink: [[https://wizardzines.com/comics/units](https://wizardzines.com/comics/units)](https://wizardzines.com/comics/units)


Reference material: I found [this section on lengths](https://www.w3.org/TR/css-values-3/#lengths) from “CSS Values and Units Module Level 3” pretty straightforward.


### selectors


Permalink: [[https://wizardzines.com/comics/selectors](https://wizardzines.com/comics/selectors)](https://wizardzines.com/comics/selectors)


Reference material: section [6.4.1 to 6.4.3](https://www.w3.org/TR/CSS2/cascade.html#cascade) from the CSS 2 spec.


### `position: absolute`


Permalink: [[https://wizardzines.com/comics/position-absolute](https://wizardzines.com/comics/position-absolute)](https://wizardzines.com/comics/position-absolute)


### inline vs block


Permalink: [[https://wizardzines.com/comics/inline-vs-block](https://wizardzines.com/comics/inline-vs-block)](https://wizardzines.com/comics/inline-vs-block)


One piece of errata for this one: you actually can set the width on an inline
element if it’s a “replaced” element
