---
title: "Please don't use Discord for FOSS projects"
date: 2021-12-28
url: https://drewdevault.com/2021/12/28/Dont-use-Discord-for-FOSS.html
slug: Dont-use-Discord-for-FOSS
word_count: 1051
---

Six years ago, I wrote a post speaking out against the use of Slack for the
instant messaging needs of FOSS projects. In retrospect, this article is not
very good, and in the years since, another proprietary chat fad has stepped up
to bat: Discord. It’s time to revisit this discussion.

In short, using Discord for your free software/open source (FOSS) software
project is a very bad idea. Free software matters — that’s why you’re
writing it, after all. Using Discord partitions your community on either side of
a walled garden, with one side that’s willing to use the proprietary Discord
client, and one side that isn’t. It sets up users who are passionate about free
software — i.e. your most passionate contributors or potential
contributors — as second-class citizens.

By choosing Discord, you also lock out users with accessibility needs, for whom
the proprietary Discord client is often a nightmare to use. 1  Users who cannot
afford new enough hardware to make the resource-intensive client pleasant to use
are also left by the wayside. Choosing Discord is a choice that excludes poor
and disabled users from your community. Users of novel or unusual operating
systems or devices (i.e. innovators and early adopters) are also locked out of
the client until Discord sees fit to port it to their platform. Discord also
declines service to users in countries under US sanctions, such as Iran.
Privacy-concious users will think twice before using Discord to participate in
your project, or will be denied outright if they rely on Tor or VPNs. All of
these groups are excluded from your community.

These problems are driven by a conflict of interest between you and Discord.
Ownership over your chat logs, the right to set up useful bots, or to moderate
your project’s space according to your discretion; all of these are rights
reserved by Discord and denied to you. The FOSS community, including users with
accessibility needs or low-end computing devices, are unable to work together to
innovate on the proprietary client, or to build improved clients which better
suit their needs, because Discord insists on total control over the experience.
Discord seeks to  [domesticate its users](https://seirdy.one/2021/01/27/whatsapp-and-the-domestication-of-users.html) , where FOSS treats users as peers
and collaborators. These ideologies are fundamentally in conflict with one
another.

You are making an investment when you choose to use one service over another.
When you choose Discord, you are legitimizing their platform and divesting from
FOSS platforms. Even if you think they have a bigger reach and a bigger
audience, 2  choosing them is a short-term, individualist play which signals a
lack of faith in and support for the long-term goals of the FOSS ecosystem as a
whole. The FOSS ecosystem needs your investment. FOSS platforms generally don’t
have access to venture capital or large marketing budgets, and are less willing
to use dark patterns and predatory tactics to secure their market segment. They
need your support to succeed, and you need theirs. Why should someone choose to
use your FOSS project when you refused to choose theirs? Solidarity and mutual
support is the key to success.

There are great FOSS alternatives to Discord or Slack. SourceHut has been
investing in IRC by building more accessible services like  [chat.sr.ht](https://sourcehut.org/blog/2021-11-29-announcing-the-chat.sr.ht-public-beta/) . Other
great options include  [Matrix](https://matrix.org)  and  [Zulip](https://zulip.com) . Please consider these services
before you reach for their proprietary competitors.

Perceptive readers might have noticed that most of these arguments can be
generalized. This article is much the same if we replace “Discord” with
“GitHub”, for instance, or “Twitter” or “YouTube”. If your project depends on
proprietary infrastructure, I want you to have a serious discussion with your
collaborators about why. What do your choices mean for the long-term success of
your project and the ecosystem in which it resides? Are you making smart
investments, or just using tools which are popular or that you’re already used
to?

If you use GitHub, consider  [SourceHut](https://sourcehut.org) 3  or
 [Codeberg](https://codeberg.org) . If you use Twitter, consider  [Mastodon](https://joinmastodon.org)  instead. If you use YouTube,
try  [PeerTube](https://joinpeertube.org) . If you use Facebook… don’t.

Your choices matter. Choose wisely.

1. Discord [had to be
sued](https://www.lflegal.com/2021/10/discord-agreement/) to take this
seriously. Updated at 2021-12-28 15:00 UTC: I asked a correspondent of mine who works on accessibility to
comment:
I’ve tried Discord on a few occasions, but haven’t seriously tried to
get proficient at navigating it with a screen reader. I remember finding
it cumbersome to move around, but it’s been long enough since the last
time I tried it, a few months ago, that I couldn’t tell you exactly why.
I think the general problem, though, is that the UI of the
desktop-targeted web app is complex enough that trying to move through
it an element at a time is overwhelming. I found that the same was true
of Slack and Zulip. I haven’t tried Matrix yet. Of course, IRC is great,
because there’s a wide variety of clients to choose from.

However, you shouldn’t take my experience as representative, even though
I’m a developer working on accessibility. As you may recall, I have some
usable vision, and I often use my computer visually, though I do depend
on a screen reader when using my phone. I didn’t start routinely using a
GUI screen reader until around 2004, when I started writing a screen
reader as part of my job. And that screen reader was targeted at
beginners using simple UIs. So it’s possible that I never really
mastered more advanced screen reader usage.

What I can tell you is that, to my surprise, Discord’s accessibility has
apparently improved in recent years, and more blind people are using it now. One
of my blind friends told me that most Discord functionality is very accessible
and several blind communities are using it. He also told me about a group of
young blind programmers who are using Discord to discuss the development of a
new open-source screen reader to replace the current Orca screen reader for
GNOME. ↩︎
2. Discord appears to inflate its participation numbers compared to other services. It shows all users who have ever joined the server, rather than all users who are actively using the server. Be careful not to optimize for non-participants when choosing your tools. ↩︎
3. Disclaimer: I am the founder of SourceHut. ↩︎
