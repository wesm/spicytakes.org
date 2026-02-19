---
title: "Interview: Brent Simmons"
date: 2003-03-28
url: https://daringfireball.net/2003/03/interview_brent_simmons
slug: interview_brent_simmons
word_count: 8953
---


Brent Simmons is the author of [NetNewsWire](http://ranchero.com/netnewswire/), the runaway smash-hit RSS news
aggregator for Mac OS X, and the founder of [Ranchero Software](http://ranchero.com/), which he runs in partnership with his wife, [Sheila](http://sheila.inessential.com/). Brent’s personal weblog is [inessential.com](http://inessential.com/).


I interviewed Brent via email, and our extensive discussion covered a wide range of topics, including: Apple’s treatment of small Mac developers; deciding which features would separate the Pro and Lite versions of NetNewsWire; Brent’s previous experience working for [UserLand Software](http://www.userland.com/); and much more.


---


John Gruber: RSS syndication has been around for several years. But its popularity
	has skyrocketed in the last year. One could definitely make the case
	that NetNewsWire has played a significant role in the RSS explosion,
	but I also think it’s the case that NetNewsWire Lite debuted in the
	right place at the right time.


Prior to NetNewsWire, I had always seen RSS syndication as a
	technology that was mostly useful for publisher-to-publisher
	communication. Like the way that Slashdot uses RSS feed to populate
	their “Slashboxes” on their customizable homepage. When did you
	begin thinking about creating a personal RSS aggregator?


Brent Simmons: I’m not sure when I began thinking about a personal aggregator. The 
idea came up several times and disappeared several times. I was working 
at UserLand, and we had a server-based aggregator (My.UserLand.Com) — 
and then we developed Radio UserLand’s news aggregator, one of the 
first personal aggregators.


But even before we started working on Radio’s aggregator I had seen 
Chuck Shotton’s Gossip, which was a sort of personal aggregator. I 
don’t recall if it used RSS or not: it may have done screen-scraping 
only. Gossip was different from Radio (though browser-based) and 
different from NetNewsWire.


As a science fiction reader since I was a kid I always knew that 
“personal newspapers” were coming. That’s an old science fiction 
prediction. I didn’t know what they’d look like — and they’re still in 
the early stages — but they’re here now. So I always thought of RSS 
syndication as publisher-to-reader rather than publisher-to-publisher.


Gruber: How much was NetNewsWire based on what *you* wanted in an
	aggregator, and how much was what you thought the public would want?


Simmons: The basic layout — the three-paned thing, like Mailsmith or Outlook — 
that’s what I wanted. I wanted a nice-looking OS X desktop app.


I hoped that the public would want it too, and I was utterly pleased 
when the first people who saw it liked it a lot.


But then lots of features have come from what people ask for. For 
instance, the idea of having groups and of having a feed that shows all 
new items — that comes from users. My original vision was just a flat 
list of sites.


Gruber: One problem you faced when NetNewsWire debuted is that most Mac
	users had never seen or used a news aggregator. It’s really a new
	class of application, and one which I think is hard to explain the
	need for without actually using it for a few days. Were you worried
	at the outset that NetNewsWire wouldn’t take off?


Simmons: Yes — but not *too* worried, because if it didn’t take off there are 
always plenty of other ideas.


Some of the things that helped (I think) were that it took really no 
configuration to get started. Just launch it and you have some news. 
And the Sites Drawer made it easy to start customizing your feed list.


But the biggest thing was probably just that the interface is so 
familiar — millions of people have used this interface before with 
email or Usenet. So while the concept of a news aggregator may be new 
to lots of people, the app doesn’t feel (I hope) like some radical 
departure into the far reaches of geek space.


Another thing was doing the tag line: “More news, less junk. Faster.” 
That came to me with almost no effort.


Now, maybe nobody reads the tag line — but if they do, they understand 
the claim that this software helps you keep track of more news with 
less work in less time. A simple, clear statement of benefits.


I don’t really know if that has anything to do with NetNewsWire’s 
success so far or not. I like to think so.


Gruber: I agree. In fact, I think the entire Ranchero web site is just
	terrific. It is everything a developer’s web site should be, and
	nothing more. They say you shouldn’t judge a book by its cover, but
	I generally find there’s a high correlation between the design of a
	developer’s web site and the design of their software. Not
	necessarily the *quality* of their software, but the design. Most
	web sites are over-designed. So is most software.


Simmons: Thanks!


Gruber: What are your goals for the Ranchero.com web site?


Simmons: Lots of different little things. It could be a bit more attractive, 
perhaps — but I’m not a graphics guy, so that part isn’t easy.


I’d like for pages like the NetNewsWire home page to be a bit less
cluttered. There’s too much stuff there, and it will only get worse 
unless I do something about it.


Gruber: I think that speaks volumes about your sensibilities, since the NetNewsWire
	home page is already a lot less cluttered than most web pages.


Simmons: I’d like to have more resources for other developers. I have a couple 
tutorials and some open source classes (for parsing RSS and OPML), and 
I’d like to do more of that. If I have some success with NetNewsWire and 
make money, it’s good karma to be as generous as I can, not just with 
people who use my software but with other developers. As a developer 
I’ve always appreciated when other developers do that, so I try to do 
it too. So, whenever I can make time I plan to add more tutorials and 
open source Cocoa code and things like that. Well, even if there’s no 
real karma at work at least it makes me feel good and it’s fun to do.


And then there are some little things like making the bug tracking 
system easier to use (and probably making it available via RSS).


The main thing is to just keep reducing clutter, making it easy to use 
and easy to read, and making sure there’s good stuff there — news, 
software, tutorials, sample code, docs, and so on.


Gruber: NetNewsWire only supports RSS; it doesn’t do screen-scraping. Have you 
	considered adding screen-scraping capabilities to NetNewsWire?


Simmons: What I might do is support screen-scraping indirectly. One feature 
request has been to allow feeds that are actually local scripts — Perl 
scripts or AppleScript scripts or whatever — and those scripts would 
then be run instead of being read. Whatever the script returns should 
be a valid RSS feed.


This way anybody could write a script that scrapes VersionTracker (for 
instance) — and then you could share that script with other people if 
you wanted to.


Gruber: That’s an interesting solution. I think it’s a good thing that NetNewsWire
	only reads RSS feeds — that makes it easier to understand the
	scope of what it does.


Simmons: Exactly. One of my philosophies is that any piece of software should be 
describable in a sentence. Photoshop is a graphics editor. Nisus Writer 
is a word processor. NetNewsWire Lite is an RSS reader. NetNewsWire Pro 
is an RSS reader and weblog editor.


There are several reasons I don’t want to do screen-scraping myself:

1. Screen-scraping is prone to breakage. All the scraped site has to do 
is change its format and the screen-scrapers stop working. I’d check 
my email in the morning to find a hundred emails telling me that 
NetNewsWire has a bug because site X (a hypothetical scraped site) 
doesn’t work anymore.
2. I want sites to use RSS rather than just say, “Hey, people are 
scraping us, that’s fine, we don’t need to do anything.”
3. I don’t want to get into trouble with sites that *don’t* like being 
scraped. If you provide RSS, then that means you don’t mind if people 
read your sites with an RSS reader. If you don’t provide RSS, I can’t 
assume that you’d consent to having your site be scraped.


In fact, with just a very few exceptions, there aren’t even any RSS 
feeds in the Sites Drawer that are generated by scrapers.


Gruber: Plus, it shows that if you want to have any control at all over
	your site’s RSS feed, you need to produce it yourself. Because
	if you don’t, someone else is going to scrape it, and you won’t
	have any control over it. It’s getting very close to the point
	where RSS feeds are not optional.


Simmons: RSS feeds are not optional — I’ll think I’ll personally go to every 
web developer’s house, knock on their door, and tell them that RSS 
feeds are not optional.


Gruber: NetNewsWire seems to have arrived at the right place at the right
	time. Prior to the past year, RSS feed were, for the most part,
	only available from commercial web publications. However, with the
	explosion of blogging software and personal weblogs, RSS is now
	easily available to personal publishers. In fact, my guess is that
	NetNewsWire users are tracking way more personal RSS feeds than
	they are commercial ones. Did you foresee this when you started
	work on NetNewsWire?


Simmons: I always figured that personal weblogs would way outnumber any other 
type of RSS source. I worked on Manila when I was at UserLand, and we 
added automatic RSS generation early on, and lots of Manila users were 
publishing personal weblogs. And then when UserLand did Radio’s 
aggregator it was clear that personal weblogs outnumbered other sources 
by a large majority.


It’s cool by me, by the way — I’m totally glad to see the huge number 
of personal sites. I wish everybody in the world had a weblog or two. 
(And that they all were available via RSS.)


Gruber: How did you decide on NetNewsWire’s regular price — $39.95?


Simmons: Part of me thinks the price is too high, and part of me thinks it’s too 
low, so maybe it’s right. Deciding on a price is harder than 
programming or doing user interface or tech support or anything else. 
It’s tough. It’s tough partly because I just want to give it away, and 
partly because I want to keep feeding my cat.


Gruber: Far be it for me to tell you what to do. But I think the price
	is very fair. I certainly wouldn’t go any lower.


There’s a large contingent of users who are going to gripe about any
	price that isn’t zero. Reading the user reviews at VersionTracker,
	I’ve noticed that unless software is free, there are *always*
	numerous posts advocating either a lower price, making it free, or
	recommending that everyone use some other application that is free
	(even though it might not be as well done).


These people are morons, and they can’t be pleased. You can put
	software users into two distinct groups: those who will consider
	paying for commercial software, and those who will *never* pay for
	software.


The first group, those who will consider buying software, are the
	only people commercial developers need to worry about. Like any
	widely-generalized grouping, there can be a large variation in the
	criteria these people use to decide what to buy. Some won’t hesitate
	to buy very expensive software from companies like Adobe,
	Macromedia, and Microsoft. Some won’t spring for $600 packages, but
	will happily buy lower-cost software (which usually comes from
	smaller independent developers). Maybe they don’t have a lot of
	money. Maybe they feel good about supporting small, privately-owned
	enterprises. But regardless, they’ll at least considering paying for
	good software.


But trying to appeal to the second group, those who will not buy
	software under any conditions, is a terrible idea. By definition,
	you can’t win — they’re not buying anything. The problem is that
	there are a lot of people who fall into this category, and many of
	them are quite vocal. They are also, often, quite dishonest. They
	will say things like “I’d pay $20 for this, but not $40. $40 is
	ridiculous.” But if you cut the price to $20, they will tell you it
	ought to be $10.


What many of these people do not want to admit, even to themselves,
	is that they are simply cheapskates.


Simmons: One of the things I read sometimes is that people who develop software 
are “greedy.” And I’ll probably read that, or something like that, 
about me. Even though I’ve put nearly a year of my life into 
NetNewsWire, and there’s a freeware version, and the price is only the 
cost of a couple pizzas and a pitcher of beer.


But I’m prepared for that. When I worked at UserLand there were always 
people griping about price, and I learned that it’s a fact of the 
software business, not something to take personally.


I also get feedback that the price is too low. People remind me to 
price the app what it’s worth, that the price sends a message about the 
quality.


Gruber: I see a lot of software that’s priced in the $10-20 range, and I
	think that’s almost always a bad idea. At least if the developer is
	trying to make a living selling the software (or even a significant
	part-time supplement). If you consider *every* potential user of
	your software, something like $15 might seem like a reasonable
	average for what they’re willing to pay. But if you only consider the
	aforementioned first group — discounting people who will never buy
	software — the threshold goes much higher.


I understand the appeal of *free* from the users’ perspective,
	because they don’t have to pay anything. I like free just as much as
	anyone. But I also want talented Mac developers to be financially
	successful, so that they can spend time doing what I want them to
	do: writing software.


I also think developers can address this issue by doing freeware
	“lite” versions of their software. I assume you agree.


Simmons: Yes, I agree about freeware lite versions. Totally.


I like free stuff too, by the way. But I’m a generous person — I like 
to give away as much as I can for free, and I don’t mind paying for 
software that I like, especially when it’s from a small developer. An 
example is [Mscape’s Iconographer](http://www.mscape.com/products/iconographer.html). I totally rely on it. It only cost 
$15. I would have gladly paid more for it.


Gruber: How did you draw the line between which features are only in the Pro
	version?


Simmons: The first obvious line to draw was that Lite is read-only and Pro is 
read/write. A simple, easy-to-understand distinction.


But the Pro version also includes some advanced reading features, such 
as the Find command and date display. In future versions there will be 
more such features added to the Pro version, including the “[Kottke 
view](http://www.kottke.org/02/08/020823possible_net.html)” — where titles and headlines are together in the same pane 
rather than separated into two panes.


Gruber: Did you ever consider putting a limit on the number of subscriptions
	you could have in the Lite version?


Simmons: For maybe one second. I hate limits like that. It’s one thing to not 
have an entire feature like the Weblog Editor, but quite another thing 
to arbitrarily limit the number of subscriptions. Doing that would, in my 
mind, make the Lite version no more than an advertisement for the Pro 
version.


Gruber: Did you set out from the beginning with the intention of creating a 
	commercial version of NetNewsWire? I assume so, since the free version 
	made its debut with the “Lite” suffix.


Simmons: Yes. It was the intention from the beginning, and that the main 
difference between the full and Lite versions would be that Lite is 
read only, while the full version is also a writing tool.


Gruber: You’ve stated that one of your models for the relationship between
	the freeware NetNewsWire Lite and the commercial NetNewsWire was
	BBEdit. Does Bare Bones’s recent decision to discontinue BBEdit
	Lite give you pause?


Simmons: For about a second — but then I read (I think on your site) something 
to the effect that after so many years, BBEdit is a very well-known 
piece of software. They don’t really need BBEdit Lite to get people to 
know about BBEdit.


I was pleased when I saw them continue to make BBEdit Lite available. I 
think that’s the right thing to do.


Gruber: There’s a tricky calculus involved when creating a freeware “lite”
	version of a commercial product. On the one hand, you want to the
	free version to be capable, useful, and popular, thus creating good
	will and increased popularity. But on the other hand, you don’t
	want the free version to be so good that it hurts sales of the
	commercial version. Now that NetNewsWire is shipping, how well do
	you think you’ve balanced the differences between NetNewsWire and
	NetNewsWire Lite? Would you do anything different with NetNewsWire
	Lite if you could start over again?


Simmons: I think I’ve done a good job on the differences between Lite and the 
full version. I was lucky in that much of it was obvious.


I can’t think of anything I should have done differently with
NetNewsWire Lite, no. The differences between the Lite and full
versions will grow over time, as I add new features to the full
version.


That’s not to say that the Lite version won’t ever get new features: it 
will. For instance, I’ve been thinking about adding Rendezvous support, 
and it’s likely the Lite and full versions both will include Rendezvous 
features.


Gruber: You have a lot of respect for your users — it shows both in your
	comments and in your software design. I think it’s a common
	misconception that well-designed human interfaces should be geared
	toward making things easy for idiots. I think the opposite is true
	— the best interfaces are those which make things easy for smart
	people.


Who do you have in mind as the target user when you’re designing
	software?


Simmons: I tend to think in specifics, I think of people I know and the kinds of 
things they might like. (I also think of myself, of course.) I know 
lots of smart people who love good user interface, who love the web, 
who love to read, who love to write. That describes me and it describes 
many thousands of people.


## Programming Background — Frontier


Gruber: When did you get started programming Macintosh software?


Simmons: Let’s go way back — I got my start programming Apple computers in 
1980, when my parents bought an Apple II Plus. Both my parents were 
programmers (my Mom still is), so I learned lessons like “goto 
considered harmful” at the dinner table.


Then later as a teenager I took a break from programming, until 
returning to programming in 1994 with my first Macintosh. At first I 
tried to learn AppleScript, and it gave me gas, and then I picked up 
Frontier — and I took to it like a bird to air.


Gruber: I think a lot of people today don’t realize that Frontier and
	AppleScript were, in many ways, direct competitors for quite a
	while. Frontier more or less started as an automation scripting
	language for the Mac. Then AppleScript appeared, and Frontier
	became an OSA language. And until Late Night Software’s JavaScript
	OSA implementation appeared about two years ago, Frontier was the
	only other OSA language I knew of.


Despite serving similar purposes on the surface, however, Frontier
	and AppleScript are very different beasts. The languages use very
	different styles of syntax; AppleScript attempts to be as much like
	written English as possible, whereas Frontier uses an
	object-oriented dot-notation.


What was the status of Frontier when you first started using it?


What are your thoughts on how Frontier has evolved, and its current
	status?


Simmons: I first started using Frontier shortly after the freeware “Aretha” 
release. This was Frontier 4.0b1, if I remember correctly. It was 
before the HTML framework and Manila. It did have a CGI Framework, 
which I fell in love with immediately. My main interest was in doing 
dynamic web sites on Mac-based servers (running MacHTTP/WebSTAR).


The CGI Framework was so nice and easy. Your scripts took one 
parameter, a table containing elements of the HTTP request, and 
returned HTML text. Piece of cake. Though I haven’t written a Frontier 
CGI in years, I could probably sit right down and do it without having 
to look up any docs. It’s burned into my brain.


I think UserLand was right to realize that competing with AppleScript 
as an automation language was just not going to happen. Never mind 
issues of merit (which are hard to quantify with such different 
systems) — but AppleScript came free with every Macintosh. If you 
write an AppleScript script you know you can distribute it without 
worrying that people have AppleScript, since everybody has AppleScript.


But, more than that, I think making Frontier a system for web 
publishing was and is the right move. Reason #1 is that web publishing 
is way more fun. And it turns out that Dave Winer was right back in 
1996 — that templates and scripts and so on are going to play major 
roles in the future of web site building. (He wasn’t the only person who 
thought that, of course. But not everyone who thought that developed 
software that did that.)


Gruber: I have to admit that I certainly didn’t agree with Dave then. My 
	problem, and I think it was shared by many others (and maybe still 
	is), is that when the web appeared I was already very experienced with 
	desktop computers and hierarchical file systems. I understood files 
	and folders, and I also easily taught myself HTML. Therefore, I saw a 
	web server as a disk full of folders and HTML files (and GIF images). 
	My unit of measure when creating a web site was the individual HTML 
	file.


It ends up this is a terrible way to make a web site — at least if 
	it’s a web site you plan to update regularly. When you’re managing all 
	your files by hand, it’s hard to update links. Not hard meaning 
	“difficult to understand”, but hard meaning “pain in the ass”. The 
	whole point of weblog software is that it takes away the 
	pain-in-the-ass part of updating a web site frequently.


Simmons: Even before the term “weblog” existed, people were building weblogs 
with Frontier. For instance, here’s NewsPage, which was published in 
January 1997:


`http://www.scripting.com/frontier/netScripting/newsPage.html`


Another bit of software archaeology: NewsCenter by Phil Suh was another 
weblogging tool built in Frontier before the term “weblog” existed:


`http://www.filsa.net/frontier/software/newsCenter/whatis.html`


And you could go back even farther and find AutoWeb and Clay Basket. 
They weren’t weblog tools exactly, but they were early web publishing 
tools. AutoWeb was billed as “The Newsroom System for the Worldwide 
Web.”


`http://scripting.com/autowebdocs/whatisautoweb_119.html`


`http://scripting.com/clay/`


Gruber: I remember Clay Basket, and I thought it was overkill, useless for
	someone who knew how to hand-code HTML. But now I understand — the
	basic unit of measure on the web isn’t the file, it’s the link.


Simmons: Right on.


Part of me thinks that Frontier could have used a super-nice GUI front 
end to its HTML framework. I haven’t used Fog Creek’s CityDesk, but I 
think something along those lines might have grabbed Frontier lots more 
users back in 1996-1997. But who knows? I’m just speculating.


Gruber: I agree. I think the lack of a comprehensive GUI front-end made the 
	barrier to entry a bit high. It meant you had to read something to get 
	started. Most people are only going to try something new if they can 
	double-click an app icon and poke around. If they like what they see, 
	they might read the documentation. But they won’t read before they get 
	started.


Simmons: Agreed.


## Apple and UserLand


Gruber: The AppleScript-vs.-Frontier thing reminds me that every few years
	the same theme recurs — that Apple hurts developers by including
	competing products in the Mac OS. Like Sherlock (vs. Watson), and
	now Safari. Or Mail, which may have crippled the market for
	commercial Mac email clients — a market that was once quite
	vibrant.


I’m not complaining, necessarily, because I don’t know what else
	Apple could have done. They need to bundle a free email client with
	the system, because people rightfully expect to be able to “do
	email” as soon as they get their computer hooked up.


I think Apple’s struck a very good balance with Safari, which
	although it competes with every other Mac web browser, is also going
	to result in a very nice HTML rendering library for all Mac
	developers to use. I think OmniWeb in particular may well do
	*better* if they adopt WebKit as their rendering engine.


As a small Mac-only developer, what are your thoughts? Do you worry
	that Apple is going to create an RSS aggregator now that NetNewsWire has
	become a hit?


Simmons: I agree — there are some things Apple *has* to do. One of the biggest 
complaints about OS X was the slow browsing experience. Safari totally 
changes that, and that’s going to help sell Macs.


And as a developer I want to be able to use the Safari renderer in 
NetNewsWire.


But then there are the weird cases: I don’t know that Sherlock had to 
happen the way it did. Watson is such a good product, why not just make 
a deal and bundle it? Or make a respectable offer to buy it?


Apple might make an RSS aggregator, I totally realize that. My hope is 
that they’ve learned from the Watson thing and either don’t do it or, 
if they really want an RSS aggregator, they make a deal with me.


But I think they won’t do an RSS aggregator any time soon for a couple 
reasons:

1. RSS readers are still a little geeky. Much less so than they used to 
be, but it will still be a while before they’re seen as a mass-market 
thing like browsers and email apps.
2. Though there are thousands of RSS feeds on the web, most of them are 
weblogs, and that’s just a little too anarchic even for Apple. (Or any 
largish company.) I can imagine Apple’s default subscription list as 
being only sites like Salon and so on. Would they even have a Sites 
Drawer (or equivalent) which lists hundreds of weblogs? (Some of which 
are critical of Apple or may contain offensive language or pictures.) I 
doubt it. Though I could totally be wrong. Apple has to think about 
John and Jane Doe, while I’m lucky, I get to write software for John 
and Jane Einstein. I get to take risks that big companies can’t.


My hope — and all one can do is hope — is that Apple realizes that lots 
of great software from outside Apple is crucial to the success of OS X. 
I think they do realize that, while at the same time they have to do 
things like Safari too. They have a balancing act to perform, and they 
slip sometimes: it’s hard to walk on that high-wire.


Gruber: What other kinds of programming have you done?


Simmons: I have experience with several different languages: C, C++, 
Objective-C, Java, Python, UserTalk, PHP, even a little HyperTalk. I 
still have trouble with AppleScript. (I like AppleScript, it’s just 
that my brain is wired in such a way that makes AppleScript very 
difficult.)


Gruber: I think AppleScript is the most successful unpopular language ever.


I used to feel exactly like you do, then it eventually started
	clicking. The big difference for me was when BBEdit 6 shipped. It
	adopted an object-model approach to scripting, as opposed to the
	more simple command-and-verb approach used in previous versions. It
	broke most of my existing scripts, but once I learned my way around
	the new object model, everything just started clicking, and I felt
	like I “got it”.


Simmons: Good! Maybe if I keep trying I’ll eventually get it too. I hope.


The biggest problem for me is that it seems like English, but it isn’t. 
There’s a dissonance there — like playing a C and D note together on 
the piano. I prefer my programming languages to be at least a minor 
third away from English: a fourth or fifth is even better. (And I think 
UserTalk, C, PHP, etc. are fifths.)


Gruber: I think that’s an accurate criticism. AppleScript is the world’s
	easiest-to-read programming language. (Assuming you can read
	English, I suppose.) I think this comes at the expense of being
	hard-to-write. It’s easy to open an existing AppleScript, figure out
	what it’s doing, and then slightly tweak it. But it’s hard to start
	from scratch and get all the syntax just right.


Let’s say, as opposed to Perl, which once you learn it is very easy
	to write. Once you get the hang of Perl, what you *think* will work
	probably does. But Perl is notorious for being difficult to read.


Simmons: I don’t use Perl myself — the very look of it has kept me from wanting 
to use it. I’m sure it’s every bit as cool as people who love it say it 
is. But I’m more likely to turn to Python, which fits me better.


Gruber: I assume you’ve done web development?


Simmons: I’ve done a lot of web development, most of it in Frontier, though my 
current web site is done with PHP and MySQL.


Gruber: So you’ve rolled your own weblogging system?


Simmons: Yes. It was the first thing I did once I started out on my own last 
year. Partly for the fun of learning a new language and database 
system, partly to expand my skill set, and partly because I wanted to 
run on Linux.


But also for political reasons. As a newly independent developer who 
planned at the time to make software for people who read and edit 
weblogs, I didn’t want to be seen as being particularly tied to any one 
weblog system or vendor.


Gruber: That’s interesting. I totally understand the desire to roll-your-own
	from a tinkerer’s perspective. I was tempted as well. (If I’d gone
	that route, however, I’d still be working on the system, and Daring
	Fireball wouldn’t yet exist. I’m a horrendously slow programmer.)
	But I hadn’t thought about the political position you’re in as the
	creator of NetNewsWire.


Have you considered releasing your weblog system to the public?


Simmons: I have considered releasing my system to the public. But I haven’t done 
so for a number of reasons:

1. It takes time to make it releasable, and I’m busy with NetNewsWire.
2. There are already lots of great systems. I don’t think my system has 
anything unique to add.
3. As a former UserLand employee, I felt a karmic obligation not to 
compete in the area of creating weblogs. (I don’t think I had a 
non-compete clause, but then again I didn’t look for it.) That’s what 
Radio and Manila do, that’s UserLand’s bread-and-butter.
4. It would mean that NetNewsWire would work best with my weblog 
system. Or at least people would see it that way. The way it is now 
there’s no favoritism, and that’s important to the product and people’s 
perception of the product.


Gruber: How and when did you get started working for UserLand?


Simmons: In early 1996 UserLand released MacBird, and I loved it. In some ways 
it was like a mini-Cocoa — you had an interface builder (the MacBird 
editor) and a place to write code (Frontier). I put up a web site about 
MacBird and became an active member of the Frontier community.


Soon after that I helped Dave with his 24 Hours of Democracy project, 
and then worked with him on a few other things, and some time later I 
was hired as a contractor to do things like ContentServer (this was 
probably early 1997). Later I was hired as a regular employee.


Gruber: What else did you do at UserLand?


Simmons: In my last year or two at UserLand I started working on the Frontier 
kernel — and that was totally fun. Much of what I did was just fixing 
little glitches here, particularly UI glitches in the outliner and so 
on, but I also did some things like kernelizing the OPML parser (based 
on Dave’s original scripts) and adding some new features like support 
for icons in the outliner.


Gruber: Did you only work on the Mac version of Frontier, or were you
	working on cross-platform code as well?


Simmons: I worked on the Windows version also. I wrote a fair amount of 
Windows-specific code, even. And I learned that I don’t really like 
developing for Windows very much.


I suspect that many Mac users are like me, that they’re driven in part 
by aesthetics. And they want to use software written by people who are 
driven by aesthetics. Windows is not aesthetic.


I think I’m off-topic...


Gruber: Not at all. I think the fact that you’re only writing Mac software
	is tremendously interesting. The conventional wisdom holds that
	commercial developers should concentrate on Windows, because the
	market is so much larger. And that Mac software should be an
	afterthought, and possibly ignored unless you think you can obtain a
	significant return on investment.


[Joel Spolsky wrote about this](http://www.joelonsoftware.com/news/20020910.html) on Joel On Software, effectively arguing that it seldom makes sense to develop Mac software.
[You responded](https://inessential.com/2002/09/19/why_i_develop_for_mac_os_x) with some great comments. You wrote:


> One of the reasons I develop for OS X is that, when it comes to
> 	    user interface, this is the big leagues, this is *the show*.
> 	    That’s probably what Joel would call an “emotional appeal” — and
> 	    to call it that, that’s fine by me.


Gruber: I think the biggest difference between the Windows and Mac software
	markets is that on Windows, features sell. The app with the most
	features usually wins. This has certainly been Microsoft’s strategy
	with regard to software design, and it’s ended up being the most
	profitable business strategy in the history of capitalism.


On the Mac, however, it’s design that counts most. The best-designed
	app usually wins. And I don’t mean “design” in the cosmetic sense
	(although that’s part of it). I mean intuitiveness, consistency, and
	usability.


I also think that the best Mac software is designed by the
	developers themselves. Whereas on Windows, a lot of commercial
	software is designed by “product managers”, and the programmers just
	write code. Is this part of the appeal of running your own company
	— that you get to do both the design and coding?


Simmons: Absolutely. I enjoy doing the design and the coding. And doing the 
web site and writing documentation and emailing with users.


I like pretty much all aspects except things like accounting and 
setting up the e-commerce system — but I’m lucky, Sheila is wonderful 
at that stuff. (She’s a major key to understanding Ranchero Software, 
even if she’s very behind the scenes.)


Gruber: When working on Frontier, did you mostly write UserTalk or C? I’ve
	always thought that must be one of the cool things about writing a
	programming system — eventually, you can start using your own
	language to write itself.


Simmons: For most of my time working at UserLand I wrote UserTalk. It was just 
the last year or two where I did a bunch of C programming.


If you look through the source code to Manila, you’ll see my initials 
(PBS) in lots of places. That’s one area where I wrote a bunch of 
UserTalk code. (The P stands for Peter.)


Gruber: I assume you’re writing most of NetNewsWire in Objective-C. How do you like
	it as a language? Do you miss UserTalk?


Simmons: I’ve grown to love Objective-C. It’s not as daunting as it looks — 
it’s actually quite simple. Kind of like Python with brackets.


I don’t miss UserTalk much, no. I spent six years or whatever writing 
mostly in UserTalk. That’s not to say UserTalk is bad — it’s cool — 
but just that I’m happy with what I’m doing now.


Gruber: Dave Winer is a giant among Mac developers. The damn kids of today
	might not recognize it, but [MORE](http://www.outliners.com/more31) is without question one of the
	biggest smash hits in Macintosh history. People still use it today,
	and it hasn’t been updated in, what, ten years? What was it like
	programming for him?


Simmons: Ten years sounds about right for MORE’s last update time. Let’s see — 
I actually have it on my hard drive. Get Info tells me that MORE 3.1 
was created Mon, Dec. 2, 1991. I’m not sure if there was a version after 
3.1.


MORE is also one of my favorite pieces of software, ever. I adore it. 
J’adore MORE. No other outliner has come close. (As a mini-homage to 
MORE, the outliner in NetNewsWire can be set to be somewhat MORE-like. 
You can use + and - instead of icons, and you can set it so a 
double-click expands and collapses. But the outliner in NetNewsWire has 
miles to go before it would ever come close to being as good as MORE.)


Programming for Dave was great. Dave has a reputation for being a bit 
prickly. But he’s a great teacher, and not so prickly as a boss as his 
reputation might lead you to think.


In some ways you could say I’m a graduate of UserLand University.


That’s not to say there weren’t days when I wanted to tell him to fuck 
off. That’s normal, with any boss.


A good teacher knows when to lead someone by the hand through learning 
something and knows when to tell them to dive in and just leave them 
alone. Dave’s good at this.


One of the best lessons I learned from working for Dave Winer was to be 
utterly ruthless about simplicity.


That may sound surprising to anyone who knows how complex Frontier and 
even Radio UserLand are under the hood. But if you think about these 
apps as mini-operating-systems, then you realize that a certain level 
of complexity is inevitable.


So here’s an example of how I learned to be ruthless about simplicity:


The first internal version of the create-a-Manila-site form had a dozen 
or so fields to fill out. It was easy for me to use the form, but 
that’s because I was working on Manila and I understood what all the 
fields meant.


When Dave first saw it he was surprised, I think, that creating a 
Manila site should be so complex. Or he was surprised at me for not 
making it simple.


Either way, he kept at me to keep making it simpler. And I did, piece 
by piece, until finally it’s the form you may be familiar with today, 
where it asks you for a site name, a theme, and your username and 
password.


That’s the kind of lesson I learned over and over, to keep hacking away 
at complexity until it’s not complex anymore. It’s hugely important, 
and it’s something not enough people understand the value of.


Gruber: And in the end, if you do a good job, the result is something that
	looks like it was easy to create, because it’s so simple. Far too many
	people equate “lots of interface” with “good interface”.


Simmons: If people say that NetNewsWire is small and lean, that means I’ve done 
my job well. The amount of source code that goes into it is probably 
larger than most people would think. And that’s fine.


## Design and Programming Philosophy


Gruber: I think you’ve taken an interesting approach to open source
	software. You’re using some, and you’re releasing some. But the NetNewsWire
	and NetNewsWire Lite applications are not open source. This is similar in
	spirit to what Apple is doing with Safari and KHTML. What open
	source components does NetNewsWire use?


Do you agree that open source and closed source software can
	happily coexist within the same projects?


Simmons: NetNewsWire credits a few open source components in its About window. 
SQLite, SQLDatabase (a Cocoa wrapper for SQLite), cURL, and CURLHandle 
(a Cocoa wrapper for cURL).


So I benefit from open source code, and I think it’s only right to pay 
something back by also releasing open source code and freeware 
versions. The generosity of so many developers is one of the things 
that makes me proud to be a developer. There aren’t that many fields 
where people are and have the means to be so generous.


I agree that open source and closed source can coexist within the same 
projects. NetNewsWire is an example of that. Mac OS X is sort of an 
example (even though it’s not one project) — there’s a lot of mix 
there, lots of open source, lots of commercial software. I think that’s 
a good thing, if for no other reason than diverse ecosystems tend to be 
healthier.


What I’d like to see is less zealotry from all corners. Open source is 
good, shareware is good, commercial software is good. It all comes down 
to good apps, using the right tool for the job. I prefer less ideology 
and more generosity. For me, Mac OS X is the only OS that seems to have 
in its DNA that spirit.


Gruber: I find it interesting that you’ve adopted a public beta policy for the
	development of NetNewsWire. Why? And how well do you think it’s
	worked, compared to a more traditional closed beta?


Simmons: The early beta program — *alpha* program, actually — was closed 
because it’s simply not fair to inflict such unfinished software on 
lots of people. The people who did help with those early versions have 
my thanks.


I opened the beta program as early as I possibly could. For several 
reasons:

1. It’s way more fun than the closed approach. I like connecting with 
people, and I like that they can connect with me. That’s the fun part 
of doing software. (Robb Beal once said to me that it’s like crack. It 
is.)


One of my software philosophies is that I don’t want users in the sense 
of John and Jane Doe — I want people whose names I know, whose 
web sites I know, who come up with good ideas, who care about software 
and the web and other people.


One of the fun parts about doing NetNewsWire is that I can put all 
these people’s weblogs in the Sites Drawer. I like that links to 
people’s web sites are actually in the product. (In fact, often I think 
this is the best part of NetNewsWire.)
2. The public beta for NetNewsWire Lite worked so well. NetNewsWire 
Lite owes a great deal to the people who reported bugs and had good 
ideas about how it should work. Had the beta program been closed I 
would have gotten only a fraction of those bug reports and good ideas, 
and it would have shown in the software.
3. Since Ranchero Software is just me and my wife Sheila, it’s not like 
we have a group of testers right here to use. We have to do software 
development in public. Which is totally cool by me. Even if we had a 
choice I’d still do it this way, as open as possible.


Bottom line: a closed beta means the software isn’t as good as it could 
and should be. At least in my case. (That may not be true for big 
companies like Adobe, of course — but I strongly recommend this 
approach for smaller developers.)


Gruber: The counter argument would go something like this:

1. Beta software is by definition buggy. Anyone trying your
	    software while it is in beta is going to get their first
	    impression based on its current state.
2. Most public beta testers aren’t going to submit valuable
	    feedback. They just want free software.
3. If there is a serious bug, innocent people could suffer. Like
	    with the bug in the first release of Safari that could result in
	    people’s home directories getting erased.


I can’t think of any other commercial software that I use which was
	developed using a public beta test. But I suspect we’ll be seeing
	more of it.


Simmons: Good arguments. My counter-counter-arguments may not apply to everyone.

1. I have great faith in my beta-testers. The tag line for the Ranchero 
Software site is “News and software for smart people. Mostly Mac.” — 
and I think I’m lucky enough that my software attracts smart people.


Beta-testers also get an impression of the development process and of 
the developer. How responsive is the developer? Is he open about 
things? Does he fix bugs and implement feature requests? These days I 
think this stuff is very important, because when people buy software 
they don’t just evaluate the software itself, they think about the 
source.
2. Again, maybe I’m lucky, but I get tons of great bug reports and 
feature requests. A good number of the reports come from people who I 
know from my UserLand days — they’ve done beta testing on UserLand 
products I’ve worked on, so I know them and they know me and they’re 
great testers.
3. One of the things I do is be extremely careful about things like 
writing to disk. First I look at the code and wonder if there’s any 
chance it could go haywire. Step through the code looking for potential 
pitfalls. Step through it again. Then I test and test. Look at it 
again. And then I make sure any potentially harmful code is fully 
burned in on my machine before beta testers ever see it. For instance, 
the feature in NetNewsWire Pro where feeds are cached on disk — that 
feature ran on my machines for a few months before any beta tester ever 
saw it. (It was done before the Lite version even shipped, it just 
wasn’t enabled except for my test builds.)


And should a serious bug like that appear despite my best efforts 
(which can happen even to Apple), I’ll make sure it’s known about and 
fixed as soon as is humanly possible. Not days, but hours or even 
minutes is preferable. (Of course, step one would be to alert people. 
Right away.)


Gruber: I think this is the key to your success with public betas. You
	respond quickly, both with information on your web site, and with
	new builds. There is always a sense of forward development momentum.


I also think the web itself, along with the pervasiveness of the
	Internet, are key to public betas. The traditional closed-beta model
	was in place long before the Internet was commonplace. A public beta
	like yours — with frequent new builds and information for your
	testers — wouldn’t have been possible 10 years ago.


That’s why I think public betas are going to become more common
	going forward.


Simmons: D’accord. For me personally the biggest thing is that it’s more fun.


Gruber: Cocoa is, by all accounts, a terrific application framework. But
	it’s not magic, and it’s quite large. So it took a while for
	existing Mac developers to ship applications built using Cocoa.


Now, two years after Mac OS X first shipped, there are a lot of very
	interesting new applications being written in Cocoa.


How does Cocoa, along with Project Builder and Interface Builder,
	compare to what you were used to?


What would you like to see improve in the future?


Simmons: My previous application work was with CodeWarrior and ResEdit. And most 
of that was working on Frontier and Radio UserLand. The interfaces in 
those apps are almost entirely code-built. With Cocoa you have Interface 
Builder, which allows you to set up interfaces in advance.


I didn’t think I’d care about that — I don’t mind doing interfaces in 
code — but it turns out be a huge advantage. There’s so much you get 
for free: toolbars, split views, table and outline views, and so on. 
That makes development faster and it means I have less code to 
maintain. For a small developer it makes sense to use the 
system-provided stuff as much as possible.


I find myself not really thinking much about what I’d like to see 
improved in Cocoa. I think it may be because I’m too busy.


I want WebKit. WebKit WebKit WebKit. I want to be able to use Safari’s 
renderer in NetNewsWire.


Gruber: What are you guys doing for e-commerce?


Simmons: [Kagi](http://www.kagi.com/). We’ve sent them a list of pre-calculated serial numbers, so when 
you buy NetNewsWire you get your serial number right away. Which is as it 
should be.


Gruber: Is Sheila working with you full-time now?


Simmons: Yes. To my delight. And to the betterment of the business and the 
software.


Gruber: I suspect you’re frequently asked if you plan to port NetNewsWire to
	Windows. How do you respond to such requests?


Simmons: The most frequent person to ask about a Windows port is my Mom. (She’s 
a systems architect and, ugh, a Windows user.)


I tell people that if they pay me a ton of money up front I’ll do it.


Gruber: How are you handling technical support for Ranchero? How much time
	does it consume?


Simmons: So far I’m handling technical support just via email. I expect Sheila 
will help with it before long. And sometimes users help other users via 
the mailing list, and I totally appreciate that.


One of my goals in software development is to minimize the amount of 
technical support needed. NetNewsWire is designed to not really require 
much support.


I also try to make sure the docs cover things. Half the time I answer a 
question just by pointing to the FAQ page.


I spend just a few minutes a day handling technical support. Not much: 
half an hour would be a busy technical support day. If that increases, 
it’s probably because I’m selling a lot of software, and I’d be able to 
hire someone to help.


Gruber: The nature of NetNewsWire puts you in a unique position. In addition to
	being the developer of the application, you also get to decide which
	RSS feeds are in the default subscription list.


This might not be such a big deal in a few years, when RSS aggregators
	are commonplace and everyone will already have a long list of feeds
	they subscribe to. But now, while RSS aggregation is still fairly new,
	I suspect that being in the default list is a big deal and can
	generate a lot of traffic for a site — sort of like being in the
	bookmarks menu back when Mosaic and Netscape introduced web browsing.
	You added Daring Fireball to the default subscription list when
	NetNewsWire 1.0 shipped, and I saw a noticable increase in traffic.


How seriously do you take this responsibility? What kind of mix do
	you hope to achieve in the default subscription list?


Simmons: I take this responsibility very seriously.


The prime directive is “do no harm.” In earlier versions I just put 
sites in there that I liked without thinking of the extra bandwidth 
costs they may incur. So now before adding a personal or small-business 
site I ask if the extra bandwidth use will be okay.


I try for a mix of personal and commercial sites and for a mix of 
interests, leaning toward Mac sites. (Since the one thing everyone who 
uses NetNewsWire has in common is that they’re using a Mac.)


Gruber: How often do people ask to be put in the default list? What do you
	tell them?


Simmons: I get about an email a week. Most of the time I reply that it’s set for 
the next release, or that I don’t think it’s a good fit, or whatever.


Gruber: Have you considered selling placement in the default list?


Simmons: I’ve considered it. The FAQ even says that it’s possible. A couple 
people have asked about the cost, and I tell them it’s something like 
$2000/month.


In other words, I don’t really want to sell placement in the default 
list.


Why not?

1. Because it reflects my editorial judgment, and I like that.
2. Paid defaults would have to be marked as such, and that means I’d 
have to add something to the UI, and that would make it more complex, 
and I don’t really want to do that.


Gruber: The Sites drawer lists a ton of feeds. How many are there? What are
	your criteria for adding a feed to the sites list?


Simmons: I don’t know how many feeds are in the Sites Drawer. Around 500, I 
think.


My criteria are basic: would somebody somewhere maybe be interested in 
this? The answer is Yes 99% of the time.


I also do a sanity-check, make sure the feed isn’t incredibly, 
way-over-the-top offensive in some way. (That hasn’t happened yet, and 
I don’t expect it to, but I suppose it’s possible. I’m a free speech 
zealot, so the feed would have to include child pornography or 
something like that before I’d reject it on these grounds.)


Gruber: How many feeds do you subscribe to?


Simmons: 127 at the moment. It keeps growing. There’s so much good stuff to read.


Gruber: What’s next for Ranchero? A new project, or more refinements to 
	NetNewsWire?


Simmons: NetNewsWire. There are bugs to fix, for starters, and I’ve received 
tons of great feature requests. The 1.0 release is barely the beginning.


Of course, I do have ideas for other projects... but no definite plans. 
NetNewsWire is the focus.



| **Previous:** | [The Party’s Over](https://daringfireball.net/2003/03/the_partys_over) |
| **Next:** | [Get What You Pay For](https://daringfireball.net/2003/04/get_what_you_pay_for) |


PreviousNext