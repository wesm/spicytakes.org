---
title: "Update on Basecamp 3 being stuck in read-only as of Nov 8, 9:22am CST"
date: 2018-11-08
url: https://signalvnoise.com/svn3/update-on-basecamp-3-being-stuck-in-read-only-as-of-nov-8-922am-cst/
slug: update-on-basecamp-3-being-stuck-in-read-only-as-of-nov-8-922am-cst
word_count: 792
---


Basecamp 3 is now back online for reading and writing. All data was confirmed to be fully safe and intact. No emails that were sent to Basecamp during the outage were dropped. We may still have some backlogs on processing things like incoming emails, and you may still see some slowdowns here and there as we catch up. But we are back, and we are safe.


We will be following up with a detailed and complete postmortem soon. All in, we were stuck in read-only mode for almost five hours. That’s the most catastrophic failure we’ve had a Basecamp in maybe as much as decade, and we could not be more sorry. We know that Basecamp customers depend on being able to get to their data and carry on the work, and today we failed you on that.


We’ve let you down on an avoidable issue that we should have been on top of. We will work hard to regain your trust, and to get back to our normal, boring schedule of [99.998% uptime](https://basecamp.com/3/uptime).


*Note: If you were in the middle of posting something new to Basecamp, and you got an error, that data is most likely saved in our browser-based autosave system. If it doesn’t appear automatically, we can help you recover that data. *[*Please contact support*](https://basecamp.com/support)* if you’re in this situation, and we’ll have a team ready to assist.*


Below is the timeline for today:


At 7:21am CST, we first got alerted that we had run out of ID numbers on an important tracking table in the database. This was because the column in database was configured as an integer rather than a big integer. The integer runs out of numbers at 2147483647. The big integer can grow until 9223372036854775807.


At 7:29am CST, the team diagnosed the problem and started working on the fix. This meant writing what’s called a database migration where you change the column type from the regular integer to the big integer type. Changing a production database is serious business, so we had to test this fix on a staging database to make sure it was safe.


At 7:52am CST, we had verified that the fix was correct and tested it on a staging database, so we commenced making the change to the production database table. That table in the database is very large, of course. That’s why it ran out of regular integers. So the migration was estimated to take about one hour and forty minutes.


At 10:56am CST, we completed the upgrade to the databases. This was the largest part of the fix we needed to address the problem. But we still have to verify all the data, update our configurations, and ensure that we won’t have more problems when we go back online. We’re working on this as fast as we can.


At 11:33am CST, we’re still verifying that all data is as it should be for Basecamp 3. The database migration has finished, but the verification process is still ongoing. We’re working as fast as we can and hope to be back fully shortly.


At 11:52am CST, verification of the databases is taking longer than expected. We have 4 databases per datacenter and we have two datacenters with databases. So a total of 8 databases. We need to be absolutely certain that all the data is in proper sync before we can go back online. It’s looking good, but 99% sure isn’t good enough. Need 100%.


At 12:22pm CST, Basecamp came back online after we successfully verified that all data was 100% intact.


At 12:33pm CST, Basecamp had another issue dealing with the intense load of the application being back online. This caused a caching server to get overwhelmed. So Basecamp is down again while we get this sorted.


At 12:41pm CST, Basecamp came back online after we switched over to our backup caching servers. Everything is working as of this moment, but we’re obviously not entirely out of the woods yet. We remain on red alert.


I will continue to update this post with more information, and we will provide a full postmortem after this has completed.


---


Further insight on the technical problem: It’s embarrassing to admit, but the root cause of this issue with running out of integers has been a known problem in our technical community. We use the development framework Rails (which we created!), and [the default setting for that framework move from integer to big integer two years ago](https://github.com/rails/rails/pull/26266).


We should have known better. We should have done our due diligence when this improvement was made to the framework two years ago. I accept full responsibility for failing to heed that warning, and by extension for causing the multi-hour outage today. I’m really, really sorry 😢

