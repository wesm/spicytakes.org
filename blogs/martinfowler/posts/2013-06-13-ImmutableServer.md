---
title: "Immutable Server"
description: "Automated configuration tools (such asCFEngine,Puppet, orChef) allow you to specify   how servers should be configured, and bring new and existing machines   into compliance. This helps to avoid the p"
date: 2013-06-13T00:00:00
tags: ["continuous delivery", "build scripting"]
url: https://martinfowler.com/bliki/ImmutableServer.html
slug: ImmutableServer
word_count: 873
---


Automated configuration tools (such as [CFEngine](http://cfengine.com/), [Puppet](https://puppetlabs.com/puppet/what-is-puppet/), or
  [Chef](http://www.opscode.com/chef/)) allow you to specify
  how servers should be configured, and bring new and existing machines
  into compliance. This helps to avoid the problem of fragile 
  [SnowflakeServers](https://martinfowler.com/bliki/SnowflakeServer.html). Such tools can create [PhoenixServers](https://martinfowler.com/bliki/PhoenixServer.html)
  that can be torn down and rebuilt at will. An Immutable Server is the 
  logical conclusion of this approach, a server that once deployed, is 
  never modified, merely replaced with a new updated instance.


Automated configuration tools are usually used with
  [ConfigurationSynchronization](https://martinfowler.com/bliki/ConfigurationSynchronization.html) where you leave a server
  running for a potentially long period of time, repeatedly applying
  configuration to bring it into line with the latest specification.
  In theory servers can be allowed to run indefinitely, and they'll be
  kept completely consistent and up to date. In practice it's not
  possible to manage a server's configuration completely, so there is
  considerable scope for configuration drift, and unexpected changes
  to running servers.


This is where a [PhoenixServer](https://martinfowler.com/bliki/PhoenixServer.html) is helpful.


![](images/immutableServer/PhoenixServerLifecycle.png)


By frequently destroying and rebuilding servers from the base
  image, 100% of the server's elements are reset to a known state,
  without spending a ridiculous amount of time specifying and
  maintaining detailed configuration specifications.


Once you're using phoenixes, the focus of
  configuration management shifts to the management of base images.
  Fixes, changes, and updates are applied to the base image rather
  than to running systems. Each time you want a new update you modify
  the base instance and run it through an automated test harness. You only 
  create new servers when they pass these steps.


So a phoenix server's complete state is built from a combination
  of base image + automated configuration management + data 1, which reduces the pressure to have automated
  configuration manage 100% of the server.


1: 
      Data covers a variety of things, including database files and other application-managed data, runtime state, other runtime-generated data such as log files, and externally supplied configuration.


But while we can continue to run configuration management updates
  on a server during its brief lifetime, there's less value in doing
  so. In fact, there is considerable value in *not* doing so, since
  any change to a running system introduces risk.


This leads naturally to immutable servers 2.


2: 
      My colleague Ben Butler-Cole coined the term âImmutable Serverâ for this pattern on an internal Thoughtworks mailing list.


![](images/immutableServer/ImmutableServerLifecycle.png)


Once you've spun up a server instance from a well-tested base image, you 
  shouldn't run configuration management tools, since they create
  opportunities for untested changes to the instance. Any changes that
  are needed can be made to the base image, tested, and then rolled
  out. Servers without the change are torn down and replaced.


If this sounds familiar, it's because it follows the practices of
  [ContinuousIntegration](https://martinfowler.com/articles/continuousIntegration.html) and [ContinuousDelivery](https://martinfowler.com/bliki/ContinuousDelivery.html). With 
  Continuous Delivery of software, it's safer to compile a given version of
  an application into a deployable artifact only once, and know that you are 
  deploying and running a consistently built application in all environments. 
  With an immutable server, you make each change to a base image, and then 
  you know that all instances created from that image are consistent.


The main differences between instances of a server role come from
  configuration settings, which should come from outside the server.
  For example, most virtualization and cloud platforms offer a way to
  set metadata values when provisioning a new instance, which can then
  be read by the running server. New servers may also pull
  configuration values from a central registry like [Zookeeper](http://zookeeper.apache.org/).


It's advisable to minimize the number and scope of per-instance
  configuration items for immutable servers, and to run changes to
  these through automated testing where feasible.


## Handling data


If servers are disposable, the data that lives on them often is not. 
    When implementing phoenix or immutable servers you should consider what
    data needs to be persisted as servers are destroyed and created, and what
    data must be replicated in order to scale by adding additional servers.


You can ship data off of the instance when it has value but isn't needed
    at runtime, for example sending logfiles to a central syslog server. A shared 
    file system like NFS can make files available to servers, perhaps living on
    a SAN. Cloud platforms generally offer mountable storage devices like AWS
    EBS volumes which can be attached to new servers instances when the old ones
    are destroyed, or quickly duplicated and attached to replicas when scaling a
    cluster. Often you can pass the buck to a service which someone else maintains,
    like Amazon's RDS database service.


## Further Reading


Netflix has been at the forefront in using the ImmutableServer
    pattern, although I'm not aware that they've used the term. They
    have open-sourced the Aminator tool they developed to manage AMI
    instances for use on Amazon's AWS cloud and [blogged
    about how their use of this pattern has evolved](http://techblog.netflix.com/2013/03/ami-creation-with-aminator.html) with
    experience. Interestingly, the speed of instantiating new
    instances has been a key driver for them, since this helps them to
    automatically scale and recover.


## Notes


1: 
      Data covers a variety of things, including database files and other application-managed data, runtime state, other runtime-generated data such as log files, and externally supplied configuration.


2: 
      My colleague Ben Butler-Cole coined the term âImmutable Serverâ for this pattern on an internal Thoughtworks mailing list.
