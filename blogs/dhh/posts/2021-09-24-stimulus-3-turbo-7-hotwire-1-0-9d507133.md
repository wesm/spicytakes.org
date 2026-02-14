---
title: "Stimulus 3 + Turbo 7 = Hotwire 1.0"
date: 2021-09-24
url: https://world.hey.com/dhh/stimulus-3-turbo-7-hotwire-1-0-9d507133
slug: stimulus-3-turbo-7-hotwire-1-0-9d507133
word_count: 654
---

For so long, it felt like I could only tell half the story of how we make software for the web at Basecamp. Too many of the chapters about our front-end approach were missing key pages. Sure, we had some of it out there. Turbolinks, for example,
[hark back to 2012](https://github.com/turbolinks/turbolinks-classic/commit/879db1489156ed610e74f1befbb67ab5db6ee81e)
, when I was inspired by
[Chris Wanstrath](https://github.com/defunkt)
's ideas in
[pjax](https://github.com/defunkt/jquery-pjax)
, and took them further. And
[Stimulus](https://stimulus.hotwired.dev)
can trace its origin to the Christmas 2016, when I spiked the first concept in an attempt to unify all the JavaScript patterns we had in Basecamp. But it was never... complete. Now it is.
[Stimulus 3](https://world.hey.com/hotwired/stimulus-3-c438d432)
+
[Turbo 7](https://world.hey.com/hotwired/turbo-7-0dd7a27f)
paint the full picture of how my ideal stack for front-end development should look under the umbrella of
[Hotwire 1.0](https://hotwired.dev)
. This is how we're building
[Basecamp 4](https://world.hey.com/jason/the-path-to-basecamp-4-7516ee5b)
. This is
[how we built HEY](https://twitter.com/dhh/status/1275901955995385856?s=20)
. Now it's going to be
[the default answer to JavaScript in Rails 7](https://world.hey.com/dhh/rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b)
together with the new import-map approach. All the missing pages are being printed.
The story is getting out there, too. Three or four years ago, all anyone seemed to be focused on was building single-page applications with ever more complicated bundling pipelines and component frameworks. Babel me this, Webpack me that, React all the things. Today, less so.
If we start backwards, React's hegemony has splintered into a bunch of similar-but-different alternatives with Vue and Svelte. ESM is inspiring people to go
[build-less](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
. And ES6 means we no longer need to transpile to write enjoyable JavaScript.
But it's bigger than that. There's a resurgence in the wisdom of letting HTML be at the center of a web application. Even the React folks are
[getting interested](https://twitter.com/dan_abramov/status/1256652228988997638)
in server-side rendering. We just need a few more of them to realize that HTML is not just good for the first render, it's also great for all the subsequent ones. That's the essence of Hotwire: HTML Over The Wire. Use HTML to render the first page, of course, then use HTML to render the next, then use HTML to send partial updates.
HTML, HTML, HTML!
But it's bigger still than that. It's about spending some of those core advances in web technology to pay off the complexity loans we binged on during the 2010s. That same binge that gave rise to a thousand specialized niche web programmer roles, because nobody could possibly hold it all in their head all at once. That worked just fine for mega corporations like Facebook, but it raised some serious barriers for smaller teams, and made it almost impossible for anyone just starting out to follow "best practices".
We have to get back to the idea that a single developer might dare understand it all. Might do it all. Might build competitive web applications without having to blow their cap trying to cram in ever more complexity. We desperately need more
[conceptual compression](https://www.youtube.com/watch?v=zKyv-IGvgGE&t=1037s)
.
That's what's at the heart of Hotwire. Conceptual compression. After a decade plus of rapid conceptual
*expansion*
, which, along with all the complexity, absolutely brought some real, material advantages, we can reap the key rewards by boiling it down to its essence. Fast, compelling user interfaces that let people get on with the job of... mostly creating, reading, updating, and deleting rows in a database.
Because twenty-five years after I wrote my first web application, that's still mostly what we do! Connecting databases to the web through workflows that help people organize, collaborate, and communicate with information technology. It may not be rocket surgery, but it's good honest work.
And yet, it's also good fun! Wrestling with the pendulum as it swings from conceptual expansion back to conceptual compression. Trying to turn all those real advances into something that's easier to use, more fun to work with. That's the stuff of A Life's Work.
Today that work has a concrete motto: HTML Over The Wire is the way.
