---
title: "Kalzumeus Podcast 4: Apps That Matter, Angel Investing, and B2B Sales with Matt Wensing of Stormpulse"
date: 2013-04-08
url: https://www.kalzumeus.com/2013/04/08/kalzumeus-podcast-4-stormpulse-matt-wensing/
slug: kalzumeus-podcast-4-stormpulse-matt-wensing
word_count: 16649
---


Matt Wensing from [Stormpulse](http://www.stormpulse.com) (disclaimer: I’m an investor, long story below) generously took some time off of managing the nation’s severe weather risks to appear on our podcast.  (Keith Perhac couldn’t be with us when we taped this, as he was celebrating the birth of his second daughter.)  It’s been about six months since our last episode but I think this probably makes up for it, as it’s a cracker of an episode.


I apologize in advance for my audio quality — I was calling internationally from an iPhone.  If you’re an audiophile, we have a transcript below, as per the usual.  As always, the transcript includes notes from me [**Patrick notes**: called out like this.]


**What you’ll learn in this podcast:**

- The long arc of Stormpulse’s transition from a bootstrapped freemium weather site to being one of the four links on Obama’s dashboard
- Why Stormpulse had a difficult time raising funding early, and how they eventually overcame this
- Some actionable tips on how you can avoid Valley pathologies if raising is in your future
- How to think about pricing and selling a critical B2B application, and how to move from scalable low-touch sales to high-touch Big Freaking Enterprise sales


## If You Want To Listen To It


**MP3 Download (~96 minutes, ~88MB) **: Right-click [here](https://podcasts.kalzumeus.com/kalzumeus-podcast-4-matt-wensing.mp3) and click Save As.


**Podcast format**: either subscribe to [https://www.kalzumeus.com/category/podcasts/feed](https://www.kalzumeus.com/category/podcasts/feed) in your podcast reader of choice or you can search for Kalzumeus Podcast in the iTunes Store.


[powerpress]


## Transcript: Growing Stormpulse From Humble Beginnings To The White House And Beyond


**Patrick McKenzie**:  Hi, this is Patrick McKenzie for the the Kalzumeus Podcast. Keith Perhac can’t be with us today, because he’s celebrating the birth of his second daughter. I’m here with Matt Wensing, who’s the founder and CEO of Stormpulse.


**Matt Wensing**:  Hey, how you doing, Patrick?


**Patrick**:  I’m doing great, Matt. Thank you so much for taking the time to have a podcast with us today. I was just looking back at Hacker News today, because I gave it up for Lent, but now that I’m back and can check [on the [thread we met on](https://news.ycombinator.com/item?id=814685)], I realized I have known you for exactly 1,300 days.


**Matt**:  [laughs]


**Patrick**:  You had your first HN post of Stormpulse about three years ago or so, give or take, and it was a like, “Rate my brief elevator pitch,” and I gave you some advice on that.  We started our email correspondence after that. For those of us who have not been following you obsessively for the last 1,300 days, what is Stormpulse?


**Matt**:  [laughs] Yeah, first of all, thanks. The HN connection is definitely fun. Stormpulse, it started out really just as a project and an idea that I couldn’t get out of my head, because a bunch of hurricanes had hit south Florida, which is where I was born and raised. It ended up growing up from just being a project that I worked on in nights and weekends, into a fully fledged organic startup idea, as Paul Graham would say. What it is today is for business, particularly those that have a lot of assets all over the United States. We do real time weather monitoring for them. You think of it for this crowd, maybe as server monitoring, where obviously, you want to watch and see how your servers are doing. Well obviously big companies, especially those in logistics and supply chain spaces, want to watch over their infrastructure and physical goods.


We created a tool which is what Stormpulse evolved into that lets them add all their assets to a home grown, we built it from scratch, weather map, and monitor how the weather is going to potentially impact those locations over the next three to five days in particular. That could be anything from hurricanes to tornadoes to flash floods, or even just a lot of rainfall on some afternoon that delays a shipment.


**Patrick**:  The first time I heard this idea, I was really, really taken with it because I lived in Japan throughout my adult life. We have a very particular understanding of the dangers of severe weather here, but I know some folks from the US did not connect to it as strongly as I do. Can you just briefly give me a description of “why would somebody who has billions of dollars of capital in the path of a hurricane care?”  [**Patrick notes**: I am paraphrasing a few comments Matt received earlier.]


[laughter]


**Patrick**:  What are the decisions they are going to make happen based on the information Stormpulse give them?


**Matt**:  Yeah. Obviously the knee jerk reaction is, “Well, of course they care.” To get into a little bit more depth, there’s really three phases to it you can think, was really the before, during and after phases. Before an event like that, you want to take every precaution you can to not only put things into safety and out of harm’s way, but also optimally position things that you’re going to need during the event or after the event. Then, of course, during the event you need information so you can make decisions about who is doing what right now, how bad really is it, what are the effects, and should I really be worried about what’s going on under that red or purple cyclone over there? Then after the fact there’s businesses who, entire businesses only after one of these events goes through, you have everything from rebuilding to restoration to optimally moving in disaster relief efforts, and frankly even just plain old capitalism.


You have people like Wal‑Mart who come in after a disaster and say, “If we come in there with a boatload of chainsaws and a stockpile of cash, we can do business with a bunch of people who need chainsaws and don’t have electricity.” There’s just a lot of economic implications for these kinds of events, and we just love digging into all of them.


**Patrick**:  Mm‑hmm, yeah, and that totally tracks with my experience. I’ve blogged previously about my very minor experience with Japanese disaster management before.  I worked in back end systems for a Japanese university. We’re largely concerned about getting the information to people before the tsunami makes landfall, is pretty much priority number one. Weather risk management is software that obviously makes a huge difference, both for protecting people’s lives and property. Because we have lots of tech folks who listen to this podcast, let me just talk to you briefly about the technology behind it. I loved the idea when I heard about it, and the moment that this really dropped my jaw about the technological aspect of it was when you said you *wrote your own JavaScript mapping engine*.


**Matt**:  [laughs] Yeah, yeah. We approached this as a labor of love, which meant that we wanted to do everything the quote/unquote “right way.” We took a look when we started out at Google Maps, and Google Maps really did not cut it for us because we wanted to create a weather map. While Google Maps is a fantastic map for everything from bike tours to self‑driving cars and all that stuff, it really isn’t the best cartography for displaying the weather. That left us with two choices. Either compromise on the initial vision, which we were just starting out, so why would you ever do that? Or create our own mapping, so that’s what we did. I spent a fair amount of time just getting my head around…


I’m not one of those math comp sci major, so I’m not super fluent in a lot of mathematics, geometry, trigonometry, but I got up to speed really quick. Spent a lot of time on Wolfram Alpha and learned how to get my head around map projections, and got the imagery from NASA and compiled it with some clouds that I found from a guy at Cal Tech. Yeah, we actually built an entire mapping stack from nothing.


I still remember sitting there staring at my editor, which was basically blank, going, [laughs] “This is the start of a very large application, and it’s totally blank.” But I was fueled by passion and got up really early, and the rest is relatively recent history.


**Patrick**:  Yeah, you’ve been doing this for, what is it now? It’s almost as old as Bingo Card Creator so seven or eight years‑ish, I think?


**Matt**:  Yeah. I had the idea in…Those storms were going through Florida in October of 2004, and that meant that I was…Yeah. I had the idea in October 2004. I still have the blog post actually on Blogspot, where I was mulling this over and just had this idea of, “Yeah, I’m going to work on this thing.” October 2004, coming up to in a few months October 2013, which will be nine years since I had the idea.


**Patrick**:  Oh, wow, so actually even older than my business.


**Matt**:  [laughs]


**Patrick**:  It’s funny that I am comparing our two businesses, because yours saves people’s lives, and mine makes bingo cards for elementary schoolteachers.


**Matt**:  [laughs]


**Patrick**:  The Internet is a funny, funny thing.


**Matt**:  It is.


## The Best Startup Customer Acquisition Anecdote You’ll Hear In 2013


**Patrick**:  I’ve got to admit, every time I hear about your business I have the, “I wish I was working on a bigger problem,” pangs of envy, something I’ve heard from other people. Then, of course, there’s the other pangs of envy inducing story. You have a very famous customer of Stormpulse, right?


**Matt**:  Yeah.


**Patrick**:  Every time I tell this story to people they don’t even believe it, so let’s get it on the record, so I can refer people to it in the future.


**Matt**:  Yeah.


**Patrick**:  The way I remember the story, and like my father I often embellish on stories I’ve heard once, so feel free to tell me if I’m lying about this. You were sitting at the kitchen table with your son one day doing the bootstrapper dream of sales call with one hand and a bowl of cereal in the other, and you got a phone call from somebody, and called him back. That was Dan.  Where did Dan work at?


**Matt**:  Yeah. I got a voicemail. I read the voicemail and I could hardly believe it. I told my child that I had got this phone call, and they said they never heard that before. That sounded pretty outrageous to even them, and I think they were probably six or seven at the time. Then before I could even call them back they called me back, and so I ran upstairs to my home office so that I could have some peace and quiet and sound professional. Sure enough it was the White House Situation Room, which meant that it was literally the basement of the White House. [laughs]


**Patrick**:  Yeah. For folks who are not the American audience, the [White House Situation Room](http://en.wikipedia.org/wiki/White_House_Situation_Room) is the nerve center of the White House when they’re doing something that is breaking real time related generally to national security. That’s where President Obama and the team were when they caught Osama Bin Laden. It’s where they command disaster relief efforts and what not, so it is a big deal.


**Matt**:  Yeah, and the amazing part, Patrick, was that they left me their phone number as if it was my neighbor next door, I guess, with all the confidence in the world that if I abused that phone number there would be easy tracing and repercussions. But I called them back, because actually, when they called me back, I didn’t get to ask them if I could somehow capture an image or something that proved that they used it. Then I’m spending all afternoon here, I remember sitting at the lunch table with my wife and telling her this story. Her thought was, “Well, you should have figured out some way to get their name or get proof that they used it.” I built up the gumption to call them back, and sure enough, it rang. I was expecting them to say, “Thank you for calling the White House. For gift shop, press 1. For tours, press 2.”


But sure enough it just rang and rang. I think it was one and a half rings and somebody picks up the phone and says, “Situation room.” [laughs] At that point I thought maybe I had called the red phone. The very first thought I had was black helicopters. The second thought I had was “This is not urgent, so please don’t…”


I wanted to somehow explain that I’m not really trying to prank you by calling you from my bootstrap SaaS business, I just have a genuine question. The person I was calling wasn’t there, but he said she could call me back. Sure enough, she did.


But between the time between the time I hung up with him and she called me back, I found out on the White House blog, at WhiteHouse.gov, there is indeed a [tour of the situation room](http://www.whitehouse.gov/blog/2009/12/18/inside-situation-room) that they have recorded in public domain mpeg, and I was able to capture a screen shot of that tour, and put it on our website. Since it’s public domain, I think I can have free conscience and liberties to use it as much as we want.


You can actually see our product being used in the basement of the White House. Which, yeah, it’s hard to explain, really. [laughs]


**Patrick**:  For those of you keeping track at home, not only has Matt bootstrapped a company with the rest of his team which protects life and property using a SaaS application, but they bootstrapped it to the point where rather than going to NOAA, National Ocean and Aeronautics Administration, getting data directly from them, the folks at the White House preferred to consume that and make consequence and decisions affecting millions of Americans directly through Stormpulse.  [**Patrick notes**: Stormpulse owns no satellites or weather monitoring stations.  They consume NOAA data which is available in the public domain, and transform it from GBs of opaque CSV files into predictions like “The factory which makes the widget that you’re running low on has a high probability of closure three days from now as a result of this hurricane”, which lets the user take consequential actions like “Put in a rush order at our alternate supplier so our main production line doesn’t block on lack of input 6 days from now.”  When factory lines go down that can cost in the $X00,000 region an hour.]


**Matt**:  [laughs]


**Patrick**:  Man, it’s like I’m doing a sales pitch.


**Matt**:  [laughs]


**Patrick**:  If I wasn’t totally convinced that Stormpulse was going to take over the world when I first met Matt and was talking to him the last couple of years, when I heard the White House story, didn’t the White House initially send you a feature request?


**Matt**:  Well, what they did was they just really had a question about…Oh, that’s right. I did see them come into our database as, what was it, it was somebody’s name at NSC.EOP.GOV, which went right over my head at first, but when, when I was trolling through our records, sure enough. I figured out what those acronyms mean, which was National Security Council, dot Executive Office of the President, dot gov. Then I believe it. [laughs]


**Patrick**:  Let’s see, so there’s again, feed you the stories. The one I heard from you is that there’s a *particular user* of the Stormpulse application that has to remember a lot of passwords and didn’t like having to remember one more, so there was a feature request made with regards to that user.  Can you tell us the story?


**Matt**:  Yeah.  We had just done a new release of the software which bumped the price, and a customer called to ask if they could get a feature request as part of the upgrade.  They wanted to know if we could make sure that it did not automatically sign the user out. They wanted the login cookie to persist indefinitely. I said, “Well, good news is our application already works that way because we have a lot of people in enterprises that don’t want to have to remember all these passwords, and it’s up to them to sign out.” He said, “Well that’s good because, if *the guy* goes to use it and it signs him out and he has to remember a password, that would not be good.”


I dug into this about the guy and I learned that it’s outside a conference room in the White House, and so I said, “Well, I’m imaging there’s quite a lot of conference rooms.” He said, “No, this is the only conference room that *he* uses. There’s a kiosk outside, and Stormpulse is one of the three or four short quick link applications on that, and they just want to make sure that it’s always signed in for **cough** Mr. Sir.” [laughs]


**Patrick**:  You heard it here first, guys. This is Traction with a capital T even if you don’t have two hundred million free users, which we’ll talk about later. Every time I tell this Stormpulse story to people, they can’t believe it. I’ve been called a liar to my face by people, *so hah*, there you go. In addition to various highly-placed users in the United States government and folks all over a bunch of industries that really care about stuff not being destroyed, Stormpulse is a B2B application right now, so anyone can sign up on the website to start using it in their business.


You’re doing really well in that since last year, right? We’ll talk a little in the call maybe about the difference between premium and the pricing model, but up until last year, you had a premium model where the vast majority of people paid you nothing and then you were trying to sell it to business. You switched completely to a business model and how’s that been working out for you?


**Matt**:  Yeah, we put up a paywall very quickly last April. Quickly because it was two guys and things were under crunch. We put up this paywall not knowing what would happen. We had about 6.5 million unique visitors in 2011, and out of those 6.5 million, we had almost 1,000 customers sign up. So, 6.5 million freebies was nice and all, but having a customer base is even more exciting, I’ll say. Certainly a different phase, there’s lot of stories that come from the free, and there’s actually lots of benefits in terms of distribution, so I won’t say it doesn’t have its benefits, but there does come a time where you should make money, and that’s the phase we’re in now.


It’s definitely turned a good corner, you might even say pivot, and yeah, here we are now in this pay‑only model. We have a free trial, but the freemium product has been retired.


**Patrick**:  Great. Because this is largely targeted to large businesses, government organizations that, again, lives and property are on the line, so this isn’t exactly like a project management application that you sign up with your credit card and pay $20 a month for it. Your price point start at the high hundreds a year region and go up drastically from there for the enterprise stuff, right?


**Matt**:  Our single‑seed price this year is $750 for the year for the year, for one user, which is like a mid‑grade SalesForce subscription if you wanted to do it monthly, although we bill annually which is good for cashflow. Our pricing goes all the way up into five figures depending on how many seats you want to get and now we’re starting to think and talk about enterprise which is even bigger than that. That’s all of our whole breadth.


**Patrick**:  Switching gears a little moment: I keep wanting to claim credit for something about Stormpulse so I’ll claim credit on the prognostication that I knew you guys were going to take over the world a few years ago.


**Matt**:  [laughs]


## How Stormpulse Got Angel Investing After Having A Bit Of Difficulty Raising It


**Patrick**:  Apparently, the rest of the world did not, and it sucks to be them. [**Patrick notes**: I let a bit of anger in here, as there’s a long, long story about Matt and company getting treated shabbily in their first fundraising attempts, and I view their subsequent success as a rich comeuppance.] Sorry, maybe that’s a little negative. Let’s talk about angel investing. I think this is a time to put a disclaimer. I’ve never been an angel investor before, but we talked quite a bit about angel investing last year, and in the process you eventually letting me put money into the company. Thanks.


You had been bootstrapping this for quite a while now and tried raising a few years ago and I think largely it’s because you were not in the Valley that did not exactly go over as wonderfully as you would expect given the success of Stormpulse.


Many of the folks who are listening on the call aren’t as up on angel investing as the two of us are. Why don’t we talk a little about what it is? Why you would want to take it for your business? What your experience was trying to raise outside of the Valley and what your experience is now. Also let’s talk about how the mechanics work.


**Matt**:  Sure. Yeah, sounds great.


**Patrick**:  Basically, angel investing is typically people investing on an individual basis, largely, wealthier individuals, called accredited investors usually, who are independently wealthy, often in the tech industry as a result of running their own tech businesses, who give money in return for equity in growth‑oriented businesses.  Angel investors have the expectation that that business is eventually going to exit, either by selling to a larger enterprise or either by IPOing on the stock market and they hope that they’ll get their money back when that happens. This is more of what Paul Graham would [describe as a startup](http://www.paulgraham.com/growth.html) where you’re aiming for growth, and going to get very big rather than aiming for a consistent return over…like so many compounded returns over the long term and returning dividends. We talked extensively over the last couple of years prior to you making the decision to seek angel funding over like what it would do for you personally and what it would do for the business. But from your point of view, why did you think taking angel investing was a great choice for Stormpulse?


**Matt**:  Yeah, just to clarify and make sure I understood in there, why do I think it was or was not originally or…?


**Patrick**:  Both of those, I guess.


**Matt**:  [laughs] Sure.


**Patrick**:  Why did you bootstrap when you started it and what changed?


**Matt**:  We did bootstrap initially. I guess it wasn’t for total lack of trying to raise some money. We went to friends and family first and we actually raised about $100,000 from friends and family who you could also call accredited.  [**Patrick notes**: For the very persnickety people who would claim that this makes them not “bootstrapped”, your objection is noted but I have very little desire to argue about the peripheral meanings of words.] But those friends and families supported us in the early years of bootstrapping where we had no business model whatsoever. We were just two guys with a product and no distribution. Then we ended up getting the distribution. Like I said we had the six and a half million visitors and we started seeking our first round of real angel funding. I know that there’s a lot of people who are bootstrap only, bootstrap forever.


I think that’s fine. I think it can become this religious war over who’s right. Which way is the right path? I do think there is a time when you sit there and you look at a business and you say, there’s no reason this couldn’t grow faster other than I need capital upfront to fund faster growth. In that case, raising money makes a lot of sense rather than looking for that linear growth to come through charging more customers more money and watching it grow.


It just grows much slowly that way. Of course, obviously, raising money at the same time implies that you’re going to grow fast, so if that’s not for you, if you don’t like the thought of growing 50%+ year over year, and by growing I mean, so you take last year and you double it, or so, then it’s not really for you. But if you have a huge market and a product people love, it makes a lot of sense. I always believed in Stormpulse certainly had a big market.


Took me a while to figure out exactly what corners of the massive world’s enterprises I wanted to go after but once we started figuring that out, then it made sense for us to go and try and to raise some money. We did a couple rounds of seeking. The first one didn’t work out too well but the second one did.  There are different reasons for that which we could get into but I’ll pause there and you can ask the next question if you want.


**Patrick**:  I’ll give you some of the thoughts on the bootstrapping thing.  Most of the folks listening on the call know this but I’ve bootstrapped all my businesses for the last seven or eight years now since 2006. If feel old. I perpetually have like one toe in the water of the funded startup world, which 99.95 percent is a result of Hacker News, if you spend all of your time talking to people who talked about it a lot, it will eventually pull you in.


**Matt**:  [laughs]


**Patrick**:  But, yeah… I love bootstrapping.  It iswhere my heart is. I always think that in the future, it’s possible that I continue bootstrapping forever and it’s possible that I can eventually choose to take funding for either Appointment Reminder or one of my other, perhaps future, businesses. We’ll see where the road takes me but again, it’s a decision most based on where you business is, where you want it to go, and what your personal goals are. In particular,one of the reasons that I’ve never taken it, despite several compelling offers to, is that there’s a lot of freedom associated with bootstrapping in that you are in control of roadmaps for the business both in terms of the technical roadmap, the marketing roadmap, etc.


Obviously, you have to satisfy your customers and if you have employees, you have to satisfy your employees but there aren’t other major stakeholders that you really have to keep happy. After you have any sort of professional money involved, folks can theoretically call you up and say, hey, what has my money being doing lately.


**Matt**:  Sure.


**Patrick**:  Investors might push you towards options that you might not have otherwise gone for. Not that I would call Matt up in the middle of the night and say, “Hey Matt, where’s my money at?”


Just generic advise for people trying to get money from people: attempt to raise from people who understand the business you are in. Not always an option for friends and family but if you were going to take money for investing in a tech business, from angels, like, all flowers are not created equal, it’s probably better to get money from somebody who’s in tech themselves, because they understand it, and to the extent, possible from somebody who brings knowledge to the table about your market or your industry or particular topics of interest for you.


If somebody had made their millions on Facebook games or whatever, they might not be the ideal investors for Stormpulse, simply because they don’t really have all that much to tell you about the distribution story for getting into more places like the White House Situation Room.  Come to think of it, scratch my head a little bit, I wonder how much I had to add to that equation. But I do hope that I give good advice every once in a while.


**Matt**:  Yes. I think you’re absolutely right. One thing about investing that people who haven’t, well, I say fundraising, because really we’re on this side of the table, that people might not have thought about before if this is their first time around is, there’s genuine value ad and there’s a fellow by the name of Patrick Vlaskovits who wrote a [great post](http://vlaskovits.com/2012/08/how-not-to-get-fcked-by-an-investors-lack-of-value-add/) on this about what is real value ad, you can find him on Twitter @PV. But value add can actually be genuine, helpful advice or insight or rolling‑up‑the‑sleeves help. Or, there is a value ad which is the total absence of any involvement.  The derogatory way of saying it is “dumb money”, but really that means that that’s money that gets involved, that tries the meddle and mess things up.


It’s really *laissez‑faire money* which can also be very valuable if you just need money and a bank isn’t the answer and you’re just looking to fund something if the person is just willing to make an investment and not make a lot of demands or get involved which is to say, pretty much be silent if that’s the way they like to invest and manage things, that can also be really good for the entrepreneur. I would say you really want to be on either side of the spectrum. Either somebody who’s genuinely helpful, or somebody who just completely stays out of the way.


The worst thing is obviously people who think they’re adding value but really aren’t. Then they’re just wasting your time and theirs and adding stress. None of those are going to help you.


**Patrick**:  We talked from your perspective as the entrepreneur of what you wanted to do about getting angel investing.  From my perspective as the angel investor, here’s what I get out of this relationship. Primarily for me, it’s not an opportunity to make a lot of money because I have a fairly successful software business and that’s the  numbers would work out for me. My software business is going to dwarf returns from any investing I do. I really believe in the vision of Stormpulse. I’ve lived in Japan my entire adult life. There has to be better technological approaches to severe weather risk management and also we’ve been corresponding for the last three years and when I heard you were raising an angel round I wanted to do anything possible to accelerate the success of the business.  I thought in my little, sometimes accurate, sometimes perhaps not so much estimation, that the most credible statement I could make to Silicon Valley investors when I was trying to introduce you to was “By the way guys, my money is already in this.”


That’s my endorsement. You can do it too. Would you mind us saying publicly who I introduced you to?


**Matt**:  Yes. No, that’s completely fine. Yeah, that’s a good story.


**Patrick**:  I’m peripherally involved in 500 Startups which is a well regarded super angel… actually they’re closer to a mini-VC fund mini‑VC funds these days, but it’s a fund in Silicon Valley run byDave McClure, Paul Singh, and a group of other partners including  Christine [Tsai] and some folks who I haven’t met yet. Anyhow, they’re a good people. Paul Singh knew me over the Internet, and so you would be amazed how many people I could say, “Oh yeah, I’m Internet buddies with him these days,” far too much time on Hacker News, what can I say. We had swapped some thoughts about selling software which is something he used to do and something that I do on a fairly regular basis.


I went there to just say hi one time when I was in the Valley, for whatever reason. I think probably to a conference or something. He asked if I wanted to be a mentor at 500 Startups, which is all the fun of being a consultant without the complication of actually taking money for anything. [**Patrick notes**: If it isn’t obvious from the context, that’s a joke. Obviously I was happy to do it or I would have politely declined.] You just talk to people that they are invested in, or incubating, and I give them advice.


That sounded like a pretty fun thing for me, because give me a text area, and I’m physically incapable of not typing in it. Talking to startups is like having a text area with less HTML involved.


One of the nice things about having social connections like that is that, Silicon Valley is a place I have a *complicated relationship* with, because there’s wonderful things about it, and not so wonderful things about it.


One which straddles the line of those two, is that it’s a very relationship oriented place. It’s very difficult to raise money in Silicon Valley, if you don’t know anybody. On the other end of the ledger is, if you happen to know lots of people, you can raise money in Silicon Valley, perhaps, independent of the quality of the thing you are raising money for.


The nice part is that since I have a social “in” with 500 Startups, and with other folks in the Valley, I can do one of the Valley’s little social rituals, which is called “an introduction”, which is basically, “You, person X, should know this other person Y, I vouch for Y, ergo you should rub off some of your trust for me onto them.”


Which is pretty much the only way to get investments from most VC funds, and savvy angel investors, because otherwise they’d have 5,000 people coming out of the woodwork, talking about their new Facebook for dogs. I introduced Matt to 500 Startups, and told them that if they didn’t come to terms I would come over to the office and pound their faces in if they did not invest in you.  [Patrick notes: I didn’t actually threaten anybody… but I was mentally when choosing very, very strong language in my recommendation.] Obviously you had the numbers, and the story to support it. So they did, which is awesome.


**Matt**:  Yeah. I think it’s worth highlighting just how important that introduction is, or is to their mechanics of 500 Startups. Dave McClure said, “If you can’t get an intro to us, you’re not really trying hard enough,” to paraphrase. In other words, it shouldn’t be that hard. It’s a test of the entrepreneur, of whether or not you can make these kinds of connections. At first, especially if you’ve never raised money before, and you’re totally outside of the Silicon Valley world, I don’t live there, so I can’t speak from direct exposure experience, but it can definitely feel, obviously, insulated, and nepotistic, and there’s all these pejoratives for it obviously. At the same time, like you said, with all the quantity of people with ideas, and napkins. Social proof in that sense goes back a long, long time, in terms of trust, and referrals.


I was just going to say, what 500 Startups is doing, by and large, is scaling social proof behind the scenes, and actually quantifying it, and using it in investment decisions much more quantitatively than say, a traditional VC, or angel. [**Patrick notes**: See especially the increasing use of AngelList, which does a lot of social proof based on essentially graph algorithms and some secret sauce.] Getting a hat tip from someone like Patio here is a really big deal, getting other ones from other people. Having that social network, work for you as an entrepreneur, is probably the best way to get their attention. Yes. I am greatly indebted to you Patrick, for that introduction, and I appreciate it.


Paul Singh ended up being the partner I spoke to, and just to give you the dramatic ending to that story, obviously he really liked our numbers, he thought we were, in one sense, undervalued for the amount of traction that we had, similar to you.


**Patrick**: I so strongly agree with that.


**Matt**:  Stormpulse, the reaction has been very polarized. Maybe polarized isn’t the right word, because I don’t get anybody that is strongly negative, but it’s either no reaction whatsoever, or just a dead stare, or somebody’s just foaming at the mouth excited, so if you can take that as a compliment. [laughs] You, and the other 12, or 13 angel investors in the last round, were obviously on that side. Some of them took a little bit more cajoling, convincing, proof, but they were just all really excited about the business. I find it really interesting, because what it tells me, is that when you combine that element of social proof, or trust, and you combine great traction, it just goes a really long way to making it a decision where the investor does not feel like they’re taking a huge risk. From the entrepreneurs stand point you think, “Well, I want to get investors because I want to have some risk takers on my side.” [laughs]


Then you talk to them, and the first thing you realize is, hopefully it’s not the first thing realize, hopefully you’ve listen to this podcast, and you realize it, but they don’t really want to take risks if at all possible. That’s not why they’re investing, is too take risks. They are engaging in the worlds riskiest form of investment, so that they can make some of the world’s best returns [**Patrick notes**: An overstatement, see below!], but taking risks is not what they’re all about.


Your job as an entrepreneur is to remove every possible risk from the equation, before you ever present it to them. Getting referrals, and thumbs up from people that they already have credibility in their network, and then having great traction, I think those are the most important. I honestly believe that once you do those, you still may find yourself in a lurch, so for us, say in 2012, before we put up the paywall, actually that was 2011, before we put up the paywall, we talked to VCs, and it was just really hard to get them to that “yes.”


They’re always looking for ways to say no. No is the default, it has to be. [**Patrick notes**: The default is even more insidious: it’s just not getting an email in your inbox when you have been lead to expect one.] To get a yes, you have to get those referrals, so we get introductions, but our traction, because we weren’t charging money of everybody, left something to be desired, and because of that, I don’t think we were able to transition into the realm of yes.


I think the realm of yes, is that stage where the person allows themselves to get excited about the business, to the point that they, I might even say, “overlook some of the flaws of the start‑up,” because they just believe so much in what they see, in the positive trends they see. It’s obviously a very nuanced thing, and for the entrepreneur who’s going through it, I can totally identify with just how difficult, and frustrating it can be.


In order to raise just over half a million dollars in convertible debt, I think I ended up speaking to almost 80 people. I’d say out of those first 50, 49 were no, and there was maybe one yes. Then out of the other 30, we got a increasing frequency of yes’s, and toward the end it was all yes’s. [**Patrick notes**: This is an incredibly important point about the nature of social proof, by the way.  Matt has previously described his funding round in a single [tweet](https://twitter.com/mattwensing/status/288860395710599168): “Our seed round in 65 characters: NNNNNNNNNNNNNNNNNNNNNNNNNNNNYNNNNNNNNNNNNNNNNYNNNNYNNYYYYYYYYYYY”]


For the entrepreneur that can be a incredibly emotionally, trying experience, so part of what I offer, and if anybody wants to reach out to me after this Podcast, is [laughs] I would love to help anyone navigate that a little bit, because it is very emotional. I think the key is, the key I had inside was, how do you get the investor as well to the point, where they are emotionally excited about your business?


That’s where they fall in love with the girl, so to speak, and they say, “Yes, she doesn’t know how to cook, and yes, she also has a really annoying way that she laughs, but I don’t care, because I love her, because of this, this, this, and this.” Until you get to that point, what you find is, all the investors want to do is point out your flaws, and say, “Well, that’s why I’m not investing.”


I think that’s a little bit of a red herring, because if an entrepreneur can get investors to the point that they’re genuinely excited about your business, I think that actually atones for a multitude of problems, because no start‑up is perfect, right?


**Patrick**:  Almost like selling a product, right? In that, if you totally nail the emotional connection of the user to your product, the fact that it doesn’t have a sexy UI or isn’t the cheapest in the market, or what not, will be details to the customer.


**Matt**:  Exactly.


**Patrick**:  There’s so many interesting things that we just brought up there. Why don’t we start with this commentary on the Valley, and the Valley’s little peculiarities, by two people who are very outside of the Valley. Like you said, it’s a pretty insular place. Where are you currently physically located right now when you’re doing this call?


**Matt**:  I’m in my office in Austin, Texas. Yes.


**Patrick**:  Matt’s coming from Austin, I’m physically in Osaka right now which is a nice big city in Japan, which is not the usual small town in Japan [Ogaki, Gifu] that I’m broadcasting from. Clearly it’s possible to make connections to the Valley, and not physically being in the Valley. Intent by the way, there are people on the Twitters don’t dislike talking to small entrepreneur’s, hint, hint… anyhow. I could go back, and forth on how much of a barrier I think that necessarily creating a connection in the Valley is to a determined entrepreneur. My personal experience, having done sales to enterprises, and having made a bit of a name for myself over the years in the Valley is that selling to enterprises is so much harder than getting someone to make a coffee date with you. If you think you’re going to be successful in business. Getting on the radar of people in Silicon Valley, not quite as hard as you would think.


If you write three blog posts of a particular topic of interest to a start‑ups with money is enough to get you on the right peoples radar screens. Suddenly you get some sort of distribution through those blog posts, which can be an entire podcast by itself.


## What Is This “Traction” Which Silicon Valley Seems So Beholden To?


I mentioned the magic of Silicon Valley where no one ever defines. I want to dig into it a little bit. “Traction.” You have traction. “We can’t invest in you, because you don’t have enough traction.” “Call us back when you have more traction”, or the most insidious form of a VC “no”, which is just, “We’d love to see a little more traction, before deciding on looking at the start‑up again.”


I will link it in the notes, but there’s a [great talk](http://lanyrd.com/2012/twilio-conference/scdccz/) between Naval [Ravikant]  and Dave McClure on what counts as traction in the Valley.  We’ll talk about it from our biased and narrower perspectives on the matter.  [Patrick notes: Much of the talk between Naval and Dave focused on B2C startups aiming at truly massive distribution via mobile apps rather than B2B SaaS companies like Matt and I run, where your user numbers are at a thousandth of the scale and your revenues are infinity percent higher.] I think folks might be intimated a bit by the “6.5 million visits a year” stats from earlier, but that is totally an achievable number.


Bingo Card Creator craters the approach to 6.5 million a year [**Patrick notes**: the main site is at 1.X million a year, give or take], but Bingo Card reader doesn’t have traction, because it’s not going very fast, and the market is not ginormous, and because unfortunately Bingo Card Creator has revenue, and after you have revenue, the salience of large visitor numbers drops a little bit, and then people will look at the revenue.  [**Patrick notes**: Also, if you tried to look at metrics of high interest to e.g. broad B2C apps, the “new normal” is 10 million monthly active users and BCC has only 10,000 or so.]


For revenue based traction, for recurring SaaS-model businesses, if you’re bootstrapping a business, and you get up to $8,000 a month, you’re in a wonderful place to be in life. $8,000 a month craters the approach of where you start getting angel investment, as long as it’s growing.


After you start to get into the low to high five figures a month, of your recurring revenue, you will start to get on progressively larger angel/VC firms radar screens. If you need a number to shoot at, that’s your number. Low five figures, and then that will quickly get you into the right place.


It can even be lower than that, if it’s growing very fast, or you have a particularly good story about the market. Like, “Everybody will be using this technology in five years.” “We grew revenues from $2,000 to $3,000 over the last month. We don’t see it slowing down.” Does that match your understanding of it?


**Matt**:  Yeah. It’s interesting. I agree with that, and yet obviously I would add to it, first of all, probably in the world you’re looking at, you have more experience in the month to month revenue business than I do. We charge yearly, and our business is very yearly, just because we’re B2B. I tend to think in more yearly numbers, than monthly numbers, but you’re probably right on the quantities.


**My definition of traction, if I can throw it out there, is evidence that you can capture value at a rate that moves the business forward.** Then the next question is, moving forward into what? Are you about to max out at $100,000 a year, or is this a $10 million a year business?


That is also proving this feedback loop, where the more traction you get, the more evidence you have that the market may be bigger than you originally thought. It’s a virtuous cycle, or spiral if it’s working out. If it’s not working out, or if it’s flat, you may say, “Well, we have six and a half million users” “Yeah, but they’re all free.”


You don’t have evidence that, that’s a business. You have evidence that you have *a much smaller version of the Weather channel*. [**Patrick notes**: I love that line.] For us traction was not until we had strong evidence that we could collect money at a rate, that let us move the business forward, which meant pursuing enterprise, hiring more people, growing a business that was on course to do in the millions of revenue, rather than in the hundreds of thousands forever, and ever.


I say captured value, because really what you’re also doing is, if you had enough free traffic, then you can make the, “Ye olde advertising argument”, which is, “We’re going to place a tax on the attention that we’re capturing, so the value you’re capturing thereand, “We’re going to tax it with these advertisements”, or “We’re not going to tax it very much with these AdWords, and make a ton of money.”


It’s shifting. Sometimes it’s eyeballs, sometimes it’s dollars, but like you said, sometimes eyeballs are better than dollars, because when we were a $195,000 per year business, people gave us the blank stare. [laughs]


**Patrick**:  The reason, by the way, for that, for folks playing along at home, is for an individual person, $195,000 is a wonderful, wonderful outcome, but if you’re an investor in Silicon Valley, you know that $195,000 does not even cover a single engineer. [**Patrick notes**: Ballpark $20,000 per month, fully loaded.] If you do not see that growing explosively, then it doesn’t have any potential, in terms of, strategic value leading towards an exit, which again is what people are aiming for at the end of the day.


**Matt**:  Exactly, so in our case, traction with a capital T. In hindsight we can apply the narrative, and say, “Look the President was using it, isn’t that awesome?” VC’s, believe it or not, not so excited about the President using it, as much as, “Well, how much did he pay you?” because now you’re in the post‑revenue zone. [**Patrick notes**: I respectfully disagree with Matt and strongly suggest that if you have the line “if @current_user.is_president_obama? {…}” anywhere in your codebase you mention that early and often in pitches. It got quite a lot of attention when I was talking Stormpulse up to people.]  If you’re going to do it on eyeballs, then I suggest you stay in the pre‑revenue zone, or be prepared to quickly accelerate the revenue aspects. We basically poured six and a half million people through a very large funnel, and 1,000 customers came out the other end. Then when you have a conversation with somebody, and you say, “Yes, we have 195 customers”, or you say, “We have close to 1,000 customers,” totally different order of magnitude.


Speaking of which, Gabriel Weinberg wrote a recent blog post on, “Orders of Magnitude”, and I think that’s really, in many ways, what getting VC’s excited is about, is proving that you hit that next order of magnitude, and the next order of magnitude is just around the corner, so this 195,000 is about to become 1.95 million, and soon after that, in two years, we can see it being 19.5 million. If you can keep moving the decimal points, on any metric, than you’re probably in good shape. [laughs]


**Patrick**:  Right, we should talk a little bit about the difference between angels, and VCs. Angels are typically people who are investing their own personal money. A VC, Venture Capitalists have what’s called, “limited partners” (LPs) in the Venture Capital funds. Which are typically extraordinary wealthy families like, Bill Gates wealthy, or institutional investors like, pension funds, or Harvard Endowment, which has billions, and billions of dollars of assets. They take a small portion of those assets, like the majority are in more traditional investments, like stocks and bonds, like that you and I could buy.


A small portion of that is their risk capital, that they allocate to quickly growing businesses. The Harvard Endowment does not want to be dealing with entrepreneurs themselves, they write a check for for $10 million or $20 million to a venture capital fund. The venture capital fund takes four of those checks put together, collects $50 million dollars, and then attempts to dribble it out to entrepreneurs in investments in the single-digit millions range.


The incentives in the structure of angels, and VC’s are different, in particular, with regards to scale. Paul Graham has a great [essay](http://www.paulgraham.com/future.html) or two that will teach you the basics [**Patrick notes**: “basics” relative to what he knows, rather than relative to what I know, since he’s forgotten more than I know.  Most relevantly for people listening to this conversation, the scale of exit that can be a win for an angel is orders of magnitude lower than the scale of exit that could be a win for a VC.


Not talking about Stormpulse here, but hypothetically assume I had a second angel investment, which I don’t currently.


If I invested at a hypothetical valuation of a million dollars, and it sold for $10 million dollars, then plus or minus some rounding error due to dilution that 10Xes my investment in the company.  That would be a happy result for me, as an angel.  For a VC fund, if a company exits for $10 million, that goes into their books as a loss, because they did not hit the multiple hundreds of millions of dollars exit, that they need to make the numbers in their business model to work out. If they collect a lot of losses like that, they will not be able to close their next fund. It would really suck to be them. [**Patrick notes**: Important corollary to this: VC firms do not win on acqu-hires, where e.g. a 5-man engineering team gets bought out for $5 million and their project gets scrapped.]


Angels can be pretty happy with exits in millions of dollars to tens of millions of dollars range. The super angels, which are the angels investing other people’s money, like I think 500 Startups themselves might self-identify as one, can be pretty happy with exits in the $10 million, $30 million, $50 million, on up from there, and then once you get into VC land, and have reached that serious investment, you’re shooting for in the hundreds of millions of dollars range.


After you get Series B / Series C / etc VC, and what not, God help you, you better IPO or no soup for you.  Those are for exit valuations, by the way. The interplay between a company’s revenue, and a company’s exit valuation is complicated, depending on who’s doing the buying. For example, if you were Google, and you had strategic reasons to control the Internet, you might pay a heft premium on the revenue of a company like e.g. Youtube.  [**Patrick notes**: Or Facebook and Instagram, etc etc.]


As a rule of thumb: if you’re trying to meet the victory condition for your investors of the exit in the mid tens of millions range, you should be thinking of having millions of dollars to low tens of millions of dollars in revenue.  Revenue requirements scale up linearly from there with exit requirements. All that sounds fairly on point to you?


**Matt**:  Yeah, I would say so. [laughs] If I were going out and raising money again for the first time, what I wish I had really understood is very much what you just said. One thing that can help you is, if you’re looking at a VC firm, not all VC firms are the same in terms of fund size. How much money they got from those LPs can vary anywhere from as “tiny” as say $20 million, all the way up to $1 billion or more. That size of their fund is going to greatly influence how much money it takes to, as they say in VC and entrepreneur parlance, “move the needle.”


The needle on the dashboard of the VC’s car does not move if they have a $500 million fund, and they got, let’s see, let’s say you sold your company for $50 million, and they owned 33 percent, then they get their $16.6 million.  That doesn’t really do anything for them whatsoever, like you said.


For that $500 million fund, they want to own a larger stake in a company that sells for $500 million plus. As a rule of thumb which might be controversial: **you should aim to sell for more than their fund size**.


If you’re approaching a $500 million fund, and you’re thinking your company is a $50 million exit, you are probably are wasting your time. Unless, they get so excited that they convince you that it could be sold for $500 million instead, or there’s just something you don’t know. A $50 million VC fund, which would be a micro VC, could be extremely excited about that, $10, $20, $30, $40 million exit, $50 million even better. Obviously, no VC is going to turn down more than that.


If Sequoia sells a company for a billion dollars, and their fund size is $1.5 billion, they’re pretty happy about that, obviously. You got to know who you’re partnering up with.


**Patrick**:  Yes, all true advice. Just as a rough rule of thumb for people playing along at home. In VC fund typically invests for a period of 10 years, within that 10 years they want to have experts that approach a particular internal rate of return. It works out to be that, as a rule of thumb, they want to triple their money. If it’s a $50 million funds, then they have to achieve $150 million of return, which, if they own 10 percent of typical company at exit, actually, they have to sell $1.5 billion worth of companies. Do the math there. It doesn’t support many $2 million exits.  [**Patrick notes**: Especially because the number of investments they can make is limited by the number of board seats they can take up.  Paul Graham can explain [why that matters](http://www.paulgraham.com/superangels.html).]


**Matt**:  One thing to mention as well, which, maybe this fund raising 201, instead of 101, but it’s important when you’re talking about angels and VCs, is that, many angels will often get the opportunity to exit earlier. If the company, you don’t have to go IPO, for example, and many angels won’t. When the company that took an angel investments ends up raising money at triple the valuation of that angel round, some of that money that comes in could very well go into the pockets of angels, so that that VC can buy them out, and own their share of the company. If a VC comes in and says, “I want to own 40 percent of this,” and on the books, there’s 10 percent equity in angels’ pockets, those angels will often be bought out completely, and get their three X, and then take it, and play with again, and the VC is now in for the longer haul.


Of course, some VCs that get in very early in companies that end up going huge, could also do that, if you end up raising a series B, C, or D. Yeah, there’s multiple ways for folks to make money. Angels are, generally not in it for the IPO.


That’s where 500 Startups is really interesting, right, because they’ll put in a very small angel sized check. They’ll wait for the cream to rise. They’ll invest again, in those companies that are winning. They will hold on for a long time. Obviously, it’s a great hybrid model, I think, part of the reason I’m excited to have them involved.


## Why You Probably Shouldn’t Be An Angel Investor, via Crowdfunding Or Otherwise


**Patrick**:  Right, I really liked how 500 Startups and YC are both doing excellent things to bring a  bit more rationality and efficiency, and to the VC markets, so yay capitalism . Some folks listening along to this and might think, “Wow, this is wonderful, I want to be an angel investor.”


**Matt**:  [laughs]


**Patrick**:  **I want to disabuse you from that notion, right now.  For the vast majority of people listening to this, angel investment is not a good idea.**


**Matt**:  [laughs]


**Patrick**:  First, there’s a requirement, which might be eased with the crowdfunding legislation coming down the pipe. At the moment, you largely can’t invest in companies unless you are an accredited investor.  You can look up the [requirements](http://www.sec.gov/answers/accred.htm) for being an accredited investor online, but I think it requires $1 million in assets, outside of the value of your primary residence, or $250,000 in income for each of the last two years.


(People might be wondering: “Wait, if this is true, then Patrick must be an accredited investor. How in the heck did he get to one of those [given that it doesn’t appear on my yearly reports]?” The answer to that is, well, that gives you one data point on how Appointment Reminder is doing.)


Yeah. Even for people who are clearly in a fairly decent financial position, angel investing is incredibly risky. **Most people will get wiped out totally**. I don’t expect getting wiped out in Stormpulse obviously, but if a meteor struck Dallas [**Patrick notes**: Dallas, Austin, whatever, if you can’t find Gifu on a map cut me some slack] and was not predicted by the Stormpulse software, it would not compromise the ability of my wife and I to make the rent.


**Matt**:  Right. [laughs] Thank goodness. [laughs]


**Patrick**:  Yeah. The vast majority of my investment assets are in nice traditional Roth IRA investing in index funds. Many angels, by the way, are doing it for I’d say primarily non‑economic reasons. Again, structurally you have to be fairly wealthy to invest as an angel investor. The expected returns are terrible. It takes a lot of time to make investments, relative to say an index fund. Since you can only safely invest a small portion of your net worth in it, it’s not likely to really move the needle on your personal portfolio, so “Why do it?” is an interesting question. One of the reasons that there’s lots and lots of angels doing it is it’s a hobby/lifestyle choice of some people.


Particularly in Silicon Valley, there’s lots of angel investors who might have a bit of money because they were in large companies in the Valley that do social networking or search engines at the right time. They have a bit of money, and the culture in the Valley doesn’t really let you blow money on super deluxe sports cars or anything, but blowing money on angel investments is considered a wonderful thing to talk about with your friends. That’s one reason why people might do it.


Again, for me, it’s partly wanting to support Stormpulse. I want it to win.  I’m a capitalist: companies live, companies die, that happens. I liked the guy’s vision for the future, and supporting this guy is my main objective.


**Matt**:  Yeah.


**Patrick**:  Obviously I’m not saying the same about Zynga.  Zynga’s vision for the future is humanity enslaved to dopamine treadmills.


**Matt**:  [laughs] Yes, scary. I was going to add, my one cent on that would be you’re absolutely right. Angel investing, I’m not [laughs] nowhere near being an angel investor. Even though I’m an entrepreneur and I love the risk taking parts, I don’t know that I would ever be interested in angel investing. Simply because in order for it to work economically, you’d have to do it at such a scale, so I guess maybe rephrase that. I don’t think I’d ever be interested for economic reasons either, even just looking forward. Because in order for the economics to work, you would have to invest in so many companies that you would have to take a…Not spray and pray, because that’s negative way to look at it, but a making a lot of bets method.


Yeah, the angel investing that seems to work emotionally, even though it might not economically, would be the, “I’m investing in these guys because I love what they’re doing and I think I can help them.” That’s the more popular choice, like you said. The no man’s land in between is the, “Oh, great, I can invest $20,000,” and you hand it to three people or one person, and there went $20,000.


Hopefully it’s not that. Yeah, we’ll see that whole piece works out on AngelList, where people can invest even if they’re not accredited or down to $1,000.  [**Patrick notes**: There are a few crowdfunding platforms coming which have this basic business model.] For that really to work economically for somebody, they would need to make a lot of $1,000 investments I think.


**Patrick**:  Right. I don’t know that crowdfunding is a very wonderful idea to be honest.  The model is that sometimes the business would like money which comes with no involvement with the angels whatsoever, like we were talking about earlier . For a $1,000 investment to be attractive to the firm, you would have to raise that much from each of 200 people, and your service level agreement (SLA) with respect to each of them would be “You should follow our twitter feed, but we’ll never actually talk to you about this”. Otherwise the economics of raising the marginal $1,000 just don’t make sense. [**Patrick notes**: In particular, the angels would not have any expectation of being able to talk to the founders on a regular basis and would not be given updates which include material non-public information.  Both of those are routine features of angel/startup relationships in the status quo.]


**Matt**:  Right. There’s a little bit of a, I don’t know, a selection bias that happens though, or availability bias because if you think about it a lot of the best start ups aren’t looking for those dollars. They’re not necessarily desperate for another $1,000 investment or are looking for that kind of crowdsourced funding.


**Patrick**:  You called it an availability bias, but I might call it a…oh shoot, my English capacity is failing me.


**Matt**:  Just say it in Japanese. [laughs]


**Patrick**:  Adverse selection process.


**Matt**:  Yeah.


**Patrick**:  The people who have the most compelling businesses can get professional investments by the experts into those most compelling businesses, and people who don’t have quite so compelling businesses, but might still want to raise some money, might go to folks who are wealthy but amateurish with respect to their investment decisions. Again, this isn’t a pronouncement from on high because I am also an amateur here, but one would hope I know a bit more about it than, say, any random software engineer at a company that pays a lot of money.


**Matt**:  Yeah. [laughs]


**Patrick**:  If the cream of the crop gets picked by the professional investors and the professional investors don’t do really wonderfully numerically investing, the median return in “VC land” is probably negative.


**Matt**:  Yeah.


**Patrick**:  If professional investors who can convince people to give them $20,000,000 checks have a return which is median negative, then amateur investors investing in the non cream of the crop companies are probably not going to do well virtually for themselves.


**Matt**:  Probably not.


**Patrick**:  Don’t go angel investing with money you can’t afford to lose. **The one positive thing that I’ll say about angel investing is at least it’s better than Bitcoin**.  [**Patrick notes**: I might write a post on that someday.  Long story short: don’t buy Bitcoin.]


**Matt**:  [laughs] Sounds like.


**Patrick**:  Let’s talk like the mechanics of it because we’ve been talking about investing in high level terms. I think a lot of people will understand it as like me buying stock in your company, but that isn’t really what happens.


**Matt**:  No. It can be but [laughs] it really depends on the type of raise, right? What you do…Go ahead.


**Patrick**:  For angel investing these days for decreasing the paper work burden and getting away from needing to price around the, I don’t know if I would call it a standard, but very popular action is called a convertible note. Do you want to explain to the audience what a convertible note is?


**Matt**:  Yeah, sure. A convertible not is basically a loan with a fancy name and some fancy options, which are the angel investor or the investor loans the start up money, and there’s a maturity date on the loan just like all loans, but prior to that maturity date, since this investor does not just want to get his money back with a per annum interest rate return, before that happens there is what’s called a trigger event or a fund raise that happens, which triggers the conversion, hence the word convertible, of that money into some stock equivalent. What it basically means is, for example somebody gives somebody $25,000 on a convertible note basis, that entrepreneur then will see that $25,000 on their books as a liability [**Patrick notes**: And, naturally, an asset of $25,000 cash] until the time that, that entrepreneur raises a qualified financing, which could be any amount. Let’s just say it’s $750,000. Once he raises that $750,000 from a VC or from more angels, however it works out for him, then that $25,000 will turn into shares.


Now that investor actually has stock in that company. Until then he really just had a loan against them. Like you said, it definitely decreases the paper work. It also has, for the entrepreneurs benefit, you could have what’s called a rolling close.


Back in the selling-equity world you had more like closing on a house where this is the day they hand over the keys, everything’s done, this is my closing date. In the convertible note world you can have multiple closing dates. You can take money from, if you have a line of 15 angel investors and somebody wants to give you money today, you can take the money from them. If the other people aren’t quite ready yet, or if you’re still warming up some people, you can get them in the door later.


You might end up spending 30 days or 60 days collecting checks, which frees you up from having to have one massive convergence point, which is really hard to do because angels as opposed to VCs often have real lives and jobs and their own things to deal with so it’s not their entire job to make sure they have the bank wire all teed up for the exact day that it’s supposed to be. A lot of things just come easier when go with that method, but obviously it can have its downsides but I think if you understand it well enough the downsides are not shockers.


**Patrick**:  Right. If you want to hear this subject in a lot more detail, there’s a Paul Graham essay called [High Resolution Fundraising](http://www.paulgraham.com/hiresfund.html), which assesses the benefits in a lot of detail. One of the main benefits is again, investors are “herd creatures”, and what you’ll frequently hear is “I’m willing to invest if everybody else is willing to invest.” Given that angels include a lot of different people on varying levels of enthusiasm and sophistication and ability to access funds quickly, this can cause an unpleasant deadlock situation where “A is willing to invest if B is willing to invest, and B is willing to invest if C is willing to invest, and C is willing to invest if D is willing to invest, and D is currently on vacation to Europe, but then he’s willing to invest if A is willing to invest.”  Then nothing goes forward and you, the entrepreneur, tear your hair out.


Whereas with convertible note, literally the only thing Matt needed to do to raise money from me was we agreed on an amount, he sent over the docs, I signed them, and then I wired money to the Stormpulse account. No collusion with other investors was necessary.  I didn’t even explicitly knew who the other investors were. I was sold, so I didn’t know how many other investors were there at the time and I didn’t really have need of them.


**Matt**:  Yeah.


**Patrick**:  Obviously after you have money in the bank you can say, “I have money in the bank from people, so if you want in on this you should move quickly.”


**Matt**:  Yep.


**Patrick**:  Which again is a wonderful thing from the entrepreneur’s perspective.


We mentioned the figure $25,000 a few times. Typically, historically in angel investing, like $25,000 is the minimum size of the checks that can get a company interested in you just because of the amount of overhead it takes to bring on an initial investor and the amount of overhead that that entails going forward. That’s kind of like the baseline these days, unless you have something else that can interest the company besides just the dollar value of your investment. Are you OK with putting the number of what our investment was? I’m happy mentioning it, but I don’t know if that’s public or not.


**Matt**:  I would say this, it’s under the $25,000 number for precisely that reason, because I believe you have incredible value add for us. You made the introduction to 500 Startups and it turns out that you know a thing or two about SEO, SEM and all things Internet marketing. This is one of those cases where the dollar value isn’t the primary concern.


**Patrick**:  When I told Matt that I wanted to invest with him I said, “I want to invest somewhere between $5,000 and $25,000 with you and after you talk to my wife a bit.” In the process of talking to my wife about it, I got the bill for my wedding and eventually decided to, well, there’s a Macbook with my name on it somewhere.


**Matt**:  [laughs]


**Patrick**:  I don’t know. OK, let’s see, so we talked about convertible debt and talked about risk management for angels. I would be negligent in my duties as an investor if I didn’t mention you were trying to close another round, right?  There’s the sales pitch, guys. There is availability. Those of you who can make use of that information, please do.


**Matt**:  Thanks, Patrick.


**Patrick**:  You’re also all over AngelList. We could devote an entire podcast to the wonderfulness of angel list, but it’s the emerging standard for people raising early rounds, it helps to get a lot of the necessity of meeting social proof and whatnot. But you have a wonderfully [active profile](http://angel.co/stormpulse) on AngelList and people can easily reach out directly to you if they want to talk about this in more detail, assuming they have a checkbook with lots of zeros in it.


**Matt**:  Sure. Or know somebody that does.


## How To Price Software Which Is Mission Critical For Business Customers


**Patrick**:  Awesome. I gave a little mini‑sales pitch. Why don’t we talk for folks who might or might not be interested in the whole funded start‑up amusement game, just in terms of running a business, and running a SaaS business at emerging levels of scale? Why don’t we talk about what was learned for pricing for your business and premium versus premium distinction, and maybe some advice on doing high‑touch sales and what many folks listening are doing, which is currently just, “I hope people click over to /pricing and then put in their details into my credit card sign up form.”


**Matt**:  Sure. [laughs]


**Patrick**:  Let’s see, how did you pick $750 per user, per year?


**Matt**:  How about “We are growing the price and that is its current height”. Like I have an adolescent son and he’s getting taller and taller. Seven‑fifty is his current height. I think it can go higher from there. Definitely can go higher from there as we get into more editions, that just ended up being the price that we are experimenting with currently. We actually started out with a business that was $3.95 per month. [laughs] Now we are asking for $749 upfront. Yes, that’s a 200X price increase, more or less, since we started.


**Patrick**:  **One takeaway from this podcast, for anybody attempting to run a business on $3.95 a month, don’t.** It won’t work out. It is impossible to make the math work out like that, for any desired scale of the business. Actually, I won’t want to say impossible, there’s people who can do it. [**Patrick notes**: Backblaze?  Evernote?  That’s all I can think of off the top of my head.] But what would be the main challenge for you in your business? You’re providing, again saving people’s lives and property value or even adding a level of value to a business you can justify to people picking that $20 to $30 entrance at the low end and then it goes up from there in a very dramatic direction as you create more value.


**Matt**:  Yeah, I mean what…


**Patrick**:  Oh, sorry. You go.


**Matt**:  Yeah, I was going to add one little psychological touch. As soon as you start running your own business, and I’m sure you’ve experienced this, too, is when you get to something and in your business, you want it or need it, and it says that it’s $100 or $200, I don’t think that’s ever stopped you in your tracks and made you think, “Oh, that’s too expensive. I don’t want that.” Especially in B2B, in other words, B2C, obviously your mileage will vary greatly, but in B2B, there aren’t many business who can’t justify a $500 expense on something they just want or need.


It can be very hard for an entrepreneur who’s only been either employed by BitCo and hasn’t had a budget that they can just spend money willy‑nilly or hasn’t run their own business to get out of that impoverished mindset of “Well, gee, with my bootstrap company, I would never spend $500 on this.” It’s like, “Yes, but you are not your own customer in this case.” [laughs]


**Patrick**:  I have every love for bootstraped companies in the world. They’re my heart and soul business‑wise, but oh, boy. When we talk about this kind of stuff on Hacker News, people come out of the woodwork, “Oh man, you’re doing this thing for professional programmers that costs as much as $20 a month.” Or, $150. “Who on God’s green earth will pay that?” Yadda, yadda, yadda.


**Matt**:  [laughs]


**Patrick**:  Compared to like the budget available to the White House for protecting against hurricanes, Bingo Card Creator, *pretty freaking small.* Bingo Card Creator can drop $150 without me even noticing it.


**Matt**:  Take that, yep.


**Patrick**:  Yep. If KissMetrics costs $150 a month, it’s done. If it increases sales by five percent over the year, it pays for itself in perpetuity, which that might be what I paid for…that might be what I paid for  KissMetrics…I don’t even know what I paid for  KissMetrics, and the reason is, ***it doesn’t matter***.


**Matt**:  Right. [laughter]


**Patrick**:  Again, that’s a business that makes what, three, four, five thousand a month or so, somewhere in there. At the smallest possible scale of business, the prices that people want to charge for software don’t matter. Don’t optimize very aggressively for never getting complaints about pricing. It is not the way forward.


You guys have just the one pricing point. We’ll talk about that in more detail at some point, but we might want that conversation to be private. Anyhow, one of the reasons a lot of companies have multiple pricing points is that it helps segment and capture value.


There is a difference in the ability of Bingo Card Creator and the White House to afford things. How do you segment the usage of those two organizations such that the White House pays more for the extra service they are getting out of the software? That’s one of the reasons that you see the four column pricing plan on a lot of SaaS, typically because it prints a lot of money as soon as you introduce it.


Just as an aside, for people I have talked to, SaaS businesses, like it’s my job.  A lot of folks report that those plans generates an absurd portion of revenue. I’ll say, for Appointment Reminder, the top-most plan ($199) generates about 50% of the revenue of the publicly available plans ($9/$29/$79/$199)  [**Patrick notes**: Closer to 1/3rd when I checked the numbers recently.]


Don’t do a $9 plan either, it’s not practical if you’re selling to businesses. Lesson learned. You might think $200 is pretty rich, but it isn’t for a company, so give people the option to pay at least that much.


**Matt**:  Sure.


**Patrick**:  The $200 is not really the ceiling for selling to businesses. For selling to businesses, typically the ceiling for a month‑to‑month plan is generally $500 and they can put that on a credit card without requiring eight or 12 signatures for management. Then after $500 you have to step up your game a little because it’s not being so much of a self‑service model. You actually do have to talk to folks. I have a bit of experience with this. You have much more. There’s adjustments you have to make when it’s no longer just a website. You have to prove yourself, and you’re actually talking to folks. How does that process work for you?


## How To Sell Into The Enterprise


**Matt**:  Yeah, the process for us started by email, just having a simple email address, which hopefully, everybody has, getting those initial queries from people who say, “I want to buy this but I have a few questions first.” Answering those emails is obviously a great way if you can scale it up to a point. But then, at some point, like you said, there is definitely the right time and place to have a actual phone call, maybe a couple, or maybe a lot of them if it’s going to be a large deal. For me, that really started with sending emails to people and responding with, “Hey, call my cell phone number” kind of thing, a typical self‑starter, entrepreneur kind of method. Got a 1‑800 number from Grasshopper.com not soon after that, and ended up routing people through the 1‑800 number which then rings whatever phone we want in the business, and talking to people that way.


With our business, especially since, weather tracking in the abstract is not very emotional but when you apply, like you said, the lives and properties to it, people generally want to have a human being on the end of the line if they’re going to spend a lot of money, just to be assured that it’s going to do what they think it’s going to do. Or just to understand the right way to pay, things of that nature.


We take phone calls. We have a 1‑800 number for our sales line, and I love it when people call because it generally means that we’re going to have an opportunity to make good contact. It increases the likelihood that they’ll be retained. All kinds of good stuff happen when you talk to people on the phone, as long as you can do it profitably.


**Patrick**:  Right, and again, this is one of the differences between the stuff that you have to do when you’re trying to grow the business like that and stuff you have to do as a bootstrapper. I live in Japan, and so folks calling my cell phone directly or even indirectly through the 800 number that’s on the website would be inconvenient because it would typically land at about 4 AM in the morning. Though I like doing enterprise sales. I don’t love getting woken up at 4 AM in the morning. I drop everybody who calls the sales line straight to voicemail and then attempt to set up a time to call them, typically at about midnight because I keep engineers hours. I apologize to my wife, say I’m going to get on a phone call for half an hour, do it and then go to bed.


Just an FYI, when I do that, **half the people will hang up immediately when they get to voicemail**. You get no information from them and I have never closed a sale like that. If you’re beholden to investors, don’t do it that way. But if you’re a bootstrapper who can control the pace of growth of your business at whatever you want, it totally does work.


We both come from engineering backgrounds, so this is not exactly in our wheelhouse, constitutionally or by experience. We both learned how to do business to business sales over the years, and it’s amazing. People will actually pay money to people that they’ve only ever met on a phone call.  Lots of money! [laughs]


**Matt**:  Yes. Yeah, absolutely.


**Patrick**:  Let’s see, what stories can I tell? Again, never lie to a customer. I always be very up front with people and say, “Hey, I’m a one-man operation operating outside of Japan. I’m a professional at this,” and oft times it’s pretty good. “All the problems like, “My bus number is one, yadda yadda yadda,” if they ask about that. Appointment Reminder is currently operating in, I usually say eight of the top 10 hospitals in the United States. I’m not sure if that’s actually true. A, there’s more than eight now, and B, I’m not sure if my definition of the top 10 is reasonably rigorous. Suffice it to say, if you name a big brand hospital, Appointment Reminder might be running it. Matt, again, from his home office sold into the White House. I will never get tired of telling that story.


**Matt**:  [laughs] The craziest part about it, Patrick, is that I didn’t do that sale. [laughs] I had no idea that it even happened!


**Patrick**:  Oh, that’s right. They signed up on your website directly.


**Matt**:  Yeah. That was self serve, man. [laughter]


**Patrick**:  Oh, boy. Life is wonderful.


**Matt**:  Yeah, yeah, yeah. [laughs] Yes.


**Patrick**:  Just a quick piece of advice that folks listening at home can steal. One of the things that you can do if you’re not at a position where you can jump quick onto a sales call with somebody, maybe they’re not at that point in the relationship: use some incentive on your website to capture their email address. For example, if I were Matt, after you get the other 5,000 things off the plate, create some resource or white paper about managing severe weather events at your business, maybe specific to a particular industry.  Offer a download of this white paper if you give us your email address and say on that form “We’re going to get in touch with you every week with stuff you’ll find interesting, as a risk manager at a retail business.”


Then you will have the opportunity to provide them with stuff they’ll find interesting, and then eventually, after you’ve established credibility, attempt to sell them. That works out very, very well in terms of generating sales.


**Matt**:  Yeah, and you know what? I’ll say this. Because life is messy and it happens organically whether we like it or not, we’ve done almost everything backwards with Stormpulse. These days, I think somebody who wants to bootstrap a company has so much good advice to rely on.


**Patrick**:  Every company ever will tell you they did everything  wrong starting out. [laughter]


**Matt**:  Well, somebody who wants to bootstrap a company these days might say, “OK, here’s what I’m going to do. I’m going to charge from day one. I’m going to build this thing. Here’s the funnel that we’re going to use. Here’s the flow we’re going to use. It’s just this machine.” We are working on the machine right now, but the machine originally was just this tipping point in our distribution with Hurricane Ike hitting Houston, that took us from 1,000 to 1,000,000 visitors in 45 days. Our servers didn’t crash, but all of a sudden we were inundated with interest from people that…We were like the two guys at the hot dog stand that all of the sudden all of Milwaukee wants to come to. How do you handle that?


We didn’t have the great landing pages and stuff I’d like to talk to you about more offline. We didn’t have the great segmented landing page with the white paper download and the free trial thing set up. It was just people loved this product so much that they had to talk to us. They wanted to talk to us and they wanted to buy it, and so they did. Here I am getting emails from people saying, “Send me an invoice,” and I’m going, “I don’t even have a template for that.”


[laughter]


**Matt**:  I was just slammed with a lot of the operational stuff from the get go. [**Patrick notes**: Again, after years of working in the trenches.] There was a fair amount of self service, but definitely people…Learning trial by fire in a lot of ways. I’m sitting here looking at in front of me a receipt from, it so happens to be a hospital that uses our software. I’m looking at an invoice number, and it says 36215. What’s great about that, and if this is helpful to anybody, or at least an encouragement, that invoice number is a number that we *completely made up*. It was like here’s a piece of paper. We’re going to put some numbers on it. We’re going to send it to them. The first time I got a check from somebody that was a real company, like a Fortune 500 company, paying an invoice that I had *just made up* was like this moment of clarity.


Something came in and something came out. The plumbing works. I guess the encouragement would be don’t freak out when you get these things. In a lot of ways, you’re always in this just‑make‑it‑up stage until it works, and then you can refine it and make it look more professional.


I still have copies of the first invoices I sent out. It was like I don’t even know what I was thinking. I hate to think what the person that received them was thinking. It was the world’s least elegant invoice, but it had a number and it had a price and it had a few other details. That’s all it took. B2B is full of wonder.


**Patrick**:  That’s the story that you’re going to hear again and again and again, both bootstrapping and funded. There’s a whole lot of making it up as you go along. There’s obviously some folks who sold to the Fortune 500 prior to the two of us living, so some of the stuff you take the knocks and figure out and some of it, you talk to your mentors/buddies/whoever you find credible and figure out. This is one reason why doing things with email is helpful. It’s asynchronous, so when somebody says, “Hey, to buy this, we need proof of insurance from your company,” you can email somebody who has been in business a little while longer would say, “A hospital has asked me for proof of insurance. What does that mean?” It means say that you buy, in my case, $2,000 worth of insurance.


That takes a week of your life to get arranged, and then you can invoice the hospital enough for the software to handily pay for the insurance coverage, to put it mildly. By the way, for folks who are not in business, if you’re talking about, $500 per month is the upper reaches of the self‑serve model over the Internet. The price of software is unbounded. I think it probably wouldn’t be good to mention actual numbers from either of our companies that are the largest contracts.


Let’s say that software sold at low five figures, mid five figures, high five figures, low six figures, mid six figures, high six figures and up, up, up. It all depends on the value you’re offering and getting that customer to “yes.” Astoundingly, one of the reasons that folks don’t put prices on the website for the enterprise plans is that the only thing you need to do to get, pick a number, $100,000, out of a company is to convince them that the thing your selling is worth $100,000. Any truthful and ethical thing you do get this when you do that “yes” is what you need to get that “yes.”


**Matt**:  Exactly, and I can tell you from some experience now that what is helpful is when you’re selling B2B, there’s obviously the super scalable part. Enterprise is where you get to the point, I think, and I’m not even a true what you call the Palantir Enterprise or like the massive trilogy enterprise. Those are seven figure deals. When you’re talking about even the high five figures, low six figures, you are at that point. You are external to their company, but what you’re trying to do is actually navigate their company and the way they make a decision about whether or not it’s worth the $100,000.  They’re going to have their own way of managing that decision‑making. You are now trying to manage their management of it so that it does not get off course. [laughs]


In some sense, you are like the CEO of the buying process happening internal to your prospective customer, right?


**Patrick**:  This is probably the most important think that I’ve ever learned about doing the sales at enterprises. Basically, if there’s an internal person who wants to buy it, there’s other people that their management process means they have to convince to be able to buy it. You have to empower them. People call them your “internal champion.” You have to give them anything they need to get those sign‑offs. Which means both, A, figuring out who those people are and, B, figure out what you need to give them to get to “yes.” Your customer might not know these answers, because they aren’t experts at working their own purchasing department. This is the art and science because it’s different for every contract.


**Matt**:  Yeah.


**Patrick**:  I’ll tell a quick story from my first big enterprise deal for [Appointment Reminder](https://www.appointmentreminder.org). A hospital sent out 10 requests for proposals to 10 firms who could theoretically provide appointment reminder phone‑calls for their purposes. It was for a low‑budget project, so the larger firms in the industry got that RFP and I imagine that the sales guy’s reaction was “Beep this. I’m only going to make $100 commission off of writing this, so I’m not actually going to write a detailed response to it. I’m just going to send them a brocure and say, ‘Hey, I’ll hop on a call if you’ve got your checkbook out.’”


We’re a little hungrier than those organizations, both because I get more out of the entirety of a sale than the commission a sales guy would make, and because I very urgently wanted the social proof of having landed this contract. So I wrote a detailed 3 page response to the RFP, including quite a bit of detail that the average sales guy wouldn’t know.


Then I got on for an hour-long phone call with a nurse at this hospital, and we talked about every concern she had. After that hour long phone call, I took my (obsessive) notes, typed up a detailed response for every issue raised on the call, and emailed it to her.  I asked if she would please forward it to every stakeholder involved with the purchase, including every name she had mentioned on the call.


“Could you please forward this to Dave and Dr. Larry as well, just so they know the stuff we talked about?” Later when they had a discussion inside the hospital on whether to guy for the safe 800 pound gorilla or the little one-man operation operating outside of Japan, I was the only guy whose name they knew. They had seen emails from me and I sounded knowledgeable and trustworthy.  The nurse I had talked to also had a good impression from our phone calls.


She said a different stakeholder attempted to say, “Well, nobody ever got fired for choosing IBM, or the analog in our industry.” She said, “No, you don’t understand. I don’t know that company. I think they brushed us off, but *this is Patrick’s baby*. You take care of your baby. If we ever have a problem with it, we know exactly who we’re going to be dealing with, and he’ll fix it for us. I trust him,” and that argument carried the day.


**Matt**:  Awesome.


**Patrick**:  That’s how you beat out a company that is a thousand times bigger than you, which is a story that I’m quite certain has gotten Stormpulse a couple of wins along the way.


**Matt**:  Oh, yeah. Yeah.


**Patrick**:  Founders have an incredible advantage on sales, by the way, because you’ve got magical founder advantages when you can announce yourself as the founder or CEO or head of product, or whatever you need to be here for the phone call. People will say, “Wow, thanks for taking the time to call me!” It’s amazing. Here’s a hospital who has probably a billion dollars in gross revenue a year or some multiple of that, versus a teeny-tiny little software company whose annual revenue is probably smaller than identifiable surgeries that they do. But if you announce yourself to the hospital as, “Yeah, I’m the founder of the company that you’re talking to,” then the person at the hospital’s like, “Wow. I’m just a little person at this big hospital. This guy is the head honcho — he is really doing me a solid by getting me this phone call.” Despite the fact that I’m the founder, sole employee, and also the guy who empties out the waste paper basket every day.


**Matt**:  Yeah. [laughs]


**Patrick**:  Also, especially for founders who have both the technical and business sense, you’re able to talk about whatever they need to talk about. A sales guy will often say, “Oh, let me get back to you about that question because I need to ask the engineers.” Or even worse they’ll say, “Oh yeah, I can totally do that,” and just be lying and sound like they’re lying, because they don’t have the ring of truth in their voice. Whereas if you’re a founder you can say, “OK, the software doesn’t actually do that right now, but it sounds like something that we could get done in about two weeks. How important is this to you vis‑a‑vis your other priorities, or is there some other way we could meet this need?” When you start talking that level of detail, people will be like, “Wow, he knows what he’s talking about, unlike every other sales guy I’ve been talking to this week.”


**Matt**:  Yeah. Absolutely.


**Patrick**:  Not that I hate sales guys.


**Matt**:  [laughs]


**Patrick**:  Good sales guys are wonderful, but good sales are like good engineers because they’re very rare.


**Matt**:  Yeah. No, absolutely, absolutely.


**Patrick**:  Yeah. I think we’re probably pushing the two hour mark for this conversation, so we probably want to be wrapping up now. Matt, is there a blog that people can find you at? What’s the URL for that?


**Matt**:  Yeah. It’s [here](http://wensing.tumblr.com/). You can also find me on Twitter @MattWensing.


**Patrick:** My blog is at http://wwww.kalzumeus.com/blog/ and I’m Patio11 all over the Internet. Stormpulse is the website, storm like the weather phenomenon, pulse like the pulse of the nation, dot com. You can take a look at it, attempt to invest in it, etc.  If you’re needing to protect the lives and property of your business, it’s good stuff, consider buying it.


Thanks so much for getting on the podcast, Matt. It was an awesome conversation, and I hope the audience learned something from it.


**Matt**:  Yeah, absolutely. Thanks a lot, Patrick.


**Patrick**:  OK, and thanks very much to all you guys who are listening. I know it’s been a long wait since the last one. I really appreciate you taking time out of your day with us. We will see you again next time, hopefully in a shorter timeframe than the six months or so it took for podcast number four. All right, till next time, bye‑bye.


**Matt**:  Bye.
