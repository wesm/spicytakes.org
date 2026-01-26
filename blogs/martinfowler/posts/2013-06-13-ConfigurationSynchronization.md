---
title: "Configuration Synchronization"
description: "Automated configuration tools (such asCFEngine,Puppet, orChef) allow you to avoidSnowflakeServersby providing recipes to describe the   configuration of elements of a server. Configuration synchroniza"
date: 2013-06-13T00:00:00
tags: ["continuous delivery"]
url: https://martinfowler.com/bliki/ConfigurationSynchronization.html
slug: ConfigurationSynchronization
word_count: 728
---


Automated configuration tools (such as [CFEngine](http://cfengine.com/), [Puppet](https://puppetlabs.com/puppet/what-is-puppet/), or
  [Chef](http://www.opscode.com/chef/)) allow you to avoid
  [SnowflakeServers](https://martinfowler.com/bliki/SnowflakeServer.html) by providing recipes to describe the
  configuration of elements of a server. Configuration synchronization 
  continually applies these specifications, either on a regular schedule 
  or when it changes, to server instances throughout their lifetime. If 
  someone makes a change to a server outside the tool, it will be reverted
  to the centrally specified configuration the next time the server is 
  synchronized. If some configuration change is needed, it's made in the 
  configuration specification (recipes, manifests, or whatever the particular
  configuration tool calls it), and is then applied to all relevant
  servers across the infrastructure.


![](images/configurationSync/ConfigurationSynchronizationPattern.png)


In theory, once a server has been created, configuration
  synchronization will keep it up to date, applying upgrades and
  patches and preventing [configuration drift](http://kief.com/configuration-drift.html) for a potentially long
  lifetime.


In practice, however, it isn't feasible to keep servers
  completely consistent using current automated configuration
  management tools, so over time configuration synchronization
  leads to inconsistency. 1


1:


My colleague Max Lincoln provided these references to
  configuration tool vendors' aspirations around total system
  configuration:

- âCreate a blueprint of your infrastructure - so it can be built
    or rebuilt consistently from scratch in minutesâ - [Opscode
    Chef](http://www.opscode.com/solutions/configuration-management/)
- âEliminate configuration drift and reduce outagesâ - [Puppetlabs](https://puppetlabs.com/solutions/configuration-management/)
- âCFEngine then continuously corrects configuration drift,
    keeping systems in compliance with their Desired State.â - [CFEngine](http://cfengine.com/what-is-cfengine)


Each element of server configuration managed by an automated tool
  requires work to write, test, and maintain the recipe or manifest.
  It simply isn't reasonable to attempt to manage every single element
  of a typical server using these tools. There are far too many of
  them. And for each additional element you do specify, the
  work involved grows non-linearly thanks to the potential
  interactions, integrations, and dependencies between them.


Software packages are a particular challenge, given the
  dependencies they may have on yet more packages. Tools such as
  yum, apt-get, gems, etc. automatically work out dependencies and
  install them from repositories. So a large number of the packages
  on a system are only implicitly managed, and may change without 
  notice. Although you can micro-manage the versions and dependencies 
  of software packages installed, it's an intractable job considering 
  the number of packages involved.


If managing the stuff you want to have on your server is
  difficult, managing the things you don't want is worse, given there
  are an effectively inifinite number of them. Current configuration
  management tools require you to explicitly list each file, package,
  or other element you want removed if found. This means additional
  things can be manually added onto some servers, creating inconsistent 
  and unexpected behaviour.


![](images/configurationSync/ConfigurationSynchronization_UnmanagedChanges.png)


In reality, people using automated configuration tools get by
  well enough without specifying 100% of the configurable surface area
  of their servers. Teams apply the 80/20 rule to automated configuration,
  focusing 80% (or more like 95%) of their attention on defining that
  20% (or 5%) of the system which is most relevant to their particular
  needs, leaving the rest to the defaults installed by the base OS. So
  the majority of the system is not under automated configuration, and
  generally, this works. Unfortuantely, when it doesn't - when some
  part of the system not managed by automation tools does cause an issue, 
  the effects are unexpected and can be difficult to track down.


This problem grows worse over the lifespan of a server,
  and with the frequency of change. The longer a server stays up, the
  more it may deviate from other servers, especially newer ones.


This issue leads some people to use [PhoenixServers](https://martinfowler.com/bliki/PhoenixServer.html). By
  ensuring that a server's lifespan is kept short, frequently
  rebuilding fresh ones from a base image, the potential for
  configuration drift is kept small, without the overhead of
  specifying more of the server's configuration in a management tool
  than is really necessary. Taking the phoenix server to its logical
  conclusion leads to [ImmutableServers](https://martinfowler.com/bliki/ImmutableServer.html), which
  avoid any changes made to a server during it's lifespan.


## Notes


### 1: Vendor Aspirations


My colleague Max Lincoln provided these references to
  configuration tool vendors' aspirations around total system
  configuration:

- âCreate a blueprint of your infrastructure - so it can be built
    or rebuilt consistently from scratch in minutesâ - [Opscode
    Chef](http://www.opscode.com/solutions/configuration-management/)
- âEliminate configuration drift and reduce outagesâ - [Puppetlabs](https://puppetlabs.com/solutions/configuration-management/)
- âCFEngine then continuously corrects configuration drift,
    keeping systems in compliance with their Desired State.â - [CFEngine](http://cfengine.com/what-is-cfengine)
