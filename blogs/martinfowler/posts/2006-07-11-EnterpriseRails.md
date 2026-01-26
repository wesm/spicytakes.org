---
title: "Enterprise Rails"
description: "In the newly formed Rails community, the word 'enterprise' is 	becoming a dirty word. For many people the Rails framework, with its 	aggressive simplicity, is the antithesis of over-complex'enterprise"
date: 2006-07-11T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/bliki/EnterpriseRails.html
slug: EnterpriseRails
word_count: 973
---


In the newly formed Rails community, the word 'enterprise' is
	becoming a dirty word. For many people the Rails framework, with its
	aggressive simplicity, is the antithesis of over-complex
	['enterprisey'](http://patricklogan.blogspot.com/2006/03/its-enterprisey.html) frameworks.


At the recent [RailsConf](http://www.railsconf.org/),
	[PragDave](http://blogs.pragprog.com/cgi-bin/pragdave.cgi)'s
	opening [keynote](http://blog.scribestudio.com/articles/2006/06/30/railsconf-2006-keynote-series-dave-thomas) highlighted a
	bunch of unsolved issues with Rails, several of which involved
	dealing with some of these enterprisey concerns. An example of this
	was his call for support of more
	varied database structures, such as having compound primary keys.


[DHH](http://www.loudthinking.com/)'s response to this could not have been a more emphatic
	refusal. With a clever visual manipulation of his recent wired
	cover, DHH projected himself as the [Neo](http://imdb.com/title/tt0133093/) of the software world,
	forcefully proclaiming himself to be in a better place, and telling
	the enterprise world that they need to join him, not the other way
	around. Applying this principle to compound keys, the reaction is
	âno wayâ. Rails will do what it does, and will not complicate itself
	to support things it doesn't like.


Here is a solid example of what makes Rails âopinionated
	softwareâ. In the Rails mindset, life is much simpler if you keep
	your tables isomorphic to your objects, and give your tables
	surrogate, integer, primary keys. If you play the Rails way - life
	is easy; if not - use something else.


I confess I like this opinionated attitude. Perhaps it reflects my
	Unix background, which thrives on many tools that do one thing well,
	rather than a complex tool that tries to do many different things. I
	like Rails's focus, its determination to pick a certain class of
	application and serve that well.


In this sense I see a startling parallel between DHH and Kent
	Beck. For either of them, if you present them with a constrained
	world, they'll look at constraints we take for granted,
	consider them to be unessential, and create a world without them. I
	don't have that quality, I tend to try to work within the
	constraints gradually pushing at them, while they just stick some
	intellectual dynamite under them and move on. That's why they can
	create things like Extreme Programming and Rails which really give
	the industry a jolt.


Lying under PragDave's talk was a deeper concern. Like me he's
	spent much of this life working with people who can't apply the
	dynamite. When you need data from a database that's run by a data
	management group and has run for a decade with compound keys, you
	can't just don a pair of cool sunglasses and blow the constraint
	away. One answer to this is to âchange your organization or change
	your organizationâ, but to those who can't should they be utterly
	abandoned by Ruby?


The last word of the last paragraph is the key to the
	answer. Rails is right, I think, to ignore the enterprisey world,
	but that doesn't mean that Ruby should. One of the great strengths
	of scripting languages, like Ruby, is their
	[post-modern](https://martinfowler.com/bliki/PostModernProgramming.html) delight in diving into the muck of a chaotic software
	ecosystem. Ruby is a great place for other frameworks to fill the
	gaps left behind by Rails's opinions.


My colleague Badri gave a talk, that was sadly not very well
attended, about one of these - rBatis. rBatis is a ruby port of the
popular Java framework [iBatis](http://ibatis.apache.org)
(led by Clinton Begin, another colleague). The port is being done by
yet a third colleague [Jon
Tirsén](http://jutopia.tirsen.com/). rBatis is still a work in progress but already it
shows the same elements that made iBatis popular - fearlessly
embracing the strength of SQL rather than just trying to hide it under
layer of Query Objects. It also strengthens its appeal by making the
most of Ruby - stealing many functions from Active Record (such as
validation), and using
convenient Ruby syntax rather than XML. (Is XML the hunchback of
programming languages?) rBatis could be the answer to complicated
database issues, still fitting into a Rails web-app, but introducing a
different set of trade-offs. If you're comfortable with SQL, rBatis
looks pretty damn simple. (BTW any Rubyists out there Sydney? We may
need you to kidnap Jon's surfboard if work slows down on rBatis.)


All this tilts our perspective. Enterprise Rails may well be
	an oxymoron, but Enterprise Ruby is anything but. Indeed as I look at
	the way the enterprise world is going - a greater use of messaging,
	autonomous services featuring [ApplicationDatabase](https://martinfowler.com/bliki/ApplicationDatabase.html)s, a
	post-modern acceptance of variety - [the glue that doesn't set](http://blogs.pragprog.com/cgi-bin/pragdave.cgi/Tech/UnsetGlue.html) seems
	to be the ideal tool.


Although some people felt these talks implied that there was a rift appearing between the
Davids, further conversation suggests to me any rift is founded
on misunderstanding (now there's a mangled metaphor). PragDave's call
wasn't for Rails to support these things but for the wider community
to find a way. Similarly DHH's response was about the Rails core team;
which hardly limits other peoples' efforts - as rBatis demonstrates.
Furthermore DHH felt that most of PragDave's calls were consistent
with the Core. The notion of a narrow core rails and a wider
ruby world (including rails) supports both concerns - this is the
strength of composing small tools.


However this wide-ruby / narrow-rails view of the world has a
	catch. I joked during my keynote that RailsConf was a sign of a
	failure of Rails - since if it was truly successful Rails would be
	too simple to need a conference. The underlying truth, however, is
	that Rails has become the keyword for Web apps (even Enterprise
	apps) in Ruby. I suspect we'll see more enterprisey people at
	RailsConf than at [RubyConf](http://www.rubyconf.com/), because Rails has got the
	attention. The consequence of this is that there's a danger that
	people will hear the opinionated nature of Rails as
	a statement about Ruby, and thus give the impression that Ruby isn't
	a suitable enterprise glue. That would be a shame.
