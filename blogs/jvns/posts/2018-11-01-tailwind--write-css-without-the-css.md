---
title: "Tailwind: style your site without writing any CSS!"
date: 2018-11-01
url: https://jvns.ca/blog/2018/11/01/tailwind--write-css-without-the-css/
slug: tailwind--write-css-without-the-css
word_count: 1468
---


Hello! Over the last couple of days I put together a new website for my zines
([https://wizardzines.com](https://wizardzines.com)). To make this website, I needed to write HTML and CSS. Eep!!


Web design really isn’t my strong suit. I’ve been writing mediocre HTML/CSS for probably like 12
years now, and since I don’t do it at all in my job and am making no efforts to improve, the chances
of my mediocre CSS skills magically improving are… not good.


But! I want to make websites sometimes, and It’s 2018! All websites need to be responsive! So even
if I make a pretty minimalist site, it does need to at least sort of work on phones and tablets and
desktops with lots of different screen sizes. I know about CSS and flexboxes and media queries,
but in practice putting all of those things together is usually a huge pain.


I ended up making this site with [Tailwind CSS](https://tailwindcss.com/docs/what-is-tailwind/), and
it helped me make a site I felt pretty happy with my minimal CSS skills and just 2 evenings of work!


The Tailwind author wrote a blog post called [CSS Utility Classes and “Separation of Concerns”](https://adamwathan.me/css-utility-classes-and-separation-of-concerns/) which you should very possibly read instead of this :).


### CSS zen garden: change your CSS, not your HTML


Until yesterday, what I believed about writing good CSS was living in about 2003 with the [CSS zen
garden](http://www.csszengarden.com/). The CSS zen garden was (and is! it’s still up!) this site
which was like “hey everyone!! you can use CSS to style your websites instead of HTML tables! Just
write nice semantic HTML and then you can accomplish anything you need to do with CSS! This is
amazing!” They show it off by providing [lots](http://www.csszengarden.com/221/) [of](http://www.csszengarden.com/218/) [different](http://www.csszengarden.com/215/) designs for the site, which all use exactly the same HTML. It’s a really fun & creative thing and it obviously made an impression because I remember it like 10 years later.


And it makes sense! The idea that you should write semantic HTML, kind of like this:


```
div class="zen-resources" id="zen-resources">
   <h3 class="resources">Resources:</h3>

```


and then style those classes.


### writing CSS is not actually working for me


Even though I believe in this CSS zen garden semantic HTML ideal, I feel like writing CSS is not
actually really working for me personally. I know some CSS basics – I know `font-size` and `align`
and `min-height` and can even sort of use flexboxes and CSS grid. I can mostly center things. I made
[https://rbspy.github.io/](https://rbspy.github.io/) responsive by writing CSS.


But I only write CSS probably every 4 months or something, and only for tiny personal sites, and in
practice I always end up with some media query problem sadly googling “how do I center div” for the
500th time. And everything ends up kind of poorly aligned and eventually I get something that sort
of works and hide under the bed.


### CSS frameworks where you don’t write CSS


So! There’s this interesting thing that has happened where now there are CSS frameworks where you
don’t actually write any CSS at all to use them! Instead, you just add lots of CSS classes to each
element to style it. It’s basically the opposite of the CSS zen garden – you have a single CSS file
that you don’t change, and then you use 10 billion classes in your HTML to style your site.


Here’s an example from [https://wizardzines.com/zines/manager/](https://wizardzines.com/zines/manager/). This snippet puts images of the cover
and the table of contents side by side.


```
<div class="flex flex-row flex-wrap justify-center">
  <div class="md:w-1/2 md:pr-4">
    <img src='cover.png'>
  </div>
  
  <div class="md:w-1/2">
    <a class="outline-none" href='/zines/manager/toc.png'>
    <img src='toc.png'>
   	</a>  
  </div>
</div>

```


Basically the outside div is a flexbox – `flex` means `display: flex`, `flex-row` means
`flex-direction: row`, etc. Most (all?) of the classes apply exactly 1 line of CSS.


Here’s the ‘Buy’ Button:


```
<a class="text-xl rounded bg-orange pt-1 pb-1 pr-4 pl-4 text-white hover:text-white no-underline leading-loose" href="https://wizardzines.com/zines/oh-shit-git">Buy for $10</a>

```


The Buy button breaks down as:

- `pt, pb, pr, pl` are padding
- `text-white, hover:text-white` are the text color
- `no-underline` is `text-decoration: none`
- `leading-loose` sets `line-height: 1.5`


### why it’s fun: easy media queries


Tailwind does a really nice thing with media queries, where if you add a class `lg:pl-4`, it means
“add padding, but only on screens that are ’large’ or bigger.


I love this because it’s really easy to experiment and I don’t need to go hunt through my media
queries to make something look better on a different screen size! For example, for that image
example above, I wanted to make the images display side by side, but only on biggish screens. So I
could just add the class `md:w-1/2`, which makes the width 50% on screens bigger than ‘medium’.


```
  <div class="md:w-1/2 md:pr-4">
    <img src='cover.png'>
  </div>

```


Basically there’s CSS in Tailwind something like:


```
@media screen and (min-width: 800px) {
    .md:w-1/2 {
        width: 50%;
    }
}

```


I thought it was interesting that all of the Tailwind media queries seem to be expressed in terms of
`min-width` instead of `max-width`. It seems to work out okay.


### why it’s fun: it’s fast to iterate!


Usually when I write CSS I try to add classes in a vaguely semantic way to my code, style them with
CSS, realize I made the wrong classes, and eventually end up with weird divs with the id
“WRAPPER-WRAPPER-THING” or something in a desperate attempt to make something centered.


It feels incredibly freeing to not have to give any of my divs styles or IDs at all and just focus
on thinking about how they should look. I just have one kind of thing to edit!  (the HTML). So if I
want to add some padding on the left, I can just add a `pl-2` class, and it’s done!


[https://wizardzines.com/](https://wizardzines.com/) has basically no CSS at all except for a single `<link href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css" rel="stylesheet">`.


### why is this different from inline styles?


These CSS frameworks are a little weird because adding the `no-underline` class is literally the
same as writing an inline `text-decoration: none`. So is this just basically equivalent to using
inline CSS styles? It’s not! Here are a few extra features it has:

1. media queries. being able to specify alternate attributes depending on the size (`sm:text-orange md:text-white`) is awesome to be able to do so quickly
2. Limits & standards. With normal CSS, I can make any element any width I want. For me, this is not a good thing! With tailwind, there are only [30ish options for width](https://tailwindcss.com/docs/width), and I found that these limits made me way easier for me to make reasonable CSS choices that made my site look the way I wanted. No more `width: 300px; /* i hope this looks okay i don't know help */` Here’s the [colour palette](https://tailwindcss.com/docs/colors)! It forces you to do everything in `em` instead of using pixels which I understand is a Good Idea even though I never actually do it when writing CSS.


### why does it make sense to use CSS this way?


It seems like there are some other trends in web development that make this approach to CSS make
more sense than it might have in, say, 2003.


I wonder if the reason this approach makes more sense now is that we’re doing more generation of
HTML than we were in 2003. In my tiny example, this approach to CSS actually doesn’t introduce
**that** much duplication into my site, because all of the HTML is generated by Hugo templates, so most
styles only end up being specified once anyway. So even though I need to write this absurd `text-xl rounded bg-orange pt-1 pb-1 pr-4 pl-4 text-white hover:text-white no-underline leading-loose` set of
classes to make a button, I only really need to write it once.


I’m not sure!


### other similar CSS frameworks

- [tachyons](https://tachyons.io/)
- [bulma](https://bulma.io/)
- [tailwind](https://tailwindcss.com/)
- to some extent the much older [bootstrap](https://getbootstrap.com/), though when I’ve used that I
ultimately felt like all my sites looked exactly the same (“oh, another bootstrap site”), which
made me stop using it.


There are probably lots more. I haven’t tried Tachyons or Bulma at all. They look nice too.


### utility-first, not utility-only


Tne thing the Tailwind author says that I think is interesting is that the goal of Tailwind is not
actually for you to **never** write CSS (even though obviously you can get away with that for small
sites). There’s some more about that in [these HN comments](https://news.ycombinator.com/item?id=18084013).


### should everyone use this? no idea


I have no position on the One True Way to write (or not write) CSS. I’m not a frontend developer and
you definitely should not take advice from me. But I found this a lot easier than just about
everything I’ve tried previously, so maybe it will help you too.
