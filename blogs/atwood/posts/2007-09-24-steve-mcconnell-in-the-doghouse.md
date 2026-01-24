---
title: "Steve McConnell in the Doghouse"
date: 2007-09-24
url: https://blog.codinghorror.com/steve-mcconnell-in-the-doghouse/
slug: steve-mcconnell-in-the-doghouse
word_count: 919
---

I often trot out [Steve McConnell’s doghouse analogy](https://web.archive.org/web/20071011074129/http://stevemcconnell.com/articles/art03.htm) to illustrate how small projects aren’t necessarily representative of [the problems](https://blog.codinghorror.com/the-long-dismal-history-of-software-project-failure/) you’ll encounter on larger projects.


> People who have written a few small programs in college sometimes think that writing large, professional programs is the same kind of work – only on a larger scale. It is not the same kind of work. **I can build a beautiful doghouse in my backyard in a few hours.** It might even take first prize at the county fair’s doghouse competition. But that does not imply that I have the expertise to build a skyscraper. The skyscraper project requires an entirely more sophisticated kind of expertise.


There’s a similar passage in [Rapid Development](http://www.amazon.com/exec/obidos/ASIN/1556159005), which I cited in [Following the Instructions on the Paint Can](https://blog.codinghorror.com/following-the-instructions-on-the-paint-can/).


![an old doghouse](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfA-e8_ShMOaq_PtLyAxDSb7psfLA7UITGjeTBi5EsFRl7MyL2DkiyFsSVWb4wWaCMx__f4sZkXEad-VfHXkmehNBTZGrJ9RGjxP64czlRciKm2DGkOY6SATlix43sWOoC50O9A?key=EFBg8Ij0aJ1EmCyuDte1jBlv)


> What happens if you don’t follow the instructions? If you’re painting a doghouse on a hot Tuesday night after work, you might only have 2 hours to do the job, and Fido needs a place to sleep that night. You don’t have time to follow the instructions. You might decide that you can skip steps 1 through 3 and apply a thick coat rather than a thin one in step 4. If the weather’s right and Fido’s house is made of wood and isn’t too dirty, your approach will probably work fine.
> Over the next few months the paint might crack from being too thick or it might flake off from the metal surfaces of the nails where you didn’t prime them, and you might have to repaint it again next year, but it really doesn’t matter.
> What if, instead of a doghouse, you’re painting a Boeing 747? In that case, you had better follow the instructions to the letter. If you don’t strip off the previous coat, you’ll incur significant fuel efficiency and safety penalties: a coat of paint on a 747 weighs 400 to 800 pounds. If you don’t prepare the surface adequately, wind and rain attacking the paint at 600 miles per hour will take their toll much quicker than a gentle wind and rain will on Fido’s doghouse.


The underlying lesson is the same: what works for small projects may be a total disaster on a larger scale. **Being a competent software engineer means choosing appropriate strategies for the size of the project you’re working on**. Are you working on a doghouse, a skyscraper, a jet airliner, or [the space shuttle](https://blog.codinghorror.com/were-building-the-space-shuttle/)?


Perhaps that’s why I was so entertained by [Steve’s most recent blog post](http://web.archive.org/web/20070623170339/http://blogs.construx.com/blogs/stevemcc/archive/2007/09/23/building-a-fort-lessons-in-software-estimation.aspx). He documents building a fort for his kids. It’s not *exactly* a doghouse, but it’s close. Along the way, Steve applies his considerable software estimation and project planning skills to the project. (Remember, this is the guy who [quite literally wrote the books](https://blog.codinghorror.com/recommended-reading-for-developers/) on these subjects.) It’s a small project, too, so our odds of success are about as [good as they’re going to get](https://blog.codinghorror.com/diseconomies-of-scale-and-lines-of-code/).


> Whenever I do a physical construction project like this I try to pay attention to which attributes of the project are similar to software projects and which are different. The comparisons are made more challenging by the fact that my construction projects are recreational, whereas I’m trying to draw comparisons to commercial software projects. For the first half of the project, no good similarities jumped at out me. But as the project started to take much longer than I expected, **I began to see more and more similarities between my estimates on the fort and problems people run into with software estimates.**


How did it go?


> Days 3-6 went about like Days 1 & 2 had gone, which is to say there were lots of little tasks that turned out to be medium-sized tasks, there were little tasks that I just hadn’t anticipated, and most things took longer than I had planned. By the end of Day 7 (my buffer day), I was done with the tasks I had planned for Day 3 and had a tiny start on Day 4, which is to say that I’d completed the decking, hadn’t started on the railings or framing, and had one wall of the fort framed, but that was all.
> My original plan had called for about a week full time and then another couple of weeks of finishing up loose ends like painting, installing trim, and so on. I finished the fort about 6 weeks after I started it, so I was about 100% over my planned schedule, and I ended up at 2-3x my originally planned effort.


Steve got subsumed in the unpredictable details. This completely mirrors my software project experience. **Often, you can’t even begin to accurately estimate how long something will take until you start doing it.** At least some of it. That’s why so many teams turn to [agile, iterative development techniques](https://blog.codinghorror.com/anything-but-waterfall/); part of each iteration involves exploring all those unknowns and turning them into slightly-less-unknowns for the next iteration. [The faster we iterate](https://blog.codinghorror.com/boyds-law-of-iteration/), the closer we get to an accurate estimate, and the more work we get done along the way. We plan by doing.


This is easily my favorite post in [Steve’s blog](http://web.archive.org/web/20070623170339/http://blogs.construx.com/blogs/stevemcc/default.aspx) to date. Do read the entire post for all the gory details of how things went awry. It’s a storybook example of how an [avalanche of little problems](https://blog.codinghorror.com/escaping-from-gilligans-island/) can snowball into one huge project delay – even if you’re Steve McConnell. And even if you’re only building a doghouse fort.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[project management](https://blog.codinghorror.com/tag/project-management/)
[scalability](https://blog.codinghorror.com/tag/scalability/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
