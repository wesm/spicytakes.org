---
title: "Vancouver, BC"
date: 2007-09-05
url: https://www.joelonsoftware.com/2007/09/05/vancouver-bc/
word_count: 1009
---


Vancouver, BC: Day one of the [FogBugz World Tour](https://www.joelonsoftware.com/items/2007/08/16.html). About 120 people showed up to see the first public demo of FogBugz 6.0, which will officially launch next Monday.


Vancouver is, without a doubt, one of North America’s most beautiful cities. Sparkling, clean, everything works well, nothing can possibly go wrong, people are friendly, and with the new weakened US dollar it’s really quite a prosperous place to live. Brett and I had dinner at [Joe Fortes](http://www.joefortes.ca/), where you get a choice of 4 different local species of salmon, maybe 20 other kinds of fresh fish, or about 10 different type of oysters, and there’s a beautiful rooftop deck where you can enjoy the usually pleasant Vancouver weather.


The demo went relatively smoothly, despite a few first-time kinks. At some point I was fiddling around so much with the report generator that I queued up a backlog of lengthy Monte Carlo simulations on the web server which made FogBugz lose interest in continuing with the demo; this not the kind of thing that happens in production web servers (part of the problem is that the laptop is running XP which has a kind of 3/4-baked implementation of IIS, version 5.1, which is not what anyone would run on a real server). Anyway, I had to restart IIS in the middle of the demo. Ooops. Hopefully that won’t happen again.


It couldn’t be that bad. Here’s some email feedback we already received from the demo:


> “Thank you for the entertaining and informative talk. We will be buying FogBugz as a result.” *Thank you! OK, we just broke even in Vancouver.*
> “Do you intend to provide free versions of FogBugz for open source projects, non-profits, or small teams of 2 people (like Perforce does with their products)?”. *Yes, it’s called the Student and Startup Edition. We’ll announce it soon, but it’s available now.*
> “Well, I expected to be bored about FogBugz and enraptured by fascinating tidbits of Joel Spolsky wisdom. In reality, the opposite was true. I now believe FogBugz to be a pretty interesting looking app, whereas an hour before your spiel I think I described it to someone as a “glorified Excel spreadsheet” (it’s amazing what I can come up with when I am not encumbered by facts).” *My tidbits aren’t that fascinating.*
> “ Having just attended Joel’s FogBugz 6.0 demonstration in Vancouver, we were very impressed with its capabilities.  My boss wants to go ahead and use FogBugz, however Joel mentioned that the Linux/Unix version was still in Beta.” *For Unix we’re still on 5.0 while we debug the PHP port, which I hope won’t take long. While you’re waiting for Unix FogBugz 6.0, you can either run 5.0 — and upgrade for free — or run a free trial on our server, and download the data when we’re shipping.*


The night before, in rehearsals, I discovered that the Fn+F7 trick that is supposed to turn on external monitors on this Thinkpad was actually freezing the computer solid, due to some kind of buggy interaction between the Intel 965 graphics chip software and the IBM/Lenovo Presentation Director software. I never did solve that problem, so I learned to use the Intel software to turn on the external monitor instead of pressing Fn+F7.


Flying in September after Labor Day is really not that bad, despite the scare stories you might have heard in the press; once everyone gets home from summer vacations the number of passengers in airports and on flights drops quite dramatically and flights start operating closer to schedule with much shorter lines. So far I don’t think we’ve waited in one line at an airport. Here are my favorite tricks for planning air travel to avoid chaos, delays, and cancellations:

1. The ideal time to fly is around 10 am. Usually delays pile up throughout the day, so the earlier you fly, the less likely you are to suffer delays. The very early flights are popular with people who want to get a full day in, so the midmorning flights tend to be the most civilized.
2. Always check the OAG before booking to see what flights are available. The OAG includes JetBlue and Southwest flights which the online travel agencies can’t show you.
3. Make sure you’re never on the last flight of the day if you really need to get somewhere on schedule. If something happens to the last flight, you’re in trouble. As a general principle, while planning for this trip, I always checked that there was at least one alternative flight that would get me to my next destination on time. Since we fly first class at Fog Creek, if one of our flights got cancelled, the airline will work hard to reaccomodate us while the coach passengers might have to wait forever for a rebooking.
4. Fly out of smaller airports whenever possible. My favorite alternative airports: John Wayne or Burbank instead of LAX, Ft. Lauderdale instead of Miami, Love instead of DFW.
5. If the flight you’re booked on is cancelled, don’t wait in line with the crowds for the single, overworked airline representative. Get on the phone to your airline’s frequent flyer priority number. They can rebook you just as well.
6. The American Express Platinum card pays for itself just from the free membership in Continental, Northwest, and Delta’s lounges… not only because the lounges are quiet and pleasant, but because the lounges have unharried and experienced airline agents who are happy to help you with complicated problems, rebookings, and upgrades.
7. Final trick: never schedule an important flight during the last few days of the month, especially on Northwest. Pilots are only allowed to fly a certain number of hours per calendar month and by the end of the month they’re running out of hours, especially on the more awfully-managed airlines like Northwest, so flights galore get cancelled in the last few days of every calendar month.


See you tomorrow in Seattle! There are still [five seats available](http://worldtour.fogbugz.com/Register.aspx?ixEvent=26) if you haven’t registered yet.
