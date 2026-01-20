---
title: "DTrace and Python"
date: 2005-05-10
url: https://bcantrill.dtrace.org/2005/05/10/dtrace-and-python/
slug: dtrace-and-python
word_count: 197
---

# DTrace and Python DTrace and Python May 10, 2005 Sean McGrathhas agreat blog entryon adding DTrace probes to Python. As Sean points out, this isn’t a perfect solution – but damn is it cool! For whatever it’s worth, we’re currently working on infrastructure that will address many of the problems that Sean discussed; once completed, this infrastructure will allow for user-level providers to export the same semantic richness as the stable kernel-level providers likeio,schedandproc. But as Sean’s work shows, you can still do very interesting things even with what exists today… [Sean McGrath](http://blogs.sun.com/smg) Sean McGrath has a [great blog entry](http://blogs.sun.com/roller/page/smg/20050510#beer_python_and_stuff) great blog entry on adding DTrace probes to Python. As Sean points out, this isn’t a perfect solution – but damn is it cool! For whatever it’s worth, we’re currently working on infrastructure that will address many of the problems that Sean discussed; once completed, this infrastructure will allow for user-level providers to export the same semantic richness as the stable kernel-level providers like `io` io , `sched` sched and `proc` proc . But as Sean’s work shows, you can still do very interesting things even with what exists today… Technorati tag:DTrace Technorati tag: [DTrace](http://technorati.com/tag/DTrace) DTrace
