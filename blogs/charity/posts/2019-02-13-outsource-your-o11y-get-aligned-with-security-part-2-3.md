---
title: "Outsource Your O11y: Get Aligned With Security (part 2/3)"
date: 2019-02-13
url: https://charity.wtf/2019/02/13/outsource-your-o11y-get-aligned-with-security-part-2-3/
word_count: 1905
---


*This is part two of a three-part series of guest posts:*

1. * [How To Be A Champion](https://charity.wtf/2019/02/13/5247/), on how to choose a third-party vendor and champion them successfully to your security team.  ([George Chamales](https://criticalsec.com))*
2. *[Get Aligned With Security](http://charity.wtf/2019/02/13/outsource-your-o11y-get-aligned-with-security-part-2-3/), how to work with your security team to find the best possible outcome for all sides ([Lilly Ryan](https://twitter.com/attacus_au))*
3. *[Now Roll It Out And Keep Them Happy](http://charity.wtf/2019/02/13/outsource-your-o11y-now-roll-it-out-and-keep-them-happy-part-3-3/), on how to operationalize your service by rolling out the integration and maintaining it — and the relationship with your security team — over the long run ([Andy Isaacson](https://twitter.com/eqe))*


*All this pain will someday be worth it.  🙏❤️  charity + friends*


---


## “Get Aligned With Security”


##### by Lilly Ryan


If your team has decided on a third-party service to help you gather data and debug product issues, how do you convince an often overeager internal security team to help you adopt it?


When this service is something that provides a pathway for developers to access production data, as analytics tools often do, making the case for access to that data can screech to a halt at the mention of the word “production”. Progressing past that point will take time, empathy, and consideration.


I have been on both sides of the “adopting a new service” fence: as a developer hoping to introduce something new and useful to our stack, and now as a security professional who spends her days trying to bust holes in other people’s setups. I understand both sides of the sometimes-conflicting needs to both ship software and to keep systems safe.


This guide has advice to help you solve the immediate problem of choosing and deploying a third-party service with the approval of your security team.  But it also has advice for how to strengthen the working relationship between your security and development teams over the longer term. No two companies are the same, so please adapt these ideas to fit your circumstances.


#### Understanding the security mindset


The biggest problems in technology are never really about technology, but about people. Seeing your security team as people and understanding where they are coming from will help you to establish empathy with them so that both of you want to help each other get what you want, not block each other.


First, understand where your security team is coming from. Development teams need to build features, improve the product, understand and ship good code. Security teams need to make sure you don’t end up on the cover of the NYT for data breaches, that your business isn’t halted by ransomware, and that you’re not building your product on a vulnerable stack.


This can be an unfamiliar frame of mind for developers.  Software development tends to attract positive-minded people who love creating things and are excited about the possibilities of new technology. Software security tends to attract negative thinkers who are skilled at finding all the flaws in a system.  These are very different mentalities, and the people who occupy them tend to have very different assumptions, vocabularies, and worldviews.


But if you and your security team can’t share the same worldview, it will be hard to trust each other and come to agreement.  This is where practicing empathy can be helpful.


Before approaching your security team with your request to approve a new vendor, you may want to run some practice exercises for putting yourselves in their shoes and forcing yourselves to deliberately cultivate a negative thinking mindset to experience how they may react — not just in terms of the objective risk to the business, or the compliance headaches it might cause, but also what arguments might resonate with them and what emotional reactions they might have.


My favourite exercise for getting teams to think negatively is what I call the *Land Astronaut* approach.


#### The “Land Astronaut” Game


Imagine you are an astronaut on the International Space Station. Literally everything you do in space has death as a highly possible outcome. So astronauts spend a lot of time analysing, re-enacting, and optimizing their reactions to events, until it becomes muscle memory. By expecting and training for failure, astronauts use negative thinking to anticipate and mitigate flaws before they happen. It makes their chances of survival greater and their people ready for any crisis.


Your project may not be as high-stakes as a space mission, and your feet will most likely remain on the ground for the duration of your work, but you can bet your security team is regularly indulging in worst-case astronaut-type thinking. You and your team should try it, too.


> The Game:
> Pick a service for you and your team to game out.  Schedule an hour, book a room with a whiteboard, put on your Land Astronaut helmets.  Then tell your team to spend half an hour brainstorming about all the terrible things that can happen to that service, or to the rest of your stack when that service is introduced.  Negative thoughts only!
> Start brainstorming together. Start out by being as outlandish as possible (what happens if their data centre is suddenly overrun by a stampede of elephants?). Eventually you will find that you’ll tire of the extreme worst case scenarios and come to consider more realistic outcomes — some of which which you may not have thought of outside of the structure of the activity.
> After half an hour, or whenever you feel like you’re all done brainstorming, take off your Land Astronaut helmets, sift out the most plausible of the worst case scenarios, and try to come up with answers or strategies that will help you counteract them.  Which risks are plausible enough that you should mitigate them?  Which are you prepared to gamble on never happening?  How will this risk calculus change as your company grows and takes on more exposure?


Doing this with your team will allow you all to practice the negative thinking mindset together and get a feel for how your colleagues in the security team might approach this request. (While this may seem similar to threat modelling exercises you might have done in the past, the focus here is on learning to adopt a security mindset and gaining empathy for this thought process, rather than running through a technical checklist of common areas of concern.)


While you still have your helmets within reach, use your negative thinking mindset to fill out the spreadsheet from the first piece in this series.  This will help you anticipate most of the reasonable objections security might raise, and may help you include useful detail the security team might not have known to ask for.


Once you have prepared your list of answers to George’s worksheet and held a team Land Astronaut session together, you will have come most of the way to getting on board with the way your security team thinks.


#### Preparing for compromise


You’ve considered your options carefully, you’ve learned how to harness negative thinking to your advantage, and you’re ready to talk to your colleagues in security – but sometimes, even with all of these tools at your disposal, you may not walk away with all of the things you are hoping for.


Being willing to compromise and anticipating some of those compromises before you approach the security team will help you negotiate more successfully.


While your Land Astronaut helmets are still within reach, consider using your negative thinking mindset game to identify areas where you may be asked to compromise. If you’re asking for production access to this new service for observability and debugging purposes, think about what kinds of objections may be raised about this and how you might counter them or accommodate them. Consider continuing the activity with half of the team remaining in the Land Astronaut role while the other half advocates from a positive thinking standpoint. This dynamic will get you having conversations about compromise early on, so that when the security team inevitably raises eyebrows, you are ready with answers.


Be prepared to consider compromises you had not anticipated, and enter into discussions with the security team with as open a mind as possible. Remember the team is balancing priorities of not only your team, but other business and development teams as well.  If you and your security colleagues are doing the hard work to meet each other halfway then you are more likely to arrive at a solution that satisfies both parties.


#### Working together for the long term


While the previous strategies we’ve covered focus on short-term outcomes, in this continuous-deployment, shift-left world we now live in, the best way to convince your security team of the benefits of a third-party service – or any other decision – is to have them along from day one, as part of the team.


Roles and teams are increasingly fluid and boundary-crossing, yet security remains one of the roles least likely to be considered for inclusion on a software development team. Even in 2019, the task of ensuring that your product and stack are secure and well-defended is often left until the end of the development cycle.  This contributes a great deal to the combative atmosphere that is common.


Bringing security people into the development process much earlier builds rapport and prevents these adversarial, territorial dynamics. Consider working together to build Disaster Recovery plans and coordinating for shared production ownership.


If your organisation isn’t ready for that kind of structural shift, there are other ways to work together more closely with your security colleagues.


Try having members of your team spend a week or two embedded with the security team. You may even consider a rolling exchange – a developer for a security team member – so that developers build the security mindset, and the security team is able to understand the problems your team is facing (and why you are looking at introducing this new service).


At the very least, you should make regular time to meet with the security team, get to know them as people, and avoid springing things on them late in the project when change is hardest.


#### Riding off together into the sunset…?


If you’ve taken the time to get to know your security team and how they think, you’ll hopefully be able to get what you want from them – or perhaps you’ll understand why their objections were valid, and come up with a better solution that works well for both of you.


Investing in a strong relationship between your development and security teams will rarely lead to the apocalypse. Instead, you’ll end up with a better product, probably some new work friends, and maybe an exciting idea for a boundary-crossing new career in tech.


But this story isn’t over! Once you get the green light from security, you’ll need to think about how to roll your new service out safely, maintain it, and consider its full lifespan within your company.  Which leads us to part three of this series, on rolling it out and maintaining it … both your integration and your relationship with the security team.


*[Lilly Ryan ](https://twitter.com/attacus)is a pen tester, Python wrangler, and recovering historian from Melbourne. She writes and speaks internationally about ethical software, social identities after death, teamwork, and the telegraph. More recently she has researched the domestic use of arsenic in Victorian England, attempted urban camouflage, reverse engineered APIs, wielded the Oxford comma, and baked a really good lemon shortbread.*
