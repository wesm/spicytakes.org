---
title: "Do Rails programmers use node.js? Visualizing correlations in command usage"
date: 2013-10-24
url: https://jvns.ca/blog/2013/10/24/do-rails-programmers-use-node-visualizing-correlations-in-command-usage/
slug: do-rails-programmers-use-node-visualizing-correlations-in-command-usage
word_count: 125
---


A few months ago I got curious about which unix command line utilities were
the most popular, so I ran a survey on Hacker News. I ended up getting 1,500
responses or so.


Once I had that, I wanted to know how commands are related to each other: do
people who use `gcc` use `python`? What about `scala` and `clojure`?


So I made a visualization to explore this question! It shows a graph where commands which
are strongly correlated together are linked (for example `ruby` and `rails`).


[You can look at it here](http://jvns.ca/projects/unix-command-survey/graph.html).
I enjoy it a lot, especially the part of the graph around `gcc`, because it’s
pretty sparse. Try clicking ‘See the whole graph’; it’s beautiful. Just do it in
Chrome, not Firefox.
