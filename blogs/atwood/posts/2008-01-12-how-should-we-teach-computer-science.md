---
title: "How Should We Teach Computer Science?"
date: 2008-01-12
url: https://blog.codinghorror.com/how-should-we-teach-computer-science/
slug: how-should-we-teach-computer-science
word_count: 1070
---

[Greg Wilson](https://web.archive.org/web/20080115085415/http://www.cs.toronto.edu/~gvwilson/) recently emailed me the following question:


> I’m teaching a software engineering class to third-year students at the University of Toronto starting in January, and would like to include at least one hour on deployment – **[deployment] never came up in any of my classes, and it’s glossed over pretty quickly in most software engineering textbooks**, but I have learned the hard way that it’s often as big a challenge as getting the application written in the first place.


Deployment is a huge hurdle. It’s a challenge even for the best software development teams, and it’s incredibly important: if users can’t get past the install step, none of the code you’ve written matters! And yet, as Greg notes, existing software engineering textbooks give this crucial topic only cursory treatment. Along the same lines, a few weeks ago, a younger coworker noted to me in passing that **he never learned anything about source control** in any of his computer science classes. How could that be? Source control is the very [bedrock of software engineering](https://blog.codinghorror.com/what-is-modern-software-development/).


If we aren’t teaching fundamental software engineering skills like deployment and source control in college today, we’re **teaching computer science the wrong way**. What good is learning to write code in the abstract if you can’t work on that code as a team in a controlled environment, and you can’t deploy the resulting software? As so many computer science graduates belatedly figure out after landing their first real programming job, it isn’t any good at all.


Today’s computer science students should **develop software under conditions as close as possible to the real world**, or the best available approximation thereof. Every line of code should be written under source control at all times. This is not negotiable. When it’s time to deploy the code, try deploying to a commercial shared web host, and discovering everything that entails. If it’s an executable, create a standalone installer package that users have to download, install, and then have some mechanism to file bug reports when they inevitably can’t get it to work. Students should personally follow up on each bug filed for the software they’ve written.


Will this be painful? Boy, oh boy, will it ever. It’ll be *excruciating*. Students will hate it. They’ll begin to question why anyone in their right mind would want to write software.


Welcome to the real world.


After I wrote my response to Greg, Joel Spolsky posted an [entry on computer science education](http://www.joelonsoftware.com/items/2008/01/08.html) that, at least to my eye, seemed hauntingly similar to the advice I offered:


> I think the solution would be to create a programming-intensive BFA in Software Development – a Julliard for programmers. Such a program would consist of a practical studio requirement developing significant works of software on teams with very experienced teachers, with a sprinkling of liberal arts classes for balance.
> When I said BFA, Bachelor of Fine Arts, I meant it: software development is an art, and the existing Computer Science education, where you’re expected to learn a few things about NP completeness and Quicksort is singularly inadequate to training students how to develop software.
> Imagine instead an undergraduate curriculum that consists of 1/3 liberal arts, and 2/3 software development work. The teachers are experienced software developers from industry. The studio operates like a software company. You might be able to **major in Game Development and work on a significant game title, for example, and that’s how you spend most of your time, just like a film student spends a lot of time actually making films and the dance students spend most of their time dancing.**


This is not to say that computer science programs should neglect theory. Fundamental concepts such as algorithms and data structures are still important. My algorithms class was my favorite and by *far* the most useful class I ever took for my own computer science degree. But teaching these things at the *expense* of neglecting more prosaic real world software engineering skills – skills that you’ll desperately need as a practicing software developer – is a colossal mistake. It’s what Steve Yegge was alluding to in his [fantastical Wizard School essay](http://steve-yegge.blogspot.com/2006/07/wizard-school.html)... I think.


There is the concern that all those highfalutin’ computer science degrees could degenerate into little more than vocational school programs, something Joel mentioned in his [excellent Yale address](http://www.joelonsoftware.com/items/2007/12/03.html):


> At Ivy League institutions, everything is Unix, functional programming, and theoretical stuff about state machines. As you move down the chain to less and less selective schools Java starts to appear. Move even lower and you literally start to see classes in topics like Microsoft Visual Studio 2005 101, three credits. By the time you get to the 2 year institutions, you see the same kind of SQL-Server-in-21-days “certification” courses you see advertised on the weekends on cable TV. Isn’t it time to start your career in (different voice) Java Enterprise Beans!


You can have it both ways. That’s why I’m so gung-ho for internships. College CS classes tend to be so dry and academic that you *must* spend your summers working in industry, otherwise you won’t have the crucial software engineering skills you’ll need to survive once you graduate. Unimportant little things like, say, source control and deployment and learning to deal with users. I constantly harp on internships whenever I meet college students pursuing a computer science degree. It’s for your own good.


It does strike me as a bit unfair to force students to rely on internships to complete their education in computer science. Or, perhaps, something even worse. “Want to learn computer science? No college necessary! Just download some ISO images and found your own social networking startup!” Unleashing the naked greed of the TechCrunch crowd on tender young programming minds seems downright cruel.


So **how should we teach computer science?** The more cynical among us might say [you can’t](https://blog.codinghorror.com/separating-programming-sheep-from-non-programming-goats/). I think that’s a cop-out. If students want to prepare themselves for a career in software development, they need to shed the theory and spend a significant portion of their time creating software with all the warty, prickly, unglamorous bits included. Half of software engineering is pain mitigation. If you aren’t cursing your web hosting provider every week, fighting with your source control system every day, deciphering angry bug reports from your users every hour – you aren’t being taught computer science.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[teaching methodologies](https://blog.codinghorror.com/tag/teaching-methodologies/)
[deployment](https://blog.codinghorror.com/tag/deployment/)
[computer science education](https://blog.codinghorror.com/tag/computer-science-education/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
