---
title: "The Last Technical Interview"
date: 2026-05-29
url: https://steve-yegge.medium.com/the-last-technical-interview-bc13ddcf4564?source=rss-c1ec701babb7------2
source: medium
word_count: 4403
---


Today we will pour one out for the vaunted technical interview process, which is on its last leg. And we’ll talk a little about what’s replacing it.


This post has been almost 35 years in the making; that’s how long I have been conducting technical interviews. And for a few of those decades, I also worked to try to improve the process itself. I’ve had to care a lot about it, because it’s so broken.


It turns out interviewing was broken long before I learned the trade, and despite the many attempts to band-aid it, it’s still broken today. It has managed to survive in spite of that. But it is finally dying on its own. People are a bit unclear on what’s next, so we’ll talk about some of our options.


But it’s not an easy path I bring you, no silver bullet. Remember that, grasshopper, when you get to the end and come back to yell at me.


**The Two Big Dogs**


Back at Amazon, we had this elite group, the Bar Raisers, which I hear is similar to a role at Microsoft they call As-Appropriate (AA). In both cases, a trusted interviewer (the BR/AA) is assigned to every interview loop, and has the power to veto any unqualified people the interviewers try to sneak through. I was a BR, and also part of “Bar Raisers Core”: a small group Bezos and Dalzell tasked with defining the BR role itself, choosing new bar raisers, training them, and reporting on the program’s efficacy.


The BR and AA roles are a tacit acknowledgement that you can’t trust your interview teams to make good hiring decisions. Which even more broadly, suggests that if every single interview loop needs a babysitter, then it is a flawed process. But we were doing our best.


Of course we don’t frame it as babysitting, naturally. We cheerlead and rah-rah about keeping a “high hiring bar.” And BR/AA aren’t the end of it. There are tons of other interview process band-aids, all variations on how you conduct four to six interviews in a single day. Everything revolves around fitting the assessment into a single round or two of interviews. That part never changes.


None of these band-aids really help — we still all hire tons of false positives (unqualified) and turn away false negatives (actually qualified), despite every attempt to make the process perfect, or even good.


The reality is that talent evaluation, a corner of our industry that hasn’t changed much in five-ish decades, is embarrassingly busted. It just doesn’t work that well in practice.


The people who know this best, and who feel it most day to day, and who ultimately have the *least* power to change it, are all in HR. The tech side of the tech industry doesn’t want to change it because of inertia: the process has worked just barely well enough all these years to resist an overhaul. So all HR can do is show us how bad it is, and then try to do damage control when it fails. I’ll share an amazing story about this in the next section.


After Amazon, I kept on trying to improve the interviewing process while I was at Google. I spent years on Google Kirkland’s “Hiring Committee”, where we processed thousands of Microsoft résumés, would-be escapees from over the hill in Redmond. I published a 30-page internal résumé screening guide. I even wrote a blog post,[ Get That Job At Google](https://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html), which is still handed out by Google recruiters, seventeen years later. I took this stuff pretty seriously back then!


In short, there is very little that I don’t know about the tech-assessment business. And I’m about to pull a Kitchen Confidential on it.


This post comes with a diagnosis and a prescription. But the important part is the diagnosis. I want to convince you that we need a radical change in how we assess people, and that tech interviews are on their last leg.


Let’s see how well I do. As for the solution, we can figure that out once we agree that it’s a problem.


**Remember That Time We All Fired Ourselves?**


The outcomes from interviewing are statistically terrible. Google did wave upon wave of analysis over the years, and all the results were incredibly depressing.


To name just a few off the top of my head: interviewers barely agreed with each other. Put the same candidate in front of two of our sharpest people and you’d routinely get a confident “strong hire” from one and a flat “no” from the other. There’s no oracle interviewer, not even Jeff Dean.


And once people were actually on the job, their interview scores told you next to nothing about how they’d do — at least the way we ran the loops. Hell, some of our star performers failed their Google interviews four or five times, finally got in after 2+ years, and then outshone everyone else.


Interviewing, it turns out, is a big game of darts. A “do I like you” dating round.


All we could find at Google, from all the statistics, is that there are a bunch of horrible unconscious interviewer biases keeping us from hiring people who ought to be working there. Google never published the results internally and I just got to hear rumors from HR friends, but yeah it was pretty bad.


Gergely asked me about the tech-assessment situation in one of our podcasts, and I told him a story that I think is relevant so I’ll recount it here. You can hear the longer, funnier version over on his podcast.


At Google, rather than putting a little black desk on every interview loop, they just assumed all the interviewers had their heads up their arses (an evidence-based assumption), and they formed a committee at each site called Hiring Committee (HC). This committee acted as the final arbiter and gatekeeper on all hiring for the site. And I was on it for quite a few years.


Our HC group at the time was roughly fifteen strong, and included many local powerhouse Googler colleagues, including co-inventors of huge technologies, authors of interviewing book series, and people who are now very senior leaders.


We felt like we knew our shit.


One day, the recruiters gave us a special round of packets to review. In these special packets, we were able to read the interviewer notes and candidate responses. All personal details were stripped out, and we were told it was a “calibration exercise.” We had to do our regular voting job with these special packets, and see how it went. I think we may have assumed they were from another site, since cross-site calibration was common.


Our group did our job, and voted not to hire about 2/3 of the packets. This was about par for the course.


But surprise surprise, this time, those were *our own packets* from when we had all interviewed at Google. The recruiters had tricked us into reviewing our own interview packets, and we had voted not to hire most of our own group.


For that brief moment, we all had a glimpse into how utterly broken our process was. The people-team had rubbed our noses in it.


But we never fixed it.


![](https://cdn-images-1.medium.com/max/1024/1*7PEsAhc1jgBhq1mJn2fU6g.png)

*The moment we realized it was us*


**Change is Taboo**


I once challenged the interview process at Google in a public mailing list, and an Important Eng Leader took me aside and told me I’d “farted in church.” People are not allowed to question whether the interview process is valid. Challenging it is akin to casting aspersions on the entire engineering staff. First of all, how dare you?


Moreover, many engineers and managers continue to defend the process, even knowing how broken it is, because it’s a gauntlet that they passed, so others must, too. Which sounds very silly when I say it like that, but you hear echoes of it whenever you suggest changing the process.


When you add it all up, and putter around with it for about 35 years, you ultimately find that interviewing, which aims to determine “can this person do this job,” is *fundamentally* unable to answer that question with any degree of reliability. It’s bordering on pseudoscience.


Bravo to Google for at least trying to measure it. They did find some actionable stuff. For instance, any more than four interviews and you’re just playin’ with your food. Stuff like that. But overall it was a bleak and mostly non-actionable picture.


Most companies never introspect at all on their own interviewing processes — at least, not in any real “we’re aiming to change this” sense. They might shuffle around which competencies get covered, or what the debrief meeting might look like.


The fundamental process — a short series of 1-hour interviews — hasn’t changed in fifty years. We have all been using the same stupid, broken interview process since before most of us were born. Dunno about you, but I’ve had enough of it.


So in today’s blog post, I’m going to show you everything that’s been tried, then point in the direction of a better way. And as an industry, we can start moving in that direction. As long as enough of us are doing approximately the same thing, it should gain traction.


I believe that within a few years we will mostly stop conducting technical interviews, and they will fade into a cute historical footnote like phrenology (which I would not be shocked to hear some interviewers still use). Interviewing will become just another somethin’ weird we used to do.


You ready? I am. Let’s goooo!


**The Signal Problem**


Talent assessment is a problem of signal. You need a lot of it. You want to try to paint an increasingly clear picture of the candidate, and that takes a lot of data.


The first signal source you get is a candidate’s résumé. “A résumé,” as Dave Barry tells us, “is much more than just a piece of paper. It is a piece of paper with lies written all over it.” Companies get thousands to millions of résumés per year, and the signal-to-noise ratio is awful. AI-assisted writing is exacerbating the problem, and résumés have become all but useless as a signal today.


What we *used *to do first was a technical phone screen. They were super hard, for both sides. Everyone hated them. Imagine writing code for someone with only audio. Zoom made them obsolete. But even those awful phone screens were still a *much* better signal than a résumé, because you get to spend time with the person.


The next level of signal is “work completed”, which includes credentials and assessments like coding academies and challenges, as well as the person’s OSS work. They are both weak signal sources because you don’t get to work with the person while they’re doing it. But they can be a useful tie-breaker or foot-in-the-door signal that boosts you to the next evaluation stage.


The hiring signal doesn’t start to improve dramatically until you get to on-site interviews. But even in-person interviewing is infamously unlike real-world work. How does interviewing at a whiteboard compare to working with them in real life? I think we all know the answer to that.


So you get a few minutes with their résumé, a half hour video screen, and a handful of in-person interviews. Today’s standard hiring process only involves collecting a few hours of signal, in order to make a decision that could last years.


**Provisional Employment to the Rescue**


The gold standard talent-assessment signal, when available, is an internship. This situates the candidate as a quasi-employee for typically around 3 months. They are part of a team, they get “real” work — as real as the team can make it, which varies — and they are evaluated on how well they complete that work.


A 3-month internship is self-evidently a much stronger signal than a one-day interview loop. Chances are, unless you really drop the ball on managing the internship (it’s easier to mess up than you’d think), then you’re going to have a much clearer picture of their skills and capabilities, and how well they “mesh” in your team, than you did at the start of the internship. The signal is so much stronger than the interview loop that you often ignore the interview feedback when making the final decision. It was just what got the intern their foot in the door, and the internship itself turns into the assessment.


I’ve seen companies go even further than an internship, in their quest to find the Right People For The Job. The first company I worked for, Geoworks, had a strict requirement: every single candidate had to complete a six-month co-op, before they would make the hiring decision.


The co-op resembled a summer internship, but we were highly paid full-time employees (with benefits for anyone who didn’t have them from school), doing hardcore real work for twice as long, all of us desperately wondering if we were going to get hired at the end of it.


There is a material difference between the signal from an internship (~7 weeks of usable work time after ramp-up) vs a co-op (5 months actually working). That year, 1992, Geoworks hired 3 out of 8 of us. Crazy high bar, it felt like they were making new Witchers. Sad for the ones who didn’t make it. But their approach produced a company of nearly all stars and superstars.


As evidence of the co-op’s effectiveness, Amazon acqui-hired the Geoworks Seattle office in 1999, a few months after I joined, bringing in nearly 30 engineers (I kicked off the process myself, and it was surreal to see my old coworkers wandering the halls a few months later.) Amazon leaders have said many times, and I’ve even heard it from an old-timer VP as recently as two weeks ago, that the Geoworks group was by far the strongest group of people they ever brought in. Many Geoworkers went on to do incredible things at Amazon and/or Google.


So the Geoworks 6-month co-op is platinum-level signal. Can you go further? How far are you willing to go? On the supply side, the University of Waterloo famously sends their Computer Science students through a total of six internships, giving them roughly 2 years of real-world work experience before they graduate. This boosts the signal out of Waterloo, and companies compete fiercely for Waterloo interns and grads above all other schools.


What we’re talking about here is *provisional employment*. It’s lazy evaluation before binding the “hire” variable. It doesn’t matter if it’s an internship, a co-op, or a contract-to-hire, it’s a temporary position, not a part-time one: Provisional employment is a different axis from fractional employment. Provisional employment is *currently* the best solution the industry has found for the problem of knowing reliably who to hire, before you hire them.


But wait, if provisional roles are so effective, why bother with making them provisional? Why not just hire people, put them to work, and fire them if they don’t work out?


If only it were so easy. Actually, it is, except for, you know, The Law. Most provisional employment schemes are workarounds for U.S. employment law, which, believe it or not, affords employees some protections, even if those protections are weak compared to other parts of the world.


In the U.S. you generally can’t just up and fire someone, even if they are underperforming, even if it’s at-will employment, without risking a lawsuit and some sort of cash outlay. This is what makes hiring decisions so high-stakes.


But if the employee is *provisionally* employed, well, that’s a different matter. Their internship or contract is just “over.” Thanks for playing.


So in situations where the company can get away with it, they can and absolutely do use provisional roles to defer making permanent role decisions for as long as possible.


**You call this a rescue?**


OK, then! If provisional employment is the answer (it’s not, but let’s pretend it is for the moment, since it’s best-of-class for now), then why aren’t more companies requiring internships before making their hiring decisions?


The reason is, hiring engineers has historically been so competitive that you couldn’t convince a senior engineer to *do* an internship. College kids might have all the freedom in the world, but adults have families and mortgages and need steady employment. They did not want to sign up for a job they might not get to continue after 3 to 6 months. A job where they’re actually being constantly evaluated for the go/no-go decision. It’s a no-brainer that they’ll go elsewhere.


So the industry converged on not requiring it.


That was the old equilibrium, and it only held because good engineers always had somewhere better to be. That assumption is starting to wobble. I won’t belabor what I think you all can already feel coming, but if a sizable slice of the skilled-labor pool ends up “between gigs” at the same time, there may be no elsewhere for them to go.


At that point, if there are enough people on the market, try-before-you-buy is no longer an insult that you’d never dare float to a senior engineer. It’s a foot in the door that they’ll be glad to have.


Today’s hiring process is heavily optimized, and it’s going to be hard to change. I suspect this is why we are seeing so many tweets from founders firing their HR teams. HR is designed to keep things compliant with laws that are struggling to keep up with the pace of change, so they’re admittedly in a tough spot. Just be aware that if you want to make radical changes to your hiring process, there will be strong pushback from all corners of your org.


In spite of that pushback, I see some forces appearing on the horizon which are converging to squeeze the system, after a half a century, to its breaking point.


We’re seeing the first breakdowns at the fringes — offline assessments poisoned by AI cheating, online interviews turning out to be fronts for sanctioned North Korean IT workers, résumé floods that cannot be dealt with in any reasonable way. The system is undergoing tremendous strain that it was never designed for.


There’s an even more fundamental breakdown happening, which is the rate of change of the *shape* of knowledge-work roles. Hiring used to be something that changed very slowly. Every ten years there would be a revolution: internet, mobile, cloud, and people would have to learn some new stuff, and update job descriptions. But for the most part, the fundamentals of computer science, software engineering, project management etc. have remained stable for decades.


This meant that it was pretty easy to do long-term planning for what kinds of questions you want to ask people, what sorts of things to evaluate candidates on, and how much faith you can put in the results. But that has changed almost overnight, and it continues to change pretty rapidly. We no longer know what job roles to post, what questions to ask, nor how to evaluate candidates properly using any of our existing processes.


So. It ain’t working. And yet we’re still not talking about what it will take to change it. Because it’s unthinkable. It’s farting in church.


Let’s talk about what a real rescue would look like.


**Let’s Stop Simulating Work**


Every step of the interview process is an elaborate attempt to simulate actually working with someone. Reading their résumé, you close your eyes and imagine what it would have been like to get all those Ph.D.s. They must be insufferable. Moving on! Then there’s the phone screen, where you try not to imagine them wearing a gorilla suit, and usually fail. Then the interview, where you learn how they *actually* smell.


Whiteboards, made-up design questions–it’s all just theater, trying to act like it’s real work.


We’ve already established that **the gold standard of assessment is working directly with someone on real work,** in a real environment, for as long as needed to make the call.


So the short answer is, stop simulating. Post real pieces of work, let the candidate do it, look at what they actually produced, and decide from that work.


We never did this before for all sorts of reasons. It’s a lot of work to carve out work. Hard to get people the credentials they need, etc. Carving up work might be easier with AI now in some cases, but still pretty hard if you’re a locked down enterprise.


Another reason is that on the supply side, nobody wants to sign up to do a bunch of free work just to be rejected. If you just put up work, the candidates incur all the risk, meaning they walk away with nothing if you don’t hire them. You can pay them, which helps soften it, but they’re still looking for full-time work that you might not offer them in the end.


So until very recently, the idea of using real work as an assessment tool has encountered too much resistance on both sides of the interview table.


**Campfire Is The New Interview**


If you spend any time doomscrolling on X, the new meta in SF is “come work with us for a few days.” Paid, real codebase, real ticket, real team. From what I’ve heard, it generates the best signal people have ever seen, by a mile. I don’t think it beats a six-month co-op, but it’s a hell of a lot better than a standard interview loop.


So there’s already a movement away from traditional interviewing, which is why I feel comfortable making the claim that it’s already starting to die out on its own. It’s being replaced by bringing people in for longer stints. I’ve been calling this working model the[ campfire](https://steve-yegge.medium.com/the-anthropic-hive-mind-d01f768f3d7b): pull up a log, build something together, see how it feels. Bringing in outside contributors is pretty easy, as they’ll have agents and should be able to come up to speed very quickly. If they can’t, there’s your signal.


But even though people are experimenting with it, the way it’s done today is a mess. Every shop is reinventing a bespoke solution. And it’s unportable: candidates do brilliant work in a trial, they don’t get the offer for reasons, and the signal evaporates. The next company they campfire-interview at starts them at zero.


**Count Work Twice**


Big companies all have mountains of work. Heck, everyone has mountains of work. And most companies are engulfed in a forest fire of résumés. If you can carve real pieces off your work mountain, and connect them to that fire, you can make a campfire model that scales.


Great for you, you get outside help with your work mountain. But how can it be made fair for the candidates contributing work? Easy: You make the work count twice. Once for you: you get strong assessment signal, and some real output from candidates that you will often get to keep, or at least use as a starting point.


And then, importantly, each work item also counts once for the candidate: they walk away with a permanent, portable record of what they did and how well they did it, signed by you, whether or not you make an offer.


When candidates get to walk away with something of lasting value that they can keep forever, something that may even compound over time, it no longer feels like “six hours of free work to get rejected.” It feels like a six hour investment in a permanent small reputation bump. That’s *infinitely* better than a flat rejection.


**Make Interviewing A Profit Center**


Interviewing has always been a cost center. It costs engineer-hours to produce a yes or a no, which is why people have resisted increasing interviewing time to improve the signal. It’s already considered a lot. But if you run things campfire-style, it potentially flips into a profit center. And it can pay for itself twice: once in real work shipped, and once again in something else you could probably use more of, which is gravity.


Every stamp that you hand out, pass or fail, leaves a candidate richer than they showed up. This attracts strong candidates to you, because even your rejections are worth something to them. Stamp honestly and generously enough and you stop rooting around through a trickle of identical AI-polished résumés, and start standing up a reserve: people who’ve done real work with you, can prove it, and will pick up when you call.


But they can also walk away, and take their record with them.


This system is basically worth exactly what your honesty is worth. If you hand out gold stars to everyone, you’re just reinventing LinkedIn endorsements, which are worthless. Companies whose stamps mean anything will be the ones known for only handing them out for quality work. Being a hard, fair judge is an advantage for everyone.


**Where Do the Stamps Originate?**


Every rideshare platform already mints the kind of record we’re talking about here: star ratings, badges for this and that, rides completed, Grab and Uber have all of it. The one thing wrong with it is that it’s trapped on each platform and disappears if the driver leaves. The whole trick to reinventing talent assessment is letting the workers carry the assessments out the door.


I’m aware of some solutions evolving in this space, both commercial and open-source, and I’m excited to share more when I can. Candidly, I wanted to hand you a coherent solution today, and through a combination of running out of space, and Opus 4.8 being way too goddamn critical of everything all the time (jfc), I decided I’d hold it for now. We’ll all just have to start experimenting.


But now you have the shape of it. Please, treat any prescription I’ve made here as a sketch. Mostly I just want you to come around on the diagnosis, and agree that we need to fix it properly for the first time in 50 years. Maybe you conclude that everyone has to require six-month co-ops. I don’t care. As long as it’s not more of the same. I just wanted to move the Overton window a bit.


Personally, I think campfire is the most intellectually satisfying solution I’ve heard as a viable replacement for our aging interview infrastructure. Hope to see you at a campfire soon!


![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=bc13ddcf4564)
