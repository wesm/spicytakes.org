---
title: "Asset Capture"
description: "Asset capture is a strategy for developing aStranglerFigApplication. You can think of many applications   as managing a key set of assets. A payroll system looks after   employees, a trading system lo"
date: 2004-06-29T00:00:00
tags: ["evolutionary design", "legacy modernization"]
url: https://martinfowler.com/bliki/AssetCapture.html
slug: AssetCapture
word_count: 294
---


Asset capture is a strategy for developing a
  [StranglerFigApplication](https://martinfowler.com/bliki/StranglerFigApplication.html). You can think of many applications
  as managing a key set of assets. A payroll system looks after
  employees, a trading system looks after trades, a leasing system
  looks after leases. To gradually cut over to a new system, you can
  begin by identifying a subset of assets that you'll start with
  the new system. Often the best assets to start with are either
  simple assets (because they are quick to get going) or those that
  have needs that are particularly difficult to handle with the old system.


To make this work smoothly you'll need a mechanism to migrate
  assets from the old application to the strangler *and back
  again*. Reverse migration sounds unnecessary, yet it's very
  effective both to reduce the risk and to handle cases where an asset
  may dynamically change in such a way that the new application can no
  longer handle it. So an initial payroll system may not be able to
  handle employees on sick leave, bi-directional migration allows you
  to move an employee over when they fall sick.


In order to manage the assets you'll need to use [Event
  Interception](https://martinfowler.com/articles/patterns-legacy-displacement/event-interception.html) to make sure you grab all the events you need for the
  captured assets. You don't need to intercept all the events, just those for
  the captured assets. You may also need to ensure the old system doesn't get
  events for assets it no longer manages, using something like a [Content-Based
  Router](http://www.enterpriseintegrationpatterns.com/ContentBasedRouter.html)


Most rewrites I've worked on have used some form of asset
  capture. My only regret with it is that we didn't use finer grained
  capturing to allow more frequent releases. Often the blocker was not
  having bi-directional migration. Once that's in place frequent
  releases are much easier.
