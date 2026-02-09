---
title: "Bugs Faster than the Speed of Thought"
date: 2021-06-30
url: https://blog.mempko.com/bugs-faster-than-the-speed-of-thought/
slug: bugs-faster-than-the-speed-of-thought
word_count: 478
tags: ['#wordpress', '#Import 2024-11-03 23:36']
---



I got access to OpenAI’s GPT-3 last year and one of the first things I did was prompt it with a C++ interface struct and have it write the implementation. I was generally surprised by the results. Some of the completions were even code that was clearly from Github projects with valid Github links. My thought was “Wow, this would be an impressive auto-complete”. Today, Github just released [Copilot](https://copilot.github.com/?ref=blog.mempko.com), which is a GPT-3 powered auto-complete feature. It’s very impressive.


![](https://blog.mempko.com/content/images/wordpress/2021/06/image-2.png?resize=1008%2C840&ssl=1)


Anybody who has created a production AI system will know that only 20% of the work goes into creating the models, the scaffolding around it is the remaining 80%. I’m sure it took a lot of work to go from using the GPT-3 playground to something well integrated into an IDE like Copilot.


Being well integrated is key to the success of Copilot and it’s going to be used by hundreds of thousands if not a million programmers very quickly. Which is precisely what makes it so dangerous.


In [Code Complete](https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670?ref=blog.mempko.com), Steve McConnell wrote extensively on defects in production systems. The industry average defect rate is about 15 – 50 bugs per 1000 lines of code. Some techniques used by NASA can get bug count to almost zero. Open source software likely has MORE bugs per 1000 lines of code because most open source projects have [1 developer and no eyeballs.](https://www.sciencedirect.com/science/article/pii/S0950584921000902?ref=blog.mempko.com)


Copilot isn’t magic and will perform worse than a human coder on average. If it’s trained on the gigantic, 100 million project corpus of Github projects, it will most certainly have more than 50 bugs per 1000 lines of code. This is faster than Copy-Pasting code snippets because Copilot will auto-complete code that will likely compile and require less human correction. All programmers understand why copy-pasting code is bad. It likely introduces bugs. With Copilot, bugs will be transmitted faster than the speed of thought.


What can the consequences of buggy software being written at a breakneck pace be? The fatal Boeing 737 MAX8 crash involving Ethiopian Airlines in 2019 was the result of [AI gone wrong](https://en.wikipedia.org/wiki/Maneuvering_Characteristics_Augmentation_System?ref=blog.mempko.com). They took a safety system that was supposed to only engage in critical situations and expanded it to noncritical situations. Black box systems kill. Imagine this for a second, building AI systems is the future of software. You will no longer write algorithms but the scaffolding of learning systems. Now imagine your scaffolding ***itself*** is written mostly by Copilot. Bugs will propagate in new ways, via systems that build systems.


Building software is building a small world. It’s about meaning, and we ***know*** GPT-3 doesn’t understand meaning. It won’t understand your problem either. When programmers get used to auto-complete code that compiles, how deep will they go into it? Will they review it carefully? Building human-machine interaction is hard and you don’t want humans writing software [asleep at the wheel](https://www.msn.com/en-us/news/other/no-one-was-driving-in-tesla-crash-that-killed-two-men-in-spring-texas-report-says/ar-BB1fMTLS?ref=blog.mempko.com).

