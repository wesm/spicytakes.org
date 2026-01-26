---
title: "Ruby Microsoft"
description: "AtRailsConf2007there was a lot of excitement over JRuby. This small   team had taken a moribund project and turned it into what looks like   a first class implementation of the Ruby platform on the JV"
date: 2007-05-30T00:00:00
tags: ["ruby"]
url: https://martinfowler.com/bliki/RubyMicrosoft.html
slug: RubyMicrosoft
word_count: 1631
---


At [RailsConf2007](https://martinfowler.com/bliki/RailsConf2007.html) there was a lot of excitement over JRuby. This small
  team had taken a moribund project and turned it into what looks like
  a first class implementation of the Ruby platform on the JVM. They
  got a lot of cheers and deserved them all.


So with JRuby pretty much here, the spotlight moves onto the other
	common managed code runtime - .NET. Microsoft's intentions for Ruby
	are currently much less clear. They have announced Ruby as a
	language for scripting Silverlight - but that still leaves a lot of
	open questions. Is this a full implementation of the ruby language,
	or is some form of Ruby++ - an enhanced subset of Ruby?


JRuby serves two distinct but complementary purposes. On the one
  hand it's a powerful scripting language for the JVM, allowing you to
  weave a dynamic language into a Java application. It's second
  purpose is an implementation of the Ruby platform in the JVM, which
  allows a Ruby application, in particular a Ruby on Rails
  application, to run on the JVM just as well as it runs on the MRI
  (Matz's Ruby Interpreter, the current C runtime).


The big question for Microsoft's âIron Rubyâ is how compatible will it be? Will
it be a full implementation on the CLR? All the signals I hear tell me
that John Lam, the main force behind Iron Ruby, is determined to get a
fully compatible implementation. However this may be very difficult to
do as things stand. Soon-to-be-ThoughtWorker Ola Bini, a JRuby
committer,  reckons that it's almost impossible to figure out how to
implement a Ruby runtime without looking at source code of the MRI - but
Microsoft imposes drastic limitations on its employees' ability to
download open source software, let alone look at the source. The
open-source community does much of its communication through source
code - so this makes collaboration with an open-source community very
difficult.


Overshadowing this, of course, is Microsoft's historically difficult
	relationship with the open source world. In the past Microsoft has
	gone out of its way to vilify and threaten the open source
	community. In recent years things have improved, but there's a real
	question about Microsoft's core intentions. The recent patent
	threats are seen by many as proof that Microsoft is still intent on
	fighting open source to the death.


Unlike most other technology companies, Microsoft has struggled
to find a way to co-exist with the open source world. It is harder for
Microsoft - unlike Sun, Apple, or IBM they are overwhelmingly a
software company. Open source projects like Linux, GNU, and Open
Office are directly competing with Microsoft's crown jewels. However
I've never felt that declaring war on open-source, trying to stamp it
out, was a viable long-term solution. Open-source is here to stay, the
question is how to accommodate  it.


With Ruby Microsoft is in a different position to the more
visible death match. Ruby doesn't compete with the core revenue
generators in Microsoft's line up.  What's more there is a real desire
in the Ruby community to co-operate with Microsoft. Most people I
talked to at RailsConf were very keen to see a full
range of support for Ruby on Microsoft - and there were a lot of
creative ideas floating around on how we could try to come with an
approach that could make it work. The overwhelming sense I heard in
the community was not âRuby will kill evil Microsoftâ but âhow can we
overcome the problems to get Ruby on Microsoft.â


As Chris Sells pointed out, we do have to consider the question
âwhat's in this for Microsoftâ. I see a couple of reasons. First off
is the role of .NET and Windows in the data center. If Microsoft
doesn't support the Ruby platform, it runs the risk of people moving
away from .NET (and Windows) on server farms if Ruby on Rails becomes
successful.


Another reason is people. Microsoft doesn't like to acknowledge
this in public, but there is a real concern that
[AlphaGeek](https://martinfowler.com/bliki/AlphaGeek.html)s are [moving away](http://www.hanselman.com/blog/IsMicrosoftLosingTheAlphaGeeks.aspx) from the Microsoft platform.
There's a growing sense that Microsoft's vision is armies of Morts in
command-and-control organizations. There often seems to be outright
discouragement of tools to enable talented enterprise developers, or
of agile development processes.


A few years ago my (limited) contacts in Redmond told me that
	they were seeing a real drift of technical leaders away from
	the Windows platform. More recently these signs seem to be increasing. Reading
	the 'softie part of my blogroll I got a sense of real disillusionment
	amongst people who have been long-time Microsoft
	supporters. Agile-oriented developers have been frustrated with the
	direction of Microsoft tools. Microsoft conferences barely
	mentioning agile processes, leaning much more to waterfall
	approaches. The tools, with their rigid role-separations, actively
	discourage the blurry boundaries that agilists prefer.


At RailsConf, Tim Bray contended that the key decisions on
	technology are made by the programming community. I partly agree
	with this. The reason we have so much bloatware in IT is because IT
	purchasing decisions are usually made on golf courses by people who
	have lost meaningful contact with the realities of software
	development. However golf-course decisions may dominate the
	short-term, but as time rolls on I think Tim's contention is
	true. So losing the alpha geeks may not matter this year or next, but will
	inexorably harm Microsoft over time.


Indeed it's already past next year for Microsoft. We've seen a
noticeable drop-off in interest from our clients for Microsoft
projects, particularly in the US. In Australia, .NET hasn't got any
foothold at all amongst our clients. I'm not sure what to make of this
data. We aren't so big to be a statistically valid sample on our own.
But it's a useful data point nonetheless particularly since we like to
think our clients are the âalpha IT shopsâ.


Perhaps more significant is the story within Thoughtworks. When
.NET appeared there was a lot of interest in the platform. Many people
were pleased to see a strong competitor to the Java platform and were
keen to get involved on .NET projects. Yet over the last year or so
there's been a big turn away from .NET. This is despite the fact that
there is some really interesting things coming out of Redmond. Mike
Two is very keen on the windows workflow tools, I've been very
impressed by Linq and other language developments. But the general
view of Microsoft technologies is a loud yawn. This is important
because, as Tim O'Reilly believes, the alpha geeks point to what
everyone else will be doing in a few years time. And the crucial point
is that the attitude to Microsoft isn't hatred (a common attitude
amongst many geeks) but boredom. This is what Paul Graham means when
he says that [Microsoft is dead](http://www.paulgraham.com/microsoft.html) because it's no longer dangerous.


The attitude to open-source is a large part of this problem. When
Java appeared there were yawning gaps in its portfolio, and worse some
dreadful standard tools in its API (visions of Entity Beans spring to mind).
Those gaps and bad ideas were fixed by the open-source community. Ant
gave us a build tool, EJB was displaced by Spring and Hibernate. .NET
has also got its gaps, and again the open source community has stepped
up to fill them. Yet Microsoft refuses to collaborate with these
efforts, even seems to go out of its way to undermine them. I was
particularly sickened by Microsoft's reaction to [NUnit](http://nunit.com) - an excellent
XUnit testing tool, elements of whose design were lauded by Anders
Hejlsberg at OOPSLA. Microsoft ended not just bringing out a
competitive library, but deliberately making it incompatible. That's
not the kind of reaction that encourages people to invest their time
in the platform.


To be fair, that debacle was a couple of years ago. Actions like
	hiring Jim Hugunin and John Lam have helped counter that
	impression. Technologists like Chris Sells, Don Box, and Jim Newkirk
	are working to make Microsoft are a more open environment. But like
	any large organization, Microsoft is full of contradictory forces
	and we don't know which ones will prevail.


My colleague John Kordyback pointed out that at the heart of all
this is realizing that Ruby is not Yet Another .NET Language but a
whole community and attitude to software development. Ruby is a
community where open source, agile thinking, and lightweight solutions
are deeply ingrained values. He says a common problem in Redmond is
that âThey ask me 'Why is this language important' rather than 'Why is
this *thinking* important?'â


So what I see for Ruby and Microsoft is an opportunity. The Ruby
community seems eager to work with Microsoft. This provides an
opportunity for Redmond to figure out how to deal with the problems of
working with open source and for this effort to serve as an exemplar
for future collaboration. A first class implementation of the full
Ruby platform on .NET would be a wonderful product of this
collaboration. Perhaps an even better result would be for this work to
serve as  an example of how Microsoft can collaborate with a community
that's centered on openness and agility; an example that can be a
springboard for further spreading of attitudes that can further help
programmers and their customers throughout the Microsoft world.


There's been quite a few reactions to this (see [Technorati](http://technorati.com/search/http://martinfowler.com/bliki/RubyMicrosoft.html) for a
  full list). Particularly worth reading are the ones from: [Sam
  Gentile](http://codebetter.com/blogs/sam.gentile/archive/2007/05/31/microsoft-at-the-crossroads.aspx), 
[Cory Foy](http://www.cornetdesign.com/2007/05/martin-fowler-on-ruby-at-microsoft.html), [Luke Melia](http://www.lukemelia.com/blog/archives/2007/05/30/microsoft-ruby-open-source/), [Jeremy Miller](http://codebetter.com/blogs/jeremy.miller/archive/2007/06/01/maybe-it-s-just-not-that-bad-to-be-a-microsoft-developer.aspx), [Rockford Lhotka](http://www.lhotka.net/weblog/ALackOfEnthusiasmInTheMicrosoftWorld.aspx), [John Lam](http://www.iunknown.com/2007/05/microsoft_and_i.html), 
[Evan
Hoff](http://evanhoff.com/archive/2007/06/02/18.aspx), 
[Karl Seguin](http://codebetter.com/blogs/karlseguin/archive/2007/06/02/jeremy-s-right-being-a-microsoft-developer-isn-t-that-bad.aspx),  
[Ola Bini](http://ola-bini.blogspot.com/2007/06/there-can-be-only-one-tale-about-ruby.html), 
[Miro Adamy](http://thinkwrap.wordpress.com/2007/06/03/martin-fowlers-article-on-ruby-and-microsoft/), 
[Charles Nutter](http://headius.blogspot.com/2007/06/response-to-olas-ironruby-post.html), 
[Peter Laudati](http://blogs.msdn.com/peterlau/archive/2007/06/11/shaking-out-the-innovation.aspx), 
[Nick Malik](http://blogs.msdn.com/nickmalik/archive/2007/06/12/martin-fowler-wants-to-see-ruby-on-microsoft-to-save-the-alpha-geek.aspx)


**Update:** Recently (august 2007) we've seen some very encourging signs coming out
  of Redmond. In particular, [IronRuby](http://www.iunknown.com/2007/07/a-first-look-at.html) will be hosted on RubyForge with
  what looks like a very permissive licence - Ola [approves](http://ola-bini.blogspot.com/2007/07/ironruby-scoop.html).
