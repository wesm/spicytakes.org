---
title: "New talk: High Reliability Infrastructure Migrations"
date: 2018-12-15
url: https://jvns.ca/blog/2018/12/15/new-talk--high-reliability-infrastructure-migrations/
slug: new-talk--high-reliability-infrastructure-migrations
word_count: 553
---


On Tuesday I gave a talk at KubeCon called [High Reliability Infrastructure
Migrations](https://www.youtube.com/watch?v=obB2IvCv-K0). The abstract was:


> For companies with high availability requirements (99.99% uptime or higher), running new software
> in production comes with a lot of risks. But it’s possible to make significant infrastructure
> changes while maintaining the availability your customers expect! I’ll give you a toolbox for
> derisking migrations and making infrastructure changes with confidence, with examples from our
> Kubernetes & Envoy experience at Stripe.


## video


### slides


Here are the slides:


since everyone always asks, I drew them in the Notability app on an iPad. I do this because it’s
faster than trying to use regular slides software and I can make better slides.


## a few notes


Here are a few links & notes about things I mentioned in the talk


### skycfg: write functions, not YAML


I talked about how my team is working on non-YAML interfaces for configuring Kubernetes. The demo is
at [skycfg.fun](http://skycfg.fun), and it’s [on GitHub here](https://github.com/stripe/skycfg). It’s based on
[Starlark](https://github.com/bazelbuild/starlark), a configuration language that’s a subset of
Python.


My coworker [John](https://john-millikin.com/) has promised that he’ll write a blog post about it at
some point, and I’m hoping that’s coming soon :)


### no haunted forests


I mentioned a deploy system rewrite we did. John has a great blog post about when rewrites are a
good idea and how he approached that rewrite called [no haunted
forests](https://john-millikin.com/sre-school/no-haunted-forests).


### ignore most kubernetes ecosystem software


One small point that I made in the talk was that on my team we ignore almost all software in the
Kubernetes ecosystem so that we can focus on a few core pieces (Kubernetes & Envoy, plus some small
things like kiam). I wanted to mention this because I think often in Kubernetes land it can seem
like everyone is using Cool New Things (helm! istio! knative! eep!). I’m sure those projects are
great but I find it much simpler to stay focused on the basics and I wanted people to know that it’s
okay to do that if that’s what works for your company.


I think the reality is that actually a lot of folks are still trying to work out how to use this new
software in a reliable and secure way.


### other talks


I haven’t watched other Kubecon talks yet, but here are 2 links:


I heard good things about [this keynote from melanie cebula about kubernetes at airbnb](https://www.youtube.com/watch?v=ytu3aUCwlSg&index=127&t=0s&list=PLj6h78yzYM2PZf9eA7bhWnIh_mK1vyOfU), and I’m excited to see [this talk about kubernetes security](https://www.youtube.com/watch?v=a03te8xEjUg&index=65&list=PLj6h78yzYM2PZf9eA7bhWnIh_mK1vyOfU&t=0s). The [slides from that security talk look useful](https://schd.ws/hosted_files/kccna18/1c/KubeCon%20NA%20-%20This%20year%2C%20it%27s%20about%20security%20-%2020181211.pdf)


Also I’m very excited to see Kelsey Hightower’s keynote as always, but that recording isn’t up yet. If you
have other Kubecon talks to recommend I’d love to know what they are.


### my first work talk I’m happy with


I usually give talks about debugging tools, or side projects, or how I approach my job at a high
level – not on the actual work that I do at my job. What I talked about in this talk is basically
what I’ve been learning how to do at work for the last ~2 years. Figuring out how to make big
infrastructure changes safely took me a long time (and I’m not done!), and so I hope this talk helps
other folks do the same thing.
