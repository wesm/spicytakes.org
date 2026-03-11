---
title: "I accidentally ported Steve Yegge’s Beads to Windows"
date: 2025-10-21
url: https://www.danshapiro.com/blog/2025/10/accidentally-ported-steve-yegge-beads-to-windows/
word_count: 463
---


Tuesday, 9:40am, Seattle. Whatsapp buzzed. [Harper](https://harperreed.com/) sent a link – a new project from Steve Yegge that makes AI agents more effective. Worth a try.


I opened Codex CLI* in Powershell and said, “Install [Beads](https://github.com/steveyegge/beads)“.


I didn’t read the compatibility notes. I didn’t check to see if it had Windows support. I needed coffee.


### **Spring 2023: BabyAGI incinerates $122.47**


Flashback to spring 2023, peak [BabyAGI](https://github.com/yoheinakajima/babyagi) fever. We were fresh-faced and convinced autonomous agents could solve all of our problems while we contemplated the singularity. Or, at least, willing to give them a whirl and see where the state of the art was sitting.


Fine, BabyAGI. Strut your stuff. “Find me a good, cheap standing desk.”


It started sensibly. It googled standing desks, pulled a few product pages, started comparing features. Then it decided it needed to understand ergonomic standards before making a recommendation. Fair enough.


But the first academic paper it encountered had some questionable statistics. So naturally it decided it needed to install R to verify the regression analysis.


The R installation failed due to missing dependencies.


So it decided to compile R from source.


Which required a working C compiler.


When I finally killed the process, it had burned through $122.47 in OpenAI API calls and was halfway through cloning the GCC source repository so it could build a compiler for Windows. To audit a research paper. To recommend a desk.


I did not get a standing desk recommendation. I got a $122 lesson in why you don’t let agents recurse unsupervised.


### **So imagine my surprise**


Fast-forward to yesterday. Codex CLI is not BabyAGI. It runs off your ChatGPT subscription, so for one thing – no surprise bills.  But it is autonomous within its sandbox. And it’s very patient. And very smart.


I regularly trust it with simple tasks like installing things on the command line, and troubleshooting the inevitable minutia that result. Who needs to remember bash or powershell when you can use english?  My expectations were either success, or some sort of patient declaration of failure.


What I was not expecting was to discover that there **was no Windows version** and it had **ported it itself**.


I posted back in Whatsapp.


![](https://www.danshapiro.com/blog/wp-content/uploads/2025/10/image-1.png)


And that’s how Beads accidentally got Windows support.


[https://github.com/steveyegge/beads/pull/91](https://github.com/steveyegge/beads/pull/91)


It’s pretty fantastic, and it makes Codex even Codexier. [Try it yourself](https://github.com/steveyegge/beads?tab=readme-ov-file#windows-11)!


* The tooling is so much better in Claude Code, but gpt-5-codex on high thinking is just devastatingly effective. It stays on track and gets the job done, while sonnet has the ‘oh squirrel’ tendency to do what it thinks you should want, rather than what you asked (pleaded, begged) for. I still use them both.

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
