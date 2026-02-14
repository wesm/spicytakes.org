---
title: "You can't get faster than No Build"
date: 2023-10-11
url: https://world.hey.com/dhh/you-can-t-get-faster-than-no-build-7a44131c
slug: you-can-t-get-faster-than-no-build-7a44131c
word_count: 276
---

For the first time
[since the 2000s](https://www.youtube.com/watch?v=cGdCI2HhfAU)
, I'm working on a
[new Rails application](https://once.com)
without using any form of real build steps on the front-end. We're making it using vanilla ES6 with
[import maps](https://github.com/rails/importmap-rails)
for
[Hotwire](https://hotwired.dev)
, and vanilla CSS with
[nesting](https://caniuse.com/css-nesting)
and
[variables](https://caniuse.com/css-variables)
for styling. All running on a delightfully new simple asset pipeline called
[Propshaft](https://world.hey.com/dhh/introducing-propshaft-ee60f4f6)
. It's all just so... simple.
It's also fast. Really fast. Infinitely fast. Here's a tongue-in-cheek slide I featured as part of
[my Rails World keynote](https://www.youtube.com/watch?v=iqXjGiQ_D-A)
last week talking about this No Build process:

![no-build-speed.jpg](https://world.hey.com/dhh/7a44131c/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTM5MTk4NzM3OSwicHVyIjoiYmxvYl9pZCJ9fQ--529c659f3aecd840ac9b8e6dd3e1b21d36d6adc3c936d451a223a709a42bf996/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--b3779d742b3242a2a5284869a45b2a113e0c177f0450c29f0baca1ee780f6604/no-build-speed.jpg)

Now I fully understand why someone might want to use esbuild or bun, and I've gone out of my way to work on
[great tooling](https://github.com/rails/jsbundling-rails)
for Rails to make that really easy. Rails 7.1 ships with
[native support for bun](https://rubyonrails.org/2023/10/5/Rails-7-1-0-has-been-released#support-for-bun)
in the box, and esbuild is already compiling JavaScript for lots of Rails applications in production (including Basecamp!). These are great tools, and I'm thrilled they work so well with Rails.
But for the first time in probably 15 years,
[the state of the art](https://world.hey.com/dhh/modern-web-apps-without-javascript-bundling-or-transpiling-a20f2755)
is no longer finding more sophisticated ways to build JavaScript or CSS. It's not to build at all. To lean on HTTP/2 and the now
[universal support for import maps](https://caniuse.com/import-maps)
to avoid bundling, and to lean on the fundamental progress in support for modern JavaScript and CSS to avoid compiling what browsers already know how to read.
If you aren't wedded to React, Vue, or whatever, you should have a look at what's possible to build with Hotwire and No Build these days. You just might want to shed the weight of complexity and enjoy the lighter stack.
