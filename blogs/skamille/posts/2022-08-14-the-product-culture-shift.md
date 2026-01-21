---
title: "The Product Culture Shift"
date: 2022-08-14
url: https://www.elidedbranches.com/2022/08/the-product-culture-shift.html
word_count: 1593
---


Adding product management to more traditional software infrastructure organizations, sometimes with a shift towards platform engineering, is all the rage today. As someone who has done both these things, it doesn’t surprise me to see so many people struggling to make it work. Both of these shifts require going from a siloed, process, tech-focused mindset to a portfolio, usability, and customer-focused mindset. This is a hard transformation, and it’s easy for people who have spent their whole career building infrastructure to misunderstand what product and platform really mean. So I thought I’d share the secret to making this work.


### Your whole engineering culture has to change.


#### Yes, seriously.


Infrastructure organizations tend to be good at many things. They are good at cost management, vendor negotiations, and running systems at scale. They have specialists who know the murky depths of databases, the nuances of networking, and how to debug nasty kernel issues. They may even be good at triaging bug requests from tens or hundreds of teams, planning large-scale failure tests, and coordinating massive migrations.


Unfortunately, they are not usually very good at thinking about the people who will use their systems, taking their preferences into account, and treating them like customers who they are trying to keep. Why should they? The people who use their systems are a captive audience! As I mentioned in my post about [product for internal platforms](https://skamille.medium.com/product-for-internal-platforms-9205c3a08142), this is a major challenge that platform and infrastructure teams have to overcome to build great products.


This culture, with its focus on cost, scale, and process, over people and usability, is very hard to root out. And you don’t want to lose all those rare skills in the process. So what do you do?


### **You can’t just rub product managers on it and call it a day.**


To start, let’s be clear about one thing: as tempting as it might be, just hiring product managers won’t fix this problem. Even if you could find enough good product managers who want this type of job, which you can’t, product managers are only useful when they are paired with willing engineering teams. If the engineering teams don’t feel a sense of ownership for delivering a great product to their customers, product managers are unlikely to close that gap, and they will more likely turn into glorified backlog groomers than true product leaders.


### **You need to change the way you support your products.**


The ticket system black hole is a great way to make your customers feel more like a burden than a focus. I understand that it is hard to manage all the incoming requests for your teams, but taking a close eye to how you provide support, what your response time is for questions, and how you triage incoming issues is critical to this transition. Your engineers should spend time supporting their products. If they are not regularly answering questions, they are missing a chance to appreciate the pain that customers are facing when trying to use the systems. Be careful about making this optional, or leaving it to only junior engineers. Your senior folks will not build the kind of humane products that you need if they are incapable of interacting with the users in a polite and helpful way, no matter how brilliant they might seem. If you have someone you can’t trust to engage productively in help situations, watch out, because this person is probably not building products that are easy to use. Over time, you may find yourself redoing a lot of their work because it is harder to support and drives a high volume of complaints.


### **You need to update your interview process.**


I recommend adding screening for what I call “customer empathy” to all of your interview lineups. This doesn’t have to be deep, it can be simple as asking them how they think about how they write code so that other developers can understand it, or what their approach is to answering questions about the systems they have built. But you want to set the tone that you expect your developers to think not just about how to build the systems, but about the people who are going to use them or work with them.


### **You need to update your systems of recognition and reward.**


If you only promote people who solve big technical problems, you’re going to have a hard time retaining the people who do the work to smooth out the usability edges, actively listen to the customer teams, and adjust their work priorities to fix the stuff that is causing the most pain. So look closely at what you are celebrating, paying, and promoting, and make sure you are including work that makes the product better whatever that looks like, even if it isn’t the hardest technical bits. Remember, this is a cultural change, and cultural changes that don’t involve changes to what is valued when it comes to recognition and rewards are destined to failure.


### **Do you have too many project managers?**


There may always be some need for project managers, but in infrastructure organizations, heavy reliance on project managers can result in a lack of up-front technical planning around one of the most common infrastructure team tasks: migrations. If your migrations are so painful that both your team and your customer teams need project managers to understand where all the dependencies lie and track what is happening, you are not taking ownership of the user experience for your software. Yes, migrations are part of your UX! I am astonished at how often infrastructure teams offer new systems that do not have compatibility with the systems they are replacing, and expect the customers to do all of the work to migrate to those new systems, often on a timeline dictated by the initiating team.


If you are moving to a platform model, you are going to need to own much more of the migration than you have up until now. That platform value add must include lowering the migration pain for customers, which means getting better at doing them entirely yourselves. By limiting the number of project managers now, you force engineers to face project management work that they will not want to do. And the good ones will realize that if they created automation to support the migration, whether it is detection of dependencies, compatibility bridging libraries, or abstractions that allow them to change the internals without changing the client libraries, they won’t have to do so much of that tedious project management work. By saving themselves time, they will save their customers time. So limiting project managers is a good forcing function. Just make sure that you are giving teams time to do this work, and not just making them miserable or shifting the project management onto your new product managers.


### **Your teams are going to spend more time talking to customers, and less time purely writing code.**


There’s no way to shortcut the product mindset transition for your engineering team. You can’t just add a product manager or a customer advisory board meeting once a quarter and call it a day. The team will need to spend more time with the customers, and more time strategically planning for how to address holistic concerns, rather than just triaging the latest set of customer complaints. There will be an up-front cost as you change the way people work. They may complete fewer tickets or other process-oriented measures of productivity, and the pace of work might look slower than it did when they were just churning through a never-ending backlog of tickets. But over time, the work that is produced should be better, as measured by customer surveys, adoption, migration timelines, and eventually, engineering productivity.


### Keep it fun!


By the time companies go through this transition, they are often in a deep state of us-vs-them between their infrastructure organization and their other business/product engineering teams. This situation never feels good to the infrastructure organization. No matter how much they may claim outwardly that their users are hopeless or ungrateful (or worse), it is simply not much fun to have an antagonistic relationship with your users, and to feel like you are deep inside of an us-vs-them dynamic with colleagues. So while this transition is going to be tricky, it can also be fun if you let it. Get feedback from your users about what they love about the product. Share kudos as they come in, and take the time to celebrate improvements in your customer satisfaction metrics. Make sure your teams are part of the celebrations when their work enables an application team to do something they couldn’t do before. This is an exciting opportunity, a chance to learn, to modernize your approaches to work, and to create a more positive culture, and leading with a positive attitude will make all the difference in how fun it is for everyone.


### **Wrapping up**


In many ways, this cultural shift echoes the changes that happened during the “devops”/SRE transformation. Engineers in SRE-focused organizations do not build code that they carelessly throw over the wall to an operations team. In the same way, engineers in a product-focused organization do not build software without consideration of the users of that software. These transformations ask more of the engineering teams, but deliver higher-quality outcomes as a result. It’s expensive and takes time but I promise you, it’s worth it.


*Enjoy this post? You might like my book, *[*The Manager’s Path*](http://amzn.to/2nw1QN5)*, available on Amazon and Safari Online!*
