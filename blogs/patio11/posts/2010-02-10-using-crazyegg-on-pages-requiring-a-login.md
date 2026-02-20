---
title: "Using CrazyEgg on Pages Requiring A Login"
date: 2010-02-10
url: https://www.kalzumeus.com/2010/02/10/using-crazyegg-on-pages-requiring-a-login/
slug: using-crazyegg-on-pages-requiring-a-login
word_count: 272
---


Long-time readers of this blog know I’m absolutely goo-goo for [CrazyEgg](http://www.crazyegg.com), principally because they [keep making me money](https://www.kalzumeus.com/2009/02/04/crazyegg-makes-me-serious-money-again/).  They’re seriously my favorite $19 to pay every month, even when I don’t actually use them, because some day I know I’ll get the itch again and then *bam* actionable insights into what my customers are doing. Today is an itchy day.


One thing I have never gotten around to is tracking how users click on pages in my web application, behind the login screen.  CrazyEgg can do this but you need a bit of magic to let their screenshot bot grab samples of the page being interacted with — otherwise, they won’t be able to match up the events their Javascript recorded with the form fields on, um, your login screen.


CrazyEgg’s current user-agent string is:


Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.4) Gecko/20091016 (CrazyEgg 2 screenshot agent) Firefox/3.5.4


Then just shortcircuit your login procedure for people with that user agent.  (This may be undesirable if you are very, very security conscious.  I sell bingo cards to 60 year old women.  If you are security conscious, email them and they’ll provide a listing of IPs to whitelist.)


In Rails, doing something on the basis of the user agent is easy but, and I know this might come as a surprise, not covered in the documentation.


For a quick 30 second solution, I signed up as a trial user for my own service with the email address crazyegg@bingocardcreator.com, and have the analogue to the above method on my site just pretend that anybody with the appropriate User Agent is authenticated as that user.
