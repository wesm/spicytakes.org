---
title: "Problem Solving At My Job and My Business"
date: 2009-01-20
url: https://www.kalzumeus.com/2009/01/20/problem-solving-at-my-job-and-my-business/
slug: problem-solving-at-my-job-and-my-business
word_count: 786
---


One of my customers just got in touch with me to express their dissatisfaction with my Mac support, in particular how long it took me between updates, and asked when I was planning to release an update and if not how quickly I could have their money back.


Three thoughts went through my head:

1. Happily, I just released a new version and am putting out the inevitable minor brushfires to prove it.
2. Oh well, its perfectly reasonable that he hasn’t heard about the update yet, its only been out for 20 hours.  And my last major addition to the software  was almost a year ago.
3. My Mac support is, compared with my PC support, rather lackluster.  I don’t own a Mac, I have to rely on my blog readers to pull me out of the bacon for it, and while I think I’m probably the best bingo card creator on the platform I have plenty of room for improvement.


Then I looked up his registration details, because I was giving him instructions on how to install an update and I always read people their Registration Key when I tell them to install anything (just in case — shouldn’t be needed).


Now, if you open up my Rails console and type in Customer.find_by_any_identifying_information(“whatever”), which I used instead of the web version (I had a shell open and am lazy like a fox), you get back an array of records.  Which, in Rails, includes all the fields in each record — including timestamps on when the record was created.  This customer’s timestamp was from March, 2008.


Wow, that is an interesting take on the 30-day guarantee, I though.  Then I remembered, wait, I only started tracking these things in Rails back in March… which means his record might have been one of the ones created when I loaded the database with all my previous transaction records.


So I typed “customer.sale.time”, which gets the actual time of the sale rather than the time the record was written to the DB.


Tue **Dec 26** 04:27:28 UTC **2006**


Wowza.  I really had not been expecting that one.  And then banged out  the following:


Hello $NAME.  You might be interested in knowing that I released version 2.5 of Bingo Card Creator for both the Mac and PC yesterday.  It includes approximately 500 word lists and a few new features that people have requested.


You can upgrade to it by going to [http://www.bingocardcreator.com](http://www.bingocardcreator.com/) and …


Please tell me if you’re not satisfied with the new version.  I wouldn’t want to keep your money unless you’re happy.


One minor brushfire put out, two more to go.  Though it may seem unlikely in light of the instant circumstances, I mean it when I say it: *I love this job*.  In comparison with my day job, which is generally a pretty nice place to work don’t get me wrong, I have the absolute right to change anything I want to solve problems for myself and the customer, and oh is that intoxicating.


It is particularly intoxicating after having to fight for authority to schedule myself to write design documentation in English to hand over to one of our outsourcing teams.  “Your time is too valuable to use on translation” is a lovely thing to hear, but I’m closer to the opinion that my time is too valuable to spend the next 6 months dealing with code that is totally orthogonal to the customer’s actual needs.


This was richly demonstrated when, following the traditional “figure out what the designed behavior of the system is by pushing buttons and seeing what happens” documentation method, our outsourcing team filed a bug about the system being configured improperly, because they attempted to login with the credentials which we provided (after a week of laboriously setting up a copy of the system — without reference to English documentation, mind you) caused them to see a screen full of red text.


This resulted in my most amusing conversation ever about designed behavior:


“Are you seeing the error message above or below the weather report?”


“Why is the login screen showing a weather report?  That is probably a bug, too.”


“No, the weather report is not a bug.  If you flag an announcement with announcement_type = 5, then it shows up in big red text on the login screen.”


“That is the error message!  The big red text!”


“Oh, then this is expected behavior for the system.  The administrator has chosen to share it with the users, and it is in the test data and being displayed appropriately.”


“But why is it in huge red letters?!”


“Because the weather report reads


# ‘Typhoon Warning‘


Closing this bug as ‘by design’.”
