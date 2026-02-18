---
title: "Running containers without Docker"
date: 2016-10-26
url: https://jvns.ca/blog/2016/10/26/running-container-without-docker/
slug: running-container-without-docker
word_count: 1252
---


Right now at work, my team’s job is basically to be Heroku for the rest of the
company – we want it to be really easy for developers to run and operate code
on our servers.


I’m not going to talk right now about why “make it easier for developers to
run code on our servers” might involve “containers”, because that’s a whole other
post. Let’s suppose we believe that.


So if you have a bunch of existing infrastructure that you maybe want to move
to containers, what’s the migration plan? How do you get from here to there?


I was having trouble coming up with a migration plan that made sense to me,
but with the help of some delightful coworkers now I have one  that I think
makes sense! This post makes an argument for that migration plan! Here’s the
tl;dr: (as usual everything that is wrong in this post is my responsibility
:))

1. You can run containers without using Docker or Kubernetes or Mesos or anything like that
2. Running containers has a bunch of advantages even with no Docker
3. If you’re going to move to Docker/k8s eventually, you need to containerize *anyway*. You can separate out this work into a smaller project!
4. so this might be a good migration plan if you want to eventually move to Kubernetes or something


As usual I am not a container expert. I am just trying to figure out how to
use them. Maybe this will be useful to you too! I’m writing this because I
think having more ideas for migration plans on the internet to think about and
compare is a good thing.


### vertical change vs horizontal change


If you’re trying to make a big infrastructure change (like migrate to
Kubernetes), there are basically two ways to do it. You could make a new small
Kubernetes cluster which contains all your hopes and dreams, and slowly
migrate things into the new cluster.


The second way is to incrementally roll out small changes. So you start out
making a bunch of changes horizontally across your infrastructure, and move
everything a little towards Kubernetes, and a little more, and a little more,
and a little more, and then finally hopefully you have what you want.


Right now making changes horizontally feels less risky to me, because it means
you can check that your changes will actually work everywhere and there’s less
danger of “we have this cool new world but a bunch of our software can’t
actually use any of it right now”.


But there are also good things about building the Cool New World first! You can
start to learn how to operate your Cool New World by deploying less critical
applications there.


### what does “use containers without Docker” mean (and why you might want to start without Docker)


I mean a pretty specific thing by “just use containers”. We learned [a while back](https://jvns.ca/blog/2016/09/15/whats-up-with-containers-docker-and-rkt/) that Docker has a daemon. This daemon does a **bunch** of stuff for you, like

- supervising your containers and restarting them when they stop
- redirecting your programs’ logs
- letting you run commands like `docker ps` to see what you have running on the box
- I don’t even know what else


Lots of cool orchestration features like with Kubernetes or Mesos or Docker
Swarm mean that I need to learn how the software works and how it operates and
exactly how it can fail in production. Which I am okay with doing, eventually!
But in the short term, if I want to deploy changes that I can confidently run in
production, using all kinds of exciting features like this just slows me down.


So, what’s the minimal way to use containers, where you use as few features as
possible but still get some advantages?


Right now I think it’s:

- build a container image. Use whatever you want to do this (a Dockerfile, [packer](https://www.packer.io/), whatever). You can use as many fancy tools as you want to build your containers.
- run that container with [rkt](https://github.com/coreos/rkt). rkt just runs containers, the same way you run a program. I know how to run programs! This is awesome.
- run the container in your host network namespace (same place as before) so you don’t need to worry about any fancy networking business
- supervise it the same way you supervise things currently
- run the container in its own pid namespace


And rkt is mostly just responsible for starting up my process in a reasonable
environment and passing on any signals it gets to my process. It seems like it
would be hard to screw that up too much. (though, as usual with software, who
knows what will happen until you try)


rkt actually does a bit more than I’ve described – it keeps a local store of
containers on your machine, it does a bunch of security checks at runtime, and
it runs systemd as an init process inside your container. There’s probably more
that I don’t understand yet, too.


### what just containers can do for me


Three things I would really like:

- have less lines of puppet configuration that I am scared of changing
- stop thinking in terms of how to provision specific computers (“I need to put this file at /etc/awesome/blah.xml on this computer”), and worry more about services (“this program always needs /etc/awesome/blah.xml to exist”)
- have better standards around how we run services (less special snowflakes)


I think that just using containers by itself will force us to be disciplined
about how we package and run services (you have to install all the stuff the
service needs inside the container, otherwise the service will not work!).


There’s no way for it to silently depend on the host configuration, because
its filesystem is totally separate from the host’s filesystem.


To get these advantages, you don’t need to run Docker or Kubernetes or Mesos
or anything! You just need to have a container that is isolated from the rest
of your operating system.


To be clear, I don’t necessarily think it makes sense to stop at “just use
containers”. This is just about separating work into smaller useful chunks.


### migrating to using containers without docker might be really easy!


The exciting thing to me about “use containers without docker” is that I don’t
need to learn how to operate any new programs in production. I’m hoping that
if we do this, we can get it done pretty quickly, and then move on to the
business of deciding how to manage the containers.


And you’ll have to do all this “make your programs work with containers” work
anyway to use *any* containerization magic! So you’re just doing work that
you’d have to do anyway.


### cautiously optimistic


I used to be really annoyed about containers because it seemed like a
buzzword. But it seems like right now a lot of the thinking & software being
built around “make it easy for developers to run code” is happening in the
context of containers. So it seems like it’s worth it for me to learn what’s
happening in containerland!


So I’m going to try this stuff out, but I think we’re going to start slowly and
introduce as little new software into our production environments at a time as
I can :)


thanks to Kamal for reading this and being the best. Also to
[Greg](https://github.com/grepory) my coworker who is the best for telling me
many things about containers.
