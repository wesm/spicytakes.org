---
title: "Dark Launching"
description: "Dark launching a feature means taking a new or changed back-end behavior   and calling it from existing users without the users being able to tell it's   being called. It's done to assess the addition"
date: 2020-04-29T00:00:00
tags: ["continuous delivery"]
url: https://martinfowler.com/bliki/DarkLaunching.html
slug: DarkLaunching
word_count: 388
---


Dark launching a feature means taking a new or changed back-end behavior
  and calling it from existing users without the users being able to tell it's
  being called. It's done to assess the additional load and performance impacts
  upon the system before making a public announcement of the new capability.


![](images/dark-launch/sketch.png)


An example of this might be adding cross-selling recommendations to a
  retail site's checkout flow. (The kind of thing that says if I buy a toaster,
  I clearly want to also buy a new set of steak knives.) Figuring out
  recomendations will obviously add some time and load to the system, slowing
  down the checkout process and potentially the whole site. Dark launching gives
  us a way of assessing this impact before we release the feature to the public.
  We begin by using an [Keystone Interface](https://martinfowler.com/bliki/KeystoneInterface.html) to build the new
  feature, integrating into production releases of the code, but with no
  user-interface so the users cannot tell it's there. But before we add the
  keystone, we modify the checkout flow to call the recommendation engine just
  as we would do in production, but not showing the results in the UI. This way
  the recommendation does all the work it would do when it's released, but
  nobody can see that it's doing it. If we use a [Feature Flag](https://martinfowler.com/bliki/FeatureFlag.html) we can switch the recommendation on and off easily in
  production, so if we do see an worrying impact on performance we switch it off
  before anyone really notices. We can then continue to tune the recommendation
  engine until its performance is acceptable, at which point we can finally add
  the keystone and reveal the feature to the world


Dark launching can also enable parallel running of a
  re-implemented feature. The old and new code can both be called and their
  results checked to see if there are changes with the new algorithm, but only
  one answer returned to the interface.


Dark launching works best when it's a process that enhances existing user
  interactions and isn't something users choose to do. To test something that
  depends on a user's choice, [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html) is the way to go.


Since the term first
  appeared, however, its usage has been subject to [Semantic Diffusion](https://martinfowler.com/bliki/SemanticDiffusion.html). So I've heard people use âdark launchâ to mean
  canary releases, or other variations on partial release strategies.
