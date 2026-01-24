---
title: "A Question of Programming Ethics"
date: 2008-03-07
url: https://blog.codinghorror.com/a-question-of-programming-ethics/
slug: a-question-of-programming-ethics
word_count: 472
---

From the ACM [Code of Ethics](http://www.acm.org/about/code-of-ethics):

kg-card-begin: html

> As an ACM member I will
> Contribute to society and human well-being.
> Avoid harm to others.
> Be honest and trustworthy.
> Be fair and take action not to discriminate.
> Honor property rights including copyrights and patent.
> Give proper credit for intellectual property.
> Respect the privacy of others.
> Honor confidentiality.

kg-card-end: html

It’s hard to square that with the following hair-raising tale **Dustin Brooks** sent me via email:

kg-card-begin: html

> I was looking for a way to back up my gmail account to a local drive. I’ve accumulated a mass of important information that I would rather not lose. During my search I came across G-Archiver, I figured what the heck I’ll give it a try.
> It didn’t really have the functionality I was looking for, but being a programmer myself I used Reflector to take a peek at the source code. What I came across was quite shocking. John Terry, the apparent creator, hard coded his username and password to his gmail account in source code. All right, not the smartest thing in the world to do, but then I noticed that every time a user adds their account to the program to back up their data, it sends and email with their username and password to his personal email box! Having just entered my own information I became concerned.
> I opened up a browser and logged in to gmail using his account information. It still worked.
> Upon getting to the inbox I was greeted with 1,777 emails with account information for everyone who had ever used the software and right at the top was mine. I decided to go ahead and blast every email to the deleted folder and then empty it. I may have accidentally changed the password and security question to something I don’t remember as well, whoops, my bad. I also contacted google to erase this account as I didn’t see a way to delete it myself.

kg-card-end: html

I generally try to give people the benefit of the doubt, but it’s difficult to imagine any scenario where this isn’t a **completely malicious violation of people’s trust**. This is every user’s greatest fear when giving out their login credentials, and to see it realized hurts the trust relationship between users and every other professional programmer working today. I’ve inadvertently posted my own login information to this very blog before. Fortunately for me, an eagle-eyed reader by the name of Israel Orange didn’t abuse that information for his own gain, but instead kindly pointed out my error to me in a private email.


I certainly hope there are more programmers out there like Israel Orange than John Terry. Ethics matter for programmers, too.

[privacy](https://blog.codinghorror.com/tag/privacy/)
[ethics](https://blog.codinghorror.com/tag/ethics/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[security](https://blog.codinghorror.com/tag/security/)
[confidentiality](https://blog.codinghorror.com/tag/confidentiality/)
