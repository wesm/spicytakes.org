---
title: "Twitter: Service vs. Platform"
date: 2007-04-12
url: https://blog.codinghorror.com/twitter-service-vs-platform/
slug: twitter-service-vs-platform
word_count: 696
---

Twitter is a victim of its own success. The site has massive scaling problems, to the tune of 11,000 pageviews per second. According to this [interview](https://web.archive.org/web/20070506140525/http://www.radicalbehavior.com:80/5-question-interview-with-twitter-developer-alex-payne/) with a Twitter developer, a lot of the scaling problems are attributable to Twitter’s choice of platform:


> By various metrics Twitter is the biggest [Rails](http://www.rubyonrails.org/) site on the net right now. Running on Rails has forced us to deal with scaling issues – issues that any growing site eventually contends with – far sooner than I think we would on another framework.
> The common wisdom in the Rails community at this time is that scaling Rails is a matter of cost: just throw more CPUs at it. The problem is that more instances of Rails (running as part of a Mongrel cluster, in our case) means more requests to your database. At this point in time there’s no facility in Rails to talk to more than one database at a time. The solutions to this are caching the hell out of everything and setting up multiple read-only slave databases, neither of which are quick fixes to implement. So it’s not just cost, it’s time, and time is that much more precious when people can[’t] reach your site.
> None of these scaling approaches are as fun and easy as developing for Rails. All the convenience methods and syntactical sugar that makes Rails such a pleasure for coders ends up being absolutely punishing, performance-wise. Once you hit a certain threshold of traffic, either you need to strip out all the costly neat stuff that Rails does for you (RJS, ActiveRecord, ActiveSupport, etc.) or move the slow parts of your application out of Rails, or both.
> It’s also worth mentioning that there shouldn’t be doubt in anybody’s mind at this point that Ruby itself is slow. It’s great that people are hard at work on faster implementations of the language, but right now, it’s tough. If you’re looking to deploy a big web application and you’re language-agnostic, realize that the same operation in Ruby will take less time in Python. All of us working on Twitter are big Ruby fans, but I think it’s worth being frank that this isn’t one of those relativistic language issues. Ruby is slow.


I’ve often said that [performance doesn’t always matter](https://blog.codinghorror.com/the-day-performance-didnt-matter-any-more/). But if, like Twitter, your business model is predicated on how fast your users can press the Refresh button in their browser, you could be in serious trouble if your service becomes popular.


What I find particularly amusing is the performance comparison with Python. It’s hard to believe that Python is that much faster than Ruby. Python, like Ruby, is an interpreted language, and **interpreted languages are so slow that if you have to ask how much performance you’re giving up, you can’t afford it**. Consider this chart from Code Complete 2.0:

kg-card-begin: html


| **Language** | **Type of Language** | **Execution Time Relative to C++** |
| C++ | Compiled | 1:1 |
| Visual Basic | Compiled | 1:1 |
| C# | Compiled | 1:1 |
| Java | Byte code | 1.5:1 |
| PHP | Interpreted | > 100:1 |
| Python | Interpreted | > 100:1 |


kg-card-end: html

I realize that Web 2.0 is built on the back of the cheap [“whatever box” server](https://blog.codinghorror.com/web-2-0-and-the-whatever-box-server/). Twitter is probably the perfect storm of refresh-heavy design coupled with exponential growth. Most websites wish they were so lucky.


To be fair, it sounds like most of Twitter’s problems are database problems, so maybe it doesn’t matter what language they use. But it does make you wonder: **what’s more important – the service, or the platform you deliver that service on?**


In the case where the latter is jeopardizing the former, I think it’s pretty clear where your allegiances should lie. Your users don’t care how cool the Rails platform is – but they sure do care about consistent availability of your service.

kg-card-begin: html

Update: This entry isn’t as clear as it could be. See my [followup to this post](https://blog.codinghorror.com/reddit-language-vs-platform/) for a better explanation of my position.

kg-card-end: html

[ruby on rails](https://blog.codinghorror.com/tag/ruby-on-rails/)
[scaling issues](https://blog.codinghorror.com/tag/scaling-issues/)
[database](https://blog.codinghorror.com/tag/database/)
[caching](https://blog.codinghorror.com/tag/caching/)
[read-only slave databases](https://blog.codinghorror.com/tag/read-only-slave-databases/)
