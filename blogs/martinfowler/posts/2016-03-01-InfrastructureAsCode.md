---
title: "Infrastructure As Code"
description: "Infrastructure as code is the approach to defining computing and network   infrastructure through source code that can then be treated just like any software   system. Such code can be kept in source "
date: 2016-03-01T00:00:00
tags: ["continuous delivery", "microservices"]
url: https://martinfowler.com/bliki/InfrastructureAsCode.html
slug: InfrastructureAsCode
word_count: 825
---


[Kief Morris's book](https://www.amazon.com/gp/product/1491924357/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491924357&linkCode=as2&tag=martinfowlerc-20) is the core text for
    more depth on how to use infrastructure-as-code to take advantage of the
    shift from iron age to cloud age.


Infrastructure as code is the approach to defining computing and network
  infrastructure through source code that can then be treated just like any software
  system. Such code can be kept in source control to allow auditability and
  [ReproducibleBuilds](https://martinfowler.com/bliki/ReproducibleBuild.html), subject to testing practices, and the full discipline of
  [ContinuousDelivery](https://martinfowler.com/bliki/ContinuousDelivery.html). It's an approach that's been used over the last decade to
  deal with growing [CloudComputing](https://martinfowler.com/bliki/CloudComputing.html) platforms and will become the dominant way
  to handle computing infrastructure in the next.


I grew up in the [Iron
  Age](https://www.thoughtworks.com/insights/blog/infrastructure-code-iron-age-cloud-age), when releasing a new server application meant finding some physical hardware to
  run it on, configuring that hardware to support the needs of the application, and
  deploying that application to the hardware. Getting hold of that hardware was usually
  expensive, but also long winded, usually a matter of months. But now we live the Cloud
  Age, where firing up a new server is a matter of seconds, requiring no more than an
  internet connection and a credit card. This is a **dynamic infrastructure** where software
  commands are used to create servers (often virtual machines, but can be installations on
  bare metal), provision them, and tear them down, all without going anywhere near a
  screwdriver.


![](images/infrastructureAsCode/sketch.png)


## Practices


Infrastructure as Code is based on a few practices:

- **Use Definition Files: **all configuration is defined in executable configuration
    definition files, such as shell scripts, Ansible playbooks, Chef recipes, or Puppet
    manifests. At no time should anyone log into a server and make on-the-fly
    adjustments. Any such tinkering risks creating [SnowflakeServers](https://martinfowler.com/bliki/SnowflakeServer.html), and so should only be done
    while developing the code that acts as the lasting definition. This means that applying
    an update with the code should be fast. Fortunately computers execute code quickly,
    allowing them to provision hundreds of servers faster than any human could type.
- **Self-documented systems and processes:** rather than instructions in documents
    for humans to execute with the usual level of human reliability, code is more precise and
    consistently executed. If necessary, other human readable documentation can be
    generated from this code.
- **Version all the things:** Keep all this code in source control. That way every
    configuration and every change is recorded for audit and you can make
    [ReproducibleBuilds](https://martinfowler.com/bliki/ReproducibleBuild.html) to help diagnose problems.
- **Continuously test systems and processes:** tests allow computers to rapidly find many
    errors in infrastructure configuration. As with any modern software system, you can
    set up [DeploymentPipelines](https://martinfowler.com/bliki/DeploymentPipeline.html) for your infrastructure code which allows you to practice
    [ContinuousDelivery](https://martinfowler.com/bliki/ContinuousDelivery.html) of infrastructure changes.
- **Small changes rather than batches:** the bigger the infrastructure update, the more
    likely it is to contain an error and the harder it is to detect that error,
    particularly if several errors interact. Small updates make it easier to find errors
    and are easier to revert. When changing infrastructure [FrequencyReducesDifficulty](https://martinfowler.com/bliki/FrequencyReducesDifficulty.html).
- **Keep services available continuously:** increasingly systems cannot afford downtime
    for upgrades or fixes. Techniques such as [BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) and
    [ParallelChange](https://martinfowler.com/bliki/ParallelChange.html) can allow small updates to occur without losing availability


## Benefits


All of this allows us to take advantage of dynamic infrastructure by starting up new
  servers easily, and safely disposing of servers when they are replaced by newer
  configurations or when load decreases. Creating new servers is just a case of running
  the script to create as many server instances as needed. This approach is a good fit
  with [PhoenixServers](https://martinfowler.com/bliki/PhoenixServer.html) and [ImmutableServers](https://martinfowler.com/bliki/ImmutableServer.html)


Using code to define the server configuration means that there is greater consistency
  between servers. With manual provisioning different interpretations of imprecise
  instructions (let alone errors) lead to snowflakes with subtly
  different configurations, which often leads to tricky faults that are hard to debug.
  Such difficulties are often made worse by inconsistent monitoring, and again using code
  ensures that monitoring is consistent too.


Most importantly using configuration code makes changes safer, allowing
  upgrades of applications and system software with less risk. Faults can be found and fixed more
  quickly and at worst changes can be reverted to the last working configuration.


Having your infrastructure defined as version-controlled code aids with compliance
  and audit. Every change to your configuration can be logged and isn't susceptible to
  faulty record keeping.


All of this increases in importance as you need to handle more servers, making
  infrastructure as code a necessary capability if you're moving to a serious adoption of
  [microservices](https://martinfowler.com/microservices). Infrastructure as Code techniques scale
  effectively to manage large clusters of servers, both in configuring the servers and
  specifying how they should interact.


## Acknowledgements


This post is based on the writing and many conversations with **[Kief Morris](http://kief.com/)**, who wrote the [the definitive book](https://www.amazon.com/gp/product/1491924357/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491924357&linkCode=as2&tag=martinfowlerc-20) on the subject. The list of
    practices is taken directly from this book


Ananthapadmanabhan Ranganathan, Danilo Sato, Ketan Padegaonkar, Piyush
    Srivastava, Rafael Gomes, Ranjan D Sakalley, Sina Jahangirizadeh, and Srivatsa Katta

    discussed drafts of this post on our internal mailing list.
