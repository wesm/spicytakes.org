---
title: "The Stack Overflow Age"
date: 2018-04-06
url: https://www.joelonsoftware.com/2018/04/06/the-stack-overflow-age/
word_count: 1491
---


Hi, everyone! A lot of stuff has happened since I was writing all those blog posts about Aeron chairs 18 years ago. Some of those blog posts are old enough to go to college.


And, also: [Stack Overflow](https://stackoverflow.com/) will be ten years old soon! Wow! So I thought it would be cool to get the old band back together for a little reunion tour over the next few weeks. I want to catch you all up on some stuff but mostly I want to tell the story of Stack Overflow in a not-completely-disorganized way. With some perspective, it’s clearer now what we did right and what we messed up, so I’ll try to cover the good and the bad over a series of blog posts.


And, also: we’re just a few weeks away from launching Stack Overflow Teams, the biggest upgrade to Stack Overflow ever, so that’s going to be really cool. I’ll get to that in a future blog post!


Today is chapter one. I want to talk a little bit about what it was like for developers before Stack Overflow, the problem that Stack Overflow tried to solve, and early origins.


In the early days of the Internet, before the Web, there was a system called [Usenet](https://today.duke.edu/2010/05/usenet.html) which created primitive online discussion forums. When programmers had problems with their code, they could ask a question on a Usenet forum. (They were technically called newsgroups, not forums (even though they had nothing to do with news. (You couldn’t even get news on Usenet.)))


As soon as the world wide web became a thing, Usenet was immediately technically obsolete. We programmers started asking about our problems on various web-based forums, of which there were thousands.


One of the biggest such forums was called Experts Exchange. The first version of Experts Exchange was not successful financially. Apparently they went bankrupt in 2001. Eventually new owners bought the assets and resurrected the site with a clever business model: charging money to read answers.


This actually fixed the business, which started making money, but it caused some problems.


The first problem was that programmers with problems would search on Google, not on Experts Exchange. And Google only knows about free, open websites, not websites that you have to pay to access. So EE did a bamboozle: when the Google Robot came by, they showed it the full question and its answers. But when regular people went to the same page, they saw the answers were scrambled, with instructions to pay (I think it was about $250 a year) to see the results. Most programmers couldn’t be bothered.


The second problem was that EE let you get a free membership if you answered a certain number of questions. As it turned out, the people who were most desperate for free memberships were not exactly the best programmers in the world, and they wrote low quality answers to questions just to get those free memberships. And the quality of answers on the site went down.


For a long time (at least five years, I think) programmers would constantly come across EE in the Google search results, try to click on them, discover that it was a pay site, grumble, and just go back to Google and try to find an answer for free.


And I kept thinking, how hard is it to run a discussion forum on the Internet? For fudge sake, I had written one in Visual Basic in a weekend. (Not kidding, actually. Yeah I know that I am always saying “I could do that in a weekend in Visual Basic” when developers tell me some feature is going to take a year. This is why). So I was confident that it was only a matter of time before one of the 9,000,000 smart programmers in the world decided to route around this EE damage and make a free forum.


You know what? Nobody ever did. I kept waiting.


Another thing I wrote in a weekend (well, to be precise: a fortnight (shut up, I’m telling this lie)) was a [job listing board for this blog](https://www.joelonsoftware.com/2006/09/05/introducing-jobsjoelonsoftwarecom/). And in the first month of running that job board I think we sold about $90,000 of job listings. Huzzah! And then I thought, wow, if we smashed these ideas together—replace Experts Exchange with a free site, and pay for it with job listings—we could undo the damage to the internet and let developers get work done again.


I kept thinking “Man, this is so obvious, somebody is going to do it.”


And they never did.


And I went to one of the programmers at Fog Creek, and explained my idea, and he was like “yeah yeah sounds like a great idea, but I really like working on FogBugz.”


And more time went by.


And eventually, early in 2008, a developer/blogger named [Jeff Atwood](https://blog.codinghorror.com/) called me up, and said, “Hey Joel, I’m thinking of quitting my day job to be a Pro Blogger; you’re a blogger: what do you think?”


And I said, “Jeff, I’ve got a better idea” and I told him about the idea to combine the job listings with the Q&A site for developers, and, it took more than a weekend, but eventually I convinced him. We started talking about all the ways our Q&A site would be amazing. Jeff started working on the code in April 2008, recruited two other programmers to join him (Geoff and Jarrod, who are still here), and the three of them heroically launched what became Stack Overflow in September 2008.


And thus began the Stack Overflow Age.


Stack Overflow was better because it was free, but it had a ton of other “innovations” (which I put in quotes because we stole them from other Internet pioneers) which made it a much, much better site for getting answers to programming questions.


We wanted the whole thing to be a fun game, with incentives to answer questions, so we had a reputation system. The more you answer, the more reputation you earn. The reputation idea had been seen before on sites like Slashdot and Reddit.


As you earn reputation, you also earn moderation privileges on the site. So the site actually moderates itself, which is pretty cool.


Instead of putting all the Java programmers in one little forum and all the C++ programmers in another, we dumped everyone together and just let them tag their questions. This idea was stolen from [flickr](https://www.flickr.com/) (remember flickr?) who, I think, stole it from del.icio.us (now gone)—who knows, anyway, the point is, tags were the new hotness and made Stack Overflow work great.


Most importantly, we realized that each question is asked by one person but the answers are seen by thousands of people who found it through a search. So we decided to optimize everything to be useful for the thousands, not the individual. We literally have 1000 visitors for every person who asks a question. That’s why we sort the answers by votes. It’s also why we optimize for questions and answers that will be helpful to other people, later.


Interestingly, when Jeff and I started Stack Overflow, we didn’t really care if it was a business and we didn’t need it to be a big profitable success. We created it because the internet sucked for programmers and we needed to make it better. We thought the job listings would pay the bills, and we’d fix the internet, and that was all we cared about and it’s what motivated us to work so hard.


Of course, it turned out a lot bigger than we thought it would. The company today has 250 employees, is profitable, and has made it possible for millions of people to learn how to code and to deal with the new, super-complicated world of APIs and frameworks that we live in. But we just wanted to fix the internet.


I have met a lot of people who started businesses because they wanted to start a business. [Paul Graham calls this “Playing House.”](http://startupclass.samaltman.com/courses/lec03/) And they didn’t really care what the business did; they just wanted to “be entrepreneurs.” Which is weird, because being an entrepreneur really sucks. It’s really hard to get through all the extraordinary difficulty, pain, and stress of starting a company if you’re not super, super motivated to solve a problem for the world.


The entrepreneurs who succeed do so because it is incredibly important to them a thing exist in the world, and it does not exist, so they work like crazy until it does. When we started Stack Overflow we didn’t expect it to be a big business; we just wanted there to be someplace where developers could get help to daily problems, while showing off how smart they were helping other developers.


Ok, that’s chapter one. I’ve got a lot more to talk about. In the next installment, I’ll talk more about [how Stack Overflow’s light dusting of gamification made it really take off.](https://www.joelonsoftware.com/2018/04/13/gamification/)
