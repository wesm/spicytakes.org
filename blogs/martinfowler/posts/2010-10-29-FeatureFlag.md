---
title: "Feature Flag"
description: "One of the most common arguments in favor ofFeatureBranchis that it provides a mechanism for pending   features that take longer than a single release cycle. Imagine you are   releasing into productio"
date: 2010-10-29T00:00:00
tags: ["continuous delivery"]
url: https://martinfowler.com/bliki/FeatureFlag.html
slug: FeatureFlag
word_count: 1110
---


One of the most common arguments in favor of
  [FeatureBranch](https://martinfowler.com/bliki/FeatureBranch.html) is that it provides a mechanism for pending
  features that take longer than a single release cycle. Imagine you are
  releasing into production every two weeks, but need to build a
  feature that's going to take three months to complete. How do you
  use Continuous Integration to keep everyone working on the mainline
  without revealing a half-implemented feature on your releases? We
  run into this issue quite a lot and feature flags are a handy tool
  to deal with it.


![](images/featureToggle/featureToggle.png)


(Although “flag” is probably the most popular term for this now, “toggle”
  is still widely used 1. In this post I'll use both
  interchangeably.)


1: 
      (July 2023) When Pete and I originally wrote the blog post and article in
      the mid 2010s “flag” and “toggle” were both used; together with feature
      bits, flippers, switches, and the like. Since then “flag” seems to have
      settled down as the most common term, but we still see toggle used
      reasonably frequently.


The basic idea is to have a configuration file that defines a
  bunch of flags for various features you have pending. The running
  application then uses these toggles in order to decide whether or
  not to show the new feature.


Most of these decisions occur in the user-interface of the
  application. So if you are building a web application using jsp, you
  may use a set of jsp tags to surround any user-interface parts of a
  pending feature.


```

    <toggle name="petSurvey">
      <p>Take our new <a href = 'petSurvey'>pet survey</a></p>
    </toggle>

```


The implementation of the toggle tag then just passes through the
  content if the flag is set to on, and skips it otherwise. Other UI
  technologies will use different details, but the basic notion of
  wrapping the pending elements is the same.


Some features may be like introducing a new pricing algorithm,
  where there might be no user-interface elements. Here the test of
  the flag would be in the application code, it could be as crude as
  a conditional test, or something more sophisticated like a strategy
  wired through dependency injection.


Toggle tests should only appear at the minimum amount of **toggle points**
  to ensure the new feature is properly hidden. There could be many
  screens in the pet survey feature, but if there's only one link on
  the home page that gets you there, then that's the only element that
  needs to be protected with the toggle tag. Don't try to protect
  every code path in the new feature code with a flag, focus on just
  the entry points that would lead users there and toggle those entry
  points. If you find that creating, maintaining, or removing the
  flags takes significant time, then that's a sign that you have too
  many toggle tests. Remember that although simple conditionals are
  the easiest way to implement a toggle, you should use techniques
  like polymorphic substitution to minimize how many points the flag
  is tested.


So far I've described feature flags as something you use to hide partly built
  features, a kind of feature flag I call **release toggles**. Hodgson also
  identifies **experiment toggles** for A/B testing, **ops toggles** to
  provide controls for operations staff, and **permissioning toggles** to control
  access of features for different subsets of users.


Most feature flags I've heard about are set at run-time, but
   I've also seen cases where release toggles are set at build time.
   The small advantage of a build time toggle is that none of the new
   feature's code gets compiled into the released executable.


One danger with feature toggles is an accidental exposure, when
  someone forgets to wrap the UI feature in a toggle tag. This is
  awkward to test, since it's difficult to form a test that
  nothing that should be hidden is visible without calling out the
  individual elements - which are likely to be forgotten at the same
  time.


A common question we hear about feature flags concerns testing
  - does using feature flags mean a combinatorial
  explosion of tests? In general there's no need to test all
  combinations of features. For release flags it's usually
  sufficient to run two combinations

- all the flags on
  that are expected to be on in the next release
- all flags on


This is pretty much the same as what you need to do with feature
  branches if you want to find any integration bugs.


It's very important to retire release flags once
  the pending features have bedded down in production. This involves
  removing the definitions on the configuration file and all the
  code that uses them. Otherwise you will get a pile of toggles that
  nobody can remember how to use. In one memorable example I heard of,
  it required making a special recompilation of the linux kernel to
  handle enough command line switches.


## Release flags are the last thing you should do


Release flags are a useful technique and lots of teams use
    them. However they should be your last choice when you're dealing
    with putting features into production.


Your first choice should be to break the feature down so you
    can safely introduce parts of the feature into the product. The
    advantages of doing this are the same ones as any strategy based
    on small, frequent releases. You reduce the risk of things going
    wrong and you get valuable feedback on how users actually use the
    feature that will improve the enhancements you make later.


If you really must hide a partly built feature, then the best way is to
    use a [Keystone Interface](https://martinfowler.com/bliki/KeystoneInterface.html): build all of it save the UI
    entry point and add that UI in a single release cycle. This way the non-ui
    code is fully integrated with everything else, but nothing is visible or
    used until you add the last bit at the end.


Only if you can't do small releases or a [Keystone Interface](https://martinfowler.com/bliki/KeystoneInterface.html) should you
    employ release flags.


## Further Reading


For a detailed picture of feature flags and their usage, look at [Pete Hodgson's
    article](https://martinfowler.com/articles/feature-toggles.html).


## Acknowledgements


(Thanks to Charles Bradley, Kent Beck and Christian Gruber for tweets that reminded
    me of points I forgot to include.)


## Revisions

Updated 2016-02-12 to fit in with Pete Hodgson's detailed article.
    2023-07-14 changed url and title to “FeatureFlag” and replaced many uses in
    the text to “flag”.

## Notes


1: 
      (July 2023) When Pete and I originally wrote the blog post and article in
      the mid 2010s “flag” and “toggle” were both used; together with feature
      bits, flippers, switches, and the like. Since then “flag” seems to have
      settled down as the most common term, but we still see toggle used
      reasonably frequently.
