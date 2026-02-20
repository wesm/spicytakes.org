---
title: "I Love It When People Fix My Problems"
date: 2007-04-30
url: https://www.kalzumeus.com/2007/05/01/i-love-it-when-people-fix-my-problems/
slug: i-love-it-when-people-fix-my-problems
word_count: 400
---


One feature that I had in mind for the 1.1 release of Kalzumeus (does it even make sense to have a 1.1 version of a webapp?  Well, you get the general drift) was the ability to send a real, honest-to-God postal mail in an automated fashion.  It is a requirement with legal significance for some of my customers, and *all* of my customers would see the ability and go “Oooh, that would save me so much hassle”.  I have been searching for a good way to do this for a while.  Obviously, doing it myself would transform me from a highly-paid software developer to a low-paid postal clerk, which is frankly stupid when there are plenty of businesses out there which offer ways to do it without ever having to lick a stamp.


I was originally planning on using the Post Office’s API.  They have a service called NetPost which is aimed at direct marketers.  The prices are pretty high for one piece ($2.25 or so) but reasonable if you’re sending hundreds, I guess.  I used to use this any time I needed to send a letter to America which didn’t need a physical signature on it, since it costs about the same as sending a letter internationally and gets there a week earlier.


However, cost issues aside ($2.25 is dwarfed by the number of sales this will get me, and I can probably charge extra for it for customers who use it on a regular basis), I really hate having to learn *another* API.  It is one more thing that can go wrong with my application, and the consequences of a letter not being sent when my app reports it sent are rather severe.  Then today I ran into a site called Postful, which has a much more convenient interface — [send them an email, they send out a letter](http://www.postful.com).  You preload your account in advance and after that its $.99 a letter for one page, which is where all the letters I’d be sending are.


Composing an email to my requirements is trivial, since I already have the exact same functionality elsewhere in the program to deliver this notification via email.   As a result, this will probably get into the 1.0 release of Kalzumeus.


As an extra bonus, I can now save myself $1.25 the next time I have to send out a letter to the States.  Yay.
