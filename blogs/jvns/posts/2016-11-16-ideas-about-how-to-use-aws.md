---
title: "Ideas about how to use AWS"
date: 2016-11-16
url: https://jvns.ca/blog/2016/11/16/ideas-about-how-to-use-aws/
slug: ideas-about-how-to-use-aws
word_count: 995
---


At work we have thousands of AWS instances to manage. My job these days is to
make it easy for other software engineers to deploy code to those machines.


In doing this, it’s really useful for me to have examples of platforms that
make it easy for people to deploy code. For example, Heroku is a super popular
platform! I often think “why can’t we be as easy to use as Heroku?” and then
try to make us a little more like that.


Recently I looked at [Skyliner](https://www.skyliner.io/), another platform
that lets you deploy code to computers, specifically AWS instances. Here’s their [launch post](https://blog.skyliner.io/welcome-to-skyliner-aws-is-easy-now-35c1c9bc86e7#.a7ghqrozm).
I’m not super interested myself in using Skyliner or Heroku, but I am interested in looking at their design decisions! In particular I think Skyliner is
interesting if you use Amazon Web Services (like I do) because they’ve made a
bunch of choices about which AWS features to use, and if you try it out you can
see exactly which AWS features they’re using and how.


A disclaimer: i know the people who founded skyliner, so I’m not an unbiased
observer. I have not used it for more than 30 minutes and I won’t make any
claims about whether you should or should not use it.


Anyway here are 3 new things I learned:


### New AWS instances take less than 5 minutes to start up


Skyliner deploys your code by

- Launching entirely new AWS instances
- Setting them up
- Making sure they work (with a healthcheck)


When I saw this I thought it might take forever. But it turns out that starting
new AWS instances is not that slow! Neat. It’s still kind of slow, quite a bit
slower than my deploys at work. But not as slow as I thought. And it comes with
a lot of nice properties (security updates get applied every time you deploy,
it’s completely impossible for state from the previous deploy to leak).


### You can use Docker in a simple way


I’ve been skeptical of Docker on this blog. Docker has a ton of super
complicated pieces. The Skyliner people wrote a post that advocates [Use containers. Not too much. Mostly for packaging.](https://blog.skyliner.io/the-happy-genius-of-my-household-2f76efba535a#.fzgavtp32).
But what does that even mean?


WELL I FOUND OUT WHAT IT MEANS. Coda (who wrote that post) told me the exact
command line arguments they use with Docker today and it explained a lot.


```
docker run --detach --net host --log-driver syslog --log-opt tag="{$appName}"
--restart always --env-file /etc/{$appName}.env {$appName}{\n}`

```


`--net host` means “use the host networking namespace, don’t do any weird container networking stuff”. GREAT.


They don’t use a Docker registry. They package the Docker image into a tarball,
encrypt it, put it in S3, and then download it onto your machine. Super simple.
It also doesn’t use Docker Swarm or any of the new container orchestration
stuff – a single application runs on a single AWS instance. This makes me feel
a lot more comfortable with Docker – I’ve been reading a lot of bad press
about Docker recently but it seems like if you’re very careful with which
features you use, maybe it will work fine!


### Load balancers are the best


Okay, I already know that load balancers are the best. At work we have load
balancers, and when a box explodes or a service goes down, it says “whoops,
guess that healthcheck failed”, routes traffic away from that box, and
everything is totally fine. Nobody even knows there was a problem.


Skyliner uses Amazon Application Load Balancers. The cool thing about these
load balancers (vs HAProxy, which is what I use at work) is that they have an
**API**. You can ask them questions about what they’re up to. Why is this
interesting? WELL.


Let’s say you’re doing a deploy, and you want to know if your new instances
that you deployed are a) totally fine or b) completely exploded. I do not know
how to do this with HAProxy (though maybe there is a way that I do not know!). But with these LBs, you can use the
[DescribeInstanceHealth API method!](http://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeInstanceHealth.html).
Then you can be like “wow, those instances… those are not up, nope, not at all”
and roll back. You can also register new instances and deregister instances and
all kinds of things.


Skyliner describes their load balancers like this:


> An Application Load Balancer, which supports both HTTP/2 and WebSockets, configured to send logs to your S3 log bucket. Connection draining is enabled, which allows for zero-downtime deploys.


So they tell your load balancer “hey, don’t use this instance anymore! Except wait 5 minutes and let any old connections finish please!”. That’s called “connection draining”.


This week I am weirdly extremely excited about load balancers with APIs,
probably more than a normal person should be.


### Spying on architecture is fun


AWS is a super complicated platform. They have like 30 bajillion services you
can use. SNS! SQS! RDS! EC2! SES! FPS! KMS! DynamoDB! Container registry!
Container service! And that is only a small fraction. I often find it really
overwhelming and it is my job to work with AWS.


Skyliner isn’t open source. But as a Skyliner non-user (and an AWS user), just
being able to look at how they’ve put together AWS stuff into a coherent
product and considering which choices they made might also be good choices for
me is super useful! Like, they use Amazon key management service! Should I be
using that? Well, what do they use it for?


I’ve been talking to friends a lot about how good architecture is super super
valuable – if someone can write down in a document how a system should work,
and that description is workable, then it can save a ton of missteps even if
you still have to write all the code. Skyliner’s architecture seems useful
to me so far! If you would like to also read some architecture there is an
[architecture document here](https://www.skyliner.io/help/architecture).
