---
title: "Bingo Card Creator 2.0 is done!  (Finally!)"
date: 2008-02-09
url: https://www.kalzumeus.com/2008/02/09/bingo-card-creator-20-is-done-finally/
slug: bingo-card-creator-20-is-done-finally
word_count: 196
---


… but not quite released yet.  I finally figured out what was giving Java problems with reading the 200 new bingo card files (stupid Windows Notepad inserting a byte order mark into UTF8 text, stupid Java not reading BOMs in UTF8 despite them being in the standard, stupid me for letting this delay a release by almost a month…)


I’ll be releasing it into the wild as soon as the site redesign is complete — ideally, sometime this weekend.  In the meanwhile, I’ve already put it on Daily Bingo Cards as sort of an early-warning-system for issues.  For once, I rather doubt there will be any.  If there were, my new and improved automated test suite would have croaked when doing the output run for all the DBC cards.


New in 2.0

- ~200 new bingo card Wizards
- better support for foreign character sets
- much, much better printing for many large words and phrases
- assorted bugsquashing
- eased some trial restrictions that were only causing problems as opposed to sales


In the crazy busyness of January I forgot about pre-announcing the price increase, so I’m going to put that off for another month.
