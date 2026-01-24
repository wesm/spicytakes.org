---
title: "Complaint-Driven Development"
date: 2014-02-18
url: https://blog.codinghorror.com/complaint-driven-development/
slug: complaint-driven-development
word_count: 1356
---

If I haven’t blogged much in the last year, it’s because we’ve been busy building that [civilized discourse construction kit](https://blog.codinghorror.com/civilized-discourse-construction-kit/) thing I talked about.


![](https://blog.codinghorror.com/content/images/2025/02/image-149.png)


(Yes, that’s actually the name of the company. This is what happens when you put me in charge of naming things. [Pinball machines](http://en.wikipedia.org/wiki/Pinball_Construction_Set), people, what’s the difference? I’ve apologized to Bill Budge already.)


So if you, like my investors, are wondering why this process took [a whole entire year](http://blog.discourse.org/2014/02/one-year-of-discourse/), I should explain **how I build things**, or at least, how we built Stack Overflow and [Stack Exchange](http://stackexchange.com/) and now [Discourse](http://www.discourse.org/):

1. Do a ton of detailed research on everything out there in your space. The successes: what are they getting wrong? The failures: what did they get right? Nobody should know more about the history of your area than you do. Have a story that makes sense, something you believe in, and more importantly, a story you can get others to believe in.
2. Based on this research, assemble a team and build the minimum viable product that does something useful. If you need seed funding, this is the time to get it, so I hope you’re pretty good at all that stuff in step 1, and maybe famous too, and ideally already successful as well, otherwise you are screwed.
3. Have your team and yourself start using that minimum viable product, every day, all day long. This is way more than mere software development: *it’s your whole life*. If you aren’t living in the software you’re building, each day, every day, all day… things are inevitably going to end in tears for everyone involved. And honestly, if I have to explain this to you, guess what? You’re screwed.
4. Launch a brief closed beta and get feedback from your Special Internet Friends™ on what you’ve built so far. I know what you’re thinking: *Friends! Damn it! I knew those things would be useful to me at some point!* Listen to all their feedback with an open mind, no matter how dumb it probably is. Identify and fix everything major that comes up. Your product will still be terrible, but it’ll be slightly marginally *less* terrible, and you’ll now be slightly marginally less screwed than you otherwise would. (This is what we business experts call a “competitive advantange.” Look it up.)
5. Rapidly get to a public launch. It will suck, but you will [ship it anyway](https://blog.codinghorror.com/version-1-sucks-but-ship-it-anyway/). Don’t screw up the basic logistics of the launch. You know what I’m talking about because you’ve seen those sad launches. Don’t be those companies. Don’t be those teams. Don’t worry, you’ll have ample time to screw everything up royally in the next step.
6. Hey, remember all those brilliant ideas you had based on all that painstaking, detailed research you did in step 1? Turns out once you put them in front of actual honest-to-god real world users they were *all… completely… wrong*. Now spend the next year doing nothing but fixing all your idiotic screwups and stupid mistakes.
7. ???
8. Profit!


I never said it was a *good* plan for building software, but hey. Y’know. [It’s a plan](https://blog.codinghorror.com/rule-of-three/).


![](https://blog.codinghorror.com/content/images/2025/02/image-150.png)


Each one of those steps is worthy of a blog entry in its own right, but it’s step six that I want to focus on today because in my opinion that’s the most critical part of this whole so-called “plan.” I like to refer to this phase as **complaint driven development**:

- Get your software in front of as many real users as you can.
- Listen to all the things they complain about. It will be… a lot.
- Identify and fix the top 3 things people keep repeatedly complaining about.
- Do it again.


Now, we have a bit of an unfair advantage here because [Discourse is discussion software](http://www.discourse.org/faq/). We host the discussions about all the things that are wrong with Discourse… on Discourse itself. But that’s also why we built an open source discussion platform in the first place – my deeply held belief that **actually listening to your customers should matter to your business**.


Provided you’re equipped to listen to your customers, complaint driven development isn’t that difficult. Until you get deep into a multi-year design, you’re dealing with **fairly obvious, easy to fix complaints from users**. You just have to be out there listening. As Steve Krug says in [Don’t Make Me Think](http://www.amazon.com/dp/0321965515/):


> You don’t need to find all the problems. In fact, you’ll *never* find all of the problems in anything you test. And it wouldn’t help if you did, because of this fact:
> *You can find more problems in half a day than you can fix in a month.*
> You’ll always find more problems than you have the resources to fix, so it’s very important that you focus on fixing the most serious ones first. And three users are very likely to encounter many of the most significant problems related to the tasks that you’re testing.


For example, we launched Discourse with a requirement that all topic titles and bodies be above a certain minimum character length, because we believe that extremely short posts and particularly titles aren’t conducive to actual conversation. Philosophically, this is an important default for us, because it strongly relates to our core mission of building software that helps cultivate meaningful conversation on the Internet.


Unfortunately, users *hated* it:


> I think it’s especially annoying that there’s no indicator of how many characters that you have to type. You only have whether or not the “Reply” button is greyed out or not, and not all users will realize that it’s greyed out at first. Even then, if you click on the reply button it can bounce back on you if your post was mostly white-space. It’s annoying as hell.


This was one of the consistently strongest bits of early feedback we got. So in the first 7 days after launch we quickly added a real time character count to the bottom right of the editor.


![](https://blog.codinghorror.com/content/images/2025/02/image-151.png)


I thought that’d help. It didn’t. The complaints about our terrible, awful, onerous default title and body length restrictions kept pouring in. So we experimented with ways to make these requirements clearer, by using a red border, or a red background on the fields.


![](https://blog.codinghorror.com/content/images/2025/02/image-152.png)


![](https://blog.codinghorror.com/content/images/2025/02/image-153.png)


We deployed all of the above and more. Complaints did not abate one bit. Now this is a configuration setting, if you want the minimum title and body length to be 1 character in your community, it’s trivially settable via a web browser in about 15 seconds. Frankly I started getting really sick of hearing all the complaints about the setting.


So we finally deployed the nuclear option: **bouncy error dialogs right next to the field** as soon as they lose focus.


![](https://blog.codinghorror.com/content/images/2025/02/image-154.png)


Since that change, I haven’t heard word one about our terrible, onerous, awful default body and title character limit policies. Not one. Single. Complaint.


So *that’s* the sort of thing we’ve been doing post launch, each day, every week, for the last year. **It took us a full year of complaint driven development to get to software worth using.** And even though we are now cautiously [accepting customers](http://www.discourse.org/buy/), we’re still practicing complaint driven development every day, just perhaps weighted a bit more heavily towards the people actually paying us money.


It’s true that [gathering feedback from your community](https://blog.codinghorror.com/listen-to-your-community-but-dont-let-them-tell-you-what-to-do/) can be hard work. And 90% of the feedback you’ll get will be terrible for a whole host of reasons. It’s a lot easier to imagine some heroic expert swooping in and magically blessing you with the correct answer. Well, [good luck with that fantasy](https://blog.codinghorror.com/are-you-an-expert/). The only thing I’ve ever seen work is **getting down deep and dirty in the trenches with your users, communicating with them and cultivating relationships**. That’s how you suss out the rare 10% of community feedback that is amazing and transformative. *That’s *how you build a community that gives a damn about what you’re doing – by caring enough to truly listen to them and making changes they care about.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[product development](https://blog.codinghorror.com/tag/product-development/)
[minimum viable product](https://blog.codinghorror.com/tag/minimum-viable-product/)
[research](https://blog.codinghorror.com/tag/research/)
[team-building](https://blog.codinghorror.com/tag/team-building/)
