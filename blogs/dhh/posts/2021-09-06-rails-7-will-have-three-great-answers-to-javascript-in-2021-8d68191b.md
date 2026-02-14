---
title: "Rails 7 will have three great answers to JavaScript in 2021+"
date: 2021-09-06
url: https://world.hey.com/dhh/rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b
slug: rails-7-will-have-three-great-answers-to-javascript-in-2021-8d68191b
word_count: 1528
---

Rails has been unapologetically full stack since the beginning. We've continuously sought to include ever-more default answers to all the major infrastructure questions posed by modern web development. From talking to a database, to sending and receiving emails, to connecting web sockets, to rendering HTML, to integrating with JavaScript. This full-stack strategy has been key to the success of Rails, but it also remains an enduring source of controversy. What's too much to include? What's not enough?
To consistently answer that evergreen question, we look to
[The Rails Doctrine](https://rubyonrails.org/doctrine)
, and especially the third pillar of
[The Menu Is Omakase](https://rubyonrails.org/doctrine/#omakase)
. It's why we fret so much over the defaults, but also why the option to substitute is so crucial.
There's been no more fretting over the defaults, or a closer examination of the substitutes, than with the JavaScript part of the question over the years. And especially lately, as the ever-present churn and fundamental change has pushed new options into the limelight. But after much experimentation, I believe we now have a solid answer for Rails 7.

# Rails 7 will default to import-mapped Hotwire

With Rails 7, we're replacing Webpacker, Turbolinks, UJS with
[import maps](https://github.com/rails/importmap-rails)
plus
[Turbo](https://turbo.hotwired.dev/)
and
[Stimulus](https://stimulus.hotwired.dev/)
from
[Hotwire](https://hotwired.dev/)
as the defaults. It's the most comprehensive answer we've ever shipped in the box. Turbolinks + UJS provided a good baseline for making apps feel like they had that single-page-app snappy, but as soon as you needed to do anything dynamic beyond that, it was pretty much Bring Your Own JS-FU.
Hotwire is far more ambitious. Turbo has taken the Turbolinks basics and gone much further with form submissions, frames, and streams. Now you really can get away with creating the bulk of your dynamic elements with just Turbo (without writing any custom JavaScript!). Then on top of that, there is Stimulus, the modest JavaScript framework for the HTML you already have (by generating it from Rails server side views). It's a complete alternative to heavy JavaScript client-side apps that speak JSON to a backend.
This Hotwire setup is then served via HTTP2, ES6/ESM, and import maps in Rails 7. I've already explained in depth
[why this triple threat is a game changer for the modern web](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
, so I won't repeat those arguments here. I'll only repeat the summary that these technologies together with Hotwire and
[JavaScript CDN-based package management](https://github.com/rails/importmap-rails#using-node-modules-via-javascript-cdns)
are the real deal. I offered a tour of how it all works together in this
[Alpha preview: Modern JavaScript in Rails 7 without Webpack](https://www.youtube.com/watch?v=PtxZvFnL2i0)
.
We've been running a version of
[HEY](https://hey.com/)
on this stack for a few weeks, and it's a peach (full report and rollout coming soon!). No separate watch process needed for builds, no wrestling with configs, instant reloads, none of the node tooling needed at all, with no overall loss of performance or capability. It's the best of all worlds – for us at Basecamp.
I say "for us" because HEY was obviously developed with this vision in mind. It was never packed full of thousands of JavaScript files (we ship about ~130 in the browser-based ESM version). It never used transpiler-requiring code, like JSX. It was where Hotwire was honed for release. So I guess it's kinda an OF COURSE that it works great here.
But at the same time, HEY is no aberration. In fact, the fidelity level sought with HEY as a modern web application is right up there. This is an application that competes head-to-head with Gmail, which for eons has been held up as the kind of application you
*definitely*
wanted to build with thick client-side frameworks, JSON peddling, and all the latest transpiler tricks.
Yet Gmail downloads about three
*megabytes*
worth of JavaScript to render its inbox. HEY downloads less than sixty
*kilobytes*
. If you can build a Gmail rival with this stack, and have it be met with broad applaud by tens of thousands of paying customers, you can probably build just about anything with it.
That means it's a great choice for the default stack in Rails.

# Rails 7 has full support for traditional JS bundling

But another Rails doctrinal pillar is that we're trying to
[push up a big tent](https://rubyonrails.org/doctrine/#big-tent)
. Hotwire and import maps will emphatically not be The Answer for everyone. It's a great answer. It's the default answer. But it's not the only answer. Rails needs to be a wonderful framework for developing traditional single-page JavaScript applications – complete with client-side routing, heavy state management, and all the other complexities of that style. And it's going to be.
So in Rails 7, we're simultaneously offering a great, default way to avoid dealing with the entire node/npm/bundling setup
*and*
offering a fully-supported alternate route that embraces all of those things. But we're going to do it in a different way than before.
[Webpacker](https://github.com/rails/webpacker/)
was born almost five years ago with a mission to make the JavaScript bundling pipeline easy to use for Rails developers who weren't necessarily interested in becoming JavaScript experts. With ES6 requiring transpilation for widespread use in browsers at the time, and npm needed to access the ecosystem of packages for node, there really wasn't a way around it. We could either embrace that reality or relegate Rails to only being an API for such applications.
[We chose the embrace](https://weblog.rubyonrails.org/2017/2/23/Rails-5-1-beta1/)
.
But today the trade-offs made for Webpacker are starting to make a lot less sense. It's sorta stuck in the muddy middle between two clearer paths. There's the new path of forgoing the bundling pipeline altogether, which is much easier to setup, has fewer dependencies, and less awkward divisions of labor between Ruby and JavaScript. And then there's the all-in path where we don't try to hide or wrap the JavaScript complexities at all. We simply provide a bridge by which the generated JavaScript can be used in the Rails application, but leave it to the JavaScript ecosystem to provide all the answers.
I wrote the initial version of Webpacker, and we've used it to good effect in both Basecamp and HEY, and it's served the community well as a transition phase between then and now. But I don't see the trade-offs made five years ago serving the present or the future well.
Instead, Rails 7 is going to offer an alternate path that is much slimmer, and far more conventional in terms of the JavaScript world. You develop your JavaScript by keeping your source in app/javascript, running build scripts via package.json definitions, and then hand off the final builds to the asset pipeline in app/assets/builds, so they can be digest-stamped, CDN-prefaced, and served in the app. This is the approach taken by the
[jsbundling-rails](https://github.com/rails/jsbundling-rails)
gem.
This gem provides the basic setup required for esbuild, rollup.js, or Webpack. It installs the baseline dependencies for the chosen bundler, prepares a config file where appropriate, and leans on the twin conventions of a default entry point in app/javascript/application.js and builds placed in app/assets/builds. That's it! The responsibility for managing and updating dependencies flows to the developer.
It's this path you should probably pick if you're going all-in on something like React with JSX or another JavaScript framework that demands a transpilation step.
[You can do React with import maps](https://www.youtube.com/watch?v=k73LKxim6tw)
, but it'll be through htm, and that might well be a compromise too far for those who are all-in.
If you're on Webpacker today, it's a very modest jump to switch to one of the bundlers made available through the jsbundling-rails gem. You don't even have to stick with Webpack. Fundamentally, they all work in the same way: take an entry point, produce a build. We've initially taken that path with Basecamp 3, converting from Webpacker to esbuild. But with HEY, we took the full step of going straight to import maps. Neither choice involved a lot of effort. The JavaScript is still the JavaScript. You're mostly adjusting a few import paths.
If you don't already have a strong preference, but you know you need a bundler, I'd encourage you to start with esbuild. It's hella fast, and ships preconfigured for JSX and even TypeScript.

# Rails 7 will have three clear choices for JavaScript

Finally, you have the option of simply using Rails as an API. Keeping the single-page JavaScript application that consumes it in a different project and repository entirely. Rails has supported this path for a long time with --api, and will continue to do so. This is not a path I'd recommend for small-to-medium-sized teams, but if you're inside a large organization committed to making SPAs with high walls between front-end and back-end departments, it might make sense.
So that's the story for JavaScript in Rails 7 and beyond. A default path with Hotwire and import maps, an alternate path using a thin integration with one of the popular JavaScript bundlers, and finally the strict API path with a separate repository for the front-end.
Three solid answers for the reality of modern web development in 2021.
*There'll be an alpha release of Rails 7 out shortly, and we intend to celebrate the final release before year end. Please help us get there by helping to test and improve these releases!*
