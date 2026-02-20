---
title: "'Thats Funny, No One Has Bought a CD In Weeks'"
date: 2007-03-27
url: https://www.kalzumeus.com/2007/03/27/thats-funny-no-one-has-bought-a-cd-in-weeks/
slug: thats-funny-no-one-has-bought-a-cd-in-weeks
word_count: 456
---


I’ve had my best month of sales ever, but only 1 CD in that time.  Typically about half of my customers get the CD.  I had a vague feeling that there were fewer CD orders than usual this month but it didn’t raise any flags with me.  Then I got a fairly typical email saying “How do I purchase your software?”  Thanks for your interest, click the big red button which says Purchase Now.  “That doesn’t say it comes with a CD.”  Thanks for your continued interest, you need to click the one next to the text Purchase a CD.  “That doesn’t work.”  Thanks for your continued interest, you need to… oh, wait.  It actually *doesn’t* work.


It seems that when I switched the item numbers in e-junkie (to accomodate SwiftCD integration) I forgot to also switch the item numbers in the e-junkie links on my page.  For some reason this actually didn’t cause a problem for at least the first two weeks.  It had to be working for one of my customers to get an order for a CD through on March 3rd.  At some point after that the e-junkie system began saying “Oh, wait, the item number that link references doesn’t exist anymore” and bailing when you tried to use it to add things to the cart.  I assume that most of my customers who saw this error either shrugged and said “OK, I’ll take the download!” and some, more worrisomely, probably left.


This is one of those bugs that just makes me want to die inside as a programmer.  The systems involved have well-understood interfaces but the inner workings are complex and totally opaque to me.  As a result, bugs are hard to predict except by seeing them, and if their visibility is obscured by whatever system interaction happens its likely that I’ll be the last to know.  I guess the only solution to that is regular monitoring and applying enough concentration to know when the process is out of control.


As long as I’m on the subject of CDs: if you’ll excuse my own HTML coding errors, the integration of SwiftCD and e-junkie has been flawless in every respect.  Its also cut the amount of customer support I had to do literally in half — back when half of my orders were CDs I spent as much time retyping addresses and invoice numbers into cd-fulfillment.com as I did answering customer emails.  Now delivering a CD takes as much marginal work as delivering a registration key: nothing.  Granted, at my level of sales thats probably 5 minutes saved 3-4 times a week, but for some reason minor repetitive nuisances like that grate on me far more than their absolute time required would suggest.
