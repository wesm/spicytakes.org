---
title: "Trans Media Application"
description: "Mobile is still a smaller   part of traffic than the traditional web, but its share is growing,   so we need to think about our strategy for developing effective   mobile applications. We discuss thin"
date: 2013-06-06T00:00:00
tags: ["team organization", "requirements analysis", "application architecture", "mobile", "front-end"]
url: https://martinfowler.com/bliki/TransMediaApplication.html
slug: TransMediaApplication
word_count: 1425
---


Mobile applications have been a hot item in software development
  over the past couple of years. Like many software delivery
  companies, Thoughtworks get a lot of requests from clients asking us
  to build a mobile application for them. However most of the time a
  company asks us (or anyone) to build a mobile application they are
  starting off on the wrong foot. I'd argue that for most situations,
  even though you want users to interact with a mobile device, 
  you should **never think of building a mobile application**.
  Instead you need to think about building a single application that presents
  across multiple devices: mobile, desktop, tablet - or whatever
  device your users might use.


![](images/transDeviceApp/app-per-device.png)


A common mistake is to think of different apps for different
    delivery devices.


![](images/transDeviceApp/trans-app.png)


Instead think of a single app with different presentations on
    different devices.


Imagine I'm using an app to find cool bars. There are many
  contexts in which I could use such an application:

- sitting in a coffee shop for breakfast, figuring out on my
    tablet where I'm
    going to meet my friends this evening.
- editing my photos at my desk 1 I see a picture of a really good
    bar I want to recommend to someone, so I access the application for
    information that I then email off with the photo
- it's five-thirty, I've had a long meeting, and I'm walking the
    streets looking for a nearby bar on my phone.
- I'm at home, with some friends, and we're exploring bar options
    for later on my ginormous flat screen tv.


In these cases what I'm trying to do is interact with some
   notional application, but I'm doing so through very different devices
   in very different contexts. Despite this, however, I don't want to
   see these as separate applications, but as different presentations
   of a single application. Ideally I could swap between them even in
   a single context (I don't know how to find bars near me on the
   web site on my laptop, so it's quicker to do it the way I normally do on
   the phone than look up the help docs.)


That's a consumer case, but the same thinking applies for
  in-house applications. If I'm a retail store manager I may do some
  stock checking by prowling the aisles with a tablet, but do other
  stock management work at my desk where I have a bigger monitor and
  keyboard.


As usual, what counts here is the user experience, it's about how
  software helps the user achieve their desires better.The user just
  wants that [âI
  Ruleâ](http://headrush.typepad.com/creating_passionate_users/2006/02/its_the_stupid.html) moment. The fact that the company commissioning the
  software wants to send out the web site and mobile app to different
  software houses is less relevant than 1923's baseball scores. So the
  user goes elsewhere and the app provider is a victim of the [shattered
  future](http://www.informit.com/articles/article.aspx?p=1946001).


> It's as though the single screens of yesterday have been
>     shattered and the shards have been embedded into our pockets, our
>     environment, and the products we use.
> -- [ Jonny LeRoy](http://www.informit.com/articles/article.aspx?p=1946001)


Such transmedia thinking 2 goes beyond the common
  phone/web/tablet devices. Back in 2005 when Tim O'Reilly launched
  the Web 2.0 meme, one his patterns for the next generation of
  software was [Software
  Above the Level of a Single Device](http://oreilly.com/pub/a/web2/archive/what-is-web-20.html?page=4). His exemplar for this was
  the iPod, whose success was partly due to how âThis application
  seamlessly reaches from the handheld device to a massive web
  back-end, with the PC acting as a local cache and control stationâ
  The product wasn't just the iPod, it was the iPod plus iTunes
  combination. Todays leading exemplar might be Netflix, which is a
  product you habitually use in a transmedia manner - with many
  different devices allowing you to see your movies on a TV, including
  one of which involves the post office as a data transport medium.


2: 
      The term âtransmediaâ comes from the concept of transmedia storytelling
      which is all about telling a single story that
      uses different media: film, comics, games etc. This is [different
      to using different representations of the same story](http://www.fastcompany.com/1745746/seven-myths-about-transmedia-storytelling-debunked), such
      as novelizations, in that the different media are intended to be
      woven into a single whole. This is why I think that âtransmediaâ
      is a good term to appropriate for this kind of application. (My
      thanks to Kyle Hodgson for introducing me to the transmedia
      meme.)


This last point should remind us that transmedia thinking is in
  many ways just basic systems analysis. When doing analysis work for
  a software project, the point is to look at the overall domain
  process and consider how software can best support it. The
  transmedia label helps remind us that software can pop up in all
  sorts of places where we might not consider it before.


An important of part envisioning a transmedia application is that
  each device is used in different contexts to do different things. As
  a result the experience needs to designed with these contexts in
  mind - both in being aware of the different contexts and thinking
  about how they flow together. If you're looking for bar on your
  phone, you're much more likely to want to know nearby bars than if
  you're going through the website on your desk. If you're interacting
  with a travel management application, it should be able to tell that
  you're accessing via a phone, you're in your connecting airport
  between two flights, and thus make it easy for you to see how long
  you have to get to your connecting flight and how to get to the
  gate.


This is why I consider the desire to create a mobile application
  to be a Wrong Thought. It immediately frames the mobile application
  as something separate from the web site, as is the thinking that
  you're building just a web site. Instead you need to start
  with the user, figuring out what it is that they want to do and how
  software can help them do that. When thinking about this everyone
  needs to be thinking in a transmedia manner - and by everyone I
  mean all parts of the work: user experience, software architecture,
  project management…. The application, and the project team that
  builds it, need to be thought of as a single whole, all dedicated to
  making their users happy.


## Further Reading

- Kelly Sommers (kellabyte) [provides
      an example](http://kellabyte.com/2012/04/06/creating-boundless-experiences-with-continuous-client-and-transmedia) what a transmedia application might look like.
      This article also explores the notion of transmedia storytelling with
      some interesting links and videos.
- Joshua Topolsky coined the term [Continuous
      Client](http://www.engadget.com/2010/05/26/a-modest-proposal-the-continuous-client/) which is a similar concept 3, Kelly Sommers also has a
      post with thoughts about [implementing
      a continuous client](http://kellabyte.com/2011/06/26/continuous-client-my-first-attempt-at-multi-device-user-experience-transitions/).
- Google produced a research report on [navigating the new
      multi-screen world](http://googlemobileads.blogspot.com/2012/08/navigating-new-multi-screen-world.html), which is their thinking on the transmedia
      application.
- Jonny LeRoy wrote a couple of articles on [surviving the
      shattered future](http://www.informit.com/articles/article.aspx?p=1946001), talking about the challenges in a world where
      users want to use different media to interact.


## Notes


1: 
      A lot of people I talk to these days think the desktop is fast
      dying and that in time all our computer usage will be using
      tablets or mobiles. But I like working at a desk. When we bought
      our house I ensured we installed an ethernet jack on the porch
      so I could do my email on a laptop (this was before wireless).
      And for several years I'd use my laptop like this for a good
      chunk of time. But eventually I found it too limiting to work
      that way compared to the huge monitors on my desk. So while I
      think there's an increasing role for tablets and other devices,
      I still think the desktop will remain an important environment.


2: 
      The term âtransmediaâ comes from the concept of transmedia storytelling
      which is all about telling a single story that
      uses different media: film, comics, games etc. This is [different
      to using different representations of the same story](http://www.fastcompany.com/1745746/seven-myths-about-transmedia-storytelling-debunked), such
      as novelizations, in that the different media are intended to be
      woven into a single whole. This is why I think that âtransmediaâ
      is a good term to appropriate for this kind of application. (My
      thanks to Kyle Hodgson for introducing me to the transmedia
      meme.)


3: 
      Although continuous client is clearly a very similar concept, I
      do see a distinction in that I can imagine applications that are
      designed and experienced as separate applications supporting
      continuous client behavior by coordinating on how they do
      hand-offs between each other. The result would be an effective
      continuous client, but not a holistic transmedia application.
