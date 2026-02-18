---
title: "Apps of the Year, 2004"
date: 2005-02-16
url: https://daringfireball.net/2005/02/apps_of_the_year_2004
slug: apps_of_the_year_2004
word_count: 3489
---


Six weeks late but better than never, here are my favorite new Mac
apps from 2004. The rules are simple: these are the apps released
last year that I like best.

1. Interarchy 7
2. Affrus 1.0
3. SpamSieve 2.2
4. BBEdit 8.0


Plus a few others that deserve mention.


## Interarchy 7


File transfer apps constitute a very crowded class of Mac software.
I’m not sure of any other category where there are so many
reasonably serious contenders. But at the top of the heap are two:
Panic’s [Transmit](http://www.panic.com/transmit/), and Stairways Software’s [Interarchy](http://www.interarchy.com/).
My hunch — based mostly on people I know personally, and thus a
small sample size — is that Transmit users tend to be younger
and/or newer Mac users; whereas Interarchy users tend to be older
and longer-term Mac users.


Interarchy’s roots go back at least as far as December 1993, when
[Peter N Lewis released Anarchie 1.0](http://www.stairways.com/press/1993-12-07) — which was before the
Mac OS even offered built-in support for TCP/IP networking. (The
“archie” in “Anarchie” comes from [Archie](http://en.wikipedia.org/wiki/Archie_search_engine), a long-since
forgotten search engine for public FTP servers.) Anarchie’s primary
rival during the System 7 era was Jim Matthews’s [Fetch](http://fetchsoftworks.com/), which
[Matthews originally developed in 1989](http://fetchsoftworks.com/Goodies/story.html) as an in-house tool for
use at Dartmouth College.


Anarchie and Fetch were both terrific apps — small, fast, and
stable. Both offered robust support for then-new Mac technologies
such as AppleScript and the Drag Manager (yes, that’s right, a
decade ago, good drag-and-drop support was a high-end feature).
Their primary difference, to my mind at least, was in terms of their
windowing metaphors. Anarchie worked like the Finder, creating a new
window to display the contents of each FTP directory you opened.
Fetch worked like a browser, using a single window for each
connection.


As much as I was (and remain) an enormous fan of the old Finder’s
“each folder opens in its own window” metaphor, for *remote* file
access via a protocol such as FTP, I’ve always preferred the
single-window metaphor. Thus, for most of the ’90s, I was
predominantly a Fetch man.


Back in 2000, [when Stairways changed the name of the app](http://db.tidbits.com/getbits.acgi?tbart=06080)
from Anarchie to Interarchy, they also changed the scope of what the
app did. Rather than focusing solely on FTP, they turned the app
into a sort of Swiss Army knife networking toolkit, rolling together
into one app several other network diagnostic utilities which
Stairways had previously developed as separate apps. Some of the
features were minor (e.g. support for the finger: protocol), and
others were quite powerful (e.g. a network traffic monitor that can
record all incoming and outgoing network traffic to your machine).


The other big change in the move from Anarchie to Interarchy was
that the entire user interface became skinnable, via plug-in
packages they called “magic wands”. It was, more or less, analogous
to the skinnable UIs of music-player apps like SoundJam and [Audion](http://www.panic.com/audion/). I considered it utterly silly, and apparently so did others —
Stairways quietly de-emphasized “wands” in subsequent Interarchy
releases. This lack of focus led me to lose interest in Interarchy
as an FTP app. Or more specifically, it led me to stick with my copy
of Anarchie 3.


Starting around 2001, my use of Fetch waned as well, as the sites I
worked on began switching from FTP to SFTP. (Even today, [Fetch
doesn’t support SFTP](http://fetchsoftworks.com/Support/faq.html#feat2), although it is slated for the next major
release.) The first app I used for SFTP was [MacSFTP](http://pro.wanadoo.fr/chombier/MacSFTP/SFTP_info.html), a
relatively unheralded little gem by Jean-Pierre Stierlin. Later on,
I switched to Panic’s [Transmit](http://www.panic.com/transmit/), version 2 of which was
rewritten specifically for Mac OS X. Transmit certainly has a more
polished UI than MacSFTP, and also offers more features and a bit
more configurability. However, MacSFTP offers a much better
AppleScript interface than does Transmit.


Thus, for most of 2003, I used Transmit for GUI access to SFTP, and
MacSFTP for automating a few tasks via AppleScript.


### Enter Interarchy 7


When Interarchy 7 was released last year, I was intrigued. It too
had been rewritten specifically for Mac OS X (and in a very nice
gesture, Stairways made Interarchy 6.3 — the last version that ran
on Mac OS 9 — [available as a free download](http://www.stairways.com/main/download)). Here are the
features that made me decide to give Interarchy 7 a shot:

- It now defaults to a browser-style interface, exactly what I
prefer for a file-transfer app. (But there’s a preference to
always open folders in new windows, if that’s what you prefer.)
- Aesthetically, it instantly struck me as a very well-done Aqua
app; the Interarchy web site has a page full of [screenshots](http://www.interarchy.com/documentation/7/screenshots) to prove it.
- Interarchy 7 supports tabs, very similar to those in Safari.
(In fact, if you tweak Safari’s nib file to turn off the brushed
metal theme, Interarchy’s tabs are nearly identical to
Safari’s.) ⌘T creates a new empty tab, ⌘-double-click opens a
directory in a new tab.
- Interarchy’s list view supports hierarchical disclosure
triangles, much like the Finder’s. I’ve wanted disclosure
triangles for S/FTP list views for years; now that I have
them in Interarchy, I use them nearly every day.
- Column and icon views, much like the Finder. I tend to use list
view almost exclusively, but you can pretty much view files
however you like with Interarchy 7.


Plus, Interarchy 7 offers all of the things previous versions were
well-known for:

- Fast, reliable network connections. New connections open
quickly; open connections never drop.
- Terrific AppleScript support, including recordability. Anarchie
and Interarchy have always had superior AppleScript support.
- Pretty good [documentation](http://www.interarchy.com/documentation/7/).
- Great support for remote file editors (i.e. “opening” files in
BBEdit (or another text editor) over SFTP), including the
ability to open files for editing by double-clicking on them.
- Low resource use. (As I write this, I’ve had Interarchy running
non-stop for several days, with two or three connection windows
and up to 10 tabs; it’s only using 5.5 MB of private memory.)
- Fast, easy-to-configure, easy-to-invoke mirroring to sync local
and remote folders.


New single-user licenses for Interarchy start at $39 (USD) — about
$10-15 more than most competing apps, but it’s easily worth the
premium. Plus, upgrade pricing is generous — I upgraded from
Anarchie 3 for just $19, a pittance considering I hadn’t sent
Stairways a dime since 1999.


What’s great about Interarchy isn’t that it has tons of features
(although it does), but that its features are so well done. It’s the
attention to detail that makes Interarchy a pleasure to use. In
almost every way, it simply works exactly how I expect and want an
S/FTP client to work.


The end result is that since I switched to Interarchy 7 last March,
it’s the first time I’ve been satisfied with a file-transfer app in
nearly 10 years.


## Affrus 1.0


Late Night Software’s flagship product is Script Debugger, far and
away the best AppleScript editor — and, of course, debugger —
available.


Last March, Late Night released [Affrus 1.0](http://latenightsw.com/affrus/), a $99 (USD)
editor and debugger for Perl. It is both simple and powerful. Its
basic operation is exactly what you’d expect (especially if you’ve
ever used Script Debugger):

- Perl scripts are displayed with highly configurable syntax
coloring, as well as function navigation. Perl’s syntax is
highly flexible, which makes it notoriously difficult for other
software to parse; Affrus does a fine job.
- Debugging is controlled via the normal conventions of an IDE
debugger: you can set breakpoints, step into or over subroutine
calls, step into modules, and pretty much step through each line
of your scripts from beginning to end.
- While debugging, it’s easy to observe the contents of complex data
structures (such as, say, a hash of hashes).
- A command-line ‘affrus’ tool acts as a stand-in for Perl, accepting
parameters as well as STDIN; the only difference from calling the
regular ‘perl’ tool is that your script opens in Affrus for debugging.
This makes it a cinch to invoke.


Plus — and this is not surprising given its pedigree — Affrus is
itself a wonderfully scriptable application via AppleScript.
(Although it would be a nice touch if you could script it using
Perl, too. E.g. something analogous to BBEdit’s Unix Filters, for
modifying the text content of a window.)


If $99 strikes you as a lot of money to pay for a text editor that
just does Perl, you either don’t need a Perl debugger or you’re
missing the point. While Affrus can indeed serve as a fine text
editor for writing Perl, it is in no way intended as a replacement
for a general text editor. In fact, Affrus supports BBEdit and
TextWrangler as external editors (and conversely, BBEdit and
TextWrangler support Affrus as the target of their #! menu’s “Run in
Debugger” command).


The point of Affrus is debugging, and no other editor for Mac OS X
offers what Affrus does. The ‘perl’ command line tool offers its own
debugging mode, of course, and if you like it, well, you can save
your money for something else. To me, the point of Perl’s built-in
debugger is that it allows something such as Affrus to be built on
top of it; prior to Affrus, I typically “debugged” my Perl code the
old-fashioned way — by sprinkling extra `print` statements wherever
I wanted to observe data values in my code.


If you write a lot of Perl, Affrus, quite simply, can save you a
tremendous amount of time. And if you’re writing Perl
professionally, that time is money.


### Outstanding Help


It’s also worth mentioning that Affrus ships with extraordinary
documentation. This isn’t surprising, considering that it was
written by [Matt Neuburg](http://www.tidbits.com/matt/), whom I consider the best technical
writer in the business. But what *is* surprising is the nature and
format of the documentation. First, Affrus ships with a 37-page PDF
document, titled “Getting Started With Affrus”. It’s well-written
and does exactly what its title claims.


But where Affrus’s documentation enters a league of its own is its
help. Yes, the help files — the documentation you access via the
Help menu, which consists of HTML files displayed in the Mac OS X
Help Center application. The sort of help files which, if you’re
like most Mac users, especially the sort of technically savvy ones
who might be interested in something as esoteric as a debugger for
Perl, you completely ignore. Help is ignored because it tends to
utterly suck. (Apple, I am looking in your direction.)


Ignoring Affrus’s help would be tragic, because it not only doesn’t
suck, it is quite simply the finest software documentation I have
every encountered. It’s not just that it’s well-written, detailed,
accurate, and complete. It’s that it truly takes advantage of the
nature of hypertext. It is cross-referenced and cross-linked out the
ying-yang. If you have a specific question, it is easy to find the
answer and jump to it directly. (And every question I’ve ever had
about Affrus is answered in the help documentation.) But if you want
to read the documentation linearly, from beginning to end, it’s easy
to do that too.


Affrus’s help isn’t just good when compared against the deplorable
state of your average help book (“*Help isn’t available for
>insert app name<*”) — it’s just plain great by any standard.


(If you’re a technical writer, I urge you to download the Affrus
demo and examine its help, even if you have no interest in using
Affrus. Even better, Mr. Neuburg wrote an [article for O’Reilly’s
MacDevCenter describing how Affrus’s help was produced](http://www.macdevcenter.com/lpt/a/4734) using
[Tinderbox](http://www.eastgate.com/Tinderbox/).)


### It Is, However, a One-Point-Oh


I recommend Affrus wholeheartedly, but that’s not to say it doesn’t
have plenty of room for improvement. There are only two types of 1.0
products: those which ship with missing features, and those which
never actually ship.


Two big features are missing from Affrus 1.0:

- Debugging CGI scripts
- Support for debugging languages other than Perl


But for what it’s worth, Late Night Software’s Mark Alldritt has
acknowledged both of these as features he’d like to add in the
future. [Regarding CGI debugging](http://groups.yahoo.com/group/affrus-talk/message/26):


> There are three forms of CGI debugging that I’m trying to
>  provide for in future versions of Affrus:
> apache CGI debugging
> mod_perl debugging
> CGI simulation with the Affrus UI


[Regarding support for other languages](http://groups.yahoo.com/group/affrus-talk/message/23):


> Affrus is designed to support multiple languages. We had to
> pick one to focus on for a 1.0 release and we chose Perl, but
> in a future version we are going to offer Python (so far, we
> have received a vast number of requests for Python support and
> only a few for Ruby).


### See Also

- Simon Cozens wrote a more feature-oriented [review of Affrus](http://www.perl.com/pub/a/2004/05/14/affrus.html) for 
Perl.com back in May.
- Late Night Software is currently offering a bundle: Affrus 1.0
and Script Debugger 3.0 for $239 (USD) — which saves you $49 off
their regular prices.


## SpamSieve 2.2


Michael Tsai’s SpamSieve epitomizes the idea of utility software
that does one thing, and does it well. What SpamSieve does is
identify spam in your email, and it does so with accuracy that
approaches perfection.


SpamSieve 2.2 was released in August, ostensibly as a relatively
minor feature to SpamSieve 2.x. My results with 2.2 (and continuing
up through the current 2.2.4 release) have been a decided and
noticeable increase in accuracy. SpamSieve went from great to really
great.


From September through now, its overall accuracy has steadily
increased from around 99.5 percent to 99.8 percent. More
importantly, when it’s wrong, especially regarding false positives
(good messages incorrectly flagged as spam), it tends to only err
with edge cases. E.g. a thrice-forwarded joke from a mouth-breathing
Hotmail user.


Here are my stats from 1 December 2004 through 14 February 2005:



| Filtered Mail |
| 7960 Good Messages |
| 16469 Spam Messages (67%) |
| 215 Spam Messages Per Day |




| SpamSieve Accuracy |
| 29 False Positives |
| 29 False Negatives (50%) |
| 99.8% Correct |



In addition to 2.2’s even-better general accuracy, another change in
my use of SpamSieve in 2004 led to a significant improvement in its
overall effectiveness. What I did was switch to labeling messages
differently based on their scores assigned by SpamSieve. By default,
my email client (Mailsmith) treats SpamSieve’s scoring as binary —
each message is flagged as spam or not-spam.


However, [using AppleScripts available for download from Mr. Tsai’s
web site](http://c-command.com/scripts/spamsieve/), you can instead access the raw scores SpamSieve
assigns to each message: a number ranging from 0 (not spammy at all)
to 100 (smells like spam from a mile away).


So I have a filter in Mailsmith that runs an AppleScript against
each incoming message. The script gets each message’s spam score
from SpamSieve. If the score is less than 50, the message is
considered not-spam. If the score is 91 or higher, it’s considered
spam, assigned a custom message label, and moved to my spam box. But
if the score is between 50 and 90, it’s considered *suspected* spam.
These messages are still moved to my spam box, but they’re assigned
a different message label than higher-scoring spam.


I keep my spam box sorted by label; thus, I can easily scan through my “suspect” spam messages once or twice a day.


This is an incredibly powerful technique — mainly because SpamSieve
2.2 has gotten so much better about assigning very high scores to
most spam messages.


For example, at this moment, I have about two days’ worth of spam in
my spam box: 372 messages. Of those, only 13 messages are labeled as
“suspected” spam; the other 359 were scored at 91 or higher.


I only manually review my suspected spam. That means in two days,
I’ve only needed to glance at 14 messages — 13 spams and one false
positive. It was easy to spot the false positive, because I only had
to pick it out from around a dozen messages.


In the six months or so that I’ve been using this technique, I’ve
found only *one* false positive that came in with a score 91 or
higher — a ticket confirmation message from Southwest Airlines,
from whom I’d never before purchased tickets. I found the message in
my spam box because I looked for it when it didn’t appear in my
inbox a few minutes after I completed the transaction on Southwest’s
web site. It’s certainly possible that there have been other such
high-scoring false positives that I didn’t detect, but if so, it was
never anything important.


In short, by using AppleScript, you can get SpamSieve to offer a
response other than just “spam” or “not spam” — you can find out
when it’s a “maybe”. By only reviewing the maybes, I’ve cut down
tremendously on the amount of spam I need to review manually.


This is where I’ve found SpamSieve 2.2’s accuracy to be most
improved over SpamSieve 2.1 and earlier. It now assigns the vast
majority of my spam very high scores, whereas in previous versions,
many more messages that were indeed spam were flagged with lower
scores — which meant I had many more messages that I needed to
review manually before trashing them.


### Further Reading


I [interviewed Michael Tsai](https://daringfireball.net/2003/09/interview_michael_tsai) in September 2003.


## BBEdit 8.0


[I wrote an extensive review of BBEdit 8](https://daringfireball.net/2004/09/bbedit_8) shortly after it
shipped in September, and I don’t really have much to add above what
I wrote then. It’s a terrific update to my all-time favorite app.


## Honorable Mentions


Three other apps deserve mention:

- [NetNewsWire 2.0](http://ranchero.com/netnewswire/)
- [Quicksilver](http://quicksilver.blacktree.com/)
- [OmniWeb 5](http://www.omnigroup.com/applications/omniweb/)


I would have included both Quicksilver and NetNewsWire 2 on the
list, if not for the fact that both are technically in “beta”. I put
that in quotes because in both cases, we’re talking about public
betas that are in such widespread use that they stretch the concept
of beta software to the limits of credibility.


E.g., in NetNewsWire’s case, in the month of February to date, 46
percent of the hits to my main RSS feed are from people using 2.0
“betas” of NetNewsWire or NetNewsWire Lite; only 30 percent are
using NetNewsWire 1.0.x. (And yes, NetNewsWire’s combined market
share is *that* high among DF readers.) I’m not sure how it can be a
“beta” if more people are using it than are using the non-beta 1.0.x
releases.


Private betas are another matter, but I’m seriously questioning
whether it’s worth making a distinction between public betas and
release software. If next year I assemble a list of apps of the year
for 2005, I may well decide that public betas are fair game for
inclusion. My thinking for *not* including them as betas is that
they ought to count for the year in which they come out of beta —
but of course, that assumes Quicksilver is *ever* going to come out
of “beta”.


As for OmniWeb 5, I spent much of 2004 using it as my primary web
browser. I was effusive with praise for many of its features in [my
initial review](https://daringfireball.net/2004/02/omniweb_5_public_beta) of the OmniWeb 5.0 public beta, and it only
got better as a proper (non-beta) release.


However, a few weeks ago I bit the bullet and switched back to
Safari. Quite simply, the reason was performance. Safari feels much
faster than OmniWeb, and it tends to use much less memory.


This might not matter for people with faster CPUs and/or more RAM
than in my iBook, but for me, the result was that OmniWeb felt a bit
slow whenever I had more than a handful of open windows — which is
pretty much all time. Not super-slow — more like the way the entire
UI in Mac OS X 10.0 felt slow. Mouse clicks taking an extra fraction
of a second to register, that sort of thing.


It’s also the case that I prefer Safari’s page rendering. OmniWeb
plays strange games with certain fonts (Bitstream Vera Sans italic,
for example, gets an extra dose of faux-italic slanting applied when
displayed in OmniWeb), and worst of all, it insists upon
anti-aliasing Monaco 9 and 10, [which is just wrong](https://daringfireball.net/2003/03/antiantialiasing).


The Omni Group’s modified version of WebCore is a very good
renderer, but it’s not as good as the standard Web Kit renderer.


What I miss most about OmniWeb:

- Per-site display preferences
- Automatic saving and restoring of state on quit and launch
- AppleScript access to tabs
- The ability to drag tabs between windows, or to rearrange their
order within a single window


It’s quite possible that if my main Mac were a G5 with 1 GB or more
of RAM, OmniWeb 5 would have made the list. But it’s not, and so it
didn’t.



| **Previous:** | [Marking Subscriptions as ‘Private’ in Bloglines](https://daringfireball.net/2005/02/bloglines) |
| **Next:** | [How to Create an ‘App of the Year’](https://daringfireball.net/2005/02/how_to_create_an_app_of_the_year) |


PreviousNext