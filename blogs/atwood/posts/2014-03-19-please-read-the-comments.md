---
title: "Please Read The Comments"
date: 2014-03-19
url: https://blog.codinghorror.com/please-read-the-comments/
slug: please-read-the-comments
word_count: 1121
---

I find the Don’t Read The Comments movement kind of sad.


![Comments sections are frequently misogynistic, homophobic, racist, and very often POORLY WRITTEN. Why bother reading them?](https://blog.codinghorror.com/content/images/2025/09/image-19.png)


In 2006 I said that a [blog without comments is not a blog](https://blog.codinghorror.com/a-blog-without-comments-is-not-a-blog/) and I stand behind that statement. There have been brief periods where my own blog has been [temporarily without comments](https://blog.codinghorror.com/welcome-back-comments/), but they will always come back as long as I’m in charge here.


I’m a fan of comments, warts and all. They’re noisy, sure, but in my experience they reliably produce crowdsourced knowledge in aggregate. I understand being pressed for time, but if you want the complete picture, in the same way that you should follow all those little citation links in Wikipedia articles, **you should read the comments**.


I empathize with [the complaint](http://www.salon.com/2012/10/25/im_never_reading_the_comments_again/), believe me:


> I used to believe that as an online writer, I had an obligation to read the comments. I thought that it was important from a fact-checking perspective, that it somehow would help me grow as a writer. What I’ve learned is that if there’s something wrong or important or even, sometimes, good about a story, someone will let you know. I’ve over the years amassed an amazing community of Salon readers who engage via email, who challenge me, who inspire new stories, who are decent people and treat me like one in return. What I was getting in the comments was a lot of anonymous “You suck, bitch.”
> I admit it’s depressing for one who’s invested almost her entire career in online community to throw in the towel on it in this way. I want it to be better. But it’s just not. As a colleague once observed, “I just can’t take another letter from Angry Bad Divorce Guy.”


But that’s so many pesky *words*, isn’t it? TL;DR. Allow me to illustrate with a graph that your brain can absorb in milliseconds:


![](https://blog.codinghorror.com/content/images/2025/02/image-138.png)


What is *wrong* with people, amirite?


I humbly submit that this is asking the wrong question.


*What is wrong with us?*


I agree with Anil Dash. If your website is full of assholes, [it’s your fault](http://dashes.com/anil/2011/07/if-your-websites-full-of-assholes-its-your-fault.html).


> As it turns out, we have a way to prevent gangs of humans from acting like savage packs of animals. In fact, we’ve developed entire disciplines based around this goal over thousands of years. We just ignore most of the lessons that have been learned when we create our communities online. But, by simply learning from disciplines like urban planning, zoning regulations, crowd control, effective and humane policing, and the simple practices it takes to stage an effective public event, we can come up with a set of principles to prevent the overwhelming majority of the worst behaviors on the Internet.
> If you run a website, you need to follow these steps. if you don’t, you’re making the web, and the world, a worse place. And it’s your fault. Put another way, take some goddamn responsibility for what you unleash on the world.


In other words, **if you are unwilling to moderate your online community, you don’t deserve to have an online community.** There’s no end of websites recreating the glorious “no stupid rules” libertarian paradise documented in the [Lord of the Flies](http://en.wikipedia.org/wiki/Lord_of_the_Flies) in their comment sections, from scratch, each and every day. This ends exactly as you would expect it to.


![](https://blog.codinghorror.com/content/images/2025/02/image-137.png)


However, demanding that every online community, every comment section, have active moderation is a tough sell:

- Skilled moderators are difficult to find. A bad moderator is often *worse* than no moderator.
- Do you have the budget to pay full time moderators?
- Are your moderators around 24/7?
- If you have a single moderator making unilateral decisions, who appeals their decisions? If you have multiple moderators, how do they resolve disagreements?
- What happens when your moderators inevitably burn out or move on?


One of the reasons I [launched the Discourse project](http://www.discourse.org/about/) was due to the utter lack of understanding of how you build software to help online discussion communities moderate themselves. Their survival depends on it.


What I learned building Stack Overflow, more than anything else, is this: **the only form of moderation that scales with the community is the community itself.** We became quite skilled at [building systems for self governance](http://blog.stackoverflow.com/2011/01/trilogy-2011-elections-begin/) of online communities, and one of the things I’m proudest of is that – if we did our jobs well – decades from now [Stack Exchange](http://www.stackexchange.com/) will still be a network of viable, functioning, entirely self-governing communities.


It’s [always a people problem](https://blog.codinghorror.com/no-matter-what-they-tell-you-its-a-people-problem/). This is absolutely true. But it’s also true that software can *profoundly* affect people’s behavior, and provide tools for [encouraging positive behaviors](https://blog.codinghorror.com/training-your-users/) while modifying and mitigating negative behaviors. All that stuff Anil Dash described as your responsibility? Discourse handles it automatically, even if the owner installs and then walks away forever.


These are the [principles of civilized discourse](http://blog.discourse.org/2013/03/the-universal-rules-of-civilized-discourse/) that Discourse is founded on, that our discussion software is designed around. Civilization begins with software that actively works to help you create safe environments for having reasonable conversations with other human beings. On the *Internet*, even!


![](https://blog.codinghorror.com/content/images/2025/02/image-139.png)


This is all a very long winded way of saying that effective immediately, **Coding Horror is using **[**Discourse**](http://www.discourse.org/)** to power its discussions.**


You may have questions, so I will attempt to answer them:

- This blog is [now hosted on Ghost](https://blog.codinghorror.com/10-years-of-coding-horror/), which doesn’t natively support comments. All previous TypePad comments were converted into Discourse. To the best of our ability, nothing was lost.
- Discourse is still beta, but [late beta](http://blog.discourse.org/2014/01/the-road-to-discourse-1-0-2/). Expect changes and improvements as we make our way to 1.0.
- Discourse is a *companion* area to this blog, a clubhouse for the community. You can visit there directly at [discourse.codinghorror.com](http://discourse.codinghorror.com/)
- Every new blog post here results in a corresponding topic being automatically created in the Discourse discussion area.
- I do not, and will not, offer in-page commenting here. If you want to reply with a comment, you go next door to [the community clubhouse](http://blog.discourse.org/2013/05/your-online-clubhouse/). There’s a fairly strong, but permeable, membrane between the editorial area *here* and the community area *there*. This is intentional.
- At the bottom of each blog entry here you will find read only versions of all replies to the Discourse topic associated with this blog entry. I might eventually switch that to a “best of” algorithm so readers see the best comments without having to wade through dozens or hundreds of replies.


If you like what you see, Discourse is 100% [free open source software](http://github.com/discourse/discourse), so you can easily [set up the same system](https://web.archive.org/web/20140302191131/http://eviltrout.com/2014/01/22/embedding-discourse.html) for your own blog. We even have a [WordPress plugin](https://github.com/discourse/wp-discourse) to assist.


Now who’s [ready for some dogfooding](https://blog.codinghorror.com/the-ultimate-dogfooding-story/)?

[social media](https://blog.codinghorror.com/tag/social-media/)
[comments](https://blog.codinghorror.com/tag/comments/)
[blogging](https://blog.codinghorror.com/tag/blogging/)
