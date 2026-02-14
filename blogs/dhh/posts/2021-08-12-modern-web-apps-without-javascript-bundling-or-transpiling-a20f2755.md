---
title: "Modern web apps without JavaScript bundling or transpiling"
date: 2021-08-12
url: https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755
slug: modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755
word_count: 1399
---

I didn't much care for vanilla JavaScript prior to ES6. Through all of the 2000s, I chased different approaches to avoid writing too much of it. First there was RJS (Ruby-to-JavaScript). Then there was CoffeeScript. Both transpiling approaches that turned more enjoyable-to-write source code into the kind of JavaScript that browsers would execute. It sorta worked.
But it was clearly a clutch. A stop-gap while we waited for browsers to understand a better JavaScript. Though for a while  it looked like that might never happen, and we'd forever be stuck with these clutches!
Thankfully that wasn't so. JavaScript
*was*
improving, and by 2015, the huge jump that is ES6 was finalized. Yet well before that – and well after that! – the Babel transpiler was letting us write this JavaScript of the future.
It was a revelation. Being able to program using this much better JavaScript, well before broad browser support was available. It kinda felt like cheating. Like we were getting something for nothing. That wasn't quite right, though.
Transpiling with Babel ushered in the era of horrendously complicated transpiling pipelines and tooling. Writing the JavaScript of the future wasn't free. The price was an ever expanding web of complexity. This clearly wasn't the finish line.
I'm grateful that tools like Webpack made this transition possible, though. Despite the complexity, it felt worth the bargain. So back in 2016, I created
[Webpacker](https://github.com/rails/webpacker/)
, and in 2017, we shipped
[Rails 5.2](https://weblog.rubyonrails.org/2017/2/23/Rails-5-1-beta1/)
, which embraced this approach to managing JavaScript with Rails.
Five years later, the facts on the ground have finally changed. I no longer believe that this bargain is worth it for most new applications. It's not a dead-end, and there are still certain types of applications where it does make sense (hello react!), but it's no longer a good default for Rails.
The first crucial change is that ES6 is now supported by all browsers that matter. Chrome, Edge, Safari, and Firefox fully support ES6. The last major hold out was IE11, but
[Microsoft mercifully announced its end of life this year](https://www.onmsft.com/news/microsoft-end-support-for-ie11-on-june-2022)
.
This means we don't need a transpiling step to turn ES6 into something that'll run in the browser. It runs just fine, no changes needed. That's huge.
The second crucial change is that HTTP2 is now the norm. With HTTP2, you no longer pay a large penalty for sending many small files instead of one big file. A single connection can multiplex  all the responses you need. No more managing multiple connections, paying for multiple SSL handshakes. This means that bundling all your JavaScript into a single file loses many of its performance benefits (yes, yes, tree-shaking is still one).
In fact, the single-big-bundle pattern is now worse in several ways, not just developer ergonomics (like long bundling times!). When you bundle all your JavaScript modules in a single file, any change to any module will expire the entire bundle. Forcing the browser to download the whole thing anew, parsing everything again. That's bad.
When you keep each module separate, they can expire independently. So if you have 20 modules, and only one change, the other 19 remain cached. This is the kind of caching dynamics that performance enthusiasts crave.
But more importantly for our overall argument is that if you no longer need bundling for performance, you can get rid of the bundler entirely! Simply serve each module directly, as their own file, directly to the browser.
Can you see where we're getting to? No need for transpiling to write the kind of JavaScript that makes you smile, no need for bundling to package all your modules. Taken together: No need for any JavaScript toolchain to turn your source code into anything else. An entire class of complexity stands at the precipice.
The final piece that's pushing the two first crucial changes over the paradigm hill is import maps. They allow the use of logical references for modules in ES6 (also known as ESM), rather than explicit file references. The problem with explicit file references is that they pair poorly with the standard approach of long-life caches with digest-stamped file names.
When you see a filename like main-a6d26cef87d241eba5fa.js, that last bit is a digest of the entire file. It's unique for that specific file, so if we change anything in the file, the digest changes too. This means that we can tell the browser to cache the file with the digest
*forever*
because it'll never change. If it changes, it gets a new file name. This is critical to get good performance with cache expiration dynamics you control.
But imagine if you had 50 files that all had an opening import like "import { Controller } from './javascript/stimulus-a6d26cef87d241eba5fa.js'"? That would suck. You'd have to update each of those files every time you bumped your Stimulus dependency, and all of those files would individually expire when you did!
The answer to this problem is called
[import maps](https://github.com/WICG/import-maps)
, and it's
[a feature already shipping in Chrome and Edge](https://caniuse.com/?search=importmap)
. Firefox has indicated they're looking into it. Safari hasn't said a pip about it. But no matter, there's
[a perfectly workable shim](https://github.com/guybedford/es-module-shims)
available, which implements import map support for all browsers that support ESM (which all the ones with ES6 support do).
With import maps, you define the mapping of imports. So instead of "./javascript/stimulus-a6d26cef87d241eba5fa.js", it's just "stimulus", and then the import map says "stimulus": "/javascript/stimulus-a6d26cef87d241eba5fa.js". If you bump Stimulus, you just change the map, not the references. Voila!
Maintaining the import map by hand is still a bit of a chore, so for Rails, I've created the new
[importmap-rails](https://github.com/rails/importmap-rails/)
gem, which allows you to build the map programmatically, includes the shim so it'll work in all browsers, and it relies on our old faithful asset pipeline engine of Sprockets to do the digesting work. A complete package.
Take the pillars of transpiler-less and bundler-less progress, pair it with a generated import map, and you now have an environment that does not even require you to install node locally to create modern, awesome web apps.
The
[Hotwire](https://hotwired.dev)
gems for Rails, both for
[Stimulus](https://github.com/hotwired/stimulus-rails)
and
[Turbo](https://github.com/hotwired/turbo-rails)
, have already been altered to rely on this setup. The gems use the programmatic access to setup the import map behind the scenes, and in your application.js, you can thus just import the modules directly.
It's hard to convey what a difference it makes to the development experience to cut out this massive tumor of complexity. It feels like a new lease on life. But there are still some unanswered questions and concessions.
As mentioned, the first is that certain popular frameworks like React, which rely on compiling for JSX, just won't work with any of this (yet?). Anything that requires an explicit transpiling or compiling step obviously need a transpiler or compiler. And then you're back to square one.
The second is that while Hotwire, together with the JavaScript in Rails for things like Action Text, Active Storage, and Action Cable, can be made available through Ruby gems and the asset pipeline, there's a great big JavaScript ecosystem we still need better answers for.
This ecosystem needs to publish ESM packages instead of UMD (the old packaging system used by node.js). Though services like
[skypack.dev](https://www.skypack.dev)
could perhaps help bridge the gap by turning UMD packages into ESM.
And Rails needs an answer for how to depend upon these packages and update them, if it's not going to be through a package.json file with npm doing the work. I have some ideas here, but they're not yet fleshed out. In the interim, you can simply download these ESM packages and keep them locally in a vendor/ directory.
So despite how promising this all is, what a real leap forward ES6 everywhere, ubiquitous HTTP2, and import maps combine to present, there's clearly still a class of applications that'll need Webpack (and Webpacker). At least for now. And that's fine. We're moving forward by taking things out. Not everyone can take these things out yet, but those who can will be mightily pleased.
Unless new evidence comes to bear that refutes the basic tenets of this analysis, Rails 7.0 will aim to give you a default setup based on import maps, and leave the Webpacker approach as an optional alternative.
We're way overdue a correction back to simplicity for the frontend. ES6/HTTP2/Import maps looks like they'll deliver just that. Yay hurray!
