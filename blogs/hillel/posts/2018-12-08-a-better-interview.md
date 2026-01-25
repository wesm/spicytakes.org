---
title: "A Better Interview"
date: 2018-12-08
url: https://www.hillelwayne.com/post/a-better-interview/
slug: a-better-interview
word_count: 1194
---

**Caveats:** I’m not an interviewer, I’ve never done serious research on interviews, and I haven’t tested this. I propose this entirely as a thought experiment.


**Assumptions:** We interview at jobs to find ideal candidates. WE are looking for candidates who are

1. Good at programming
2. Good at software engineering
3. Can work in a team
4. A “culture fit” (not an asshole).


Technical interviews test the first two. They are primarily whiteboard questions, abstract design questions, or “write this program” questions. Candidates go through several technical interviews, and the interviewers all discuss the hire/not hire decision together.


**Problems:** Most technical interviews have several issues:

1. Large investment of interviewer time.
2. Stress: the interview process is very high stress and does not reflect how the programmer fares in more normal circumstances.1
3. Objectivity: Interviewers are basing things off some objective principles (if the candidate got the problem) and a lot of subjectivity (what was their “thought process”, how “lost” they got). This adds a lot of uncertainty to the rigour of any decisions.
4. Coarse grained: it’s difficult to extract more subtle details from the problem, such as how they think about large-scale optimization or correctness.
5. Bias: with subjective judgments, it’s extremely easy to bias the results in some way, for example by giving a “tough” interviewer to one person or judging the same personality traits differently in men and women.
6. Inaccurate: Whiteboard problems do not accurately reflect programming skill. Being able to write quicksort by heart does not show you know how to debug or optimize complex code.
7. False scope: Simple algorithms and toy problems do not reflect what someone will actually need to do for the job. Being able to design an elevator schema does not show you know how to understand and advance the actual problem domain you face.
8. Communication: A core part of software engineering is how the person works as part of a team, and this is not at all tested by most problems. Decisions with regard to this are entirely subjective.
9. Calibration: it’s difficult to track performance of a question over time, compare two candidates, or even see if a question is more difficult than you thought.


**Alternative:** Present candidate with an example codebase. Give them a day to study it, perhaps have them add a simple addition to see if they fully grok it. Then, present them with a pull request and ask them to write comments on it. They are only graded on their final comments, within reason.2


An additional twist would be to add personas to the PRs. For example, the candidate might be given two PRs, one from “a new junior programmer who’s unsure they belong here” and one from “a senior engineer who’s project lead.” The tone and content of their comments should reflect these personas.


**Advantages:** This addresses all of the problems with conventional interviews:

1. *Time.* Since the interview is unsupervised, the interviewers wouldn’t have to invest all of the face-to-face time required. They’d still need to spend time evaluating the comments, but they’d have to evaluate the interview anyway.
2. *Stress.* The candidate doesn’t have an interviewer breathing down their neck. If they want, they can write the comments while in a local park or something.
3. *Objectivity.* The comments can be checked against a rubric, such as “did the candidate point out the PR is lacking tests”, “did the candidate use hostile language”, or “did the candidate call out the logic bug in the modified `foobar` function”.
4. *Grain.* By changing the specific PR and the rubric, the question can be adapted to more specialized positions. For example, for a junior, the rubric can check that they’re asking “learning” questions, or that a DBA is thinking about large-scale performance.
5. *Bias.* The interview can be done double-blind, with the people grading the PR comments not knowing any details of the candidate they’re grading.
6. *Inaccuracy.* Reading code, discussing PRs, and evaluating changes to a system are all core parts of a programmer’s job.
7. *Scope.* The example codebase can be designed to represent the company’s problem domain. For example, a Wordpress clone could have the codebase be the comment moderation feature.
8. *Communication.* The question specifically tests the candidate’s ability to clearly, respectfully, and persuasively discuss issues with someone’s work.
9. *Calibration.* Since the candidate is only judged on the final artifact, we have a record of the PR, comments, rubric, and performance of the candidate. This can be used for data analysis and auditing.


**Weaknesses:**

- Initial time investment of setting up an example codebase and PR. This also has a higher standard on calibrating the question. This is probably the biggest issue I see.
- Requires the candidate the prep in advance. I know a lot of people find this problematic, as it demands additional investment time the candidate might not have.I don’t think there’s a way to fix this without also losing the benefits of this approach, so it’s might just be a necessary evil.
- This is not language agnostic, and requires both the designers and the candidate to be comfortable with the codebase language. This may not be a problem if you’re hiring for a specific language, since that will be found out earlier, but it could be an issue if one part of your rubric is “idiomaticness”, like using list comprehensions instead of maps in Python. Possible solution: use a fake pseudocode? Just leave out idiomatics from the rubric?
- Does not test the candidate’s ability to *write* code. Might have to be paired with a simple Fizzbuzz check over the phone. Alternatively, the interviewee is being asked to make a modification anyway. If the modification is nontrivial it could test codewriting capacity.
- Unsupervised means opportunities to cheat. Provide an audited machine to do this on?
- Codebases tend to have contexts, and a ‘bad practice’ might make sense in a given codebase. How do we capture this in the review?
- There might be a lot of information lost by not following up with the candidate to explain *why* they made certain comments. But the followup would compromise the rigour and objectivity of this approach. No good answers here.
- Tests communication but not “culture fit”. Still need to do a short followup for that.


**Misc:** I really like the “profiles” idea in particular. Feel like there’s a way to combine this with an interviewer oracle to turn this into a full on roleplaying sessions.


*Thanks to [Colin Bull](https://twitter.com/colinbul) and Andrea Magnorsky for feedback.*


---

1. A common argument is that it tests the programmer’s ability to think on their feet. Even in stressful production cases, however, the stress is a different *type* than interview stress. Seeing how a candidate performs under interview stress does not tell you how they perform under “someone deleted the production database” stress.
 [return]
2. By “within reason”, I mean like if they read the PR and say “wow this is garbage” to themselves, that’s fine if they don’t asshole up the PR comments. If they say “wow this is garbage HITLER WAS RIGHT” then that’s a red flag.
 [return]
