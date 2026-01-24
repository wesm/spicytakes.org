---
title: "Good Programmers Get Off Their Butts"
date: 2004-11-21
url: https://blog.codinghorror.com/good-programmers-get-off-their-butts/
slug: good-programmers-get-off-their-butts
word_count: 654
---

I searched for this citation, and [like Wes](https://web.archive.org/web/20050308004714/http://wesnerm.blogs.com/net_undocumented/2004/01/fire_and_motion.html), I remember reading it, but I can’t remember the exact place I read it:


> *This echoes another comment from a recently read blog article, the author of which I cannot recall. **Good programmers get off their butts. **Typically, programmers won’t write code until they have resolved some design issues, but in the process time can go by with very little advancement in the design. Productive developers will write some code, even if the design is vague, because software development is an iterative process.*


I have lost count of the number of times I’ve set out to design software, then during implementation had to throw out or radically alter my design, because...

- I forgot something really important
- I found another, easier approach
- What I’m doing doesn’t make sense
- I am reinventing the wheel, and should be looking for a download
- Hey, I don’t even need to do this in the first place!


In the real world, there’s a tight feedback loop between the implementation and the design. When you’re using Photoshop as a design tool, all things are possible. Visual Studio, unfortunately, isn’t that forgiving.


I am not proposing a code-like-hell methodology. I am merely observing that, in my experience, **coding without planning is just as futile as coding with too much planning**. Software development is [a wicked problem](https://discourse.codinghorror.com/t/development-is-inherently-wicked/1320); you should never make planning decisions without some kind of code prototype to ensure that you’re making informed decisions. If you plan too far ahead of the code, I *guarantee* you are doing work that will be thrown away or altered until it is unrecognizable.


The most destructive symptom of over-planning is the wrongheaded idea that being a Software Architect™ means drawing a lot of UML diagrams and handing them off to a group of developers in Bangalore. **UML is great if you don’t want to do any work; you just draw pictures of what it would look like if work was actually done.** This is not only borderline laziness, it’s also a recipe for disaster. You can’t architect a real world application on a whiteboard. You must prototype it in code to gather data on the performance and design implications of the choices you are making. Otherwise you really have no idea if you’re creating something that makes sense – or if it’s even possible! As noted in Robert Glass’, [Facts and Fallacies of Software Engineering](http://www.amazon.com/exec/obidos/ASIN/0321117425/), in software design, being hands on is mandatory:


> *Far from being a predictable, structurable, routinizable process, design – according to the findings of Curtis and Soloway (1987) – is a messy, trial-and-error thing. And remember, these findings are the result of studying top designers at work. One can imagine less than top designers using an even messier process. Probably the worst possible design approach, and yet one that is tempting to most design novices, is “easy-part-first.” Although it is easy to get the design process started with this approach, it all too often leads to solutions-in-the-small that won’t integrate into an overall solution-in-the-large. As a result, those solutions-in-the-small must often be discarded.
> It is easy to see from all of this that design is complex and iterative. (This thought is explicit in Wiegers [1996].) In fact, it is probably the most deeply intellectual activity of the software development process. It is also easy to see that the initial design solution is quite likely to be wrong. And what about optimal? Well, certainly initial design solutions will rarely be optimal. But that word raises another interesting question – is there such a thing as an optimal design solution?*


As software developers – and *especially* if we have pretensions of [being so-called “architects”](https://blog.codinghorror.com/it-came-from-planet-architecture/) – we should always make decisions based on experience and data. And like it or not, that means **getting off our butts and writing code**.

[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[iterative development](https://blog.codinghorror.com/tag/iterative-development/)
