---
title: "zappa: an AI powered mitmproxy"
date: 2026-04-15
url: https://geohot.github.io//blog/jekyll/update/2026/04/15/zappa-mitmproxy.html
slug: zappa-mitmproxy
word_count: 454
---

Soon, AI will be good enough to interact with the Internet in an indistinguishable way from a human. This can be an amazing opportunity for liberation from all the people who are  [targeting your attention](https://aeon.co/essays/what-we-think-is-a-decline-in-literacy-is-a-design-problem) .

I vibe coded this  `zappa`  proxy, it is not quite there yet, but I think it points the way forward. Why should I browse the Internet or use apps when machines can do it for me? Suckers getting billed for an ad impression from a 1 cent Qwen.

Instead of the source, I’ll include the prompt in this post. I used GPT-5.4 to code it.

Download mitmproxy and configure Firefox to use a SOCKS5 proxy and install the required cert to proxy HTTPS traffic. Write a plugin for mitmproxy to route all website traffic through Qwen using the Cerebras API, you need to proxy HTML, JS, and CSS. Tell Qwen to remove all ads, popups, bright colors, moving things, and enshittified crap from the website and return a good version of the site. Pass this good version back to the user through the proxy. Log everything to a file. If the AI returns an error, pass that error along to the user, do not return pages without AI transformation.

I disabled uBlock Origin for these tests, Chrome on the left is the default internet, Firefox on the right is using the proxy if by some crazy chance you couldn’t tell.

The right way to ship this is probably a browser extension in some browser that didn’t totally nerf extensions. It should be simple with a customizable prompt, then people can share prompts like they share uBlock Origin filter lists. And it should be agentic, it shouldn’t actually return the HTML, it should use tools and keep per site state. Imagine a skilled software engineer running in 100x real time cleaning up websites for you before you view them.

Don’t fall for AI browser crap that’s marketed to you, that’s just them wanting to control your attention better. You need an AI you can trust to fight back!

I hope ad people see the writing on the wall, get scared, and pivot to user aligned business model. Intelligence is about to be dirt cheap, everyone will have a full time lighting fast personal assistant to deal with the enshittified world for them.

And you can say, well they will have a smarter one on the make everything bad side, but if mine is human level and aligned with me they will have to have gone so hard that no actual human in the world can deal with them so yea good luck with that.

The Turing Test is over. Enjoy spending your ad dollars showing things to my Qwen.
