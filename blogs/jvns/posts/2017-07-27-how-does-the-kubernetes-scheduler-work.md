---
title: "How does the Kubernetes scheduler work?"
date: 2017-07-27
url: https://jvns.ca/blog/2017/07/27/how-does-the-kubernetes-scheduler-work/
slug: how-does-the-kubernetes-scheduler-work
word_count: 2257
---


Hello!  We talked about Kubernetes’ [overall architecture](https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/) a while back.


This week I learned a few more things about how the Kubernetes scheduler
works so I wanted to share! This kind of gets into the weeds of how the
scheduler works *exactly*.


It’s also an illustration of how to go from “how is this system even
designed I don’t know anything about it?” to “okay I think I understand
the basic design decisions here and why they were made” without
actually.. asking anyone (because I don’t know any kubernetes
contributors really, certainly not well enough to be like PLEASE EXPLAIN
THE SCHEDULER TO ME THANKS).


This is a little stream of consciousness but hopefully it will be useful
to someone anyway. The best most useful link I found while researching
this was this [Writing Controllers](https://github.com/kubernetes/community/blob/8decfe4/contributors/devel/controllers.md) document from the amazing amazing amazing [kubernetes developer documentation folder](https://github.com/kubernetes/community/tree/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel).


### what is the scheduler for?


The Kubernetes scheduler is in charge of scheduling pods onto nodes.
Basically it works like this:

1. You create a pod
2. The scheduler notices that the new pod you created doesn’t have a node assigned to it
3. The scheduler assigns a node to the pod


It’s not responsible for actually *running* the pod – that’s the
kubelet’s job. So it basically just needs to make sure every pod has a
node assigned to it. Easy, right?


Kubernetes in general has this idea of a “controller”. A controller’s
job is to:

- look at the state of the system
- notice ways in which the actual state does not match the desired state
(like “this pod needs to be assigned a node”)
- repeat


The scheduler is a kind of controller. There are lots of different
controllers and they all have different jobs and operate independently.


So basically you could imagine the scheduler running a loop like this:


```
while True:
    pods = get_all_pods()
    for pod in pods:
        if pod.node == nil:
            assignNode(pod)

```


If you are not that interested in all the details of how the Kubernetes
scheduler works you can probably stop reading now – this is a pretty
reasonable model of how it works.


I thought the scheduler **actually** worked this way because this is how the
[cronjob controller](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/pkg/controller/cronjob/cronjob_controller.go)
works and that was the only Kubernetes component code I’d really read.
The cronjob controller basically iterates through all cronjobs, sees if
it has to anything to do for any of them, sleeps for 10 seconds, and
repeats forever. Super simple!


### this isn’t how it works though


So! This week we were putting a little more load on our Kubernetes
cluster, and we noticed a problem.


Sometimes a pod would get stuck in the `Pending` state (with no node
assigned to it) forever. If we restarted the scheduler, the pod would
get unstuck. ([this issue](https://github.com/kubernetes/kubernetes/issues/49314))


This didn’t really match up with my mental model of how the Kubernetes
scheduler worked – surely if a pod is waiting for a node to be
assigned, the scheduler should notice and assign that pod a node. The
scheduler shouldn’t have to be restarted!


So I went and read a bunch of code. Here is what I learned about how the
scheduler actually works! As usual probably something here is wrong,
this stuff is pretty complicated and I just learned about it this week.


### how the scheduler works: a very quick code walkthrough


This is basically just what I figured out from reading the code.


We’ll start in [scheduler.go](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/plugin/pkg/scheduler/scheduler.go). (I actually [concatenated all the files in the scheduler together](https://gist.github.com/jvns/5d492d66130a2f47b47820fd6b52eab5) which I found helpful for jumping around and navigating.)


The core loop in the scheduler (as of commit e4551d50e5) is:


([link](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/plugin/pkg/scheduler/scheduler.go#L150-L156))


```
go wait.Until(sched.scheduleOne, 0, sched.config.StopEverything)

```


This basically means “run `sched.scheduleOne` forever”. Cool, what does that do?


```
func (sched *Scheduler) scheduleOne() {
	pod := sched.config.NextPod()
    // do all the scheduler stuff for `pod`
}

```


Okay, what is this `NextPod()` business? Where does that come from?


```
func (f *ConfigFactory) getNextPod() *v1.Pod {
	for {
		pod := cache.Pop(f.podQueue).(*v1.Pod)
		if f.ResponsibleForPod(pod) {
			glog.V(4).Infof("About to try and schedule pod %v", pod.Name)
			return pod
		}
	}
}

```


Okay, that’s pretty simple! There’s a queue of pods (`podQueue`) and the next
pod comes from that queue.


But how do pods end up on that queue? Here’s the code that does that:


```
podInformer.Informer().AddEventHandler(
	cache.FilteringResourceEventHandler{
		Handler: cache.ResourceEventHandlerFuncs{
			AddFunc: func(obj interface{}) {
				if err := c.podQueue.Add(obj); err != nil {
					runtime.HandleError(fmt.Errorf("unable to queue %T: %v", obj, err))
				}
			},

```


Basically there’s an event handler that, whenever a new pod is added,
puts it on the queue.


### how the scheduler works, in English


Okay now that we’ve looked through the code, here’s a summary in
English:

1. At the beginning, every pod that needs scheduling gets added to a queue
2. When new pods are created, they also get added to the queue
3. The scheduler continuously takes pods off that queue and schedules them
4. That’s it


One interesting thing here is that – if for whatever reason a pod **fails** to
get scheduled, there’s nothing in here yet that would make the scheduler retry.
It’d get taken off the queue, it fails scheduling, and that’s it. It lost its
only chance! (unless you restart the scheduler, in which case everything will
get added to the pod queue again)


Of course the scheduler is actually smarter than that – when a pod
fails to schedule, in general it calls an error handler, like this:


```
host, err := sched.config.Algorithm.Schedule(pod, sched.config.NodeLister)
if err != nil {
	glog.V(1).Infof("Failed to schedule pod: %v/%v", pod.Namespace, pod.Name)
	sched.config.Error(pod, err)

```


This `sched.config.Error` function call adds the pod back to the queue
of things that need to be scheduled, and so it tries again.


### wait why did our pod get stuck then?


This is pretty simple – it turned out that the `Error` function wasn’t
always being called when there was an error. We made a patch to call the
`Error` function properly and that seems to have made it recover
properly! Cool!


### why is the scheduler designed this way?


I feel like this design would be more robust:


```
while True:
    pods = get_all_pods()
    for pod in pods:
        if pod.node == nil:
            assignNode(pod)

```


so why is it instead this more complicated thing with all these caches and queues and callbacks?
I looked at the history a bit and I think it’s basically for performance
reasons – for example you can see this [update on scalability updates for Kubernetes 1.6](http://blog.kubernetes.io/2017/03/scalability-updates-in-kubernetes-1.6.html)
and this post from CoreOS about
[improving Kubernetes scheduler performance](https://coreos.com/blog/improving-kubernetes-scheduler-performance.html). That post says it improved the time to schedule 30,000 pods from 14 minutes to 10 minutes. That post says it improved the time to schedule 30,000 pods from 2 hours to 10 minutes. 2 hours is pretty slow! performance is important!


So it makes sense to me that it would be too slow to query for all
30,000 pods in your system every time you want to schedule a new pod,
and that you’d actually want to do something more complicated.


### what the scheduler actually uses: kubernetes “informers”


I want to talk about one thing I learned about that seems very important to
the design of all kubernetes controllers! That’s the idea of an
“informer”. Luckily there actually *is* documentation about this that I
found in by googling “kubernetes informer”.


This very useful document is called [Writing Controllers](https://github.com/kubernetes/community/blob/8decfe4/contributors/devel/controllers.md)
and it gives you design advice when you’re writing a controller (like
the scheduler or the cronjob controller). VERY COOL.


If I’d found this document in the first place I think I would have
understood what is going on a little more quickly.


So! Informers! The doc says this:


> Use SharedInformers. SharedInformers provide hooks to receive
> notifications of adds, updates, and deletes for a particular resource.
> They also provide convenience functions for accessing shared caches
> and determining when a cache is primed.


Basically when a controller runs it creates an “informer” (for example a
“pod informer”) which is in charge of

1. listing all pods in the first place
2. telling you about updates


The cronjob controller does not use an informer (using informers is more
complicated, and I think it just doesn’t care as much about performance
yet), but many (most?) other controllers do. In particular, the scheduler uses informers! You
can see it configuring its informer [here](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/plugin/pkg/scheduler/factory/factory.go#L175).


### requeueing


There’s actually also some guidance about how to handle requeuing of
items that you’re handling in the “writing controllers” documentation!


> Percolate errors to the top level for consistent re-queuing. We have a
> workqueue.RateLimitingInterface to allow simple requeuing with
> reasonable backoffs.


> Your main controller func should return an error when requeuing is
> necessary. When it isn’t, it should use utilruntime.HandleError and
> return nil instead. This makes it very easy for reviewers to inspect
> error handling cases and to be confident that your controller doesn’t
> accidentally lose things it should retry for.


This seems to be good advice, it seems tricky to handle all errors
correctly and so having a simple way to make sure reviewers can tell
errors are being handled correctly is important! Cool!


### you should “sync” your informers (or should you?)


Okay, this is the last interesting thing I learned.


Informers have this concept of a “sync”. A sync is a little bit like
restarting the program – you get a list of every resource you were
watching, so that you can check that it’s actually okay. Here’s what the
“writing controllers” guidance has to say about syncing.


> Watches and Informers will “sync”. Periodically, they will deliver
> every matching object in the cluster to your Update method. This is
> good for cases where you may need to take additional action on the
> object, but sometimes you know there won’t be more work to do.


> In cases where you are certain that you don’t need to requeue items when
> there are no new changes, you can compare the resource version of the
> old and new objects. If they are the same, you skip requeuing the work.
> Be careful when you do this. If you ever skip requeuing your item on
> failures, you could fail, not requeue, and then never retry that item
> again.


So this implies “you should sync, if you don’t sync then you
can end up in a situation where an item gets lost and never retried”.
Which is what happened to us!


### the kubernetes scheduler doesn’t resync


So!! Once I learned about this idea of a “sync”, I was like.. wait,
does that mean the kubernetes scheduler never resyncs? It seems that the
answer is “no, it doesn’t!”. here’s [the code](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/plugin/cmd/kube-scheduler/app/server.go#L75-L77):


```
informerFactory := informers.NewSharedInformerFactory(kubecli, 0)
// cache only non-terminal pods
podInformer := factory.NewPodInformer(kubecli, 0)`

```


Those numbers `0` – those are the “resync period”, which I interpret to
mean that it never resyncs. Interesting!! Why doesn’t it ever resync? I
don’t know for sure, but I googled “kubernetes scheduler resync” and
found this pull request [#16840](https://github.com/kubernetes/kubernetes/pull/16840) (which added a resync to the scheduler), with the following 2 comments:


> @brendandburns - what is it supposed to fix? I’m really against having
> such small resync periods, because it will significantly affect
> performance.


and


> I agree with @wojtek-t . If resync ever fixes a problem, it means
> there is an underlying correctness bug that we are hiding. I do not
> think resync is the right solution.


So it seems like the project maintainers decided never to resync,
because when there are correctness bugs, they’d like them to be surfaced
and fixed instead of hidden by a resync.


### some code-reading tips


As far as I know “how the kubernetes scheduler actually works
internally” is not written down anywhere (like most things!).


Here are a couple of things that helped me when reading it:

1. Concatenate the whole thing into a big file. I said this already but
it really helped me jump around between function calls – switching
between files is confusing, especially when I don’t understand the
overall organization yet!
2. Have some specific questions. Here I was mostly trying to figure out
“how is error handling even supposed to work? What happens if a pod
doesn’t get scheduled?”. So there was a lot of code about like.. the
details of how it picks which node exactly to schedule a pod to that
I didn’t need to care about at all (I still don’t know how that works)


### kubernetes is pretty good to work with so far


Kubernetes is a really complicated piece of software! To get a cluster
working at all, you need to set up at least 6 different components (api
server, scheduler, controller manager, container networking thing like
flannel, kube-proxy, the kubelet). And so (if you care about
understanding the software you run, which I very much do), I have to
understand what all of those components do and how they interact with
each other and how to set each of their 50 bajillion configuration
operations in order to accomplish what I want.


But so far the documentation is pretty good, when there are things that
aren’t documented the code is pretty easy to read, and they seem really
willing to review pull requests.


I’ve definitely had to practice “read the documentation and if it’s not
there read the code” more than usual. But that’s a good skill to get
better at anyway!
