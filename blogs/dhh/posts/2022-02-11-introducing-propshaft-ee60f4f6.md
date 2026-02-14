---
title: "Introducing Propshaft"
date: 2022-02-11
url: https://world.hey.com/dhh/introducing-propshaft-ee60f4f6
slug: introducing-propshaft-ee60f4f6
word_count: 697
---

It's an exciting time in web development. After a decade's worth of front-end progress kept demanding ever more complicated setups, we're finally moving in the opposite direction. With simpler tools that are still able to hit those high-fidelity user interface notes, but at a sliver of the cost in complexity. The long expansion of enabling concepts is now at last being compressed for human comprehension. Hallelujah!
And like with expanding complexity, where one complication often leads to another, compressing complexity also cascades.
[Propshaft](https://github.com/rails/propshaft)
, a new asset pipeline library for Rails, is the result of such a cascading compression of complexity. Enabled by
[the same trifecta](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
of HTTP/2, browser-run ES6, and import maps that powers
[Rails 7](https://rubyonrails.org/2021/12/15/Rails-7-fulfilling-a-vision)
, Propshaft is dramatically simpler than the Sprockets that went before it.
In our modern asset world, JavaScript and stylesheets are either
[sent directly to the browser without preprocessing](https://github.com/rails/importmap-rails)
, or they're being preprocessed by standalone tools like
[esbuild](https://github.com/rails/jsbundling-rails/)
,
[Dart Sass](https://github.com/rails/dartsass-rails)
, and
[Tailwind CSS](https://github.com/rails/tailwindcss-rails/)
. In both cases, our asset pipeline library needn't lift the burden.
[Sprockets](https://github.com/rails/sprockets)
, the current default asset pipeline library for Rails, was forged in the flames of HTTP/1, browsers that only supported ES3, and a limited JavaScript tooling stack from back in the late oughts. It had to do all the heavy lifting itself with transpiling, bundling, minifying, and compression.
That's a lot, so Sprockets grew large to handle all these responsibilities, but also spread itself thin. It's hard to keep up with the state of the art on all these fronts at once, and while valiant attempts were made, it kept falling behind on everything from Sass compilation to understanding ESM dependencies.
So far we've just routed around these deficiencies. The core of Sprockets still adequately serves Rails 7 as the default setup for providing a load path, digesting assets, and handling the outputs from other bundlers and transpilers. But it's doing so carrying an awful lot of baggage in the form of unused pipelines and underdeveloped features.
That's where Propshaft comes in. It was written on a clean sheet of paper to carry only what we need in the year of our lord 2022. A realm with HTTP/2, ES6, import maps, and a mature set of standalone transpilers and bundlers. Not surprisingly, it's absolutely tiny compared to Sprockets. Which means simpler to understand, fewer moving parts that can break, and conceptually tighter.
At its core, Propshaft seeks to provide just the configurable load path where assets can live in app/assets, lib/assets, vendor/assets, and inside of gems, alongside the digest stamping and URL rewriting needed for far-future cache expiration. All this accessible through either static precompilation in production or a thin dynamic server in development.
There's still more work to be done on Propshaft before it's fully able to take over the reins from Sprockets as the default asset pipeline in Rails, but we're fast moving closer.
[HEY](https://www.hey.com/)
just went into production yesterday with a Propshaft +
[Dart Sass](https://github.com/rails/dartsass-rails)
combination to fit alongside its existing use of
[import maps](https://github.com/rails/importmap-rails)
. Early Propshaft contributor
[Breno Gazzola](https://github.com/brenogazzola)
has also already launched production apps on Propshaft.
You can start new Rails 7 applications directly on Propshaft rather than Sprockets with "rails new -a propshaft myapp" or
[checkout the guide](https://github.com/rails/propshaft/blob/main/UPGRADING.md)
to migrating from Rails 6 apps running Webpacker, if you'd like to help us refine the future of asset pipelining in Rails.
The biggest hurdle is likely to be that many gems are written to depend on Sprockets offering everything from CoffeeScript to Sass compilation out of the box. Those gems will need to be updated or we'll need to find ways of offering backwards compatibility. This isn't a quick migration, and there's no prospect of considering Propshaft as the new default until Rails 8.
But it's really exciting to see how when we manage to make one aspect of Rails dramatically simpler (bye-bye Webpacker), we can often make another part much simpler too (hello Propshaft). The battle against complexity in web development is a constant tug of war. We give a little to get something new, we take it back to make it simpler.
Progress is good. Complexity is a bridge. Simplicity is the destination.
