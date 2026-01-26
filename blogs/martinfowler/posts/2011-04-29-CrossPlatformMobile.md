---
title: "Cross Platform Mobile"
description: "With the rise of so many mobile platforms, each with a different   UI, many people are looking at cross-platform toolkits. These allow   you to write a mobile app once and then deploy it to a range of"
date: 2011-04-29T00:00:00
tags: ["programming environments", "tools", "mobile"]
url: https://martinfowler.com/bliki/CrossPlatformMobile.html
slug: CrossPlatformMobile
word_count: 1244
---


With the rise of so many mobile platforms, each with a different
  UI, many people are looking at cross-platform toolkits. These allow
  you to write a mobile app once and then deploy it to a range of
  mobile devices. Are these toolkits worth using?


A cross-platform toolkit is alluring. There are
  a bunch of mobile devices out there, and it's a lot of work to write
  applications for every one. It would be so much easier if we could
  write once and run anywhere.


Of course we've been here before, with desktop applications. Over
  the years there were lots of attempts to create cross-platform
  environments for desktops. Java is perhaps the best known, but it
  was neither the best nor the first (ask Smalltalkers to tell you
  about VisualWorks). But you may notice that cross-platform apps
  have, on the whole, not been successful. 12


1: 
      These issues are issues about cross platform apps with a
      graphical UI. Libraries without a UI work very well in a
      cross-platform manner. As a result often the best strategy on a
      desktop is to combine cross-platform libraries with a custom UI
      for each platform.


2: 
      A notable exception is [Jetbrains's](http://www.jetbrains.com/) family of
      development tools. I don't have an explanation of why they are
      such an exception.


The first issue is handling the variations between UI controls on
  different platforms. You have two broad strategies: you can
  either use native components on each platform or emulate components
  using more primitive graphics - effectively creating your own UI
  system. In the Java world this was the difference between Swing
  (emulation) and SWT (native controls).


Both approaches have problems. If you use native controls you
  have to deal with the fact that similar controls on different
  platforms have slight differences in how they work, which makes it
  hard to come up with a good abstraction. Furthermore you have to
  decide about what to do with capabilities that are only available on
  some platforms - do you end up with the lowest common denominator of
  your platforms?


So emulation becomes attractive, either as an entire approach or
  to make up for controls you can't get on some platforms. Emulation
  has a couple of difficulties: firstly it's hard to get an emulated
  UI to perform responsively enough - which is a big deal for UI
  controls. Secondly it's very difficult to get them to perform
  exactly like the native controls. It's easy to get trapped in an
  [uncanny
  valley](http://en.wikipedia.org/wiki/Uncanny_valley) where things work mostly like the native controls but
  there are just enough tiny differences to throw users off. With UI
  controls you have to be really anal to get the behavior âjust
  rightâ.


Getting good UI controls are almost impossible, but that's not
  the biggest issue - which is more about the overall user
  experience. Different platforms have different ways they expect you
  to use them that alter the entire experience design. If you use a
  Unix-based system, a good experience design will make extensive use
  of the middle mouse button, since that's the way of Unix UIs. But
  try that on a Mac and you'll struggle, since the Mac thinks even two
  buttons are too many.


Mobile devices have an even bigger burden here as they have a
  greater disparity in how they approach the overall user
  interaction. Recently a client asked us to take an iPhone app we'd
  developed for them and make a version for Android. Our initial
  experiments showed us that we had to completely rethink the
  experience design from scratch to get a decent Android app. The test
  cases for the iPhone app made an extremely valuable check-list for
  the capabilities of the Android app, but the whole feel of the app
  had to be different.


So for these reasons I think cross-platform mobile toolkits are a
  dead-end. It's just too hard for them to really mimic the native
  experience. If it's worth building a native app, it's worth building
  it properly, including an individual experience design for that
  platform. 3


3: I see one path that might prove me
      wrong. In this scenario you use a cross-platform toolkit - but
      you write a different app, with a different experience design,
      for each platform you build for. The gain over doing this with
      native code is that you have a single platform for your
      developers to use and can get some reuse of common code
      (particularly non-UI code). This strategy doesn't address the
      problem of dealing with UI controls, and even if it works, it's
      only worthwhile if the developer-understanding and code reuse
      benefits are significant.


So where does this leave people who want to support lots of
  mobile platforms, but aren't prepared to deal with the cost of
  native apps for each one? Fortunately we do have a single platform
  that runs on any worthwhile mobile device - the web.  Web apps can
  be very functional and capable these days when written by people who
  know what they are doing. The biggest issue here is offline use. If
  you can live with online all the time, then this won't be a problem,
  but if you need offline you'll need to explore the [various local storage
  options](http://diveintohtml5.org/storage.html).


When you do the web app, don't try to make it look and feel like
  a native app - make it look like a mobile web app. It'll still be as
  usable as an emulated app, but will avoid plunging your users into
  the uncanny valley. This mirrors what has happened on the desktop,
  where people who want to support multiple desktop platforms have
  found the web to be an effective deployment platform. The key to its
  success here is that people expect web apps to behave like web apps,
  so they don't expect them to be like native apps - avoiding the
  problems of different user expectations on different platforms.


## To summarize:

- Don't use cross-platform toolkits
- For maximum reach: built a web app that looks like web
    app
- To appeal to a particular platform: build a native app for that
    platform, with a experience design based on that platforms
    interaction style


## Follow-Ups


Some thoughts and reactions from emails and other comments


One correspondent talked about how his company creates native apps
that are thin wrappers around web apps. This provides ease of
launching and getting to common links, while keeping most of the
behavior within the cross-platform web.


Gunnar Peterson argues that [differences
in security models](http://1raindrop.typepad.com/1_raindrop/2011/04/mobile-security-back-to-the-future.html) also discourage cross-platform toolkits.


## Notes


1: 
      These issues are issues about cross platform apps with a
      graphical UI. Libraries without a UI work very well in a
      cross-platform manner. As a result often the best strategy on a
      desktop is to combine cross-platform libraries with a custom UI
      for each platform.


2: 
      A notable exception is [Jetbrains's](http://www.jetbrains.com/) family of
      development tools. I don't have an explanation of why they are
      such an exception.


3: I see one path that might prove me
      wrong. In this scenario you use a cross-platform toolkit - but
      you write a different app, with a different experience design,
      for each platform you build for. The gain over doing this with
      native code is that you have a single platform for your
      developers to use and can get some reuse of common code
      (particularly non-UI code). This strategy doesn't address the
      problem of dealing with UI controls, and even if it works, it's
      only worthwhile if the developer-understanding and code reuse
      benefits are significant.
