---
title: "Snowflake Server"
description: "Automated configuration tools (such asCFEngine,Puppet, orChef) allow you to specify   how servers should be configured, and bring new and existing machines   into compliance. This helps to avoid the p"
date: 2013-06-13T00:00:00
tags: ["continuous delivery", "bad things"]
url: https://martinfowler.com/bliki/SnowflakeServer.html
slug: SnowflakeServer
word_count: 638
---


It can be finicky business to keep a production server running.
  You have to ensure the operating system and any other dependent
  software is properly patched to keep it up to date. Hosted
  applications need to be upgraded regularly. Configuration changes
  are regularly needed to tweak the environment so that it runs
  efficiently and communicates properly with other systems. This
  requires some mix of command-line invocations, jumping between GUI
  screens, and editing text files.


The result is a unique snowflake - good for a ski resort, bad for
  a data center.


The first problem with a snowflake server is that it's difficult
  to reproduce. Should your hardware start having problems, this means
  that it's difficult to fire up another server to support the same
  functions. If you need to run a cluster, you get difficulties
  keeping all of the instances of the cluster in sync. You can't
  easily mirror your production environment for testing. When you get
  production faults, you can't investigate them by reproducing the
  transaction execution in a development environment. 1


1: 
     Another metaphor I've heard for this is that you should treat
     your servers like cattle and not like pets. Although I confess I
     find it odd when this metaphor is used by my vegetarian
     colleagues.


Making disk images of the snowflake can help to some extent with
  this. But such images easily gather cruft as unnecessary elements of
  the configuration, not to mention mistakes, perpetuate.


The true fragility of snowflakes, however, comes when you need to
  change them. Snowflakes soon become hard to understand and modify.
  Upgrades of one bit software cause unpredictable knock-on effects.
  You're not sure what parts of the configuration are important, or
  just the way it came out of the box many years ago. Their fragility
  leads to long, stressful bouts of debugging. You need manual
  processes and documentation to support any audit requirements. This
  is one reason why you often see important software running on
  ancient operating systems.


A good way to avoid snowflakes is to hold the entire operating
  configuration of the server in some form of automated recipe. Two
  tools that have become very popular for this recently are [Puppet](http://puppetlabs.com/) and [Chef](http://www.opscode.com/chef/). Both allow you to define
  the operating environment in a form of
  [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html), and easily apply it to a given
  system.


The point of using a recipe is not just that you can easily
  rebuild the server (which you could also do with imaging) but you
  can also easily understand its configuration and thus modify it more
  easily. Furthermore, since this configuration is a text file, you
  can keep it in version control with all the advantages that
  brings.


If you disable any direct shell access to the server and force
  all configuration changes to be applied by running the recipe from
  version control, you have an excellent audit mechanism that ensures
  every change to the environment is logged. This approach can be very
  welcome in regulated environments.


Application deployment should follow a similar approach: fully
  automated, all changes in version control. By avoiding snowflakes,
  it's much easier to have test environments be true clones of
  production, reducing production bugs caused by configuration
  differences.


A good way of ensuring you are avoiding snowflakes is to use
 [PhoenixServers](https://martinfowler.com/bliki/PhoenixServer.html). Using version-controlled recipes to define
 server configurations is an important part of [Continuous Delivery](https://martinfowler.com/delivery.html).


## Further Reading


The [Visible Ops Handbook](https://www.amazon.com/gp/product/0975568604/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0975568604&linkCode=as2&tag=martinfowlerc-20) is the
   pioneering book that talked about the dangers of snowflakes and how
   to avoid them. [Continuous
   Delivery](https://martinfowler.com/books/continuousDelivery.html) talks about how this approach is a necessary part of a
   sane build and delivery process. [True artists, however, prefer snowflakes](http://tatiyants.com/devops-is-ruining-my-craft/).


## Notes


1: 
     Another metaphor I've heard for this is that you should treat
     your servers like cattle and not like pets. Although I confess I
     find it odd when this metaphor is used by my vegetarian
     colleagues.
