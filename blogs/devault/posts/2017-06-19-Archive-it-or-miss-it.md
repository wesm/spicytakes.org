---
title: "Archive it or you will miss it"
date: 2017-06-19
url: https://drewdevault.com/2017/06/19/Archive-it-or-miss-it.html
slug: Archive-it-or-miss-it
word_count: 367
---

Let’s open with some quotes from the  [Wikipedia article on link
rot](https://en.wikipedia.org/wiki/Link_rot) :

> In 2014, bookmarking site Pinboard’s owner Maciej Cegłowski reported a “pretty
> steady rate” of 5% link rot per year… approximately 50% of the URLs in
> U.S. Supreme Court opinions no longer link to the original information…
> (analysis of) more than 180,000 links from references in… three major open
> access publishers… found that overall 24.5% of links cited were no longer
> available.

I hate link rot. It’s been common when servers disappeared or domains expired,
in the past and still today. Today, link rot is on the rise under the influence
of more sinister factors. Abuse of DMCA. Region locking. Paywalls.  Maybe it
just no longer serves the interests of a walled garden to host the content.
Maybe the walled garden went out of business. Users rely on platforms to host
content and links rot by the millions when the platforms die. Movies disappear
from Netflix.  Music vanishes from Spotify. Accounts are banned from SoundCloud.
YouTube channels are banned over false DMCA requests issued by robots.

At this point, link rot is an axiom of the internet. In the face of this, I
store a personal offline archive of  *anything*  I want to see twice. When I see a
cool YouTube video I like, I archive the entire channel right away. Rather than
subscribe to it, I update my archive on a cronjob. I scrape content out of RSS
feeds and into offline storage and I have dozens of websites archived with wget.
I mirror most git repositories I’m interested in. I have DRM free offline copies
of all of my music, TV shows, and movies, ill-begotten or not.

I suggest you do the same. It’s sad that it’s come to this. Let’s all do
ourselves a favor. Don’t build unsustainable platforms and ask users to trust
you with their data. Pay for your domain. Give people DRM free downloads. Don’t
cripple your software when it can’t call home. If you run a website, let
archive.org scrape it.

And archive anything you want to see again.

```
0 0 * * 0 cd ~/archives && wget -m https://drewdevault.com
```
