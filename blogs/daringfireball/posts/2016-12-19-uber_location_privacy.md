---
title: "Regarding Uber’s New ‘Always’ Location Tracking"
date: 2016-12-19
url: https://daringfireball.net/2016/12/uber_location_privacy
slug: uber_location_privacy
word_count: 445
---


Uber’s iOS app [recently changed](http://www.npr.org/sections/alltechconsidered/2016/12/01/503985473/uber-now-tracks-passengers-locations-even-after-theyre-dropped-off) its location-tracking from “When using the app” to “Always”. The company says they’re only doing it for five minutes after a ride ends, to see where passengers go. They’re trying to improve the accuracy of where passengers get dropped off.


[Michael S. Fischer is alarmed by this](https://hackernoon.com/dear-apple-give-us-control-over-stalkerware-95c625f585fb):


> As you know, iOS allows users to control how apps can access the
> user’s location. There are three choices: “Always,” “When using
> the app,” or “Never.” These are reasonable options. Some users
> might never want an app to have access to their location. Others
> might have a strong trust relationship with the app and its
> authors and allow the app always to track them.
> Most of us, though, fall into the middle camp: We want to allow
> apps to use our location for the purpose of providing a service,
> but want to control our privacy when the app or its authors cease
> doing business with us. So what we’re asking is simple:
> *Don’t allow app developers to disable the “when using the app”
> Location privacy option.*
> It’s simply unnecessary for Uber or others to track us when the
> app isn’t in use. How do we know this? *Because these apps worked
> adequately before they disabled this option.* We were able to meet
> our drivers by opening the app, finding our location, and hailing
> a driver. We gave them enough information to get the job done, and
> we were satisfied with the results.


Few people are more skeptical about Uber than I am. Just last week [I linked to](http://daringfireball.net/linked/2016/12/12/uber-privacy) a [scathing report on Uber’s internal privacy problems](https://www.revealnews.org/article/uber-said-it-protects-you-from-spying-security-sources-say-otherwise/).


iOS does not give users the fine-grained control over apps’ location-tracking privileges that Fischer is asking for, but it does give us a way to verify that Uber is only using its “Always” privilege the way it claims to be — for five minutes after a ride ends.


Go to Settings → Privacy → Location Services and take a look at the list of apps. If Uber has checked your location recently, an indicator will appear in the list — purple if it checked “recently”, gray if in the last 24 hours. I’ve been checking this every few days ever since Uber changed its location-checking privilege, and it has never once shown any sign of misuse.


I don’t trust Uber. But we can collectively verify that in this case, they’re doing exactly what they say they’re doing.



| **Previous:** | [On Jony Ive’s Role at Apple](https://daringfireball.net/2016/11/ives_role_at_apple) |
| **Next:** | [Craig Hockenberry’s ‘Making Sense of Color Management’](https://daringfireball.net/2017/01/making_sense_of_color_management) |


PreviousNext