---
title: "Open sourcing the nginx playground"
date: 2023-07-08
url: https://jvns.ca/blog/2023/07/08/open-sourcing-the-nginx-playground/
slug: open-sourcing-the-nginx-playground
word_count: 407
---


Hello! In 2021 I released a small playground for testing nginx configurations
called [nginx playground](https://nginx-playground.wizardzines.com/). There’s a
[blog post about it here](https://jvns.ca/blog/2021/09/24/new-tool--an-nginx-playground/).


This is an extremely short post to say that at the time I didn’t make it open source,
but I am making it open source now. It’s not a lot of code but maybe it’ll be
interesting to someone, and maybe someone will even build on it to make more
playgrounds! I’d love to see an HAProxy playground or something in a similar vein.


Here’s [the github repo](https://github.com/jvns/nginx-playground/). The
frontend is in `static/` and the backend is in `api/`. The README is mostly an
extended apology for the developer experience and note that the project is
unmaintained. But I did test that the build instructions work!


### why didn’t I open source this before?


I’m not very good at open source. Some of the problems I have with open sourcing things are:

- I dislike (and am very bad at) maintaining open source projects – I usually
ignore basically all feature requests and most bug reports and then feel bad about it.
I handed off maintainership to both of the open source projects that I
started ([rbspy](https://github.com/rbspy/rbspy) and [rust-bcc](https://github.com/rust-bpf/rust-bcc)) to other people who are doing a MUCH better job than I ever did.
- Sometimes the developer experience for the project is pretty bad
- Sometimes there’s configuration in the project (like the `fly.toml` or the
analytics I have set up) which don’t really make sense for other people to
copy


### new approach: don’t pretend I’m going to improve it


In the past I’ve had some kind of belief that I’m going to improve the problems
with my code later. But I haven’t touched this project in more than a year and
I think it’s unlikely I’m going to go back to it unless it breaks in some dramatic way.


So instead of pretending I’m going to improve things, I decided to just:

- tell people in the README that the project is unmaintained
- write down all the security caveats I know about
- test the build instructions I wrote to make sure that they work (on a fresh machine, even!)
- explain (but do not fix!!) some of the messy parts of the project


### that’s all!


Maybe I will open source more of my tiny projects in the future, we’ll see!
Thanks to [Sumana Harihareswara](https://www.changeset.nyc/) for helping me
think through this.
