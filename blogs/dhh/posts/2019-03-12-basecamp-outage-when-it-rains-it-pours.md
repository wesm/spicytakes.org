---
title: "Basecamp outage: When it rains, it pours"
date: 2019-03-12
url: https://signalvnoise.com/svn3/basecamp-outage-when-it-rains-it-pours/
slug: basecamp-outage-when-it-rains-it-pours
word_count: 824
---


From 2:13am GMT March 13 / 9:13pm Central March 12 until around 4:10am GMT / 11:10pm Central, Basecamp 3 was mostly offline and Basecamp 2 unable to process file uploads and downloads, as our cloud storage provider had a severe, sustained outage.  We continued to have minor disruptions in service from 4:10am GMT / 11:10pm Central until everything was cleared at 6:53am GMT / 1:53am Central.


This is the second time in a week that I’m forced to write “I’m so sorry”. That’s incredibly painful. Both because it’s because we’re failing our customers for the second time in a week, but also because it’s showing us just how unprepared we’ve been as an organization to deal with these cloud challenges, despite our belief otherwise.


I’m not going to bother you with platitudes about “lessons to be learnt”, because I’ve already done that just a few days ago. This goes much deeper than just a few lessons. It has called into question our entire risk management and operational structure at Basecamp.


It’s also been a mighty fall. From reaching for 99.999% in uptime – the hallowed five nines! – we’re now scrambling for two of them. From riches of reliance to rags of shambles. To say this is humbling is an epic understatement.


We’re stopping all major product development at Basecamp for the moment, and dedicating all our attention to fixing these single points of failure that the recent cloud outages have revealed. We’re also going to pull back from our big migration to the cloud for a while, until we’re able to comfortably commit to a multi-region, multi-provider setup that’s more resilient against these outages.


I’m sorry. I’m really sorry (and ashamed).


For posterity, here’s the complete play-by-play updates:


Starting 2:13am GMT / 9:13pm Central, Basecamp 2 and Basecamp 3 both started going intermittently offline, as our cloud storage provider had a severe, sustained outage.


As of 3:21am GMT / 10:21pm Central, these problems are ongoing. We are working all emergency avenues and all fallback options.


As of 3:33am GMT / 10:33pm Central, we’ve managed to make both Basecamp 2 and 3 accessible more of the time. But file uploads and downloads are still offline. We’re working on all of this.


As of 3:43am GMT / 10:43pm Central, we’re seeing some improvement in both file downloads and uploads for both Basecamp 2 and 3 at the moment. But it’s still very intermittent. We’ve managed to somewhat stabilize general access to the system, though even that is somewhat intermittent as well.


As of 3:57am GMT / 10:57pm Central, our cloud storage provider believes they’ve found the root cause, and they’re working on resolving it. In the meantime, we’re working on making sure that the apps remain accessible for all other access than file uploads and downloads without interruption.


As of 4:10am GMT / 11:10pm Central, both Basecamp 2 and 3 continue to be mostly available and file uploads and downloads mostly working. We are not stopping until things are fully and completely working for everyone and for sure.


As of 4:24am GMT / 11:24pm Central, things continue to look mostly good for both Basecamp 2 and 3 and file uploads and downloads are mostly working. *Mostly*. (Not exactly a comforting word in situations like this, but here we are! 😢). Work continues.


As of 4:50am GMT / 11:50pm Central, the issues continue at a simmer. Basecamp 2 and Basecamp 3 continues to have blips, and file uploads and downloads continue to see some errors as well. The cloud storage provider is now rolling out their root-cause fix, albeit slowly. We continue to fight the best we can on our end.


As of 5:10am GMT / 12:10am Central, we continue to manage the situation the best we can on our end, including developing better error messages, and preparing backup provisions. The cloud storage provider continues their work as well.


As of 5:24am GMT / 12:24am Central, Basecamp 2 and 3 are still available, but there’s a trickle of errors with file uploads and downloads. If you see an error, retry the upload and it’ll most likely go through.


As of 5:43am GMT / 12:43am Central, Basecamp 2 and 3 are still online, but we’re not out of the woods yet. We’ll continue to update here, on our [Status Page](https://status.basecamp.com/) and on [Twitter](https://twitter.com/basecamp).


As of 6:11am GMT / 1:11am Central, we’re still working to bring Basecamp 2 and Basecamp 3 back up and fully stable.


As of 6:35am GMT / 1:35am Central, we’re not seeing the same level of errors on our end for Basecamp 2 and Basecamp 3. Neither are we seeing any customers reporting issues. But, we want to wait a beat to make sure we’re in the all clear.


As of 6:53am GMT / 1:53am Central, we’re in the all clear. Everything is back up and behaving as-expected in Basecamp 2 and Basecamp 3. All file uploads, file downloads, and avatars are working again.

