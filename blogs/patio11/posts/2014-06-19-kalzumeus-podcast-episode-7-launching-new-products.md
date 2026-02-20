---
title: "Kalzumeus Podcast Episode 7: Launching New Products"
date: 2014-06-19
url: https://www.kalzumeus.com/2014/06/19/kalzumeus-podcast-episode-7-launching-new-products/
slug: kalzumeus-podcast-episode-7-launching-new-products
word_count: 20757
---


Keith and I recorded a new episode of the podcast last year, but we didn’t get around to releasing it.


[**Patrick notes**: The transcript below has my commentary inserted like this, as usual.]


**What you’ll learn in this podcast:**

- How to pick a small, self-contained product, which is good to cut your teeth on as a dev-turned-entrepreneur.
- How Keith extracted Summit Evergreen out of his consulting work (improving infoproduct businesses).
- How to use concierge onboarding to increase conversions and decrease churn of SaaS businesses.
- That it is possible to build a very successful consultancy without being quote-unquote Internet famous.
- How to use Standard Operating Procedures documents to have employees do repetitive tasks without needing to actually automate them, while you’re still exploring for the best procedure for completing those repetitive tasks.


## If You Want To Listen To It


**MP3 Download (~115 minutes, ~85MB) **: Right-click [here](https://podcasts.kalzumeus.com/kalzumeus-7-keith-perhac.mp3) and click Save As.


**Podcast format**: either subscribe to [https://www.kalzumeus.com/category/podcasts/feed](https://www.kalzumeus.com/category/podcasts/feed) in your podcast reader of choice or you can search for Kalzumeus Podcast in the iTunes Store.


[powerpress]


## Transcript: Launching New Products


**Keith Perhac**: We’re started.


**Patrick McKenzie**: Hello everybody and welcome to…What is this? The eighth episode of the Kalzumeus Podcast. [**Patrick notes**: There was an episode #7 in recording sequence, but due to some issues, we haven’t gotten it ready yet.  It will retroactively become the 8th episode.]


**Keith**: Indeed it is.


**Patrick**: I’m Patrick McKenzie here again with my co‑host, Keith Perhac.


**Keith**: Hello, again.


## CreditCard.js: A Nice Product, Both For Customers And The Founder


**Patrick**: Let’s see, we’ve got a fun day planned ahead of us. First thing we’re going to be talking about is Creditcard.js and that’s in eponymous [creditcardjs.com](http://creditcardjs.com).


**Keith**: That’s because that came out today, I believe, on Hacker News, which will be about two weeks from when we actually get this up. [laughs]  [**Patrick notes**: Actually recorded 8+ months ago.  Sorry — life happened.]


**Patrick**: Predictably, just to give you folks an idea of what it is, it’s well executed CSS, JavaScript and HTML which does the standard static credit card form. But it does it well, such that when you start typing in a credit card number with a four, it knows that it’s a VISA and it does error correction and does the [Luhn checking](http://en.wikipedia.org/wiki/Luhn_algorithm) in real-time without having to submit it to your servers.


This is like every credit card form that you’ve ever coded in the last five years, except it’s done well without you having to work at it for three hours. It makes a very good self‑contained product, I feel. Something that can be built over the course of a few weeks, tuned to within an inch of its life, and then sold to people.


Because it’s sitting in the critical path on taking money from every website ever, it’s worth quite a bit of money relative to the amount of time I feel it would take to build, and can be sold to many people in parallel.


**Keith**: If you haven’t read the Hacker News commentary on it, or forgot about it, the community is pretty divided on it, and ironically enough, so are we.


**Patrick**: I think it’s a wonderful idea that’s going to make this guy tens of thousands of dollars, and Keith is like, “Oh, you could do that with open source in the weekend.


**Keith**: Yeah. I have to say, normally I am not on the side of open source will solve everything and I should be able to get it for free. I am more on the side of paying for it if it saves me time. This is especially apropos because I just launched my first SaaS product last Monday. This Monday, which we’ll be talking about in a little bit, I had to build the credit card form for that.


I am uniquely capable of saying, “OK, I know exactly how much time I spent in putting up my credit card.” That being said, the credit card JS right now, is $150.00 during their beta, and $250.00 after that. It’s one year of upgrades and unlimited use, is what I believe their licensing says.


**Patrick**: I think it said that the licensing is per-site.


**Patrick**: If you have 15 clients, you’re going to have 15 licenses. I think it’s rounding error next to the amount of money you typically put through a credit card form, and also next to the amount of time you’d spend in building that from scratch. I think I have probably been involved in 10 projects like that for consulting clients.


Conservatively, over those 10 projects, they have a $100,000 invested in their credit card forms.  If I could just take this off the shelf, drop it in and say, “All right, it’s going to cost a total of $1.5K and I’ll get to the more valuable AB tests” rather than having to re‑implement this from scratch every time, I would be doing that every time and all the time for consulting clients.


**Keith**: What we are talking about really is for a company or someone who does this all the time maybe it is a better investment. I actually would the opposite. If you were a consulting client, or if you are a consultant and you are doing this constantly it would be better to have your own solution instead of paying $250 for each client you install this for. If that’s billable to the client that’s something else.  [**Patrick notes**: Strongest. Possible. Disagreement.  He’s talking crazy talk.]


The reason I say this is because like I said, about a week and a half ago, I built the credit card processing on my site and I needed, essentially what this does? What this does is it makes a really pretty form and it detects the card number like Apple site does, where you put in a 42 and it automatically says, “Oh, this is a Visa” or you type 34 and it says, “It’s an American Express.”


It formats it out nicely so it’s got the spacing right, the name on the card, the expiration date, the security code that has a little about html. Here is where you find your security code, if it’s an AmEx, here’s where you find it, if it’s a Visa, et cetera.


It’s very nice. Coding it from scratch would be absolutely horrible. If you were planning on coding it from scratch I highly recommend not, and buying this instead. The problem is I use Stripe. Stripe has a lot of great open source solutions that they don’t need Stripe to be running on. One of them is I believe they call it jQuery.payment or payment.jQuery or something like that.


**Patrick**: Google it.  [**Patrick notes**: I Googled it for you.  It was, indeed, [jquery.payment](https://github.com/stripe/jquery.payment).]


**Keith**: Yeah, Google it, Stripe Payments, it’s really easy. But it has all the same functionality for the JS. It does not have the pretty form which I think is really the crux of this argument.


**Patrick**: That’s what I generally want to buy, considering pretty is not a strong suit for me. But I do tend to disagree. Stripe’s jQuery payment thing: I like it. I’ve integrated it myself. I took my nice pretty form done by a designer and then ended up integrating the javascript myself, and it’s an hour’s spent of hooking up javascript events to HTML divs and whatever with that funky dollar syntax, and it doesn’t make me any money.


**Keith**: This is true.  If you run a business, you have to do a balancing act.  It took me two hours to reproduce creditcard.js on my site. An hour of that was finding the stripe payments processing code because I had never heard of it before.


**Patrick**: This is one of these times where he’s my best friend and I want to punch him in the face because his charge out rate is $500 an hour and he’s arguing about $150 to save him two hours. [laughs]


**Keith**: But it was a good learning experience for me. That’s another thing. If I was rushed, I’m not debating whether this is a good purchase or not. Really, I’m not.


**Patrick**: A punch in the face.


**Keith**: [laughs]


**Patrick**: Shall we move on to something else?


**Keith**: Yeah, let’s move on to something else.


**Patrick**: For those of you who haven’t already got credit cards up on your site or if you feel that the user experience is not optimal and you want to try AB testing or something to see if you catch more transactions, take a look at creditcard.js.


**Keith**: I will say. I will say 100 percent I’ll stand by that. Try out creditcard.js. I would A/B test it. A/B test it against your current one, against creditcard.js. They have a 30‑day money back guarantee. If you see your sales dropping or you don’t see improvements, tell them. “Hey look. It didn’t work. It didn’t work as advertised.”


**Patrick**: As one of the two resident A/B testing gurus I can’t say I’d pop this in an A/B test right away, because how many transactions would you need to be running a month to get statistically significant data there?


**Keith**: I have clients that could do it in a week. [laughs]


**Patrick**: Well, yeah.


**Keith**: I have small clients. I have four people clients that could do it in a week.


**Patrick**: Yes, but they do run tens of thousands of transactions, right?


**Keith**: Yeah, they do.


**Patrick**: If you got tens of thousands of transactions a week, totally pop this in an AB test. If you haven’t quite gotten to the level of tens of thousands of transactions a week, just put your finger to the wind. Take a look at their landing page and say “Is this not as good as what I have currently?” If it’s not as good don’t include it.


I’ve given this advice to a lot of my A/B testing clients like so.  Earlier on in the funnel when you have high volumes and have a relatively high conversion rates like to email submissions,for example, it’s easy to just find volume to do A/B testing. But at a certain firm size, like even in the say $10 to $50 million range A/B testing the credit card form can be kind of difficult just because you don’t have the massive volume on transactions.


Typically at my companies they would be doing high value transactions. Even at $10 million that might be only a thousand through 10,000 transactions which won’t be easy just to get to statistical significance.  It will take a, emperor, era, reign, age thing.


**Patrick**: What is the English word for that?


**Keith**: Era-century? Era, I think?


**Patrick**: No, like 平成、is what?  [**Patrick notes**: Sorry if you don’t understand Japanese because this part of the conversation will be pretty unintelligible but *we* know what we’re talking about.]


**Keith**: About 25 years right now?


**Patrick**: Yeah, I know that. Heisei is an example of what? I keep coming back to the words “imperial reign…”


**Keith**: Imperial era.


**Patrick**: Imperial era, that’s right. This is how we count years in Japan by the way. What emperor is reigning during the relative period of time and how many years. But, yeah, you won’t achieve statistical significance before we have a new emperor and every Japanese company has to update every payment form. That’s going to be a lot of fun work.


**Keith**: That’s a lot of chances for business.


**Patrick**: Apropos of nothing, a world created by programmers would have no dates, time zones, imperial reign things, all of it…


**Keith**: Or sales tax.


**Patrick**: Sales tax. These things just like burning with fire. Why did we ever come up with this [laughs] ?


**Keith**: It’s going to be interesting because as you know, next year our sales tax goes from five percent to eight percent. It’s an increase of three points. There’s a Japanese law that all prices have to written with sales tax included. Every single sign in the country will have to be reprinted.


Then one year later they’re going to be raising it to 10 percent and we’ll need to rewrite every sign again. [laughs] We said we weren’t going to get in on that.


## Keith Discusses Summit Evergreen, His New Product


**Patrick**: Launch?


**Keith**: I’ve launched my first SaaS. Going well! It’s [Summit Evergreen](http://summitevergreen.com).


**Patrick**: You should give people the elevator pitch because I don’t think that you talked about it all that much on this podcast yet.


**Keith**: We have not. As you know I do consulting for a lot of clients. A lot of my clients are info‑product people. What is the name for the product? I can see you cringing right now behind your glasses or…


**Keith**: What do you prefer as the name?


**Patrick**: Productized consulting or even sometimes I refer to the form factor, like the e‑book or video courses. Anything sounds better to me than info product because info product pushes my Internet marketing neuroreceptors and they are not happy neuroreceptors.


**Keith**: I hate the word e‑book with a burning passion, so let’s do video course.


**Patrick**: OK, a video course.


**Keith**: Patrick put out his [Lifecycle Email course](https://training.kalzumeus.com/lifecycle-emails) which is amazing if you haven’t checked it out. I am completely unbiased in that. I do a lot of consulting for clients who do video courses or just pure text courses, mainly video. One of the things that is difficult to do, especially with a video course, is to provide value over a length of time. You can say, “Here’s my course.” They get it all. It’s like, “I paid $500 for this and it was done in a day and now I don’t know what I got for that $500. I have a lot of content, but I am not led through it.”


The idea is that you take your content, you have your video course, and it’s a real *course*. When you go to a community college, they don’t just give you all the books and say, “All right, we’re done.” It’s this back and forth between the teacher, the content, and you. It’s doled out over time. I think that’s one of the key parts of a video course. It’s the same as your Lifecycle Email course is that it’s doled out over time. It’s not, “Here’s everything. Go at it.” It’s first we do this and then let’s build on it.


**Patrick**: One of the problems with critically hitting people with a wall of case, or dropping five hours of video on somebody on one day, if you actually look at the analytics for who’s successfully watches and takes action on it. (Ultimately the goal for both parties on it is them taking action on it.)


As a gateway to them taking action on it, they need to actually watch the lesson. A lot of people watch the first hour. Less people watch the second hour. It trails off. The fifth hour, five to ten percent of the people who bought my course, actually watched the fifth hour, which is sort of unfortunate.


**Keith**: Another thing that I noticed when you have the entire course, interestingly enough I got access to the Lifecycle Email course all at once because Patrick was nice enough to skip me forward. [**Patrick notes**: Keith thinks that my course was dripped out to customers, but he’s not actually correct.  It was all delivered at once.] One of the issues with it is that you tend to skip the things you think you already know.


It’s like, “Oh, I already know how to write a welcome email. I’m just going to skip that part.” That has a detrimental effect on both the customers feeling towards the course as well as their understanding of the course. Especially, if you build off things that you might have skipped, then they’re going to feel lost. That’s going to turn into churn.


**Patrick**: We might need to explain what churn means in this context. Just going back on for a second on that one, as a teacher and someone who has done one of these products before, sometimes a video that says on the tin that teaches you something you think you already might know might have a tactical implementation tips might have has wildly disparate value that people don’t always realize are there.


For example, I had consulting clients who are already sending dunning emails. Dunning emails are just emails which tell folks that they owe you money and attempt to collect it.  I won’t tell you the whole spiel now. There are good ways to write down done‑in emails. and there are bad ways to write done‑in emails.


There are a lot of clients or a lot of companies that sell SASS or some product that gets billed every month, will send out a done‑in email like, “You’re credit card failed, please update.” That will be the entire text of the email. There are better ways to do that which get higher rates of audience compliance. If you get customers to comply with the instructions to pay you money that’s worth staggering amounts of money on scale.


**Keith**: Yeah, exactly.


**Patrick**: People might skip that video because they think they’ve already implemented dunning emails. They think: “How hard is the dunning email? It is two sentences long.”  I have had consulting clients where I was in the building able to direct them through re‑implementing that and made them five or six figures for thirty minutes work on their emails. That’s unfortunate.


Back two steps, you mentioned that it helps decrease churn when you increase people’s perception of value and get them to consume more of the content that was in the video course. What do you mean by churn in that context? I think a lot of people are coming from it, “Wait. The business model is a one‑off sale. We don’t have churn in a one‑off sale.”


## A Brief Note On The Challenges Of Infoproducts In Some Markets


[**Patrick notes**: Keith has extensive experience working with clients who sell B2C infoproducts in particular markets where, by nature of the type of customer, many customers experience buyer’s remorse and attempt to cancel the purchase.  The following discussion is not quite so relevant if you e.g. sell books on Rails development or software.]


**Keith**: That’s a little dirty secret of “video course.” I put it in quotes, because you know what I wanted to say. At any sale on the Internet. A one‑time sale is not a one‑time sale as long as that a credit card was used for the purchase. The reason for that is, first of all, most video courses have a refund policy.


If people are not happy within that refund policy, say that’s thirty days, then they will refund. That’s what I mean by churn. In a refund, you’re losing money. You already gave out the course, they don’t like it. They’re refunding. Then you say, “Oh, I just won’t let them refund.” That causes another big issue which is…


**Patrick**: That’s something you never, ever, ever want to do.


**Keith**: Which is charge backs. OK, so the credit card company, how many days is a charge back now a days? 30 days?


**Patrick**: 180 days, Keith.


**Keith**: 180 all right. For 180 days after someone has purchased your product, they can go to their credit company and say, “I didn’t like this. I want a refund. It wasn’t me.”


**Patrick**: Anything that merchant did not live up to their claims on the website. You will almost invariably lose that charge back.


**Keith**: You will indeed. That charge back will not only take your money and they will charge you a hefty fee on top of that for trying to take someone’s money.


**Patrick**: I almost had one of these for the Bingo Card Creator. They’re annoying. It’s a cost of doing business. I understand this happens once or twice a year for reasons which are only somewhat in my control. You get the $30 for the product back. I just got assessed a $15 fee from the bank.


**Keith**: That $15 is from Stripe who is nice about it. Other processors will have $25 to up to $100.


**Patrick**: Yep, because it’s largely a manual process for chargebacks. They are not handled through APIs like Stripe is.


**Keith**: You want a refund policy. You don’t want to piss off your customers because they will hurt you more than it costs you to give them the free product. That’s what I mean by churn. You want people to be happy. You want people to find value from your product. Not only because you want to help people, which you should do, but also because it will financially hurt people if they are not happy with it.


**Patrick**: I should note that the base rate of refunds is wildly disparate depending on what the audience for the product is. For example, in the B2B case, refunds are very rare both for video courses, SaaS, virtually anything you sell to businesses. The refund rates are scandalously low. I think I had on order 250 sales of my course, and two refunds.


One of which they refunded so that they could buy the more expensive version instead, so net one refund. A baseline B2C rate of refunds, let’s see. Bingo Card Creator has a very high refund rate because I am very aggressive about offering customers refund to solve customer service issues. That’s on the order of 2.4 per cent in most years. Higher this year due to a PayPal fraud ring.


**Keith**: Video courses…Didn’t you have a higher one?


**Patrick**: Yeah. Especially as you get closer and closer into the dun-dun-dun Internet marketing space, the refund rates approach like the double digits range where if you are getting close to that, something is wrong.


**Keith**: Yeah. I think refunds are the dirty little secret. No one ever thinks about that when they are creating their product. “Oh I made a million dollars in sales this year.” Well, fifteen percent refunded. That is 15 percent of your revenue gone. [**Patrick notes**: Again, in most industries relevant to you guys, if you have a 15% refund rate that’s a four alarm emergency for the business. This should never, ever, ever happen to you.]  You really have to care for your users. Going back to the topic at hand, that’s what a dripped course does and a dripped course.


A dripped course is a course that’s doled out over time from the time that the person purchases. This is a very common thing in video courses and what not. The problem is that there’s no real software that supports this right out of the box. Most people either build their own solution like Patrick did.


**Patrick**: Don’t do that by the way.


**Keith**: It’s really a pain in the ass honestly. The other thing is to do a launch and then drip it out manually, which is what they do when you use WordPress or what not. Essentially what happens is, on launch day, you say everyone’s buying on this day. Then, for the next, at the beginning of the week, I am going to launch the next week of content.


The problem with this is you can only do that once. If you want to sell it again, you got to do it again. What people end up doing is they make an e‑book, because e‑books are very easy to evergreen.  [**Patrick notes**: Keith is here using evergreen as a verb to mean “To sell in an ongoing fashion rather than as a one-off sales event.”  Think more like selling books and less like selling movie tickets, although it is actually the case that sales for most books are, like movie tickets, highly front-loaded.  Still, in general, you can sell books outside of the “new release” window and its attendant publicity, but this doesn’t happen to movie tickets.] They are very easy to make once and sell to everyone.


**Keith**: This is one of the interesting conversations that I had a multiple times on hacker news as well. How much do you consider an e‑book to be worth?


**Patrick**: I think that varies wildly depending on what’s in the e‑book. Let’s say hypothetically that e‑book is being sold to businesses and has something that will eventually increase their revenue or reduce their costs.


**Keith**: Let’s talk the highest cost an e‑book could probably get you for a business as a downloadable pdf.


**Patrick**: OK as a download a book pdf, I think you could definitely do things like Nathan Barry had done with higher tiers.


**Keith**: He puts things together with the e‑book.


**Patrick**: Just a flat downloaded pdf. I’m thinking somewhere in the $49 to $99 range.


**Keith**: Yeah exactly. How much is your life cycle email course?


**Patrick**: $497 or something rounded to $500.


**Keith**: Yeah. Do you think you could have sold that as e‑book for $500?


**Patrick**: I think it would be very difficult to convince people that it was worth $500 as an e‑book.


**Keith**: Actually, I do this with my consulting clients as well because many of them do the e‑books because it’s very easy to evergreen. They launch once and they forevermore say, go to my site, my shopping cart page, buy the e‑book, and then you’ll have it. Then they’re like and that’s worth $50‑$60. The problem is that’s worth $50‑$60, that’s great. You’re not going to sell a $2,000 or a $3,000, or even a $500 e‑book like that.


You can take similar content, add video, add downloads, add all these other extra things in there and drip it out over time to make it more valuable. That’s what the course does. That’s what my system does, Summit Evergreen.


Let’s you do is take your video course, take your audio course, take your written course, take your download, take your feedback, and drip it out over time in an evergreen fashion. Based on whenever a person purchases, they run through the whole course. Just like the course that Patrick wrote from scratch. How many months did that take you to build your courseware?


**Patrick**: I think it was, I want to say, two weeks. That’s like an engineer’s two weeks, so it’s probably really four weeks.


**Keith**: Four weeks?


**Patrick**: Yeah.


**Keith**: As a very good engineer, with the framework, and you would have done processing with Stripe before. You knew how to hook up their API. You used a lot of code from other places, yeah?


**Patrick**: Copy/pasted in the entire user model from Bingo Card Creator.


**Keith**: [laughs] So we’re really talking, if you have all the modules and everything, great, very easy to set up, four weeks of engineering time.


**Patrick**: It’s easily in the five figures of engineering time.


**Keith**: It’s a large project.


**Patrick**: That’s often a cash cost for a lot of Keith’s customers because these people who do training on the Internet do not necessarily have Ruby on Rails developers just flowing out of their ears. When Keith’s clients come to Keith, they pay Keith cash money to set up systems to sell this.


**Keith**: That’s one of the things that we’ve been doing. We’ve looked at the ways that people have marketed their video courses, ways that people need to look at their video courses, and not only the data. Patrick you say that you only have 250 customers.


I say “only” not with any derision, but with love. I have some clients that have 10,000, 20,000, 30,000 users running through theirs. What do you have for user analytics. Do you have anything?


**Patrick**: Nothing.


**Keith**: Exactly, you are not alone in this, this is another one of those dirty little secret like refunds. Once people buy the course, are they using it? Even if they don’t run a refund, did they use it? What did they like? What did they not like? What should I do for my next course?


**Patrick**: I’ve done ad hoc surveys after they bought it. Talked to them individually, and there’s a page I can go to in Wistia which will showhow many people watched a particular video, and if I do the math there at, I could figure x over 250 equals over 25 percent of the people or only 10 percent of the people watch this video so question mark.


I supposed that could tell me something. I haven’t spent any time or built any analytics software to help me do that in a more systematized manner.


**Keith**: I think that’s really important because you can learn a lot from not only are people watching but who’s watching it. We’ve done dives into our analytics. This is basis of what the software we built. OK, let’s look at people who are refunding. We’ve found out that 70 percent of the people who listed their occupation as “education” refunded. Now we have a…


**Patrick**: What are you proving? That teachers are terrible, terrible market?


**Keith**: [laughs] If only me had created some Bingo cards or something for middle aged teachers in the Midwest.


**Patrick**: If there’s anyone on this podcast who does not yet understand it, *do not go after the education market*. Please, save yourself a lot of time and pain.


**Keith**: [laughs] What I was saying with that was now we have a flag. Now, that customer has a flag. That client has a flag to know when an educational customer gets within that refund period, at about that three week market, they should send extra support emails. They have a little flag that says send an extra support email that says, “Hey is there anything that we can help you with?” That helps in reducing refunds a ton.


**Patrick**: I really love this mid-touch idea where it’s not high touch like an enterprise sales process where your first contact with the company is, “OK, I’m going to give the sales guy my phone number. He’s going to call me, invite me out to a steak dinner, and then attempt to sell me a $750,000 solution.”


It’s not low touch like Bingo Card Creator where my idealized interaction with the costumer is never talk to them at all. They just deal with the website and email, “Give me $25.95″ and I never learn their names.


Somewhere in the middle where customers are sufficiently engaged with the product or they’re savvy enough or whatever the combination of things is. They can get all the value out of the product without even needing me to touch, talk to you. That’s fine. They can do it. Then, there’s customers who might need a little prodding or handholding, can be offered that prodding or handholding, but at scale and at such manner it doesn’t require basically one to one use of the company’s time and the customer’s time.


## Concierge Onboarding


**Keith**: This was a key word that we brought up a lot. I am going to skip ahead one and then come back to one. Patrick and I went to MicroConf Prague, or MicroConf Europe in Prague, what three weeks ago?


**Patrick**: Yeah.


**Keith**: What was one of the key words there that we keep saying?


**Patrick**: “Concierge onboarding.”


**Keith**: Concierge onboarding.


**Patrick**: OK, concierge is probably one of the most important word that I’ve learned or has come into fashion in the last year or so for selling software on the Internet. Mind if I take concierge for a little bit? Back in the olden days, where it was just high-touch sales and enterprises selling things to other enterprises for $100,000 and there was a sales guy involved, and steak dinners and fancy bottles of wine preceded invoices.


There was this thing that was called “professional services.”Professional service was basically consulting that you had to use to get the software to be in some state and functionality, but the company was very rarely interested in consulting as a profit center. It was you would sell someone $20,000 of consulting to enable an $80,000 license sale of software.


Concierge onboarding is taking the core of that idea and applying it to the SaaS model. Instead of $100,000 licenses, it’s $50 to $500 per month. What concierge onboarding is rather than someone coming to your website and saying “I want the Small Business plan. It costs $80/month. I interact with their automated onboarding process.


Click, click, click, I interact with their automated onboard email sequence. Click, click, click the thing, never talk to anybody, OK it’s thirty days later and I pay my $80 on my credit card.”


**Keith**: If you’re lucky.


**Patrick**: Yeah, if you’re lucky. Twenty five percent of them if you’re very, very good at it will pay the $80 on the credit card.


You affirmatively get in touch with somebody that is a prospect for your service. They’re a lead or a trial. They just signed up for the service. You say, “Hey. There’s some configuration or data import or learning curve associated to getting up and running on this. We want you to grease the skids, grease wheels, of that onboarding process for you.


For example, if it is an analytics product, you’re going to have paste some JavaScript into your website.  You might not be technical and that might be difficult for you. Tell you what, I will log into your website and do the copy pasting for you. You tell me your FTP username and password. I will get it done.”


In my case, Appointment Reminder  often  requires importing somebody’s contact data base into the appointment reminder system. There’s actually isn’t a system that takes an arbitrary data dump from any arbitrary patient or contact management system, converts it into an Excel file, and allows you to see arbitrary columns and import them into the data base.


Just tell people, “Look, get me any data file in any format that you can come up with, send it to me via email, I will figure out how to proxy it and import it into the system for you.”


On the assumption, that has been proven out in data, by the way, that OK, if someone comes in the door and says, “I want a $200 account.” Twenty five percent of them are going to actually convert into paying $200 a month and that’s happy. Seventy five percent of them who have their data imported into the system will actually convert into paying $200 a month.


That adds literally thousands of dollars to the lifetime value to move someone from the 25 percent chance of conversion to the 75 percent chance of conversion via importing.


**Keith**: Since there’s not that many people doing concierge right now. Once you have your data somewhere, it’s very hard to move out.


**Patrick**: Right, right. You don’t even have to use any Microsoft nastiness to make it difficult to get people’s data out of the system, you can just let friction work.


**Keith**: Right. [sarcasm]You can export all of your Google data, all your Facebook data to a nice, easy‑to‑understand Excel document. Then what the F are you going to do with that?[/sarcasm]


**Patrick**: If anybody ever wanted to leave the Appointment Reminder platform, I would be so happy to export them an Excel file of all the data they have in the system. Since nobody’s going to import that for them to free, that’s not really a competitive risk for me.


**Keith**: Right, exactly. The people who are going to import that for free are people who are directly your competitors.


**Patrick**: Or, to phrase it the other way, if someone gets their data from one of the competing appointment reminder platforms or one of the complimentary patient management platforms I will be happy to walk over any sort of engineering issue to get that data into my system just to make it easy for them to get up and running.


**Keith**: Exactly, exactly. Remember, your competition is not just your competition. You’re their competition. The better services you can get in getting their data into your system, the better you are.


**Patrick**: I feel like we’re kind of rat‑holing on that import thing.  Back to concierge on‑boarding. I’ve seen companies that have successfully implemented it across their entire range of accounts.


One thing you can do just to get a baseline for how much that’s is going to cost you in terms of founder time or customer support team time or customer success advocate time or whatever you want to call it.  Offer for a week to a small selection of people who are on the higher value plans.


“We saw you signed up for the higher value plan.”  Don’t actually call it that. “Thanks for signing up for the office plan of the software. As a special benefit to you, I’d like to make it as easy as possible for you to get up and running. Why don’t we spend an hour on Skype to walk you through it?” That’s what Brandon Dunn does.


“Or can I help you with the data import? Just send me the stuff I’ll take care of it.” You do that five times, 10 times, figure out what your average cost of doing it is, and then run the numbers. What percent increase in conversion or percent decrease in churn rate do you need to justify doing that for all the customers on the higher tier plans?


You can offer it as an explicit benefit on the pricing page. Let’s say Appointment Reminder is priced based on how many appointments you use per month, and it’s the primary axis of segmentation between customer types. You’ve got to figure that some of the doctors who are on the $29 a month plan would be happy to pay more money if it was less painful for them to use.


Importing things manually by retyping is painful. I might say, “If you’re on a plan at least one level higher like the $79 plan we’ll take care of that importing stuff for you.” The doctor might say, “I only run enough appointments a month to do the $29 plan, but I’ll bump up to the $79 plan and not have to have my office manager lose her fingers retyping our customer data.”


That gets $50 a month times average customer lifetime of two years. That’s an extra $1,000 in my pocket just for offering what is, from my perspective, perhaps 15 to 20 minutes of scripting.


**Keith**: Same with Summit Evergreen. We’re concierge on‑boarding everyone, especially in the first trial, right now. Most of the people who are starting off at this not only didn’t have an idea, they already have a product somewhere. They have it on WordPress, they have it on…who else is really big right now?


They write their own systems, et cetera. I have a lot of people who have all their data in GitHub and Markdown and they process it themselves. We’ll say, “We’ll take your data, we import it into the database. You have a theme? We’ll help you convert your theme and import it into the system, and you’re up and running in a couple of days.”


Once you’re up and running, it’s so much easier to stay in that system, and it’s so much easier to get what you want to do done instead of spending all your time, like you say, wearing your fingers down to the bone reproducing what you already have.


**Patrick**: This is something that’s really important for basically any system where you’re trying to convince someone from moving off a working system they already have. Eventually, I think Keith will be moving into building this sort of system or selling this sort of system to people who it’s their first rodeo at the products on the Internet thing.


People who, in general, for selling business tools, the people who are easiest to convince to start using something and who have the highest budgets for it are not people who it’s their first rodeo. [**Patrick notes**: This is important, guys!] They already have a working system. It has some sort of disadvantage associated with it.


You convince them to move to your system, and then start charging them money for it and learning what your system needs to do to grow into the other under‑served segments of the audience.


Great example of that: Rob Walling recently launched [Drip](http://getdrip.com), which is a life cycle email/drip marketing management tool. I’ve been building drip marketing systems for years. Many of my clients would be on something like MailChimp. There’s pluses and minuses for using MailChimp for drip marketing. We’ll just leave that out there.


If you go to a J. Random Client and say, “You should switch to this new guy’s system,” all of them are going to tell you, “We have something that kind of works right now. We might have a bit of dissatisfaction with it, but it cost us $10,000 to get it up and running the first time and, honestly, nobody here has enough time to spend a week rewriting it for your tool.”


What Rob Walling will do is say, “If you will point us at a series of blog posts or an existing email campaign, we will screen‑scrape with our eyeballs everything out of that, get it up and running in our system, and then all you have to do is turn the key on your site. Re‑target your form from submit to MailChimp to submit to the Drip thing. Then, boom, you’re live on us. No work required on your part, hardly.”


Then the inertia works in his favor rather than working against him. “I’m up and running on Drip now, why would I use anything else?”


**Keith**: Pains of changing are really things you cannot discount. Once someone’s on something, the inertia to stay on that system is very strong. Even if you have overcome that inertia to we’re going to switch to the new system and there’s a bump on the road then the whole thing can come crumbling down.


We’re actually on MailChimp right now. Love MailChimp. We have more experience with AWeber. We’re going to move our [**Patrick notes**: heavily NDAed] number of people from MailChimp over into AWeber, and they have a nice import feature. We decided before we move everyone over we’re going to test this once. Good thing we did because it will send a confirm email to every single person on that list that has already opted in.


They have to reconfirm their email address to get into AWeber. We were all ready, we bought the account, we had everything. At that point, we were like this is a bump. We could probably call support and deal with it, but MailChimp is good. They’ve treated us well. We’ll just stay with that.


**Patrick**: That’s not just a bump, by the way.


**Keith**: That’s a pretty big bump. [laughs]


**Patrick**: I have an idea of what client he’s talking about.


**Keith**: No, it was me.


**Patrick**: That was you?


**Keith**: That was Summit Evergreen, yeah.


**Patrick**: Figure if you ask for a reconfirmation, unless your list is incredibly hanging on your every word, you’re probably going to lose between 60 and 80 percent of them.


**Keith**: Oh God, that’s a low‑ball.


**Patrick**: I think *I* would lose 60 percent on my list if I asked them to reconfirm their email addresses today given that about 50 percent of them open every email. I might get 80 percent compliance on the yes, I want to continue getting email from you.  [**Patrick notes**: 40% is thus calculated via Bayes theorem, which is a college-level way to say “3rd grade multiplication.”]


Not to brag, but I think I have higher than the average emailer kind of loyalty for my list.


**Keith**: On the other hand, it’s not just loyalty. You’ve already been on a list. This is kind of going rat‑hole, but I just want to say this really quick. You’ve been on a list and they send you a reconfirm. First of all, you think maybe this is spam. Maybe you just trash it. Maybe you don’t open it. Maybe you email Patrick and say, “Hey, I got a reconfirm,” which I’ve gotten before.


I’ve had people email me that have been moved over to a new list and said, “Hey, I’m already confirmed, but I’m getting a reconfirm. Apparently someone’s trying to spam me from your address.” You just created so many support handles and support issues.


**Patrick**: It’s possible that someone has affirmatively moved your email from Google’s new promotions tab into their main inbox because they want to see it every time, but the reconfirm notice goes into the promotions tab and they don’t see that and suddenly they don’t get an email anymore. There’s just lots and lots of issues.


That’s one of the reasons why email marketing tends towards stasis. After you have a system that’s working, you don’t want to nudge it. Sort of like doing a DevOps.


**Keith**: Oh, God, yes.


**Patrick**: If you’ve ever gotten a particular version of Ubuntu running on your server, never upgrade it ever.


**Keith**: There’s a reason that I still have sites running on Slicehost generation one servers now owned by Rackspace…


**Patrick**: Obviously, you have to update your kernel everyone once in a while or there are going to be security vulnerabilities, and I understand that. I Just know, the last time I did the kernel update on Rackspace I had six and a half hours of downtime.


**Keith**: Exactly. I think that’s good about concierge servicing.


**Patrick**: That’s concierge stuff. Concierge is a tactic Keith is using for Summit Evergreen. Let’s talk a little bit more about that topic because there’s some interesting things that people who are doing their first SaaS business might benefit from.


Customer development is a catch‑word in the industry. I like Keith’s thing here for doing customer development. Basically, Summit Evergreen is an extraction out of his wildly successful consulting practice.


It’s not like the typical thing where I think I’m going to make schedule management for massage therapists, and I have not ever run a massage therapy business or whatnot so I don’t know if there’s a market for that yet.


In customer development, hopefully you would go out to the massage therapists and ask, “What do you use for schedule management? Do you have a burning schedule management problem in your business?” prior to building a solution and attempting to sell it to them.


Otherwise, you’re going to find that you make a solution that targets a problem that nobody has. Keith knows people who had businesses who sell meaningful amounts of money on these online courses have problems with the online course management.


They paid him previously ***meaningful amounts of money***. Like meaningful amounts of money in a consulting sense rather than a $50 to $200 a month sense ‑‑ to solve these problems.


Are you comfortable saying what an average invoice is for somebody, one of the clients doing this?


**Keith**: I am, unfortunately, not.


**Patrick**: Let me pick a number out of thin air from my consulting experience as a ballpark number for having a high‑level consultant work for your business. Let’s say it’s $40,000 a project. If you have a successful consulting practice and you’ve been selling some certain segment of business, $40,000 services to get that aspect of their business better, then you know there must be someone who has at least enough burning desire to fix that problem such that they’re willing to pay for a software as a service offering if that software as a service offering is some percentage as good as having your expertise in the business for one week or two weeks or however you schedule your consulting engagement.


It’s highly unlikely that Keith is going to go to market now with Summit Evergreen, which is priced at whatever.


## Tiered Pricing For SaaS and Infoproducts


**Keith**: Starting at 99.


**Patrick**: Starting at 99. What’s your pricing model for this?


**Keith**: 99, 250, and 500, I believe.


**Patrick**: What’s the pricing axis for that?


**Keith**: How do you mean?


**Patrick**: What determines whether I pay $99 or I pay $500, aside from the names of the plans? Naming plans are really, really important.


**Keith**: It’s all the names of the plan. No, I’m kidding. [laughs]


**Patrick**: I’ve honestly seen companies like that. No lie, guys. Seriously just putting the name “Enterprise” on something makes it more valuable than having the name “Hobbyist.” Can I tell my anecdote that I always tell about this?


**Keith**: Please.


**Patrick**: When I was working at a Japanese company, we needed to use Crazy Egg for something. Crazy Egg, shows you where you’re clicking on the website or where your customers are clicking on the website. I was the engineer in charge of this project. I ran the numbers.


We needed the hobbyist plan of Crazy Egg for nine dollars a month. I submitted an expense authorization form to my boss saying we needed the hobbyist version of Crazy Egg. It’s nine dollars a month which is about 1,000 yen.


My boss opens up the Crazy Egg page, scratches out hobbyist, writes enterprise, scratches out nine dollars, writes down $500 or whatever the equivalent in yen is, returns the form to me for re‑authorization so he can send it to his boss.


I said, “Boss, boss! We don’t need to spend $500 a month. We only need to spend nine. I’ve run the numbers. I’m very sure that we’ll have plenty of headroom under that.”


He says, “F if I’m going to my superior with the word ‘hobbyist’ on it.” It was worth $490 extra a month just to save face for an interaction between two people at this company which would have been over in less than five seconds.


**Keith**: This is one of the core marketing concepts that, surprisingly, a lot of people doing video courses do not get which is **tiered pricing**.


**Patrick**: SaaS companies don’t get this either, by the way.


**Keith**: It’s amazing. It’s absolutely amazing. At any pricing point, there is someone who will or will not pay it based on that. The idea is that you have a price point for whatever someone is willing to pay. If they’re only willing to pay $100, you have a $100 plan.


This, of course, you don’t want to have a five dollar plan. If someone is willing to pay $500 to $1,000 you better have a plan for them. Otherwise, they’re going to be on that $50 plan and you’re going to be out $900.


**Patrick**: Right. In the economics literature, there’s words for this kind of stuff that we’re just beating around the bush here. “Customer surplus” is the difference between what someone is willing to pay and what you actually make them pay.


Let’s say the value to my business of adopting this technology would be $1,000 so I’m willing to pay up to $1,000 to adopt that. Let’s say it’s $2,000. I have a 50 percent discount rate. I’m willing to pay up to $1,000. You charge me 50. That means I just received $950 in customer surplus from you.


One tactic to capture the customer surplus is called price discrimination — charging people different prices. Price discrimination in the classical market is sort of difficult because you have to offer…this isn’t a legal requirement or anything. Just operationally, it’s difficult to offer people the same product at different prices in such a way that you can maximally discriminate on their propensity.


SaaS does that by doing the nice, traditional, three to five column SaaS pricing tier thing and thinking really, really carefully about what’s in those three to five columns. Knock on wood, aspirationally, you think really, really carefully. The actual practice of a lot of SaaS companies is what a junior engineer threw up three years ago and no one’s touched.


**Keith**: This is really sad.


**Patrick**: On the plus side, if you ever work in a SaaS company, take a look at that pricing page. Do one to two days of really deep thinking. Every element on that page is should get asked: “Whose perception of the pricing offering is it supposed to modify and how?” Make a new version and test it. *You can often add 25 percent plus to the enterprise value of the company for two days of work.*


BTW, there are a lot of people who charge a lot of money for pricing advice just because the leverage on it is absolutely astounding.


**Keith**: If you improve someone’s pricing page and they improve their end of year sales that’s worth however much money they made that year because they’ll make it again next year and the year after that.


**Patrick**: It’s not just the bottom line. The leverage doesn’t extend just to the bottom line, it’s to the enterprise value of the company. [**Patrick notes**: If your company is valued at, say, 5X sales, and a change to the pricing page causes sales to go from $40 million to $50 million, that change isn’t worth $10 million, it is worth $50 million.  Or at least that’s the number to claim if you’re a consultant trying to justify your rates.] It’s absolutely insane.


**Keith**: Which is why, actually, our tiers…you asked what our axis is. Our main axis is the number of customers. Since it’s Evergreen, it’s not the overall number of customers, it’s customer per month. If you got 200 new customers this month then you will probably want to buy this tier. If you’re expecting 500 new customers a month, you’ll want this tier, et cetera.


**Patrick**: This is one of the good patterns for both SaaS pricing and info product, video course pricing, too. Align the price with customer success. It’s one of the reasons people like micro metering models. I generally hate micro metering models for pricing most things, unless it’s basically a purely transactional thing like PayPal or Stripe or whatever where you’re getting a percentage of every transaction.


The one good thing that you can say about those is that they scale pretty directly with customer success. If someone sells $100,000 of stuff through Stripe they pay $3,000 or whatever in Stripe fees. If they sell a million dollars it goes up to 30,000. Stripe captures some percentage of the upside is their business grows and becomes more successful based on the Stripe platform.


Sometimes, SaaS are priced in a way that does not necessarily align them with customer success. That’s often unfortunate. As an example, I don’t know if they would appreciate me telling the name of it but there was a company I was involved with, and they sell to developers. One of their pricing axes was how many repositories we have.


The count of repositories in your organization is a very imperfect proxy for your business success. I don’t know if this is actually true, but the word on the street is that Google has exactly one repository stored in Perforce or something ‑‑ one repository across an organization that makes like $100 billion a year.


There’s a lot of two-man Ruby on Rails consultancies that have 100 repositories just because Ruby on Rails and the Git model encourages you to have a repository for everything you do.


If you’re thinking of charging J. Random Two Person Ruby on Rails consultancy orders of magnitude more than you would charge at Google for a product that is approximately the same value proposition, your pricing might need a little tweaking.


**Keith**: This is one of the advantages, I think, that Bit Bucket has over GitHub because GitHub, for their private repositories, does what you’re saying. I’m almost positive you’re not referring to GitHub in that.


**Patrick**: No.


**Keith**: They do, do that. They’re competitive pricing. You get five private repos for five dollars or something. It’s nothing. Like you said, I have 50 repos sitting around, and I want them private because either they’re client stuff or they’re small things. I hope that’s a yawn and not you viewing me in disgust. Good. [laughs]


That’s one of the things I like about Bit Bucket. Bit Bucket’s pricing model for private repos is not on the number of repos, it’s the number of contributors you have to that repo. If you were doing a project where it’s just you then, yeah, it’s just free storage.


If you’re doing any business and you have more than 5 to 10 people in a repo, then they’re going to charge you for it.


**Patrick**: I really like scaling on team size because team size, again, it’s a imperfect approximation for the value received from a given product. It’s a really good approximation of ability to pay simply because somebody who has 10 employees in the company, no matter what their job title is, no matter what their salary is, if they have 10 employees then the company must be spending at least $20,000 a month on something.


Therefore, kicking your price up from $50 to $250, no needle at the company, changes as a result of that.  But when you 5X your prices it very much makes a difference at *your* company. I don’t even think it’s on our pricing page, but Appointment Reminder will kick you in from the $29.00 bucket to the $200.00 bucket if you have. I don’t know what the number is off the top of my head ‑‑ it’s like three employees or five employees or what not.


I’ve never had a single complaint about that.


**Keith**: And Atlassian is great, because that’s their whole marketing for the on demand service, and their normal service. They have the 10 for 10. Ten dollars a month for any product for up to 10 users. It’s great for small companies. I have exactly 10 people, actually, working for me. I have 10 people. I have six or seven of their products now, so I’m not paying $10.00 unfortunately.


As my business grows, as I get more people in my business, and I have the money to pay their salary, of course I’m going to move to the next level in Atlassian. Because first of all, they’ve been really good to me up until now. Second of all, all my data for the last five years is in there.


I’m not going to move to Red Mine, or what not, and move five years of customer data, and everything into that new system.


**Patrick**: It’s funny because I assume that Atlassian probably has an export feature, and…


**Keith**: Oh yes they do. Very good.


**Patrick**: …They don’t try to lock you in, or anything. It’s just the nature of all businesses. Like we were talking earlier, after you have a working system that impetus is in favor of working in things that actually matter in the business, and not twiddling around with trying to move to a different software solution, and save, what is from the business perspective, a minuscule amount of money.


**Keith**: The pain point has to be very high before you are willing to switch over. Actually I did just switch over one of my systems, which we’ll talk about in a bit if we have time.


**Patrick**: By the way, for those of you who are thinking of doing a SaaS right now, so if you’re going to follow our advice, and target a SaaS that is targeted to business, or launch a SaaS that is targeted to businesses, that last bit we just said about there are huge switching costs involved in doing anything, so if there isn’t a lot of pain you wouldn’t do the switch should inform your idea of what should make for a SaaS.


If you are talking to potential customers, and the idea, the pain point that you’re going to target is not one of the top two most pressing issues in their life right now, don’t do that. _Do one of the top two things. _As a business, I’m a very busy guy. I have run four products. I have thousands of customers and off ‑ag0ain employees. Things are going on. And I have way, way too little time to deal with it all.


If you’re not on my top two issue list, I’m not going to buy your thing. I could tell you, “Oh, that’s nice. It sounds like a great idea. The UI is beautiful. I love it. I might even implement it someday when I get a moment.” But the truth is, I never get a moment. I very rarely have time to get things that are lower on the priority stacks than the top two things.


So if you were trying to sell to me or to the generalized class of small business owners who I kind of represent, sell solutions to the top two problems. I wonder what my top two problems are.


**Keith**: I can tell you right off the top of my head what mine are ‑‑ billing and product management.


**Patrick**: Mine are probably getting more customers at scale for Appointment Reminder.


**Keith**: [laughs]


**Patrick**: Seriously. **Someone out there will eventually crack the Da Vinci code of getting scalable customer acquisition for SaaS businesses. And that person is going to be a billionaire.**


**Keith**: This is another thing. So you say your top two. Let’s take me for example, with my billing and project management, and top two pain points. Those are my top two. However, if someone had a SaaS and it’s like scalably increase your business, then that would be number one, right there.


**Patrick**: To the magic money wand. Please wave the magic money wand for me.


**Keith**: Exactly. If there is something that I can pay money to, and the return on actual money is greater than the amount of money I am paying, then it’s a no‑brainer. I think we had this conversation one time. Maybe it was just you and me.


We were talking about the price of accountants, and there was a very expensive accountant that we were talking about, and it saved someone a very large amount of money ‑‑ about 20K. Let’s just throw out a number.


**Patrick**: I’ll put actual numbers. I thought I owed the IRS $14,000. My accountant charged me $5,000 to do my taxes for the year, which is on the high side for accountants, was able to reduce that $14,000 bill to, I kid you not, 11 bucks.


Just because he had comprehensive knowledge of the US‑Japan Social Security Totalization Agreement and the US‑Japan Technical Implementation Notes for the US‑Japan tax treaty.


**Keith**: Apparently you were also overpaying for the last three years as well.


**Patrick**: Yeah. You probably could get me that money back too. You just haven’t done that yet.


**Keith**: After hearing this story…I have a slightly expensive accountant ‑‑ not that expensive. But people in Japan, especially in this area, who are very thrifty, would keep saying, “Why are you paying that much for an accountant?” I’m like, “Because he makes me more than I am paying. He saves me more money on my taxes than I am paying him. Therefore I am happy.”


**Patrick**: Right.


**Keith**: And a huge amount of stress at the same time.


**Patrick**: Oh God. I had to do taxes and those of you who’ve done taxes know that it’s like pulling teeth, and it gets harder every year for me, because my business gets increasingly complex. And b) there was the stress of knowing, “OK, there’s some way to optimize this.


“And I’m not sure what it is. Every minute that I spend optimizing my taxes is a minute that I don’t spend optimizing duh, duh, duh, increasing the number of accounts on Appointment Reminder’” which rationally should be the only thing I work on aside from all the other things I have to work on.


**Keith**: To pull back real quick, the number one thing you should be focusing on is things that make people money. That’s the number one thing that people will buy. If your service can make someone money, they will buy it. The number two one is, hitting those top two pain points. What are the things that people hate doing in their business or in their personal life?


I say business because B2B prints money. B2C is really F’ing hard. What are the two pain points that you can solve easily? And push for that.


**Patrick**: Not to beat on the anti‑B2C drum again, but to beat on the anti‑B2C drum again…


**Keith**: [laughs]


**Patrick**: With the amount of money flowing around in the venture capital world right now and also the likes of Facebook, Apple, Google, etc., who are basically driving the cost of software down to zero because it’s a complementary good for their various ecosystems that allow them to print money, I don’t think that there’s really great opportunities for small businesses to do quite so well in B2C software anymore.


There was a thriving Mac market of $30 softwares a couple years ago…


**Keith**: Nothing.


**Patrick**: …Back in the post‑shareware days, and now, even though the market is probably expanding due to the presence of app stores and whatnot, Apple has basically designed the mechanics of the app stores to encourage churn and encourage the pricing to go to zero.


**Keith**: You have to sell quantity.


**Patrick**: Because the happiest outcome in the world for Apple is there’s an app for everything and none of them cost more than 99 cents. That will allow us to sell a lot of our $600 iPhones.


**Keith**: Exactly. They just released Pages, Numbers, and whatever the other one is, not word. I wish it was word. No, that’s pages. I don’t know. Keynote. Keynote. For free. The latest version of Mac OSX is free. Windows is now five dollars or something like that? I don’t know if that was a limited time or not, but I think the upgrade to Windows eight was five dollars, if I remember correctly.


**Patrick**: Was this in one of Joel Spolsky’s [strategy letters](http://www.joelonsoftware.com/articles/StrategyLetterV.html), where he’s like, “Commoditize your complements”?


**Keith**: Yeah.


**Patrick**: This is totally coming true in the software business. The big platform companies have decided, “OK. Software is now a complementary good to the service that we offer.” With Facebook, it’s the social graph. With Google, it’s controlling navigation on the Internet/advertising.


With Apple, it’s the hardware. They want to make the software experience…people say, “Oh yeah, we have a developer community. We want them to build wonderful businesses on our platform.” But they want you to build wonderful businesses by pinching your margins to the absolute bone.


Similarly, while your margins are getting pinched to the absolute bone, you’re going to be competing with people who are venture‑funded based on the huge size and growth opportunities on these platforms, who are capable of having negative margins, just because they have made money behind them.


There was a photo‑sharing startup that recently got shuttered.


**Keith**: [Everpix](http://www.theverge.com/2013/11/5/5039216/everpix-life-and-death-inside-the-worlds-best-photo-startup).


**Patrick**: Everpix, yeah. They spent two million dollars to make a hundred thousand dollars. So many parts of that story make me kind of sad. One is that by all accounts, their service was actually really useful and people loved it.


But it would have been an awesomely successful business making $30,000 a month or whatever. If it was a solo founder who had built it up as a labor of love by himself and then was getting to a point of significant success, where at $30,000 you’ve covered the day job, you have a legitimate business. You’d start reinvesting into it by hiring people ‑‑ one person at a time, and then slowly ramping up.


Due to the “throw gas on the barbie” venture capital model, they had seven full‑time employees. The payroll cost was on the order was like two million dollars over a two‑year period.


It’s very hard to make the math of, “I’ll pay my employees two million dollars and take in $200,000 of revenue work out overtime.” They didn’t have the hockeystick growth curve that would convince the VCs to stake them with another four million in the hopes that they eventually got to a hundred times where they were.


**Keith**: I do want to put some numbers in perspective. Two million for seven people sounds like a ton of money. Over two years, it’s still 140k per person per year. It’s definitely not anything close to bootstrapping, but it’s not like they were blowing money on their employees.


**Patrick**: Right. Yeah. They were probably taking below‑market costs in San Francisco. There’s a breakdown of their numbers that we’ll [link to in the show notes](http://www.theverge.com/2013/11/5/5039216/everpix-life-and-death-inside-the-worlds-best-photo-startup), but their payroll costs were so much…If you compare their total payroll cost number to their total salary number, it’s pretty clear that they were not getting the “standard benefits package” you would expect as a white‑collar worker.


**Keith**: In the San Francisco area?


**Patrick**: Right. They’re getting below‑market salaries. Presumably, any one of the employees of that company could have worked at, without loss of generality, Google or Facebook and gotten the famous free food, and free massages, and paid health care for you and your family, all those other things that you typically get if you’re working as an engineer.


It’s not that they were setting money on fire for salaries, it’s just that venture capital allowed them to grow the team heavily in advance of where the business was. That gamble did not quite work out.


**Keith**: Right. Exactly.


**Patrick**: It burns two million dollars of venture capital guys’ money. I’m not really concerned about that because you pay your money and you take your chances, when you’re an accredited investor.


**Keith**: But when you’re bootstrapped, especially like us…


**Patrick**: Right.


**Keith**: …I don’t have seven million to burn. [laughs]


**Patrick**: Right. Getting back to the point of where you guys as small businesses might be, if you have a venture capital funded competitor in the market, like let’s say you were in the Everpix space, today might be happy for you, actually, because you have the option to go swoop in and rescue 30,000 customers from, “Hey, your service is getting turned off? Maybe you should use us instead.”


But the two years prior to this, it’s like, “Well, there’s this beautiful, well‑designed app which has seven full‑time employees worth of effort expended into it, and it can afford to outspend me 10 to 1 on customer acquisition, because they don’t have to be profitable at it.” That’s not a happy place to be. So don’t do B2B


**Keith**: Sorry.


[laughter]


**Patrick**: Do do B2B.


**Keith**: Do not do B2C.


**Patrick**: Don’t do B2C where you’ll be competing with people who can afford to lose money on every sale and make it up on volume or, at least, will until a Series A Crunch kills their company. I don’t want to rub it in the nose of these guys. I’m sure they are great people and…


[crosstalk]


**Keith**: No. I think they are great people. I think it just was not really shitty luck, but just shitty circumstances for them.


**Patrick**: Yeah.


**Keith**: They did have a great product, by the way.


**Patrick**: It’s the mob. Venture capital, nine companies out of every 10 companies are going to fail. But, if you invest enough of them, eventually you invest in Facebook or Google ‑‑ which is a great outcome if you have a very large portfolio. Perhaps less of a great outcome if you’re confined to any one company.


**Keith**: Exactly.


**Patrick**: People often ask me about it — man, this is a tangent — It’s my first job in the industry. Should I get a job at a funded startup or should I get a job at Google, or Facebook, or whatever? Or should I do the solo bootstrapper thing, or should I get a job as programmer at a non‑technical company?”


**Keith**: That’s a…


[laughter]


**Keith**: …Hard question.


**Patrick**: That’s a hard question.


**Patrick**: We should do an episode about that. I’m going to table that discussion for a while…


**Keith**: Yeah, let’s do that.


**Patrick**: …Because it will make this podcast go six hours long.


[laughter]


**Patrick**: What was next on the agenda?


## Patrick’s Upcoming Course On Conversion Optimization


**Keith**: I think we were going to talk about what is following up the Lifecycle Email course.


**Patrick**: Yeah. Originally, I announced I was going to launch it in August. Then stuff happened. I have a health issue. I might talk about that later. But it didn’t happen. Knock on wood. End of November/early December in July, I hope to launch a video course, similar in character to the Lifecycle Emails product, talking about conversion optimization and A/B testing for software companies.


This is something I did a lot of work on in my consulting days. As we’ve mentioned previously, I’ve quit consulting, but people continued coming back to me and saying, “Hey, what would you do at our page like quickly, not just to increase sales of the product or to increase the number of trials we had on a monthly basis?”


I think that’s something that I can probably have some fairly decent advice about. I do it informally for friends still and have racked up some very fun anecdotes they’re going to let me share publicly. I’m going to productize that and see where it goes. Then, probably, pitch it at the price points roughly similar to the Lifecycle Email course. I guess I don’t want to talk about too much of the plans there because I do need to have some reason for you guys to come to the landing page.  [**Patrick notes**: You can [pre-order the course here](https://training.kalzumeus.com/software-conversion-optimization).]


[laughter]


**Patrick**: I’m not trying to sell you stuff, but I am trying to sell you stuff. But I’m only trying to sell two percent of you stuff. The funny thing about courses like this and whatnot it’s like, “OK. There is,” whatever is in 8,000 people on my email list 1,000 of you opted in for dedicated emails about this product and this topic in specific. Nowhere near 8,000 or probably even 1,000 folks are going to buy it.


I want to produce as much value as possible for everybody in the audience, with the knowledge that I want to spike the value creation with regards to, say, 50 to 500 of the audience who are going to whip out the company credit card and put down that 500 buck, or 2,000 bucks, or whatever it is that it eventually gets priced at.


**Keith**: This is a great topic for our next podcast, if our next podcast is not what we had just talked about, which is the idea of ‑‑ Nathan Berry talk about this a lot ‑‑ marketing by telling everything you know, teaching everything you know.


I think we’ve touched on this before. Not even marketing. Just tell people everything and be very open with what you do.


[crosstalk]


**Patrick**: I don’t know about everything, honestly.


**Keith**: Maybe not everything, but…


[crosstalk]


**Patrick**: I was a “let it all hang out” guy back in the early, early days of being a card creator. As I’m older and wiser now, there are some little aspects I would put on these “totally one hundred percent radically transparent and give everyone access to your QuickBook files.”


**Keith**: I was thinking more of knowledge instead of hard numbers.


**Patrick**: Knowledge, I don’t know. Isn’t it like some sort of picture book, storybook, written by hippies about…


**Keith**: [laughs]


**Patrick**: Have any of you ever read this book where there’s the Warm Fuzzies and the Cold Pricklies. You give Warm Fuzzies to people and, “Wow, you give a Warm Fuzzy to someone, and you magically get a Warm Fuzzy yourself.” Cold Pricklies, they don’t work like that.


**Keith**: That sounds really familiar. I don’t think I’ve read it, but…


**Patrick**: I really think there is actually some hippie book that says this.


**Keith**: [laughs]


**Patrick**: Teaching people things in the B to B context is like a Warm Fuzzy generator. You do not lose stuff by having your information out there. I’ve had consulting clients, where I was doing a presentation internally at a consulting client. They said, “We would like to take this on behalf of the people at our company who are currently not at this presentation. We’re sensitive to your desire to not cannibalize the value of your advice, so we won’t tape it if you’re not OK with us taping it.”


I appreciate that. That’s very thoughtful of you. From my business perspective, not only do I want you to tape it and show it to everyone in the company, but also, if it’s OK with you, let’s tape it and put it online. Let’s get it in front of 100,000 people. Nothing about my business is going to get worse if it gets publicized that this is the advice that I would give your company.


**Keith**: We should definitely go into that in detail. There’s a ton that we can go into with that.


**Patrick**: Next podcast then.


**Keith**: Next podcast. One of the things that I want to mention, going back to the A/B testing course, your next course that you’re putting out. I launched my product on Monday. I’ve been doing this, very similar consulting as you, for three years now, so conversion consulting, OK this page doesn’t work right, this is how we need to structure things to funnel.


**Patrick**: Can I time out here for a second, by the way. Keith and I ran consulting businesses which had different core client bases but very similar levels of sophistication involved and the advice that we would give clients. We had roughly similar price points — within an order of magnitude within each other.


Roughly similar geographic distribution of customers, Japan, the United States, wherever the work found us.


One thing that was not the same about Keith’s and I’s business was that I have an “Internet profile” and Keith a little less of an “Internet profile.”


**Keith**: That’s an understatement.


**Patrick**: I just wanted to throw this out there. OK, I am looking at Keith here and can I name a number at Keith. Keith is looking at me with a look that says “don’t name numbers.” Let’s just say his business is bigger than mine by a lot. There are a lot of people who tell me that “Consulting is great if you’re Internet famous like you are. You cannot be high in consulting unless you’re Internet famous.” You have been disproven by counter-example here.


**Keith**: I have no English website. The new product that I have is all in English. For my consulting, I have no English website. My only website is in Japanese and I will promise you the majority of my clients are not Japanese nor can they read Japanese.


**Patrick**: The primary customer acquisition channel was, “Oh, did you get your job on oDesk?”


**Keith**: No, that was not oDesk.


**Patrick**: Correct, it’s actually doing a really good job with clients and getting referrals by word of mouth. You don’t need 100 million clients to build a very nice consultancy for yourself.


**Keith**: Exactly. What I was going to get into there is I launched my first product. The blinders you get when launching your first product is absolutely crazy. It’s very…I don’t want to say it’s easy. I am used to going into other people’s systems, into other people’s sales funnels, and saying, “OK, here are your main bottlenecks.”


Then, one of the reasons is that I am not super close to that funnel. I haven’t been working in it for three years, five years, so the thorns stick out like you wouldn’t believe. We have been working on this product two years now.


When you’ve been working on it as long as that, you notice that the thorns don’t seem so thorny. I am looking at my own conversion pages. These are totally not optimized. I should really get a consult to come and look at these.


**Patrick**: You guys laugh. You get the equivalent of banner blindness when you’re working on your own products. I was once working with consulting client. We were looking at the sign up page or something and I said, “the decision X, Y, and Z that you’re making on this sign up page are clearly suboptimal. Let’s do something about that.” They’re like, “I copy pasted that from a Appointment Reminder.” I was like, “What. No, you didn’t.” I looked at the Appointment Reminder. “Oh God, you did. What idiot was in charge of this website?”


**Keith**: Yeah, it’s pretty amazing. A lot of my clients are really savvy, really smart people. It is amazing because the mistakes that really smart people can make with their own product, because they are so entrenched in it, are just mind blowing.


**Patrick**: Or there’s so much going in the business, we don’t make optimal decisions about where we spend our limited pool of resources. If I am running a business, so if you were Homunculus economicus, the rational decision maker. If you were Skynet, just decide I have 100 points of resources amongst all the aspects of the business.


You would distribute them at points of maximum leverage for the business. That would mean that everybody’s business would be 99.95 percent spent conversion optimization on their sign up page and .05 doing everything else.


All my consulting clients gave me the death glare there. All of them disagree on me on that. OK, I’ve got my little own take on things. None of us distribute our resources rationally.


Instead, we do the stuff that makes us feel good. Stuff that we think are important, but isn’t important. The day to day grind it out of the business where it’s not urgent but it has to be done anyhow, like responding to emails from people who couldn’t figure out how to click confirm in the email lists.


Doing stupid business administration stuff which we should outsource but we haven’t figured out how to outsource exactly. Bookkeeping for me until I got a bookkeeper.


Stupid wastes of time that chewed up two days of my life, I lost my wallet and so because I have not yet delegated to my relationship to the bank to anyone else, I had to call thirteen banks and say, please reissue my credit cards. Now, after they get reissued over the next week to two weeks, I will have to re‑type them into 50 systems. That’s not going to be the core source of growth for any of my businesses this year, but that happened.


[laughter]


**Keith**: Something derailed it.


**Patrick**: Sometimes its controllable, I’ve spent lots of times this year, something that I did and I’ve should have known that it wouldn’t have been worth nearly as much as working on conversion optimization. For example, in building my own drip course delivery system, like Keith was talking about, I scratch coded that in Ruby on Rails. Somebody approached me, Ryan Delk, from [Gumroad](http://www.gumroad.com), asked about maybe using Gumroad for it.


This is funny because it’s something that I would have posted it on Hacker News, but since I said it in real life and didn’t immediately download myself. I actually said it, “Oh well, you charge five percent of the sale and I don’t think it’s worth five percent of the sale.” Instead I am going to spend weeks of my time implementing them from scratch, and ruby on rails, and doing half a good a job as you guys could do it. Conversion rate optimization.  The Gumroad purchasing experience is *so* good.


**Keith**: It’s the best purchasing experience that I have ever had online. I have been looking at Meteor. Sasha Grief made a [Discover Meteor](https://www.discovermeteor.com/) online course which is great. I went to buy it. The checkout experience was so nice that I emailed Sasha and said that was the best checkout experience of my life. That is how good Gumroad it. It is amazing.


**Patrick**: They are more like towards Amazon. Amazon has I don’t even know how many hundreds of millions of dollars of time invested into making the checkout experience, making shopping actually fun.


**Keith**: I think Gumroad’s checkout experience is easier than Amazon.


**Patrick**: I think it’s quite easier than Amazon. On the scale that people would probably use, Amazon, easy to check out with. They remember your credit card. They do all the “obvious” UX tricks that are not obvious at all. Then, there are a lot of businesses that you do business with where it’s, “Oh my God what idiot made these decisions.” It’s some junior engineer because they don’t have a UX guy on staff and they don’t care about it.


There was a hotel. I was trying to give them $4,000 towards a hotel stay. They wouldn’t take my $4,000 because they said, “you’re credit card is invalid,” I swear I retyped that thing 15 times. I finally figured out by, I kid you not, manually inspecting the F’ing JavaScript that that the thing that’s making my credit card invalid was putting spaces in between the four digits, digit groupings, on credit cards.


**Keith**: Was it a Japanese company?


**Patrick**: No, it was an American company. It was a multi‑billion dollar American company. I wanted to take my laptop and throw it out their window because of…”Do you hate your customers?”


**Keith**: It’s such a solvable problem.


**Patrick**: I think I should call them out. Starwood Hotels.


**Keith**: Really, I hear great things about them all the time, but not their online service.


**Patrick**: Apparently, the reason why I use Starwood Hotels is a mutual friend of Keith and I said, “Oh, they’ve got the best credit card/reward perk thing ever.”


**Keith**: And they do, they really do. They have a great perk system.


**Patrick**: I did lose the credit card. Hopefully it will get reissued eventually and Amex gets me the new card. The website [moans] .


**Keith**: Jale, that was actually a bad day. They have not realized that there’s a space between my first and middle name and inserting that space will not pull out.


**Patrick**: Oh, don’t get me started about names.


**Keith**: We’ve done this I suppose a couple of times.


**Patrick**: I have the entire list of 40 [falsehoods programmers believe about names](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/). It bit me again when I was getting my credit card reissued. I will go on a little rant here about life, the universe, and everything. I think we’re living in this a dystopian cyberpunk future already. We’ve don’t realize it yet because our lives are pretty much livable these days. If you don’t live in “the system,” you’re just totally F’ing screwed.


This doesn’t just affect just middle class Americans or Japanese people that often because we’re middle class. By definition, we are in the system. If you’re not in the system: *welcome to Kafka*. It’s so bad.


I had a bank. The bank could not accept my report of losing my credit card which was in the wallet that I lost without photo identification from me, which was also in the wallet that I lost. This is despite me being customer of the bank for 10 years.


The manager knows me by name. “I am sorry Mr. McKenzie.It’s just procedure. I can’t take this down unless you show me your card to let me that you are the same person who has been coming here in the last 10 years.” This is Japan by the way, where there are only two white people in this town. It’s either Keith or I.


**Keith**: People still mistake us.


**Patrick**: He has a beard. I don’t. Whatever, all white people look alike to us. This topic almost makes me feel Marxist. None of the people who are doing scholarly literature on it, the differences between classes, would be surprised in the least by, “Poor people don’t have photo identification on them all the time, necessarily. Upper and middle class people do.”


Middle class people don’t see that you needing photo identification to vote as a big imposition. People who are not as acculturated into the middle class might see that as an imposition. If you get broken out of the comfort zone for you, you realize how totally non-fault tolerant a lot of the systems are right now, like losing your identification makes systems is a very non-fault tolerant. Systems we designed, too.


I don’t want to sound like a Marxist act now. We can say The System with capital letters as something that is controlled by other people and that we are not responsible.


**Keith**: No, no.


**Patrick**: As programmers, we are responsible for this kind of user experience in our own stuff. As programmers, we often think that we understand what email addresses we use, what user names we typically use, what email address and password we use to sign up for a typical website. This is a highly questionable assumption for many user populations.


I will bet you that if you don’t remember the email address that you used to sign up to your own website that the experience you get is totally sucky. Just try that. Pretend I don’t remember what my email address is. What’s the recovery path for that?


For a lot of services, there is no recovery path. You go to the website, you type in the email address and password you think you used. It tells you “One of those two things is wrong. I’m not going to tell you which.” You can type stuff into that thing all day and it will not help you.


Then you go to the password recovery form and type in your email. Often, for spurious security reasons, the password recovery form will not tell you whether the email you typed in is actually an email that they have on file. Which ‑‑ by the way ‑‑ I want to punch in the face anybody at your company who made that security decision.


The reason being if I type in my email address into the password recovery form and you tell me yes, you got the email right, the email is on the way to do the password recovery. Yes, that does disclose the existence of that email address being in your database, which could leak that to an attacker.


On the other hand, if you only allow an email being in your database once, the fact that someone can use your sign‑up form and see whether the email has been used already leaks the same information. **It’s just pure spite and hatred for your customers that you don’t tell them that email address is wrong or that email address is right when doing logins or password recovery.**


**Keith**: I had a system. I can’t remember where it was. I went to get my password because I had forgotten it. I seemed to remember which email address it was. I put in my email address. It says, “We found your email address, it’s on the way.” Wait 5 minutes, 10 minutes, 20 minutes. It’s still not there.


I put in another email address that is very similar but I know is completely bogus. It said, ‘Your email is on the way.’ Whatever you put in, for security reasons, it would tell you that the email is on the way.


**Patrick**: I’ve been involved in systems like that before. A well‑implemented system, if you’re 100% convinced you want to do this into this, will send you an email regardless of whether you’re email is in the system or not. If your email wasn’t in the system, you wrote it correctly, it would say, ‘We’re sorry, we didn’t have any information on you.’


I was told by a security officer this is a great trade‑off. It doesn’t disclose the existence prior to proving they control the email account. After they’ve proven they control the email account, it’s not a totally horrible user experience.


It is a totally horrible user experience because you have to wait five minutes for the email to show up and then they check it. It’s like “your princess is in another castle.”


**Keith**: Especially with Gmail and G Apps supporting the plus. I have tons and tons of email addresses that all go to the same place, one for each system, in fact.


**Patrick**: I have a dirty confession to make about the plus and whatnot. If you actually read the RFCs for what pluses are supposed to be used for, it’s pretty much just for convenience for the user. I have a lot of people who might be listening to this podcast. If you think I’m talking about you, it’s not you, it’s someone else that’s listening to the podcast.


They think they’re very smart and sign up with my name plus Kalzumeus at Gmail.com to be able to filter it out if I ever start spamming them. When you try to log in to this system, you forget that you used the plus Kalzumeus and so your email address would not actually be in the system.


What I do is my log in form checks both foo@example.com and foo+kalzumeus@example.com.


**Keith**: It takes out the plus first?


**Patrick**: Right. It takes out the plus first, tests for the existence. If you provide the plus on the log in form, which no one remembers to do, it will do what you expect it to. That saves them. I have a running counter on my dashboard. The title about it is “Hacker News Users Who Thought They Were Smarter than They Actually Are.” Currently 47.


**Keith**: That is going into my software. That is the next feature I am pushing live. That is going in front of building fixes. [laughs]


**Patrick**: That’s users acting against their own interests. As programmers, we often act against our users’ interests by making processes which are not fault-tolerant for our business.


**Keith**: It’s amazing. It’s the same thing with blinders. If someone had written on Hacker News that I was doing this, people would jump on him that he was raw meat and they were a bunch of hyenas, honestly.


**Patrick**: I don’t know. I think if someone said, “I have a security rationale for this,” that would get a lot of thumbs up for them.


**Keith**: I think it would be very split. The point I’m saying is people are much more critical and much more able to be critical about other people’s mistakes than their own. That’s not out of spite or purposely, it’s just the blinders issue.


**Patrick**: The ability to consider an issue in isolation gives you a much higher resolution into the intricacies of the problems associated with it than when you’re seeing the entire freaking system at once. When you have a system that has 40,000 lines of code, your password recovery function doesn’t jump at you as the one thing that you should be working on right now.


Especially for B2B SaaS where the lifetime value of customers is, at any given point, in thousands of dollars in terms of future revenue for them. Not having someone cancel their account because they can’t figure out how to log into your system is sort of a win.


I would encourage you to make that interaction not totally suck.


**Keith**: Harping on the forgotten password thing, this is very interesting. I always thought who uses Forgot Password. I have all my passwords stored in Chrome or Key Pass or Last Pass or whatever.


**Patrick**: This is another one of those inabilities to empathize with the user.


**Keith**: Yes. I thought this until a couple of years ago when I was watching the logs because we were doing some purchasing testing or something. As I’m watching the logs over maybe a 20 minute span, I could see people — so‑and‑so requested password, so‑and‑so requested password, so‑and‑so requested password.


How many people are forgetting their effing password? It obviously was real users. It wasn’t going at a high rate. The usernames were completely different. People were requesting their passwords. **People forget their passwords like you wouldn’t believe.**


**Patrick**: There’s honestly some users for whom passwords, they’re done with that nonsense. They just jam on the keyboard and then every time their session gets timed out they request a password again. I’ve seen that usability report.


There was actually an open source project that was supposed to support that as your primary access tool for websites where every time you wanted a new session you would have to click a link on your email. I don’t think they got any traction. It’s not crazy.


**Keith**: It’s not crazy. It’s obnoxious but not crazy.


**Patrick**: Close to crazy.


**Keith**: We’re not going there.


**Patrick**: Not going to rat‑hole. This is the talking about making money for software business. This is not the rat‑holing about little, tiny implementation details podcast.


**Keith**: We’ve gone an hour and a half. We want to cut here or we have three more topics? Two more topics.


## What We Learned At Microconf (In 2013)


**Patrick**: I would love to talk a little more about stuff we learned at MicroConf.


**Keith**: I would, too.


**Patrick**: We talked about concierge. That’s the big one.


**Keith**: I took, I shit you not, 13 pages of notes in the first day. It was a two day course, three day conference?


**Patrick**: Two day conference.


**Keith**: Two day conference. I have an F‑ton of notes. I’m flipping through them now. Is there anything that went out to you at front?


**Patrick**: I have vague memories of MicroConf here, partly because it was similar to me as the one I attended in Vegas so a lot of stuff is it’s interesting but I’ve heard it once. The stand‑out talk, for me, was probably Rob Walling going into what he did to 10x his business.  [**Patrick notes**: Rob’s talk was videoed and is available [here](http://www.microconf.com/videos-2013.html).  Also, you should come to [MicroConf](http://www.microconf.com) if you are at all interested in bootstrapped software businesses.]


He bought a business called HitTail . It was at 1X of revenue. I’m not sure he would be happy with me mentioning the 1X out loud so just say some certain amount of revenue.


Over the course of the next 12 months, he went into a build up the product, learn about the marketing approaches, and then scale the marketing approaches series of three steps that he goes into in a lot of detail to increase the amount of revenue the product was making by a factor of 10.


It’s a kick in the pants for me because I think that would be an awesome process to go through with Appointment Reminder in the next 12 months given that I’ve pussyfooted around for the last three years or so. Also, a lot of stuff is very applicable for every Software as a Service business.


Finding out paid channels which actually work for customer acquisition for you. You test six of them, only two work. Then the two that work you throw money on them until they’re not profitable anymore at the margin. There general rule of thumb in Software as a Service that we don’t grow up knowing that you’re told at some point and find to be true is that you want to spend one‑third of your lifetime value on paid customer acquisition when you can get that, which requires you to know what your lifetime value is. There’s a fairly easy formula for that.


Your easy LTV formula: The amount of money you charge per month divided by your churn rate. That’s it. There are hardly formulas that you can talk to a CPA and learn things about like the time value of money and the discount rate and what that would do to it. Don’t need calculus, just do this simple division.


If your plan costs $50 per month, five percent of customers turn every month, that means 50 times 20 is $1,000. Your lifetime value is $1,000. Done! Spend in the $300 range to acquire a new customer. That’s typically something that you want to do.


If you spend $800 to acquire a new customer, it takes forever to get payback on that and you will have a cash flow deficit in your SaaS business. There are ways to get beyond a cash flow deficit in the SaaS business, but they’re very stress‑inducing and they make your business very, very risky.


You don’t have an iron‑plated guarantee from God that the five turn rate is going to be maintained over the course of the next 20 months. You generally don’t want to take that level of risk in a business. If you’re only spending a third upfront there is less risk involved there.


**Keith**: My biggest takeaway from MicroConf. I will be flat‑out honest. I am not what you would call a businessman. [**Patrick notes**: Hah. Yeah, we’re both totally unqualified for the jobs we do every day.] I am a designer and developer who, I think, is very good at finding holes in things. I find holes in funnels, I find holes in conversion, I find good technical solutions to solve business problems.


Managing a business such as how to make sure that everyone’s working on the right thing, make sure that people are up‑to‑task is not my strong point.


**Patrick**: Keith and I are both similar in this regard. Hackers in the PG sense, we like complicated systems and finding the ways they break and then breaking them to our advantage. Whereas, the mechanics of running a business is something that we just got decently good at for both of us, mostly out of having to.


Also, the fact that if you look at what you want to get from life, the universe, and everything, or from your career, this little, itty bitty slice of your life…maybe you want more time.  The Foolish Adventure guy (Tim) has a great phrase for it: time, income, and mobility are three things you could potentially want to get from a career.


Time, we are both family men. We like having free time with our wives and, in Keith’s case, Keith’s little girls. Income, reasons to have it are fairly obvious. Mobility, like running your business out of Japan rather than running it out of San Francisco or New York or any of the other big tech hubs. We could potentially run our businesses from anywhere our laptops are.


In terms of getting those things out of your career, there is a bunch of levers that you can hit. Both of us, I was a programmer back in the day and Keith was a designer back in the day, that’s one lever you can push, and you will get a certain amount of benefits of working from pushing that lever very well.


There is an asymptote that you approach as you level up as a programmer, I’m going to learn Ruby on Rails in addition to learning Java, and I’m going to become the best darn Ruby on Rails programmer I could possibly be. Don’t get me wrong, that is a very successful career path for a lot of people.


There are a lot of folks who are uncomplicated programmers. They just program up to instructions that were given to them. They work for Google for 50 or whatever hours per week and get paid very well for doing that and love their jobs and lives, et cetera.


**Keith**: You do have to look at it like that. You say they’re told what to program. They could want to be a system designer at Google. It’s still the same thing. There’s a very different thing between yes, I want to work at the best of my field or I want to take that out and grow my own business. That’s the crux.


**Patrick**: Right. The trick for both of us is we took some level of ability with our “core skills,” the stuff our employers were paying us for back in the day, and then drizzled on a wee, little bit of the minimum viable businessman on top of the core skills. I use the word ROFLstomp when other people do it. I’m not sure I’m comfortable saying we ROFLstomped. Let’s go.  We ROFLstomped capitalism, basically.


**Keith**: Honestly, if you had said three years ago, five years ago that we’d be in this position, I would have laughed like you wouldn’t believe.


**Patrick**: When was three years ago? 2010. January 2010 I think both of us put together maybe $5,000 a month at our jobs, our Japanese salaryman jobs.


**Keith**: Together? Yeah.


**Patrick**: If you had balled the two of us together, $5,000 a month at a Japanese salaryman job probably working 70 plus hours a week each.


**Keith**: Something like that, yeah.


**Patrick**: Pretty miserable. I was very, very miserable. Keith was…


**Keith**: I was having days that were less miserable than others, but not many.


**Patrick**: Don’t become a Japanese salary man. We’ll talk about Japan, the universe, and everything in another version of the podcast.


**Keith**: Later.


**Patrick**: Don’t become a Japanese salaryman. Our careers had a fairly nice trajectory over the last three years, largely from this combination of the core skills we bring to the table and increasing that core skill set and then marrying it to the understanding of business and running things on top of it.


Even without necessarily being Harvard MBA levels of adjusting capitalization tables and whatever they teach you to do at Harvard MBA.


**Keith**: We have no idea what they teach you at Harvard MBA.


I won’t say that’s holding back our business because obviously not, but it is holding back growth in some aspects because I don’t know how to manage people other than the standard this is how I would like to be managed and this is how I managed my development teams in the past.


The idea of managing an entire company where I’m managing not only projects with the developers but also how’s billing going, how’s payroll going. Have you talked to the accountant about reducing our taxes somehow?


**Patrick**: This is one reason I still don’t have employees, just because I’m not ready for that level of responsibility. All my friends who have gone to multi‑member consultancies — Keith being one of these — say you get 10 employees together and suddenly you’re responsible for $100,000 every two weeks to make payroll.


If you do not make payroll, people’s families starve. Not going to do it. Not ready to do that yet.


**Keith**: Exactly. Actually, at my old job they offered to put me as vice president of the company, and I said, “I am not willing to do that because I do not want the success of this company on my shoulders. I would rather go out on my own and do it.” I think I’ve done fairly well.


Anyway, going back to what we wanted to talk about with MicroConf. I feel so bad about this because I forget the two of their names. The [TropicalMBA](http://www.tropicalmba.com) guys. I think it was Dan and…


**Patrick**: Dan and Ian.


**Keith**: Dan and Ian, thank you.


**Patrick**: From formerly the Lifestyle Business Podcast. Now it’s called Tropical MBA Podcast. Very good podcast, by the way.


**Keith**: They were amazing. Everyone was amazing, but they spoke closest to me because they were talking about growing a business.


**Patrick**: Can you believe that was their first speaking gig ever?


**Keith**: Really? No, I did not know that. It was amazingly good. They were just talking about how to structure your business so that you don’t have to deal with minutia. They gave an example that really hit home to me. Steve Jobs, complete control freak, as much of an anal control freak as I am, no one eclipses Steve Jobs. Anyone who has worked with him, anyone who has read anything about him would probably agree with that. How does someone with that level of detail into everything be able to control a company with how many thousands of people? 5,000, 10,000. I don’t even know.


**Patrick**: Apple has X tens of thousands of employees. A lot of them are retail workers in the US now, but there’s let’s say 10,000 engineers and knowledge workers at Apple.


**Keith**: Let’s just say 10,000.


**Patrick**: 10,000 knowledge workers.


**Keith**: How would someone with that amount of microscopic detail‑orientedness be able to manage that? It’s obvious. He doesn’t manage it. How would things get done to his specifications? The answer is that ‑‑ and what Dan and Ian said ‑‑ is he only interacted with I think it was seven people in that entire company. Out of 10,000 knowledge workers, he interacted with seven people.


Those seven people were essentially extensions of him. They were close to him. They understood how he thought. They understood what needed to be done to move the company forward in his vision or in the company’s vision.


Dan and Ian called those types of folks lynchpin employees, essentially people that you can delegate an entire section to, an entire job to, who are able to think on their own for their own stuff and move the company forward in a solid, single direction.


That spoke miles to me because it is so difficult to find people like that, both who you can trust almost implicitly and who can be given the managerial task of managing another 1,000 people with their own lynchpin employees.


**Patrick**: And who also want to be employees. One of the problems I’ve heard about on the grapevine, as it were, is that the kind of people that do really well at a) I need a combination of the responsibility to bring this project in without much management from above and b) I also have to be expert enough to manage the people below you and think on your feet and whatnot.


Those kind of people exist. They’re called *entrepreneurs*. They start companies and they often don’t aspire to being the number three guy in charge of server architecture at a tech company.


**Keith**: Exactly. Exactly.


**Patrick**: Figuring out how to identify, groom, and hire those folks is a useful skill to have if you are trying to build up a large company. It wouldn’t be too useful for me.


**Keith**: That was my main point.


**Patrick**: That was your takeaway from Dan and Ian’s. The one I got from it was having repeatable processes for just about everything in the company.


**Keith**: Yes. They call them SODs. In my business, we always call them SOPs ‑‑ standard operation procedures.


**Patrick**: This is something I pulled off their podcast, actually, a couple months ago. It made my life much, much easier because it allowed me to get one task that’s recurring and obnoxious off my plate. Shoot. Broke a rule from my SOP. I should have never called customer support “obnoxious.”


I love my customers. I love my customers.


I have been supporting Bingo Card Creator as literally the only person who had ever sent an email with regards to Bingo Card Creator from July 1st, 2006 to approximately July 1st, 2013. That is eight years of handling all the customer support load.


**Keith**: I want to make a quick disconnect. Patrick always talks about how he always talks about emailing the support and it’s like the Blue Google or the Green Google, ha, ha. There’s a $40,000 a week consultant [**Patrick notes**: Nah, my last rate prior to the recording of this podcast was only $30k.] answering emails from 50 or 60 year‑old elementary school teachers, who don’t understand what the Blue Google or the Green Google is. I just want to throw that out there real quick.


**Patrick**: It wasn’t a huge amount of time, but it was meaning it to be shackled to a machine every day to answer the email within my not quite promised, but want to get to emails within 24 hours generally, or 24 business hours. Stopped doing email on weekends, so it was one of the best decisions ever.


If you send an email during the middle of the workweek, I want to have a response to you the next day, your time, in the workweek. That’s my desired level of service for this product.


In 8 years, I probably answered 10,000 emails about Bingo Card Creator, which means literally hundreds of times that I’ve explained to someone how to reconfigure a printer, or how to use the, “I forgot my password button,” or, dot‑dot‑dot. Dealing with the technical support issues of the largely nontechnical customer base with the product, which, while it’s been improved over the years, is not the world’s easiest to use.


My skills do not generally reside in making wonderful, easy‑to‑use products. Yes, I’m done with that! The way I’m done with that is, I have a standard operating procedure document, which is two pages long. The first page is a statement of principles for the company.


My principle is that, and I joke about it, but I genuinely do love my customers. I got into the business in the first place because I have awesome respect for teachers, and want to make their lives easier, yadda, yadda. I would always rather satisfy a customer rather than having their money if those two ever come into conflict.


I have a hair‑trigger on the refund button. If they say a minor issue caused them to miss the class periods that they wanted to do the event in, I’m very sorry for that. I’ll very happily refund them for that.


So my SOP just states my 12 principals, I have a roughly general nature about that. The second page of the document was, “Here are my top 10 customer support issues that I’ve dealt with for the last eight years.”


I gave these to my virtual assistant who I hired through [Pepper](http://www.peppervirtualassistant.com/). It’s named after Pepper Potts, by the way. don’t tell Marvel that or there’ll be a hammer of Thor dropped on their heads.


Anyhow, I gave it to my virtual assistant, and said, “OK, here are the general principles I run my business by. Here are 10 specific issue that customers often come to me about, and here’s [Snappy](http://besnappy.com) which is the system I use for ticketing.” It’s a very good way to have a lightweight, low ceremony way to share an inbox, basically.


“You are now tier one customer support, which means if someone has an issue, that you are the first point of contact. If it’s one of these 10 issues, deal with it according to the rules I’ve set out here.”


“If it’s something like they need a refund, then tell them, “Look, Patrick will process you a refund within the day,” and here are a couple of words to say that.” But one of my principles is, “We do not copy‑paste stuff. We are humans talking to humans,” because I’m very big on that.


I gave it to my virtual assistant. I said, “OK, this document is a living document. If we discover that there is an eleventh most common customer issue that you can deal with using our tools, or we can build you a new tool to deal with, we’ll add that to the document such that the business grows over time and that this can be…If I need to get a different virtual assistant or a different employee doing this in the future, we can have them start where you left off.”


Then, for the first couple of weeks, I sat in when she was doing these tickets. She would write the response to the customer and then I would take a look at the response she had written, and say, “OK, Sugar.” [**Patrick notes**: For avoidance of doubt, that is her name.]


“Sugar, thanks for writing this response to the customer. I have a bit of feedback for you on how to handle this situation in the future. Great job.”


Then, after that, it was just passive monitoring for her. “OK, Sugar is pretty much keeping it up.”


After that it’s no monitoring. I don’t even know how many tickets we’ve dealt with this week. Honestly, unless something happens, I don’t care because she’s perfectly capable of handling that by herself. Apparently, she rather likes it. The money works out very well for her and very well for me, so yay.


I now went down from maybe 20‑30 issues on Bingo Card Creator per a week to 2‑3, which also means that I can afford to often not check email for a day because, probabilistically, there will be no email that got past Sugar, which is nice. This is something that I’m now thinking of, “OK. What other stuff can I systemize in my business?”


**Keith**: It’s interesting. As a consultant, there’s a lot of the day‑to‑day stuff that can be systemized. Dan and Ian gave the same thing where they said…They were posting a blog post or something. There was some part of the business where they were like, “Only I can do it.”


They had a consultant come in, who was good at writing up these SODs. He says, “Well, there’s 12 steps. You can replace this entire thing, all your thinking, in 12 steps.” He wrote out the SOD, and he says, “Give this to anyone, and they can reproduce exactly what you were doing.”


**Patrick**: Yeah. This is a cycle I have gone through with a lot of people. In the beginning, for any sort of new operation our company is doing, it’s just you throwing stuff at the wall and seeing what sticks, using your magic entrepreneurial powers of deduction. Then, after you figure out what sticks, you describe some theory of why that works or some process of how it works.


You operate on the process and see if the process still works without you using constant levels of supervision or decisionmaking authority on it like, “Is the process at least as good as me?” If the process works, then you have options of giving that process to another person or maybe totally automating the process.


**Keith**: Exactly.


**Patrick**: Then, you move on to a different high‑leverage area of the business, and throw stuff at the wall, and see what sticks.


**Keith**: Like you said with Pepper, ‑‑ Pepper and Sugar, I love that. [laughs]


The documents are living. This isn’t something like, “Now that I have said it, we can never change it. This has to be the way it works.” If things aren’t working with the person who’s in charge of it or they know of a better way, then you change it.


**Patrick**: Yeah.


**Keith**: You find the better way to do it.


**Patrick**: This is one of the nice things about not rushing to automate things.


**Patrick**: I’m a software guy myself. I know we love automating stuff. There’s a lot of issues where it’s like, “OK. My first inclination for how to…” What’s an actual thing that I would think should be automated?


**Keith**: How about updating ‑‑ this is something I do a lot ‑‑ a registration page for a once‑a‑month webinar?


**Patrick**: OK, that sounds great. Let’s make a data description language or a DSL, a domain specific language, for generating a one‑time webinar pages which we will all add a cronjob to automatically update this thing, yadda, yadda, yadda. Wait, wait, wait. We’re going to spend 10 hours of work, which we could be doing optimizing landing things and whatnots.


[crosstalk]


**Keith**: Optimizing so many of your pages.


**Patrick**: The high‑leverage stuff in the business. Instead, we’re throwing it into automating this thing that really doesn’t take all that much time or require all that much brain effort. Rather than doing that, we’ll just describe the process for doing it, then hand it off to somebody who has much less pressing demands on their time than we have.


Then, if we need to change that procedure, it’s as simple as changing our minds and changing the document.


**Keith**: Instead of rewriting code.


**Patrick**: Without us having to rewrite code. **I default to not rewriting code because code, after you’ve written it, it’s nice that it keeps executing for forever. The downside is it keeps executing for forever. You need to maintain it.**


There’s going to be some sort of technical debt that you built into it. You’re going to need to make sure that system stays running for the rest of your life and the security patches, yadda, yadda, yadda. There’s definitely times to write code. Don’t get me wrong. We’re both from in software business, but I try it with people first.


That’s another reason it counts to do concierge onboarding, by the way.


**Keith**: Exactly. It’s like, “What is the amount of time it would take for you to create an import function, or to create guiders, or all that? And what is the amount of cost it would take for one of your support staff to just take half an hour to walk everyone through?”


**Patrick**: Or, in the early days of a product, if you’re not sure, “Should my concierge onboarding be me hand‑holding them for an hour through the entire setup process? Should I do the setup process by myself? Should I just ask for their data and import that for them? Should it be me doing a guided tour through only the demo of the product but not actually using their data? Dot‑dot‑dot…What is the optimal way to get people through this funnel?”


In the early phases of the product, building those things out in parallel would be a whole lot of engineering expense, whereas just trying it, like, “OK, I’m going to take five customers and do them through my first idea. I’ll take five customers, do them through my second idea, take five customers, do them through my third idea,” and see quantitatively and qualitatively, was the experience useful for the customers? Did they understand what was going on?


Does it seem to be working for me? And then for the stuff that is working, invest in automating that or making tools to semi‑automate it. The mid‑touch. Oh, I love the mid‑touch.


**Keith**: The mid‑touch. Yeah.


**Patrick**: I think we’re coming up on almost two hours.


**Keith**: We’re two hours in right now.


**Patrick**: That seems to be a good point to cut it off.


**Keith**: If you’ve stayed with us this long, we applaud you.


[applause]


**Keith**: That was not canned clapping, by the way. That was actually us clapping.


**Patrick**: We are still the lowest‑ranked podcast on the Internet with our regular every three months or so release cycle.


**Keith**: We’ve been doing this for about two years now and I think we’re on episode eight.


**Patrick**: Yeah. There’ve been some less‑official ones in the middle there, but yeah…


**Keith**: Yeah.


**Patrick**: …Episode eight or so. Anyhow, thanks very much for sticking with us, guys. We’ll see you next time, same bat space, same bat channel. You can check out Keith’s product, Summit Evergreen at [summitevergreen.com](http://summitevergreen.com).


**Keith**: Yup.


**Patrick**: My email list is at [training.kalzumeus.com](https://training.kalzumeus.com). Good stuff coming to that in the near future, including about my new product launch, which will, knock on wood, happen at the end of November, early December [**Patrick notes**: July!  Seriously, and sorry for the delay.  Health issues happened.]


**Patrick:** Thanks very much. Thanks very much for sharing your time with us and we’ll see you next time.


**Keith**: All right. Have a good day. Cheers.
