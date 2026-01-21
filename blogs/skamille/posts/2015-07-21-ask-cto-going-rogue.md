---
title: "Ask the CTO: Going Rogue"
date: 2015-07-21
url: https://www.elidedbranches.com/2015/07/ask-cto-going-rogue.html
word_count: 882
---

*I often get asked one-off questions about engineering leadership and management, and thought it would be fun to share my answers here. Asker's question has been anonymized and generalized.*
**The challenge:**
I have an employee that was supposed to be adding a needed feature to one of our core systems. A few days ago I notice in GitHub that he has created a new repo and been working solely in that repo for the past two weeks. Instead of adding a feature to the new system, he is completely rewriting it! Furthermore, the repo is in a new language that no one in the team uses and that we have never put into production. I feel bad, I should have noticed this before it got this far, but I never expected someone we consider to be a senior engineer to go off and do this without at least checking in. How should I address this?
**My thoughts:**
Oof. This has happened to most of us at least once, in some fashion. Engineers want to be able to use what they think is the right tool for the job, even when the right tool is brand-new to the company. And generally speaking, this should be OK! The last thing you want to do is stifle people's initiative to create solid solutions and learn new things.
That being said, there is a high overhead to adding new things to your stack, and at some point, it usually makes sense to have some policy around how to add new things. I whipped together such a policy for my team about a year ago, when we had reached around 40 on the team and there were some folks discussing creating a new service in a language that we had very limited experience with. Our policy looks something like this:

> Before any new language/framework is chosen for a production system, the following needs to be in place and approved by Camille and an architecture review board (*group of senior engineers who are knowledgable in the area of change and would be impacted by it*)


> the engineers advocating for the language/framework will present a case as to the benefits it will provide over existing choices
> there is a plan for what sorts of systems this language/framework should be used to implement, and what existing systems could be rewritten in it
> a style guide and templates for readability, testing, continuous integration, monitoring, logging, deployment and production standards will have been created
> at least four engineers on the team must sign up on learning how to write readable, production quality code and support the new systems in production


> This must be done before the start of any project for engineering to commit to supporting the resultant code.

This is a bit of a heavyweight list, but it articulates some of the challenges with bringing new languages and frameworks into teams. If you are in a team that wants to be conservative with new languages, frameworks and tools, clearly articulating the process for adding new things is an important element to avoid unexpected surprises on both sides of the equation.
So, you can put such a policy in place and point to it in the future to try and prevent such things from happening, but it has happened now, and there is an argument to be made that part of being a senior engineer is knowing when to communicate scope changes such as the need to move to new languages or frameworks.
*Even if you don't agree with my conservative approach to adding new things,*
you probably appreciate it when you get a heads-up on important changes early in the process.
The conversation you have now should involve first understanding their perspective: Why the new language? Why didn't they grab you earlier to tell you about it? What you learn from their perspective might surprise you. Perhaps you skip all of their 1-1s and they think you are unapproachable. Perhaps they are frustrated with the way you make decisions. Perhaps they knew you would be mad and were simply afraid to show you new work early when you would shoot it down.
Once you have gotten their perspective (and perhaps some takeaways for you), now it is time to clarify your perspective and expectations of them. As a senior engineer, you need them to push information to you. You expect them to communicate the scope of changes and approximate timelines, and let you know when these things change. They need to think about their peers, and have empathy for the needs of the team as well as their own interests; all too often teams will reject projects they weren't aware of and didn't have any say in. Socializing change not only to your manager but to your team is part of the role of the senior engineer.
So, to sum it up:
If you care about having a somewhat conservative process for new languages/frameworks, clarify what that process is and share it with your team
When someone ignores the process or otherwise surprises you, first ask why and try to understand their perspective
Finally, clarify your expectations to them, helping them understand the impact that their actions have on others and the importance of communcation