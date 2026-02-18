---
title: "The Location Field Is the New Command Line"
date: 2004-06-22
url: https://daringfireball.net/2004/06/location_field
slug: location_field
word_count: 1669
---


When you publish your opinions on a regular basis, it’s hard to
resist the urge to gloat after you’ve been proven correct. (For
example, I’ll be I-told-you-so-ing with regard to the iPod mini for
the next couple of years.)


It’s also rather easy to ignore the times when you’ve been proven
wrong.


It’s a good thing I wasn’t publishing Daring Fireball back in the
mid-to-late ’90s, because if I had been, I’d currently be eating an
awful lot of crow with regard to what I would have written about the
web’s potential as an application platform.


At that time, at the peak of the Netscape-Microsoft browser war, the
conventional wisdom was that the web was the future of application
development. The technology certainly didn’t yet exist, but the idea
was that Netscape’s web browser posed a serious threat to
Microsoft’s Windows monopoly — that at some point in the future,
user applications would be written to run within the browser.


Thus, Microsoft’s incredible change of course, going from more or
less ignoring the Internet to completely dominating it within the
course of a few years. The idea was that Microsoft killed Netscape
because Microsoft saw them as a threat to Windows.


Me, however, I just didn’t buy it. I completely saw the potential of
the Web as a *publishing* medium, but I just didn’t see how the Web
was ever going to serve as a high-quality application development
environment. The way I saw it, Microsoft killed Netscape not because
it was a threat to Windows, but simply because they (Microsoft)
wanted control over this new publishing medium.


I simply couldn’t have been more wrong. The conventional wisdom was
in fact correct — the web *has* turned into a popular application
development environment. Where I’d gone wrong was in getting hung up
on the idea of it needing to be high-quality before it could become
popular.


I was thinking in terms of the apps that I used every day, circa
1996: BBEdit, QuarkXPress, Photoshop, Eudora. There was simply no
way that a “web app” could ever provide the same quality experience
as the “real” apps I was already using. And I was right about that
— the user experience of any app running in a web browser is
crippled.


What I’d overlooked is that most people don’t use advanced text
editors or desktop publishing software; and more importantly,
most people simply don’t care about the quality of an app’s
user experience. Not at all. They just want it to work, and to be
“easy”.


My saying that web apps would never become popular was like a
theater critic in the early 1950s dismissing television.


The user experience limitations of a web app are glaringly obvious.
They simply don’t look or act like normal desktop apps. The browser
in which they’re running — *that’s* a normal app. But the web apps
running within the browser aren’t. They don’t have menu bars or
keyboard shortcuts. (The browser itself does.) This isn’t about
being “Mac-like” — it applies equally to Windows and open source
desktop platforms. Instead of looking and feeling like real
Mac/Windows/Linux desktop apps, web apps look and feel like web
pages.


The persnickety little UI details I obsess over — these are nothing
compared to the massive deficiencies of even the best web app. But
most people don’t care, because web apps are just so damned easy to
use. What’s interesting is that web apps are “easy” despite their
glaring user experience limitations.


What they’ve got going for them in the ease-of-use department is
that they don’t need to be installed, and they free you from
worrying about where and how your data is stored. Exhibit A:
web-based email apps. In terms of features, especially comfort
features such as a polished UI, drag-and-drop, and a rich set of
keyboard shortcuts, web-based email clients just can’t compare to
desktop email clients.


But.


With web-based email, you can get your email from any browser on any
computer on the Internet. “Installation” consists of typing a URL
into the browser’s location field. The location field is the new
command line.


Google’s Gmail has turned the competition up a notch by providing a
few features that actually do compare well against desktop email
clients — fast, accurate search (of course), and a very nice
threaded display for discussions. Gmail also offers a bunch of
keyboard shortcuts, implemented in JavaScript, but as [Mark Pilgrim
described them in his Gmail review](http://diveintomark.org/archives/2004/04/10/gmail-accessibility), they


> [appear] to have been designed by vi users (`j` moves
> down, `k` moves up, and we are expected to memorize
> multi-key sequences for navigation).


Gmail’s threading and searching are indeed nice, but its overall
look-and-feel is far inferior to that of a real desktop mail client.
What it has going for it is what all webmail apps have — zero
installation, zero maintenance, access from any computer,
anywhere (including from work, a major factor for personal email).
Gmail is simply better than the other major web-based mail apps; but
Yahoo and Hotmail and the others are still ragingly popular.


What I missed when I dismissed them a decade ago is that web apps
don’t need to beat desktop apps on the same terms. What’s happened
is that they’re beating them on an entirely different set of terms.
It’s all about the fact that you just type the URL and there’s your
email.


## Who Loses As Web Apps Win?


What got me thinking about this was [Joel Spolsky’s “How Microsoft
Lost the API War”](http://www.joelonsoftware.com/articles/APIWar.html), a terrific essay published last week. The
gist of Spolsky’s argument is that Microsoft’s crown jewel is the
Win32 API — the set of programming interfaces that developers use
to write desktop Windows software — and that web app development is
gaining momentum, at the direct expense of Win32 development.


The reason the Win32 API is so important to Microsoft’s Windows
monopoly is dependence: if your company relies on Win32 software,
then it also relies on Windows. And conversely, as a developer,
writing against the Win32 APIs allows your software to run on over
90 percent of the computers in the world. That’s the cycle that
built a $50 billion pile of cash — customers use Windows because
that’s where the software is, and developers write Windows software
because that’s where the customers are.


Switching to, say, Mac OS X is an expensive proposition for a large
corporation. Not only do you need all-new hardware, but you also
need all-new software. And we’re not just talking about buying new
licenses — for large corporations, we’re also talking about custom
apps written in-house (what do you think all those Visual Basic
developers have been writing all these years?).


Switching to open source desktops — KDE or Gnome or what have you
— is also expensive. No, you don’t need new hardware, but you still
run into the same situation with regard to software. (Yes, I know —
you can run Win32 apps on Linux using the [WINE](http://www.winehq.com/) Win32 emulator,
or with Virtual PC for Macs, but these are second-class Win32
environments. I’m not saying it can’t be done, just that it’s
unappealing.)


Switching to web applications, however — well, that’s different. It
can be done gradually, because you can switch one app at a time
while still running Windows, and thus, still running all your other
Win32 software.


It’s not so much that switching to web apps is cheap, as that it’s
easy. In fact, in many ways, switching your employees to web apps is
even easier than upgrading the Win32 apps they’re already using.
I.e. it’s easier for corporations to migrate to web apps than it is
for them to stay Windows-only.


Web apps are easier to deploy. No need to install software on each
client machine; there’s just one instance of the app, on a web
server. Every user gets the latest version of the software,
automatically.


Custom web apps are easier to develop than custom desktop apps.
That’s not to say it’s easy to make a web app that looks and feels
like a desktop app — that’s not really even possible. But it’s easy
to write a web app that looks and feels like a web page, which is
apparently good enough for most purposes, especially data-entry and
data-retrieval apps that tie into server-hosted SQL databases.


And if you think the 90-percent market share of computers that can
run Win32 software is huge — how many computers do you think run a
typical web app?


Most email web apps (e.g. Gmail and Yahoo Mail) run on any computer
with IE, Safari, or any Mozilla-derived browser. Most weblog web
apps (e.g. [Blogger](http://blogger.com/), [Movable Type](http://www.movabletype.org/), [WordPress](http://wordpress.org/), and
[Textpattern](http://textpattern.com/)) run in every browser I’ve ever tried. These
apps are effectively usable from any Internet-connected computer in
the world.


I’ve been thinking about the rise of the web as an application
platform for a while. But what hadn’t occurred to me until I read
Spolsky’s essay last week is this, which I think is quite
remarkable: Microsoft totally fucked up when they took aim at
Netscape. It wasn’t *Netscape* that was a threat to Windows as an
application platform, it was the web itself.


They spent all that time, money, and development effort on IE,
building a browser monopoly and crushing Netscape — but to what
avail? Here we are, and the web is still gaining developer
mindshare at the expense of Win32.


There are certainly exceptions — banking sites come to mind — but
for the most part, web apps are being built to run in any modern
browser, not just IE.


I think Spolsky is very much correct that Microsoft is losing the
API war. But what’s ironic is that they’re losing this war despite the
fact that they won the browser war. Winning the browser war —
destroying Netscape — was supposed to prevent there ever even being
an API war.



| **Previous:** | [Membership Giveaways](https://daringfireball.net/2004/06/membership_giveaways) |
| **Next:** | [More Membership Prizes](https://daringfireball.net/2004/06/more_membership_prizes) |


PreviousNext