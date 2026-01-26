---
title: "Evaluating Ruby"
description: "In my recent post onEvaluatingRubyI mentioned that a colleague 	had put together a web app with some fancy numerical graphs. Someone 	emailed to ask how he did that. I added my short answer, ploticus,"
date: 2006-06-19T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/bliki/EvaluatingRuby.html
slug: EvaluatingRuby
word_count: 789
---


If you're reading this I assume you're aware of the fact that
	there's been a huge amount of fuss about the Ruby programming
	language, and in particular the Rails framework for developing web
	applications. Some see it as the future of programming, others as a
	dangerous diversion.


I started with ruby several years ago. The [pragmatics](http://www.pragmaticprogrammer.com/) got me
	interested and it soon became my preferred scripting language. Over
	time it grew to handle much of the production of this website - in
	particular this bliki. I like the language a lot.


There's a jump between my personal liking and whether it's
something that should be used by our clients. We can evaluate its
suitability for client projects based on its features - and this leads
to many arguments about the pros and cons of dynamic typing, convention
over configuration, processes versus threads, and the like. Such
discussions are useful but I remain wary of them. Too many things are
hard to judge that way - hence we spend so much of our time on client
projects being slowed down by technology that sounded good on a golf
course. My preference is to make this judgment based on experience - 
find people who have a track record for delivering in the mainstream
environments and who have tried using Ruby.


Some of this can be seen with public writers. Ruby has attracted
	many people who have good experience elsewhere but feel Ruby gives
	them an additional edge, names like the [both](http://www.toolshed.com/blog) the [Prags](http://pragprog.com/pragdave), [Justin Gehtland](http://blogs.relevancellc.com/),
	[Bruce Tate](http://weblogs.java.net/blog/batate/) et al should be enough to make Ruby worth
	looking at. But parochial as I may be I've been keeping my ear
	closest to ThoughtWorkers: people whose history I know and whose
	projects I can more easily check up on.


It's still early days yet, but I now have a handful of project
	experiences to draw on. So far the results are firmly in favor of
	Ruby. When I ask the question âdo you think you're significantly
	more productive in Ruby rather than Java/C#â, each time I've got a
	strong 'yes'. This is enough for me to start saying that for a suitable
	project, you should give Ruby a spin. Which, of course, only leaves
	open the small question of what counts as 'suitable'.


One thing to mention is that although we have a couple of what I
	might call typical web projects that fit in well with what's
	currently talked about as prime Rails territory, there are also
	elements that are different.

- A kiosk device where
	consumers are directly manipulating a touch screen. Rails is present
	here, as the UI is a very Ajaxian web front end. But there's also
	communication with hardware devices, crypto, odd networking stuff -
	all on an appliance like Linux box.
- A lot of SQL
	manipulation in batch processes where Ruby is used to specify what's
	needed and the resulting Ruby expressions are converted to SQL to
	carry out the real work. There's a splash of Rails on the front end
	- but again it's not the typical Rails app.
- A project that looks like a standard web app in many ways, but
		involves a great deal of munging data from different formats and
		some very fancy graphs and charts (using [Ploticus](http://ploticus.sourceforge.net/)).


In all these cases, those involved said they are getting
	functionality, and value, faster out of the door than they had in
	other platforms. This suggests to me that if you're looking for
	delivery speed and productivity you should take a serious look at Ruby.


There are still some open questions. In particular it's still too
	early to see what happens in later enhancement stages, particularly
	when you get team changes. Some people think that the dynamic nature
	of Ruby and the lack of tools will be a problem, others that the
	simplicity that Ruby encourages will make up for the
	difference. Such is the nature of the question that we can't really
	tell yet - I'll update you when I find out more.


Cedric Beust [argues effectively](http://www.beust.com/weblog/archives/000382.html) that even if Ruby is a superior
platform it may not become mainstream. I certainly understand that argument,
like many an ex-smalltalker I've long known of more productive
platforms than the current mainstream enterprise choices. If it's
important to you that you are only using mainstream platforms, you'll
need to wait longer to see what happens. There are plenty of course,
who [don't care about following the mainstream](http://www.loudthinking.com/arc/000584.html).


There's also plenty of projects where development productivity is
	swamped by political and other communication factors. Here Ruby's
	advantage would be significantly attenuated.


But overall these experiences, from trusted colleagues mean I'm
increasingly positive about using Ruby for serious work where speed,
responsiveness, and productivity are important.
