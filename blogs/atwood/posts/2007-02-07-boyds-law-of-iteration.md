---
title: "Boyd’s Law of Iteration"
date: 2007-02-07
url: https://blog.codinghorror.com/boyds-law-of-iteration/
slug: boyds-law-of-iteration
word_count: 601
---

Scott Stanfield forwarded me a link to Roger Sessions’ [A Better Path to Enterprise Architecture](https://web.archive.org/web/20070211180233/http://msdn2.microsoft.com/en-us/library/aa479371.aspx) yesterday. Even though it’s got [the snake-oil word “Enterprise”](https://blog.codinghorror.com/the-great-enterprise-software-swindle/) in the title, the article is surprisingly good.


I particularly liked the unusual analogy Roger chose to illustrate the difference between iterative and recursive approaches to software development. It starts with Air Force [Colonel John Boyd](http://en.wikipedia.org/wiki/John_Boyd_(military_strategist)) researching a peculiar anomaly in the performance of 1950’s era jet fighters:


> Colonel John Boyd was interested not just in any dogfights, but specifically in dogfights between [MiG-15s](http://en.wikipedia.org/wiki/Mikoyan-Gurevich_MiG-15) and [F-86s](http://en.wikipedia.org/wiki/F-86_Sabre). As an ex-pilot and accomplished aircraft designer, Boyd knew both planes very well. He knew the MiG-15 was a better aircraft than the F-86. The MiG-15 could climb faster than the F-86. The MiG-15 could turn faster than the F-86. The MiG-15 had better distance visibility.
> The F-86 had two points in its favor. First, it had better side visibility. While the MiG-15 pilot could see further in front, the F-86 pilot could see slightly more on the sides. Second, the F-86 had a hydraulic flight control. The MiG-15 had a manual flight control.
> The standing assumption on the part of airline designers was that maneuverability was the key component of winning dogfights. Clearly, the MiG-15, with its faster turning and climbing ability, could outmaneuver the F-86.
> There was just one problem with all this. Even though the MiG-15 was considered a superior aircraft by aircraft designers, the F-86 was favored by pilots. The reason it was favored was simple: in one-on-one dogfights with MiG-15s, the F-86 won nine times out of ten.


How can an inferior aircraft consistently win over a superior aircraft? Boyd, who was himself one of the best dogfighters in history, had a theory:

kg-card-begin: html

> Boyd decided that the primary determinant to winning dogfights was not observing, orienting, planning, or acting better. The primary determinant to winning dogfights was observing, orienting, planning, and acting faster. In other words, how quickly one could iterate. Speed of iteration, Boyd suggested, beats quality of iteration.
> The next question Boyd asked is this: why would the F-86 iterate faster? The reason, he concluded, was something that nobody had thought was particularly important. It was the fact that the F-86 had a hydraulic flight stick whereas the MiG-15 had a manual flight stick.
> Without hydraulics, it took slightly more physical energy to move the MiG-15 flight stick than it did the F-85 flight stick. Even though the MiG-15 would turn faster (or climb higher) once the stick was moved, the amount of energy it took to move the stick was greater for the MiG-15 pilot.
> With each iteration, the MiG-15 pilot grew a little more fatigued than the F-86 pilot. And as he gets more fatigued, it took just a little bit longer to complete his OOPA loop. The MiG-15 pilot didn’t lose because he got outfought. He lost because he got out-OOPAed.

kg-card-end: html

This leads to **Boyd’s Law of Iteration – *speed* of iteration beats *quality* of iteration.**


You’ll find this same theme echoed throughout every discipline of modern software engineering:

- Unit tests should be small and fast, so you can run them with every build.
- Usability tests work best if you make small changes every two weeks and [quickly discard what isn’t working](https://web.archive.org/web/20070217102609/http://www.uie.com/articles/fast_iterations/).
- Most agile approaches recommend iterations [no longer than 4 weeks](http://www.mountaingoatsoftware.com/article/view/30).
- Software testing is about [failing early and often](https://web.archive.org/web/20070212034622/http://blogs.msdn.com/micahel/archive/2005/08/17/FailFast.aspx).
- Functional specifications are best when they’re [concise and evolving](https://blog.codinghorror.com/dysfunctional-specifications/).


When in doubt, *iterate faster*.

[software development](https://blog.codinghorror.com/tag/software-development/)
[iterative approach](https://blog.codinghorror.com/tag/iterative-approach/)
[recursive approach](https://blog.codinghorror.com/tag/recursive-approach/)
[enterprise architecture](https://blog.codinghorror.com/tag/enterprise-architecture/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
