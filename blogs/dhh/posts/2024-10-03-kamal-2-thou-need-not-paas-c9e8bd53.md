---
title: "Kamal 2: Thou need not PaaS"
date: 2024-10-03
url: https://world.hey.com/dhh/kamal-2-thou-need-not-paas-c9e8bd53
slug: kamal-2-thou-need-not-paas-c9e8bd53
word_count: 318
---

[Kamal](https://kamal-deploy.org/)
was our ticket out of the cloud. A simple tool for deploying containerized applications onto our own hardware, without the need for the complexity of something like Kubernetes.
[Kamal 2](https://dev.37signals.com/kamal-2/)
is a huge leap forward for that tool, and it has just shipped.
Now you can deploy multiple applications to the same server, and you can have SSL certificates automatically provisioned via Let's Encrypt. A big compression in complexity, especially when just getting started.
Because Kamal isn't just for high-end cloud exits where applications rely on an entire fleet of machines. It's also an excellent option for running a bunch of smaller apps on a single server. Imagine just how you can run on
[one of those amazing Hetzner EPYC 9454 boxes](https://www.hetzner.com/dedicated-rootserver/ax162-r/configurator/#/)
with 96 threads and 256GB of RAM that they sell for $220/month!
[Our move out of the cloud](https://basecamp.com/cloud-exit)
would not has been nearly as smooth or as fast without Kamal. And I'm thrilled we can share such a tool with everyone else who might want to reconsider the cost of Platform-as-a-Service setups. Kamal works great whether you're starting on a cheap $5 VPS, moving onto a fleet of cloud VMs, using dedicated-but-managed servers, or running your own hardware entirely.
In fact, it's chief mission is to allow you to move through all those stages of a production deployment without onerous migration costs or delays. We can't have competition in the cloud as long as folks are locked into proprietary or overly-complicated setups that makes moving from one vendor to another a huge hassle and expense.
If this sounds at all appetizing,
[checkout the new Kamal 2 demo](https://www.youtube.com/watch?v=QC4b2teG_hc)
, which shows how to deploy a simple Go application (Kamal isn't just for Rails!), how to add another Rails app on the same box, and how to move that Rails app onto a three-machine Hetzner cloud setup. All in under half an hour.
Enjoy Kamal 2!

![kamal-demo.webp](https://world.hey.com/dhh/c9e8bd53/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTgzNTY4MjkwMywicHVyIjoiYmxvYl9pZCJ9fQ--1c72af5b68153728f967da3cf83dd88d09dc0fe9ccd076125460f85759daed67/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJ3ZWJwIiwicmVzaXplX3RvX2xpbWl0IjpbMzg0MCwyNTYwXSwicXVhbGl0eSI6NjAsImxvYWRlciI6eyJwYWdlIjpudWxsfSwiY29hbGVzY2UiOnRydWV9LCJwdXIiOiJ2YXJpYXRpb24ifX0--12725a832e6e7b2dd7d56a507f20442609781a7502597503a7a5e38f72548391/kamal-demo.webp)

