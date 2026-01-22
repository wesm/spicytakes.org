---
title: "Thoughts on the future of math education"
date: 2016-06-15
url: https://mathbabe.org/2016/06/15/thoughts-on-the-future-of-math-education/
word_count: 5102
---


*This is a guest post by Kevin H. Wilson, a data scientist who usually resides in Brooklyn, but is currently in Chicago as a Mentor at the Data Science for Social Good Fellowship. In past lives he’s gotten a Ph.D. in math, worked as a data scientist at Knewton for several years, and continues to oversee programming classes in rural schools for Microsoft’s TEALS program. This note comes from that latter work and associated policy work.*


**Programming is a Tool and Should be Taught as Such**


A very popular trend nowadays is to demand that computer science be taught in schools. Indeed, [President Obama has started an initiative](https://www.whitehouse.gov/blog/2016/01/30/computer-science-all) to bring computer science to all schools in America. Before that, [Mayor DeBlasio of New York](http://www.nytimes.com/2015/09/16/nyregion/de-blasio-to-announce-10-year-deadline-to-offer-computer-science-to-all-students.html) demanded computer science in all schools in the City by 2025. The [Hour of Code](https://hourofcode.com/us) is basically a mandatory volunteer activity in many tech firms. And a search for high school hackathons or Capture the Flag on Google reveals huge interest in this topic.


These initiatives seem to miss the broader point about computers: they have fundamentally transformed the way that we interact with the world and school should reflect that. As structured now, high school computer science initiatives tend to build programming courses. These courses tend to focus either on the “cool” things you can do with coding, like building games, or the rigorous implementation details of complicated languages, as in AP Computer Science A. Even the better courses, such as AP Computer Science Principles, often constrain the skills learned to a single classroom.


Programming, however, is simply a tool which solves other problems. Specifically, programming is a tool that allows data to be manipulated. Some of that data is static data, like a business’s annual accounts payable and receivable; and some of that data is dynamic streams, like a user’s interaction with a game she’s playing on the computer. Programming’s genius is to abstract these to the same basic paradigm, a paradigm that has made it possible for Google and Facebook and Uber and Blizzard and countless other companies to improve[1] our lives using what, by historical standards, are extremely cheap and accessible devices.


Tools, however, should be taught like tools. To properly teach a tool, it must be used in context and reinforced horizontally (across the school day in multiple subjects) and vertically (across the years as students become more comfortable with more complicated tools). These imperatives have found purchase before, often in the form of encouraging medium- or long-form writing in all subjects,[2] or in the use of (some) math in all science-based courses.[3]  But our generally balkanized curricula often lead to a general perception among students (and, as students become adults, among the general populace) that knowledge is a bunch of tiny islands whose inhabitants are called the “Good at Math” or the “Good at English.”


I believe that computers and their ability to easily manipulate data offers a chance to truly redefine the mathematics curriculum, to make it more horizontal, and to refocus the tools we teach on what is actually useful and stimulating. Statistics, not calculus, should be the pinnacle achievement of high school, not relegated to box-and-whisker plots and an AP course which is accepted by relatively few universities. Algebra, the math of manipulating symbols, should be taught alongside programming. Calculus, a course which I have heard multiple people describe as “easy but for the Algebra,” should be relegated to a unit in Statistics. Trigonometric identities and conics should go away. And earlier math should focus on how and why a student arrives at an answer, and why her procedure always works, not just the answer itself.


**The First Bias: Historically Computation was Hard**


Why then, if this is such a good idea, hasn’t it happened already? Well, in some limited cases, it has. The Common Core math curriculum has brought statistical modeling to the forefront and clarified the balance between learning facts by rote and understanding why procedures always work. There are beautiful curricula like [Bootstrap](http://www.bootstrapworld.org/) which place Algebra and Computer Science side-by-side. AP History courses have made understanding primary sources and data important to getting an A, and some teachers have gone so far as to incorporate Excel usage into their classrooms.


But there are extremely long-lived biases preventing more radical transformation. Most interesting to me is that historically statistical analysis was hard. Brahe spent an entire lifetime collecting measurements of the solar system, and Kepler spent another lifetime turning those into general rules.[4]  And the annals of science is littered with famous insights made possible by introducing nicer notation. For instance, Mendeleev, inventor of the Periodic Table, is considered one of the greatest scientists in history simply because he realized that data on atoms was periodic and there was a compact and insightful way to lay out a bunch of numbers that people already had access to!


Programming allows its user to take means or do t-tests or bootstrap or graph or integrate numerically in an instant. These bread and butter techniques, as central to statistics as long division is to arithmetic, involved days and days of human computation when the curriculum was last revised. Imagine the process in the 1930s for even finding the median of 500 numbers, a task whose first step is to meticulously sort those 500 numbers. Imagine sorting 10 decks of cards into one big deck of cards. And imagine that as a necessary step to understanding. Such a requirement is a fantastic way to miss the point the first few times, and, since sorting 500 numbers doesn’t get any faster the 20th time you’ve done it, it is a severe impediment for providing reinforcement opportunities.


**The Second Bias: Measuring Computational Ability is Easy**


This leads to a second bias, which is toward the easily measurable. Statistics, like programming, is really a tool that allows its user to answer questions about the world around them. But the world is complex, and there shall never be a procedure as ordered as those in the traditional high school mathematics curriculum[5] which allows the user to easily capture “the truth.” If there were, then we people called “Data Scientists” would be out of a job!


This bias toward the easily measurable doesn’t just exist in schools. For instance, Kaggle is a platform for “data science contests.” Basically, teams compete to “best model” some phenomenon present in real data sets using whatever statistical techniques their hearts desire. Typically, in the end, teams submit some code, and Kaggle runs the code on some data the submitter couldn’t see ahead of time and computes a score. The highest score wins.


Any professional data scientist or statistician will tell you this is the easy part. Once you’ve got a nice CSV filled with data, it’s usually pretty clear what the battery of models are that you would probably run on that data. Indeed, there’s now a sort of “[meta-Kaggle](https://groups.csail.mit.edu/EVO-DesignOpt/groupWebSite/uploads/Site/DSAA_DSM_2015.pdf)” competition where academics build algorithms that automatically write solutions to Kaggle problems! These typically do pretty well.


The hard parts about statistics and data science is what comes before you even start to model the data. How was it generated? What assumptions does that imply about your data? What does it look like? Does the data look like it reflects those assumptions?[6] And so forth.


And what do you want to do with this data and what does this imply about what metric of success you should impose? If you’re Google or Facebook, you want to sell more ads, so likely you want more profit as your ultimate metric. If you’re the Chicago Department of Public Health and you’re trying to stop children from contracting lead poisoning, then likely your ultimate metric of success is [fewer children with lead poisoning](http://dssg.uchicago.edu/project/predictive-analytics-to-prevent-lead-poisoning-in-children/). But these are long term metrics, and so how do you translate them into objectives that you can actually train against?


These questions are the hard ones, and proficiency in answering them is much harder to measure than filling in a few bubbles on a standardized test. They must include writing, long form, explaining choices made and why those choices led where they did.[7] Of course, this sort of mathematical and statistical long form writing isn’t what we typically think of as writing in schools. Instead we imagine portfolios of fictional stories or persuasive essays. This writing would be filled with tables and math and charts and executive summaries, but its ultimate goal, persuading the reader to accept its conclusions, is a completely familiar one.


To assess these skills, we must teach teachers how to teach a new form of writing, and we must grade it. Of course, long form writing takes much more time to grade than multiple choice answers, and so we must find new ways to grade this writing.


**The Third Bias: Learning Happens only in the Classroom**


This brings us to a third bias which prevents the curriculum from changing: the troubling view that the classroom is the sole responsibility of the teacher. This view leads to many bad behaviors, I think, but most relevant here is simply the fact that teachers and teachers alone must grade literally everything that students produce in the class. But what if some of the grading could be outsourced, or perhaps “insourced”? What if students could grade each other’s work?[8] What if teachers from other schools could grade students’ work? What if parents could grade students’ work? What if parents could grade students who aren’t their children’s work? What if members of the community at large could grade students’ work? What if somebody from the next state over or the next country over could grade students’ work?


This idea is not new. Science fairs are often graded by a “distinguished panel of (non-)experts” and AP tests which involve essays are graded in big hotel ballrooms [by college faculty and high school teachers](https://www.ets.org/scoring_opportunities/onsite). Students critiquing each other’s work is often an integral part of creative writing classes, if not English classes in middle and high schools. In some places, they’re even [letting community members](http://www.npr.org/sections/ed/2014/06/01/317433695/in-kentucky-students-succeed-without-tests) grade some projects and classes.


Moreover, computers, in their capacity to move data around at will, can facilitate this process greatly. Among other things, I work with [TEALS](http://www.tealsk12.org), a program out of Microsoft which helps start programming classes in schools. In particular, I help coordinate and train volunteers who live in big cities to teach programming classes for students in far flung areas of the countries. They rely on systems such as [Canvas](http://canvas.instructure.com), [Edmodo](https://www.edmodo.com/), and [Google Classroom](https://classroom.google.com/) to interact with students on a daily basis and to collect and assess homework and plan classes with teachers.


**The Fourth Bias: Teachers Must be Trained**


TEALS was built, indeed, to overcome the final bias I’ll mention preventing change: teachers know how to teach the current curriculum and teacher training programs are geared toward preparing teachers to teach this curriculum. There are extremely few opportunities for teachers to learn to teach new classes or even for teachers to learn new techniques! Teachers rarely observe, much less critique, other teachers, and the current teacher promotion system typically involves jumping to administration.


This is ludicrous. Every single classroom is a hotbed of experimentation. Each child is slightly different and every area of the United States is inculcated in different norms that affect the way students learn and cooperate. Yet teachers are given very little time to reflect on their teaching, to observe each other, or to, heaven forbid, write about their work in local, regional, or national journals and conferences. It is not at all implausible to imagine a teacher promotion system which includes an academic (as in “the academy”) component.


But all this is to say that teachers, for all their professionalism and hard work, are given very few opportunities to learn and teach new subjects. And education schools, bound to churn out teachers who can tick off various certification requirements and pass particular exams, find it hard to train teachers in rarely-taught subjects. And if a teacher coming to teach a single new and interesting course is so hard, imagine how hard it would be for them to learn an entirely new curriculum or for an education school to begin to support it!


This is certainly not a theoretical concern. Common Core has gotten so much negative press in part because of an extremely botched rollout plan.[9] Teachers were not trained in it, new textbooks and other materials to support it were not ready, and the tests meant to evaluate progress in the standards were, like all new measurement devices, faulty. And this for a set of standards that, while radical in many respects, still had the same shape as what we have been teaching for a century.


**On the Other Side of the Fence: Community-Based Projects**


What then would lie on the other side of change if roadblocks like these could be removed? Let’s start at what I think would be the best possible end goal: a project that high school seniors would complete before graduation that would serve as the culmination of their years of study. From there we can work backwards.


What I imagine is a project which explicitly uses all the tools students have learned over their years of high school to advocate for change in their communities. This could take many forms depending on the focus the student wants to take. For instance, students focused on writing could write op-eds detailing the history of something that troubles their community and advocating for realistic change. Or perhaps, if journalism is not their cup of tea, they could write a piece of fiction which has at its heart some spiritual conflict recognizable to those in their community.


What most interests me, though, is the sort of work that computers and statistics could open up. Imagine a project in which students identified a potential problem in their community, collected and analyzed data about that problem, and then presented that report to someone who could potentially make changes to the community. Perhaps their data could come from public records, or perhaps their data could come from interviews with community members, or from some other physical collection mechanism they devise.


Imagine a world where students build hardware and place it around their community to measure the effects of pollutants or the weather or traffic. Imagine students analyzing which intersections in their town see the most deaths. Imagine students looking at their community’s finances and finding corruption with tools like [Benford’s law](https://en.wikipedia.org/wiki/Benford%2527s_law).


Or for those who do not come up with an original idea, imagine continuing a long running project, like the school newspaper, but instead the school’s annual weather report, analyzing how the data has changed over time.


All of these projects require a broad range of skills which high schoolers should be proficient in. They require long to medium term planning, they require a reasonable amount of statistical knowledge, they require the ability to manipulate data, they require an understanding of historical trends, and they require the ability to write a piece of persuasive writing that distills and interprets large numbers of facts.


Moreover, such projects have the potential to impact their communities in profound ways. Places like the coal towns of Appalachia are desperately attempting to make their towns more amenable to investment, both in terms of dollars from outside capitalists and in terms of years of life from their progeny. From time to time I have the opportunity to ask kids in Eastern Kentucky whether they planned to stay in their hometowns after their high school graduation, and I have yet to receive a single “yes.”[10] Towns who rally around training their students to change their own thinking, I believe, will receive huge dividends.


Of course, we can daydream about these projects’ effects, but what sorts of curriculum would actually support them? I won’t pretend to remake the entire K-12 curriculum here, and so let’s focus instead on the mathematics curriculum. Further, I don’t have the space or time right now to completely reimagine the the whole of K-12, nor do I think such a reimagining at all practical, so let’s focus on high school subjects.


**What Curriculum is Necessary to Support these Projects?**


**1. Programming and Algebra merge**


First, we must teach programming. There is no hope for doing data manipulation if you don’t understand programming to some extent. The question is when and how. I believe that algebra and introductory programming are extremely synergistic subjects. I would not go so far as to say they are interchangeable, but they are both essentially arithmetic abstracted. Algebra focuses a bit more on the individual puzzle, and programming focuses a bit more on realizing the general answer, but beyond this, they fundamentally amount to the realization that when symbols stand in for data, we may begin to see the forest and not the trees.


And just how might these two things be interwoven? Well, we have some examples of what might work. The Common Core, for example, emphasizes “computational thinking” in its mathematics curricula for all grade levels, which essentially means encouraging students to learn how to turn their solutions to specific problems into solutions for more general problems.[11] As such we’re seeing a large number of new teaching materials reflect this mandate. Perhaps my favorite of these is [Bootstrap](http://www.bootstrapworld.org/), which I would highly recommend checking out.[12]


**2. Geometry is replaced by Discrete Math and Data Structures**


Programming, though, is only a means and not an end, so how will we employ it? Next in the traditional curriculum we find geometry. Geometry is officially the study of space and shapes, but traditionally in America it is the place where we teach students formal logic. We drill them on the equivalence of a statement and its contrapositive, we practice the masochistic yoga of two-column proofs, and we tease them with questions such as “is a quadrilateral whose opposite sides are congruent a parallelogram?”


But there isn’t anything particularly special about the SSS and AA rules when it comes to constructing logical puzzles. These sorts of puzzles are simply meant to teach their players how to produce strings of implications from collections of facts. For instance, Lewis Carroll famously constructed [nonsensical logic puzzles](http://www.math.hawaii.edu/~hile/math100/logice.htm) for his tutees which entertained while abstracting the actual logical process from the distracting influences of reality.


While I find these sorts of logical puzzles entertaining, I don’t think they’re nearly as useful to students as deriving the facts they will prove themselves. Imagine instead a course in discrete math and data structures. In this course, students would still be asked to construct proofs, but the investigation of the facts would involve programming numerous examples and extrapolating the most likely answer from those examples.


Students would come much more prepared to answer questions in discrete math having essentially become familiar with induction and recursion in their programming classes. Students could also empirically discover that sorting a random list with merge sort takes quasilinear time, and then they could go forth and prove it!


Many of these types of empirical studies would also be the beginning of a statistical education. Plotting times for sorting lists of the same size would introduce the concepts of “typical” and “worst” cases, as well as the idea of “deviance”, which are at the very center of statistical conundra.


**3. Algebra II begone! Enter Statistics based on Open Data Sets**


This then would lead to the next course, a replacement for the traditional and terrible Algebra II. This course, which includes some subset of solutions to systems of (in)equalities, conic sections, trigonometry, and whatever else the state decided to cram in,[13] is generally a useless exercise, where there really is no good answer to the ever-present question of, “Why do we need to know this?”


Thus, I would propose to replace this course wholesale with a course on statistics, expanding on the statistical knowledge that our data structures course laid the foundation for. However, since students have experience in programming and data structures, we can go much, much further than what we traditionally expect from a traditional statistics course. We would still teach about means and medians and z-tests and t-tests, but we can also teach about the extraordinarily powerful permutation test. Here students can really come to understand the hard lessons about what exactly is randomness and what is noise and why these tests are necessary.


Moreover, in traditional statistics courses like AP Statistics, students are usually taught various rules of thumb about sample sizes being sufficiently large and are asked to apply these rules to various fictional situations. But there are a huge number of massive data sets available nowadays, which they could not manipulate without their programming experience. The focus should move away from memorized rules of thumb for small samples to the actual analysis portion and the implications of their explorations for society.[14]


Projects in this course would be multipage reports about exploring their data sets. They would include executive summaries, charts, historical analysis, and policy recommendations. This is a hugely important form of writing which is often not a part of the high school curriculum at all.


**4. Machine Learning subsumes Calculus; Calculus becomes a one-month unit**


Finally, the capstone class, for the most advanced students, would move away from Calculus and instead into Machine Learning. The typical way this course is taught in colleges nowadays is as an overview of various mathematical and statistical techniques from across the subject, though perhaps the two major themes are linear algebra, especially eigenvectors, and Bayesian statistics, especially the idea of priors, likelihoods, and posteriors. Along the way students would pick up all the Calculus they’ll likely need as they learn about optimizing functions.


Indeed, such a course is already being taught at some of the more elite schools in the country, and I have no doubt that anybody who could climb their way to an AP Calculus course, if taught a curriculum like the one outlined above, would be able to approach a machine learning course.


Of course, as mentioned above, the real capstone of this course of study would be the capstone project. The three previous classes contain all that is necessary to be able to approach such a project, though many other classes that students might take could be brought to bear in spectacular ways. History courses could help students put what they learn into the context of the past; biology courses might yield fruitful areas of study, e.g., around pollution; journalism courses might lead to an interest in public records.


And all throughout, the community would be involved. Perhaps they would serve as mentors for these capstone projects, or perhaps they would help grade some of the more specialized projects during the junior year. Or even better, maybe the final exam for the introductory programming course would involve teaching an Hour of Code to community volunteers. And of course the capstone project would focus around the community itself.


**Why would this be better? Lessening the linearity of mathematics**


One immediate pushback I’ve gotten when I tell people this story is to ask why I think kids will perform better at this curriculum than the one that we have now. Isn’t this one even harder? To which my answer is, yes, but is is both more interesting to students and their communities and begins to help solve the problem of mathematics notoriously linear structure. To understand tenth grade math requires understanding ninth grade math requires understanding eighth grade math and so forth. Moreover, there are very few places where students who somehow fell behind have a place to catch up. This wall persists even into adulthood, with many parents dreading they day they have to tell their kids, “Oh, honey, I never understood that stuff.”


This mathematical linearity is quite different from traditional humanities curricula. In these curricula, the true emphasis is on practicing the skills of history or the styles of writing or the understanding of culture. And while History has themes and English has great turns of phrase that should be memorized, missing a few for any particular reason does not preclude the student from jumping back into the subject next time around. That great writers spent their youth ignoring their teachers or participating in traditionally educational activities speaks to the flexibility of these subjects to welcome the “late bloomers” into them.


And while the proposed math curriculum does not completely refactor out prerequisites, it does begin to weaken them. This, I think, is a good thing for getting more students on board. The focus shifts from performing specific tasks (like manipulating one trigonometric expression into another) to being able to constantly improve a set of skills, specifically, looking out into the world, identifying a problem, collecting data on that problem, and using that data to help determine means to address that problem.


These skills, identifying problems and supporting the analysis of those problems with facts, is a skill whose importance is paramount. Indeed, the Common Core State Standards for English and Language Arts bring up this point as early as the Seventh Grade.[15] But as data become easier to gather and process, “facts” shall come more and more to mean monstrous collections of data. And being able to discern what “facts” are plausible from these collections of data becomes more and more important.


**What next?**


There are many obstacles to this dream, even without the status quo biases that I discussed at the beginning. Even the simple job of building materials, much less the community and teacher infrastructure, to support this change is massive and will take years. And though the Common Core standards are reasonable, the move to extreme standardization of the schools does preclude experimentation on the parts of individual schools and teachers with curriculum.


Where next? Immediately, the first order of business is to understand if such a high school curriculum could be built without changing the middle and elementary school curriculum too much, since changing four years worth of curriculum is already extremely disruptive.


Assuming that is the case, then there are several possibilities. One is to take the route of the Bootstrap curriculum and explicitly teach specific skills required by the current curriculum while supplementing them with computer science concepts. This runs into the problem that the school day is already pretty full, especially for high-achieving kids, and adding in new “requirements” would burden them.


Another route is to build a charter or charter-like school around such a curriculum and forsaking the traditional standardized tests. This has the problem of being risky in that if the curricular idea is terrible, then these kids will be disadvantaged relative to their peers.


Whichever way is chosen, the process will be long, involving the hours of many people, not just writing curriculum but also from the community, who themselves by design will be involved in the week-to-week of the courses, and involving the training of many educators in a relatively new type of math curriculum.


---


**Footnotes**

1. Some would quibble with the word “improve.” If, dear reader, you are such a person, I implore you to replace this with “radically transform.”
2. Well, except often in math, where even though mathematicians have been writing long form proofs for years, students are often stuck with the terrible two-column variety.
3. Though, traditionally the “vertical” reinforcement of math has gone off the deep end into the various properties of conic sections and the opaque relationships between trigonometric functions without the aid of complex numbers. Common Core actually does a fair bit to help on this front.
4. Though maybe he [faked it](http://www.nytimes.com/1990/01/23/science/after-400-years-a-challenge-to-kepler-he-fabricated-his-data-scholar-says.html).
5. Long division, taking determinants, solving polynomials, taking formulaic derivatives all spring to mind, though there are many more.
6. A piece of advice to aspiring data scientists: If you are applying for a job and they ask you to do a written test ahead of time, there should be at least one plot in your writeup. Unless your solution is brilliant, you aren’t getting hired if there’s not at least one plot.
7. To what I think is its tremendous credit, this sort of writing is integral in the PARCC tests developed for Common Core-aligned curricula in some states. I have not had the chance to review the competing test, called Smarter Balance, but I would expect it would be similar.
8. There are actually many teachers who use peer grading, and also quite a bit of research on its effects, some good, some bad. The point here is that we should be open to using novel methods of grading, and especially interested in exploring how computers can facilitate these novel methods.
9. What I do not talk about here but which is also an essential problem with any change to the curriculum is that parents play a huge role in their children’s education, and so any change to the curriculum that involves reeducating teachers must also, to some degree, involve reeducating parents. Since this piece is about high school, by which time many parents have already “given up” on helping their students with homework because they are not “Good at Math” (a fact I do not have hard numbers for, but I have commonly experienced among my students), I’m leaving this massive issue out of the main text.
10. Of course, take this with a grain of salt. I tend to only get to ask this question of kids in computer science classes.
11. These solutions often take the form of “algorithms,” which are central to computer science, and thus the name “computational thinking.”
12. Perhaps my favorite aspect of the Bootstrap curriculum is that they emphasize professional development, a woefully underappreciated aspect of improving the curriculum.
13. There is no universal definition of Algebra II as far as I know. However, the Common Core has gone a long way to standardizing a definition. The [PARCC Model Content Frameworks](http://parcconline.org/resources/educator-resources/model-content-frameworks/mathematics-model-content-framework) may be useful for the interested.
14. This is not to say that warnings about small samples shouldn’t be ingrained into students as well, but here large data sets can help as well. For instance, a simple exercise for the whole class could involve giving every student a randomly sampled set of 20 rows from a very large data set and asking them to run some sort of analysis. In the end, each student would come to vastly different conclusions, and thus, come to learn that sample size matters.
15. See CCSS.ELA-LITERACY.RI.7.9, which states, “Analyze how two or more authors writing about the same topic shape their presentations of key information by emphasizing different evidence or advancing different interpretations of facts.”
