---
title: "Hiring programmers with a take-home test"
date: 2020-04-28
url: https://signalvnoise.com/svn3/hiring-programmers-with-a-take-home-test/
slug: hiring-programmers-with-a-take-home-test
word_count: 1540
---


There’s no perfect process for hiring great programmers, but there are plenty of terrible ways to screw it up. We’ve rejected the industry stables of [grilling candidates in front of a whiteboard](https://twitter.com/dhh/status/834146806594433025) or [needling them with brain teasers](https://signalvnoise.com/posts/3071-why-we-dont-hire-programmers-based-on-puzzles-api-quizzes-math-riddles-or-other-parlor-tricks) since the start at [Basecamp](https://basecamp.com/). But you’re not getting around showing real code when applying for a job here.


In the early days of the company, we hired programmers almost exclusively from the open source community. I simply tapped people I’d been working with on the [Ruby on Rails](https://rubyonrails.org) project, and I knew that their code would be good, because I’d seen so much of it! This is how we hired Jamis, Jeremy, Sam, Josh, Pratik, Matthew, and Eileen.


But if you only consider candidates from the open source community, you’re going to miss out on plenty of great programmers who just don’t have the time or the inclination to contribute code to open source.


And unfortunately, it’s rarely an option for candidates to submit code from a previous job with an application to a new job. Unlike design, which is at least somewhat out in the open, commercial code is often closely guarded. And even if it wasn’t, it’s often hard to tease out what someone was actually personally responsible for (which can also be a challenge with design!).


So what we’ve started to do instead at Basecamp is level the playing field by asking late-stage candidates to complete a small programming assignment as part of the final evaluation process. I’m going to show you two examples of these projects, and the submissions from the candidates that ended up being hired.


But first it’s important to recognize that we don’t ask applicants to do these assessments as part of their initial application. We simply get way too many applications for most openings to make that practical or fair. [The last opening on the Research & Fidelity team](https://signalvnoise.com/svn3/basecamp-is-hiring-a-front-end-programmer/) got over 1,300 applications. Nobody can review that many code submissions!


So we whittle the group of candidates down aggressively first. This means judging their cover letter and, to a far lesser extent, their resume. For the opening we had on the Research & Fidelity team, we gave 40 people the take-home test, and even that proved to be too many. For [the opening we had on the Security, Infrastructure & Performance team](https://signalvnoise.com/svn3/basecamp-is-hiring-a-senior-programmer/), we only gave 13 people the take-home test. That felt better. In the future, we’ll target fewer than 20 for sure.


Then there’s the assessment itself. I’ve heard many fair complaints that companies are asking candidates to complete massive projects that may take 20-30-40 hours of work, which is all unpaid, and which might be difficult for candidates to fit in with their existing job and life. Yeah, don’t do that. Asking someone for forty hours of work product, without pay, which might well go nowhere, is not what we do or advocate at Basecamp.


On the design side, we have asked candidates to complete more substantial projects, perhaps asking 10-20 hours of work, but then we pay them for the work. It’s like getting hired for a small freelance gig, even if you don’t get the job, and even if we’re never going to use the work.


But for programmers, we don’t need a project that large to get a good indication of someone’s programming skills or thought process. With both of the last two openings, we used assignment that were estimated to take 3-5 hours to complete.


That’s still a very substantial commitment! I wouldn’t ask anyone to submit such unpaid work without believing they were clearly in the running for the position. But when you look at our numbers, we usually don’t end up asking more than 1-3% of our applicants for such a commitment.


And it’s worth contrasting that against the work we’re not asking people to do. We don’t run candidates through some recruiter mill, where they have to do phone screening after phone screening. We don’t use any sort of automated tooling to scan resumes or whatever. We don’t even have people travel for interviews.


On our side, we often spend *weeks* perfecting the job opening itself. We put in an absolutely tremendous amount of work to conduct a fair, human, respectful, and thorough job search.


And the rules of the game are specified up front. You shouldn’t apply to a programming job at Basecamp unless you’re prepared to put in the work writing a considered, tailored cover letter, and then making the 3-5+ hours available to complete the programming assessment, if you make it into that top group of 1-3% of applicants.


## The SIP assignment


Anyway, let’s take a look at these take-home assignments. The first is from our Security, Infrastructure & Performance team, and it was designed by Rosa. This was for a senior programmer opening. 13 applicants were asked to complete the assignment, and they were given a full week to do it (such that the estimated 3-5 hours could be spread out over several week nights or maybe the weekend).


It focused on a sliver of a real problem we’d been dealing with at Basecamp: [Support for ban in rack-ratelimit](https://gist.github.com/rosa/783d23a4a835b9a81ea7e8cec5eaf671). So it wasn’t some Tower of Hanoi abstract, computer-sciency test that you can look up a million solutions to, and which favor recent grads of CS algorithm courses. No, it was for implementing a feature in the same way you might well be asked to do on the job. There was a clear example of the API we wanted, and then candidates could solve it as they saw fit.


Jorge Manrubia, who we ended up hiring, submitted his solution as a [full pull request](https://github.com/jorgemanrubia/rack-ratelimit/pull/1) –– complete with system tests and performance tests and documentation! It was a very comprehensive solution, but almost to a fault. I remember one of my concerns with Jorge’s submission was that it was borderline gold plated. We had several other submissions that were also wonderful, but far smaller, which could just as well had made for the final choice.


Jorge admitted to spending closer to 7-8 hours, in total, on his submission. We never policed this, because it really wasn’t a material part of the assessment. The solution would have been as compelling without all the extracurriculars, and several other candidates shone just as brightly with more modest submissions.


Which goes to a second point: Completing a programming assignment is required *but insufficient* to land a job at Basecamp. You can’t get hired without demonstrating a core competency in writing great code, but you also won’t get hired just because you can write great code alone.


The programming assessment simply unlocks the next step of the evaluation process. Out of the 13 candidates that received the programming assignment, 10 progressed to a first phone interview with Andrea (our head of people ops), then 6 progressed to interviews with the whole team, and finally 2 candidates got an extra interview to determine who we were going to hire.


## The R&F assignment


For [the programmer opening on our Research & Fidelity team](https://signalvnoise.com/svn3/basecamp-is-hiring-a-front-end-programmer/), we followed a very similar process, but made the mistake of giving the programming assignment to too many people –– 40 in total. As discussed earlier, we should, and will in the future, cap that to 20 max.


This assignment was designed by Javan, and focused on another real-life sliver of the work we were doing on HEY: [Enhance datalist autocomplete](https://gist.github.com/javan/b3205fa057341f09d97710d7941107a7). The challenge came complete with the basic HTML form, and then directions on how to use JavaScript to enhance it to get us the universal autocomplete across the three major browsers.


Nabeelah Ali, who we ended up hiring here, submitted [her solution](https://gist.github.com/nali/69d374d403e95276149d9511ac54827e) with fewer flourishes than Jorge, but code no less impressive. Everything contained in a single page to make the solution work.


Like Jorge, Nabeelah also ended up spending more than the estimated 3-5 hours to complete the assignment. Somewhere around double there too. Much of that spent refactoring and polishing the solution. As a new mother with a 10-month old, just being back to work, and dealing with nightly wake-ups, this definitely wasn’t easy. But, as she said, “I would do that any day over a doing a live coding challenge”.


Which goes to the point that the alternative to a take-home programming assignment is rarely “nothing”. It’s often spending as much time, or more, traveling for a day of packed interviews. Some times traveling more than once! Dealing with the whiteboard assessments. Or going through abstract programming games or assessments that aren’t reflective of the work the team actually does.


There are of course other alternatives too. Some do half a day of pair programming together with candidates. Others ask for a code review, where the candidate comments on existing code. To me, the former often relies on an in-person meeting to work well (and that wasn’t going to happen, with Jorge hired from Spain, and Nabeelah hired from Norway), and the latter isn’t someone’s own code.


Hiring is hard. Applying is hard. Doing either with programmers without looking at actual code they wrote often risks leading down a path of bias (or, as we call it today, “fit”), credentialism, whiteboard puzzles, and brainteasers.


We’ll stick with the hard work.

