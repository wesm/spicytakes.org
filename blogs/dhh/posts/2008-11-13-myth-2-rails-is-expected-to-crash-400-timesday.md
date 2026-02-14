---
title: "Myth #2: Rails is expected to crash 400 times/day"
date: 2008-11-13
url: https://dhh.dk/posts/31-myth-2-rails-is-expected-to-crash-400-timesday
slug: myth-2-rails-is-expected-to-crash-400-timesday
word_count: 421
---


Zed Shaw's [infamous meltdown](http://www.zedshaw.com/rants/rails_is_a_ghetto.html) showed an angry man lashing out at anything and everything. It made a lot of people sad. It made me especially sad because this didn't feel like the same Zed that I had dinner with in Chicago or that I had talked to so many times before. I actually thought he might be in real trouble and in need of real help, but was assured by third party that he wasn't (Zed never replied to my emails after publishing).


But Zed's state of mind isn't really what this is about. This is about the one factual assault he made against Rails that despite being drenched in unbelievable bile somehow still stuck to parts of the public conscious.


**The origin of the claim**

Zed insinuated that it's normal for Rails to restart 400 times/day because Basecamp at one point did this with a memory watcher that would bounce its Mongrels FCGIs when they hit 160MB 250MB. These FCGIs would then gracefully exit after the current request and boot up again. No crash, no lost data, no 500s.


But still an inconvenience, naturally. Nobody likes a memory leak. So I was happy when a patch emerged that fixed it and we could stop doing that. I believe the fix appeared some time in 2006. So even when Zed published his implosion at the end of 2007, this was already ancient history.


Yet lots of people didn't read it like that. I've received more than a handful of reports from people out talking Rails with customers who pull out the Zed rant and say that their consultants can't use Rails because it reboots 400 times/day. Eh, what?


**Fact: Rails doesn't explode every 4 minutes**

So let's make it clear once and for all: Rails doesn't spontaneously combust and restart itself. If we ever have an outright crash bug that can take down an entire Rails process, it's code red priority to get a fix out there.


A Rails application may of course still leak memory because of something done in user space that leaks. Just like an application on any other platform may leak memory.


Update: Zed points out that the leak was occurring while Basecamp was still on FCGI, not Mongrel, which is correct. I don't know how that makes the story any different (it was the fastthread fix that stopped the leak and our minor apps were on Mongrel with leaks too), but let's definitely fix the facts.


*See the [Rails Myths](29-the-rails-myths.html) index for more myths about Rails.*

