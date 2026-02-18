---
title: "Day 40: screen flickering & a talk about containers"
date: 2021-01-16
url: https://jvns.ca/blog/2021/01/16/day-40--screen-flickering---a-talk-about-containers/
slug: day-40--screen-flickering---a-talk-about-containers
word_count: 598
---


On Friday I gave a talk about containers and worked a bit more on the puzzle
website design. I’m going to talk about something else though which is my
attempt to understand what’s going on with laptop screen flickering.


I still don’t know a lot about this so as usual it’s possible some things in
here are wrong.


content warning: some flickery images ahead.


### why do I have a headache? (maybe PWM?)


I’ve had a headache every day this week since I got a new laptop which has been
pretty unpleasant. This is a new thing and I mentioned this to Kamal and he
suggested “maybe your new screen is flickering”.


I searched something like “thinkpad t14 headache”, and
learned about something called “pulse width modulation” or PWM that some people are
sensitive to. Apparently the way some screens do screen dimming is to rapidly
flicker the screen on/off.


I thought a screen was called a screen but everyone on the internet talking
about laptop/TV screens seem to call them “panels” so I guess I’ll say “panel” for the rest of this post.


### the thinkpad panel lottery


Another thing I learned which was surprising to me is that Lenovo won’t tell
you which exact monitor panel you get when you order a laptop from them. People
seem to talk a lot about this on the internet because some the panels can be
pretty different from each other.


This
[page from notebook check](https://www.notebookcheck.net/Lenovo-s-Panel-Lottery-continues-with-3-different-14-inch-LowPower-displays.426538.0.html)
talks about the panel lottery a bit.


### taking a video of my screen


I read on the internet that you can diagnose flickering issues by taking a slow motion video of your screen so I took videos of 3 laptops: my old laptop (x250), my new laptop (t14s), and Kamal’s laptop (t14).


here’s my old laptop (which didn’t cause me problems), with a LP125WF2-SPB2 panel.


![](https://jvns.ca/images/my_old_laptop.gif)


here’s the new laptop: (the suspected culprit), with a R140NWF5 RA panel.


![](https://jvns.ca/images/new_laptop.gif)


and here’s kamal’s laptop: (which doesn’t look like a video at all, but what’s happening is that there’s just no flickering). that’s a N140HCR-GL2.


![](https://jvns.ca/images/kamal_laptop.gif)


I find the results here kind of weird – both the videos of my old and new
laptops seem kind of intense and if the new one is causing me problems I don’t
understand why the old one wouldn’t as well. But maybe the black bar going down
the screen on the old one is actually the screen refreshing and not PWM? I
don’t really know what to make of this.


### how to find out what panel you have


I found out which panel I have (on Linux) by running:


```
strings /sys/class/drm/card0-eDP-1/edid

```


It output `R140NWF5 RA`. I found some information about the R140NWF5 RA on
[this page from notebook check](https://www.notebookcheck.net/Lenovo-ThinkPad-T490-Laptop-Review-The-Comet-Lake-U-Update.455237.0.html)
reviewing a different Thinkpad laptop with the same panel which says that this
panel has a PWM frequency of about 980 hertz.


That seems kind of high (900 times a second is fast!) and that site says “The
frequency of 980.4 Hz is quite high, so most users sensitive to PWM should not
notice any flickering.” So I’m still not quite sure if this is the reason I
have a headache. More experimentation required!


### not sure what I’ll do about this yet


I might try to get the panel replaced with a different one (maybe the same one
that Kamal has) and see if it helps – it seems like they’re not that expensive
to buy and there’s a computer shop nearby who I’ve had good experiences with
going to for repairs in the past.
