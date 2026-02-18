---
title: "A list of Linux container software"
date: 2016-10-02
url: https://jvns.ca/blog/2016/10/02/a-list-of-container-software/
slug: a-list-of-container-software
word_count: 339
---


I have been confused about the plethora of container software in the world. This is a
list, mostly to remind myself that there is a lot of software and so it is not surprising
that I do not understand what it all is yet.


I’ve tried to restrict this to just “software that you might reasonably want to
use/consider/understand when running containers in production”. My rough heuristic for
this is just “software someone has told me about more than once, and is not experimental”.
Obviously some of these things are more important than others.


Having written this down, I feel a bit better – there are only 17 pieces of software on
this list, from 6 different organizations. That’s actually less than I felt like it was
and I kinda sorta know what all of these things do.


The major organizations writing open source software to help people run containers on
Linux seem to be (alphabetically): Canonical, CoreOS, Docker, Google, HashiCorp, Mesosphere, Red Hat, and OCI (cross-company foundation).


I’ve tried to summarize each one in 3 words or less which is hard because a lot of this
software has a lot of different jobs.

- docker stuff
  - [docker](https://www.docker.com/)
  - [containerd](https://www.containerd.tools) (process supervisor)
  - [docker swarm](https://docs.docker.com/swarm/) (orchestration)
- Kubernetes stuff
  - [kubernetes](http://kubernetes.io/) (orchestration, has many components)
- Mesosphere stuff
  - [Mesos](http://mesos.apache.org/) (orchestration)
- CoreOS stuff
  - [CoreOS](https://coreos.com/why/) (linux distribution)
  - [rkt](https://coreos.com/rkt)  (runs containers)
  - [flannel](https://coreos.com/flannel/docs/latest/) (network overlay)
  - [etcd](https://coreos.com/etcd/) (key-value store)
- HashiCorp stuff
  - [consul](https://www.consul.io/) (key-value store, service discovery)
  - [packer](https://www.packer.io/intro/) (creates containers)
  - [vault](https://www.vaultproject.io/) (secrets management)
  - [nomad](https://www.nomadproject.io/) (orchestration)
- OCI (open container initiative) stuff
  - [runC](http://runc.io/) (runs containers)
  - [libcontainer](https://github.com/opencontainers/runc/tree/master/libcontainer) (donated by Docker, powers runC)
- systemd-nspawn ([man page](https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html)) (starts containers)
- [dumb-init](https://github.com/Yelp/dumb-init) (init process)
- [LXC](https://linuxcontainers.org/) (runs containers, from Canonical)


There are also a bunch of container registries you can pay for, like [quay (from CoreOS)](https://quay.io/), [google’s one](https://cloud.google.com/container-registry/), [docker trusted registry](https://docs.docker.com/docker-trusted-registry/), etc.


I’ve probably missed at least one important organization / piece of software here. As
usual you can tell me about it [on twitter](https://twitter.com/b0rk).
