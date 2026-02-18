---
title: "A few things I've learned about Kubernetes"
date: 2017-06-04
url: https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/
slug: learning-about-kubernetes
word_count: 1671
---


I’ve been learning about [Kubernetes](https://kubernetes.io/) at work recently. I only started
seriously thinking about it maybe 6 months ago – my partner Kamal has
been excited about Kubernetes for a few years (him: “julia! you can run
programs without worrying what computers they run on! it is so cool!”,
me: “I don’t get it, how is that even possible”), but I understand it a
lot better now.


This isn’t a comprehensive explanation or anything, it’s some things
I learned along the way that have helped me understand what’s going on.


These days I am actually setting up a cluster instead of just reading
about it on the internet and being like “what is that??” so I am learning
much faster :)


I’m not going to try to explain what Kubernetes is. I liked Kelsey
Hightower’s introductory talk at Strange Loop called [“Managing Containers at Scale with CoreOS and Kubernetes”](https://www.youtube.com/watch?v=pozC9rBvAIs), and
Kelsey has given TONS of great Kubernetes talks over the years if you want an intro.


Basically Kubernetes is a distributed system that runs programs
(well, containers) on computers. You tell it what to run, and it
schedules it onto your machines.


### a couple sketches


I drew a couple of “scenes from kubernetes” sketches today trying to
explain very briefly things like “what happens when you add a new
node?”. Click for a bigger version.


### Kubernetes from the ground up


One of first thing that helped me understand what was going on with
Kubernetes was Kamal’s “Kubernetes from the ground up” series


He basically walks you through how all the Kubernetes components work
with each other one at a time – “look, you can run the kubelet by
itself! And if you have a kubelet, you can add the API server and just
run those two things by themselves! Okay, awesome, now let’s add the
scheduler!” I found it a lot easier to understand when presented like
this. Here’s the 3 post series:

- Part 1: [the kubelet](http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/)
- Part 2: [the API server](http://kamalmarhubi.com/blog/2015/09/06/kubernetes-from-the-ground-up-the-api-server/)
- Part 3: [the scheduler](http://kamalmarhubi.com/blog/2015/11/17/kubernetes-from-the-ground-up-the-scheduler/)


Basically these posts taught me that:

- the “kubelet” is in charge of running containers on nodes
- If you tell the API server to run a container on a node, it will tell the kubelet to get it done (indirectly)
- the scheduler translates “run a container” to “run a container on node
X”


but you should read them in detail if you want to understand how these
components interact. Kubernetes stuff changes pretty quickly, but
I think the basic architecture like “how does the API server interact
with the kubelet” hasn’t changed that much and it’s a good place to
start.


### etcd: Kubernetes’ brain


The next thing that really helped me understand how Kubernetes works is
understanding the role of etcd a little better.


Every component in Kubernetes (the API server, the scheduler, the
kubelet, the controller manager, whatever) is stateless. All of the
state is stored in a key-value store called etcd, and communication
between components often happens via etcd.


For example! Let’s say you want to run a container on Machine X. You do not
ask the kubelet on that Machine X to run a container. That is not the
Kubernetes way! Instead, this happens:

1. you write into etcd, “This pod should run on Machine X”.
(technically you never write to etcd directly, you do that through
the API server, but we’ll get there later)
2. the kubelet on Machine X looks at etcd and thinks, “omg!! it says that pod should be running and I’m not running it! I will start right now!!”


Similarly, if you want to put a container **somewhere** but you don’t
care where:

1. you write into etcd “this pod should run somewhere”
2. the scheduler looks at that and thinks “omg! there is an unscheduled
pod! This must be fixed!”. It assigns the pod a machine (Machine Y) to run on
3. like before, the kubelet on Machine Y sees that and thinks “omg! that is scheduled to run on my machine! Better do it now!!”


When I understood that basically everything in Kubernetes works by
watching etcd for stuff it has to do, doing it, and then writing the new
state back into etcd, Kubernetes made a lot more sense to me.


### The API server is responsible for putting stuff into etcd


Understanding etcd also helped me understand the role of the API server
better! The API server has a pretty straightforward set of
responsibilities:

1. you tell it stuff to put in etcd
2. if what you said makes no sense (doesn’t match the right schema),
it refuses
3. otherwise it does it


That’s not too hard to understand!


It also manages authentication (“who is allowed to put what stuff into
etcd?”) which is a pretty big deal but I’m not going to go into that
here. This [page on Kubernetes
authentication](https://Kubernetes.io/docs/admin/authentication/) is
pretty useful, though it’s kind of like “HERE ARE 9 DIFFERENT
AUTHENTICATION STRATEGIES YOU COULD USE”. As far as I can tell the
normal way is X509 client certs.


### the controller manager does a bunch of stuff


We talked about how the scheduler takes “here’s a pod that should run
somewhere” and translates that into “this pod should run on Machine X”.


There are a bunch more translations like this that have to happen:

- Kubernetes daemonsets say “run this on every machine”. There’s a “daemonset
controller” that, when it sees a daemonset in etcd, will create a pod on every
machine with that pod configuration
- You can create a replica set “run 5 of these”. The “replica set
controller” will, when it sees a replica set in etcd, create 5 pods that the scheduler will
then schedule.


The controller manager basically bundles a bunch of different
programs with different jobs together.


### something isn’t working? figure out which controller is responsible and look at its logs


Today one of my pods wasn’t getting scheduled. I thought about it for a
minute, thought “hmm, the scheduler is in charge of scheduling pods”,
and went to look at the scheduler’s logs. It turned out that I’d
reconfigured the scheduler wrong so it wasn’t starting anymore!


The more I use k8s, the easier it is to figure out which component might
be responsible when I have a problem!


### Kubernetes components can run inside of Kubernetes


One thing that kind of blew my mind was that – relatively core
Kubernetes components (like the DNS system, and the overlay networking
system) can run inside of Kubernetes! “hey, Kubernetes, please start up
DNS!”


This is basically because in order to run programs inside Kubernetes,
you only need 5 things running:

- the scheduler
- the API server
- etcd
- kubelets on every node (to actually execute containers)
- the controller manager (because to set up daemonsets you need the
controller manager)


Once you have those 5 things, you can schedule containers to run on
nodes! So if you want to run another Kubernetes component (like your
overlay networking, or the DNS server, or anything else), you can just
ask the API server (via `kubectl apply -f your-configuration-file.yaml`)
to schedule it for you and it’ll run it!


There’s also
[bootkube](https://github.com/Kubernetes-incubator/bootkube) where you
run *all* Kubernetes components inside Kubernetes (even the API server)
but that’s not 100% production ready today. Running stuff like the DNS
server inside Kubernetes seems pretty normal.


### Kubernetes networking: not impossible to understand


[this page](https://Kubernetes.io/docs/concepts/cluster-administration/networking/)
does a pretty good job of explaining the Kubernetes networking model
“every container gets an IP” but understanding how to actually make that
happen is not trivial!


When I started learning about Kubernetes networking I was very
confused about how you give every container an IP address. In retrospect I think
this was because I didn’t understand some of the fundamental networking
concepts involved yet (to understand what an “overlay network” is and
how it works you actually need to understand a bunch of things about
computer networking!)


Now I feel mostly able to set up a container networking system
and like I know enough concepts to debug problems I run into! I wrote
[a container networking overview](https://jvns.ca/blog/2016/12/22/container-networking/) where I
tried to summarize some of what I’ve learned.


This summary of how Sophie debugged a kube-dns problem ([misadventures with kube-dns](http://blog.sophaskins.net/blog/misadventures-with-kube-dns/)) is a good example
of how understanding fundamental networking concepts can help you debug
problems.


### understanding networking really helps


Here are some things that I know about now that I didn’t understand very
well, say, 2
years ago. Understanding networking concepts really helps me debug issues in
my Kubernetes cluster – if I had to debug networking issues in a
Kubernetes cluster without understanding a lot of the networking
fundamentals, I think I would just be googling error messages and trying
random things to fix them and it
would be miserable.

- overlay networks (I wrote [a container networking overview ](https://jvns.ca/blog/2016/12/22/container-networking/) about this last year)
- network namespaces (understanding namespaces in general is really
helpful for working with containers)
- DNS (because Kubernetes has a DNS server)
- route tables, how to run `ip route list` and `ip link list`
- network interfaces
- encapsulation (vxlan / UDP)
- basics about how to use iptables & read iptables configuration
- TLS, server certs, client certs, certificate authorities


### the Kubernetes source seems easy enough to read


The Kubernetes source code is all in Go which is great. The project
moves pretty fast so stuff isn’t always documented (and you end up
reading github issues sometimes to understand the current state of things),
but in general I find Go code eays to read and it’s reassuring to know
that I’m working with something written in a language I can
understand.


### the Kubernetes slack group is great


There’s a slack organization you can join by going to
[http://slack.kubernetes.io](http://slack.kubernetes.io). I usually try to figure things out on my own
instead of going there, but people there have been super super helpful
when I have asked questions.
