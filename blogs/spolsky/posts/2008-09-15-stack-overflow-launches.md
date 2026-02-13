---
title: "Stack Overflow Launches"
date: 2008-09-15
url: https://www.joelonsoftware.com/2008/09/15/stack-overflow-launches/
word_count: 1676
---


You know what drives me crazy? Programmer Q&A websites. You know what I’m talking about. You type a very specific programming question into Google and you get back:

- A bunch of links to discussion forums where very unknowledgeable people are struggling with the same problem and getting nowhere,
- A link to a Q&A site that purports to have the answer, but when you get there, the answer is all encrypted, and you’re being asked to sign up for a paid subscription plan,
- An old Usenet post with the exact right answer—for Windows 3.1—but it just doesn’t work anymore,
- And something in Japanese.


If you’re very lucky, on the fourth page of the search results, if you have the patience, you find a seven-page discussion with hundreds of replies, of which 25% are spam advertisements posted by bots trying to get googlejuice for timeshares in St. Maarten, yet some of the replies are actually useful, and someone whose name is “Anon Y. Moose” has posted a decent answer, grammatically incorrect though it may be, and which contains a devastating security bug, but this little gem is buried amongst a lot of dreck.


Well, technology has gotten better since those discussion forums were set up. I thought that the programming community could do better by combining the idea of a Q&A site with voting and editing.


Would it work? I had no idea. And it looked like there was no way to find out, because everyone at Fog Creek was really busy so nobody had any time to build this.


Then, out of the blue, Jeff Atwood called me up. His own blog, [Coding Horror](http://www.codinghorror.com/), was starting to [rack in the dough](http://www.codinghorror.com/blog/archives/000893.html), and he was trying to figure out if that meant he could quit his day job and just blog.


Pattern-matching rules fired in my brain. The hardest thing about making a new Q&A site is not the programming—it’s the community. You need a large audience of great developers so you have the critical mass it takes to get started. Without critical mass, questions go unanswered and the site becomes a ghost town. I thought the combination of my audience (#15 on [Bloglines](https://beta.bloglines.com/topfeeds)) and Jeff’s (#89) would bring enough great developers into the site to reach critical mass on day one. So Jeff and I decided to go in together on this.


We’ve been working all summer to build the site. OK, that’s extremely unfair. Jeff Atwood, together with two of his friends, Geoff Dalgas and Jarrod Dixon, have been doing most of the building. I just chime in with advice once in a while, which Jeff justifiably ignores; you can hear the process in our weekly status phone call, publically available in the form of [the Stack Overflow podcast](http://blog.stackoverflow.com/).


In the beginning of August, the beta opened to a small group of just a few hundred developers. The site lit up instantly! People were asking questions and, for the most part, getting answers! And the voting was working too… in most questions, you could see that the best answers were voted up promptly. I tried to ask a programming question for something I was working on and found that (a) it had already been asked (b) there were already good answers and (c) the search engine worked so well I never got a chance to post my question.


After a very short, five-week private beta, we’re opening [Stack Overflow](http://stackoverflow.com/) to the public today.


Here’s how it’s supposed to work. This is a community project, so I’m being careful to avoid saying this is how it *will* work… that’s up to the community. But this is roughly what I have in mind.


Every question in Stack Overflow is like the Wikipedia article for some extremely narrow, specific programming question. *How do I enlarge a fizzbar without overwriting the user’s snibbit?* This question should only appear once in the site. Duplicates should be cleaned up quickly and redirected to the original question.


Some people propose answers. Others vote on those answers. If you see the right answer, vote it up. If an answer is obviously wrong (or inferior in some way), you vote it down. Very quickly, the best answers bubble to the top. The person who asked the question in the first place also has the ability to designate one answer as the “accepted” answer, but this isn’t required. The accepted answer floats above all the other answers.


Already, it’s better than other Q&A sites, because you don’t have to read through a lot of discussion to find the right answer, if it’s in there somewhere.


Indeed, you can’t even *have *a discussion. A lot of people come to Stack Overflow, not knowing what to expect, and try to conduct a discussion when they should be answering the question. The trouble here is that answers are always listed in order of votes, not chronologically, so the discussion instantly becomes scrambled when the votes start coming in.


Instead, we have editing. Once you’ve earned a little bit of reputation in the system (and there are all kinds of ways to earn reputation), you can edit questions and answers.


Fred asks: *How do I keep from overwriting the user’s snibbit?*


Kathy answers: *Normally the user’s snibbit will not be overwritten. Are you enlarging the fizzbar?
*


Fred answers: *Yes. And it’s getting overwritten*.


*BZZT! WRONG! *Fred just made a mistake… he provided an answer which isn’t an answer. VOTE IT DOWN!


Chastised, Fred edits his original question, changing it to: *How do I keep from overwriting the user’s snibbit while enlarging the fizzbar?*


Now Kathy can answer by editing her previous answer. And you’re left with a nice clean single-question, single-answer, instead of a lot of boring discussion that would be unnecessary flotsam to the next person to come along with snibbit overwriting problems.


There are lots of good ways to edit things. You can improve spelling, grammar, and even copy edit any question or answer to make it better. After all, for the next 20 years, this question will be the canonical place on the web where programmers will come to find out about enlarging fizzbars without overwriting snibbits. Anything you can do to clarify, explain, or improve the question or the answer will be a public service. If there’s code in the answer, you can debug it, refactor it, or tweak it to make it better.


You can also improve on the answers. If an answer is incomplete, expand on it. If an answer has a bug in it or is obsolete, you can edit it and fix it. Because Q&A in Stack Overflow are editable, you can safely link to a Stack Overflow permalink knowing it will always have a good answer. Stack Overflow won’t have the problem of other sites where obsolete or incorrect answers have high Google PageRank simply because they’ve been on the Internet for so long. If someone finds a security bug in an answer, it can be fixed… it won’t keep coming up in Google’s results for years and years poisoning future code.


Want to know an easy way to earn reputation? Find a question somewhere with several good, but incomplete, answers. Steal all the answers and write one long, complete, detailed answer which is better than the incomplete ones. Sit back and earn points while people vote up your comprehensive answer.


In addition to voting on answers, you can vote on questions. Vote up a question if you think it’s interesting, if you’d like to know the answer, or if you think it’s important. The **hot** tab on the home page will show some of the highest-ranked recent questions using an algorithm similar to [digg](http://digg.com/) or [Reddit](http://www.reddit.com/). If you’re generally interested in programming and want to learn something new every day, visit the hot tab frequently.


Want to test your knowledge? Visit the **Unanswered** tab. Right now, you just see a list of questions with no answers (and there are very few), but in the near future, we’ll actually tailor the list to show you questions that we think you have a chance of answering, based on questions you’ve successfully answered in the past.


We have tags. Every question is tagged so, for example, if you’re a Ruby guru, you can ignore everything but Ruby and just treat Stack Overflow as a great Ruby Q&A site. A single question can have multiple tags, so you don’t have to figure out which single category it fits in best. Like everything else, the tags can be edited by good-natured individuals to help keep things sorted out neatly. And you can have a little fun: stick a **homework** tag on those questions where someone seems to be asking how to delete an item from a linked list.


Don’t combine multiple answers. For example, suppose someone asks


*What are your favorite keyboard shortcuts in Emacs?*


Well, I could list them all in one answer, but how does anyone vote on that? Instead, I’ll provide a bunch of separate answers, and let people vote on the answers. And in fact, if you see a question which is really a poll, do me a favor, go in there and edit it:


*What is your single favorite keyboard shortcut in Emacs? (One shortcut per answer, please).
*


What kind of questions are appropriate? Well, thanks to the tagging system, we can be rather broad with that. As long as questions are appropriately tagged, I think it’s okay to be off topic as long as what you’re asking about is of interest to people who make software. But it does have to be a question. Stack Overflow isn’t a good place for imponderables, or public service announcements, or vague complaints, or storytelling.


I’m extremely excited about Stack Overflow. It’s fast and clean. It costs us practically nothing to operate, so we won’t need to plaster it with punch-the-monkey ads; we plan to keep it free and open to the public forever. And it might make it a little bit easier to be a programmer.
