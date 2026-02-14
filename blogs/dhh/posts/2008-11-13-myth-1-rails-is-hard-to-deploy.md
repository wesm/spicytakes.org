---
title: "Myth #1: Rails is hard to deploy"
date: 2008-11-13
url: https://dhh.dk/posts/30-myth-1-rails-is-hard-to-deploy
slug: myth-1-rails-is-hard-to-deploy
word_count: 669
---


*(If you don't want to bother with the history lesson, just skip straight to the answer)*


Rails has traveled many different roads to deployment over the past five years. I launched Basecamp on mod_ruby back when I just had 1 application and didn't care that I then couldn't run more without them stepping over each other.


Heck, in the early days, you could even run Rails as CGI, if you didn't have a whole lot of load. We used to do that for development mode as the entire stack would reload between each request.


We then moved on to FCGI. That's actually still a viable platform. We ran for years on FCGI. But the platform really hadn't seen active development for a very long time and while things worked, they did seem a bit creaky, and there was too much gotcha-voodoo that you had to get down to run it well.


**Then came the Mongrel**

Then came [Mongrel](http://mongrel.rubyforge.org/) and the realization that we didn't need Yet Another Protocol to let application servers and web servers talk together. We could just use HTTP! So packs of Mongrels were thrown behind all sorts of proxies and load balancers.


Today, Mongrel (and it's ilk of similar Ruby-based web servers such as [Thin](http://code.macournoyer.com/thin/) and [Ebb](http://ebb.rubyforge.org/)) still the predominate deployment environment. And for many good reasons: It's stable, it's versatile, it's fast.


**The paradox of many Good Enough choices**

But it's also a jungle of options. Which web server do you run in front? Do you go with Apache, nginx, or even lighttpd? Do you rely on the built-in proxies of the web server or do you go with something like HAProxy or Pound? How many mongrels do you run behind it? Do you run them under process supervision with monit or god?


There are a lot of perfectly valid, solid answers from those questions. At 37signals, we've been running Apache 2.2 [with HAProxy](http://www.37signals.com/svn/posts/1073-nuts-bolts-haproxy) against monit-watched Mongrels for a few years. When you've decided on which pieces to use, it's actually not a big deal to set it up.


But the availability of all these pieces that all seem to have their valid arguments lead to a paradox of choice. When you're done creating your Rails application, I can absolutely understand why you don't also want to become an expert on the pros and cons of web servers, proxies, load balancers, and process watchers.


And I think that's where this myth has its primary roots. The abundance of many Good Enough choices. The lack of a singular answer to How To Deploy Rails. No ifs, no buts, no "it depends".


**The one-piece solution with Phusion Passenger**

That's why I was so incredibly happy to see [the Phusion team](http://www.phusion.nl/) come out of nowhere earlier this year with [Passenger (aka mod_rails)](http://www.modrails.com/). A single free, open source module for Apache that brought mod_php-like ease of deployment to Rails.


Once you've completed the incredibly simple installation, you get an Apache that acts as both web server, load balancer, application server and process watcher. You simply drop in your application and touch tmp/restart.txt when you want to bounce it and bam, you're up and running.


But somehow the message of Passenger has been a little slow to sink in. There's already a ton of big sites running off it. Including [Shopify](http://www.shopify.com/), [MTV](http://style.mtv.com/), [Geni](http://www.geni.com/), [Yammer](http://www.yammer.com/), and we'll be moving over first [Ta-da List](http://www.tadalist.com/) shortly, then hopefully the rest of the [37signals suite](http://37signals.com/) quickly thereafter.


So while there are still reasons to run your own custom multi-tier setup of manually configured pieces, just like there are people shying away from mod_php for their particulars, I think we've finally settled on a default answer. Something that doesn't require you to really think about the first deployment of your Rails application. Something that just works out of the box. Even if that box is a shared host!


In conclusion, Rails is no longer hard to deploy. Phusion Passenger has made it ridiculously easy.


*See the [Rails Myths](29-the-rails-myths.html) index for more myths about Rails.*

