---
title: "Tips for analyzing logs"
date: 2022-12-07
url: https://jvns.ca/blog/2022/12/07/tips-for-analyzing-logs/
slug: tips-for-analyzing-logs
word_count: 1144
---


Hello! I’ve been working on writing a zine about debugging for a while now
(we’re getting close to finishing it!!!!), and one of the pages is about
analyzing logs. I [asked for some tips on Mastodon](https://mastodon.social/@b0rk/109473352725574776)
and got WAY more tips than could fit on the page, so I thought I’d write a
quick blog post.


I’m going to talk about log analysis in the context of distributed systems
debugging (you have a bunch of servers with different log files and you need to
work out what happened) since that’s what I’m most familiar with.


### search for the request’s ID


Often log lines will include a request ID. So searching for the request ID
of a failed reques will show all the log lines for that request.


This is a GREAT way to cut things down, and it’s one of the first helpful tips
I got about distributed systems debugging – I was staring at a bunch of graphs
on a dashboard fruitlessly trying to find patterns, and a coworker gave me the
advice (“julia, try looking at the logs for a failed request instead!”).  That
turned out to be WAY more effective in that case.


### correlate between different systems


Sometimes one set of logs doesn’t have the information you need, but you can
get that information from a different service’s logs about the same request.


If you’re lucky, they’ll both share a request ID.


More often, you’ll need to manually piece together context from clues and the timestamps of the request.


This is really annoying but I’ve found that often it’s worth it and gets me a key piece of information.


### beware of time issues


If you’re trying to correlate events based on time, there are a couple of things to be aware of:

- sometimes the time in a logging system is based on the time the log was
**ingested**, not the time that the event actually happened. Sometimes you
have to write a date parser to get the actual time the event happened.
- different machines can have slightly skewed clocks


### log lines for the same request can be very far apart


Especially if a request takes a long time (maybe it took 5 minutes because of a
long timeout!), the log lines for the request might be much more spread out
than you expected. You can accumulate many thousands of log lines in 5 minutes!


Searching for the request ID really helps with this – it makes it harder to
accidentally miss a log entry with an important clue.


Also, log lines can occasionally get completely lost if a server dies.


### build a timeline


Keeping all of the information straight in your head can get VERY confusing, so
I find it helpful to keep a debugging document where I copy and paste bits of
information.


This might include:

- key error messages
- links to relevant dashboards / log system searches
- pager alerts
- graphs
- human actions that were taken (“right before this message, we restarted the load balancer…”)
- my interpretation of various messages (“I think this was caused by…”)


### reformat them into a table


Sometimes I’ll reformat the log lines to just print out the information I’m
interested in, to make it easier to scan. I’ve done this on the command line
with a simple `awk` command:


```
cat ... | awk '{print $5 - $8}'

```


but also with fancy log analysis tools (like Splunk) that let you make a table on the web


### check that a “suspicious” error is actually new


Sometimes I’ll notice a suspicious error in the logs and think “OH THERE’S THE
CULPRIT!!!”. But when I search for that message to make sure that it’s actually
new, I’ll find out that this error actually happens constantly during normal
operation, and that it’s completely unrelated to the (new) situation that I’m
dealing with.


### use the logs to make a graph


Some log analysis tools will let you turn your log lines into a graph to detect
patterns.


You can also make a quick histogram with `grep` and `sort`. For example  I’ve
often done something like:


```
grep -o (some regex) | sort | uniq -c | sort -n

```


to count how many of each line matching my regular expression there are


### filter out irrelevant lines


You can remove irrelevant lines with `grep` like this:


```
cat file | grep -v THING1 | grep -v THING2 | grep -v THING3 | grep -v THING4

```


Or if your log system has some kind of query language, you can search for `NOT THING1 AND NOT THING2 ...`


### find the first error


Often an error causes a huge cascade of related errors. Digging into the
later errors can waste a lot of your time – you need to start by finding the
**first** thing that triggered the error. Often you don’t need to understand
the exact deals of why the 15th thing in the error cascade failed, you can just
fix the original problem and move on.


### scroll through the log really fast


If you already have an intuition for what log lines for this service *should*
normally look like, sometimes scrolling through them really fast will reveal
something that looks off.


### turn the log level up (or down)


Sometimes turning up the log level will give you a key error message that
explains everything.


But other times, you’ll get overwhelmed by a million irrelevant messages
because the log level is set to `INFO`, and you need to turn the log level down.


### put it in a spreadsheet/database


I’ve never tried this myself, but a couple of people suggested copying parts of
the logs into a spreadsheet (with the timestamp in a different column) to make
it easier to filter / sort.


You could also put the data into SQLite or something (maybe with [sqlite-utils](https://sqlite-utils.datasette.io/en/stable/)?) if you want to
be able to run SQL queries on your logs.


### on generating good logs


A bunch of people also had thoughts on how to **output** easier-to-analyze
logs. This is a bigger topic than a few bullet points but here are a few quick
things:

- use a standard schema/format to make them easier to parse
- include a transaction ID/request ID, to make it easier to filter for all lines related to a single transaction/request
- include relevant information. For example,  “ERROR: Invalid msg size” is less helpful than “ERROR: Invalid msg size. Msg-id 234, expected size 54, received size 0”.
- avoid logging personally identifiable information
- use a logging framework instead of using `print` statements (this helps you have things like log levels and a standard structure)


### that’s all!


Let me know on Twitter/Mastodon if there’s anything I missed! I might edit this to add a
couple more things.
