---
title: "ONCE #1 is entirely #nobuild for the front-end"
date: 2023-12-20
url: https://world.hey.com/dhh/once-1-is-entirely-nobuild-for-the-front-end-ce56f6d7
slug: once-1-is-entirely-nobuild-for-the-front-end-ce56f6d7
word_count: 589
---

The dream has come true. It’s now possible to build fast, modern web applications without transpiling or bundling either JavaScript or CSS. I’ve been working towards this personal nirvana ever since we begrudgingly started transpiling and bundling assets in the late 2000s. Browsers just weren’t good enough back then to avoid it. But they are now.
Here’s a chart of the 68 individual JavaScript files that we load in
[ONCE #1](https://once.com)
via import maps. The waterfall is vertical. HTTP/2 ensures we scarcely pay any penalty for sending so many individual files, yet reap huge rewards with fine-grained cache expiration:

![preload-all.png](https://world.hey.com/dhh/ce56f6d7/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MTg2MjgxNSwicHVyIjoiYmxvYl9pZCJ9fQ--8e47f3d90b899ccd3b27462f00e52993ebe9e39c7f2b97e8d916992b12995cbf/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/preload-all.png)

I know you have to be a real nerd to think this is pretty, but I think this is pretty. Because I know what’s behind it. I know that looking at any of those individual files via
[View Source](https://m.signalvnoise.com/paying-tribute-to-the-web-with-view-source/)
reveals exactly the same source code that I see in my editor. It’s been a long time since JavaScript developers and designers could say that. Now it’s possible.
And yes, this is now true about CSS as well. Here’s the same chart for our CSS. Individual files, relying exclusively on standardized CSS available in the latest evergreen versions of Chrome, Safari, and Firefox:

![css-nobuild.png](https://world.hey.com/dhh/ce56f6d7/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MTg2NTYzNywicHVyIjoiYmxvYl9pZCJ9fQ--682b2c32dcbfaab09264c9a96147599605d137087e1e5fc5757959c271ddb5f8/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/css-nobuild.png)

And look at what that CSS actually looks like:

![image.png](https://world.hey.com/dhh/ce56f6d7/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MTg2Njc5OCwicHVyIjoiYmxvYl9pZCJ9fQ--127e79ec46f0ab5ca8ceaf13f26569174a65ed2426995c90ff7953eb8a2895a0/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/image.png)

To people who haven’t seen modern, vanilla CSS, something like this might look like it’s from the future. Nesting?! Variables?! Yes. Yes. It’s good!
And if you run this application, and all these many, small individual files, against the test of PageSpeed Insights, you’ll get a perfect 100 on the performance measurement. Our browsers are finally good enough to natively deliver the performance and ergonomics needed. Incredible achievement by the teams at Apple and Google and Firefox:

![page-insights.jpeg](https://world.hey.com/dhh/ce56f6d7/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTQ4MTg2Nzg5MSwicHVyIjoiYmxvYl9pZCJ9fQ--2468812f0386b5767599d24eaa6a018e5c97bb7484df189516051d938d9b8332/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJqcGVnIiwicmVzaXplX3RvX2xpbWl0IjpbMzg0MCwyNTYwXSwicXVhbGl0eSI6NjAsImxvYWRlciI6eyJwYWdlIjpudWxsfSwiY29hbGVzY2UiOnRydWV9LCJwdXIiOiJ2YXJpYXRpb24ifX0--86fa621099aa99aa0c7ae156d97d21b387d30fa6ac57aa5c89948af503464a06/page-insights.jpeg)

Now, when some JavaScript people see arguments like this, it seems like their brain just turns into a red mush of rage. Like I’ve insulted their religion and all its holy prophets.
I don’t quite get it, but let me try to ameliorate it anyway: It’s OK to still use bundlers! I’ve been pretty excited about the progress brought forward with esbuild and bun. I think both projects are really cool, and if you’re working on one of those big, honking SPA apps with hundreds or thousands of NPM dependencies, and megabytes of JavaScript that needs to travel over the wire, you should take full advantage of these powerful tools.
All I’m demonstrating here is that it’s no longer necessary to live and work like this. You can choose something different.
[Hotwire](https://hotwired.dev/)
is an alternative.
[#Nobuild](https://world.hey.com/dhh/you-can-t-get-faster-than-no-build-7a44131c)
is an alternative. Nobody is taking your favorite bundler away. TypeScript is still there for those who want that. IT’S ALL GOOD!
What I’m saying is that I’m just incredibly, over-the-moon pleased with the fact that I don’t need any of that stuff any more. That I can develop entirely against the superb runtime that’s shipped with every browser to handle JavaScript and CSS. I think that’s so cool! I think that’s part of what makes the web so special as a development platform.
I don’t even mind having had to travel a long way to get here. I did webpack, I’ve done esbuild, I’ve done all of it along the way. But I’m a firm believer that complexity ought to be a temporary price we pay for progress. The final destination, for me, has always been simplicity. And nothing is simpler than sending a plain-text JavaScript or CSS file straight to a browser and watch the magic play.
Viva the web!
