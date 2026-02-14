---
title: "Scaling to multiple databases with Rails"
date: 2007-04-15
url: https://dhh.dk/posts/3-scaling-to-multiple-databases-with-rails
slug: scaling-to-multiple-databases-with-rails
word_count: 309
---


Remember that point about Rails lacking an easy-to-use way of dealing with multiple read/write databases? Strike that. [Nic Williams has released](http://drnicwilliams.com/2007/04/12/magic-multi-connections-a-facility-in-rails-to-talk-to-more-than-one-database-at-a-time/) [Magic Multi-Connections](http://magicmodels.rubyforge.org/magic_multi_connections/). It makes it dead easy to use a cluster of databases to scale read and write speeds higher than a single connection would ever allow.


That in itself is wonderful. Williams let code be his reply to the discussion of [Twitter's woes on scaling the database](http://www.loudthinking.com/arc/000608.html). I would of course rather have seen this work come out of Twitter, but I'm happy that they got a free offering handed to them regardless. They didn't even have to pass step 1 in [Brian McCallister's road map for getting stuff fixed in open source](http://kasparov.skife.org/blog/src/ruby/your-responsibility.html). And the turn-around time was within the same day of this whole thing blowing up.


Now how could this be. How could Nic fix such an apparent "critical flaw", as others have billed the lack of this facility in Rails, in such a short time? Simple, he did it in less than 75 lines of Ruby as a plugin for Rails. Less than 75 lines.


In my mind, that's the crux of the story. That extending Rails to do what you want is often much simpler than you think. That you can't compare extending a high-level framework written in a language like Ruby to, say, patching Apache or MySQL. The barriers of entry are simply not in the same sport.


So let's use this occasion to celebrate the wonders of open source ("some times you can just ask and you will receive"), but at the same time keep the effort involved in this example as a guidance for the future ("maybe next time, I could just have a look at how hard it would be to fix myself"). And of course, a big thanks to Nic Williams to making a big fuss a non-issue.

