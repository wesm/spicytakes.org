---
title: "Some questions about Docker and rkt"
date: 2016-09-15
url: https://jvns.ca/blog/2016/09/15/whats-up-with-containers-docker-and-rkt/
slug: whats-up-with-containers-docker-and-rkt
word_count: 1042
---


Hello! I have been thinking about containers at work. I’m going to talk about
running containers in production! I’ve talked before about how
[using Docker for development is great](http://jvns.ca/blog/2015/11/09/docker-is-amazing/),
but that’s not what this post is about. Using docker in development seems really great and fine and I have no problems with it.


However I have VERY MANY QUESTIONS about running Docker in production. As a
preface – I have never run containers in production. You should not take
advice from me. So far reading about containers mostly feels like [this hilarious article](https://circleci.com/blog/its-the-future/).


So: your setting is, you have a server, and you want to run programs on that
server. In containers, maybe! Should you use Docker? I have no idea! Let’s
talk about what we do know, though.


If you want to know what containers are, you could read [You Could Have Invented Container Runtimes: An Explanatory Fantasy](https://medium.com/@gtrevorjay/you-could-have-invented-container-runtimes-an-explanatory-fantasy-764c5b389bd3)


### reasons to use containers


**packaging**. Let’s imagine you want to run your application on a computer. Your application depends on some weird JSON library being installed.


Installing stuff on computers so you can run your program on them really
sucks. It’s easy to get wrong! It’s scary when you make changes! Even if you
use Puppet or Chef or something to install the stuff on the computers, it
sucks.


Containers are nice, because you can install all the stuff your program needs to run in the container **inside the container**.


packaging is a huge deal and it is probably the thing that is most interesting to me about containers right now


**scheduling**. $$$. Computers are expensive. If you have custom magical computers that are all set up differently, it’s hard to move your programs from running on Computer 1 to running on Computer 2. If you use containers, you can make your computers all the same! Then you can more easily pack your programs onto computers in a more reasonable way. Systems like Kubernetes do this automagically but we are not going to talk about Kubernetes.


**better developer environment**. If you can make your application run in a container, then maybe you can also develop it on your laptop in the same container? Maybe? I don’t really know much about this.


**security**. You can use seccomp-bpf or something to restrict which system calls your program runs? [sandstorm](https://sandstorm.io/) does stuff like this. I don’t really know.


There are probably more reasons that I’ve forgotten right now.


### ok so what’s up with the Docker daemon


Docker has a daemon. Here is an architecture diagram that I shamelessly stole from [this article](https://medium.com/@adriaandejonge/moving-from-docker-to-rkt-310dc9aec938#.mmmi6m9ql)


![](https://jvns.ca/images/docker-rkt.png)


Usually I run programs on my computers. With Docker, you have to run a magical “docker daemon” that handles all my containers. Why? I don’t know! I don’t understand what the Docker daemon is for. With rkt, you just run a process.


People have been telling me stories that sometimes if you do the Wrong
Thing and the Docker daemon has a bug, then the daemon can get deadlocked and
then you have to kill it and all your containers die. I assume they work
pretty hard on fixing these bugs, but I don’t **want** to have to trust that
the Docker daemon has no bugs that will affect me. All software has bugs!


If you treat your container more like a process, then you can just run it,
supervise it with supervisord or upstart or whatever your favorite way to
supervise a process is. I know what a process is! I understand processes, kind
of. Also I already use supervisord so I believe in that.


So that kind of makes me want to run rkt, even though it is a Newer Thing.


### PID 1


My coworker told me a very surprising thing about containers. If you run just one process in a container, then it apparently gets PID 1? PID 1 is a pretty exciting process. Usually on your computer, `init` gets PID 1. In particular, if another container process gets orphaned, then it suddenly magically becomes a child of PID 1.


So this is kind of weird, right? You don’t want your process to get random zombie processes as children. Like that might be fine, but it violates a lot of normal Unix assumptions about what normally happens to normal processes.


I think “violates a lot of normal Unix assumptions about what normally happens to normal processes” is basically the whole story about containers.


Yelp made a solution to this called [dumb-init](https://engineeringblog.yelp.com/2016/01/dumb-init-an-init-for-docker.html). It’s kind of interesting.


### networking


I wrote a pretty bad blog post about container networking a while back. It can
be really complicated! There are these “network namespaces” that I don’t
really understand, and you need to do port forwarding, and why?


Do you really need to use this complicated container networking stuff? I kind
of just want to run container processes and run them on normal ports in my
normal network namespace and leave it at that. Is that wrong?


### secrets


Often applications need to have passwords and things! Like to databases! How do you get the passwords into your container? This is a pretty big problem that I’m not going to go into now but I wanted to ask the question. (I know there are things like vault by hashicorp. Is using that a good idea? I don’t know!)


### creating container images


To run containers, you need to create container images! There seem to be two main formats: Docker’s format and rkt’s format. I know nothing about either of them.


One nice thing is that rkt can run Docker containers images. So you could use Docker’s tools to make a container but then run it without using Docker.


There are at least 2 ways to make a Docker image: using a Dockerfile and [packer](https://www.packer.io/). Packer lets you provision a container with Puppet or Chef! That’s kind of useful.


### so many questions


From the few (maybe 5?) people I’ve talked to about containers so far, the overall consensus seems to be that they’re a pretty useful thing, despite all the hype, but that there are a lot of sharp edges and unexpected things that you’ll have to make your way through.


Good thing we can all learn on the internet together.
