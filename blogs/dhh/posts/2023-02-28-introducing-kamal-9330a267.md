---
title: "Introducing Kamal"
date: 2023-02-28
url: https://world.hey.com/dhh/introducing-kamal-9330a267
slug: introducing-kamal-9330a267
word_count: 453
---

It's finally time to talk about the technology we've been building at 37signals to
[leave the cloud](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)
with HEY and many of our legacy applications. We already run Basecamp on our own hardware, but we deploy it using an old tool known as Capistrano. This is the deployment tool we originally wrote at 37signals all the way back in 2005, when we first had to deploy applications to multiple servers. It's been a trusty companion for many years, but it's time is up, and the game has moved on.
[Enter Kamal](https://kamal-deploy.org/)
!
Kamal marries the procedural simplicity of Capistrano with the advantages of modern containerization techniques. It sits on top of basic Docker, and harvests all the benefits you get from isolated containers with a sliver of the complexity associated with most other solutions. Instead of sending the deployment pipeline off to servers in the cloud, it runs entirely on your own machine. Just like Capistrano did.
This makes Kamal really fast. Our sophisticated, Kubernetes backed deployment pipeline for HEY often takes minutes to deploy a new version. Depending on how the underlying images are cached, it can take even longer than that. We've put a fair amount of effort into speeding things up with all sorts of sophisticated techniques, but that's still where we are. With Kamal, we can deploy a new version of HEY in as little as 20 seconds.
But speed is just one factor. The bigger factor, and the reason we wrote Kamal, is because it allows us to use the cloud advantages of containerization on our own bare-metal hardware. There are also just way fewer moving parts. Illustrated here by the +/- on lines of configuration and code with the Kamal pull request for Writeboard:

![writeboard-code-change.png](https://world.hey.com/dhh/9330a267/representations/eyJfcmFpbHMiOnsiZGF0YSI6MTEzMzQ4MjAyMywicHVyIjoiYmxvYl9pZCJ9fQ--057fc5c483458bb728b98a95b2c6b6871d83a4b540918ca0e709bbf3f4d823aa/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJwbmciLCJyZXNpemVfdG9fbGltaXQiOlszODQwLDI1NjBdLCJxdWFsaXR5Ijo2MCwibG9hZGVyIjp7InBhZ2UiOm51bGx9LCJjb2FsZXNjZSI6dHJ1ZX0sInB1ciI6InZhcmlhdGlvbiJ9fQ--7edc7b21f6fad97fa22412618822c4d19725431f296c7ce47dc174b61535d27c/writeboard-code-change.png)

Ironically, Kamal is also a great option, even if you're running in the cloud! It makes your entire system setup vendor independent in a way we never managed to truly achieve with Kubernetes.
This is still beta software. Yes, we're using it in production already, but I'm sure some elements will still move around on the way to v1.0. Which we intend to release in celebration of the last application leaving the cloud at 37signals sometime this summer.
So if you're the adventurous kind, please do jump in, help develop Kamal on its way to a stable release. And if you're less adventurous, consider the video demonstration a teaser of what's to come soon.
It's our gift, as the makers of
[Basecamp](https://basecamp.com/)
&
[HEY](https://www.hey.com/)
, to everyone who'd like
[more independence, to serve the internet, and to spend their money wisely](https://world.hey.com/dhh/five-values-guiding-our-cloud-exit-638add47)
on their infrastructure. As with everything we share, it's entirely free and licensed under the permissive MIT license.
Please enjoy Kamal!
