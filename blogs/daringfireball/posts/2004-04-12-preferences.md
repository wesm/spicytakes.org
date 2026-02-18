---
title: "Preferences"
date: 2004-04-12
url: https://daringfireball.net/2004/04/preferences
slug: preferences
word_count: 502
---


There’s a new item in the sidebar menu, “Preferences”. At the
moment, it provides two options: a menu to choose a default font
size, and a checkbox to display referrer listings. However, like any
preferences system, over the course of the next few years it will
expand to several hundred options.


The font size switcher addresses the number-one complaint about
Daring Fireball’s design: that the body font is “too small”. This
stemmed from the fact that (1) I specify the default font size using
px (a CSS unit of measurement that corresponds, more or less, to
screen pixels); (2) one popular browser won’t let users resize text
specified using px; and (3) that browser happens to be used by 90-95
percent of the world.


Rather than offer only a small/medium/large triumvirate of font size
options, this site’s switcher allows you to choose any size from
10–16 px, or to use the default size specified in your browser’s
preferences. (**Implementation note, of potential interest to web
nerds:** Rather than switching between multiple style sheets, I’m
still using just one screen-media style sheet, but which is partly
assembled on-the-fly using PHP tomfoolery.)


Making the referrer listings a preference, off by default, solves a
few problems. The main one is that it acts as a gentle
countermeasure against spammers. If you pay attention to DF’s
referrer listings, you may notice the daily appearance of
“referrers” which quite obviously are not actually linking to this
site, the vast majority of these forged referrers coming from our
good friends in the pornography industry.


Referrer spamming is [a growing cottage industry](http://textism.com/article/780/refer-spamming). The point of
it, however, is indirect. I don’t think these scum bags have any
interest or hope that Daring Fireball readers are particularly
likely to click a link to “gay-hitchhiker.top-porn-sites.net” (not
made up); what they’re trying do to is gain a bit of [Google juice](http://c2.com/cgi/wiki?GoogleJuice). The basic idea being:

1. Daring Fireball is at least somewhat respected by the major
search engines.
2. These search engines spider DF and take note of the sites I
link to.
3. Thus, a link to a porno site in my referrer listings will be
noted and given some iota of PageRank value by search engines.


I’m not saying this actually works for the spammers. In fact, I
strongly suspect the major search engines — Google, Yahoo, and MSN
in particular — have some anti-spam defenses in place to counter
this sort of chicanery.


But regardless, by no longer listing referrers by default, search
engine spiders will no longer see any of these links. This will have
no preventive effect whatsoever to keep the spammers out, but it
guarantees they won’t benefit from their scum-bag behavior.


## Gruber vs. Nielsen


Humility almost, but not quite, prevents me from directing your
attention to Andrei Herasimchuk’s “[Gurus v. Bloggers](http://www.designbyfire.com/000076.html)”, wherein
yours truly is pitted against Jakob “Two Wide Columns of Text Are
Better Than One” Nielsen.



| **Previous:** | [Sundry ‘Spray-On’ Clarifications and Corrections](https://daringfireball.net/2004/04/sundry_spray_on) |
| **Next:** | [Crying Wolf](https://daringfireball.net/2004/04/crying_wolf) |


PreviousNext