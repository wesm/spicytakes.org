---
title: "Moving To Nokogiri"
description: "Most of this site, including this bliki, is built using an XML to HTML transformation process. I write the articles and bliki entries in my own XML vocabulary and then transform these sources to the H"
date: 2011-01-10T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/MovingToNokogiri.html
slug: MovingToNokogiri
word_count: 750
---


Most of this site, including this bliki, is built using an XML to
HTML transformation process. I write the articles and bliki entries in
my own XML vocabulary and then transform these sources to the HTML you
read. When I stated back in 2000 I did it in XSLT. While I got pretty
good at programming XSLT I came to the conclusion that I was not
enough of a masochist to want to continue using it. After a short
experiment, writing the bliki transformer in Ruby on a flight to
Bangalore, I switched to Ruby using the REXML library. Now it's time
to change that core library to Nokogiri


When I started the Ruby transformer the default way to parse XML in
Ruby was the REXML library. Although it had its quirks, on the whole I
liked it. The API was certainly much easier to work with than the java
libraries of that era. But time has marched on. REXML is a ruby
library and is thus slow compared to libraries based on libxml. Other
libraries have come out that provide a nicer API to work with.


The popular choice for XML parsing these days seems to be
Nokogiri. As a result over the last few months I've given it a spin
for a number of transformation tasks and have grown to like it. It
soon became my first choice for new transformation tasks. But this
still leaves the big question, should I replace REXML for my core
transformations?


Until recently, my life has been dominated by the DSL book, so I
didn't consider any serious work on my site generation code. Once that
was done my first priority was to redo the look and feel of the site
and introduce the guide pages. This didn't require much surgery to the
existing ruby code, so I left it as it is. But my next steps require
more serious refactoring of that code, which brought the thought of
Nokogiri replacement more to the front of my thinking.


Indeed I decided to tackle it first, for two reasons. One is that
much of the transformation code involves mucking around with XML, and
I want to use Nokogiri's API to do that. Second is that my primary
functional test is to rebuild the site and diff the result with the
released version. Nokogiri's speed advantage (10 seconds versus 1
minute) becomes more important when I'm doing that.


## Making the change


Replacing the XML library in a program that mainly does XML
processing is often seen as a fraught task. There are REXML calls all
over the code, so this is very much a global change. Since I'm the
only programmer I can be more casual than if I was working on a team
with this, but I still follow much the same habits that I would if
working with other people.


The basic plan comes in three steps:

- Introduce an insulating layer between my code and REXML. This way
all my transformation code calls this insulating layer which then
passes on the calls to REXML. At this stage the interface of the
insulating layer is close to REXML.
- Create an alternative implementation of the insulating layer that
passes the same calls onto Nokogiri instead. Once I'm done with this I
can build the site entirely with Nokogiri.
- Adjust the interface and application code to change it from REXML
style to Nokogiri style. Finish by removing the insulation layer.


I use this approach to keep the steps smaller. Switching over to
Nokogiri in one fell swoop is too big a change, instead I can
gradually implement it while my site can still build fine with the
REXML version until the Nokogiri implementation is complete. If I was
working with others, this would be more important as I'd need to have
them building new functionality while I was doing the surgery. This
way I can gradually ease them over to the insulating layer while it's
being built.


There's an argument for leaving the insulating layer in place,
effectively turning it into an anti-corruption layer. That would be a
good idea if I wanted use a different API to Nokogiri's. I didn't do it
in this case since I actively want to use the Nokogiri API. Of course
this means that should I change the library I'll have to rebuild it
then, but I'd rather pay that price then than have to pay the price of
dealing with an unnecessary layer now.
