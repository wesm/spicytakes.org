---
title: "Basecamp 2 and Basecamp 3 search outage report"
date: 2019-03-07
url: https://signalvnoise.com/svn3/basecamp-2-and-basecamp-3-search-outage-report/
slug: basecamp-2-and-basecamp-3-search-outage-report
word_count: 1619
---


From [4:30am GMT March 7 / 10:30pm Central March 6](https://everytimezone.com/?t=5c805f00,10e) until [1:02pm GMT / 7:02am Central](https://everytimezone.com/s/a2ff28a3), Basecamp 2 and the search feature in Basecamp 3 were mostly offline due to a catastrophic network failure with our cloud provider. Both our primary network link, our backup network link, and several additional ad-hoc network links between critical services needed to run Basecamp 2 were forced offline, as the cloud provider sought to deal with underlying network problems they were having.Both Basecamp 2 and the search feature in Basecamp 3 are now fully back online.But this was one of the worst outages we’ve had in the history of Basecamp. We’re incredibly sorry about just how long and broad of an interruption this caused, especially for our European customers of Basecamp 2. We’re so very sorry about this. We know this caused real and deep interruption to many people’s workflow from the early morning to the early afternoon on the main European timezones.  And of course to any other customers around the world, including the US, who were also affected.We’ve learned some hard lessons about network availability, the limitations of redundant, and double redundant backup connections. We’ll be working diligently to change how we work with cloud providers in the future, and how we can insulate ourselves and our customers from any future incidents like this. While this incident may have been triggered by network issues outside of our immediate control, it’s always within our control how we architect our systems, how we prepare for disasters, and how we ensure something like this never has the power to inflict such a traumatic outage.So I want to make absolutely clear that this is our failure. Even in this new world of cloud services, it’s still always our fault when Basecamp isn’t available. Whatever the underlying problem for an outage, there’s always something you could have done to prevent it. And our list in this case includes a number of both obvious and not-so-obvious steps we could have taken. We will now take them.Once again, I’m deeply sorry for this terrible outage. We will work as diligently we can to ensure that this doesn’t happen to any version of Basecamp again, neither past or present. Thank you for understanding, thank you for your patience, and thank you for being a customer, even if you with all justification ran out of both understanding and patience during this utterly unacceptable outage.Below is a play-by-play timeline of how the outage unfolded:At [4:30am GMT March 7 / 10:30pm Central March 6](https://everytimezone.com/?t=5c805f00,10e), all of Basecamp 2 and the search feature in Basecamp 3 went offline due to network connections issues with our cloud services provider. The problem took out both our primary and backup network connection. We immediately started working on a secondary backup solution, which involved rerouting all the troubled network traffic over a different connection.At [around 5:30am GMT / 11:30pm Central](https://everytimezone.com/?t=5c805f00,14a), we successfully established a backup network connection, which brought Basecamp 2 back online. Unfortunately that was a short-lived reprieve, as this secondary backup solution only lasted a couple of minutes before also going dark.


At [around 6am GMT / 12pm Central](https://everytimezone.com/?t=5c805f00,168), we finally established a third backup network connection, which brought Basecamp 2 back online, albeit with intermittent issues, and running somewhat slower than usual.


At [around 6:45am GMT / 12:45pm Central](https://everytimezone.com/?t=5c805f00,195), we got the search feature in Basecamp 3 back online, as one of our primary network links was tentatively restored. We’re not out of the woods yet, and there may yet be still more interruptions with both Basecamp 2 and Basecamp 3 search, but we’ll continue to work until everything is back in perfect working order.


At around 7:08am GMT / 1:08am Central, we again lost the primary network link, which took the search feature in Basecamp 3 back offline. Basecamp 2 continued to be online via our backup network link. Working to make Basecamp 3’s search feature accessible via the backup link as well.


As of 7:22am GMT / 1:22pm Central, we’re still working on restoring access to the search feature in Basecamp 3. Basecamp 2 continues to be online and accessible.


As of 7:32am GMT / 1:32pm Central, the temporary solution we had in place for Basecamp 2 ran into trouble again. Basecamp 2 is currently offline, and search for Basecamp 3 remains offline as well.


As of 7:44am GMT / 1:44am Central, we’ve confirmed that the search feature in Basecamp 3 is working again. Still addressing the issue with Basecamp 2, which remains offline.


As of 8:01am GMT / 2:01am Central, we’re still working on bring Basecamp 2 back online. While working on this, we’ve managed to get the proper error screen showing, which directs users to our status and Twitter pages for updates.


As of 8:16am GMT / 2:16am Central, we continue to be dealing with major network disruptions from our cloud provider. While they’re working on solving the underlying issues, we’re working on all the possible backup options.


As of 8:32am GMT / 2:32am Central, work continues on routing around the major network issues that the cloud provider continues to deal with. We’re trying to send traffic around our system in a way to avoid the damage. It’s not a straight forward task, but we’re trying everything we can to make it work.


As of 8:53am GMT / 2:53am Central, we’ve managed to bring Basecamp 2 back online. But we are not out of the woods. Work will continue to get everything stable. It’s highly likely that we’ll continue to see issues until we’ve fixed the root cause plaguing the network with our cloud provider.


As of 9:19am GMT / 3:19am Central, all systems have been running and stable for about half an hour. We continue to work on ensuring that stays like that. There are still network issues with the cloud provider, but we’ve managed to string together a solution that works around the remaining issues for now.


As of 9:38am GMT / 3:38am Central, the network was once again disrupted as our cloud provider continues to pull things offline trying to sort the root cause. We continue to do what we can to work with our backup links and solutions. This means that both Basecamp 2 and the search feature for Basecamp 3 are offline again. So sorry.


As of 10:07am GMT / 4:07am Central, the network disruption continues while the cloud provider is still working to address the underlying issue. We are doing everything we can to route around the damage, but it’s unfortunately very difficult. We won’t rest until it’s all sorted and stable. Again, so very sorry for this unacceptably long outage.


As of 10:27am GMT / 4:27am Central, we’re still trying to find a way around this network disruption. Basecamp 2 and the search feature in Basecamp 3 are both offline, and we’re working hard to get them up and running. So sorry for the continued outage, and thank you for your patience.


As of 10:41am GMT / 4:41am Central, Basecamp 2 and the search feature for Basecamp 3 are still offline, as the network issues with the cloud provider continue. We’re working to get both online and come up with a permanent solution, and we won’t rest until we do. Sorry again for this extended outage.


As of [11:02am GMT / 5:02am Central](https://everytimezone.com/?t=5c805f00,294), we’re in a holding pattern waiting for our cloud provider to restore their network connectivity. While they do that, Basecamp 2 and the search feature in Basecamp 3 are offline. We’re still trying to find a way around these problems, and we’ll keep updating you until everything is back online and stable.


As of [11:21am GMT / 5:21am Central](https://everytimezone.com/s/0571c59e), we continue to deal with major network disruptions from our cloud provider. While they’re working on solving the underlying issues, Basecamp 2 and the search feature of Basecamp 3 are inaccessible. So sorry.


As of [11:38am GMT / 5:38am Central](https://everytimezone.com/s/674b46cb), Basecamp 2 and the search feature of Basecamp 3 are still offline. Unfortunately, we don’t know when our cloud provider will have fixed the network issues causing this. Until they do, and we know everything’s working perfectly, we’ll keep you updated. Thanks so much for being patient with us.


As of [11:55am GMT / 5:55am Central](https://everytimezone.com/s/b8d1df28), our cloud provider hasn’t resolved the network connectivity issues which are causing us problems. Basecamp 2 and the search feature of Basecamp 3 are still offline. We’re so sorry for the trouble this is causing you all.


As of [12:13pm GMT / 6:13am Central](https://everytimezone.com/s/60ed3573), Basecamp 2 and the search feature of Basecamp 3 are still offline. We’re still working on this as the cloud provider continues to resolve its network issues. We’re really sorry, because we know how much you all rely on Basecamp.


As of [12:30pm GMT / 6:30am Central](https://everytimezone.com/?t=5c805f00,2ee), the cloud provider is still working on its network connectivity issues. Basecamp 2 and the search feature of Basecamp 3 remain offline until those are fixed. We’re really sorry for the continued outage.


As of [12:48pm GMT / 6:48am Central](https://everytimezone.com/s/a2ff28a3), Basecamp 2 and the search function in Basecamp 3 are still offline. We’re waiting for the cloud provider to fix their network issues, and exploring some alternative means of resolving the problem. We don’t yet know if this is going to work, but we’ll keep you posted. Thanks so much for being patient with us, and sorry again.


As of [1:02pm GMT / 7:02am Central](https://everytimezone.com/s/a2ff28a3), Basecamp 2 and the search feature in Basecamp 3 are back online. The root cause hasn’t been fixed, however, so we don’t know if these connections will remain stable. Right now, you should be able to work in Basecamp. Sorry again for all the trouble this caused.


[
 ]("</p)

