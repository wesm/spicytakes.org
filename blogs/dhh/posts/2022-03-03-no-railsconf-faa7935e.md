---
title: "No RailsConf"
date: 2022-03-03
url: https://world.hey.com/dhh/no-railsconf-faa7935e
slug: no-railsconf-faa7935e
word_count: 1526
---

2021 was an incredible year for Ruby on Rails. We started it off still celebrating
[the third major version of Ruby](https://www.ruby-lang.org/en/news/2020/12/25/ruby-3-0-0-released/)
, and left it with the accomplishment of
[the seventh major version of Rails](https://rubyonrails.org/2021/12/15/Rails-7-fulfilling-a-vision)
. Together, these releases sparked a renewed enthusiasm for building modern web applications with Ruby on Rails, unlike anything I can recall since the late oughts. The moment was
[finally right](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
, and we were right for the moment.
I spent most of my time last year advancing the new vision of Rails on the frontend with a slew of projects. The biggest lift was getting the dream of a Node-free default Rails approach validated, solidified, and production ready.
I worked to make that happen by creating
[importmap-rails](https://github.com/rails/importmap-rails/)
, and by
[taking HEY to this new frontier](https://world.hey.com/dhh/hey-is-running-its-javascript-off-import-maps-2abcf203)
as a confirmation that we'd crossed the chasm from vision to reality. Collaborating with Guy Bedford on his crucial enabling work with
[es-module-shims](https://github.com/guybedford/es-module-shims)
.
As a result, we really did manage to dramatically
[compress the complexity](https://m.signalvnoise.com/conceptual-compression-means-beginners-dont-need-to-know-sql-hallelujah/)
of both getting started with Rails, and making those high-fidelity apps that rely on modern JavaScript.
This happened concurrently with the effort to have
[Rails adopt Hotwire](https://world.hey.com/dhh/rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b)
as a replacement for the old Turbolinks and Rails UJS combo. Giving every new Rails app
[the power of Turbo 7 and Stimulus 3](https://world.hey.com/dhh/stimulus-3-turbo-7-hotwire-1-0-9d507133)
as standard, without having to deal with a node_modules directory of thousands of dependencies or webpack configurations up the wazoo. I built
[turbo-rails](https://github.com/hotwired/turbo-rails)
and
[stimulus-rails](https://github.com/hotwired/stimulus-rails)
to make the integration seamless with the JavaScript frameworks we'd spent years developing at Basecamp.
Between getting rid of Node, forging a part with import maps, and committing to Hotwire, the default frontend story for Rails became complete and compelling unlike anything we've ever had before. No more excuses or apologies for the rabbit hole that Webpacker could often be or the limitations of Sprockets.
While this new, daring default path for Rails 7 turned out to be a bull's eye hit, I'm almost as proud of the improvements to the alternate route as well. There are many reasons why someone would
*want*
to embrace Node, transpiling, bundling, and the rest of the complexities inherent with the traditional JavaScript path. Whether that be because the entire UI is written in React, Vue, or whatever, this approach isn't going anywhere, and Rails should have first-class affordances. Now it does!
With
[jsbundling-rails](https://github.com/rails/jsbundling-rails/)
, I created a bridge between a fully "native" JavaScript experience and our Rails asset pipeline. Free from being hardcoded to webpack and a particular configuration of that, Rails 7 has made it trivial to use all of the major bundlers, including esbuild and rollup.js. But perhaps in particular esbuild, which has emerged as the most promising solution with incredibly fast compilation and simpler configuration.
I then followed the crumbs of compression from jsbundling-rails and created
[cssbundling-rails](https://github.com/rails/cssbundling-rails/)
. Which leaned on the same insights and simplifications to make integrating with Tailwind CSS, Bootstrap, PostCSS, and Dart Sass a turn-key operation. Embracing the fact that many of these modern CSS frameworks require a full JavaScript setup for detailed configuration and integration.
So whether you want to go Node-less, full Node, or no front-end inside the Rails app at all, we now have
[stellar answers for every choice](https://world.hey.com/dhh/rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b)
.
[That's a big tent!](https://rubyonrails.org/doctrine#big-tent)
Which means that more people in more situations can enjoy and collaborate on the parts of Rails that we all love and share. Active Records and Action Controllers pair perfectly with all the options.
As if that wasn't enough, I was really happy to finally crack the nut of a proper Redis abstraction in Rails together with Kasper Timm Hansen. We've been using Redis for a very long time at Basecamp, but always at a surprisingly low level. Then suddenly, emerging from the work we'd done in HEY and Basecamp, the right abstraction appeared, and the result became
[Kredis](https://github.com/rails/kredis)
. Now an official second-party framework to Rails, and suggested in the default Gemfile.
To properly commemorate all this delightful progress, as well as capture the energy and enthusiasm of the reception, I worked with our new designer Sean Mitchell at Basecamp to create
[the first new Rails site in six years](https://rubyonrails.org)
. With a fresh identity, bootscreen, and introduction video. It looks great, and perfectly capped off this monumental effort to set Rails on a new course.
And these are just the projects and improvements that hit primetime in 2021! I also spent the year charting a direction for compounding compressions to come in Rails 8, and beyond.
Our trusted asset pipeline, Sprockets, has been long in the tooth, underdeveloped, and overcomplicated for our needs today for too long. To remedy that for tomorrow, I created
[Propshaft](https://world.hey.com/dhh/introducing-propshaft-ee60f4f6)
as a clean-sheet implementation of an asset pipeline built for the challenges we face in 2021+. And then worked with Breno Gazzola to make that production ready faster than I had imagined (we're already running on Propshaft in production with HEY!).
This led directly to the development of
[tailwindcss-rails](https://github.com/rails/tailwindcss-rails)
and
[dartsass-rails](https://github.com/rails/dartsass-rails)
. Two wrap-the-standalone-executables gems that make using the full power of Tailwind CSS and Dart Sass possible with a Node-less application, and specifically designed for Propshaft (since it doesn't have a built-in Sass compiler, unlike Sprockets). Mike Dalessio was instrumental in setting up the gem-by-platform encapsulation, and I can't thank Adam Wathan and the Tailwind team enough for heeding my pleas to wrap Tailwind CSS 3 as standalone version we wouldn't need Node for.
While these developments are already suitable for those who enjoy life at the frontier, I'm even more excited to get them to a place where they can become stronger, perhaps default, recommendations going forward. But that's chatter for a Rails 7.next or Rails 8 discussion. Point is that all of this was conceived, coordinated, and built in 2021.
What. A. Year.
So imagine my surprise when I got this email from the folks at Ruby Central, who've been organizing RailsConf, the conference I helped kick off in 2006:

> *Hi David,
> Hope you’ve been well.
> With you having been mostly offline the last year, the program committee has decided it would be valuable for the community to start sharing the opening keynote stage with other contributors. We have a few in mind but if you have any suggestions of people who have been impactful this year, please share them.
> If you have any questions, please let me know.
>  - Evan*

It's a real shame that this is the world we find ourselves in now. One so sharply divided by politics and ideology that we can't even share the love of Ruby on Rails together at a conference without a need to settle scores.
But I guess it shouldn't come as a surprise. The way
[the debacle around the announced web3 track](https://twitter.com/railsconf/status/1489311414237884419)
at RailsConf was handled was just one illustration that this is where we are now. That an interest in learning and exploring new technologies first need to pass a partisan filter, and if it doesn't, there's hell to pay and groveling apologies to be made. No matter whether that's a space that has activity from some of the largest Rails apps and employers.
What does "you having been mostly offline the last year" even mean? Is there a pious tweet minimum? What does that have to be with being "impactful" with the work? I know, trying to deduce an inner logic of an obvious pretext is a fool's errand.
But it also casts an unfortunate shadow of uncertainty over the whole event. Should companies that support RailsConf by sending employees, speakers, or sponsorship money expect retaliation or exclusion if they end up transgressing against whatever shrinking ideological ring surround the organizers or program committee?
Would GitHub have faced such retaliation if
[the ICE controversy](https://github.blog/2019-10-09-github-and-us-government-developers/)
had broken today? Would Shopify employees have been denied stage time if the Breitbart issue had happened now? Is a company like Coinbase or Block or even Shopify welcome at all
[given their involvement](https://www.shopify.com/nft)
with crypto and web3?
Either way, while it's a shame that the organizers and program committee for RailsConf have chosen this path, it's not going to dim my enthusiasm for Ruby on Rails and our bright future in the slightest. There's so much exciting energy right now, and I have more motivation for pushing our framework forward than I've had in many years. I'll be thrilled to share my yearly keynote with everyone either at another in-person conference this year or online.
With close to twenty years of involvement in this community, I'm confident we'll be able to eventually route around the fractious politicization that's been leaking into our proceedings. I don't believe that this is what most programmers or most companies ultimately want. But it's a perilous time to reveal preferences, so I fully understand why many choose to duck instead.
For me, this work has always been a labor of love. It's so gratifying to see new programmers
[realize what they can build,](https://world.hey.com/dhh/the-one-person-framework-711e6318)
and existing Ruby on Rails companies reach the skies. Nothing can detract from that. Cheers to another two decades and beyond of open source collaboration, beautiful code, and happy programmers!
✌️❤️
