---
title: "The business of big data audits: monetizing fairness"
date: 2014-05-23
url: https://mathbabe.org/2014/05/23/the-business-of-big-data-audits-monetizing-fairness/
word_count: 422
---


I gave a talk to the invitation-only [NYC CTO Club](https://www.linkedin.com/groups/New-York-CTO-Club-45712/about) a couple of weeks ago about my fears about big data modeling, namely:

- that big data modeling is discriminatory,
- that big data modeling increases inequality, and
- that big data modeling threatens democracy.


I had three things on my “to do” list for the audience of senior technologists, namely:

- test internal, proprietary models for discrimination,
- help regulators like the CFPB develop reasonable audits, and
- get behind certain models being transparent and publicly accessible, including credit scoring, teacher evaluations, and political messaging models.


Given the provocative nature of my talk, I was pleasantly surprised by the positive reception I was given. Those guys were great – interactive, talkative, and very thoughtful. I think it helped that I wasn’t trying to sell them something.


Even so, I shouldn’t have been surprised when one of them followed up with me to talk about a possible business model for “fairness audits.” The idea is that, what with [the recent bad press about discrimination in big data modeling](https://mathbabe.org/2014/05/07/inside-the-podesta-report-civil-rights-principles-of-big-data/) (some of the audience had actually worked with the Podesta team), there will likely be a business advantage to being able to claim that your models are fair. So someone should develop those tests that companies can take. Quick, someone, monetize fairness!


One reason I think this might actually work – and more importantly, be useful – is that I focused on “effects-based” discrimination, which is to say testing a model by treating it like a black box and seeing how it works on different inputs and gives different outputs. In other words, I want to give a resume-sorting algorithm different resumes with similar qualifications but different races. An algorithmically induced randomized experiment, if you will.


From the business perspective, a test that allows a model to remain a black box feels safe, because it does not require true transparency, and allows the “secret sauce” to remain secret.


One thing, though. I don’t think it makes too much sense to have a proprietary model for fairness auditing. In fact the way I was imagining this was to develop an open-source audit model that the CFPB could use. What I don’t want, and which would be worse than nothing, would be if some private company developed a proprietary “fairness audit” model that we cannot trust and would claim to solve the very real problems listed above.


Update: [something like this is already happening](http://www.cs.cmu.edu/~wing/publications/Sen-Wing14.pdf) for privacy compliance in the big data world (hat tip David Austin).
