---
title: "Atom Feeds"
description: "(Updated as Sam Ruby persuaded me to use second-precision on my dates.)"
date: 2007-01-02T00:00:00
tags: ["tools"]
url: https://martinfowler.com/bliki/AtomFeeds.html
slug: AtomFeeds
word_count: 1491
---


(Updated as Sam Ruby persuaded me to use second-precision on my dates.)


When I started this bliki, on that flight to Bangalore, I decided
	to use RSS 0.91 for my feed on the grounds that it was simple. All I
	had to do was look at an example (PragDave's as it happened) and I
	could easily create the XML provide that capability.) It's served
	me well, but I do get occasional complaints that the posts aren't
	dated.


I asked Ade Oshineye, the man who keeps [ThoughtBlogs](http://www.thoughtworks.com/blogs) running for his
advice. He gave me a page of carefully considered reasons for either
staying with RSS 0.91 or choosing a new format (and which one). In the
end I followed his rather more passionate conclusion: âFor the love of
god please use [Atom](http://en.wikipedia.org/wiki/Atom_(standard)).â


Cutting to the chase, I now have atom feeds. I still have the RSS
	0.91 feeds, but if I ever have to do any work to maintain them I
	     will summarily drop them. So I suggest cutting over to the atom
	     feeds when you can. I've updated the references on my web pages
	     for them or you can find them in the now badly named [RssFeeds](https://martinfowler.com/bliki/RssFeeds.html) page.


What follows are a few experiences and thoughts on the conversion.


Over Christmas I dug out what information I could find on
	atom. My first thought was to find and use Ruby libraries. Ruby has
	a pretty sophisticated feed processing library called [FeedTools](http://sporkmonger.com/projects/feedtools/). It
	claimed it could produce a feed, and I believe it. However all the
	documentation was about consuming and converting feeds, caching them
	in a database, and the like. It introduced a bunch of dependencies
	and it wasn't glaringly obvious how to use it just to create a feed.


So I decided to create the XML file myself. After all this is
	very easy in Ruby, especially now we have the awesome [builder](http://builder.rubyforge.org/)
	library.


So the next trick was to figure out what an atom file looked like
	and what the bits meant. I found three things very helpful to
	me.

- Me being me, I always want a real life example. I reckoned [Sam
		Ruby's](http://www.intertwingly.net/blog/) [feed](http://www.intertwingly.net/blog/index.atom) should
		be a good exemplar.
- One big reason Ade gave for favoring atom was a solid
		[specification](http://atompub.org/rfc4287.html). Like most specifications I skimmed it to answer the
		questions I needed. In general I prefer to start with an example
		and gradually tweak it until it works, going to the specification
		when I have a problem. This is the typical behavior of a [moron](http://diveintomark.org/archives/2004/08/16/specs).
- Possibly the best reason to use Atom is the excellent test
		framework: [feedvalidator](http://feedvalidator.org/). I found this
		to be extremely helpful.


I have three feeds to work on: my updates feed, my bliki feed,
	and the feed for refactoring.com. The data for the feeds came from
	different formats, so this was the common but tedious task of data
	conversion from one arbitrary format to another. Much of enterprise
	software is like this, and it's not the fun part.


I started out by creating my own feed and entry objects to act as
[gateways](https://martinfowler.com/eaaCatalog/gateway.html).
This way I could program to objects that made sense to me for the
three conversions and keep the XML conversion and any atom weirdness
that might appear in one place. Initially I wondered if this would
be worthwhile, after all builder is so simple to use. I quickly found
it to be worthwhile.


Most of the process was very straightforward. I just looked at
	how I created the RSS feed and did the same with the atom feed. (Yes
	I know I should have used gateways for the old RSS feeds. I get to
	be foolish too.) The tricky bits were really about things that were
	new to the atom feed.


The first of these were ids. Atom insists that you give each
	entry an id. This makes it easier for aggregators to spot multiple
	copies of the same entry that might come from different sources, or
	just to tell if a new entry is a truly new entry or an updated old
	entry. For my bliki it was easy to choose an id - the entries
	correspond exactly to the web bliki entries so I just used the URL
	of the bliki entry.


For news updates there isn't a particular page. Looking at Sam
	Ruby's page I saw he used tags. These were new to me, but googling
	found an [explanation](http://www.faqs.org/rfcs/rfc4151.html). I
	generated tags with my domain name, a date, and cleaned up text from
	the title - copying from Sam Ruby again.


```

def calculate_atom_id
  specific = title.gsub(/\W/,'-')		
  return âtag:#{domain_name},#{date.strftime(â%Y-%m-%dâ)}:#{specific}â
end

```


The real driving purpose of this was to add dates and this
	introduced a couple of oddities. First was the [RFC 3339 dates](http://www.apps.ietf.org/rfc/rfc3339.html), which
	I had to look up to see how they worked. It didn't look like the
	Ruby date classes had a method to return an RFC 3339 date, but after
	some poking around I realized that the Time class has exactly what I
	need as the method Time.xmlschema.


One thing that wasn't clear in the spec was what the updated date
really meant. The spec merely said it was  âthe most recent instant in
time when an entry or feed was modified in a way the publisher
considers significant.â When I change a bliki entry it's either to fix
a typo, or to revise the entry in some way. Typos I don't
consider significant. I do expect aggregators to update their copy of
the entry, but I don't expect them to highlight it as new or changed. The
latter changes I do expect to be highlighted. It would have been
helpful had the spec given some suggestions as to how aggregators and
readers might interpret the date - after all it's that interpretation
that conveys the true meaning of the field. I often find this problem,
writers of specifications are reluctant to put in a standard what
clients should do, because they don't want to constrain clients. I
understand that concern, but I do think it's really helpful to say how
they imagine it might be used with some scenarios.


The most awkward aspect of the updated date for me is the
precision of the updated date. The atom spec says that âDate values
should be as accurate as possible. For example, it would be generally
inappropriate for a publishing system to apply the same time-stamp to
several entries that were published during the course of a single
day.â However I've always looked at my updates as something with date
precision. The time I upload the entry to the server isn't relevant to
me, just which date I did it. My timestamps thus reflect that - they
only mention the day (and indeed use Ruby's Date class which is Date
precision).


My initial thought was to leave them at Date precision, picking
	an arbitrary 00:00Z for the time part to satisfy RFC 3339. The atom
	spec said 'should' rather than 'shall', which
is an important distinction in [StandardsSpeak](https://martinfowler.com/bliki/StandardsSpeak.html) and
feedvalidator marked two entries with the same time-stamp as a warning
rather than an error. Unless I could understand a downstream problem,
I didn't see why I should put in the work to handle second-precision updates
rather than date-precision.


[Sam Ruby](http://www.intertwingly.net/blog/2007/01/01/Date-Precision) provided a compelling scenario. Some people, including
	him, aggregate multiple feeds and read them by starting at the
	latest and reading back till they read something they read
	earlier. My entries would usually be inserted earlier in the time
	log than they were supposed to and wouldn't get read. (I could give
	them an arbitrary late time part which would keep them at the top of
	the list, but that would just irritate the reader.)


So I decided to use second precision. I needed to replace the
	Date objects I was using to handle timestamps with Ruby's Time
	objects. I also now need to start putting full times in posts, which
	from this entry onwards I will do.


I downloaded a copy of feedvalidator to test my feeds out as I
	gradually filled them out. It was easy although I grimaced at
	actually having to install raw as opposed to just using apt-get - I
	guess I'm getting soft.


As a final aside story. A year or two ago a Very Large Software
	Company (one that makes software I'm sure you're familiar with)
	asked me if I minded having my feed aggregated into an architecture
	feed they were producing. My response, as it usually is, was âfine,
	that's what feeds are forâ. A month or two later I got an email
	saying they couldn't use my feed and I needed to change it to RSS
	2.0. It was more effort than I fancied, so I declined. But I
	couldn't help chuckle that this big organization, which had clearly set
	up a full blown project to do this work, couldn't do what Ade does
	for us in his spare time.
