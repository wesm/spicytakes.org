---
title: "Boiled Carrot"
description: "I hated carrots when I was growing up, hating the smell and texture of the things.     But after I left home and started to cook for myself I started to like them. Nothing     changed about the carrot"
date: 2016-06-23T00:00:00
tags: ["process theory"]
url: https://martinfowler.com/bliki/BoiledCarrot.html
slug: BoiledCarrot
word_count: 999
---


I hated carrots when I was growing up, hating the smell and texture of the things.
    But after I left home and started to cook for myself I started to like them. Nothing
    changed about the carrots, nor did my taste buds get a radical overhaul, the
    difference was in the cooking. My mother, like so many English people of her
    generation, wasn't a great cook - particularly of vegetables. Her approach was to boil
    carrots for twenty minutes or more. I since learned that if you cook them properly,
    carrots are a totally different experience.


This isn't a site about cooking, but about software development. But I find that
    often a technique or tool is like the poor carrot - blamed for being awful when the
    real problem is that the technique is being done incorrectly.


Let's take a couple of  examples. Several friends of mine
commented how stored procedures were a disaster because they weren't
kept in version control (instead they had names like GetCust01,
GetCust02, GetCust02B etc). That's not a problem with stored
procedures, that's a problem with people using bad practices with them.
Similarly a criticism that TDD led to a brittle design on further
questioning led to the discovery that the team in question hadn't done
any refactoring - and refactoring is a critical step in TDD.


Both of these are boiled carrots - useful tools that have been misused. I've seen
  teams gain value out of both stored procedures and TDD. If we discard them without
  taking their usage into account we lose useful tools from our toolbox.


Not every failure of technique is a boiled carrot. I'm reliably informed that there's
  no way to cook squirrels so they are appetizing to anyone who isn't desperate (which is
  a shame considering what they've been doing to our garden this spring). If I come across
  a team working on code in a shared folder, without any version control, there's no way
  to cook that technique which isn't similarly appalling.


So when we hear of techniques failing, we need to ask a lot
more questions.

- Was it the technique itself that had problems, or was some
other thing being missed out. Does the technique have an influence on
this? (Version control is a separate thing to stored procedures, but
it can be harder to use version control with stored procedures due to
nature of tools involved.)
- Was the technique used in a context that wasn't suitable for
it? (Don't use wide-scale manual refactoring when you don't have
tests.) Remember that software development is a very human activity,
often techniques aren't suitable for a context because of culture and
personality.
- Were important pieces missed out of the technique?
- Were people focused on outward signs that didn't correspond to
the reality? This kind of thing is what Steve McConnell called [Cargo Cult
Software Engineering](http://www.stevemcconnell.com/ieeesoftware/eic10.htm).
- Is the technique something that works at some scale, but is being used outside its
    zone of applicability? It's worth remembering Paracelsus's principle that the
    difference between a medicine and a poison is the dosage. Testing a system through the
    UI is useful with a few scenarios, but if you use it as your main testing approach
    you'll end up with slow and brittle tests which will either slow you down or get ignored.


An interesting aspect of this is whether certain techniques are
  fragile; i.e are they hard to apply correctly and thus more prone
  to a faulty application? If it's hard to use a technique properly,
  that's a reasonable limitation on the technique, reducing the context
  when it can be used. Some delicate foods have to left to a master chef. That doesn't
  make them a bad technique, but it does reduce their applicability to more skillful
  teams. I'd argue this is the fundamental problem with late integration of components.
  While some teams can develop components to careful specifications that can integrate
  together late in the day, in practice few teams are able to pull that off, and late
  integration ends up being like Fugu.


While we need to be wary of boiled carrots, we also need to bear in mind we also get
  the situation that I've observed as âno methodology has ever failedâ. With any failure
  (assuming you can know [WhatIsFailure](https://martinfowler.com/bliki/WhatIsFailure.html)) you can find some variation from the
  methodology - which leads its defenders to say it wasn't followed and thus didn't fail.
  There's a genuine tension here, one that can't be resolved without a deep understanding
  of the deeper principles underlying a technique. The real point is that such techniques
  aren't rigorously describable, just as Spaghetti Carbonara does not have one precise
  recipe that can be followed without thinking. In the end what really counts is the dish,
  the technique to prepare it can inspire and guide a good chef but cannot guarantee
  success to someone without a certain degree of skill.


Like any profession, we can advance faster if we learn from each others' experiences.
  Reports of people using techniques and tools are important so that we can judge what to
  try in our own work. However a simple label usually isn't enough to go on. We are as
  unable to measure compliance with the proper use of a technique as we are unable to
  measure their successfulness. The important thing to do is whenever you hear of a
  technique failing - always dig deeper to see if the carrot's been in the pot
  too long. Otherwise we risk missing out on something worthwhile.


I originally wrote about this topic under the heading âFaulty Technique Dichotomyâ, but
  now feel the boiled carrot metaphor is more memorable.


## Further Reading


I liked Ron Jeffries parable for a similar phenomenon [âWe tried baseball and it didn't
  workâ](http://ronjeffries.com/xprog/articles/jatbaseball/).


## Acknowledgements

Henrique Souza, Jeantine Mankelow, Karl Brown, Kief Morris, Kyle Hodgson, Matteo
  Vaccari, Patrick Kua, Rebecca Parsons, Ricardo Cavalcanti, Roni Greenwood, Sriram Narayan,
  and Steven Lowe

  discussed drafts of this post on our internal mailing list.