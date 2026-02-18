---
title: "Analyzing HN moderation & censorship"
date: 2017-09-13
url: https://drewdevault.com/2017/09/13/Analyzing-HN.html
slug: Analyzing-HN
word_count: 2455
---

[Hacker News](https://news.ycombinator.com)  is a popular
“ [hacker](http://www.catb.org/jargon/html/H/hacker.html) ” news board. One thing
I love about HN is that the moderation generally does an excellent job. The site
is free of spam and the conversations are usually respectful and meaningful (if
pessimistic at times). However, there is always room for improvement, and
moderation on Hacker News is no exception.

**Notice** : on 2017-10-19 this article was updated to incorporate feedback the
Hacker News moderators sent to me to clarify some of the points herein. You may
view a diff of these changes
 [here](https://github.com/SirCmpwn/sircmpwn.github.io/commit/553d051c84a4631c3bd3264a437dfbc6c9807d13) .

For some time now, I’ve been scraping the HN API and website to learn how the
moderators work, and to gather some interesting statistics about posts there
in general. Every 5 minutes, I take a sample of the front page, and every 30
minutes, I sample the top 500 posts (note that HN may return fewer than this
number). During each sample, I record the ID, author, title, URL, status
(dead/flagged/dupe/alive), score, number of comments, rank, and compute the rank
based on  [HN’s published algorithm](https://news.ycombinator.com/item?id=231209) .
A note is made when the title, URL, or status changes.

The information gathered is publicly available at
 [hn.0x2237.club](https://hn.0x2237.club)  (sorry about the stupid domain, I just
picked one at random). You can search for most posts here going back to
2017-04-14, as well as view recent
 [title](https://hn.0x2237.club/title-changes)  and
 [url](https://hn.0x2237.club/url-changes)  changes or  [deleted
posts](https://hn.0x2237.club/deleted) 
( [score>10](https://hn.0x2237.club/deleted-10) ). Raw data is available as JSON
for any post at  `https://hn.0x2237.club/post/:id/json` . Feel free to explore the
site later, or  [its shitty code](https://git.sr.ht/~sircmpwn/hnstats) . For now,
let’s dive into what I’ve learned from this data.

### Tools HN mods use

The main tools I’m aware of that HN moderators can use to perform their duties
are:

* Editing link titles or URLs
* Influencing story rank via “downweighting” or “burying”
* Deleting or “killing” posts
* Detaching off-topic or rulebreaking comment threads from their parents
* Shadowbanning 
misbehaving users
* Banning misbehaving users (and telling them)

The moderators emphasize a difference between deleting a post and killing a
post. The former, deleting a post, will remove it from all public view like it
had never existed, and is a tool used infrequently. Killing a post will mark it
as [dead] so it doesn’t show up on the post listing.

Influencing a post’s rank can also be done through several means of varying
severity. “Burying” a post will leave a post alive, but plunge it in rank.
“Downweighting” is similar, but does not push its rank as far.

There are also automated tools for detecting spam and  voting
rings , as well as automated de-emphasizing of posts based on certain
 secret
keywords  and controls to prevent flamewars. Automated tools on Hacker
News are used to downweight or kill posts, but never to bury or delete them.
Dan spoke about these tools and their usage for me:

> Of these four interventions (deleting, killing, burying, and downweighting),
> the only one that moderators do frequently is downweighting. We downweight
> posts in response to things that go against the site guidelines, such as when a
> submission is unsubstantive, baity or sensational. Typically such posts remain
> on the front page, just at a lower rank. We bury posts when they’re dupes,
> but rarely otherwise. We kill posts when they’re spam, but rarely
> otherwise. […] We never delete a post unless the author asks us to.

Dan also further clarified the difference between dead and deleted for me:

> The distinction between ‘dead’ and ‘deleted’ is important. Dead posts
> are different from deleted ones in that people can still see them if
> they set ‘showdead’ to ‘yes’ in their profile. That way, users who
> want a less moderated view can still see everything that has been
> killed by moderators or software or user flags. Deleted posts, on the
> other hand, are erased from the record and never seen again. On HN,
> authors can delete their own posts for a couple hours (unless they are
> comments that have replies). After that, if they want a post deleted
> they can ask us and we usually are happy to oblige.

Moderators can also artificially influence rank upwards - one way is by inviting
the user to re-submit a post that they want to give another shot at the front
page. This gives the post a healthy upvote to begin with and prevents it from
being flagged. The moderators invited me to re-submit this very article using
this mechanism on 2017-10-19.

Banning users is another mechanism that they can use. There are two ways bans
are typically applied around the net - telling users they’ve been banned, and
keeping it quiet. The latter - shadowbanning - is a useful tool against spammers
and serial ban evaders who might otherwise try to circumvent their ban. However,
it’s important that this does  *not*  become the first line of defense against
rulebreaking users, who should instead be informed of the reason for their ban
so they have a chance to reform and appeal it. Here’s what Dan has to say about
it:

> Shadowbanning has proven to still be useful for spammers and trolls
> (i.e. when a new account shows up and is clearly breaking the site
> guidelines off the bat). Most such abuse is by a relatively small
> number of users who create accounts over and over again to do the same
> things. When there’s evidence that we’ve repeatedly banned someone
> before, I don’t feel obliged to tell them we’re banning them again.
> […] When we’re banning an established account, though, we post a comment
> saying so, and nearly always only after warning that user beforehand. Many such
> users had no idea they were breaking the site guidelines and are
> quite happy to improve their posts, which is a win for everyone.

Dan also shared a link to search for comments where moderators have explained
to users why they’ve been banned. Of course, this doesn’t include users who were
banned without explanation, or that use slightly different language:

[dang’s bans](https://hn.algolia.com/?query=by:dang%20we%20banned&sort=byDate&dateRange=all&type=comment&storyText=false&prefix&page=0)

[sctb’s bans](https://hn.algolia.com/?query=by:sctb%20we%20banned&sort=byDate&dateRange=all&type=comment&storyText=false&prefix=false&page=0)

## Data-based insights

Here’s an example of a fairly common moderator action:

[This post](https://hn.0x2237.club/post/15217697)  had its title changed at
around 09-11-17 12:10 UTC, and had the rank artificially adjusted to push it
further down the front page. We can tell that the drop was artificial just by
correlating it with the known moderator action, but we can also compare it
against the computed base rank:

Note however that the base rank is often wildly different from the rank observed
in practice; the factors that go into adjusting it are rather complex. We can
also see that despite the action, the post’s score continued to increase, even
at an accelerated pace:

This “title change and derank” is a fairly common action - here are some more
examples from the past few days:

[Betting on the Web - Why I Build PWAs](https://hn.0x2237.club/post/15219154)

[Silicon Valley is erasing individuality](https://hn.0x2237.club/post/15210767)

[Chinese government is working on a timetable to end sales of fossil-fuel cars](https://hn.0x2237.club/post/15208565)

Users can change their own post titles, which I’m unable to distinguish from
moderator changes. However, correlating them with a strange change in rank is
generally a good bet. Submitters also generally will edit their titles earlier
rather than later, so a later change may indicate that it was seen by a
moderator after it rose some distance up the page.

I also occasionally find what seems to be the opposite - artificially bumping a
post further up the page. Here’s two examples:
 [15213371](https://hn.0x2237.club/post/15213371)  and
 [15209377](https://hn.0x2237.club/post/15209377) . Rank influencing in either
direction also happens without an associated title or URL change, but
automatically pinning such events down is a bit more subtle than my tools can
currently handle.

Moderators can also delete a post or indicate it as a dupe. The latter can be
(and is) detected by my tools, but the former is indistinguishable from the user
opting to delete posts themselves. In theory, posts that are deleted  *after*  the
author is no longer allowed to could be detected, but this happens rarely and my
tools don’t track posts once they get old enough.

### Flagging

The users have some moderation tools at their disposal, too - downvotes,
flagging, and vouching. When a comment is downvoted, it is moved towards the
bottom of the thread and is gradually colored grayer to become less visible, and
can be reversed with upvotes. When a comment gets enough flags, it is removed
entirely unless you have showdead enabled in your profile. Flagged posts are
downweighted or killed when enough flags accumulate. These posts are moved to
the bottom of the ranked posts even if you have showdead enabled, and can also
be seen in /new. Flagging can be reversed with the vouch feature, but flagged
stories are almost never vouched back into existence.

**Note** : detection of post flagged status is very buggy with my tools. The API
exposes a boolean for dead posts, so I have to fall back on scraping to
distinguish between different kinds of dead-ness. But this is pretty buggy, so I
encourage you to examine the post yourself when browsing my site if in doubt.

### Are these tools abused for censorship?

Well, with all of this data, was I able to find evidence of censorship? There
are two answers: yes and maybe. The “yes” is because users are  *definitely* 
abusing the flagging feature. The “maybe” is because moderator action leaves
room for interpretation. I’ll get to that later, but let’s start with flagging
abuse.

#### Censorship by users

The threshold for removing a story due to flags is rather low, though I don’t
know the exact number. Here are some posts whose flags I consider questionable:

[Harvey, the Storm That Humans Helped Cause](https://hn.0x2237.club/post/15129859)  (23 points)

[ES6 imports syntax considered harmful](https://hn.0x2237.club/post/15116132)  (12 points)

[White-Owned Restaurants Shamed for Serving Ethnic Food](https://hn.0x2237.club/post/14415411)  (33 points)

[The evidence is piling up – Silicon Valley is being destroyed](https://hn.0x2237.club/post/14152602)  (27 points)

A good place to discover these sorts of events is to browse hnstats for posts
deleted with a score  [>10 points](https://hn.0x2237.club/deleted-10) . There are
also occasions where the flags seem to be due to a poor title, which is a
fixable problem for which flagging is a harsh solution:

[Poettering downvoted 5 (at time of this writing) times](https://hn.0x2237.club/post/14679207)

[Germany passes law restricting free speech on the internet](https://hn.0x2237.club/post/14676296)

The main issue with flags is that they’re often used as an alternative to the
HN’s (by design) lack of a downvoting feature. HN also gives users no guidelines
on  *why*  they should flag posts, which mixes poorly with automated removal of a
post given enough flags.

#### Censorship by moderators

Moderator actions are a bit more difficult to judge. Moderation on HN is a black
box - most of the time, moderators don’t make the reasoning behind their actions
clear. Many of their actions (such as rank influence) are also subtle and easy
to miss. Thankfully they are often receptive to being asked why some moderation
occurred, but only as often as not.

Anecdotally, I also find that moderators occasionally moderate selectively, and
keep quiet in the face of users asking them why. Notably this is a problem for
 paywalled  articles, which are  [against the
rules](https://news.ycombinator.com/newsfaq.html)  but are often allowed to
remain.

Dan sent me a response to this section:

> [It’s true that we don’t explain our actions], but mostly because it would be
> hopeless to try. We could do that all day and still not make everything clear,
> because the quantity is overwhelming and the cost of a high-quality explanation
> is steep. Moreover the experiment would be impossible to run because one
> would die of boredom long before reaching 100%. Our solution to this
> conundrum is not to try to explain everything but to answer specific
> questions as best we can. We don’t answer every question, but that’s
> mostly because we don’t see every question. If people ask us things on
> HN itself, odds are we won’t see it (also, the site guidelines ask
> users not to do this, per ([our
> guidelines](https://news.ycombinator.com/newsguidelines.html)). If they
> [email us](mailto:hn@ycombinator.com), the probability of a
> response approaches 1.

I can attest personally to success reaching out to  [hn@ycombinator.com](mailto:hn@ycombinator.com)  for
clarification and even reversal of some moderator decisions, though at a
response ratio further from 1 than this implies. That being said, I don’t think
that private discourse between the submitter and the moderators is the only
solution. Other people may be invested in the topic, too - users who upvoted the
story might not notice its disappearance, but would like more attention drawn to
the topic and enjoy more discussion. Commenters are even more invested in the
posts. The submitter is not the only one whoses interests are at stake. This is
even more of a problem for posts which are moderated via user flags - the HN
mods are pretty discretionate but users are much less so.

Explaining every action is not necessary - I don’t think anyone needs you to
explain why someone was banned when they were submitting links to earn money at
home in your spare time. However, I think a public audit log of moderator
actions would go a long way, and could be done by software - avoiding the need
to explain everything. I envision a change to your UI for banning users or
moderating posts with that adds a dropdown of common reasons and a textbox for
further elaboration when appropriate - then makes this information appear on
/moderation.

### Conclusions

I should again emphasize that most moderator actions are benign and agreeable.
They do a great job on the whole, but striving to do even better would be
admirable. I suggest a few changes:

* Make a public audit log of moderation activity, or at least reach out to me to
see what small changes could be done to help improve my statistics gathering.
* Minimize use of more subtle actions like rank influence, and when used,
* More frequently leave comments on posts where moderation has occurred
explaining the rationale and opening an avenue for public discussion and/or
appeal.
* Put flagged posts into a queue for moderator review and don’t remove posts
simply because they’re flagged.
* Consider appointing one or two moderators from the community, ideally people
with less bias towards SV or startup culture.

Hacker News is a great place for just that - hacker news. It has been for a long
time and I hope it continues to be. Let’s work together on running it
transparently to the benefit of all.
