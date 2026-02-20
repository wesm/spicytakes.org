---
title: "Running Apache On A Memory-Constrained VPS"
date: 2010-06-19
url: https://www.kalzumeus.com/2010/06/19/running-apache-on-a-memory-constrained-vps/
slug: running-apache-on-a-memory-constrained-vps
word_count: 692
---


Yesterday about a hundred thousand people visited this blog due to my post on [names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/), and the server it was on died several fiery deaths. This has been a persistent issue for me in dealing with Apache (the site dies nearly every time I get Reddited — with only about 10,000 visitors each time, which *shouldn’t be a big number on the Internet*), but no amount of enabling WordPress cache plugins, tweaking my Apache settings, upgrading the VPS’ RAM, or Googling lead me to a solution.


However, necessity is the mother of invention, and I finally figured out what was up yesterday. The culprit: KeepAlive.


Setting up and tearing down HTTP connections is expensive for both servers and clients, so Apache keeps connections open for a configurable amount of time after it has finished a request.  This is an extraordinarily sensible default, since the vast majority of HTTP requests will be followed by another HTTP request — fetch dynamically generated HTML, then start fetching linked static assets like stylesheets and images, etc.  Look, of 43 requests, 42 were not the last request in a 3 second interval.  It is a huge throughput win.  However, if you’re running a memory constrained VPS and get hit by a huge wave of traffic, **KeepAlive will kill you**.


When I started getting hit by the wave yesterday, I had 512MB of RAM and a cap (ServerLimit = MaxClients) of 20 worker processes to deal with them.  Each worker was capable of processing a request in a fifth of a second, because everything was cached.  This implies that my throughput should have been close to 20 * 60 * 5 = 60k satisfied clients a minute, enough to withstand even a mighty slashdotting.  (That is a bit of an overestimation, since there were also static assets being requested with each hit, but to fix an earlier Reddit attack I had manually hacked the heck out of my WordPress theme to load static assets from Bingo Card Creator’s Nginx, because there seems to be no power on Earth or under it that can take Nginx down.)


However, I had KeepAlive on, set to three seconds.  This meant that for every 250ms of a worker streaming cached content to a client, it spent 3 seconds sucking its thumb waiting for that client to come back and ask for something else.  In the meantime, other clients were stacking up like planes over O’Hare.  The first twenty clients get in and, from the perspective of every other client, the site totally dies for three seconds.  Then the next twenty clients get served, and the site continues to be dead for everybody else.  Cycle, rinse, repeat.  The worst part was people were joining the queue faster than their clients were either getting handled or timeouted, so it was essentially a denial of service attack caused by the default settings.  The throughput of the server went from about 60k requests per second to about 380 requests per second.  380 is, well, not quite enough.


Thus the solution: turning KeepAlive off.  This caused CPU usage to spike quite a bit, but since the caching plugin was working, it *immediately* alleviated all of the user-visible problems.  Bingo, done.


Since I tried about a dozen things prior to hitting on this, I thought I’d quick write them down in case you are an unlucky sod Googling for **Apache settings for your VPS**, possibly **Ubuntu Apache settings**, or that sort of thing:

- **Increase VPS RAM**: Not really worth doing unless you’re on 256MB.  Apache should be able to handle the load with 20 processes.
- **Am I using pre-fork Apache or the worker MPM?** If  you’re on Ubuntu, you’re probably using the pre-fork Apache.  MPM settings will be totally ignored.  You can check this by running apache2 -l .  (This is chosen at compile time and can’t be altered via the config files, so if — like me — you just apt-get your way around getting common programs installed, you’re likely stuck.)
- **What should my pre-fork settings be then?**


Assuming 512 MB of RAM and you are only running Apache and MySQL on the box:
