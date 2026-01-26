---
title: "Datensparsamkeit"
description: "Datensparsamkeit is a German word that's difficult to translate   properly into English. It's an attitude to how we capture and store   data, saying that we should only handle data that we really   ne"
date: 2013-12-12T00:00:00
tags: ["database", "web development", "internet culture", "legal", "data analytics", "privacy"]
url: https://martinfowler.com/bliki/Datensparsamkeit.html
slug: Datensparsamkeit
word_count: 834
---


Datensparsamkeit is a German word that's difficult to translate
  properly into English. It's an attitude to how we capture and store
  data, saying that we should only handle data that we really
  need.


![](images/datensparsamkeit/sketch.png)


These days there's a lot of hype around the idea of Big Data -
  and with it the notion that we should capture and store every bit of
  data we can get our hands on. We might not have an immediate use for
  the contacts our users store in their address books, but we'll ask
  for it anyway in case it comes in useful later. We'll record every
  click on our website and squirrel it away in case we want to trawl
  it later. We set up our smartphone app to ask for location information so
  if we come up with some way to use that data later, we can. After
  all, storage is cheap - so why not?


The problem with the âcapture-it-allâ approach is that it raises
  serious questions of privacy. Even if we trust ourselves to not
  abuse the data we collect, each data store represents a target for
  criminals or government surveillance agencies. This issue is
  particularly fraught in Germany which has seen successive regimes
  where governments have carried out extensive surveillance of their
  citizens in order to control them. Germany consequently has strong
  data privacy laws.


Datensparsamkeit 1 is a concept from these privacy laws that is an
  opposite philosophy to âcapture-all-the-thingsâ. A translation isn't
  straightforward (which is why I've retained the German word) but
  loosely you might translate it as something like âdata austerityâ,
  âdata minimizationâ, âdata parsimonyâ, or âdata frugalityâ  2. It means
  that you should always ask yourself why you are capturing or storing
  data, and look to handle only the minimum amount of data you need
  for your purpose.


1: 
      Here's some [help on pronunciation](http://www.forvo.com/word/datensparsamkeit/)


2: 
      Since I originally wrote this entry, the principle has got a lot more
      traction, particularly with the introduction of the European Union's GPDR
      rules. In this context I'm increasingly hearing the concept referred to as
      âData Minimizationâ. I'm keeping this page with its original name for the
      moment.


An example of this is tracking users on your web site to
  determine how many unique visitors you have. If the same person
  accesses several pages within a few hours, you want to count that as
  one visit. If they visit several times a month, you still only want
  to count them as a single visitor. One way to do this is to log
  IP addresses, you count each IP address as a single person 3. But an IP address is very revealing, and could be
  used for much more than counting vistors. Datensparsamkeit suggests
  that you shouldn't store the IP address directly, perhaps instead
  you should hash it and only store the hash.


3: 
      I realize that with Network Address Translation, things are
      rather more involved than this, but I wanted a simple example.


A similar example involving IP addresses is using them to infer
  demographic information such as region and country. You can get most
  of this information and practice datensparsamkeit by just logging the first
  three octets of the IP address.


Datensparsamkeit isn't just about bad people stealing data, it's
  also about your relationship with the primary company themselves.
  The default attitude at the moment is that any data you generate is
  not just freely usable by the capturer but furthermore becomes their
  valuable commercial property.  Privacy advocates,
  including me, think this assumption needs to be changed. Companies
  should only capture what they need and the burden of demonstrating
  need should fall on them. In addition, of course, they must be
  completely transparent about what they capture, what they store, and
  who they share their data with. Any breaches of data security must
  be immediately publicized (instead of covered up, which is the
  current default).


Even if you don't share my views on personal control of our own
  data, the risks of security breaches mean that datensparsamkeit is a
  wise course of action. If you hold data that you don't need, and
  someone steals it and causes damage, shouldn't you be liable for
  that damage? Even if there's no legal liability the publicity will
  have serious consequences - and thus there is risk for anyone who
  doesn't practice datensparsamkeit.


## Acknowledgements

[Erik Dörnenburg](http://erik.doernenburg.com/)
introduced me to Datensparsamkeit. The meme â… all the thingsâ
    seems to have been around forever (at least a decade) so I'm glad
    Korny Sietsma taught me that
[it started in 2010](http://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html)
.

## Notes


1: 
      Here's some [help on pronunciation](http://www.forvo.com/word/datensparsamkeit/)


2: 
      Since I originally wrote this entry, the principle has got a lot more
      traction, particularly with the introduction of the European Union's GPDR
      rules. In this context I'm increasingly hearing the concept referred to as
      âData Minimizationâ. I'm keeping this page with its original name for the
      moment.


3: 
      I realize that with Network Address Translation, things are
      rather more involved than this, but I wanted a simple example.
