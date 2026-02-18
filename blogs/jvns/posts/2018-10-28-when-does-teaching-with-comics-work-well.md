---
title: "When does teaching with comics work well?"
date: 2018-10-28
url: https://jvns.ca/blog/2018/10/28/when-does-teaching-with-comics-work-well/
slug: when-does-teaching-with-comics-work-well
word_count: 1305
---


I’m speaking at [Let’s sketch tech!](https://letssketchtech.splashthat.com/) in San Francisco
in December. I’ve been thinking about what to talk about (the mechanics of making zines? how comics
skills are different from drawing skills? the business of self-publishing?). So here’s one
interesting question: in what situations does using comics to teach help?


### comics are kind of magic


The place I’m starting with is – comics often feel **magical** to me. I’ll post a comic on, for
instance, /proc, and dozens of people will tell me “wow, I didn’t know this existed, this is so
useful!”. It seems clear that explaining things with comics often works well for a lot of people.
But it’s less clear which situations comics are useful in! So this post is an attempt to explore
that.


See also [How to teach technical concepts with cartoons](https://jvns.ca/teach-tech-with-cartoons/)
which is more about techniques I use and less about “when it works”.


### what’s up with “learning styles?”


One possible way to answer the question “when does using comics to teach work well?” is “well, some
people are visual learners, and for those people comics work well”. This is based on the idea that
different people have different “learning styles” and learn more effectively when taught using their
preferred learning style.


It’s clear that different people have different learning **preferences** (for instance I like
reading text and dislike watching videos). From my very brief reading of Wikipedia, it seems less
clear that folks actually learn more effectively when taught using their preferences. So, whether or
not this is true, it’s not how I think about what I’m doing here.


Here’s all the reading I did about this (not much!):

- the [wikipedia article](https://en.wikipedia.org/wiki/Learning_styles)
- [how to talk about learning styles](http://www.learningscientists.org/blog/2016/5/8/weekly-digest-9) from a learning science blog
- [a blog post about alternative theories that might have better evidence](http://www.learningscientists.org/blog/2017/5/25-1)
- [a new york times article](https://www.nytimes.com/2010/09/07/health/views/07mind.html?_r=3&hp=&pagewanted=all) on study skills / learning styles
- the abstract of this review of [learning styles research](http://journals.sagepub.com/doi/abs/10.1111/j.1539-6053.2009.01038.x) which doesn’t find evidence that students learn better with their preferred learning style
- [a nice comic about learning styles](https://prairieworldcomicsblog.wordpress.com/2017/05/04/legacy-comic-learning-styles/) (possibly sourced from wikipedia?)


### learning preferences still matter


You could conclude from this that learning preferences don’t matter at all, and you should just
teach any given concept in the best way for that *concept*. But!! I think learning preferences still
matter, at least for me. I don’t teach in a classroom, I teach whoever feels like reading what I’m
writing on the internet! And if people don’t feel like learning the things I’m teaching because of
the way they’re presented, they won’t!


For example – I don’t watch videos to learn. (which is not to say that I’m incapable of learning
from videos, just studies show I just don’t watch them). So if someone is teaching a lot of cool
things I want to learn on YouTube, I won’t watch them!


So right now I’m reading statements like “I’m a visual learner” as a preference worth paying
attention to :).


### when comics help: diagrams


A lot of the systems I work with involve a lot of interacting systems. For example, Kubernetes is a
complicated system with many components. It took me **months** to understand how the components fit
together. Eventually I understood that the answer is this diagram:


![](https://jvns.ca/images/kube-components.png)


The point of this diagram  is that all Kubernetes’ state lives in etcd, every other Kubernetes
component decides what to do by making requests to the API server, and none of the components
communicate with each other (or etcd) directly. Those are some of the most important things to know
about Kubernetes’ architecture, which is why they’re in the diagram.


Not all diagrams are helpful though!! I’m going to pick on someone else’s kubernetes diagram ([source](https://x-team.com/blog/introduction-kubernetes-architecture/)), which is totally accurate but which I personally find less helpful.


![](https://jvns.ca/images/sad-architecture-diagram.png)


I think the way this diagram (and a lot of diagrams!) are drawn is:

- identify the components of the system
- draw boxes for each component and arrows between components that communicate


This approach works well in a lot of contexts, but personally I find it often leaves me feeling
confused about how the system works. Diagrams like this often don’t highlight the most
important/unusual architectural decisions! The way I like to draw diagrams is, instead:

- figure out what the key architecture decision(s) are that folks need to understand to use it
- draw a diagram that illustrates those architecture decisions (possibly including boxes and arrows)
- leave out parts that aren’t key to understanding the architecture


So, for that kubernetes diagram, I left out pods and the role of the kubelet and where any of these
components are running (on a master? on a worker?), because even those are very important,
they weren’t my teaching goals for the diagram.


### when comics help: explaining scenarios


Something I find really effective is to quickly explain a few important things about something
that’s really complicated like “how to run kubernetes” or “how distributed systems work”.


Often when trying to explain a huge topic, people start with generalities (“let me explain what a
linearizable system is!”). I have another approach that I prefer, which I think of as the
“scenes from” approach, or “get specific!”. (which is the same as the best way to give a lightning
talk – explain one specific interesting thing instead of trying to give an overview).


The idea is to zoom into a common specific scenario that you’ll run into in real life. For example,
a really common situation when using a linearizable distributed system is that it’ll periodically
become unavailable due to a leader election. I didn’t know that that was commmon when I started
working with distributed systems!! So just saying “hey, here is a thing that happens in practice”
can be useful.


Here are 2 example comics I’ve done in this style:


Comics are a really good fit for illustrating scenarios like this because often there’s some kind of
interaction! (“can’t you see we’re having a leader election??”)


### when comics help: writing a short structured list


I’ve gotten really into using comics to explain command line tools recently (eg the [bite size
command line zine](https://wizardzines.com/zines/bite-size-command-line)).


One of my favorite comics from that zine is the grep comic. The reason I love this comic is that it
literally includes every grep command line argument I’ve ever used, as well as a few I haven’t but
that I think seem useful. And I’ve been using grep for 15 years! I think it’s amazing that it’s
possible to usefully summarize grep in such a small space.


I think it’s important in this case that the list be **structured** – all of the things in this
list are the same type (“grep command line arguments”). I think comics work well here just because
your can make the list colourful / fun / visually appealing.


### when comics help: explaining a simple idea


I spent most of [bite size linux](https://wizardzines.com/zines/bite-size-linux) explaining various Linux ideas.
Here’s a pipes comic that I was pretty happy with! I think this is a little bit like “draw a
diagram” – there are a few fundamental concepts about pipes that I think are useful to
understand, specifically that pipes have a buffer and that writes to a pipe block if the buffer is
full.


I think comics work well for this just because you can mix text and small diagrams really easily,
and with something like pipes the tiny diagrams help a lot.


### that’s all for now


I don’t think this is the ‘right’ categorization of “when comics work for teaching” yet. But I think
this is a somewhat accurate description of how I’ve been using them so far. If you have other
thoughts about when comics work (and when they don’t!) I’d love to hear them.
