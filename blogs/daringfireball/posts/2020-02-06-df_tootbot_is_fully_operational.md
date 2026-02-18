---
title: "The DF Tootbot Is Once Again Fully Operational"
date: 2020-02-06
url: https://daringfireball.net/2020/02/df_tootbot_is_fully_operational
slug: df_tootbot_is_fully_operational
word_count: 1138
---


A brief housekeeping note. In early November, I moved this website to a new server. It had been at the old server since 2007. One small thing that broke during the move is the script I use to automatically tweet links to new DF posts from [the @daringfireball Twitter account](https://twitter.com/daringfireball) — the DF Tootbot.


What broke is fairly technical, so I’ll try to make this short. The basic gist of how the script works:

1. Read the DF RSS feed to get a list of all current posts.
2. Go through each post in the feed and see if there are entries that (a) haven’t yet been tweeted, and (b) are at least 5 minutes old. (The reason for (b) is so that I have a few minutes after initially publishing to fix any egregious mistakes or typos.)
3. Upon finding an entry that meets both criteria in #2, tweet it, using the entry’s title and URL as the text of the tweet.
4. Add that DF post to a history log so that it won’t get tweeted again.


The script runs once per minute as a cron job. That’s it.


What broke when I moved servers was the history log. When I first wrote the script 10+ years ago, I used a database, cleverly thinking, “*If this Twitter thing is here to stay, I’ll eventually tweet tens of thousands of posts, so I should use a database so lookups don’t get slow and the whole thing continues to run fast years from now.*” The database I chose, unfortunately, is one that sometimes changes its underlying file format with major version updates.1 There were *a lot* of major version updates to Perl in the years since I last moved servers.


What I could have done is just start over with a new history log on the new server, and manually fill the new database with the last few weeks of entries. For the purposes of tweeting new entries from the RSS feed, there’s no reason to keep a full historical log. The script just needs to know which *recent* articles — articles still in the feed — have already been tweeted.


It bothered me that the script was using a database at all. It bothered me because the database wasn’t something I could just open in BBEdit and inspect and edit by hand. I’m a text file guy, [as you may know](https://daringfireball.net/projects/markdown/). Because here’s the thing: reading a simple text file log with tens of thousands of lines is really really fast on a modern computer. It would have been more than fast enough 10 years ago, and it’s much faster today.


I wrote a test script and ran it against a 53 MB text file log with *1 million lines*. It ran in a blink of an eye. A fraction of a second. I hope to write Daring Fireball for a long time to come, but I really doubt I have a million posts in me.


A database was overkill. [I ran afoul of Donald Knuth’s well-known axiom](https://en.wikiquote.org/wiki/Donald_Knuth):


> Programmers waste enormous amounts of time thinking about, or
> worrying about, the speed of noncritical parts of their programs,
> and these attempts at efficiency actually have a strong negative
> impact when debugging and maintenance are considered. We should
> forget about small efficiencies, say about 97% of the time:
> premature optimization is the root of all evil.


So, I decided I should rewrite that part of the DF Tootbot to do what it should have done all along: use a simple human-readable text file for the history log. There were a few other changes I wanted to make, too — like switching from DF’s RSS feed to the [JSON feed](https://jsonfeed.org/) as the source for new articles, and supporting Twitter’s 280-character limit.


In the meantime, I had a copy of the old version of the script on my Mac that I could run manually. Three months of procrastination later, I finally spent Monday writing the new version and getting it running on the new DF server. [This](https://twitter.com/daringfireball/status/1224441011524341760) was the first tweet posted by the new Tootbot.2


In the interim, during the previous three months when @daringfireball tweets were only being triggered by me manually, the time between when I posted new items to Daring Fireball and when they got tweeted was, to put it mildly, erratic. Manually doing anything that should be automated is a bad idea for anyone, but it’s a particularly bad idea for someone with a strong tendency to think about only one thing at a time and pretty much forget everything else.


---


So why do I even bother with my own custom script for posting these tweets? Indeed, there are [many](https://ifttt.com/) [services](https://dlvr.it/) one can use for posting new items from a blog to a Twitter account.


I like having control over such things. Shocker, I know. For example, I want complete control over the exact text of the tweets. What happens, for example, when a DF post has a headline that’s too long to fit in a tweet? In that case, I want the headline to be truncated as elegantly as possible, at a whole word, with an ellipsis added to indicate the truncated words, and *inside* any double or single quotation marks that end the headline. With Twitter’s 2017 change from 140 characters to 280 as the upper limit of a tweet, that’s not common — [but it can happen](https://twitter.com/daringfireball/status/1225579433177673729).


---


For those of you who don’t follow [the @daringfireball Twitter account](https://twitter.com/daringfireball), consider it. It’s a great way to see when something new or updated has been posted to DF, and with Twitter’s app, you can even get notifications of new items. (Go to the @daringfireball account profile and tap the little bell icon — you can use this to get per-account Twitter notifications from anyone.)


For those of you who do follow @daringfireball, I apologize for the erratic posting schedule these last three months. It should be back to normal now, and for the foreseeable future.


---

1. Perl nerds only: I was using `DB_File` to [tie a hash with a Berkeley DB](https://perldoc.perl.org/DB_File.html). I have never used `DB_File` before or since, and in hindsight really can’t believe that I used it for this. ↩︎
2. Keen observers will note a slight formatting change. The old Tootbot tweeted `title + ": " + url` (title and url separated by a colon and space); the new Tootbot tweets `title + "\n" + url` (title and url separated by a newline). This new format is a better compromise between how Twitter itself and third-party clients like [Tweetbot](https://tapbots.com/tweetbot/) and [Twitterrific](https://twitterrific.com/) — both much-used by DF readers — display tweets. ↩︎︎



| **Previous:** | [My 2019 Apple Report Card](https://daringfireball.net/2020/02/my_2019_apple_report_card) |
| **Next:** | [Locations of Media Files in MacOS 10.15 Catalina](https://daringfireball.net/2020/02/catalina_media_file_locations) |


PreviousNext