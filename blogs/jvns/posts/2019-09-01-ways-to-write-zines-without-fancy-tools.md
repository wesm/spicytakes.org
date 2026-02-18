---
title: "How to write zines with simple tools"
date: 2019-09-01
url: https://jvns.ca/blog/2019/09/01/ways-to-write-zines-without-fancy-tools/
slug: ways-to-write-zines-without-fancy-tools
word_count: 1042
---


People often ask me what tools I use to write my zines ([the answer is
here](https://tweets.jvns.ca/b0rk/status/1160171769833185280)). Answering this question as written has
always felt slightly off to me, though, and I couldn’t figure out why for a long time.


I finally realized last week that instead of “what tools do you use to write zines?” some people may
have actually wanted to know “how can I do this myself?”! And “buy a $500 iPad” is not a terribly
useful answer to that question – it’s not how I got started, iPads are kind of a weird fancy way to
write zines, and most people don’t have them.


So this blog post is about more traditional (and easier to get started with) ways to write zines.


We’re going to start out by talking about the mechanics of how to write the zine, and then talk
about how to assemble it into a booklet.


### Way 1: Write it on paper


This is how I made my first zine (spying on your programs with strace) which you can see here: [https://jvns.ca/strace-zine-unfolded.pdf](https://jvns.ca/strace-zine-unfolded.pdf).


Here’s an example of a page I drew on paper this morning pretty quickly. It looks kind of bad
because I scanned it with my phone, but if you use a real scanner (like I did with the strace PDF
above), the scanned version comes out better.


### Way 2: Use a Google doc


The next option is to use a Google doc (or whatever other word processor you prefer). [Here’s the Google doc I wrote for the below image](https://docs.google.com/document/d/1byzfXC0h6hNFlWXaV9peJpX-GamJOrJ70x9nu1dZ-m0/edit?usp=sharing), and here’s what it looks like:


They key thing about this Google doc approach is to apply some “less is more”. It’s intended to be
printed as part of a booklet on **half** a sheet of letter paper, which means everything needs to be
twice as big for it to look good.


### Way 3: Use an iPad


This is what I do (use the Notability app on iPad). I’m not going to talk about this method much
because this post is about using more readily available tools.


### Way 4: Use a single sheet of paper


This is a subset of “Write it on paper” – the [Wikibooks page on zine making](https://en.m.wikibooks.org/wiki/Zine_Making/Putting_pages_together) has a great guide that shows how to write out a tiny zine on 1 piece of paper and then fold it up to make a little booklet. Here are the pictures of the steps from the Wikibooks page:


Sumana Harihareswara’s [Playing with
python](https://www.harihareswara.net/pix/playing-with-python-zine/playing-with-python-zine.pdf)
zine is a nice example of a zine that’s intended to be folded up in that way.


### Way 5: Adobe Illustrator


I’ve never used Adobe Illustrator so I’m not going to pretend that I know anything about it or put
together an example using it, but I hear it’s a way people do book layout.


### booklets: the photocopier method


So you’ve written a bunch of pages and want to assemble them into a booklet. One way to do this (and
what I did for my first zine about strace!) is the photocopier method. There’s a great guide by Julia Gfrörer in
[this tweet](https://twitter.com/thorazos/status/1158556879485906944), which I’m going to reproduce
here:


That explanation is excellent and I don’t have anything to add. I did it that way and it worked
great.


If you want to buy a print copy of that how-to-make-zines zine from Thruban Press, you can [get it
here on Etsy](https://www.etsy.com/thorazos/listing/693692176/thuban-press-guide-to-analog-self?utm_source=Copy&utm_medium=ListingManager&utm_campaign=Share&utm_term=so.lmsm&share_time=1565113962419).


### booklets: the computer method


If you’ve made your zine in Google Docs or in another computery way, you probably want a more
computery way of assembling the pages into a booklet.


**what I use: pdflatex**


I do this using the `pdfpages` LaTeX extension. This sounds complicated but it’s not really, you don’t
need to learn latex or anything. You just need to have pdflatex on your system, which is a `sudo apt install texlive-base` away on Ubuntu. The steps are:

1. Get a PDF with the pages from your zine (pages need to be a multiple of 4)
2. Get the latex file from [this gist](https://gist.github.com/jvns/b3de1d658e2b44aebb485c35fb1a7a0f)
3. Replace `/home/bork/http-zine.pdf` with the path to your PDF  and `1-28` with `1-however many pages are in your zine`.
4. run `pdflatex formatted-zine.tex`
5. Tweak the parameters until it looks the way you want. The [documentation for the pdfpages package is here](http://texdoc.net/texmf-dist/doc/latex/pdfpages/pdfpages.pdf)


I like using this relatively complicated method because there are always small tweaks I want to make
like “oh, the right margin is too big, crop it a little bit” and the pdfpages package has tons of
options that let me make those tweaks.


**other methods**

1. On Linux you can use the `pdfjam` bash script, which is just a wrapper around the pdfpages latex
package. This is what I used to do but today I find it simpler to use the pdfpages latex package
directly.
2. There’s a program called [Booklet Creator](https://www.bookletcreator.com/) for Mac and Windows
that [@mrfb uses](https://twitter.com/mrfb/status/1159478532545888258). It looks pretty simple to
use.
3. If you convert your PDF to a ps file (with `pdf2ps` for instance), `psnup` can do this. I tried
`cat file.ps | psbook | psnup -2 > booklet.ps` and it worked, though the resulting
PDFs are a little slow to load in my PDF viewer for some reason.
4. there are probably a ton more ways to do this, if you know more let me know


### making zines is easy and low tech


That’s all! I mostly wanted to explain that zines are an easy low tech thing to do and if you think
making them sounds fun, you definitely 100% do not need to use any fancy expensive tools to do it,
you can literally use some sheets of paper, a Sharpie, a pen, and spend $3 at your local print shop
to use the photocopier.


### resources


summary of the resources I linked to:

- Guide to putting together zines with a photocopier by Julia Gfrörer: [this tweet](https://twitter.com/thorazos/status/1158556879485906944), [get it on Etsy](https://www.etsy.com/thorazos/listing/693692176/thuban-press-guide-to-analog-self?utm_source=Copy&utm_medium=ListingManager&utm_campaign=Share&utm_term=so.lmsm&share_time=1565113962419)
- [Wikibooks page on zine making](https://en.m.wikibooks.org/wiki/Zine_Making/Putting_pages_together)
- Notes on making zines using Google Docs: [this twitter thread](https://twitter.com/mrfb/status/1159478532545888258)
- [Stolen Sharpie Revolution](http://www.stolensharpierevolution.org/) (the first book I read about
making zines). You can also get it on Amazon if you want but it’s probably better to buy directly
from their site.
- [Booklet Creator](https://www.bookletcreator.com/)
