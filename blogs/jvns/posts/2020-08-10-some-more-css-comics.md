---
title: "Some more CSS comics"
date: 2020-08-10
url: https://jvns.ca/blog/2020/08/10/some-more-css-comics/
slug: some-more-css-comics
word_count: 398
---


I’ve been continuing to write pages about CSS! Here are 6 more.


Two of them are about how to think about CSS in general (“CSS isn’t easy” and
“backwards compatibility”), which is something I’m still trying to wrap my head
around.


### handling browser bugs is normal?


The fact that finding workarounds for browser bugs is kind of a normal part of
writing CSS really surprised me – there’s this great repo called
[flexbugs](https://github.com/philipwalton/flexbugs) which catalogs bugs in
browser implementations of flexbox. A lot of the bugs are in IE which means
(depending on your goals) that you can just ignore them, but not all! A bunch
of the flexbugs are in Chrome or Safari or Firefox.


For example, I ran into [flexbug #9](https://github.com/philipwalton/flexbugs#flexbug-9) a few days ago, which is
that in Safari a `<summary>` element can’t be a flexbox, so instead you need to
put an extra div inside the `<summary>` to be the flex element.


In the past I would have reacted to this in a more grumpy way (WHY?
NOOOOO? WHAT IS HAPPENING?!?! CSS?!?!?!). But this time I noticed that my site
looked weird in Safari on my iPad, figured out after 30 minutes or so that it
was a Safari bug, implemented a workaround, and it actually wasn’t that big of
a deal!


I think this mindset of “oh, there’s a browser bug, oh well, I guess that
happens sometimes!” is a lot healthier and more likely to result in success
than getting mad about it.


### there are a lot of ways CSS can go wrong


I think there are at least 3 different ways your CSS can be buggy:

1. that element doesn’t have the styles applied that it should (for example
it’s supposed to be `background; blue` but it’s `background: red` instead)
2. the element has the “right” styles applied, but those styles do something
confusing / unexpected to me because of something I misunderstood about the
CSS spec
3. the element has the “right” styles applied and those styles do the right
thing according to the spec, but the browser has a bug and isn’t
implementing the spec correctly


Anyway, enough CSS musings, here are the comics :)


### css isn’t easy


Permalink: [[https://wizardzines.com/comics/css-isnt-easy](https://wizardzines.com/comics/css-isnt-easy)](https://wizardzines.com/comics/css-isnt-easy)


### backwards compatibility


Permalink: [[https://wizardzines.com/comics/backwards-compatibility](https://wizardzines.com/comics/backwards-compatibility)](https://wizardzines.com/comics/backwards-compatibility)


### CSS specificity


Permalink: [[https://wizardzines.com/comics/css-specificity](https://wizardzines.com/comics/css-specificity)](https://wizardzines.com/comics/css-specificity)


### centering in CSS


Permalink: [[https://wizardzines.com/comics/css-centering](https://wizardzines.com/comics/css-centering)](https://wizardzines.com/comics/css-centering)


### padding syntax


Permalink: [[https://wizardzines.com/comics/padding-margin](https://wizardzines.com/comics/padding-margin)](https://wizardzines.com/comics/padding-margin)


### flexbox basics


Permalink: [[https://wizardzines.com/comics/flexbox-basics](https://wizardzines.com/comics/flexbox-basics)](https://wizardzines.com/comics/flexbox-basics)
