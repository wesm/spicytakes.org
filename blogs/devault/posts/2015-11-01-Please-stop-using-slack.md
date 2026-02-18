---
title: "Please don't use Slack for FOSS projects"
date: 2015-11-01
url: https://drewdevault.com/2015/11/01/Please-stop-using-slack.html
slug: Please-stop-using-slack
word_count: 1045
---

I’ve noticed that more and more projects are using things like Slack as the chat
medium for their open source projects. In the past couple of days alone, I’ve
been directed to Slack for Babel and Bootstrap. I’d like to try and curb this
phenomenon before it takes off any more.

## Problems with Slack

Slack…

* is closed source
* has only one client ( *update: errata at the bottom of this article* )
* is a walled garden
* requires users to have a different tab open for each project they want to be
involved in
* requires that Heroku hack to get open registration

The last one is a real stinker. Slack is not a tool built for open source
projects to use for communication with their userbase. It’s a tool built for
teams and it is ill-suited to this use-case. In fact, Slack has gone on record
as saying that it  *cannot*  support this sort of use-case: “it’s great that
people are putting Slack to good use” but unfortunately “these communities are
not something we have the capacity to support given the growth in our existing
business.”  1

## What is IRC?

IRC, or Internet Relay Chat…

* is a standardized and well-supported protocol  2
* has hundreds of open source clients, servers, and bots  3
* is a distributed design with several networks
* allows several projects to co-exist on the same network
* has no hacks for registration and is designed to be open

### No, IRC is not dead

I often hear that IRC is dead. Even my dad pokes fun at me for using a 30 year
old protocol, but not after I pointed out that he still uses HTTP. Despite the
usual shtick from the valley, old is not necessarily a synonym for bad.

IRC has been around since forever. You may think that it’s not popular anymore,
but there are still tons of people using it. There are 87,762 users  *currently
online*  (at time of writing) on Freenode. There are 10,293 people on OFTC.
22,384 people on Rizon. In other words, it’s still going strong, and I put a lot
more faith in something that’s been going full speed ahead since the 80s than in
a Silicon Valley fad startup.

## Problems with IRC that Slack solves

There are several things Slack tries to solve about IRC. They are:

**Code snippets** : Slack has built-in support for them. On IRC you’re just asked
to use a pastebin like Gist.

**File transfers** : Slack does them. IRC also does them through XDCC, but this
can be difficult to get working.

**Persistent sessions** : Slack makes it so that you can see what you missed when
you return. With IRC, you don’t have this. If you want it, you can set up an IRC
bouncer like  [ZNC](http://znc.in/) .

**Integrations** : with things like build bots. This was never actually a problem
with IRC. IRC has always been significantly better at this than Slack. There is
 *definitely*  an IRC client library for your favorite programming language, and
you can write your own client from scratch in a matter of minutes anyway.
There’s an  [IRC](https://github.com/nandub/hubot-irc)  backend for Hubot, too.
GitHub has a built-in hook for announcing repository activity in an IRC channel.

## Other projects are using IRC

Here’s a short, incomplete list of important FOSS projects using IRC:

* Debian
* Docker
* Django
* jQuery
* Angular
* ReactJS
* NeoVim
* Node.js
* everyone else

The list goes on for a while. Just fill in another few hundred bullet points
with your imagination. Seriously, just join  `#<project-name>`  on Freenode. It
probably exists.

## IRC is better for your company, too

We use IRC at  [Linode](https://www.linode.com/) , even for non-technical people.
It works great. If you want to reduce the barrier to entry for non-technicals,
set up something like  [shout](https://github.com/erming/shout)  instead. You can
also have a pretty no-brainer link to webchat on almost every network,  [like
this](http://webchat.esper.net/?nick=&channels=truecraft) . If you need file
hosting, you can deploy an instance of
 [sr.ht](https://github.com/SirCmpwn/sr.ht/)  or something like it. You can also
host IRC servers on your own infrastructure, which avoids leaving sensitive
conversations on someone else’s servers.

## Please use IRC

In short, I’d really appreciate it if we all quit using Slack like this. It’s
not appropriate for FOSS projects. I would much rather join your channel with
the client I already have running. That way, I’m more likely to stick around
after I get help with whatever issue I came to you for, and contribute back by
helping others as I idle in your channel until the end of time. On Slack, I
leave as soon as I’m done getting help because tabs in my browser are precious
real estate.

[First discussion on Hacker News](https://news.ycombinator.com/item?id=10486541)

[Second discussion on Hacker News](https://news.ycombinator.com/item?id=11013136)

## Updates

Addressing feedback on this article.

**Slack IRC bridge** : Slack provides an IRC bridge that lets you connect to
Slack with an IRC client. I’ve used it - it’s a bit of a pain in the ass to set
up, and once you have it, it’s not ideal. They did put some effort into it,
though, and it’s usable. I’m not suggesting that Slack as a product is worse
than IRC - I’m just saying that it’s not better than IRC for FOSS projects, and
probably not that much better for companies.

**Clients** : Slack has several clients that use the API. That being said, there
are fewer of them and for fewer platforms than IRC clients, and there are more
libraries around IRC than there are for Slack. Also, the bigger issue is that I
already have an IRC client, which I use for the hundreds of FOSS projects that
use IRC, and I don’t want to add a Slack client for one or two projects.

**Gitter** : Gitter is bad for many of the same reasons Slack is. Please don’t
use it over IRC.

**ircv3** : Check it out:  [ircv3.net](http://ircv3.net)

**irccloud** : Is really cool and solves all of the problems.  [irccloud.com](https://www.irccloud.com/)

**2018-03-12** : Slack is shutting down the IRC and XMPP gateways.

1. [Slack is quietly, unintentionally killing IRC - The Next Web](http://thenextweb.com/insider/2015/03/24/slack-is-quietly-unintentionally-killing-irc/) ↩︎
2. [RFC 1459](https://www.rfc-editor.org/rfc/rfc1459.txt) ↩︎
3. [Github search for IRC](https://github.com/search?o=desc&q=irc&s=stars&type=Repositories&utf8=%E2%9C%93) ↩︎
