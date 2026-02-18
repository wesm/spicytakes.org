---
title: "Why Data Warehouse Automation is not more popular"
date: 2017-06-28
url: https://www.ssp.sh/blog/why-data-warehouse-automation-is-not-more-popular/
slug: why-data-warehouse-automation-is-not-more-popular
word_count: 2297
---

![Why Data Warehouse Automation is not more popular](https://www.ssp.sh/blog/why-data-warehouse-automation-is-not-more-popular/images/DWA_wordle1_c-1-1024x466.png)

Contents

I was working with a Data Warehouse Automation (DWA) tool for a little more than a year, and I have to say I loved it. As a BI developer you could focus on the challenges you had in dimensional modelling, what granularity should you have the fact tables and going crazy with the business requirements and everything **fast, consistent and tested!**

But why is Data Warehouse Automation not used more often and more popular? I’m asking that myself more and more. That’s why I’m writing a series of blog posts all about DWA. In this first blog, I’m trying to find possible reasons behind and also argue for DWA, and why we should use it more often.


> Every one needs to make data driven decision faster, why not use a generator which gives you answers in days instead of months..?


## Losing control


What do I mean by that? Many people and therefore many companies fear to lose control in general, but particularly what code the tool produces. **Do we really need to be in control of it?** I would say yes. Especially in the long run and as far as I can tell, the vendors recognised that and give you most of the time the ability to work with templates to where you can customise how the generated code will look like. I appreciated that much in [biGenius](https://bigenius.info), the tool I worked with most.


There are others tools like [timeXtender](http://www.timextender.com) where the focus is more on the business users, and the code is further hidden in the backend. With it, the architecture is also more or less fix created as best practice. However, you need to consider, that the code you get is thoroughly tested, optimised by tuning experts and most probably outperform manually written code in most of the cases. Of course not always, sometimes due to lack of time the manual code is written poorly or not optimised at all.


Additionally, you also have to ask yourself what you want. If you want an effortless and fast delivery of the DWH, why you have to bother with all the architectural questions? And as I learned with timeXtender, this tools is straightforward to use and can even be used by business users directly without having much knowledge about the complexity of data warehousing.


I like their commercial which is (only) a bit over exaggerated but still very true in my opinion in nowadays life 🙂


## Locked-in (black-box)


The next pain point is mostly: “I cannot use it because then I lock myself in later!”. Yes maybe, but **what does it matter if you use it for a short and fast [PoC](https://en.wikipedia.org/wiki/Proof_of_concept)**, or if you know you have a very static data source(s)? Not much in my opinion. I fully agree if you’re creating a big enterprise DWH. In that case, **I would look for a Data Warehouse Automation tool that doesn’t lock you in, and yes they exist**.


True there are so many nowadays, I didn’t get the chance to try them all, however, some of them I worked with or tested. If I would need to create a DWH today, I’d probably consider [biGenius](https://bigenius.info) and [BimlStudio](https://www.varigence.com/BimlStudio) (not really a DWA but very soon they are launching [BimlFlex](https://varigence.com/Products) which is the DWA framework around, coming in [July](https://www.linkedin.com/pulse/why-choose-data-warehouse-automation-software-lock-contract-avenant)) that let you choose or customise your architecture totally free and adaptable to the DWH of your needs. There is also an open source DWA tool from New Zealand called [ODE](http://optimalbi.com/blog/2017/03/09/whats-new-in-ode-version-4/) which has the full source code on [GitHub](https://github.com/OptimalBI/optimal-data-engine-mssql).


Very helpful and probably the future, some of the tools give you the opportunity to generate SSIS packages as a delivery. In that case, you’re no more locked-in meaning you can just stop whenever you want and carry on with the plain SSIS packages.


The positive side effect about beeing locked-in (or using DWA tools) is, that your meta-model is always up-to-date. By that, your model gets very consistent not only with the many times of generating the DWH but also because you and all other developers use the same metamodel and therefore the same way of handle the general methodology like logging, adding technical fields, doing the lookup in the Data Mart etc. These conditions are very difficult to keep consistent in the traditional way of data warehousing, I’ve seen that a lot of times. Even when you only working yourself on a DWH it can be hard and tempting to not follow the same structure all the time.


## Skilled people


Another argument against Data Warehouse Automation is **you need to have highly skilled people** who understand what they are doing. Plus **new employees have a hard time understanding the existing DWH logic**. I believe if you don’t trust in your employees why then even hire in the first place? Of course, it needs more time to understand what’s going on with a DWA tool, but isn’t that the whole purpose to invest in something a bit more complex and gain X-time faster delivery (and more consisted, and everything else) on the other hand? Another point is if you have limited resources and specialists are hard to find on the market anyway so you **can achieve with the existing resources more in the same time and don’t even have to hire new employees**!


A simple illustration made by [WhereScape RED](https://www.wherescape.com/products-services/wherescape-red/) which can be easily applied to other DWA tools:


[

](https://www.ssp.sh/blog/why-data-warehouse-automation-is-not-more-popular/images/what-we-do.Crm3dQ.jpg)Illustration by WhereScape


You could even say the opposite is the case and not use any specialists at all. With a good Data Warehouse Automation tool, the person doesn’t need to know about SCD2  in details nor hot to implement, the tool is doing it for you by simply checking the checkbox.


## Licence fee


Some of the tools can be very expensive but others having reasonable prices. Furthermore, there are also open source Data Warehouse Automation tools free of charge for example for Microsoft technology [ODE](http://optimalbi.com/blog/2017/03/09/whats-new-in-ode-version-4/) created by [OptimalBI](http://optimalbi.com/contact-us/). Or you can use [Biml](http://bimlscript.com/) and create your own little framework. Biml is open source and perfectly fits for any SSIS or SSAS automation.


*A little bit more about this in my other post in this series shortly to come.*


### Return on Invest (ROI)


I made the experience that you save plenty of time on the development part, even more after you delivered your first sprint. The ROI cannot be stated generally, it has to be calculated individually depending on the requirements and amount of dimension and fact tables (this is, by the way, a good indicator to calculate your costs and compare them with and without DWA).


We tried to calculate the difference with using a DWA tool and without in a big project running over one year period split into 3 chunks, each of them as big to be a DWH in itself (total: 162 Tables, 15 facts, 43 dimensions). The first junk was **delivered after 3 months running daily in the production environment** (43 tables) including requirements engineering with the customer and building a data store layer with SCD2. This was with nobody of us (1 project manager, 1 requirement analyst, 2 developers) knowing the DWA tool beforehand. Chunk 2 and 3 were benefited a lot by the learning curve from chunk 1 and deploying new features to production much faster.


We concluded this would never have been possible with traditional data warehousing. Only getting the requirements and putting them into a specification would have taken three months. In this way, the DWA tool allowed us to develop in parallel to gather all the requirements, which you would obviously avoid in the traditional way.


## Speed


It takes much more time to deliver with a complex Data Warehouse Automation tool is another thing I hear sometimes. But as said by timeXtender with the fast changing environments and shorter delivery cycles, there is not really a way around automation:


> By combining the power of automation …, you get results that are five times faster than traditional methods, including a 70% reduction in build costs and a 60%-80% reduction in maintenance costs. Short iterations ensure that your analytics platform is constantly aligned with the needs of your business. With the power of automation, you can respond to changes quickly and efficiently, make updates easily, and solve problems in minutes that once took days or weeks.


Certainly, the numbers always sound great from a Data Warehouse Automation tool vendor. Me for myself focusing more on the real-time examples and they clearly show a huge improvement in terms of delivery and time saved. Although you may say, **the most amount of work is in gathering the data and defining the data model** including meetings with the business. I partly agree. In traditional data warehousing, yes you spent the most time doing that but not in the automation and _agile _way. One problem is because doing that in sequences, another that after the first deployment the hell starts as changes are taking ages to integrate and especially the deployment process is hard and painful. Furthermore, until you get to the first deployment takes normally several months (even years in EDWH) because of every technical detail has to be clarified.


Which in DWA way, all these circumstances are defined from the beginning. Logs are written, technical fields are automatically added to all the tables and so on… Surely you can fine tune and change everything at any time later on, but you can start up right away. Also as mentioned before, deployment is less painful as you deploy every time and by that, you actually test the structure and the loading all the time!


## Emotion


Finally, there are emotions included often (always?) around this topic. Probably because most people are thinking they get replaced by a machine which is a general phenomenon these days. You could think of it in that way, and sure there are certain tasks which can be replaced with a tool and it does it probably even better than we humans do, we need to accept that. Yet still, there isn’t a machine or a tool that can do it all and knows by itself what to do. **Data Warehouse Automation tools are here to automate the boring tasks and leave the fun stuff for the developer**, meaning the developers are still highly needed in all processes, except in the above-mentioned example in chapter *skilled people* where the business users can do little PoC’s themselves.


I don’t like having an emotional discussion, **emotions only blur the picture. In my opinion, it should always be based on facts**. One reason why I created that blog post to hopefully cause more discussions based on facts 🙂.


## Conclusion


The way I see it, there is not a way around Data Warehouse Automation in the long run. The business wants to see results faster and faster also because they get used to the way of working with data lakes where data can be added immediately e.g. (a follow-up blog post on that topic will be published soon included in this blog series).


As a developer, I’m looking forward to learn new exciting tools, deliver significantly faster, with higher consistency and leave the boring tasks to the tool. I will go for the potential and not fight against it.


Go to the next Blog post [Why automate? What does DWA for us?](https://www.ssp.sh/blog/why-automate-what-does-dwa-for-us) or see similar articles in the links below.

## Links {#Links}

Other blog posts that I find useful around this topic:

  * The data warehouse isn’t dead: it just needs an automation overhaul by Kevin Lonergan - <a href="http://www.information-age.com/data-warehouse-isnt-dead-it-just-needs-automation-overhaul-123459596/" rel="noopener">http://www.information-age.com/data-warehouse-isnt-dead-it-just-needs-automation-overhaul-123459596/</a>
  * Data Warehouse Automation: Selecting the right tool by Johan Machielse - <a href="http://johanmachielse.blogspot.dk/2015/07/data-warehouse-automation-wherescape.html" rel="noopener">http://johanmachielse.blogspot.dk/2015/07/data-warehouse-automation-wherescape.html</a>
  * 9 Reasons Data Warehouse Projects Fail by Chris Merrick - <a href="https://blog.rjmetrics.com/2014/12/04/10-common-mistakes-when-building-a-data-warehouse/" rel="noopener">https://blog.rjmetrics.com/2014/12/04/10-common-mistakes-when-building-a-data-warehouse/ </a>
      * Comment _sspaeti_: If you look at most common errors done in Data Warehousing, then you will see that many of them just disappear with Data Warehouse Automation.

*Just to state it clearly, I’m not supported by any vendors. Everything in my post is based on my own experience and opinion, [free](https://www.ssp.sh/blog/the-more-you-share-the-more-you-get/) to share 🙂.


## Comments


### Comment by Hans Michiels on 2017-06-28 19:45


Great post Simon, I fully agree with most of it.

Also since a few days, DWA tools can be compared on the web site [[http://www.dwa.guide](http://www.dwa.guide)](http://www.dwa.guide)

It is a quite complete overview.


### Comment by sspaeti on 2017-06-29 21:32


Hi Hans, thank you for your feedback and for sharing your guide, it looks very comprehensive yes ð


### Comment by Johan Machielse on 2017-07-03 21:10


Nice article Simon!


### Comment by sspaeti on 2017-07-05 23:25


Thank you, Johan! Good to hear that you liked it


### Comment by adstam on 2017-07-17 10:47


Nice article, but maybe in this group you are just preaching for the converted ;-). A common pitfall, developers do’nt trust dwa tools because they believe they always can outsmart any toolvendor. I’m a bog supporter of dwa tools since I came across the first one in early 2000. One should have very specific reasons not to use a DWA tool and I can’t think of one


### Comment by Peter Avenant on 2017-07-18 23:27


Nice to see the mention of BimlStudio and BimlFlex. We will be posting a number of Walkthroughs on the Varigence website over the coming weeks.


### Comment by sspaeti on 2017-07-19 15:18


You are probably right It’s hard to believe in DWA tools without actually getting the chance to use one.


### Comment by sspaeti on 2017-07-19 15:21


Hi Peter, I saw the new webinar, is excellent! For those who haven’t seen it, here is the link: [[https://www.varigence.com/Blog/Post/69](https://www.varigence.com/Blog/Post/69)](https://www.varigence.com/Blog/Post/69)

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/why-data-warehouse-automation-is-not-more-popular/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[BiGenius](https://www.ssp.sh/tags/bigenius/)
[Data Warehouse Automation](https://www.ssp.sh/tags/data-warehouse-automation/)
[TimeXtender](https://www.ssp.sh/tags/timextender/)
