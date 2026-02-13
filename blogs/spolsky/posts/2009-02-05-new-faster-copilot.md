---
title: "New, faster Copilot"
date: 2009-02-05
url: https://www.joelonsoftware.com/2009/02/05/new-faster-copilot/
word_count: 489
---


Something I knew: if you just put traffic on the Internet, it’s not necessarily going to go by the most efficient route.


Something I didn’t know: that can make a pretty big difference. The default routes can be slow, clogged, and high latency. Think Cross-Bronx Expressway.


[Akamai](http://www.akamai.com/) sent a couple of salespeople over to pitch us a service called [IP Application Accelerator](http://www.akamai.com/ipa). According to the goofy pictures-with-clouds in the whitepaper, when you subscribe to this service, your packets go straight to the nearest Akamai node, which are installed all over the world, and then they magically zip on a superfast superclean superhighway to the Akamai node nearest your destination, after which they hop off and take the city bus to their final destination.


I have to admit to being extremely skeptical. Isn’t that what the Internet is supposed to do anyway? When I heard about this I really didn’t think it would work. I mean, sure, I understand Akamai’s original product, whereby the big static files in your site would be copied to nodes all over the Internet for faster delivery, but I didn’t expect great speed improvements for an application like Fog Creek [Copilot](https://www.copilot.com/), which can’t cache anything.


Jason, on the Copilot team, wanted to try anyway. Performance is the biggest complaint about Copilot, so we were ready to try anything that increased the “speed of light.” Setting it up turned out to be pretty easy. The costs were reasonable and Akamai was more than happy to let us see if it worked as well as advertised before committing to spending anything. Setup consisted entirely of changing an IP address or two.


Well, the new Akamaized Copilot seems to get about 100% more throughput going from Boston to Los Angeles. More importantly, our exhaustive scientific experiments using beakers and chemicals and graph paper and slide rules proved that the usability of Copilot jumped from “tolerable” to “pretty snappy.”


My high school science teacher would be proud.


Last week in Munich I was staying in a hotel (Bayerischer Hof) with ridiculously bad internet connectivity (provided by Swisscom) that was bursty, had lengthy dropouts, surprisingly low bandwidth (I couldn’t watch YouTube movies of cats doing funny things, even at the lowest resolution), and was poorly managed (it literally could not route to many popular sites). So I tried the new Akamaized Copilot back to my desk in New York and was blown away… Copilot’s speed and reliability doing remote desktop was actually better than the native internet access in the hotel. This shows, I think, that Akamai managed to pull its traffic off of the crappy Swisscom network before Swisscom could do any more damage. Awesome.


It’s still too early in the experiment to decide conclusively that this was a good move. The internet is a huge place, and we’ve only done a handful of experiments. The final verdict will come from our customers, but so far I’m a believer.
