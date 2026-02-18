---
title: "Day 57: Trying to set up GitHub Actions"
date: 2021-02-10
url: https://jvns.ca/blog/2021/02/10/day-57--fighting-with-github-actions/
slug: day-57--fighting-with-github-actions
word_count: 263
---


On Monday I got a very exciting pull request on [rbspy](https://github.com/rbspy/rbspy) which implements a feature that I’ve wanted to implement for years – identifying C functions!


Previously if there was a C function in the stack, rbspy would just call it `<c function> - unknown`. But it turns out that there’s actually support in Ruby’s `.gdbinit` for finding the name of these C functions, and this [new PR](https://github.com/rbspy/rbspy/pull/282) ports that into rbspy!!


I still haven’t totally understood how the PR works, but I spent a bunch of time with Tim and Mikkel yesterday trying to understand it and it was really fun. I might write about this more later after I’ve understood what it’s doing better.


### debugging CI is frustrating


While trying to merge some other rbspy PRs I ran into this chain of events:

- merge pull request
- realize that the Travis builds are getting slower at building the releases
- think “maybe I’ll implement GitHub actions, how hard can it be?”
- spent a billion years trying to debug various things in GitHub actions
- get very sad


This was just exactly the same as every other time I’ve tried to set up CI –
it’s fine, but it’s always kind of frustrating.


But when I woke up this morning and opened Twitter I saw a tweet from someone who was also having a sad GitHub Actions day, and someone in their replies suggested this [debugging with tmate](https://github.com/marketplace/actions/debugging-with-tmate) action to let you ssh in! So I’m going to try that and maybe that will make everything a lot easier.
