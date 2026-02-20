---
title: "Adding some backend tracking…"
date: 2008-03-17
url: https://www.kalzumeus.com/2008/03/17/adding-some-backend-tracking/
slug: adding-some-backend-tracking
word_count: 257
---


I have been working on backend stats tracking for Bingo Card Creator to supplement Analytics.  While most of it is completed, I have to get the stats out of the Rails console, which while quite useful (arbitrary queries!) leaves something to be desired in the eye candy department.  Since I eventually want to present stats to my users, I figured I would teach myself how to use the [Plotkit Javascript library](http://media.liquidx.net/js/plotkit-doc/PlotKit.html), which makes pretty charts client-side so they don’t crash my server.


I’m sort of tired at the moment, so I can’t describe exactly everything I did to get this running (some other day, I promise), but as a proof-of-concept I graphed the total number of times bingo cards have been downloaded from Daily Bingo Cards and Bingo Card Creator (and, of course, the combined site as of March 1st).  Its a little rough around the edges but, hey, its dynamically updated.  Interested folks (and competitors ;) ) can [find it here](http://www.bingocardcreator.com/stats/bingo-card-downloads).


Two goals here:

1. Better data visualizations lead to better decisionmaking.  I really started believing this after working with CrazyEgg for a while.
2. If I can hook this sort of stuff directly into the backend sales tracking I can have the website report my monthly sales without having to do any work.  Programming is the art and science of being strategically lazy, after all.  Then that is one less blog post a month I have to write.  (Or fail to write, as the case may be — need to catch up on that tomorrow.)
