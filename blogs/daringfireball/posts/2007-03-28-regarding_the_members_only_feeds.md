---
title: "Regarding the Members-Only Feeds"
date: 2007-03-28
url: https://daringfireball.net/2007/03/regarding_the_members_only_feeds
slug: regarding_the_members_only_feeds
word_count: 742
---


Good time for an update and reminder about the members-only XML feeds here at Daring Fireball.


## This Morning’s Outage


My MySQL server was offline this morning from about 7 - 10 am ET. (It was a silly mistake on my part, and should be fixed now.)


During this time, anyone with a Daring Fireball membership who tried to access their password-protected feeds received an error that their username and password weren’t valid. This was simply a side effect of the database not being available, and was not related to the current membership campaign. My apologies for the interruption and for any confusion.


Speaking of memberships, sign-ups were also not working properly during this window. If you tried to sign up or renew your membership this morning, and it doesn’t seem to have worked, stand by for another hour or so. I’ll create and update those memberships manually after posting this article.


## About the Feeds


The members-only feed system at Daring Fireball has proven to be a very popular feature — last I checked, somewhere around 80-85 percent of active members are subscribed to at least one of these feeds.


But it’s also proven to be a source of confusion for readers new to Daring Fireball, who are accustomed to sites where everything appears in the “free” RSS feed. (*“When I look at your web site, I see a bunch of new links, but your RSS feed hasn’t updated in days.”*) So, to answer this recurring FAQ, here’s how the feeds work:

- The main feed, which is freely available to anyone who wishes to subscribe, contains the headlines and brief excerpts of each full article that I write. It does not contain any of the links from my Linked List.
- Daring Fireball members each receive a unique “key” which they can use as a password (using their email address as the username) to access additional feeds. One contains the entire content of each full article; one contains each item posted to the Linked List; and, my personal favorite, a “combination” feed that contains the Linked List items *and* the full content of each article. The combination feed more or less contains everything posted to the front page of Daring Fireball.


More information, including the URLs for each of these feeds, is available on my [Feeds page](http://daringfireball.net/feeds/).


If you’re already a member and have forgotten or lost your key(s), you can have them sent to you via email [using this form](http://daringfireball.net/members/keys).


## Google Reader


The biggest downside to these password-authenticated feeds is that they do not work with Google Reader. Google Reader does not support HTTP authentication; if there were some way to work around this, I would, but it’s up to Google.


Back in 2004, rather than using HTTP authentication, the feeds worked by using the secret member key as part of the URL. Each member would subscribe to a feed that looked like `http://daringfireball.net/feeds/rss/*secret_key_here*`. The advantage to this scheme is that it worked with web-based feed readers that don’t support true authentication. (You would never want to do this with a feed that contained genuinely private or sensitive information, but it was just fine for Daring Fireball, where all the content is freely available for everyone on the web site.)


The problem with this scheme is that many web-based feed readers default to making the feed URLs you’re subscribed to public. There were more non-members accessing these feeds via “found” URLs than there were members, so I switched to using real authentication.


## Expiration Reminders


Lastly, a word of warning. A few weeks before a membership is due to expire, the members-only feeds are configured to insert a personalized message into the feeds themselves with a brief reminder about the pending expiration.


I think this is pretty clever, if I do say so — and far less intrusive than sending reminders via email. However, a few readers have emailed to say that the notices gave them quite a jolt: when they checked their feed reader and saw a new item in their Daring Fireball feed entitled “[Reminder for *Your Name Here*]: Daring Fireball membership expires on April 20”, they briefly think that I’ve posted an article to Daring Fireball with their name in the title, reminding them to renew.


My apologies for any skipped heartbeats.



| **Previous:** | [Creating New Text Files From the Finder’s Contextual Menu](https://daringfireball.net/2007/03/new_text_files_contextual_menu) |
| **Next:** | [The New Daring Fireball T-Shirts](https://daringfireball.net/2007/03/new_daring_fireball_tshirts) |


PreviousNext