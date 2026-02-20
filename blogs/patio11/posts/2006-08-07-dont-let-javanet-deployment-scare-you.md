---
title: "Don't Let Java/.NET Deployment Scare You"
date: 2006-08-07
url: https://www.kalzumeus.com/2006/08/07/dont-let-javanet-deployment-scare-you/
slug: dont-let-javanet-deployment-scare-you
word_count: 586
---


[Ali ](http://www.phplazy.com/)commented, in regards to my last post, that I should really program my next project in C++ or similar, as requiring a Java/.NET library download scares off lots of dialup customers.  This would have been a valid consideration… in 1998.


In 2006, not so much.


1)  **I don’t have dialup customers**.  I am targetting a group of very non-technical customers.  The biggest two ISPs in my logs are Comcast and AOL, very mass-market ISPs.  Do you know how many of my visitors stroll on by with dialup?  **10%**.  60% are on cable/DSL and 30% are on a corporate internet (mostly teachers on their work computer, I’m guessing).  Additionally, of the 10% of customers who are on dial-up fully half of them hail from countries where I do not expect to ever sell a single copy of my software.


2)  **Java/.NET deployment is very high**.  97% of my visitors have some flavor of Java installed and enabled.  **97%**.  (Similarly, Flash stats: 98% total, 85% v8 or v9.) That doesn’t help me if they have the ancient MS1.1 JRE installed, which is one of the only widely-deployed JREs Bingo Card Creator won’t run on.  I don’t have any convinient way to check for that other than getting them to visit a certain page on my site, which most people don’t.  Of the highly unrepresentative sample that do, 80% of them at last count have Sun 1.3 or higher.  Don’t believe the statistics from 2000 that you read on the Internet about 50% deployment rates — Java, like Flash or .NET or anything, is a very viral bit of software.  You’ll eventually stumble across content which you want to access that needs it, and after you do this you’re set until your next computer upgrade.  The average person upgrades computers once every 4-6 years, which means as time goes on the number of machines which will have any given runtime approaches 100%.


3)  **Know your market. ** Lots of educational software, including the stuff distributed on CDs, requires Java to run.  I am able to happily piggyback on the inroads made by metric truckloads loads of eduware.  Its like how you can assume DirectX is installed on the machine of anyone who has bought a AAA computer game in the past, oh, ten years or so.


4)  **Java comes pre-installed on most new consumer PCs**.  it can’t be bundled with Windows anymore, but it [comes bundled](http://java.sun.com/developer/technicalArticles/upgrade/javaplatform/) with your Dell, Gateway, Mac, etc etc.


From where I sit, its not worth the vastly higher development time and impact on the user experience to cut Java out of the equation, unless its  in favor of .NET, which I may very well try out for my next project but which has exactly the same wrinkle.  At current traffic rates, assuming every one of my dialup customers had no JRE and refused to install, that would cost me a total of 5 successful trial installations a month.  I get more installations originating from AdSense spam sites every week.


I’m not totally sanguine about requiring the JRE to run my application, but I think its a good tradeoff of market size versus development complexity.  I guarantee you that if I had to do my interface in MFC I’d still be months away from launch.  I suppose I could be convinced to change my mind by hard statistics showing that vast numbers of my potential customers can’t run Bingo Card Creator, but the best statistics I have available indicate this is not the case.
