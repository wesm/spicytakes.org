---
title: "Postmortem on the read-only outage of Basecamp on November 9th, 2018"
date: 2018-11-12
url: https://medium.com/signal-v-noise/postmortem-on-the-read-only-outage-of-basecamp-on-november-9th-2018-9165c315ee7f?source=rss-54bcbf647830------2
slug: postmortem-on-the-read-only-outage-of-basecamp-on-november-9th-2018
word_count: 704
---


![](https://cdn-images-1.medium.com/max/998/1*6aOuZYkr-5o10PhGrzhgIA.png)


Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, but no new information could be entered, and no existing information could be altered. Everything was frozen in place.


The root cause was that our database hit the ceiling of 2,147,483,647 on our very busy events table. Almost every single activity in Basecamp is tracked in this table. When you post a message, update a todo list, or applaud a comment, we track that activity in the events table. So when we became unable to write new events to that table, every attempt to do practically anything in Basecamp was halted.


This was an avoidable problem. We were actively working on expanding the capacity of the events table in the days prior to this outage, but we failed to properly account for how quickly we were running out of headroom.


To compound the avoidable factor, we should had been aware of the general issue much sooner. The programming framework we use, [Ruby on Rails](https://rubyonrails.org) (which was originally extracted from Basecamp!), moved to [a new default for database tables](https://github.com/rails/rails/pull/26266) in version 5.1 that was released in 2017. That change lifting the headroom for records from 2,147,483,647 to 9,223,372,036,854,775,807 on all tables. Which ended up being the same root-cause fix that we applied to our tables.


It’s bad enough that we had the worst outage at Basecamp in probably 10 years, but to know that it was avoidable is hard to swallow. And I cannot express my apologies clearly or deeply enough.


We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998%. This near five-hour outage has taken that impressive statistic down to [a more humbling 99.978%](https://basecamp.com/3/uptime).


Some companies might choose to weasel around an outage like ours by claiming that it was only a “partial outage”, because the application remained available in read-only mode for the majority of this time. But that’s not what we’re going to do at Basecamp. We’re going to take the scar in our uptime record as a reminder to do better.


Because we owe everyone using Basecamp to do better. It’s embarrassing and humbling to have suffered the biggest outage at Basecamp in a decade from an issue that we should have addressed years ago, and that we were actively working on addressing, but failed to complete in time.


As the CTO of Basecamp and the creator of Ruby on Rails, I accept full responsibility for our failures. I should have been more vigilant with our own database schema when Rails 5.1 announced the new default, and I should have followed up and asked the right questions when we finally did start work on remediation. I’m really sorry to have failed you 😢


If you have any questions, or if we can help in any way, please reach out to our wonderful support crew who’ve been dealing with each report individually.


I also want to express my deep gratitude to everyone who’ve been so gracious with their kind words of encouragement and support during and after this ordeal. I don’t know if we’ve earned such understanding, given our clear culpability, but we are extremely grateful none the less.


Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop [using our status.basecamp.com updates](https://status.basecamp.com/status/bc3/2018/11/8) and [a play-by-play record on our blog](https://m.signalvnoise.com/update-on-basecamp-3-being-stuck-in-read-only-as-of-nov-8-9-22am-cst-c41df1a58352?source=collection_home---4------1---------------------&gi=d7434c48625d). We can’t promise to be perfect, but we promise always to keep you informed in a timely and completely transparent manner.


*On a personal note, I want to apologize for not posting this postmortem until today. The plan was to have this final summary ready on Friday, but then the Woolsey fire hit, and our family was forced to evacuate our home in Malibu. It’s been a crazy week 😬*


![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=9165c315ee7f)


---


[Postmortem on the read-only outage of Basecamp on November 9th, 2018](https://medium.com/signal-v-noise/postmortem-on-the-read-only-outage-of-basecamp-on-november-9th-2018-9165c315ee7f) was originally published in [Signal v. Noise](https://medium.com/signal-v-noise) on Medium, where people are continuing the conversation by highlighting and responding to this story.

