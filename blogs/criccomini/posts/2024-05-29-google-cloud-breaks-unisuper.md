---
title: "Google Cloud Breaks UniSuper and Is Kind of Sorry"
subtitle: "Google Cloud still doesn't understand its enterprise customers."
date: 2024-05-29T19:48:44+00:00
url: https://materializedview.io/p/google-cloud-breaks-unisuper
slug: google-cloud-breaks-unisuper
word_count: 1260
---


Welcome! There are quite a few new subscribers since I postedS3 Is Showing Its Agelast week. I normally do three different kinds of posts: roundups, interviews, and editorials. This week, I’m doing an editorial on Google’s recent UniSuper outage.Click hereto read some of my other popular posts.


---


I am a bigGoogle Cloudfan. We ran Google Cloud atWePay, my previous employer. I just got through praisingGoogle Cloud StorageinS3 Is Showing Its Age. So it pains me to write this post. But it’s important to talk about a company’s failures as well as their successes. Google Cloud’s response to its recent outage definitely falls into the “failure” category. I see a few problems:

1. Google still hasn’t figured out enterprise customers
2. Google’s incident remediation appears cursory
3. Google Cloud is gaining a reputation for instability


Before we get to the problems, let’s review what happened. Theoutage I’m referring toimpactedUniSuper, an Australian superannuation (retirement) fund. UniSuper’scustomer portal(and related user services) went offline forover a weekwhen Google accidentally deleted one of UniSuper’s private clouds. Actual trading was not impacted. The issue was caused by a—you guessed it—rather mundane misconfiguration.


> Google operators followed internal control protocols. However, one input parameter was left blank when using an internal tool to provision the customer’s Private Cloud. As a result of the blank parameter, the system assigned a then unknown default fixed 1 year term value for this parameter.After the end of the system-assigned 1 year period, the customer’sGCVEPrivate Cloud was deleted. No customer notification was sent because the deletion was triggered as a result of a parameter being left blank by Google operators using the internal tool, and not due a customer deletion request. Any customer-initiated deletion would have been preceded by a notification to the customer.


BothGoogleandUniSuperhave posted incident summaries with more detail.


## Understanding Enterprise Customers


What caught my eye was not the incident, but Google’s response. The tone of theirincident write-upis bad. The entire post reads as though Google feels thenegative press they receivedwas unfair. Google repeatedly highlights that the issue impacted a single customer in a single region, that the issue was unprecedented, and that the issue impacted only of UniSuper’s manyGoogle Cloud VMware Engine(GCVE) instances.


Nowhere does Google’s post even apologize. In fact, the only apology I can find is onUniSuper’s website. Instead, Google’s incident write-up ends with a claim that Google Cloud is one of, “the most resilient and stable cloud infrastructure in the world.” They conclude with a link to an “independently validated” report attesting to their stability. While this may be true, I find it completely tone-deaf. So much for customer empathy.


This response is, to me, yet another indication that Google still doesn’t understand its enterprise customer’s needs. Enterprises expect more than a terse single-page remediation with no apology. Enterprises also expect deletions to be staged before hard-deleting anything.


Unsurprisingly, Google has earned a dubious entry on UniSuper’soutage FAQ:


> Will we stay with Google Cloud moving forward?UniSuper has and always will take our responsibility to deliver secure, reliable services to our members extremely seriously. Google Cloud is not the only cloud service provider UniSuper utilises, and this planning has ensured our ability to restore services and minimise data loss.While a full root cause analysis is ongoing, Google Cloud has confirmed this is an isolated one-of-a-kind issue that has not previously arisen elsewhere.We will assess this incident and ensure we are best positioned to deliver services for our members.


This is not a strong statement of commitment from UniSuper, and I don’t blame them. It’s also an example of a well-worded enterprise-quality statement; something Google could learn from.


We loved Google Cloud at WePay, but I often got indications that Google didn’t understand its enterprise customers. Google ran their cloud product the way it ran its other software. Many security features were missing at the time. And when we spoke to product managers, we would often get a lesson on how Google did things, rather than listening to our needs.


I recall debugging a production issue with a site reliability engineer (SRE) sitting next to me. We both had the Google Cloud console up, and I asked the SRE to press a button for me on his console. Upon loading the page, we discovered his console didn’t have the button I had—one of us was in an A/B test that the other wasn’t. You don’t want to A/B test user interfaces in an organization when they’re in the middle of a production outage.


About this time,Diane Greenewas brought in fromVMwareto run Google Cloud. We were told she “understood enterprise” and that these issues would be addressed. During (and after) Greene’s tenure, Google Cloud’s security offering did improve. But she left Google Cloud in 2019. I can’t comment on Google Cloud’s enterprise maturity over the last few years, but Google’s UniSuper incident response doesn’t leave me feeling good.


## Weak Remediation


Google also seems to have done only a superficial level of remediation on the issue. Normally, when an incident like this occurs, you would expect a fairly exhaustive set of actions taken that spanned multiple teams and products.Chapter 10of Google’s own SRE book states:


> Rather than only investigating the proximate area of the system failure, the postmortem explores the impact and system flaws across multiple teams.


Google’s remediation summary lists only three steps:


> We deprecated the internal tool that triggered this sequence of events. This aspect is now fully automated and controlled by customers via the user interface, even when specific capacity management is required.We scrubbed the system database and manually reviewed all GCVE Private Clouds to ensure that no other GCVE deployments are at risk.We corrected the system behavior that sets GCVE Private Clouds for deletion for such deployment workflows.


This feels very proximate to me. They’ve simply automated the exact deletion flow that led to the outage, made sure that no other private clouds were misconfigured, and “corrected system behavior” for the deletion workflow.


Google could have audited their other deletion flows, their other tools, and their other products. They could have modified deletion workflows to stage deletions. Instead, they did none of this. Why?


I’m not alone in this;Hacker News’s top commenton the subject is all about Google’s weak remediation. Separately, an engineer I was having coffee with today expressed the same sentiment: shock at the lack of depth in Google’s remediation.


Google’s remediation indicates that they don’t understand how damaging this outage was to their brand.


## Brand Damage


I have always thought of Google Cloud as stable. We certainly had stability issues with Google Cloud at WePay, but it was fairly run-of-the-mill stuff. So I was surprised to see that many users (with extensive multi-cloud experience) regard Google Cloud as less stable.


![](https://substackcdn.com/image/fetch/$s_!sDvz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2f63c14-a67e-48a2-9f12-e1602b38305f_693x555.png)

*View Post*


This is a dangerous sentiment for Google. If Google Cloud is regarded as less stable, enterprises aren’t going to use it. This begs the question, does Google even use it? I asked someone fromWaymorecently if they use Google Cloud for their infrastructure. The answer did not instill confidence.


![](https://substackcdn.com/image/fetch/$s_!LGwl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F821b7d25-f393-4498-978d-0ba1b78bf604_685x191.png)

*View Post*


If Google won’t use their cloud service, what business do you have selling it to others? This is not the signal you want to send to enterprise buyers.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
