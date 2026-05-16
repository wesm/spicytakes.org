---
title: "Moving away from Tailwind, and learning to structure my CSS"
date: 2026-05-15
url: https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/
slug: moving-away-from-tailwind--and-learning-to-structure-my-css-
word_count: 1806
---


Hello! 8 years ago, I [wrote excitedly about discovering Tailwind](https://jvns.ca/blog/2018/11/01/tailwind--write-css-without-the-css/).


At that time I really had no idea how to structure my CSS code and given the
choice between a pile of complete chaos and Tailwind, I was really happy to choose
Tailwind. It helped me make a lot of tiny sites!


I spent the last week or so migrating a couple of sites away from Tailwind and
towards more semantic HTML + vanilla CSS, and it was SO fun and SO interesting,
so here are some things I learned!


As usual I’m not a full-time frontend developer and so all of my CSS learning
has happened in fits and starts over many years.


### it turns out Tailwind taught me a lot


When I started thinking about structuring CSS, I was intimidated at first: I’m
not very good at structuring my CSS! But then I started reading blog posts
talking about how to structure CSS (like [A whole cascade of layers](https://www.miriamsuzanne.com/2022/09/06/layers/) or [How I write CSS in 2024](https://jacobb.nyc/writing/how-i-write-css-in-2024))
and I realized a couple of things:

1. Every CSS code base has a bunch of different things going on (layouts! fonts! colours! common components!)
2. It’s extremely useful to have systems or guidelines to manage each of those things, otherwise things descend into chaos
3. Tailwind has systems for some of these, and I already know those systems! Maybe I can imitate the systems I like!


For example, Tailwind has:

- a reset stylesheet
- a [colour palette](https://jvns.ca/blog/2026/05/04/css-colour-palettes/)
- a [font scale](https://v2.tailwindcss.com/docs/font-size)


### the systems I’m going to talk about


I’m going to talk about a few aspects of my CSS codebase and my thoughts so far
what kind of rules I want to impose on the codebase for each one. Some of them
are copied from Tailwind and some aren’t.

1. reset
2. components
3. colours
4. font sizes
5. utility classes
6. the base
7. spacing
8. responsive design
9. the build system


### 1. reset


I just copied Tailwind’s “[preflight styles](https://v2.tailwindcss.com/docs/preflight)”
by going into `tailwind.css` and copying the first 200 lines or so.


I noticed that I’ve developed a relationship with Tailwind’s CSS reset over time,
for example Tailwind sets `box-sizing: border-box` on every element (which means
that an element’s width includes its padding):


```
* { box-sizing: border-box; }

```


I think it would be a real adjustment for me to switch to writing CSS without
these, and I’m sure there are lots of other things in the Tailwind reset (like
`html {line-height: 1.5;}`) that I’m subconsciously used to and don’t even realize are
there.


### 2. components


This next part is the bulk of the CSS!


The idea here is to organize CSS by “components”, in a way that’s spiritually
related to Vue or React components. (though there might not actually be any Javascript at all in the site)


Basically the idea is that:

1. Each “component” has a unique class
2. The CSS for one component never overrides the CSS for any other component
3. Each component has its own CSS file


So editing the CSS for one component won’t mysteriously break something in
another component. And probably like 80% of the CSS that I would actually want
to change is in various component files, so if I’m editing a 100-line component,
I just have to think about those 100 lines. It’s way easier for me to think
about.


For example, this HTML might be the `.zine` “component”.


```
<figure class="zine horizontal">
    <img src="whatever.jpg">
</figure>

```


And the CSS looks something like this, using nested selectors:


```
.zine {
  ...
  &.horizontal {
    ...
  }
  &.vertical {
    ...
  }
  &:hover {
    ...
  }
}

```


I haven’t done anything programmatic (like web components or
[@scope](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope))
that ensures that components won’t interfere with each other, but just having a
convention and trying my best already feels like a big improvement.


Next: conventions to maintain some consistency across the site and keep these
components in line with each other!


### 3. colours


`colours.css` has a bunch of variables like this which I can use as necessary.
Colour is really hard and I didn’t want to revisit my use of colour in this
refactor, so I left this alone.


The only guideline I’m trying to enforce here is that all colours used in the
site are listed in this file.


```
:root {
  --pink: #fea0c2;
  --pink-light: #F9B9B9;
  --red: #f91a55;
  --orange: rgb(222, 117, 31);
  ...
}

```


### 4. font sizes


One thing I appreciated about Tailwind was that if I wanted to set a font
size, I could just think “hm, I want the text to be big”, write `text-lg`, and
be done with it! And maybe if it’s not big enough I’d use `xl` or `2xl` instead.
No trying to remember whether I’m using `em` or `px` or `rem`.


So I defined a bunch of variables, taken from Tailwind, like this:


```
  --size-xs: 0.75rem;
  --line-height-xs: 1rem;

  --size-sm: 0.875rem;
  --line-height-sm: 1.25rem;

```


Then if I want to set a font size, I can do it like this. It’s a little more
verbose than Tailwind but I’m happy with it for now.


```
h3 {
  font-size: var(--size-lg);
  line-weight: var(--line-weight-lg);
}

```


### 5. utilities


There are some things like buttons that appear in many different components.
I’m calling these “utilities”.


I copied some utility classes from Tailwind (like `.sr-only` for things that
should only appear for screenreader users).


This section is pretty small and I try to be careful about making changes here.


### 6. the base


“base” styles are styles that apply across the whole site that I chose myself. I
have to keep this section really small because I’m not confident enough to
enforce a lot of styles across the whole site. These are the only two I feel
okay about right now, and I might change the `<section>` one:


```
/* put a 950px column in the middle of each <section> */
section {
  --inner-width: 950px;
  padding: 3rem max(1rem, (100% - var(--inner-width))/2);
}

a {
  color: var(--orange);
}

```


I think for the base styles it’s going to be easiest for me to work kind of
bottom up – first start with almost nothing in the base styles, and then move
some styles from the components into base styles as I identify common things
I want.


### 7. spacing


I haven’t completely worked out an approach to managing padding and margins yet.
I’m definitely trying to be more principled than how I was doing it in Tailwind
though, where I would just haphazardly put padding and margins everywhere until
it looked the way I wanted.


Right now I’m working towards making the outer layout components in charge of
spacing as much as possible. For example if I have a `<section>` with a bunch of
children that I want to have space between them, I might use this to space the
children evenly:


```
section > *+* {
  margin-top: 1rem;
}

```


Some inspiration blog posts:

- [the owl selector](https://piccalil.li/blog/my-favourite-3-lines-of-css/)
- [“no outer margin”](https://kyleshevlin.com/no-outer-margin/)


### 8. responsive design: use more grid!


The way I was doing responsive design in Tailwind was to use a lot of media
queries. Tailwind has this `md:text-xl` syntax that means “apply the `text-xl`
style at sizes `md` or larger”.


I’m trying something pretty different now, which is to make more flexible CSS
grid layouts that don’t need as many breakpoints. This is hard but it’s really
interesting to learn about what’s possible with grid, and it’s a good example of
something that I don’t think is possible with Tailwind.


For example, I’ve been learning about how to use `auto-fit` to automatically use
2 columns on a big screen and 1 column on a small screen like this:


```
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 400px), max-content));
  justify-content: center;

```


I also used [`grid-template-areas`](https://wizardzines.com/comics/css-grid-areas/) a lot which is an amazing feature that I don’t think you can use with Tailwind.


Some inspiration:

- [A responsive grid layout with no media queries](https://css-tricks.com/a-responsive-grid-layout-with-no-media-queries/) from CSS Tricks


### 9. the build system: esbuild


In development, I don’t need a build system: CSS now has both built in import statements, like this:


```
@import "reset.css";
@import "typography.css";
@import "colors.css";

```


and built in nested selectors, like this:


```
.page {
  h2 { ...}
}

```


If I want, I can use `esbuild` to bundle the CSS file for production. That looks something like this.


```
esbuild style.css --bundle --loader:.svg=dataurl  --loader:.woff2=file --outfile=/tmp/out.css

```


Even though I usually avoid using CSS and JS build systems, I don’t mind using esbuild
(which I [wrote about in 2021 here](https://jvns.ca/blog/2021/11/15/esbuild-vue/))
because it’s based on web standards and because it’s a static Go binary.


### why migrate away from Tailwind?


A few people asked why I was migrating away from Tailwind. A few factors that
contributed are:

- Tailwind has become much more reliant on a build system since 2018, I think it’s
impossible (?) to use newer versions of Tailwind without using a build system.
So I’ve been using Tailwind v2 for years. (there’s also [litewind](https://litewindcss.com/) apparently)
- It’s always been true that you’re supposed to use Tailwind with a build
system, but I’ve never really done that, so I have 2.8MB `tailwind.min.css`
files in a lot of my projects and it feels a little silly.
- I’m a lot better at CSS than I was when I started using Tailwind
- Ultimately Tailwind is limiting: if you want to do Weird Stuff in your CSS,
it’s not always possible with Tailwind. Those limits can be extremely useful
(a lot of this post is about me reimplementing some of Tailwind’s limits!) but
at this point I’d like to be able to pick and choose.
- I ended up with sites that mixed both vanilla CSS and Tailwind in the same
project and that was not fun to maintain
- I got curious about what writing more semantic HTML would feel like.


### CSS features I’m curious about


While doing this I learned about a lot of CSS features that I didn’t use but am
curious about learning about one day:

- `@layer` (from [A Whole Cascade of Layers](https://www.miriamsuzanne.com/2022/09/06/layers/))
- [@scope](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope))
- [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
- [subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid)


### that’s all for now!


I still feel happy that I started using Tailwind, even if I’m moving away from
it now. I learned a lot from using it and I can still use some parts from it in
my sites even after deleting `tailwind.min.css`.


Thanks to [Melody Starling](https://melody.dev/) who originally designed and wrote the CSS for
[wizardzines.com](https://wizardzines.com), everything cool and fun
about the site is thanks to Melody.


Also I read so many incredible blog posts about CSS while working on this (from [CSS Tricks](https://css-tricks.com/), [Smashing Magazine](https://www.smashingmagazine.com/), and more), I’ve tried to link some of them
throughout this post and I really appreciate how much folks in the CSS community share their practices.
