---
title: "Black box auditing is fine"
date: 2024-02-15
url: https://mathbabe.org/2024/02/15/black-box-auditing-is-fine/
word_count: 596
---


Last week I read [this paper](https://arxiv.org/abs/2401.14446) entitled “Black-Box Access is Insufficient for Rigorous AI Audits” with some excitement, since I do black box algorithmic auditing [at my company](https://orcaarisk.com/) and I was looking forward to knowing what more I could do with even more access. Also, it was written by a bunch of smart people from MIT, Harvard, Northeastern, Stanford, and so on.


But I’m not very impressed! Actually I think this paper is a weird result of what happens when academics write about stuff that mostly happens outside of academia. In particular, and I’ll skip a lot of things, I want to focus on their section entitled “Limitations of Black Box Audits,” because of the five bullet points they include, they are all wrong. I’ll just go through them one by one:


**1. Black-box methods are not well suited to develop a generalizable understanding.**


Their argument here is that you don’t understand weird inputs that could lead to strange behavior. They argue it causes the black box auditor to rely on heuristics. But that’s not at all true! When I audit algorithms, either with private companies who provide the data, or follow my instructions, or with regulators or enforcement agencies that insist on the data from the companies deploying algorithms, we always use all of the historical data that we can get our hands on. In other words, we do not rely on heuristics or synthetic inputs, we instead see how actual people were actually treated by these systems. This is a much more thorough black box audit, and it doesn’t require “understanding,” which I think is a misleading and unattainable goal; even the coders don’t really “understand” algorithms (just ask them).


**2. Black-box access prevents system components from being studied separately.**


Yes, that’s true! And no, that’s not a flaw! Audits are not supposed to identify where things go wrong, they are supposed to decide whether something is going wrong. From the perspective of an auditor, if certain stakeholder groups (say, [black patients in the case of Optum](https://www.healthcarefinancenews.com/news/study-finds-racial-bias-optum-algorithm)) are being treated badly, then that’s the point of the audit. The question of what exactly went wrong and when is the problem of the folks who set out to fix the problem, but they are not auditors.


**3. Black-box evaluations can produce misleading results. **


The example they give here is that an algorithm can pass statistical tests of non-discrimination but still have underlying flaws in reasoning. But I’d argue, as an auditor, we don’t actually care what the underlying reasoning looks like as long as it *consistently* passes the discrimination tests! Of course, it’s likely that there should be a battery of tests rather than just one. I’m happy to talk endlessly about how to design such a battery.


**4. Black-box explanation methods are often unreliable.**


Yes, true, but that’s because explanations of algorithms are almost always nonsense. I’d suggest you stop trying to understand “how an algorithm thinks” and start testing whether an algorithm is causing meaningful harm to stakeholders.


**5. Black-box evaluations offer limited insights to help address failures.**


True, but again, not a problem! If you want to be an engineer paid to fix problems, don’t call yourself an auditor. Indeed there would be a conflict of interest if that were the same job, because you’d be incentivized to find problems to fix, or to only find fixable problems, etcetera.


If one of the authors of this paper wants to discuss this with me, I’d be more than happy to. We could even have a public conversation, since I live in Cambridge!
