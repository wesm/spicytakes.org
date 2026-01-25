---
title: "Blog Or Get Off The Pot"
date: 2006-03-15
url: https://steve-yegge.blogspot.com/2006/03/blog-or-get-off-pot.html
word_count: 2570
---

I hate blogs.
It's not that I
hate
them, really; I just don't like the "diary" format.  It doesn't suit my needs very well.
However, I have this day job, you know, just like you probably do.  And that takes up most of my time.  If there's any time left, I'd like to spend some amount of it actually blogging, as opposed to dicking around endlessly with software and configuration just to enable me to blog the way I want to.  If I'm going to dick around with coding stuff, I'd rather do something other than that.
But I hate blogs.  The format's not right.  Chronological ordering of my posts just plain sucks.  It forces you to dig around through monthly archives, wondering if there's anything good in all the crap I spew out.
What I want is closer to my own personal Reddit, or Digg, or something like that (but not quite like them, either).  I don't want you to come to my site and see what I've posted most recently.  RSS can take care of that.  I want you to see what other people have voted as my best entries.  On
my
site.  You shouldn't have to go to Reddit to get a decent directory of my blog.  Anyway, you can't; anything that makes it onto Digg or Reddit or del.icio.us is mixed in with everything else, and gets bumped down into oblivion by stuff that's newer and/or better.
Blog entries should be organized by popularity, not time.  Or ideally, you can pick either one.  Why the hell don't blogs do that?
But it's got to be even better than that.  Having a self-organizing browse interface like Digg's on my blog page would be nice, but I want more.
For instance, I want inline comments.  Putting everyone's comments at the end is pretty lame.  Even worse, most blog packages these days don't even seem to have Slashdot-style threaded commenting.  Instead, the comments are ordered chronologically, just like the entries.  So the comment threads are invisible, and commenters have to say stuff like "um, actually I was replying to Dave, not Peter", and quote each other heavily -- a whole subculture of commenter hacks, just to fake threading.
Why the hell don't blogs have threaded comments?  Sure, sure, some do.  But that's still not enough.  Not by a long shot.  They need threaded comments
and
inline comments.
What do I mean by inline comments?  I want people to point at a particular sentence I wrote, get all excited or pissed off about it, and say "I want to comment on THIS!  This point right here!"  So when you're reading, you should get to that part, and see a little icon or link that takes you off to a comment thread on that particularly interesting or disputed section.
In other words, the commentary on a blog entry should grow
outward
, not
downward.
And I want versions.  I want to make changes to my entries sometimes -- heck, frequently.  But that's culturally weird, and feels dishonest to me, because I've sort-of permanently overwritten the old version.  I think people have a right to see how my ideas changed over time, after they yelled at me or made brilliant observations or whatever.  So people should be able to see the revision history for individual posts.
It's starting to sound slightly Wiki-like, isn't it?  Yeah, a little.  But what I want doesn't exist today.  It's not a blog, and it's not a wiki, but it's similar to both of them.  I want an essay-publishing system, basically.
All that revision-history stuff complicates the commenting, of course; each comment has to keep metadata about which blog revision it was talking about.  It's even more complicated if you have versioned comments, so users can go back and fix their typos or change their minds.  But it's not like that stuff's impossible, is it?  Aren't there companies whose full-time efforts are going into making cool blog software?
Blogs have evolved into the dominant form of self-publishing, and yet nobody's doing it right.  To me, that can only mean one of two things, both depressing.  Either nobody's been clever enough to figure out an interface that actually works for people who aren't just posting their daily cat picture, or web programming is so insanely hard that nobody's been able to get features out fast enough to keep pace with the ideas.
It's probably a little of both.  But my God, if they're hurting for ideas, all they need to do is ask.  They're bursting from me; I can't keep them in anymore.
Want some?  OK.  Here's one:  I'm sick of global configuration options.  Global config options are so 1970s.  When I go into Firefox, I want to be able to override every single configuration option on a per-page basis, or even better, with url pattern-matching rules.  Doesn't that seem just patently obvious?  And yet there aren't any browsers that let you do that.  (Or are there?  You tell me.  Wouldn't it be nice if you could put an inline comment
right here
letting me and all the readers know?)
Same goes for my blog software:  I want per-post configuration.  It seems like I should be able to specify different stylesheet templates for each entry if I want — at least for different categories.  Technical posts should have a different stylesheet from the posts about my last vacation.
And I should be able to change the settings for how I'm notified about comments on a per-post basis, because I'll care more about some of them than others.
Isn't all this stuff
obvious
?  How can people not think of this stuff?
Oh, and not to put too fine a point on it, but how about a decent content-editing tool?  Blog software packages can't seem to get this simple thing right.  You pretty much get simple "convert line breaks" behavior, or you can embed HTML tags and screw with them for
hours
until you figure out how to make the blog HTML renderer behave the way the
exact same tags
work in every other page in your browser.  If you're lucky.  Sometimes it's just impossible, and you have to live with their screwed-up interpretation of the spacing before/after an ordered list or a heading element or whatever.
Can it really be that hard to get this stuff right?  O'Reilly's group blogs don't even put a frigging blank line after a heading element, so your first sentence is smooshed right up under the heading.
I'm not asking for WYSIWIG here; I realize that's almost impossible given the amazingly crappy mix of browser technology standards we have to work with today.  All I'm asking for is something halfway decent, like you get from any Wiki worth its salt.  RedCloth would be my personal preference, but gosh, just about any wiki-style markup language would be preferable to the current choices ("convert line breaks" or "embed HTML tags that don't work properly") that most blog systems give you.
So I've been meaning to set up a public blog for nearly a year, and I haven't done it because all the blog-hosting options are just so wrong.  I've been struggling with this whole issue -- not having the right self-publishing software -- and wondering whether to try writing it myself, or to just bite the bullet and live with the crap that's out there today.
**Giving it the Ole College Try**
How would I approach writing it myself?  Well, I'd probably use Ruby on Rails.  I don't think it's the end of the evolutionary road for web programming, not even close, but damn if it isn't so much farging better than the alternatives.  I plan to blog about my vision for web programming of the future at some point.  I think you'll like it.  But for now, we've got Rails.
With Ruby on Rails, you can actually think about writing your own blog software.  That level of grandiose ambition (and it
is
grandiose if you have as little free time as I do) enters the realm of plausibility.  Until recently, it just wasn't a feasible part-time effort, because, let's face it, Web Programming is a Big Crap Sandwich, and we all have to take a bite of it.  But Rails makes the idea at least conceivable.
So the other day, I poked at it a little.  I set up a Rails server with Apache and SCGI, and then immediately thought -- HMMMMmmmmm, if Rails is so cool, then maybe someone's already written a blog software package in Rails.  I could set that up, and since it's Rails, and I'm familiar with it, I could start evolving the software in the directions I want it to go.
Well, it's true.  There is one.  It's called Typo.  But I have no idea if it's cool or not, because you can't install it.  I mean, you
can
, but not in the amount of time I'm willing to allot to the effort.  There's almost no documentation, and what docs exist are all completely outdated, because apparently most software developers still don't understand that nobody will use their shyte if they don't document it.  The Typo folks are far from the only ones guilty of this.
And as if the Typo doc situation weren't bad enough, Rails doesn't have a model yet for hosting multiple applications in the same Rails codebase.  You have to manage them as separate code trees, and handle all the routing in your webserver.  Which is pretty lame, if you think about it, because Rails has a really cool routing-rules minilanguage, so why the hell can't you use it for your routing?  So I have to keep Typo and any other Rails apps I want to run in their own little jail cells, with Apache as the illiterate prison guard who can't understand complex instructions I want to give it.
Dammit, what's a person to do?
I wonder how software engineers set their priorities, sometimes.  Are the Rails folks even thinking about the multiple-app installation problem?
And look at MovableType, which still evidently doesn't have threaded comments, but they support group blogs.  But what good is a group blog?  They're just weird.  I haven't seen one that works well.  Maybe there are a few out there.  But what percentage of
all
blogs do they really constitute?  It doesn't seem like it was the most important feature to add.
I'm just speculating, though, since I haven't looked at MT in a long time.  I'm not a big fan of Perl anymore, and I'd rather throw my weight behind software written in languages I at least like a little bit.
And yeah, I'm sure you'll all want to tell me to please try your blogging software cuz its k00l.  But I can't frigging install them all, only to find they suck as bad as Typo did.  I've installed MovableType before, and it took at least half a day of tedious labor.  I'm sure YOURS will also be a day of work.  Forget it; there's no point in wasting precious days evaluating your probably-broken software and digging around your probably-missing documentation.  There are plenty of hosts out there, and after looking at Typo, I decided to use one.
Supporting languages I like is partly why I picked Blogger; it's got a mix of Java and Python folks working on it, or so I've heard, and I think Java and Python are a darn sight better than Perl.  Python, especially.  It's a good language.  Also picked Blogger because I have some friends that work there.  And I hear it's going to get better at some point in the future.  And "Blogger" is a cool name.  So I'm willing to live with its inadequacies for now.
So I'm going to start blogging.  It was blog, or get off the pot.  Posting static HTML pages was ridiculous.  (But hey, I honestly didn't think anyone was going to read them.  It didn't really become a problem worth thinking about until late December.)
**What will I blog about?**
I have a lot of stuff to say.  For one thing, I've realized that I have more ideas than time.  Way more.  It's not even close.  I've been hoarding ideas for several years now, hoping I'd find time to get around to implementing (or documenting, or publishing, or whatevering) them someday.  But it's not going to happen.  Software and documentation both take time to write.  Lots of time.  If I come up with ten ideas that take 5 years each, I'm pretty screwed.
I did a 5-year idea once.  I had an
[idea for a game](http://www.cabochon.com)
in 1993.  I knew
exactly
what game I wanted to play.  I could envision it and even describe it in great detail.  It was a fusion of all my favorite games to date:  Nethack, Darker Realms LP Mud, Ultima IV, and Crossfire.  A multi-player, tile-based, graphical MUD.  I knew it would be a wonderful game, and yet nobody was writing it, or even discussing it.  After a year or so, I realized nobody was thinking about it like I was.  But I wanted to play the thing, so I decided to buckle down and write it myself.  I figured it'd take me about 18 months.  I mean, it's a tiles game; how hard could it really be?  So I started working on a design in 1996, and started coding in 1997.
18 months, what a joke of an estimate.  The game was pretty much "done" the way I'd originally envisioned it after about 5 years.  I spent another 2 years pushing it to new levels; after actually having it online, new ideas started really coming in, both from me and from the players.  After a total of 7 years, I threw in the towel, because my productivity had slowed to a crawl, all because of Java.  God, I wish I'd picked Python.  Or Common Lisp, or
*something*
that supports dynamic development.  But in 1996, Java had great marketing, so that's what I picked.  Thanks, Sun!  You screwed me!
Half the game's written in Jython now; it simply isn't possible to do an extensible game like that in Java.  You either write your own minilanguage or you use a JVM language; those are your only choices.  People are adding code to the game right now, as we speak, and they're changing it on the fly.  They can't go rebooting the f***ing server with a hundred players online every time they want to make a change.  Java just doesn't work for that kind of application.  Nor does C++.  So all online games use dynamic extension languages.  No exceptions.
Five years, that's how long that little idea took.  Plus 2 years of adding bells and whistles.  And that, folks, is why I'm giving in and using a blog host.  Because I have lots of ideas, lots of things to say and to explore, but only a few dozen years left at best.  I can't afford to go chasing every 5-year idea that springs to mind.  After due consideration of the crap web frameworks and crap blog packages out there, I decided that I don't want to spend my next 5 years implementing my vision for a decent self-publishing system.  Someone else can do it.
But those static HTML pages had to go.  I had to blog or cut bait.
So here we go.  I'm blogging now.  I hope you'll like it!