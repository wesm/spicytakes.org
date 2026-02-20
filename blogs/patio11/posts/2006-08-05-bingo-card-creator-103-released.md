---
title: "Bingo Card Creator 1.03 Released"
date: 2006-08-05
url: https://www.kalzumeus.com/2006/08/05/bingo-card-creator-103-released/
slug: bingo-card-creator-103-released
word_count: 292
---


Well, seeing as how I had some time free today I decided to finally get off my duff and start distributing [Bingo Card Creator 1.03](http://www.bingocardcreator.com). The main changes:

- Vastly improved memory usage while printing. Customers who try printing 50 cards on individual pieces of paper will not see the program die on low-memory machines anymore (I hadn’t anticipated anybody would try to do this and so didn’t test it… doh?)
- Printing is now threaded. This means that for folks with printers which are getting a little long in the tooth, the interface won’t appear to lock up for two minutes at a time. Its mostly a cosmetic improvement since I’m guessing after printing most people will go straight to the printer, but app responsiveness is generally a nice thing to have. For 1.04 I’ll consider putting in some sort of dialog to indicate the printing is actually currently taking place — maybe popup a progress bar somewhere.
- No more flickering — I render all the pages to get printed just off the screen in a JWindow, which means that there won’t be an ugly gray flicker in front of the main application window, and it won’t lose focus.


While at least two of these had been on the back burner for a while (“Hmm, that code is ugly and inefficient… I should fix it… sometime…”), they got kicked to the front burner *directly* after being cited as reasons for my first return. Yay for useful feedback, especially useful feedback that doesn’t technically cost me any money (did you know that processing a return through Paypal is totally free? Yeah, I was pleasantly pleased, too, but they refund your fee after you do one.), although it did cost a sale.
