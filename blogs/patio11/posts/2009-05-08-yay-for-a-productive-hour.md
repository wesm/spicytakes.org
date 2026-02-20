---
title: "Yay for A Productive Hour"
date: 2009-05-08
url: https://www.kalzumeus.com/2009/05/08/yay-for-a-productive-hour/
slug: yay-for-a-productive-hour
word_count: 135
---


I finally killed that little permissions error (protip: if you symlink a to b, and are wondering why you can’t access a/c, a/d, and a/e despite the preferences on a, c, d, and e all being right, check to make sure you’ve chmod-ed b/. properly.)


I also did my very first push out to github, which was slightly on the painful side (Windows user — I’m used to Rails programming having its share of pain) but cleared up fairly fast. I think I’m really going to like git for source control, although since I already have a SVN repository I’ll probably keep that as my main method.


Here’s what I did: took (a particular version of) Delayed::Job and extended it so that it can accommodate multiple workers at once. You can see the details [here](http://github.com/patio11/delayed_job/tree/master).
