---
title: "The Overnight Webcam App"
date: 2026-03-25
url: https://www.danshapiro.com/blog/2026/03/the-overnight-webcam-app/
word_count: 468
---


I’ve been working with teams on applying Dark Factory principles to build software with AI. There are a few tools to do this, but my favorite is [trycycle.ai](http://trycycle.ai). It’s just a skill. You install it by telling your favorite agent:


`Read https://raw.githubusercontent.com/danshapiro/trycycle/main/README.md. Follow the installation instructions there.`


You use it by saying


`build the thing I want with a trycycle`


in Claude Code, Codex CLI, or OpenCode. It’s outrageously simple, works for hours unattended, does what you ask it, and scales from ‘fix this bug’ to ‘deliver a fully featured personal CRM system from this 10-page spec I wrote’ (I did that last night too). It works with just about every AI model you can imagine, from free to Opus and every price point in between.


The idea is simple. Every project has an plan, tests, and code. Trycycle works on the plan until it can’t find any more problems. Then it does it again for the tests. Then it does it again for the code. It checks in once with you before it really gets going. Otherwise, it usually does not bother you until your code is *working.*


So last night I had five projects going. Three were new features for my company’s products. Two are systems to help our company’s operations. One was that personal CRM thing to remind me who I needed to email.


And then my “Canon EOS Webcam Utility Pro” software crashed.


Again.


Like a World War Two bunker on an otherwise beautiful beach, this software monstrosity is a leftover from the depths of covid lockdown, pigging out on memory and processor cycles on my otherwise well-behaved computer with the only goal of repurposing my Canon into an overachieving webcam.


I was not happy.


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/03/image-4.png)


In a fit of irritation, I asked Claude Code how hard it would be to just build the app from scratch in Rust so it would be faster, more stable, and less stupid. Claude asked – could we reuse the DLL file that shipped with it, and scrap everything else?


“Sure”, I said.


“Just 2-3 weeks of work!” Claude told me.


I woke up the next morning and wasn’t quite sure what to expect. What I definitely was not expecting was a fully functional Rust webcam app that worked immediately, with no discernible bugs, that I’ve been using all day.


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/03/image-5.png)


And one more thing: I’ve been burning all my Claude Code and Codex tokens to the ground lately, so I decided to try something new. I did all this in Opencode, using Kimi K2.5 – a perfectly fine, open source, absolutely not frontier coding model, billed by the token.


Total time: Six hours (sleeping)


Total cost: twenty one cents.

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
