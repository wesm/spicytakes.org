---
title: "Sex, Lies, and Software Development"
date: 2009-04-08
url: https://blog.codinghorror.com/sex-lies-and-software-development/
slug: sex-lies-and-software-development
word_count: 1438
---

Are there any programming jobs you wouldn’t take? Not because the jobs didn’t pay enough, had poor benefits, or limited upside – but because the work itself made you uncomfortable? Consider the tale of [one freshmeat.net writer](https://web.archive.org/web/20090412130129/http://freshmeat.net/articles/excessive-code-and-excessive-nudity-what-gives):


> Back in the old days (let’s say 1996), I was just another Perl coder writing CGI scripts for a living. Well, pocket money’s more like it, but okay. I wrote scripts for fun, I wrote them to make some cash, and I wrote them because I’m a geek and I love programming. Then, one day, I got a phone call from this company. A friend of mine had referred them to me, and they wanted me to write a CGI script. The gentleman I spoke with was very well mannered, very well educated – the typical likeable manager.
> After some talking, he came to the point. The CGI script I was to create was supposed to take an archive of images and make them searchable by topic. In itself nothing amazing, but when I asked, out of curiosity, what kind of images we were talking about, I was surprised to find out it was porn. Yes, **porn**.
> I accepted the job, and life changed dramatically. Instead of friends saying “cool” or some coders I knew saying “nice script,” they shied away, refused to talk to me, refused to look at the script. For a long time, I wondered why. This year, I went to a convention. I was just out there looking for new cool stuff, not much else. Everyone I talked to was friendly, and downright nice, right up until the point when I told them what I did for a living. Then they suddenly remembered they had something better to do.
> And why? Does working on the adult part of the net mean I’m a scumbag? Does it mean I’m sleazy? Does it mean I’m untrustworthy? Does it mean my code is bad?


That was eight years ago. I wonder how the now over-thirty author of the original article is getting on in his career. **Does he still write code for the adult industry?** Somehow, I doubt it.


This isn’t just random noodling on my part. I’ve almost been in the same situation. About ten years ago, I had an interview for a programming position with a prominent North Carolina based purveyor of adult products. After the interview, I asked my girlfriend (now my wife) how she would feel if I took a job that was, more or less, in the adult industry. Although she’s flexible on almost every topic, this is one area where she had serious reservations. I think the operative words were “what will we tell our parents?” It’s a fair question. For that matter, what do you tell your friends when they ask where you work? Your peers? It was enough to keep me from taking the job.


Years later, I encountered one of my previous coworkers who *had* taken a programming job there. It turns out I made the right choice, but not for the reasons you might think. There were technical and managerial problems on the job that far outstripped any effects from the unusual choice of industry. That said, when I asked him what the environment was like, working daily with adult products, he had a one word response: *weird*.


The adult industry does present interesting technical and scaling challenges, perhaps more interesting than building yet another line of business [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) application for Yet Another MegaCorp. A recent Reddit discussion thread which asked [if you designed a porn site, would you put it on your resume?](http://www.reddit.com/r/programming/comments/844pj/if_you_designed_a_porn_site_would_you_put_it_on/) had some excellent examples.


> [Adult] sites have oodles of top-quality attributes to them; payment processing, secured content, username and password maintenance (especially self-service maintenance) rapid updates and, if your site was successful, some interesting scaling problems to engineer around.
> I work for an [adult] site. It’s going on my resume. Anybody I’ve told in a professional or semi-professional setting has been impressed and wanted to know the technical details about our server setup and bandwidth. I have yet to meet anybody, friend or prospective employer who was turned off by the thought of my serving up [adult content]. And I’m willing to say that I wouldn’t work for someone who would judge me negatively because of it. I got into it because of the interesting scaling problems and potential for wisdom-of-crowds filtering and selection. And you know what, it’s kinda fun.
> I’ve worked in the [adult] industry for over 8 years. If I were to apply for a new job, you bet I would include it on my resume. I don’t think I’d want to work for a company that couldn’t see the benefit of having someone onboard that’s worked with systems that must always work, have a known cost-per-minute of downtime, and are on a permanently continuous release cycle.


The general tone of the advice is that, if you choose to work in the adult industry, **you have to tell white lies about your work** – small evasions about what your work is, and who it is for, depending on the audience. Invoke vague NDAs. Describe things in broad, general terms.


What if you saw this programming job listing:

- Work from home on a large, high-traffic website with lots of challenging scaling problems.
- Use the latest frameworks and technologies.
- Set your own hours.
- Excellent pay through wire transfer from an offshore account, with full benefits.


(I am not making any of this up, I’m actually summarizing a real job listing.) Seems like a *fantastic* programming job, right? But what if I told you this job listing was for an **adult website?** Would you still consider it?


I bring this up because I recently read a great in the trenches story about [continuous deployment](http://timothyfitz.wordpress.com/2009/02/10/continuous-deployment-at-imvu-doing-the-impossible-fifty-times-a-day/).


> Our tests suite takes nine minutes to run (distributed across 30-40 machines). Our code pushes take another six minutes. Since these two steps are pipelined that means at peak we’re pushing a new revision of the code to the website every nine minutes. That’s 6 deploys an hour. Even at that pace we’re often batching multiple commits into a single test/push cycle. On average we deploy new code fifty times a day.


My enthusiasm for this supreme feat of software engineering was tempered by the fact that, when I clicked through to find out more about the company that was doing such sophisticated software engineering, I learned that it’s a 3D chat avatar system. A very... *sexy*... 3D chat avatar system. Just look at their ads to see what I mean:


![](https://blog.codinghorror.com/content/images/2025/04/image-346.png)


What is being sold here? I’ve even seen similar “sexy” IMVU ads with female 3D avatars in skimpy lingerie come up organically on my [Fake Plastic Rock](https://web.archive.org/web/20090415213817/http://www.fakeplasticrock.com/) blog, of all places. I’m not the first person to [make this connection](http://www.shamusyoung.com/twentysidedtale/?p=955), either.


> A reader expressed their irritation with the IMVU ads that have been running in the sidebar recently. I was actually glad to see I wasn’t the only one. They have a trashy, lowest-common-denominator feel to them. Kind of a “Welcome to Hoochie World” vibe. The ad has been running for over a month, and I’ve never seen a picture of a single male avatar. It’s either the quasi-jailbait in a bikini, or a couple of skanks in a pseudosapphic embrace. Using a pretty girl to sell your stuff is perfectly reasonable, but doing it with such a lack of class gets on my nerves. I’ve never used the software, but the ads make me think their chat software is a world inhabited by l337-speaking teenage boys that would make the average FARK thread sound like the Mclaughlin Group by comparison.


The [profile for IMVU user “hottiepie4life”](http://avatars.imvu.com/hottiepie4life) makes it abundantly clear that IMVU, while not *quite* part of the adult industry per se, skirts awfully close to the edge of it. Enough to make me, personally, uncomfortable about working there, or talking to anyone who worked there. And it certainly colors and devalues my impression of the technical work going on there.


Maybe this is my problem. Does the subject matter dilute the excellent technical work the IMVU team might be doing? No. But at the same time, **I can’t help questioning the ultimate value of that work.** I’m no prude. And I don’t expect every programmer to be doing noble, selfless work for the good of humanity. All the same, it’s difficult for me to respect software engineering in the service of such least common denominator interests.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[cgi scripting](https://blog.codinghorror.com/tag/cgi-scripting/)
[perl](https://blog.codinghorror.com/tag/perl/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
