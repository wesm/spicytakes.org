---
title: "Speeding up HEY's The Feed"
date: 2021-05-20
url: https://world.hey.com/dhh/speeding-up-hey-s-the-feed-82e4d2ee
slug: speeding-up-hey-s-the-feed-82e4d2ee
word_count: 620
---

Modern emails are essentially HTML pages. Particularly newsletters, which are full of images, styles, and tables. Showing these HTML emails inside a web-based email client is not a trivial problem. Unlike a normal HTML page that has the whole browser to itself, these HTML emails have to be shown inside the navigational chrome of the email client. You have to keep the HTML from the emails from interfering with each other, with the HTML of the email client itself, and show them at the right size.
That means quarantining the rendering of the email, and ensuring text is scaled correctly, with images reflowing as intended, when they're shrunk. Making all this work as you'd expect is easily one of the most complicated parts of HEY (and the area with the longest outstanding list of issues!).
But where most email clients have to tackle this problem from the perspective of rendering a single email, HEY's unique feature for reading newsletters called
[The Feed](https://www.hey.com/features/the-feed/?source=hey-world-dhh)
needs to deal with rendering as many of these HTML emails as you can scroll through. On a single page. Across all devices. Including ones that are… ehmmm… computationally challenged.
The problem is that even rendering 8 of these HTML emails upfront, which is what we were doing until recently, is surprisingly taxing for a lot of devices! It's basically like opening 8 browser tabs concurrently. Modern computers are fast, but that's still a reasonable challenge if you want a sub-second response (especially when most newsletter HTML isn't exactly designed with the outmost care to lightness).
Just look at
[how slow that was on even a modern Android phone](https://twitter.com/heyhey/status/1395038283839770629)
, which is shown in the gif on the left. On the right, we're running the new version where the initial load is turned into a two-parter. Night'n'day difference. Now we just load 2 emails on the initial render (even on a tall screen, that'll fill the screen), then immediately load 6 more emails asynchronously as you're reading the first two, so that when you start scrolling, you'll still have the same 8 emails before a pagination break.
We made this staged, endless pagination scheme in HEY using a few different components. First, we use
[geared pagination](https://github.com/basecamp/geared_pagination)
to load first 2, then 6 (right after the page is loaded), then 9 (once you scroll down), and then 12 emails per page (as you keep scrolling). This means the first loads are faster when you're just reading them in order, but we'll load ever more, as you might be scrolling a lot to search for something (someone using HEY might have hundreds of emails in The Feed – although hopefully they're
[now recycling them](https://world.hey.com/dhh/hey-will-soon-let-you-recycle-your-emails-9ea2890d)
regularly!).
Second, we use a
[Stimulus-based](https://stimulus.hotwire.dev/)
[pagination controller](https://gist.github.com/dhh/f459dfc3455d2376ce3a7ecb026e6fdf)
, which employs an
[IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
to look for a page link tag to be scrolled into view, then triggers the pagination request, and automatically appends the new emails to the existing container.
This combination means that the server-side code can essentially be written oblivious to the fact that pagination is going on. There's no separate, special return for subsequent pages compared to the first. We just return the whole thing, and the pagination controller does the work to append what's new to what's already there.
Ultimately, this is all about improving the perceived speed. We still end up loading and rendering the same number of emails, but by doing it in intelligent chunks, preloading some, paginating the rest, we can make a dramatic improvement to how the feature feels.
That's really the essence of performance design for most web apps. Optimize that first rendering where people are literally just waiting, then do more of the work when they don't care what the computer is doing in the background.
