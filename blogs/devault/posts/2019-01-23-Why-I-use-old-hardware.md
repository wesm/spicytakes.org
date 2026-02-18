---
title: "Why I use old hardware"
date: 2019-01-23
url: https://drewdevault.com/2019/01/23/Why-I-use-old-hardware.html
slug: Why-I-use-old-hardware
word_count: 560
---

Recently I was making sure my main laptop is ready for travel 1 , which mostly
just entails syncing up the latest version of my music collection. This laptop
is a Thinkpad X200, which turns 11 years old in July and is my main workstation
away from home (though I bring a second monitor and an external keyboard for
long trips). This laptop is a great piece of hardware. 100% of the hardware is
supported by the upstream Linux kernel, including the usual offenders like WiFi
and Bluetooth. Niche operating systems like 9front and Minix work great, too.
Even coreboot works! It’s durable, user-serviceable, light, and still looks
brand new after all of these years. I love all of these things, but there’s no
denying that it’s 11 years behind on performance innovations.

Last year  [KDE](https://kde.org)  generously  [invited me](https://drewdevault.com/2018/04/28/KDE-Sprint-retrospective.html)  to and
sponsored my travel to their development sprint in Berlin. One of my friends
there teased me - in a friendly way - about my laptop, asking why I used such an
old system. There was a pensive moment when I answered: “it forces me to
empathise with users who can’t use high-end hardware”. I showed him how it could
cold boot to a productive  [sway](https://swaywm.org)  desktop in <30 seconds,
then I installed KDE to compare. It doubled the amount of disk space in use,
took almost 10x as long to reach a usable desktop, and had severe rendering
issues with my old Intel GPU.

To be clear, KDE is a wonderful piece of software and my first recommendation to
most non-technical computer users who ask me for advice on using Linux. But
software often grows to use the hardware you give it. Software developers tend
to be computer enthusiasts, and use enthusiast-grade hardware. In reality, this
high-end hardware isn’t really  *necessary*  for most applications outside of
video encoding, machine learning, and a few other domains.

I do have a more powerful workstation at home, but it’s not really anything
special. I upgrade it very infrequently. I bought a new mid-range GPU which is
able to drive my four displays 2  last year, I’ve added the occasional hard
drive as it gets full, and I replaced the case with something lighter weight 3
years ago. Outside of those minor upgrades, I’ve been using the same desktop
workstation for 7 years, and intend to use it for much longer. My servers are
similarly running on older hardware which is spec’d to their needs (actually, I
left a lot of room to grow and  *still*  was able to buy old hardware).

My 11-year-old laptop can compile the Linux kernel from scratch in 20 minutes,
and it can play 1080p video in real-time. That’s all I need! Many users cannot
afford high-end computer hardware, and most have better things to spend their
money on. And you know, I work hard for my money, too - if I can get a computer
which can do nearly 5  *billion*  operations per second for $60, that should be
sufficient to solve nearly any problem. No doubt, there are faster laptops out
there, many of them with similarly impressive levels of compatibility with my
ideals. But why bother?

1. To [FOSDEM](https://fosdem.org/2019/) - see you there! ↩︎
2. I have a variety of displays and display configurations for the purpose of continuously testing sway/wlroots in those situations ↩︎
