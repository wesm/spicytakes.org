---
title: "Capstone projects and time management"
date: 2009-10-26
url: https://www.joelonsoftware.com/2009/10/26/capstone-projects-and-time-management/
word_count: 1012
---


It is amazing how easy it is to sail through a Computer Science degree from a top university without ever learning the basic tools of software developers, without ever working on a team, and without ever taking a course for which you *don’t *get an automatic F for collaborating. Many CS departments are trapped in the 1980s, teaching the same old curriculum that has by now become completely divorced from the reality of modern software development.


Where are students supposed to learn about version control, bug tracking, working on teams, scheduling, estimating, debugging, usability testing, and documentation? Where do they learn to write a program longer than 20 lines?


Many universities have managed to convince themselves that the more irrelevant the curriculum is to the real world, the more elite they are. It’s the liberal arts way. Leave it to the technical vocational institutes, the red-brick universities, and the lesser schools endowed with many compass points (“University of Northern Southwest Florida”) to actually produce programmers. The Ivy Leagues of the world want to teach linear algebra and theories of computation and Haskell programming, and all the striver CS departments trying to raise their standards are doing so by eliminating anything practical from the curriculum in favor of more theory.


Now, don’t get me wrong, [this isn’t necessarily a bad thing](https://www.joelonsoftware.com/articles/ThePerilsofJavaSchools.html). At least they’re replacing Java with Scheme, if only because “that’s what MIT does.” ([Too late!](http://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python)) And they are teaching students to think a certain way. And given how much the average CS professor knows about real-world software engineering, I think I’d rather have kids learn that stuff at an [internship at Fog Creek](http://fogcreek.com/Jobs/SummerIntern.html).


Greg Wilson, an assistant professor at the University of Toronto, [gave a talk at the StackOverflow DevDay conference in Toronto](http://www.slideshare.net/gvwilson/bits-of-evidence-2338367), which was entertaining, informative, and generally just a huge hit. We got to talking, and he told me about his latest brainchild, [UCOSP](http://ucosp.wordpress.com/), which stands for “All The Good Names Are Taken.”


It’s a consortium of 15 universities, mostly in Canada, which are organizing joint senior-year capstone projects. They’re setting up teams of a half-dozen undergraduates from assorted universities to collaborate on contributing to an open source project, for credit and for a grade. As soon as I heard about the program I volunteered to sponsor a team to make a contribution to Mercurial. Sponsoring a team consists of offering to pay for a trip to Toronto for all the undergrads to get organized, and providing a programmer to mentor the team.


Browsing around the [UCOSP blog](http://ucosp.wordpress.com/), I was reminded of [why student projects, while laudatory, frequently fail to deliver anything useful](http://ucosp.wordpress.com/2009/10/21/a-rational-response-to-an-irrational-environment/). “One of the points of this course is to give you a chance to find out what it’s like to set and then meet your own goals,” Greg wrote. “The net result is pretty clear at this point: in many cases, students are doing less per week on this course than they would on a more structured course that had exactly the same content.”


College students in their final year have about 16 years of experience doing short projects and leaving everything until the last minute. Until you’re a senior in college, you’re very unlikely to have *ever* encountered an assignment that can’t be done by staying up all night.


The typical CS assignment expects students to write the “interesting” part of the code (in the academic sense of the word). The other 90% of the work that it takes to bring code up to the level of “useful, real-world code” is never expected from undergrads, because it’s not “interesting” to fix bugs and deal with real-world conditions, and because most CS faculty have never worked in the real world and have almost no idea what it takes to create software that can survive an encounter with users.


Time management is usually to blame. In a group of four students, even if one or two of the students are enterprising enough to try to start early in the term, the other students are likely to drag their heels, because they have more urgent projects from other classes that are due *tomorrow*. The enterprising student(s) will then have to choose between starting first and doing more than their fair share of the work, or waiting with everyone else until the night before, and guess which wins.


Students have exactly zero experience with long term, team-based schedules. Therefore, they almost always do crappy work when given a term-length project and told to manage their time themselves.


If anything productive is to come out of these kinds of projects, you have to have weekly deadlines, and you have to recognize that ALL the work for the project will be done the night before the weekly deadline. It appears to be a permanent part of the human condition that long term deadlines without short term milestones are rarely met.


This might be a neat opportunity to use Scrum. Once a week, the team gets together, in person or virtually, and reviews the previous week’s work. Then they decide which features and tasks to do over the next week. FogBugz would work great for tracking this: if you’re doing a capstone project and need access to FogBugz, please let us know and we’ll be happy to set you up for free. We can also set you up with beta access to kiln, our hosted version of Mercurial, which includes a code review feature.


I’ve been blaming students, here, for lacking the discipline to do term-length projects throughout the term, instead of procrastinating, but of course, the problem is endemic among non-students as well. It’s taken me a while, but I finally learned that long-term deadlines (or no deadlines at all) just don’t work with professional programmers, either: you need a schedule of regular, frequent deliverables to be productive over the long term. The only reason the real world gets this right where all-student college teams fail is because in the real world there are managers, who can set deadlines, which a team of students who are all peers can’t pull off.
