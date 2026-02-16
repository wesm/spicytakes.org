---
title: "Outsource Your O11y: Now Roll It Out And Keep Them Happy (part 3/3)"
date: 2019-02-13
url: https://charity.wtf/2019/02/13/outsource-your-o11y-now-roll-it-out-and-keep-them-happy-part-3-3/
word_count: 1335
---


*This is part three of a three-part series of guest posts:*

1. * [How To Be A Champion](https://charity.wtf/2019/02/13/5247/), on how to choose a third-party vendor and champion them successfully to your security team.  ([George Chamales](https://criticalsec.com))*
2. *[Get Aligned With Security](https://charity.wtf/2019/02/13/outsource-your-o11y-get-aligned-with-security-part-2-3/), how to work with your security team to find the best possible outcome for all sides ([Lilly Ryan](https://twitter.com/attacus_au))*
3. *[Now Roll It Out And Keep Them Happy](http://charity.wtf/2019/02/13/outsource-your-o11y-now-roll-it-out-and-keep-them-happy-part-3-3/), on how to operationalize your service by rolling out the integration and maintaining it — and the relationship with your security team — over the long run ([Andy Isaacson](https://twitter.com/eqe))*


*All this pain will someday be worth it.  🙏❤️  charity + friends*


---


## “Now Roll It Out And Keep Them Happy”


This is the third in a series of blog posts; previously we [analyzed the security challenges of using a third party service](https://charity.wtf/2019/02/13/5247/), and we [worked together with the security team to build empathy](https://charity.wtf/2019/02/13/outsource-your-o11y-get-aligned-with-security-part-2-3/)[ to deliver the project](https://charity.wtf/2019/02/13/outsource-your-o11y-get-aligned-with-security-part-2-3/).  You might want to read those first, since we are going to build on a lot of the ideas there to ship and maintain this integration.


#### Ready for launch


You’ve convinced the security team and other stakeholders, you’ve gotten the integration running, you’re getting promising results from dev-test or staging environments… now it’s time to move from proof-of-concept to full implementation.  Depending on your situation this might be a transition from staging to production, or it might mean increasing a feature flipper flag from 5% to 100%, or it might mean increasing coverage of an integration from one API endpoint to cover your entire developer footprint.


Taking into account Murphy’s Law, we expect that some things will go wrong during the rollout.  Perhaps during coverage, a developer realizes that the schema designed to handle the app’s event mechanism can’t represent a scenario, requiring a redesign or a hacky solution.  Or perhaps the metrics dashboard shows elevated error rates from the API frontend, and while there’s no smoking gun, the ops oncall decides to rollback the integration Just In Case it’s causing the incident.


This gives us another chance to practice empathy — while it’s easy, wearing the champion hat, to dismiss any issues found by looking for someone to blame, ultimately this poisons trust within your organization and will hamper success.  It’s more effective, in the long run (and often even in the short run), to find common ground with your peers in other disciplines and teams, and work through to solutions that satisfy everybody.


#### Keeping the lights on


In all likelihood as integration succeeds, the team will rapidly develop experts and expertise, as well as idiomatic ways to use the product.  Let the experts surprise you; folks you might not expect can step up when given a chance.  Expertise flourishes when given guidance and goals; as the team becomes comfortable with the integration, explicitly recognize a leader or point person for each vendor relationship.  Having one person explicitly responsible for a relationship lets them pay attention to those vendor emails, updates, and avoid the tragedy of the “but I thought *you* were” commons.  This Integration Lead is also a center of knowledge transfer for your organization — they won’t know everything or help every user come up to speed, but they can help empower the local power users in each team to ramp up their teams on the integration.


As comfort grows you will start to consider ways to change your usage, for example growing into new kinds of data.  This is a good time to revisit that security checklist — does the change increase PII exposure to your vendor?  Would the new data lead to additional requirements such as per-field encryption?  Don’t let these security concerns block you from gaining valuable insight using the new tool, but do take the chance to talk it over with your security experts as appropriate.


Throughout this organic growth, the Integration Lead remains core to managing your changing profile of usage of the vendor they shepherd; as new categories of data are added to the integration, the Lead has responsibility to ensure that the vendor relationship and risk profile are well matched to the needs that the new usage (and presumably, business value) is placing on the relationship.


Documenting the Intergation Lead role and responsibilities is critical. The team should know when to check in, and writing it down helps it happen.  When new code has a security implication, or a new use case potentially amplifies the cost of an integration, bringing the domain expert in will avoid unhappy surprises.  Knowing how to find out who to bring in, and when to bring them in, will keep your team getting the right eyes on their changes.


Security threats and other challenges change over time, too.  Collaborating with your security team so that they know what systems are in use helps your team take note of new information that is relevant to your business. A simple example is noting when your vendors publish a breach announcement, but more complex examples happen too — your vendor transitions cloud providers from AWS to Azure and the security team gets an alert about unexpected data flows from your production cluster; with transparency and trust such events become part of a routine process rather than an emergency.


#### It’s all operational


Monitoring and alerting is a fact of operations life, and this has to include vendor integrations (even when the vendor integration is a monitoring product.)  All of your operations best practices are needed here — keep your alerts clean and actionable so that you don’t develop pager fatigue, and monitor performance of the integration so that you don’t get blindsided by a creeping latency monster in your APIs.


Authentication and authorization are changing as the threat landscape evolves and industry moves from SMS verification codes to U2F/WebAuthn.  Does your vendor support your SSO integration?  If they can’t support the same SSO that you use everywhere else and can’t add it — or worse, look confused when you mention SSO — that’s probably a sign you should consider a different vendor.


#### A beautiful sunset


Have a plan beforehand for what needs to be done should you stop using the service.  Got any mobile apps that depend on APIs that will go away or start returning permission errors?  Be sure to test these scenarios ahead of time.


What happens at contract termination to data stored on the service?  Do you need to explicitly delete data when ceasing use?


Do you need to remove integrations from your systems before ending the commercial relationship, or can the technical shutdown and business shutdown run in parallel?


In all likelihood these are contingency plans that will never be needed, and they don’t need to be fully fleshed out to start, but a little bit of forethought can avoid unpleasant surprises.


#### Year after year


Industry best practice and common sense dictate that you should revisit the security questionnaire annually (if not more frequently). Use this chance to take stock of the last year and check in — are you getting value from the service?  What has changed in your business needs and the competitive landscape?


It’s entirely possible that a new year brings new challenges, which could make your current vendor even more valuable (time to negotiate a better contract rate!) or could mean you’d do better with a competing service.  Has the vendor gone through any major changes?  They might have new offerings that suit your needs well, or they may have pivoted away from the features you need.


Check in with your friends on the security team as well; standards evolve, and last year’s sufficient solution might not be good enough for new requirements.


*[Andy](https://twitter.com/eqe) thinks out loud about security, society, and the problems with computers on [Twitter](https://twitter.com/eqe).*


---


❤️ Thanks so much reading, folks.  Please feel free to drop any complaints, comments, or additional tips to us in the comments, or direct them to me on [twitter](http://twitter.com/mipsytipsy).


Have fun!  Stay (a little bit) Paranoid!!


— charity
