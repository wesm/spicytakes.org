---
title: "Ruby Performance Revisited"
date: 2006-09-12
url: https://www.joelonsoftware.com/2006/09/12/ruby-performance-revisited/
word_count: 902
---


Jack Herrington emailed me, in reference to the issue of Ruby on Rails performance, to write:


> I agree with you about unicode. And I agree that Rails needs some time to evolve. But I use a bunch of web technologies and they all have issues.
> I do disagree with the scalability statements. I don’t think Rails has scaling issues that can’t be gotten around, and which don’t have cousins in other technologies.
> What I would ask is that you at least put some framing around your scalability comments. Tell us about the scalability problems. Even if we don’t fix it for you, the entire community can gain from your experience.


David Heinemeier Hansson wrote:


> Rails is for the vast majority of web applications Fast Enough. We got sites doing millions of dynamic page views per day. If you end up being with the Yahoo or Amazon front page, it’s unlikely that an off-the-shelve framework in ANY language will do you much good. You’ll probably have to roll your own. But sure, I’d like free CPU cycles too. I just happen to care much more about free developer cycles and am willing to trade the former for the latter.


By way of clarification, I’m not concerned with **Rails** performance, I’m concerned with Ruby performance, and here’s why.


I’ve seen lots of comparisons of Ruby’s performance with bytecode languages like Java which I would consider slow, and I see a lot of reports of performance claiming Ruby is [10x slower](http://www.pankaj-k.net/archives/2005/11/ruby_or_java_a.html), [50x slower](http://fishbowl.pastiche.org/2004/10/28/ruby_performance), etc. Besides the random blogobuzz, Ruby comes pretty darn close to dead last in the [Computer Language Shootout Benchmarks](http://shootout.alioth.debian.org/).


Without knowing much about the implementation of Ruby, I would guess that the biggest issue is around late binding and especially duck typing, which prevents type inference or strong typing, which means that function calls will always be slow because you can never get something compiled down to the point where a function call is just a single [CALL](http://www.penguin.cz/~literakl/intel/c.html#CALL) instruction (on x86)… you always have to be exploring the object, possibly even scanning a hash table to find the function you want to call. Calling methods on objects is really, really, really, really common, especially in pure OO languages, and that bit of the code needs to get down to at least a CALL indirect on the CPU for Ruby to offer the same performance as languages where the type of the object can be determined at compile time and therefore the instruction where you’re jumping to can be gotten either at compile time (like in C) or with a single indirection through a single vtable (like in C++).


I understand the philosophy that developer cycles are more important than cpu cycles, but frankly that’s just a bumper-sticker slogan and not fair to the people who are complaining about performance. Even though our product, FogBugz, seems like something that should be perfect for Ruby on Rails, we have several parts of code where performance is extremely important. In FogBugz 6 there’s one place where we need to do literally millions of calculations to display a single chart on a single web page. We have gotten it down to 3 seconds or so in our current development environment with a lot of optimization, but frankly with a duck-typed function call I really don’t think we could do it before the web browser gave up and timed out and the sun cooled down a couple of degrees. We also have to scan incoming email messages for spam using Bayesian filtering. This is compute-intensive can take 1 sec. per message. Receiving one email per second is not unreasonable for many of our customers so we are very close to being CPU pegged. That is using a language which we know to be orders of magnitude faster than Ruby at this type of code. We would be absolutely dead on Ruby.


Even classic, simple CRUD applications — the kind of application that basically just shows you a table from a database and gives you operations to add, delete, and edit records — often discover somewhere down the line that there’s something enormously computationally intensive that they want to do, for example, blog software might want to add Bayesian filtering to eliminate spam from comments. This is where you suddenly realize that if your language of choice is 10x slower than the competition, you may be simply unable to add that feature, or you may have to call out to another language (with all the marshalling overhead that implies).


This doesn’t apply to everyone, but when people say they have performance problems with Ruby or that they just need to be able to run code faster than the core Ruby language engine can run it, it doesn’t help to have Ruby advocates singing hymns about developer cycles vs. CPU cycles. Even if you aren’t doing compute-intensive things, if you find yourself needing to buy 100 servers instead of 10 servers, you may suddenly revisit the whole developer cycle vs. CPU cycle equation.


I understand that there are plans for Ruby to address performance with some kind of bytecode compiler and that will be nice. When these things happen and when Ruby starts getting competitive benchmarks it will be a lot more appropriate for a lot more types of applications. In the meantime I stand by my claim that it’s not appropriate for every situation.
