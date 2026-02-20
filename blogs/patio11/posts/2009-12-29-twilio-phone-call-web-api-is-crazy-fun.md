---
title: "Twilio (phone call web API) is crazy fun"
date: 2009-12-29
url: https://www.kalzumeus.com/2009/12/29/twilio-phone-call-web-api-is-crazy-fun/
slug: twilio-phone-call-web-api-is-crazy-fun
word_count: 617
---


I live in Japan but my family lives in Chicago.  I wanted to make it simple for them to call me, so I looked for a service which would provide a US number and forward it to an international number.  This way they can call me without having to pay for the call to Japan or figure out how to do it, which nobody managed in nearly five years.


For the last year I’ve used [TollFreeForwarding.com](http://www.tollfreeforwarding.com), which is… adequate.  Aside from the dropped calls, poor call quality, times when they call and I am connected to an irate Chinese man wondering what happened to his wife, and service interruptions, they pretty much do what they say on the tin.


My other point of annoyance with having a Chicago number so that my family can call me at any time is that my family sometimes calls me at *any time*, and while I really like speaking to them I would prefer not to do it at 4:30 AM on a work day.  (This also goes to the Bosnian high school student who found my number on my whois records and decided to chat about software strategy at 4:30 AM.  I’m totally willing to do that, but please folks, learn to use [this website](http://www.whattimeisitnow.com).  Of course I can’t just block calls between 3 AM and 8 AM, because if it is an emergency then *I’ll deal.*


Which is a long-winded way of introducing why I love [Twilio](http://www.twilio.com), a startup that makes it easy to script phone calls with an API.  (Which uses — cue cursings from the Big Freaking Enterprise Java Web App programmer — XML.  But only a little XML.)


They were featured on Hacker News the other night with a quick guide to making a “customized international calling card”.  I promptly saw the possibilities:

1. Mom (et al) calls the 312-XXX-YYYY number they provide me.
2. Twilio’s computers answer the call and do an HTTP request to my website to get my call script.
3. If I am likely to be home and awake, the website says “Play them a little message then connect the call to my home in Japan.”
4. If I am likely to be not at home, the website says “Play them a little mssage then connect the call to my cell in Japan.”
5. If I am likely to be asleep, then the website says “Tell them it is ‘3:47 AM Japan time’ and ask them to call back tomorrow or, if it is an emergency, hit 1 to have Patrick woken up by Ride of the Valkyries.”


This took really disgustingly little code to accomplish.  My v1.0 of the “app”, which just redirected between two phone numbers with a message, was a hard-coded XML file that I whipped up in vi.  It was five lines long.  The more complicated version — not quite deployed yet, as I am still in the US for Christmas — is a Sinatra application and will be about 30 lines long, with a bit more for config files for the web server.  (Nginx, naturally.  I’m debating whether to try out Passenger.)


This would have been a bit easier if I had just deployed another Rails app to the same server as BCC but that would be gratuitous overkill, and Thomas Ptacek is trying to convince me that Sinatra is great for speedy little web dev tasks.


Anyhow, Twilio appears to be cheaper than my existing solution for my usage levels, have features more in line with my needs, and hopefully will *not* disrupt anyone’s marriage.  Which is sort of a plus.


Now if I can just find a way to use Twilio for my next application…
