---
title: "Questionable Advice: Can Engineering Productivity Be Measured?"
date: 2020-07-07
url: https://charity.wtf/2020/07/07/questionable-advice-can-engineering-productivity-be-measured/
word_count: 1039
---


> I follow you on Twitter and read your blog.  I particularly enjoy this post: [https://charity.wtf/2019/05/01/friday-deploy-freezes-are-exactly-like-murdering-puppies](https://charity.wtf/2019/05/01/friday-deploy-freezes-are-exactly-like-murdering-puppies)/ I’m reaching out looking for some guidance.
> I work as an engineering manager for a company whose non-technology leadership insists there has to be a way to measure the individual productivity of a software engineer. I have the opposite belief. I don’t believe you can measure the productivity of “professional” careers, or thought workers (ex: how do measure productivity of a doctor, lawyer, or chemist?).
> For software engineering in particular, I feel that metrics can be gamed, don’t tell the whole story, or in some cases, are completely arbitrary. Do you measure individual developer productivity? If so, what do you measure, and why do you feel it’s valuable? If you don’t and share similar feelings as mine, how would you recommend I justify that position to non-technology leadership?
> Thanks for your time.
> Anonymous Engineering Manager


Dear Anon,


Once upon a time I had a job as a sysadmin, 100% remote, where all work was tracked using RT tasks. I soon realized that the owner didn’t have a lot of independent technical judgment, and his main barometer for the caliber of our contributions was the number of tasks we closed each day.


I became a ticket-closing *machine*. I’d snap up the quick and easy tasks within seconds. I’d pattern match and close in bulk when I found a solution for a group of tasks. I dove deep into the list of stale tickets looking for ones I could close as “did not respond” or “waiting for response”, especially once I realized there was no penalty for closing the same ticket over and over.


My boss worshiped me. I was bored *as fuck*. Sigh.


I guess what I’m trying to say is, I am fully in your camp. I don’t think you can measure the “productivity” of a creative professional by assigning metrics to their behaviors or process markers, and I think that attempting to derive or inflict such metrics can inflict a lot of damage.


In fact, I would say that to the extent you can reduce a job to a set of metrics, that job can be automated away. Metrics are for easy problems — discrete, self-contained, well-understood problems. The more challenging and novel a problem, the less reliable these metrics will be.


Your execs should fucking well know this: how would THEY like to be evaluated based on, like, how many emails they send in a day? Do they believe that would be good for the business? Or would they object that they are tasked with the holistic success of the org, and that their roles are too complex to reduce to a set of metrics without context?


This actually makes my blood boil. It is condescending as fuck for leadership to treat engineers like task-crunching interchangeable cogs. It reveals a deep misunderstanding of how sociotechnical systems are developed and sustained (plus authoritarian tendencies, and usually a big dollop of personal insecurity).


But what is the alternative?


In my experience, the “right” answer, i.e. the best way to run consistently high-performing teams, involves some combination of the following:

- Outcome-based management that practices focusing on impact, plus
- Team level health metrics, combined with
- Engineering ladder and regular lightweight reviews, and
- Managers who are well calibrated across the org, and encouraged to interrogate their own biases openly & with curiosity.


The right way to look at performance is at the team level. Individual engineers don’t own or maintain code; teams do. **The team is the irreducible unit of ownership**. So you need to incentivize people to think about work and spending their time cooperatively, optimizing for what is best for the team.


Some of the hardest and most impactful engineering work will be all but invisible on any set of individual metrics. You want people to trust that their manager will have their backs and value their contributions appropriately at review time, if they simply act in the team’s best interest. You do not want them to waste time gaming the metrics or courting personal political favor.


This is one of the reasons that managers need to be technical — so they can cultivate their own independent judgment, instead of basing reviews on hearsay. Because some resources (i.e. your budget for individual bonuses) are unfortunately zero-sum, and you are always going to rely on the good judgment of your engineering leaders when it comes to evaluating the relative impact of individual contributions.


> “I would say that Joe’s contribution this quarter had greater impact than Jane’s. But is that really true? Jane did a LOT of mentoring and other “glue” work, which tends to be under-acknowledged as leadership work, so I just want to make sure I am evaluating this fairly … Does anyone else have a perspective on this? What might I be missing?” — a manager keeping themselves honest in calibrations


I do think every team should be tracking the 4 [DORA](https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling) metrics — time elapsed between merge and deploy, frequency of deploy, time to recover from outages, duration of outages — as well as how often someone is paged outside of business hours. These track pretty closely to engineering productivity and efficiency.


But leadership should do its best to be outcome oriented. The harder the problem, the more senior the contributor, the less business anyone has dictating the details of how or why. Make your agreements, then focus on impact.


This is harder on managers, for sure — it’s easier to count the hours someone spends at their desk or how many lines of code they commit than to develop a nuanced understanding of the quality and timbre of an engineer’s contributions to the product, team and the company over time. It is easier to micromanage the details than to negotiate a mutual understanding of what actually matters, commit to doing your part … and then step away, trusting them to fill in the gaps.


But we should expect this; it’s worth it. It is in those gaps where we feel trusted to act that we find joy and autonomy in our labor, where we do our best work as skilled artisans.


![](https://i0.wp.com/charity.wtf/wp-content/uploads/2020/09/selfie-7.jpg?resize=219%2C292&ssl=1)
