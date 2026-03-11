---
title: "What if you could only speak once a year?"
date: 2012-05-28
url: https://www.danshapiro.com/blog/2012/05/what-if-you-could-only-speak-once-a-year/
word_count: 967
---


Who’s been a part of a mailing list that’s suffered from poor-quality posts drowning out an otherwise-useful conversation?


OK, hands down.  It seems like it happens to just about every worthwhile mailing list I’ve ever been on: the quality of the posts goes to hell.  And in fact there are a few sub-problems:

- A small number of posters, who may or may not have anything useful to say, that monopolize the conversation;
- A series of arguments whose rapid back-and-forths make up the bulk of the list content;
- The list drifting from a narrow purpose to a wide ranging discussion of everything from the Greek debt crisis to ‘what I had for dinner last night’.


I was watching this happen yet again, to yet another list, and it got me to thinking.  The classic solution is moderation, but that tends to turn in to a dull dictatorship, not to mention cause a lot of work for the moderator.  What if there was some sort of “game mechanic” that could cause people to self-regulate the quality of their posts in a simple mailing list?


As with many ideas, I started complicated.  The idea revolved around a points system, where people could up- and down-vote participants.  Submissions that got more upvotes would be disseminated to more people – the most popular posts would go to everyone; the lousy stuff would just go to a dozen random subscribers and die out.   If you liked something you read, you could reply, and it would go to the author, plus everyone else who had replied or “liked” the post, so you could have a more in-depth conversation about topics.  And as an afterthought, there would be some sort of cool-down period so that people couldn’t get in to flame wars – once you replied, it would take a while before you could post again.


At that point, I realized that:


a) There was no way I was ever going to implement something this complicated, and


b) I had pretty much just reinvented Hacker News.


I was about to shrug and abandon the idea, but one tiny bit stuck in my head – the cool-off period.  What if mailing lists had a limit to how frequently you could post?  This seemed like an interesting idea.  It would let arguments cool down between replies, plus – if it was a little longer – it might make you think twice about if your writing was good enough to warrant a period of enforced silence.  Self-moderate, that is.


And what if you took it to an extreme?  What if every utterance contained within a vow of monastic silence, digitally enforced?  *Wouldn’t you think twice before invoking Goodwin’s Law over a comic book?  *Hypothetically speaking, of course, not that I would be involved in any such argument.


And so I created “The Best Thing This Year” around the idea of a mailing list with an enforced 1-year quiet period after every post.  Created is a bit generous, actually – I threw up a launchrock page  and waited to see what would happen.


And what happened was  surprising.  First, a lot of people signed up.   It started when I shared the idea (still just a launchrock page) with John Cook over late night karaoke, and he wrote up a quick [article](http://www.geekwire.com/2012/dan-shapiros-latest-side-project-year/). That got my butt in gear to actually build something to, you know, deliver emails.  The result was a terrible hybrid of Amazon SES, PHPlist running on an EC2 micro instance, and some custom PHP courtesy vworker.com to replace the signup page and pump directly in to the mailing list.  I also threw up a phpBB discussion board on my Dreamhost account for good measure.


My friend Elan kicked things off with the first piece about his new, augmented-reality sitcom (!) at [rides.tv](http://rides.tv), and [Pando Daily](http://www.motherjones.com/mixed-media/2012/05/the-best-thing-this-year-dan-shapiro) and [Mother Jones Magazine](http://www.motherjones.com/mixed-media/2012/05/the-best-thing-this-year-dan-shapiro) jumped in, talking about the post and the list.  And here we are, two weeks later, and the list has nearly 2,000 subscribers… *and a surprising lack of submissions.*


Not a total absence, mind you.  There’s been an epic piece about parenthood that came out for Mothers’ Day.  Yesterday was a unbelievable story about the first man to do a commercial bungee jump off of Corona arch in Moab, Utah.  But the pace has been slow.


And I’m afraid not all submissions represented the best thing a year had to offer.  The first submission was mostly shit – not metaphorically, but literally; the primary topic of the post was human feces.  While I hope to keep a light touch, I decided that did not need to wind up in a few thousand inboxes, and did not allow that submission to post.


But in general, there have been few submissions to this rather incredible audience.  I won’t out list members, but I’ve looked through the email signups and there are a lot of awesome people listening to what gets said.


So the rules continue as before.  You can sign up at [thebestthingthisyear.com](http://thebestthingthisyear.com) and you will get new posts immediately.  Over at [discuss.thebestthingthisyear.com](http://discuss.thebestthingthisyear.com) you can read previous posts and chat about new ones when they come up.  New signups have a cool-down period before they can submit, to ensure everyone doesn’t post at once – in retrospect, probably not solving for the right decision, but the policy is two weeks old and this is the internet so that makes it a tradition.


The posts will be, it seems, mostly excellent.  And if current trends hold up, fairly rare.


And I have the answer to my original question.  What would people do on a mailing list if they could only speak once a year?


Mostly just shut up and listen.

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
