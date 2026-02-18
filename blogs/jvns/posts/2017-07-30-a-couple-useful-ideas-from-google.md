---
title: "Cherry picking commits & shell scripting in golang"
date: 2017-07-30
url: https://jvns.ca/blog/2017/07/30/a-couple-useful-ideas-from-google/
slug: a-couple-useful-ideas-from-google
word_count: 1278
---


Yesterday I was talking about Kubernetes! One interesting thing about
working with Kubernetes is that it forces me to think more about
Google’s internal development practices. It’s originally a Google
project, so to contribute it, and to some extent to use it, you need to
understand a little about Google software development norms. I have never
worked at Google so I often end up asking my partner (who has) to explain
what’s going on to me.


I don’t think any of these are necessarily unique to Google but I think
they can be useful to understand when working with Google projects.


### cherry pick commits for bugfixes


Here’s how Kubernetes release management works! (from [cherry-pick.md](https://github.com/kubernetes/community/blob/8decfe42b8cc1e027da290c4e98fa75b3e98e2cc/contributors/devel/cherry-picks.md))

1. Start a release branch
2. When there are bug fixes that are made for that release in master,
cherry-pick them into the release branch
3. that’s it!


For example, the 1.6 release of Kubernetes came out in March,
but a cherry pick was merged into the release branch [on July 29](https://github.com/kubernetes/kubernetes/pull/49807) (4 months later).


It seems like there are new cherry-pick commits to the 1.6 release branch
basically every day – there have been
[447](https://github.com/kubernetes/kubernetes/compare/release-1.6) commits
since its release, probably half of those are merge commits, so I guess about 200 changes in all.


This does make me wonder a bit about the expected stability of Kubernetes
releases – if there are so many changes / bugfixes being made after a
release comes out, maybe it makes sense to delay upgrading to a release
until it’s stabilized a bit?


Related to this, we’ve started building more of our software ourselves. This is
cool because if we mostly want to be on a release (like 1.6) but have a patch
of our own we want to apply, we can easily rebuild the project from source and
deploy it.


### write shell scripts in golang


There’s a bunch of code in Kubernetes administration tooling where
you’re like “okay this is basically a shell script”. A good example of
this is [reset.go](https://github.com/kubernetes/kubernetes/blob/release-1.6/cmd/kubeadm/app/cmd/reset.go) which is like


```
fmt.Printf("[reset] Unmounting mounted directories in %q\n", "/var/lib/kubelet")
umountDirsCmd := "cat /proc/mounts | awk '{print $2}' | grep '/var/lib/kubelet' | xargs -r umount"
umountOutputBytes, err := exec.Command("sh", "-c", umountDirsCmd).Output()
if err != nil {
    fmt.Printf("[reset] Failed to unmount mounted directories in /var/lib/kubelet: %s\n", string(umountOutputBytes))
}

```


So this is literally like – you write some bash (`cat /proc/mounts | awk '{print $2}' | ...`), use `sh -c` to execute it, and embed it in a go program.


I’m actually pretty into this – this script is like 180 lines of code which is quite nontrivial for a bash script. Some cool things about writing bash scripts in Go:

- you can actually have okay command line argument handling (unlike in bash where you get to write your own command line argument handling from scratch every time)
- you get a COMPILER so it can tell you if you make typos (this is such a big deal to me)
- I’d much rather have an inexperienced Go programmer contribute to a Go program than an inexperienced bash programmer contribute to a Bash script (bash is [extremely quirky](https://jvns.ca/blog/2017/03/26/bash-quirks/) in ways that Go isn’t)
- go programs are statically compiled so if you want to use libraries in your script it’s fine! You don’t need to figure out how to distribute dependencies! (we write shell scripts in Ruby a lot and distributing the dependencies is pretty difficult/awful)
- you can’t edit the script with vim in production (you could also say this is a ‘con’ but i’m gonna go with ‘pro’ for now :))


This example also provides a good answer to “what if you want to use pipes in a
go script” which is “just run `sh -c 'thing1 | thing2 | thing3'`”.


### use services instead of shell scripts


This one is more of an “idea that is interesting but I don’t know if it’s
useful to me yet”.


Another interesting thing about Kubernetes is – most of it is structured as a
set of **services** instead of a set of scripts. I think the idea is that if
you have a continuously running service that accepts requests, that service can
ensure the state of the system is right at all times and give you reports about
its health (instead of having to manually trigger a rerun of the script).


I was looking at the Google SRE book, and there’s this section about [automation](https://landing.google.com/sre/book/chapters/automation-at-google.html) that talks about “service-oriented cluster turnup”. I’m not exactly sure yet how/if this relates to Kubernetes but I wanted to quote this section here:


> In the next iteration, Admin Servers became part of service teams’ workflows,
> both as related to the machine-specific Admin Servers (for installing packages
> and rebooting) and cluster-level Admin Servers (for actions like draining or
> turning up a service). SREs moved from writing shell scripts in their home
> directories to building peer-reviewed RPC servers with fine-grained ACLs.


> Later on, after the realization that turnup processes had to be owned by the
> teams that owned the services fully sank in, we saw this as a way to approach
> cluster turnup as a Service-Oriented Architecture (SOA) problem: service owners
> would be responsible for creating an Admin Server to handle cluster
> turnup/turndown RPCs, sent by the system that knew when clusters were ready. In
> turn, each team would provide the contract (API) that the turnup automation
> needed, while still being free to change the underlying implementation. As a
> cluster reached “network-ready,” automation sent an RPC to each Admin Server
> that played a part in turning up the cluster.


This idea of “admin servers are in charge of installing packages” instead of
“scripts are in charge of installing packages” is new to me!


I’ve been doing a lot of Kubernetes cluster turnup recently, and our Kubernetes
cluster turnup is definitely not service oriented (though we have managed to
automate it and I feel happy with it). In fact none of the tooling I’ve seen
for Kubernetes cluster setup (like kops/kubeadm) seems to be service-oriented,
it’s all like “run kops on your laptop and hope it sets up a cluster
correctly”.


For now this “service oriented admin server” idea is gonna stay in the camp of
“things I read in the Google SRE book that I don’t understand and am not going
to try to apply”, it’s not really clear to me when it makes sense.


### some ideas from google are useful!


I think it’s pretty important to be critical of software development practices
that come out of big companies like google/amazon/twitter/facebook – it’s easy
to be like “oh, if it works for google, it must be the BEST”, but google has
maybe 50,000 engineers. The practices you need to work with 50,000 other
engineers effectively don’t necessarily have any relationship to the practices
that work with like 20 or 100 or 200 engineers.


Another reason to be critical is that Google is pretty invested in selling
google cloud products to people, and if they can convince people to adopt their
operations practices (and software, like kubernetes!), then it makes it much
more natural for those people to switch to using Google-managed infrastructure. Like when I was at SRECon in March, there was a closing keynote by a Googler that basically felt like a sales pitch for GCE ([Reliability When Everything Is a Platform: Why You Need to SRE Your Customers](https://www.usenix.org/conference/srecon17americas/program/presentation/rensin))


But some of these things (like “write shell scripts in golang”) do seem like
good ideas even at a smaller scale, and I’ll always take good ideas wherever I
can get them :)
