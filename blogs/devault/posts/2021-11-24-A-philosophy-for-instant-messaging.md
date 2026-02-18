---
title: "My philosophy for productive instant messaging"
date: 2021-11-24
url: https://drewdevault.com/2021/11/24/A-philosophy-for-instant-messaging.html
slug: A-philosophy-for-instant-messaging
word_count: 1095
---

We use Internet Relay Chat ( [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) ) extensively at  [sourcehut](https://sourcehut.org)  for
real-time group chats and one-on-one messaging. The IRC protocol is quite
familiar to hackers, who have been using it since the late 80’s. As chat rooms
have become more and more popular among teams of both hackers and non-hackers in
recent years, I would like to offer a few bites of greybeard wisdom to those
trying to figure out how to effectively use instant messaging for their own
work.

For me, IRC is a vital communication tool, but many users of <insert current
instant messaging software fad here> 1  find it frustrating, often to the
point of resenting the fact that they have to use it at all. Endlessly catching
up on discussions they missed, having their workflow interrupted by unexpected
messages, searching for important information sequestered away in a discussion
which happened weeks ago… it can be overwhelming and ultimately reduce your
productivity and well-being. Why does it work for me, but not for them? To find
out, let me explain how I think about and use IRC.

The most important trait to consider when using IM software is that it is
 *ephemeral* , and must be treated as such. You should not “catch up” on
discussions that you missed, and should not expect others to do so, either. Any
important information from a chat room discussion must be moved to a more
permanent medium, such as an email to a mailing list, 2  a ticket filed in a
bug tracker, or a page updated on a wiki. One very productive use of IRC for me
is holding a discussion to hash out the details of an issue, then writing up a
summary up for a mailing list thread where the matter is discussed in more
depth.

I don’t treat discussions on IRC as actionable until they are shifted to another
mode of discussion. On many occasions, I have discussed an issue with someone on
IRC, and once the unknowns are narrowed down and confirmed to be actionable, ask
them to follow-up with an email or a bug report. If the task never leaves IRC,
it also never gets done.  Many invalid or duplicate tasks are filtered out by
this approach, and those which do get mode-shifted often have more detail than
they otherwise might, which improves the signal-to-noise ratio on my bug
trackers and mailing lists.

I have an extensive archive of IRC logs dating back over 10 years, tens of
gigabytes of gzipped plaintext files. I reference these logs perhaps only two or
three times a year, and often for silly reasons, like finding out how many swear
words were used over some time frame in a specific group chat, or to win an
argument about who was the first person to say “yeet” in my logs. I almost never
read more than a couple dozen lines of the backlog when starting up IRC for the
day.

Accordingly, you should never expect anyone to be in the know for a discussion
they were not present at. This also affects how I use “highlights”. 3  Whenever
I highlight someone, I try to include enough context in the message so that they
can understand why they were mentioned without having to dig through their logs,
even if they receive the notification hours later.

*Bad* :

```
<sircmpwn> minus: ping
<sircmpwn> what is the best way to frob foobars?
```

*Good* :

```
<sircmpwn> minus: do you know how to frob foobars?
```

I will also occasionally send someone a second highlight un-pinging them if the
question was resolved and their input is no longer needed. Sometimes I  *will* 
send a vague “ping <username>” example when I actually want them to
participate in the discussion  *right now* , but if they don’t answer immediately
then I will usually un-ping them later. 4

This draws attention to another trait of instant messaging: it is
 *asynchronous* . Not everyone is online at the same time, and we should adjust
our usage of it in consideration of this. For example, when I send someone a
private message, rather than expecting them to engage in a real-time dialogue
with me right away, I dump everything I know about the issue for them to review
and respond to in their own time. This could be hours later, when I’m not
available myself!

*Bad* :

```
<sircmpwn> hey emersion, do you have a minute?
*8 hours later*
<emersion> yes?
*8 hours later*
<sircmpwn> what is the best way to frob foobars?
*8 hours later*
<emersion> did you try mongodb?
```

*Good* : 5

```
<sircmpwn> hey emersion, what's the best way to frob foobars?
<sircmpwn> I thought about mongodb but they made it non-free
*10 minutes later*
<sircmpwn> update: considered redis, but I bet they're one bad day away from making that non-free too
*8 hours later*
<emersion> good question
<emersion> maybe postgresql? they seem like a trustworthy bunch
*8 hours later*
<sircmpwn> makes sense. Thanks!
```

This also presents us a solution to the interruptions problem: just don’t answer
right away, and don’t expect others to. I don’t have desktop or mobile
notifications for IRC. I only use it when I’m sitting down at my computer, and I
“pull” notifications from it instead of having it “push” them to me — that
is, I glance at the client every now and then. If I’m in the middle of
something, I don’t read it.

With these considerations in mind, IRC has been an extraordinarily useful tool
for me, and maybe it can be for you, too. I’m not troubled by interruptions to
my workflow. I never have to catch up on a bunch of old messages. I can
communicate efficiently and effectively with my team, increasing our
productivity considerably, without worrying about an added source of stress. I
hope that helps!

1. Many, many companies have tried, and failed, to re-invent IRC, usually within a proprietary walled garden. I offer my condolences if you find yourself using one of these. ↩︎
2. Email is great. If you hate it you might be [using it wrong](https://useplaintext.email). ↩︎
3. IRC terminology for mentioning someone’s name to get their attention. Some platforms call this “mentions”. ↩︎
4. I occasionally forget to… apologies to anyone I’ve annoyed by doing that. ↩︎
5. I have occasionally annoyed someone with this strategy. If they have desktop notifications enabled, they might see 10 notifications while I fill their message buffer with more and more details about my question. Sounds like a “you” problem, buddy 😉 ↩︎
