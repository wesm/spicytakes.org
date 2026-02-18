---
title: "Members-Only RSS Feeds Now Using HTTP Authentication"
date: 2005-02-11
url: https://daringfireball.net/2005/02/feed_authentication
slug: feed_authentication
word_count: 1017
---


Starting today, there’s a small change in the way this site’s
members-only RSS feeds are handled: access to them now requires
authentication. There are two such feeds: one containing the full
content of every regular article I publish, and one for my [Linked
List](https://daringfireball.net/linked/) linklog.


(The regular (free) RSS feed for this site, which contains a brief
summary of each article, is unaffected by these changes.)


Previously, the members-only status for these feeds was enforced by
way of membership keys — 9-character tokens placed at the end of
the feed URL. For example, if your key was “123456789”, the URL you
could use to subscribe to the full-content RSS feed was:


```
http://daringfireball.net/feeds/rss/123456789

```


And your URL for the Linked List feed would be:


```
http://daringfireball.net/linked/rss/123456789

```


I implemented it this way for a few reasons, but mainly because it
was easier than using HTTP authentication. Easier both for me,
development-wise, and easier for members, in terms of actually
subscribing to the feeds. Last June when these feeds debuted,
several popular RSS aggregators didn’t support HTTP authenticated
feeds, or, if they did, it wasn’t obvious how to subscribe to
such feeds.


The downside to this scheme, however, is that all of the information
needed to access the feeds was available in the URL itself. And with
public web-based aggregators such as [Bloglines](http://bloglines.com/), it’s become
[trivial](http://www.bloglines.com/search?t=1&r=0&q=daring%20fireball) for non-members to find and use these URLs using
other people’s membership keys.


I noticed this months ago, and wrote to Bloglines to ask if there
was anything I could do to keep these feeds truly
private. Mark Fletcher responded a short while later with the answer:
“Currently the only way that a feed is marked private is if it
contains a username/password used for HTTP authentication.”


So, that’s what I’m using henceforth.


Most popular Mac RSS aggregators — including [NetNewsWire 2.0](http://ranchero.com/netnewswire/) (technically still a public “beta”, but much more popular than
NetNewsWire 1.x), [PulpFiction](http://freshsqueeze.com/products/pulpfiction/), and [NewsFire](http://www.newsfirerss.com/) — now
support HTTP authentication easily, by prompting you for a username
and password similar to how a web browser would. (**Update**: This
feature is only available in NetNewsWire 2.0b22 or later; older 2.0
betas will not prompt you with a dialog box for authentication.)


The old-style feed URLs will continue working for another week or
so, but after that, authentication will be mandatory. The new feed
URLs are the same as the old ones, but without the keys at the end.


Full-content feed:


```
http://daringfireball.net/feeds/rss

```


Linked List feed:


```
http://daringfireball.net/linked/rss

```


The first time you refresh after changing your subscription URLs to
the above, your aggregator should prompt you for a username and
password. You only have to enter this info once. Your username is
the email address you used when you signed up for your Daring
Fireball membership. (If you paid by PayPal, for example, it’s
probably whatever email address you use for PayPal transactions.)
Your password is your membership key.


That’s it.


**Important**: If you’re using an aggregator that *doesn’t* prompt
you for a username and password — which will be the case for any of
you still using NetNewsWire 1.x, or if you’re using Bloglines — you
can still subscribe to these feeds, but to do so, you need to put your authentication credentials in the URL, in the following format:


```
http://username:[email protected]/path

```


This embedding-your-credentials-in-the-URL technique works with any
resource using HTTP authentication — it’s not specific to Daring
Fireball.


However, and this is important, because the ‘@’ symbol is used to
separate the username/password from the domain name in the URL, you
can’t use the ‘@’ symbol as part of your username. Instead, you’ll
need to URL encode it as ‘`%40`’.


So, if your email address is “[[email protected]](https://daringfireball.net/cdn-cgi/l/email-protection)”, and your
membership key is “123456789”, you can subscribe to the Linked List
feed using this URL:


```
http://address%40example.com:[email protected]/linked/rss

```


And likewise for the full-content feed:


```
http://address%40example.com:[email protected]/feeds/rss

```


If you’re confused, I’m sorry. This is why I tried to keep it simple
last year by simply having members put their keys at the end of the
feed URLs.


To review:

- If you’re using a modern RSS aggregator such as NetNewsWire 2.0,
PulpFiction, or NewsFire, you can simply remove your key from the
end of your subscription URL, and your aggregator will prompt you
for your username and password with a nice dialog box. You don’t
need to worry about encoding the ‘@’ in your email address.
- If you’re using NetNewsWire 1.0, or Bloglines, or any other
aggregator for which the above doesn’t result in your being
prompted for a username and password, then you need to subscribe
using the `http://username:[email protected]/path` format.
- If you’ve lost / forgotten your key, you can retrieve it with
the form [here](https://daringfireball.net/members/keys)
- If you know your key, but don’t remember which email address
you used to join, you can have a reminder sent using the form
[here](https://daringfireball.net/members/forgotten_email)
- If you need further assistance, you can send email to
[support@daringfireball.net](mailto:support@daringfireball.net)


My apologies for the inconvenience of all this.


## A Brief Message to Those of You Using Bootlegged Membership Keys


I don’t think the bootlegging/swiping/filching of these members-only
feeds is a big deal. If it hadn’t gotten out of hand, I would have
been happy to tolerate it for the foreseeable future. However, it
*has* gotten out of hand.


There is no members-only content at Daring Fireball; these feeds are
merely a members-only means of accessing the same content that
everyone can access for free via the web site. They’re a convenience
I offer to members as a token of my thanks for supporting Daring
Fireball.


If you’re determined to keep using these feeds for free, I’m sure
you’ll find a way, and I won’t stop you. But a one-year [membership
to Daring Fireball costs just $19](https://daringfireball.net/members/), which gets you legitimate
access to these feeds. That works out to less than $1.60 a month —
which isn’t much to you, but, in the aggregate, means a lot to me.



| **Previous:** | [Subscription Small Print](https://daringfireball.net/2005/02/subscription_small_print) |
| **Next:** | [Marking Subscriptions as ‘Private’ in Bloglines](https://daringfireball.net/2005/02/bloglines) |


PreviousNext