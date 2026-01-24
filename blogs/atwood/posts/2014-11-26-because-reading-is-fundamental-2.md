---
title: "Because Reading is Fundamental"
date: 2014-11-26
url: https://blog.codinghorror.com/because-reading-is-fundamental-2/
slug: because-reading-is-fundamental-2
word_count: 1379
---

Most discussions show a bit of information next to each user:


![](https://blog.codinghorror.com/content/images/2025/05/image-183.png)


What message does this send?

- The only number you can control printed next to your name is post count.
- Everyone who reads this will see your current post count.
- The more you post, the bigger that number next to your name gets.


If I have learned anything from the Internet, it is this: be very, *very* careful when you put a number next to someone’s name. Because **people will **[**do whatever it takes**](https://blog.codinghorror.com/for-a-bit-of-colored-ribbon/)** to make that number go up**.


If you don’t think deeply about exactly *what* you’re encouraging, *why* you’re encouraging it, and all the things that may happen as a result of that encouragement, you may end up with… something darker. [A lot darker](https://web.archive.org/web/20071102022046/http://benbrown.com/says/2007/10/29/i-love-my-chicken-wire-mommy).


Printing a post count number next to every user’s name implies that the more you post, the better things are. The more you talk, the better the conversations become. Is this the right message to send to everyone in a discussion? More fundamentally, *is this even true?*


I find that the value of conversations has little to do with how much people are talking. I find that too much talking has a *negative* effect on conversations. Nobody has time to listen to the resulting massive stream of conversation, they end up just waiting for their turn to pile on and talk, too. **The best conversations are with people who spend most of their time listening**. The number of times you’ve posted in a given topic is not a leaderboard; it’s a record of failing to communicate.


Consider the difference between a chat room and a discussion. Chat is a never-ending flow of disconnected, stream of consciousness sentences that you can occasionally dip your toes in to get the temperature of the water, and that’s about it. Discussion is the process of lobbing paragraphs back and forth that results in an evolution of positions as your mutual understanding becomes more nuanced. We hope.


### The Ars Banana Experiment


Ars Technica ran a little experiment in 2011. When they posted “[Guns at home](http://arstechnica.com/science/2011/04/guns-in-the-home-lots-of-risk-ambiguity/) more likely to be used stupidly than in self defense,” embedded in the last sentence of the seventh paragraph of the article was this text:


> If you have read this far, please mention Bananas in your comment below. We’re pretty sure 90% of the respondants to this story won’t even read it first.


The first person to do this is on page 3 of the resulting discussion, [comment number 93](http://arstechnica.com/science/2011/04/guns-in-the-home-lots-of-risk-ambiguity/?comments=1&post=21585045#comment-21585045). Or as helpfully visualized by [Brandon Gorrell](http://thoughtcatalog.com/brandon-gorrell/2011/04/the-problem-with-having-a-serious-discussion-on-the-internet/):


![](https://blog.codinghorror.com/content/images/2025/05/image-184.png)


Plenty of talking, but how many people actually read up to paragraph 7 (of 11) of the source article before they rushed to comment on it?


### The Slate Experiment


In [You Won’t Finish This Article](http://www.slate.com/articles/technology/technology/2013/06/how_people_read_online_why_you_won_t_finish_this_article.html), Farhad Manjoo dares us to read to the end.


> Only a small number of you are reading all the way through articles on the Web. I’ve long suspected this, because so many smart-alecks jump in to the comments to make points that get mentioned later in the piece.


But most of us won’t.


He collected a bunch of analytics data based on real usage to prove his point:


![](https://blog.codinghorror.com/content/images/2025/05/image-185.png)


These experiments demonstrate that we don’t need to incentivize talking. There’s far too much talking already. **We badly need to incentivize *listening***.


And online, listening = reading. That old school program from my childhood was right, so deeply fundamentally right. Reading. [Reading Is Fundamental](http://readingisfundamental.org/).


Let’s say you’re interested in World War II. Who would you rather have a discussion with about that? The guy who just skimmed the Wikipedia article, or the gal who read the entirety of [The Rise and Fall of the Third Reich](http://www.amazon.com/dp/1451651686)?


This emphasis on talking and post count also unnecessarily penalizes lurkers. If you’ve posted five times in the last 10 years, but you’ve read every single thing your community has ever written, I can guarantee that you, Mr. or Mrs. Lurker, are a far more important part of that community’s culture and social norms than someone who posted 100 times in the last two weeks. Value to a community should be measured every bit by *how much you’ve read* as much as how much you talked.


![](https://blog.codinghorror.com/content/images/2025/05/image-186.png)


So how do we encourage reading, exactly?


You could do crazy stuff like require commenters to enter some fact from the article, or pass a basic quiz about what the article contained, before allowing them to comment on that article. On some sites, I think this would result in a huge improvement in the quality of the comments. It’d add friction to talking, which [isn’t necessarily a bad thing](https://blog.codinghorror.com/training-your-users/), but it’s a negative, indirect way of *forcing* reading by denying talking. Not ideal.


I have some better ideas.

1. **Remove interruptions to reading, primarily pagination**. Here’s a radical idea: when you get to the bottom of the page, *load the next damn page automatically*. Isn’t that the most natural thing to want when you reach the end of the page, to read the next one? Is there any time that you’ve ever been on the Internet reading an article, reached the bottom of page 1, and *didn’t* want to continue reading? Pagination is nothing more than [an arbitrary barrier to reading](https://blog.codinghorror.com/the-end-of-pagination/), and it needs to die a horrible death.There are sites that go even further here, such as The Daily Beast, which actually *loads the next article* when you reach the end of the one you are currently reading. [Try it out and see what you think](http://www.thedailybeast.com/articles/2014/05/27/your-princess-is-in-another-castle-misogyny-entitlement-and-nerds.html). I don’t know that I’d go that far (I like to pick the next thing I read, thanks very much), but it’s interesting.
2. **Measure read times and display them**. What I do not measure, I cannot display as a number next to someone’s name, and cannot properly encourage. In Discourse we measure how long each post has been visible in the browser for every (registered) user who encounters that post. Read time is a key metric we use to determine who we trust, and the best posts that people do actually read. If you aren’t willing to visit a number of topics and spend time actually *listening* to us, why should we talk to you – or trust you.Forget clicks, forget page loads, measure *read time!* We’ve been measuring read times extensively since launch in 2013 and it turns out we’re in good company: [Medium](https://medium.com/data-lab/mediums-metric-that-matters-total-time-reading-86c4970837d5) and Upworthy both recently acknowledged the intrinsic power of this metric.
3. **Give rewards for reading**. I know, that old saw, gamification, but if you’re going to reward someome, do it for the right things and the right reasons. For example, we created a badge for reading to the end of a long 100+ post topic. And our trust levels are based heavily on how often people are returning and how much they are reading, and virtually not at all on how much they post. To feel live reading rewards in action, try [this classic New York Times Article](http://www.nytimes.com/2012/12/24/technology/all-the-worlds-a-game-and-business-is-a-player.html). There’s even a badge for reading half the article!
4. **Update in real time**. Online we tend to read these conversations as they’re being written, as people are engaging in live conversations. So if new content arrives, figure out a way to dynamically rez it in *without* interrupting people’s read position. Preserve the back and forth, real time dynamic of an actual conversation. Show votes and kudos and likes as they arrive. If someone edits their post, bring that in too. All of this goes a long way toward making a stuffy old debate feel like a living, evolving thing versus a long distance email correspondence.


These are strategies I pursued with [Discourse](http://www.discourse.org/), because I believe Reading Is Fundamental. Not just in grade school, but in your life, in my life, in every aspect of online community. To the extent that Discourse can help people learn to be better listeners and better readers – not just *more talkative* – we are succeeding.


If you want to become a true radical, if you want to have deeper insights and better conversations, **spend less time talking and more reading**.


> Update: There’s a [CBC interview with me](http://www.cbc.ca/radio/spark/spark-270-1.2889937/why-listening-is-more-important-than-talking-1.2890065) on the themes covered in this article.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[online communities](https://blog.codinghorror.com/tag/online-communities/)
[engagement](https://blog.codinghorror.com/tag/engagement/)
