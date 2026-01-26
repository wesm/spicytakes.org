---
title: "Evolving Publication"
description: "When I was starting out on my writing career, I began with     writing articles for technical magazines. Now, when I write     article length pieces, they are all written for the web. Paper     magazi"
date: 2015-12-03T00:00:00
tags: ["writing"]
url: https://martinfowler.com/bliki/EvolvingPublication.html
slug: EvolvingPublication
word_count: 1318
---


When I was starting out on my writing career, I began with
    writing articles for technical magazines. Now, when I write
    article length pieces, they are all written for the web. Paper
    magazines still exist, but they are a shrinking minority, probably
    doomed to extinction. Yet despite the withering of paper
    magazines, many of the assumptions of paper magazines still exact
    a hold on writers and publishers. This has particularly risen up
    in some recent conversations with people working on articles I
    want to publish on my site.


Most web sites still follow the model of the Paper Age.
    These sites consist of articles that are grouped primarily due to
    when they were published. Such articles are usually written in one
    episode and published as a whole. Occasionally longer articles are
    split into parts, so they can be published in stages over time (if
    so they also may be written in parts). 1


1: 
       One of the infuriating things about these serial articles, is that
       there's often little thought to how the series should be read after
       publication. I often come across these articles where part 3 refers to
       parts 1 and 2, but part 1 doesn't get updated to refer to the later
       installments. This suggests to me that the publisher isn't thinking of
       the series as an article that's going to be valuable in the long-term.


Yet these are constraints of a paper medium, where updating
    something already published is mostly impossible. 2 There's no
    reason to have an article split over distinct parts on the web,
    instead you can publish the first part and revise it by adding
    material later on. You can also substantially revise an
    existing article by changing the sections you've already published.


2: 
      There is a sort of an update mechanism, in that a series of
      articles might be republished as a single work. But that is
      relatively rare.


I do this whenever I feel the need on my site. Most of the
    longer-form articles that I've published on my site in the last
    couple of years were published in installments. For example, the [popular article on
    Microservices](https://martinfowler.com/articles/microservices.html) was originally published over nine installments
    in March 2014. Yet it was written and conceived as a single
    article, and since that final installment, it's existed on the web
    as a single article.


Our first rationale for publishing in installments is the
    notion that people tend to prefer reading shorter snippets these
    days, so by releasing a 6000 word article in nine parts, we could
    keep each new slug to a size that people would prefer to read. A
    second reason is that multiple
    publications allows for more opportunities to grab people's
    attention, so makes it more likely that an article will find
    interested readers.


When I publish in installments, I add an item to my news feed and
    tweet for each installment. Since I'm describing an update, I link with a
    fragment URL to take readers to the new section (in future I may
    link to a temporary explanatory box to highlight what's in the new
    installment).


But whatever the way the article is released to the world, it
    is still a single conceptual item, so its best permanent form is a
    single article. Many people have read the microservices article since that
    March, and I suspect hardly any of them knew or cared that it was
    originally published in installments.


In that case we wrote the entire article before we started the
    installment publishing, but there's no reason against writing it
    in stages too. For my [collection pipelines](https://martinfowler.com/articles/collection-pipeline/) article, I wrote and
    published the original article over five installments in July
    2014. As I was writing it, I was conscious that there were
    additional sections I could add. I decided to wait to see how the
    article was received before I put the effort in to write those
    sections.
    Since it was pretty popular, I made a number of revisions, for each one I
    announced it with a tweet and
    an item on my feed. 3


3: 
      Another great example, written after I wrote this post, was Cade and
      Daniel's article on [The Basics of Web Application
      Security](https://martinfowler.com/articles/web-security-basics.html). They wrote the first few installments in early 2016 and
      weren't sure what additional sections they would write (or even if they
      would have the energy to do them). They ended up writing a handful of
      further installments over the course of the next year.


Letting an article evolve like this is the kind of thing
    that's difficult in a print medium, but exactly the right thing to
    do on the web. A reader doesn't care that I revised the article to
    improve it, she just wants to read the best explanation of the
    topic at hand. 4


4: 
      Another form of revision is the wholesale revision of an article to
      incorporate what's been learned since the article was written. Jason Yip
      originally wrote his article on [stand-up
      meetings](https://martinfowler.com/articles/itsNotJustStandingUp.html) in 2006, but did deep revisions in 2007, 2011, and 2016.
      (Sometimes it's worth the effort to make a serious revision to an article,
      and sometimes it's best to evolve it by just adding a couple of
      footnotes.)


I do like to provide some traces of such revisions.
    At the end of each article, I include a revision history which
    briefly summarizes the changes. For a couple of revisions, such as
    the 2006 revision of my article on Continuous Integration, I made
    the original article available on a different URL with a link from
    the revised article. I don't think the original article is useful to most readers,
    only really to those tracing the intellectual history of the idea,
    so shifting the original to a new URL makes sense.


The role of the feed is important in this. The traditional blog
    reinforces the Paper Age model by encouraging people to match an article
    with its feed entry. For longer articles, I prefer to consider
    them as different things, the feed is a notice of a new article or
    revision, which links to the article concerned. That way I
    generate feed entries each installment where the feed summarizes
    what's been added.


The point of all this is that we should consider web articles
    as information resources, resources that can and should be
    extended and revised as our understanding increases and as time
    and energy allow. We shouldn't let the Print Age notions of how
    articles should be constructed dictate the patterns of the
    Internet Age.


## Notes


1: 
       One of the infuriating things about these serial articles, is that
       there's often little thought to how the series should be read after
       publication. I often come across these articles where part 3 refers to
       parts 1 and 2, but part 1 doesn't get updated to refer to the later
       installments. This suggests to me that the publisher isn't thinking of
       the series as an article that's going to be valuable in the long-term.


2: 
      There is a sort of an update mechanism, in that a series of
      articles might be republished as a single work. But that is
      relatively rare.


3: 
      Another great example, written after I wrote this post, was Cade and
      Daniel's article on [The Basics of Web Application
      Security](https://martinfowler.com/articles/web-security-basics.html). They wrote the first few installments in early 2016 and
      weren't sure what additional sections they would write (or even if they
      would have the energy to do them). They ended up writing a handful of
      further installments over the course of the next year.


4: 
      Another form of revision is the wholesale revision of an article to
      incorporate what's been learned since the article was written. Jason Yip
      originally wrote his article on [stand-up
      meetings](https://martinfowler.com/articles/itsNotJustStandingUp.html) in 2006, but did deep revisions in 2007, 2011, and 2016.
      (Sometimes it's worth the effort to make a serious revision to an article,
      and sometimes it's best to evolve it by just adding a couple of
      footnotes.)
