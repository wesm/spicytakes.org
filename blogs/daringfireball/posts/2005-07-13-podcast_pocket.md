---
title: "Is That a Podcast in Your Pocket?"
date: 2005-07-13
url: https://daringfireball.net/2005/07/podcast_pocket
slug: podcast_pocket
word_count: 3027
---


There are a couple of intriguing aspects to Apple’s recent foray into
podcasting with iTunes 4.9. First and foremost is the degree to which
they’re promoting it. Podcasting is *the* new feature in iTunes 4.9 — it’s pretty much the entire point of the release. The Podcasts icon
scored the second-to-top position in the iTunes source list, and it’s
getting a huge amount of play on Apple.com and a top spot in the
iTunes Music Store.


[**Quick primer, which will seem quaint to many of you:** Podcasting
is the use of RSS for the aggregation of audio content, generally
intended for synching with iPods and other portable music players. The
RSS feed for a particular podcast contains a list of (usually) recent
episodes, with the associated audio file as an “enclosure”. Unlike
email enclosures, however, the enclosures in an RSS feed are not
embedded in the message itself; rather, they refer to the enclosures
by URL for subsequent downloading. This means you can publish a
podcast RSS feed listing 10 recent episodes, each of which may be
several megabytes, but the RSS feed itself is just a few *kilo*bytes
of XML-formatted text. It is up to your podcasting software to
determine when and why it will download the enclosures.]


Podcasting is still very, very new. As in like still dripping-wet new.
Compare and contrast with the use of RSS for aggregating regular
(written) web content — RSS had been out for a few years and was
relatively mature by the time Apple added support for it to Safari.
Whereas podcasting really only hit the nerdosphere about a year ago,
and yet here is iTunes 4.9, already taking it to the mainstream.


On the whole, I think it’s a sign that Apple can still be rather
nimble — this strikes me as about as quickly as something new can be
adopted and embraced by a company of Apple’s size.


There are several signs, in fact, that Apple’s podcasting features
were rushed to market:

- During the first week, there were rampant problems with feeds
hosted by Apple at the ITMS. E.g. the RSS feed for [The Al Franken
Show](http://sundancechannel.com/al/), which was (and remains) one of the three most-popular
subscriptions amongst all iTunes users, was utterly broken. I
tried subscribing and re-subscribing repeatedly, each time only to
have iTunes complain that the feed contained no enclosed items. No
wonder: I looked at the feed’s RSS source and each of the
enclosure items looked like this:
`<enclosure url="" length="" type=""/>
`
(The value of the `url` attribute is supposed to be, you know, a
URL.) The workaround was simply to subscribe to Franken’s feed
directly from [his show’s web site](http://sundancechannel.com/al/), bypassing the ITMS
entirely. I.e. the original feed, hosted at sundancechannel.com,
worked fine; but the cached feed hosted by Apple at — and I swear
I’m not making this domain name up — ax.phobos.apple.com.edgesuite.net was hosed.
This has since been fixed, but the problem persisted for days. And
remember, Franken’s is currently the second-most popular feed listed
at the ITMS (first is Apple’s New Music Tuesdays podcast).
- You can’t turn off the Podcast item in the iTunes source list. This
strikes me as simply an oversight, since you can turn off all the
other optional features in the source list, such as Party Shuffle,
Radio, and even the Music Store. In the same way the Store panel in
iTunes’s preferences window has a “Show iTunes Music Store” checkbox,
there ought to be a “Show Podcasts” checkbox in the Podcasts panel.
- Even the iPod firmware updates seem rushed. The updates add a new
top-level Podcasts menu (which, unlike in iTunes, is optional) and
allow iPods to treat podcasts much like they do audiobooks, in
that when you resume playing a podcast, it goes back to where you
were, rather than starting over at the beginning of the track.
But, [Apple has confirmed](http://docs.info.apple.com/article2.html?artnum=301910) that the firmware updates for
clickwheel models breaks an existing feature: the ability for
Smart Playlists to update dynamically. E.g. if you have a playlist
for all “five-star” songs, it used to update dynamically when you
changed the star ratings for songs on your iPod; after installing
iPod Updater 2005-06-26, however, Smart Playlists only update when
you sync with iTunes. Oops.
The Knowledge Base article concludes:

This document will be updated as more information
becomes available.

Which was translated into plain English in [MDJ](http://www.macjournals.com/mdj/) 2005.07.09 as
“current Cupertino-speak for ‘We know it’s a bug and it’s not
fixed yet.’”


## A Rose by Any Other Name


All of which is not to say I’m complaining. Or at least I’m not saying
Apple shouldn’t have released its podcasting 1-2-3 punch when it did.
And let’s be clear: anyone who deems unacceptable any of the
aforementioned problems (or other problems) is implicitly stating that
Apple shouldn’t have yet released its podcasting support.


You can’t say that Apple should have released it when they did, but
without the bugs and shortcomings, unless you’re of the (mistaken)
opinion that Apple’s engineers were just sloppy, lazy, and/or
incompetent. [Real artists ship](http://folklore.org/StoryView.py?project=Macintosh&story=Real_Artists_Ship.txt), and one of the main tricks to
shipping software is knowing when to say, “This is good enough.”
Recognizing what qualifies as “good enough” is art, not science.
(Although a good QA process with lots of regression testing certainly
helps.)


The process of releasing a single major software update is hard
enough; but Apple’s podcasting support required simultaneous,
coordinated updates to the whole troika: iPod, iTunes, and ITMS.


On the whole, shortcomings notwithstanding, I think Apple’s podcasting
support was clearly good enough to ship. Shipping sooner than later,
even with more bugs, has instantly made Apple the undisputed leader of
podcasting. The whole problem that most other desktop podcasting apps
attempt to solve is getting audio files from RSS feeds into iTunes,
for synching with iPods. All of a sudden, iTunes 4.9 has turned an
entire class of software into an unnecessary middleman. (Podcasting
support in dedicated RSS aggregators like NetNewsWire still seems like
an important feature to me — many RSS feeds only contain occasional
podcast enclosures. iTunes is really only intended for use with RSS
feeds in which every item represents a podcast episode.)


And consider poor [Odeo](http://www.odeo.com/), a startup (co-founded by Blogger
co-founder Evan Williams) based solely on podcasting. It’s downright
amazing that Odeo — the first serious podcasting startup — was
beaten to market by Apple. It’s not because Odeo moved slowly; it’s
because Apple moved fast.


Apple’s podcasting support is effectively a loss-leader: iTunes is
free, and podcast downloads from the ITMS are free. So how does Apple
expect to recoup their engineering and hosting costs? Where they’ve
been making money hand-over-fist all along: iPod sales. I seriously
doubt very many people will be buying iPods *just* because of
podcasting, but every little reason to jump on the iPod bandwagon can
help. The trend line on the iPod sales graph is still sloping up,
steeply, and the main point to take away from Apple’s serious embrace
of podcasting is that they are not about to get cocky with regard to
features.


A large part of Apple’s interest in podcasting is that they’ve never
shied away from promoting the use of iPods for the consumption of
content that you don’t have to pay for. Or in the case of ripping
music from your CDs, consuming music that you’ve already paid for.
Despite all the hubbub about the imminent [500 millionth download from
the ITMS](http://www.apple.com/itunes/500million/), a big part of the appeal of Apple’s music platform is
that they in no way shove the ITMS down your throat. (E.g. as stated
previously, you can turn off the Music Store source list item in
iTunes.)


Apple has flipped the old Gillette maxim — they’re making money
selling the razors (iPods), not the blades. There’s definitely a huge
potential upside — big, big bucks — if the ITMS continues growing at
the current rate for a few more years. And it’s hard to imagine that
anything even remotely resembling any of the current iPods will still
be a high-profit-margin product 10 years from now. But at the moment,
Apple’s music revenue and profits are coming from multi-hundred-dollar
iPods, not 99-cent songs.


The other bit of good fortune is the name: podcasting. Good fortune
for Apple, at least. Clearly the “pod” in “podcasting” is about the
iPod. Apple couldn’t have come up with a better name for this
phenomenon if they’d gotten to choose it themselves. If the whole
“audio enclosures via RSS” scene were still known as “audioblogging”,
as it was when Maciej Ceglowski recorded his seminal “[Audioblogging
Manifesto](http://www.idlewords.com/2004/08/an_audioblogging_manifesto.htm)”,1 I seriously
wonder whether Apple would have done this now.


If you’re an engineer, you might be tempted to argue that
RSS-with-enclosures by any other name is still just
RSS-with-enclosures, and that it makes no technical difference whether
you call it “podcasting” or “audioblogging” or “noodlepants”.


But names do matter. And what makes this so delicious for Apple is
that the more popular “podcasting” becomes as the name for publishing
audio via RSS, the less likely it will be that a new name will ever
take hold. Which leaves Apple’s competitors — including Microsoft,
Sony, and the various other gadget-makers producing Windows Media-based
players — in the extremely uncomfortable position of choosing from
the following courses of action:

1. Embracing the word “podcasting”, even though it contains the
name of the competitor they’re chasing, and which name subtly
implies that podcasting is meant for use with iPods, which
implication sort of further implies that every other digital
music player is just an iPod knock-off. I mean, can you imagine
Apple using a term like “walkmancasting”, “dellcasting”, or
“wincasting”? It’s embarrassing.
2. Devising and using a new term for “podcasting” that doesn’t use
“pod”. Good luck with that, considering that everyone — *everyone* — who is publishing podcasts is already calling them
“podcasts”. [**Update:** According to [this story](http://seattlepi.nwsource.com/business/231986_theinsider11.html) in the Seattle
Post-Intelligencer, Microsoft employees are pushing “blogcasting”
as a “pod”-free alternative. Good luck with that.]
3. Ignoring the whole podcasting phenomenon.


There are no other options. The best-case scenario for Apple’s
competitors is for this whole podcasting thing to turn out to be
nothing more than a fad. That makes #3 a reasonable course of action.
But if it isn’t a fad, they’ve got to choose between #1 and #2, both
of which are marketing nightmares. And these guys are all already in a
deep hole, marketing-wise, versus Apple and iPod.


Hence Apple’s impatience to get their podcasting support out and in
use. If podcasting continues to grow and turns into something big, the
simple fact that the name includes “pod” is a significant and
permanent advantage in Apple’s favor.


## Creation Tools


One other complaint about Apple’s foray into podcasting is that their
entire effort is focused on podcast consumption — finding,
subscribing, and listening to podcast episodes — but they’re offering
only meager tools to help with podcast *production*.


They do have a tutorial for [creating podcasts with QuickTime Pro](http://www.apple.com/quicktime/tutorials/podcasting.html), but that pretty much boils down to “click the record button and
do your podcast in one continuous take, then save it”. Even if you’re
only vaguely serious about production quality, you’re going to need
some sort of editing tool.


They also have a tutorial for [using GarageBand for podcast recording](http://www.apple.com/support/garageband/podcasts/). This sounds better than using QuickTime Player, since GarageBand
allows you to layer separate tracks, splice, and edit. But GarageBand
is in many ways overkill, or at least overcomplicated, for recording a
podcast. It’s meant for creating your own music, not for recording
spoken-word content. (It doesn’t even work with the iSight microphone.)


What’s needed, I think — and I suspect this thought has occurred to
various indie Mac developers — is something along the lines of
Macromedia’s old SoundEdit / SoundEdit 16 (which was [discontinued](http://www.macromedia.com/software/sound/) a few years ago). A sound editor with waveform-based editing,
good recording controls, and output options geared toward minimizing
file size. The *coup de grâce* would be a nice human interface for
adding chapters and artwork. Apple’s only tool for this now is the
[command-line Chapter Tool](http://homepage.mac.com/applepodcast/podcasts/Resources/static/podcast_chapter_tool_beta.dmg) — better than nothing, but a far cry
from the sort of creative software tools that Apple and the Mac are
known for.


[**Update:** Several readers recommended [Amadeus II](http://www.hairersoft.com/Amadeus.html), a $30 app
from HairerSoft, which seems to provide many of the above features. A
few others mentioned [Felt Tip Sound Studio](http://www.felttip.com/products/soundstudio/), which costs $40.
Neither offers anything related to chapter tools, but they do provide
waveform-based splicing and fading.]


The question facing indie developers considering making such a tool,
of course, is whether Apple itself will be adding podcast recording
and editing features to iTunes itself. (I think if Apple does offer a
recording tool, it will be part of iTunes, not a separate app — bloat
be damned — because they’d want it to work for Windows users, too,
because Apple might be tempted to steer podcasters toward publishing
AAC files instead of MP3s, because AAC won’t work on Windows
Media-based players.)


On the whole, however, I don’t think the current sparsity of
podcasting production software is much of a big deal. The vast
majority of people interested in podcasting only want to listen to
them, not create them. (And, unsurprisingly, most people are mostly
interested in podcasts from name-brand professional broadcasters.)


## RSS Standards


The lowest-level, nerdiest issues that have surfaced regarding Apple’s
foray into podcasting have pertained to RSS. To wit:

- Various RSS experts have complaints about the spec for Apple’s
RSS extensions, e.g. [Edd Dumbill](http://usefulinc.com/edd/blog/contents/2005/06/28-rss-apple-itunes/read). Others, such as [Dave
Winer](http://www.reallysimplesyndication.com/2005/06/28#a682), chided Apple for not having asked the RSS community
for feedback before releasing the software.
- When fetching feeds, iTunes has no support for bandwidth-saving
HTTP features like ETags, Last-Modified headers, or gzip
compression. Every other major RSS aggregator supports all of
these features; iTunes supports none. The result is that every
time iTunes checks a feed for updates, it downloads the entire RSS
feed, uncompressed, regardless if anything has changed.
When clients support ETags and/or Last-Modified headers, they can
essentially ask the server hosting the feed, “Hey, I’d like to
download this feed, but only if it has changed since the last time
I downloaded it.” It’s a tremendous bandwidth saver, and not a
hard feature to implement, programming-wise.
- iTunes’s RSS parser is weirdly inconsistent with regard to case
sensitivity (it’s case-insensitive in many places, but XML is a
case-sensitive technology), date formats, and a few other areas.
[Sam Ruby and Mark Pilgrim](http://intertwingly.net/blog/2005/07/05/Insensitive-iTunes) (posting in the comments on
Ruby’s site) have documented these issues wonderfully, including
specific test-cases.


The idea that Apple should have sought community approval for their
RSS extensions is a non-starter. To seek approval implies that if
issues were found, or consensus could not be reached quickly (and it
seems it wouldn’t have), that Apple would have delayed the release of
their podcasting support until those issues were resolved. That wasn’t
going to happen; Apple’s podcasting support was going to be released
when Apple deemed it ready, and no later. Seeking community approval
beforehand but then ignoring it would have been worse than not having
sought it in the first place.


The RSS-parsing and standards-adherence issues raised by Ruby and
Pilgrim may seem like a bunch of niggles to the untrained eye. *Who
cares if their XML parser treats “Podcast” the same as “PodCast”?* But
the accuracy and strictness of Apple’s iTunes RSS parser matters,
simply because it is so popular. As [Pilgrim wrote](http://intertwingly.net/blog/2005/07/05/Insensitive-iTunes#c1120699228):


> Apple is an 800-lb. gorilla in this space (at least until
> Microsoft releases an RSS-enabled IE in Longhorn).  iTunes is to
> podcasting as Internet Explorer is to HTML.  RSS
> interoperability, at least as far as podcasting goes, now means
> “works with iTunes.”  Thousands of people and companies will
> begin making podcasts that “work with iTunes,” but
> unintentionally rely on iTunes quirks (e.g. Disney’s incorrect
> namespace).  This in turn will affect every developer who wants
> to consume RSS feeds, and who will be required to emulate all the
> quirks of iTunes to remain competitive.


The question shouldn’t be “Why weren’t these issues resolved from the
start?”, but instead “Will Apple care enough to resolve them going
forward?”


Judging by [this report from Tantek Çelik](http://tantek.com/log/2005/07.html#d10t0130), who met with some
friends of his on Apple’s iTunes team, the answer appears to be “yes”:


> At that point we started discussing the [iTunes podcast
> extensions (PDF link)](http://phobos.apple.com/static/podcast_specifications.pdf), and the [reactions from the blog
> community](http://www.technorati.com/search/Apple%20iTunes%20podcast%20extensions). Blog comments ranged from constructive to
> whiny, from polite to rude, from objective to snarky. But
> regardless of the tone that bloggers took, it was clear to
> Kevin and me that the iTunes team was very much open to
> feedback and constructive criticism, and subsequent fixes in
> the podcast extensions specification, and iTunes itself. [...]
> The most thorough comments came from Sam Ruby and Mark Pilgrim,
> e.g. in Sam’s post titled Insensitive iTunes. We went over Sam
> and Mark’s specific comments and came up with several things that
> could be fixed in the the spec and/or implementation. Mark’s test
> cases were particularly helpful.
> Kevin and I volunteered to help out with iterations on the spec.
> Kevin knows a thing or two about RSS and podcasting, and I know a
> thing or two about spec-writing. We’re going to be providing
> feedback within the next day or so. [...]


It’s easier to ask forgiveness than to seek permission — and, let’s
face it, Apple was not going to seek permission from anyone on
something like this. Assuming Çelik is correct about the iTunes team’s
willingness to clarify the spec and fix the iTunes RSS parser’s
failures, forgiveness ought to come easily. Apple is in a position to
do whatever they want regarding podcasting, but for the most part, it
appears that what they want to do is the right thing.


---

1. Which you should listen to before asking me why I’m not podcasting. ↩︎



| **Previous:** | [Plugged Leaks](https://daringfireball.net/2005/07/plugged_leaks) |
| **Next:** | [About the Footnotes](https://daringfireball.net/2005/07/footnotes) |


PreviousNext