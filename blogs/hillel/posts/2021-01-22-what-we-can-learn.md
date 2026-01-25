---
title: "What engineering can teach (and learn from) us"
date: 2021-01-22
url: https://www.hillelwayne.com/post/what-we-can-learn/
slug: what-we-can-learn
word_count: 2603
---

*This is part three of the crossover project. Part one is [here](https://www.hillelwayne.com/post/are-we-really-engineers/) and part two is [here](https://www.hillelwayne.com/post/we-are-not-special/). A conference talk based on this work is now available [here](https://www.hillelwayne.com/talks/crossover-project/).*


I met William at [Deconstruct 2019](https://www.deconstructconf.com/).1 We were walking back from the pre-party—too loud for my comfort level—and I took the chance to interview him.  He knew about my project and wanted to share his memories of mechanical engineering.


“Most of my skills transferred seamlessly. There’s one book, [Sketching User Experiences](https://www.amazon.com/gp/product/B005NZ5K3E),  that’s aimed at software engineers.  But it was really influential on me when I did mechanics. Up until then all the books I read were things like  [The First Snap-Fit Handbook](https://www.amazon.com/First-Snap-Fit-Handbook-Creating-Attachments/dp/1569902798): a lot about the *how* but very little about the *why*. And that’s important! But this book on user experience, though, it helped me a lot.”


“And you think more mechanical engineers should read the book on software engineering, because it would help them too.”


“I agree with that.”


Something struck me.  “That book you mentioned on snap-fits, you said it was also useful. What’s the equivalent software book?”


He thought about that.  “You know,  I can’t think of any.”


---


In the last two essays we discussed the current state of software engineering: whether it “counts” and why that matters. This essay is on the future state: how, by accepting its place in the engineering field, we can aim to improve it. This was always the most interesting part of the project for me. I’m a firm believer in the potential of interdisciplinary research, that we as software engineers can learn valuable lessons from librarians, social workers, and zookeepers. I expected the crossovers would have lots of valuable advice here.


I *wasn’t* expecting it to go the other way, too. Just as I once thought that we weren’t “real” engineers, I thought there wasn’t much we could teach them. This turned out to be false, too, and many of the crossovers had things they wanted backported. In fact it was often the *same* things: there’s a lot we can learn, true, but the things we can teach are a very, *very* big deal.


I’d summarize it like this: trad engineers are better at the overall strategic process of making a product, while software engineers are better at the day-to-day process. But these differences aren’t due to some essential tradeoff, just us having prioritized different techniques. There’s no reason we can’t do both.


I’m not a crossover, I only know software. I’m trying to synthesize ideas the crossovers shared that I have no personal experience in. If the things I share seem shallow, that’s because I did a poor job representing them, not because the engineers had bad ideas.


## What we can learn from them


> Learn to QA! *-Nick (industrial)*


The most common answers I heard fell into two broad categories: 1) we can prepare more, and 2) we can care more.


### More Methodical Processes


> I’d like to see a lot more thought and planning go into stuff. I’m sure the Agile people are gonna freak out and be like, “You’re doing waterfall!”  No, we’re not. We’re just thinking about what we want to build and why. *-Matt (chemical)*


Is it so surprising that trad engineers are much better at requirements gathering and planning than we are?


Of course, there’s technical reasons why we don’t need to plan as much as trad engineers do. In software, we can iterate much faster, meaning we can use completed prototypes to help guide the requirements from client feedback. Everybody, including all of the crossovers, recognize that. The problem is just that we’ve gone too far the other way. When even simple statecharts are decried as Big Design Up Front, are we really where we should be?


And what is “upfront planning”, anyway? Does it mean requirements gathering, analyzing the problem domain, writing a formal specification? People’s answers were scattered, covering everything from design docs to client interviews. The ultimate impression I got was what mattered most was *time*. First and foremost, there was not enough time between project conception and the first lines of implementation. Crossovers wanted more time to *think* about things before they *did* things. Just a couple of days of planning would make a big difference, regardless of how people *used* that time.


> I’m used to engineers thinking about a lot of “Where is this thing gonna fail? What is gonna go wrong?” Because that’s what I was mostly concerned about in engineering. And I find that the typical software engineer does not think about that as much. […] I find sometimes working on projects that if someone had spent two or three more days thinking about the design upfront, we probably would have avoided more pitfalls than we did. *-Mat (civil)*


The usual response to this is that software is inherently unknowable, so we cannot plan like engineers do. As discussed in the previous essay, this underestimates just how uncertain and unpredictable trad engineering is. It’s not like engineers strictly follow their plans. Trad engineers are just as likely to make last-minute changes, hack things together, and run into unforeseen circumstances as we are. The response to plans being imperfect is to make flexible dynamic plans, not to throw away planning entirely. It would be a mistake to plan as thoroughly as traditional engineers. It would be just as much a mistake to not plan at all.


### Professionalism


> You know when we were making these sensors, we held them and handled them every day. And, you know, we got to actually see them installed in places and we would meet with clients and shake their hand and gather requirements. […] And that gave us a lot more discipline about what we were doing. And we thought much more tightly about what we said we could do and what we tried to do. *-Matt*


Everybody who saw issues with our process also saw it as a symptom of a deeper problem, which is our lack of professionalism.


Doesn’t that go against everything I said? Not exactly. Things like licensure or training are part of the *trappings* of the job, while the “lack” is aimed at the *mindset*. Most trad engineering is physical, while most software is intangible. That makes it harder to feel responsible for its impact. Much as they tried, many of the crossovers felt that they “cared less” about the software they produced than about the things they built. It’s easier to wave off a frustrating bug with “oh, that’s just computers being bad” as opposed to “we did something wrong”.


> It’s not like you can walk down the neighborhood and see our project in action, really. I work in a place where mistakes can kill people. I work in healthcare software. *-Matt (electrical)*2


You might notice this is similar to some Agile claims. Indeed, this sense that we need to take more “pride in our work” is pervasive in many modern software movements. Everybody seems to think that we, as a community, haven’t fully professionalized yet. The crossovers aren’t saying anything particularly novel here.


What *does* matter, though, is that it gives the platitude validity. The driving force of this entire project is *skepticism* about common software claims. The people saying we need to be more responsible are the same ones that think we aren’t engineers, or that think we’re too special to be engineers. If they’re wrong about engineering, are they also wrong about responsibility? Turns out, no. Or at least, the crossovers agree with them there. We culturally don’t feel the same degree of responsibility trad engineers do. Of course, just because we can *identify* a problem doesn’t mean we can *fix* it. We can all agree our culture could be better but not know how to get there.


## And What They Can Learn from us


> Learn to write a frickin’ website! *-Nick*


In contrast with the lessons we can import to software, the lessons we can export *from* software are easy. Everybody listed the same two things that software does especially well, often in great detail. These are open communities and version control.


### Openness


> Having a community that you can learn from, … I think it was the reason I got into software engineering, the reason I was able to get into it so quickly and so easily. There’s so many different ways you can learn. *-Kate (chemical)*


I originally planned to present this all at [Rebase 2020](https://rebase-conf.org/2020/). If I were instead a traditional engineer and wrote something like “are software engineers really engineers”, then the research would have died on my hard drive. Not because the trad engineering conferences are close-minded or anything; I’m sure they’d find this just as interesting as I do. There just wouldn’t be any conferences to present it at.


We software engineers take the existence of nonacademic, noncorporate conferences for granted. But we’re unique here. In most fields of engineering, there are only two kinds of conferences: academic conferences and vendor trade shows. There’s nothing like [Deconstruct](https://www.deconstructconf.com/) or [Pycon](https://us.pycon.org/) or [!!con](http://bangbangcon.com/), a practitioner-oriented conference run solely for the joy of the craft.


In addition to helping us improve our skills, software conferences also break down silos in software. [StrangeLoop](https://thestrangeloop.com/) puts [programming language theorists](https://www.youtube.com/watch?v=HnOix9TFy1A), [enterprise engineers](https://www.youtube.com/watch?v=XqKvgzXCoXc), and [origami artists](https://www.youtube.com/watch?v=kOF_fZFXTj0) in the same room. That’s the perfect environment for cross-pollination, which is exactly what happens. By contrast, many of the crossovers I talked to asked me how their trad experiences compared to others. Not other trad engineers in general: other trad engineers *in their field*. Electrical engineers would only know about the experiences of them and their friends. This was even cited as one of the major reasons why people left traditional engineering: the lack of diverse career opportunities.


> With processing and chemical engineering, me and most of the people that I knew were working mostly for big manufacturing companies, pharmaceutical companies, things like that. There’s a lot more opportunity in software. *-Kate*


I owe my own career path to this openness. When I gave up on physics grad school, I was able to teach myself software development through the huge amount of free material software engineers share online. Later, I was able to switch between two very different software fields, web development to formal verification, because of that free information. And when I decided to contribute information back, for free, that wasn’t considered odd or anything. It’s just what enthusiastic software developers do.


I’m not the only person who “fell into” software. In fact, that’s one big reason our discipline places less emphasis on formal education. Most households have computers and most of our tools are open source. People can, and do, download all the tools of the trade and learn how to program on their own. In contrast, you would need to buy a lot of additional equipment if you want to learn electrical engineering. It’s unsurprising that so many more software engineers are self-taught.


Unfortunately, that also hampers how much other fields can open up. Trad engineers could share more material online and run more practitioner conferences, but atomic spectrometers are never going to become commodity products.


But not *too* unfortunately, because there’s another idea out of the software world. And it’s much more important than anything else I covered here.


### Version Control


Almost every single person I talked to brought up version control.


Version control is the single most innovative, most revolutionary, most paradigm-shifting tool that is uniquely ours. Some other fields have proto-VCS, things with a fraction of the power and versatility of git, and the rest are still saving files as `form-draft-3.docx`.


Part of this is our preference for plaintext source code. Our VCS tools aren’t nearly as suited for things like diagrams and spreadsheets, which are more common in trad fields. But that doesn’t preclude version control on other formats: after all, GitHub can [diff CAD files](https://docs.github.com/en/github/managing-files-in-a-repository/3d-file-viewer). And many engineering artifacts are also written in plaintext. A requisition form or an SVG diagram can easily be version controlled in git.


On top of this, our tooling *surrounding* version control is extraordinary. If I’m hosting a project on GitHub, I can make every pull request kick off a test suite for a dozen different OSes, check for merge conflicts, and ping a coworker for review. One chemical engineer talked about how, whenever he needed sign off on a project at his old job, he had to get everybody to physically sign an authorization form. If someone was working remotely that day, the authorization would be delayed by a day. He is very happy to now have pull requests and automated builds.


---


Time for a confession: I screwed this essay up.


When I asked “what we can learn from engineers”, I was looking for specific ideas or concepts worth importing. Things like Snap-Fit Handbooks, or [lockout-tagout](https://en.wikipedia.org/wiki/Lockout%E2%80%93tagout), or numerical datasheets. All things that the crossovers I spoke with brought up on their own volition.


This wasn’t the question I asked, though! I’d asked something slightly different: “are there ways our overall approach to software should be more like the overall approach to engineering?” That’s a question with very different answers. Even in the topic of “what can we do different”, I’ve barely scratched the surface of what’s left to learn.


So even though the Crossover Project is now *done*, it’s not *complete*, and it never can be. There’s so, *so* much more we can learn by talking to crossovers. And I encourage you to do so! I learned more in the first two hours of interviewing than I had than from all the thought leader essays on the subject.


To summarize my ultimate conclusions:


First of all, We software engineers are “really” engineers. All the differences people give between software and “real” engineering don’t accurately reflect what “real” engineering looks like. And the biggest difference, licensure, is a political construct, not a technical one. At the same time, there is a difference between the different ways people make software, and it makes sense to think of software developers and software engineers as distinct concepts. But even then, it’s very easy for a software developer to become a software engineer and vice versa.


Second, we are not special. There are some aspects of software engineering that are unique to software, such as the speed of iteration, loose constraints, and the consistency of our material. But software engineering has far more in common with the other forms of engineering than it has differences. The same ideas that engineers use to advance their craft are equally useful in our own domain.


Finally, there is a lot we can both teach and learn. Engineering processes are more sophisticated than ours in ways that we can extract lessons from. Traditional engineers have a stronger sense of professionalism and responsibility than we tend to. In contrast, our culture is much more open and our communities much stronger than what exists in trad engineering. And our developments in version control have the potential to revolutionize traditional engineering.


I hope this was as interesting to you as it was for me. Thank you for reading.


*If you enjoyed these essays, I have a [weekly newsletter](https://buttondown.email/hillelwayne/) and am on [Twitter](https://twitter.com/hillelogram).*


*Thanks to Glenn Vanderburg, [Chelsea Troy](https://chelseatroy.com/), [Will Craft](https://twitter.com/craftworksxyz), and [Dan Luu](https://www.danluu.com) for feedback, and to all of the engineers whom I interviewed.*


---

1. Unlike the other interviews, this was not recorded.  I’m going off my notes and memory here and these aren’t transcribed quotes.
 [return]
2. Yes, this is a different Matt than the other Matt (and the Mat) I quoted.
 [return]
