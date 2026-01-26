---
title: "Phoenix Server"
description: "Automated configuration tools (such asCFEngine,Puppet, orChef) allow you to specify   how servers should be configured, and bring new and existing machines   into compliance. This helps to avoid the p"
date: 2013-06-13T00:00:00
tags: ["continuous delivery"]
url: https://martinfowler.com/bliki/PhoenixServer.html
slug: PhoenixServer
word_count: 348
---


One day I had this fantasy of starting a certification service
  for operations. The certification assessment would consist of a
  colleague and I turning up at the corporate data center and setting
  about critical production servers with a baseball bat, a chainsaw,
  and a water pistol. The assessment would be based on how long it
  would take for the operations team to get all the applications up
  and running again.


This may be a daft fantasy, but there's a nugget of wisdom
  here. While you should forego the baseball bats, it is a good idea
  to virtually burn down your servers at regular intervals. A server
  should be like a phoenix, regularly rising from the ashes.1


1: 
      My colleague [Kornelis
    Sietsma](https://twitter.com/kornys) came up with the term âPhoenix Serverâ on an internal
    discussion list.


The primary advantage of using phoenix servers is to avoid [configuration
  drift](http://kief.com/configuration-drift.html): ad hoc changes to a systems configuration that go
  unrecorded. Drift is the name of a street that leads to
  [SnowflakeServers](https://martinfowler.com/bliki/SnowflakeServer.html), and you don't want to go there without
  a big plough.


One way to combat drift is to use software that automatically
  re-syncs servers with a known baseline. Tools like Puppet and Chef
  have facilities to do this, automatically re-applying their defined
  configuration. 2 The limitation is that
  re-applying configuration like this can only spot
  drift in areas that you've defined that the tools control.
  Configuration drift that occurs outside those areas doesn't get
  fixed. Since phoenixes start from scratch, however,
  they will pick up any drift from the source configuration.


2: 
      These tools are also excellent for building phoenixes.


This doesn't mean that re-applying configuration isn't useful
  since it's usually faster and less disruptive than burning down a
  server. But it's valuable to use both strategies to fight away the
  snowflakes.


## Further Reading


Netflix has a [chaos monkey](http://techblog.netflix.com/2011/07/netflix-simian-army.html) that randomly burns down servers
    in order to test that their system is resilient.


## Notes


1: 
      My colleague [Kornelis
    Sietsma](https://twitter.com/kornys) came up with the term âPhoenix Serverâ on an internal
    discussion list.


2: 
      These tools are also excellent for building phoenixes.
