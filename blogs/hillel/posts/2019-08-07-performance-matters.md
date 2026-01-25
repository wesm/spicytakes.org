---
title: "Performance Matters"
date: 2019-08-07
url: https://www.hillelwayne.com/post/performance-matters/
slug: performance-matters
word_count: 751
---

Last year I got certified as an EMT. As part of the training I shadowed an ambulance for a day and assisted with each run. For each patient we treated, we had to fill out a patient care report.


![Image of a patient care report](pcr.png)

*A patient care report.(source)*


EMTs are just one part in a long chain. If they transport a patient to a hospital, the hospital needs to know everything about the patient and everything that happened since the call. What’s the primary complaint? What are all the symptoms, and what was the history? What were their vital signs, and did their condition change in transit? If a patient has a resting heart rate of 50 beats per minute, that’s normal. But if it was 80 bpm twenty minutes ago… that’s a problem. This all goes in the patient care report, which informs how the hospital treat the patient.


Emergency Medicine is a stressful job, there are many things that go into the PCR, and people make mistakes. Plenty of PCRs have errors in them. An error might waste valuable time as nurses chase invisible problems or ignore obvious ones. Worst case, it leads to the wrong treatment. In emergency situations these mistakes can be fatal.


The chances are pretty low, and there are a lot of checks in place for this. But over 30,000,000 PCRs are filed in the US each year.1 At that scale, low chances kill people. Murdered by statistics.


At that scale, time and life are interchangeable. Every minute writing and filing a PCR is a minute not spent on actual treatment. If 0.1% of PCRs have mistakes that waste an hour of a doctor’s time, that’s 30,000 doctor-hours not spent on other patients. It’s a factor so grand and diffuse we can’t see it in motion. We can’t think in those terms.


We know this. Many ambulances now have electronic PCRs, which fix a lot of these problems. The report is automatically filed with the hospital. The software can enter timestamps and fill in necessary boilerplate. By spellchecking known medications it saves time at the hospital. Nobody has to guess whether you scrawled “100mg” or “160mg”.


The ambulance I shadowed had an ePCR. Nobody used it. I talked to the EMTs about this, and they said nobody they knew used it either. Lack of training? «No, we all got trained.» Crippling bugs? No, it worked fine. Paper was good enough? No, the ePCR was much better than paper PCRs in almost every way. It just had one problem: it was too slow.


It wasn’t even *that* slow. Something like a quarter-second lag when you opened a dropdown or clicked a button. But it made things so unpleasant that nobody wanted to touch it. Paper was slow and annoying and easy to screw up, but at least it wasn’t *that*.


I think about that a lot.


Did that quarter-second lag kill anyone? Was there someone who wouldn’t have died if the ePCR was just a little bit faster, fast enough to be usable? And the people who built it: did they ask the same questions? Did they say “premature optimization is bad” and not think about performance until it was too late? Did they decide another feature for the client was more important than making the existing features faster? Did they even think about performance at all?


Most of us aren’t writing critical software. But this isn’t “critical software”, either: nobody will suddenly die if it breaks. You just switch back to paper PCRs. But it *could have saved lives*. At scale, it could have saved people dying from PCR errors. It could have saved the person the EMTs couldn’t get to because they lose an hour a week from extra PCR overhead. *If* it was fast enough to use.


What else happens at scale? If my code is slow, can it hurt someone? Can a slow app cause a chain reaction that leads to someone missing their flight? Can a slow CSV library eventually cause a car accident? I don’t know. I want to think not, because I can’t wrap my mind around that kind of scale. I can’t think about that many inputs to the system, that many steps in the chain, that many people. There are too many other software problems to worry about.


Then again, maybe the ePCR programmers thought that too.


---

1. I’m using the [2011](https://www.ems.gov/pdf/research/Studies-and-Reports/National_EMS_Assessment_2011.pdf) national report and assuming that every patient contact leads to a PCR.
 [return]
