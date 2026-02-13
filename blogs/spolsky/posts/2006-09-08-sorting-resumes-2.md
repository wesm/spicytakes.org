---
title: "Sorting Resumes"
date: 2006-09-08
url: https://www.joelonsoftware.com/2006/09/08/sorting-resumes-2/
word_count: 2833
---


The standard job application of cover letter plus resume is a phenomenally weak way to introduce a candidate. They give you only the faintest clues as to the quality of an applicant.


Sometimes, though, a resume gives pretty strong *negative* clues which allow you to screen out applicants without going much further. Once I got a resume from someone who claimed to be an expert in Microsoft Window [sic] programming. Another time the only experience listed on the application was a job at Dunkin’ Donuts. That resume did a pretty good job of following all the suggestions that high school career-guidance advisors love to give out (this guy “managed trays of donuts”) but there was not a smidgen of evidence that the applicant had ever seen a computer.


Other than that, though, it can be extremely hard to tell much about a candidate from a resume. Our policy at Fog Creek, then, has three parts:

1. We try to be selective about how we advertise our jobs, so as to limit the amount of noise in the resume pile.
2. We certainly don’t hire based on resumes; we only screen *out* based on resumes to reduce the number of people whom we have to interview.
3. In order to sort the remaining resumes to decide what order to interview people, we use a strictly objective system of reviewing and scoring them, so at least we are being fair and consistent in our interpretation of that very weak signal that comes from resumes.


There are several fairly objective measures that we look at, again, *solely for the purpose of sorting resumes* so that the first people we call are the ones that are most likely to work out.


**Passion.** We look for evidence that the applicant is passionate about computers and really loves programming. Typical evidence of this:

- Jobs with computers or experience programming going back to a very early age. Great programmers are more likely to have spent a summer at computer camp, or building an online appointment scheduler for their uncle the dentist, rather than working at Banana Republic folding clothes.
- Extra-curricular activities. People who love programming often work on their own programming projects (or contribute to an open-source project) in their spare time.
- Waxing rhapsodic in their cover letter about how they were moved to tears by [The Structure and Interpretation of Computer Programs](http://www.amazon.com/o/asin/0262011530).
- Sometimes certain programming languages or technologies on a resume indicate evidence of someone who loves programming enough to explore new technologies. At the time I’m writing this, seeing Ruby on a resume is a good sign of the kind of programmer who loves to check out the latest thing and try to improve their skills because they’re passionate about programming, because not so many employers are really demanding Ruby yet. You have to be careful here; in 1996 Java on a resume was a sign of the same passion, but today it adds almost no information.


**Pickiness.** We look closely at the cover letter for evidence that the applicant really wants to work for *us.* We don’t want to see a generic cover letter talking about me, me, me: we want to see a coherent argument as to why they’ve thought about this seriously and concluded that Fog Creek is the place they want to work. There are two reasons for using this as a clue. First, it’s a sign that the candidate is not applying to hundreds of jobs at the same time. The fact that they took the time to learn about Fog Creek and wrote a custom cover letter just for us means that they have a lot of confidence in their abilities, so they’re applying to a select few employers, not bulk mailing a thousand. A bulk-mailed resume can be a symptom of desperation. More importantly, a custom cover letter is a sign that if we *do* make this candidate an offer, they’re likely to accept it. That improves our yield. If I only have time to interview six people, all else being equal, I’d rather interview six people who really want to work for Fog Creek, not generic smart people that are also applying to a hundred other jobs. All else being equal.


**English.** Scoring resumes by English skills was a hard decision for us to make, because computer programming is one of those fields where an immigrant who doesn’t speak English can still be a brilliant programmer. That said, years of experience working with programmers have taught me that programmers who can communicate their ideas clearly are going to be far, far more effective than programmers who can only really communicate well with the compiler. It is crucial for documenting code, it is crucial for writing specifications and technical design documents that other people can review, and it’s crucial even for those meetings where you sit around discussing how to do something best: brilliant programmers who have trouble explaining their ideas just can’t make as much of a contribution. In this particular category, we also consider the neatness and orderliness of their resume. A disorganized resume rife with grammatical errors where nothing lines up is a pretty big red flag for a disorganized thinker or just general sloppiness; for many jobs this can be fine but not for software development. In particular we usually completely disqualify resumes that are full of English mistakes. It’s not that hard, even for a non-native speaker, to find someone to check your resume, and failure to do that usually reflects a profound lack of concern over the quality of the things that you do. That said, we try to be considerate of  non-native speakers who are nonetheless excellent communicators: leaving out articles in that charming Eastern European way, or starting every paragraph with “So” in charming Pacific Northwestian way, is not a showstopper.


**Brains.** In this category we’re looking for evidence that a candidate is, well, smart, or at least, the kind of nerdy brainiac that went to math camp. Signs of this include high GPAs, high standardized test scores, honors societies like Phi Beta Kappa, people who participate in Top Coder competitions, play competitive chess, or go to ACM Programming contests.


**Selectivity.** Another thing we look for on resumes is evidence that someone has gone through some highly selective process in the past. Not everyone at Ivy League schools is worth hiring, and not everyone at community college is worth avoiding, but getting into a very selective school does at least mean that *someone, somewhere* judged you using some kind of selection process and decided that you were pretty smart. Our company criterion for selectivity is usually getting into a school or program that accepts less than 30% of its applicants (there are about 60 schools in the US that meet this standard), or working for a company which is known to have a difficult application process, like a whole day of interviews. Highly selective branches of the military like officer’s training or pilot’s courses, or even just getting into the Marines indicates someone that has made it through some kind of difficult application/selection procedure and all in all this is a positive sign.


**Hard-core.** For experienced programmers, there are certain technologies that are considered somewhat more hard-core than others, simply because they are, well, harder to do well. Again, this is a pretty weak indicator, but all else being equal, I’m more impressed by someone who has done work in OCaml than someone who has worked in Java. Assembler or device-driver or kernel work is somewhat more impressive than Visual Basic or PHP. C++ with ATL is harder than Perl. People who have worked on operating systems or compilers are more hard core than people who have worked on simple database front-ends.


I’m sure that this will be seen as incendiary; after all, most of my personal programming experience in the past five years is with VBScript, which is sort of like a version of Visual Basic dumbed down for people with severe brain trauma. Remember again that I said that resumes are a very weak way of judging programmers and you only get the faintest signals from them; that said, some technologies are just *harder* than other technologies and if you happened to have worked with them successfully, there’s a smidgen more evidence that you might be the right person to hire, so for the purpose of sorting resumes, difficult technologies tend to float you to the top, while claiming competence in, say, Microsoft Word tends to float you toward the bottom.


**Diversity.** Before I start a massive flame war of international scope by using the loaded term “diversity,” let me carefully define what I mean by this. Specifically, I’m looking for people who come from enough of a different background than the existing team that they are likely to bring new ideas and new ways of thinking to the team and challenge any incipient groupthink that is likely to keep us boxed into our own echo-chamber way of thinking about things. When I say different background, I mean culturally, socially, and professionally. Someone who has a lot of experience with enterprise software may bring useful diversity to a team of internet programmers. Someone who grew up poor is going to bring useful diversity to a startup full of Andover preppies. A stay-at-home mom rejoining the workplace may bring useful diversity to a team of recent graduates. An electrical engineer with Assembler experience may bring useful diversity to a team of Lisp hackers. A recent college graduate from Estonia may bring useful diversity to a team of experienced management consultants from the midwest. The only theory here is that the more diverse your team is, the more likely that someone on the team will have some experience in their background that allows them to come up with a different solution.


It is *really really important* to remember that these categories—Passion, Pickiness, English, Brains, Selectivity, Hard-Core, and Diversity—are *not* hiring criteria. They are just too weak for that. There are way too many excellent people who would score low on this test or poor programmers who would score high. Before you go off ranting about how Joel only thinks you should hire from the Ivy League, or that I have some kind of GPA fetish, or whatnot, it’s important to understand that this list is just not a list of reasons to hire someone or reject someone. All it is is an objective and fair way to sort a big pile of resumes to find the candidates who are most likely to work out so that you can interview them first, and *then* decide if they’re worth hiring.


**If resumes are so weak, can’t we add some other hoops?**


This is certainly not, by any stretch of the imagination, the ideal set of rules for sorting resumes. I’d much rather be able to sort resumes by the candidate’s ability to implement a recursive algorithm, how long it takes them to find a bug in code, or whether or not they can keep nine items in short term memory, all of which are better indicators of success as programmers than things like whether you got past an elite college’s admissions committee. Unfortunately, those things aren’t on resumes.


One temptation of recruiters is to try and add a few extra hoops to the application process. I’ve frequently heard the suggestion of including a programming quiz of some sort in the application procedure. This does work, in the sense that it reduces the number of applications you get, but it doesn’t work, in the sense that it doesn’t really improve the quality. Great developers have enough choices of places to work that only require the usual cover letter/resume application to get started; by inventing artificial hoops and programming tests and whatnot simply to apply, you’re just as likely to scare away good programmers as weak programmers. Indeed, you may be more likely to scare away the best programmers, who have the most alternatives, and get left with a pool of fairly desperate candidates who are willing to do extra work to apply simply because they don’t have any alternatives.


**Don’t look for experience with particular technologies**


Once I was on a panel at NYU giving students advice on careers in I.T. My advice, excerpted from [this article](https://www.joelonsoftware.com/articles/CollegeAdvice.html), was that before graduating you should make sure to learn how to write well, maybe by taking a creative writing course, and take a class in Econ so that the business side of the business isn’t a mystery. I also recommended at least one low-level programming course in C or Assembler just to help you understand how computers work at a lower level.


On the panel with me was a nice chap from a local headhunter, in fact, one of the better tech recruiters in the city. His speech consisted of 15 minutes of tedious alphabet soup. “We’re seeing a lot of XML, some C++, SOAP and WSDL are getting hot but you’re not seeing as much COM or even ATL.” And on, and on, until my eyes were spinning. This was a fellow who entirely thought of the world in terms of keywords on resumes.


To top programmers, the most maddening thing about recruiters is their almost morbid fascination with keywords and buzzwords. The entire industry of professional headhunters and recruiters is bizarrely fixated on the simple algorithm of matching candidates to positions by looking for candidates that have the complete list of technology acronyms that the employer happens to be looking for. It becomes especially infuriating to realize that most of these recruiters have no idea what any of these technologies *are*. “Oh, you don’t have MSMQ experience? Never mind.” At least when real estate agents prattle on about Subzero refrigerators and Viking stoves, they at least know what these things *are* (although any stainless steel refrigerator counts as “Subzero” these days). The easiest way to catch-out a technical recruiter is when they inevitably insist on 5 years of experience with Ruby on Rails, or refuse to consider someone for a “Windows API” job when they only have “Win32” on their resume.


The reason recruiters do this is because it’s easy, it can be computerized, and it’s the only way they know how to judge developers.


**For almost all software development positions, though, it is the worst possible way to hire.**


Our philosophy is that we’re hiring for the long term, and any technology you happen to know right now may well be obsolete next year. Furthermore, some of these technologies are very easy to learn. If I needed to hire someone to do Ruby development, someone with extensive Smalltalk and Python experience who had never even *heard* of Ruby would be a lot more likely to be successful than someone who read a book about Ruby once. For someone who is basically a good software developer, learning another programming language is just not going to be a big deal. In two weeks they’ll be pretty productive. In two years, you may need them to do something completely different in a programming language which hasn’t even been invented.


The keywords section of a resume can’t be trusted much, anyway: every working programmer knows about these computer programs that filter resumes based on keywords, so they usually have a section of their resume containing every technology they have ever touched, solely to get through the filters.


There is, I think, one exception to this rule. If you’re hiring an architect or head developer—that is, the chief software engineer who is going to have to lay out the initial code and figure out how things work together, you probably want to hire someone with a lot of experience in the technology that you’re using. A team developing GUIs for Windows using C++ and MFC is going to need at least one Windows/MFC guru somewhere on the team who can make sure that the code is organized correctly in the first place and who has enough experience to know how to solve the really hard problems that might come up.


Don’t start a new project without at least one architect with several years of solid experience in the language, classes, APIs, and platforms you’re building on. If you have a choice of platforms, use the one your team has the most skills with, even if it’s not the trendiest or nominally the most productive. Occasionally, this may mean you interview to find a candidate with really extensive experience in a particular set of technologies (not keywords, mind you: the whole stack, such as LAMP or .NET or J2EE). But most of your software developers should not be hired by keyword matching.


Sorting resumes is only one aspect of the hiring process, which includes [making an environment that is attractive to programmers](https://www.joelonsoftware.com/articles/FieldGuidetoDevelopers.html), [attracting good resumes in the first place](https://www.joelonsoftware.com/articles/FindingGreatDevelopers.html), and using a [rigorous interview process](https://www.joelonsoftware.com/articles/fog0000000073.html) that helps you hire the programmers who can [hit the high notes](https://www.joelonsoftware.com/articles/HighNotes.html).
