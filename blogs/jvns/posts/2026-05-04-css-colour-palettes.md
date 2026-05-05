---
title: "Links to CSS colour palettes"
date: 2026-05-04
url: https://jvns.ca/blog/2026/05/04/css-colour-palettes/
slug: css-colour-palettes
word_count: 282
---


A while back I decided to stop using Tailwind for new projects and to just write
vanilla CSS instead.


But one thing I missed about Tailwind was the [colour palette](https://v2.tailwindcss.com/docs/customizing-colors#color-palette-reference) ([here as CSS](https://gist.github.com/jvns/9e59b2cd1fe12601084ba78dded072fe)).
If I wanted a light blue I could just use `blue-100` and if I didn’t like it
maybe try `blue-200` or `blue-50`. I’m not very good with colours so it makes
a big difference to me to have a reasonable colour palette that somebody who is
better at colour than me has thought about.


But I’m also a little tired of those Tailwind colours, so I asked on Mastodon
today what other colour palettes were out there. And then a friend said they
wanted links to those colour palettes, so here’s a blog post so my friend can
see them, and all the rest of you too :)


### my favourites


The ones I liked the most were:

- [uchū](https://uchu.style/) ([css file](https://code.webb.page/nevercease/uchu.git/tree/dist/uchu.css), [FAQ](https://code.webb.page/nevercease/uchu.git/about/documentation/FAQ.md))
- [flexoki](https://stephango.com/flexoki) ([css file](https://github.com/kepano/flexoki/blob/main/css/flexoki.css))
- [reasonable colours](https://www.reasonable.work/artifacts/ra005-reasonable-colors/), which seems to have a focus on accessibility ([css file](https://github.com/matthewhowell/reasonable-colors/blob/master/reasonable-colors.css))


### more colour palettes

- [web awesome](https://webawesome.com/docs/color-palettes)
- [radix](https://www.radix-ui.com/colors/docs/palette-composition/scales)
- [US web design systems](https://designsystem.digital.gov/design-tokens/color/system-tokens/)
- [material design](https://m2.material.io/design/color/the-color-system.html)


### colourscheme generators


Folks also linked to a bunch of colour palette generators

- [harmonizer](https://harmonizer.evilmartians.com/)
- [tints.dev](https://www.tints.dev/)
- [coolors](https://coolors.co/)
- [colorpalette.pro](https://colorpalette.pro/)


I’ve always found these types of generators too hard to use but maybe one day I
will get better enough at colour that I’m able to use a colour palette generator
successfully so I’ll leave those links there anyway.


and more colour tools:

- [colorhexa](https://www.colorhexa.com/E97339) has some info about colorblindness


# `oklch`


[Generative colors with CSS](https://gomakethings.com/generative-colors-with-css/) gives an example of
how to use the `oklch` CSS function to dynamically generate colors.
