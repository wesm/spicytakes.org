---
title: "Five big open source gifts from us"
date: 2023-12-20
url: https://world.hey.com/dhh/five-big-open-source-gifts-from-us-c1b42c1b
slug: five-big-open-source-gifts-from-us-c1b42c1b
word_count: 1705
---

It’s been an incredibly productive year at
[37signals](https://37signals.com)
. Perhaps our most productive one yet, in terms of total number of product improvements, new product developments, and open source extractions. But it’s only by looking back at the work from a distance that you can really appreciate it. So allow me to do that here. To appreciate the banner year of programming productivity that was 2023 at our company.
Before I get into the actual open source gifts we were able to share this year, though, I think it’s important to remark on the fact that 37signals is not an open-source software company. In the sense that we don’t make money from open source. We don’t sell service, hosting, training, or licenses. None of that stuff. We sell business software.
Our main products are the project management tool
[Basecamp](https://basecamp.com/)
and our email system
[HEY](https://hey.com.)
. And this year we’ve also finished a brand new calendar system that’ll go together with HEY, which will be released shortly, as well as an entirely new product category for us with
[the ONCE suite](https://once.com/)
, where the first application just went into a private beta release. Alongside
[an avalanche of product improvements](https://updates.37signals.com)
for Basecamp and HEY Email.
It’s from these real-world products and services that we extract our open source gifts. We don’t do speculative software development here. All these tools and frameworks have been forged in the fire of real customer usage, pressure, and demands. We build what we need to do what’s required. No more, no less.
Here are the five big open source gifts we made this year:
[Kamal](https://kamal-deploy.org)
We moved
[out of the cloud](https://world.hey.com/dhh/the-big-cloud-exit-faq-20274010)
in 2023. Took our three million-dollar cloud budget and more than cut it in half by buying our own hardware and running it ourselves. To do this, we built our own deployment tool on top of Docker called
[Kamal](https://kamal-deploy.org)
. It made it easy for us to handle our bare metal boxes with the same ergonomics we’d become accustomed to in the cloud. It’s already spawned
[a vibrant community of external contributors](https://github.com/basecamp/kamal)
reaping the simplicity and savings we’ve seen.
It's the realization that while Kubernetes and other tools have brought great sophistication and standardization to the world of hyperscalers, there's also a need for simpler offerings with a much (MUCH!) lower learning curve. You shouldn't need a PhD in container orchestration to be able to deploy applications in HEY or Basecamp or even something smaller. Kamal is the result of taking two steps back from the industry standards and say "do we really need all this?".
It's also a commitment to the idea of open source that doesn't require a service company to work. Our incentive with Kamal was to make something so simple that
[you wouldn't need a SUSE](https://world.hey.com/dhh/the-only-thing-worse-than-cloud-pricing-is-the-enterprisey-alternatives-854e98f3)
or whoever to figure it out and be confident in your deploys.
[Solid Cache](https://github.com/rails/solid_cache)
The quickest path to a fast application is by judicious caching. That goes for all layers of the stack. You should have a big InnoDB cache for your MySQL database to look up indexes and queues in memory. You should cache your web assets for far-future expiry and use fingerprinting to bust them. And you should cache the server-side rendered HTML fragments that don’t change.
That last part is where Solid Cache come in. We’ve been using Redis to cache server-side HTML fragments since forever. The big breakthroughs in that domain came with key-based expiration over a
[decade](https://signalvnoise.com/posts/3113-how-key-based-cache-expiration-works%20Russian%20Doll%20Caching)
[ago](https://signalvnoise.com/posts/3112-how-basecamp-next-got-to-be-so-damn-fast-without-using-much-client-side-ui)
. The
[Russian-doll caching approach](https://signalvnoise.com/posts/3690-the-performance-impact-of-russian-doll-caching)
is still the best way to cache deeply in Rails.
But as well as this works, it’s limited by the amount of RAM you have available for caching. So given the fact that modern SSD drives have gotten so incredibly, bonkers fast, we thought storing these fragments on disk rather than in memory would not only be good enough, but far better. Turned out to be true!
We are
[now storingmonthsworth of fragment caches](https://dev.37signals.com/solid-cache/)
for Basecamp and HEY at a sliver of the cost our old Redis-based system could do. This means faster response times, it means easy encryption of sensitive content, and it means fewer moving parts.
Solid Cache plugs right into the Rails caching framework, so it’s essentially a no-config change for the majority of Rails applications out there.
Checkout the
[in-depth presentation of Solid Cache](https://www.youtube.com/watch?v=wYeVne3aRow)
from Donal at Rails World for more.
[Solid Queue](https://github.com/basecamp/solid_queue)
Like with caching, we’ve been using a Redis-backed job queueing system for ages at 37signals. It’s called Resque, and over the years it’s grown a million tentacles and hot patches to deal with the demands of processing over a hundred million jobs every day. We had no fewer than 7 different Resque-related gems in our Gemfiles, and still had yearnings for more observability and insight.
So we thought: If modern SSDs are good enough for caching, they’re probably also now good enough for queuing. And yes, yes they are. Especially given recent advances in database technology, specifically the SKIP LOCKED syntax available in MySQL 8+ and PostgreSQL 9.5+.
That thesis has panned out as well. We’re now running millions of jobs through Solid Queue where they can benefit from ACID transactional guarantees, increased observability, and the fresh breeze of a clean-sheet design based on more than a decade’s worth of hard-won lessons in queuing at scale.
We built Solid Queue from the outset with the goal that it could become the new default queuing backend for Rails 8. So even though it works best with MySQL 8+ and PostgreSQL 9.5+ due to their support for SKIP LOCKED, it’ll also work at lower levels of throughput with SQLite. Meaning that all the default Rails databases are accounted for. Rails 8 will no long be BYOQ (Bring-Your-Own-Queue). Jobs will just work out of the box. Nice!
[Strada](https://strada.hotwired.dev)
[Hotwire](https://hotwired.dev)
, our alternative suite of JavaScript frameworks for building modern web applications, has been on an absolute tear in 2023. It seems that a lot of folks finally realized that the future of the web doesn’t have to be built by sending JSON back and forth. You can actually send HTML straight from the server to the browser, sprinkle some Stimulus controllers on a navigation flow powered by Turbo, and end up with amazing applications that use but a tiny sliver of the front-end code assumed necessary today.
Strada brought the final piece of that puzzle when it comes to native, mobile applications. It lets you create fully native controls to pair with your hybrid web views. This is how we build the excellent native
[4.7+](https://apps.apple.com/us/app/basecamp-project-management/id1015603248)
[mobile](https://play.google.com/store/apps/details?id=com.basecamp.bc3)
[apps](https://apps.apple.com/us/app/hey-email/id1506603805)
for Basecamp and HEY. They have native controls and trim where it counts, and then use server-side rendered HTML for everything else. With Strada, we can now programmatically drive those native elements straight from the HTML that’s created on the server.
This means we can release new features on the web that’s instantly available with native controls on the apps, without having to wait for App Store approval. It’s a big win in terms of mobile productivity.
Checkout the
[in-depth presentation of Strada](https://www.youtube.com/watch?v=LKBMXqc43Q8)
from Jay at Rails World for more.
**Turbo 8**
[Turbo](https://turbo.hotwired.dev/)
is the heart of Hotwire. It’s the essence of progressive enhancement. You can drop it into your Rails application (or any other type of server-side framework!), change absolutely nothing, and it’ll feel much faster and smoother. If you need even more, you can
[level up with Turbo Frames](https://turbo.hotwired.dev/handbook/frames)
to lazy-load parts of the page or restrict interactions to smaller in-page scopes. And finally, you can control each piece of the DOM over Web Socket (or in response to requests) through
[Turbo Streams](https://turbo.hotwired.dev/handbook/streams)
that’ll let you append, update, delete any element straight from the server. It’s marvelous.
But as we were developing HEY Calendar, we realized that at the outer edges of fidelity, there was room for one more step. That step is morphing. It’s not a new technique, but it’s been refined recently with the
[Idiomorph algorithm](https://github.com/bigskysoftware/idiomorph)
, which has made it much easier to use with HTML fragments that weren’t designed for morphing (like requiring every element to have an id).
The big win is that you get to preserve scroll position and input fields automatically. That’s pretty important on as complicated a UI as a calendar, so having this wrapped in such an easy-to-use form as “redirect to this page, then do a morph” is just perfect.
Turbo 8 is the only thing on this list that hasn’t been fully released yet, but there’s a beta available already, so it’s getting close.
Checkout the
[in-depth presentation of Turbo Morphing](https://www.youtube.com/watch?v=m97UsXa6HFg)
from Jorge at Rails World for more (or
[read about it on our dev blog](https://dev.37signals.com/a-happier-happy-path-in-turbo-with-morphing/)
).
All this was done by a team of 13 Ruby programmers and 7 native programmers. While they moved Basecamp and HEY big leaps forward. And created the new HEY Calendar and ONCE #1. Collaborating from around the world, working remotely. I’m really proud of that.
But it’s also only possible because people who appreciate this work and these gifts help us promote
[Basecamp](https://basecamp.com/)
and
[HEY](https://hey.com/)
. The millions of dollars we invest every year in open source gifts has to come from paying customers of these products and services. Thankfully, both applications typically sell themselves once someone gives them a try, but we still need folks to hear about them.
So a huge thank you to everyone who’ve either bought HEY for themselves or helped a business buy Basecamp. You’re literally enabling all of this. Yes, you! Even if the credit card isn’t coming out of your own wallet, the word of mouth you do to recommend our stuff is absolutely essential.
I don’t know if every year is going to be as spectacularly bountiful as 2023 was, but I promise you that we’ll try. There are so many technological advancements in the HEY Calendar and ONCE #1 that I can’t wait for us to extract and share. The new frontiers
[with PWAs](https://twitter.com/dhh/status/1736421111884288203)
,
[installable apps](https://once.com/)
, and
[#nobuild](https://x.com/dhh/status/1736764094546686331?s=20)
are really exciting. We’ll try our best to continue to push the web forward to a simpler, easier place for new and existing business to build. A world where
[the lone developer remains competitive](https://www.youtube.com/watch?v=iqXjGiQ_D-A)
.
Have a great Christmas and New Year!

![37signals-oss-presents.jpg](https://world.hey.com/dhh/c1b42c1b/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MTQ2OTQ1MCwicHVyIjoiYmxvYl9pZCJ9fQ--5f796a0060c202f907a479543aea30f7046fbe4109da0086f1df38e94664a174/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--b3779d742b3242a2a5284869a45b2a113e0c177f0450c29f0baca1ee780f6604/37signals-oss-presents.jpg)

