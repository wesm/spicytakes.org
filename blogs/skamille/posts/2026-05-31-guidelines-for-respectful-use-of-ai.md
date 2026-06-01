---
title: "Guidelines for Respectful Use of AI"
date: 2026-05-31
url: https://www.elidedbranches.com/2026/05/guidelines-for-respectful-use-of-ai.html
word_count: 1245
---


As companies adopt AI tools, a lot of time is spent on thinking about AI policies from a security, compliance, or even cost-focused angle. But many leaders are neglecting to address how their teams should work with AI in the context of the team as a whole. This creates a lot of unresolved tension, and it’s time for leaders to step up and set some guidelines not just for how to use AI in an “approved” sense, but how to use it respectfully.


When I say respectfully, I am not talking about the baseline appropriate workplace behavior (bullying, abuse, harassment, etc). Instead, I’m concerned that many of us haven’t considered that the ways AI can make an individual more productive (literally enabling them to produce more outputs) can have an overall negative impact on the team’s productivity. Leaders can’t just sit around and expect that their teams will know that they can’t just produce slop and send it to others; if you haven’t set up a thorough [policy](https://rfd.shared.oxide.computer/rfd/0576) yet, here are some suggestions on what to cover.


## Elements of Respectful AI Use


### Don’t ask someone to read/review what you haven’t read or reviewed yourself.


This is one of the most common frustrations I hear amongst people working on AI-heavy teams. Whether it’s code that the owner didn’t really bother to understand before submitting for review, or documents that they generated and didn’t bother to read, too often people try to steal productivity from their colleagues by streamlining their production of work while asking their colleagues to do all of the quality control themselves. It’s great to have a loop of AI code generation -> AI code review -> AI fixes -> final human review, but if the person prompting the AI doesn’t bother to review that code first, they’re putting a huge validation tax onto their teammate, who has to trust both that you prompted well AND that the AI understood the context and problem well enough to get a sustainable solution.


Documents are an even bigger temptation than code, because AI is so verbose and most of us hate writing and editing. It’s easy to get into a loop where you ask the AI some questions, skim the answers, output a document and send it to others. I’m guilty of this myself! But what makes sense when you’re skimming one answer at a time may not make for a good overall document, and there is a big difference between answering individual questions and writing for a human reader. In particular, the context that you have in your own head as you are talking to the AI may not come out at all in the document; if you don’t bother to read it thoroughly before sending it out, you won’t catch the gap in framing.


Even worse, sometimes people don’t even understand what the document they prompted is trying to say. Can you describe this document, and have a conversation about the concepts it presents with others and why it makes sense? If not, you have no business sending it along without at minimum the huge caveat *this is AI-generated and I still don’t really understand this space, please help me.*


Many people have reached the point where they won’t read something a person didn’t bother to write themselves, and who can blame them when so many don’t even bother to read their output before sending it on?


### Shorter is better.


Part of the annoyance of reviewing AI-generated work is that the AI can be painfully long-winded. AI code often looks like tutorial code, with much more verbosity than human developers would bother with. Add in the temptation to one-shot big changes rather than thinking about how to break the code down into pieces, and you can end up with stacks of thousand line pull requests. The documents AI produces are so thorough that something that should be 3 pages turns into 10 or 20. And for those who have fully embraced AI for all of their text-based interactions, you start to see the LLM-generated wall of text chat messages or emails.


This is, frankly, just rude. It goes hand in hand with not bothering to review your own work, but even if for some reason you convince yourself that you really did read and edit that giant PR/document/message, you’re still asking so much more of the audience than you probably put into the exercise in the first place. When it comes to code, I encourage you to honestly ask yourself: if this broke at 3am and none of the AI tools were working, would you be able to look at the PR context and the change and debug it? If not, it is probably too much. When it comes to a big document, at a minimum, have you at least summarized the important points up-front? If someone is just going to ask an AI to summarize the document themselves, you should probably do more work to provide that value before handing it off.


Finally, if you’re writing long-winded emails or chat messages with AI-assistance in order to painstakingly try to explain something, perhaps you actually need to have a meeting or call instead. Increasingly long text exchanges have always been a sign that people need to stop and talk face-to-face, and AI logorrhea hasn’t changed that.


### AI is not an excuse to turn off your brain, or your heart.


Signs we’ve switched off our brains and our hearts include: not reviewing the AI-generated work, not taking the time to do human editing, not breaking the changes down into chunks, and avoiding real conversations through AI-mediated text exchange. This guidance is about respectful use of AI because if you have empathy for your colleagues and respect for their time and skills, you will show them the courtesy of giving them work that you are proud of, that you stand behind, that you have thought through and can explain. The AI may have produced a lot of the output, but you thought about all of the pieces that needed to be done, and used the extra productivity to make something better: more reliable, simpler, well tested, whatever. If you find yourself not thinking at all and just mindlessly prompting, accepting output, and moving forward, it’s a warning sign that something is wrong. Perhaps take some advice from [Vicki Boykis](https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/) on adding friction to your development process (or whatever the equivalent is of your day to day work).


## Framing these guidelines


If you decide to do this, one final tip from me: assuming your company has some sort of company values, it’s always a good idea to call back to these values when you create policies and guidelines like this. It’s one thing to abstractly say that shorter is better, but if you can tie that to a value for your company, it will resonate more strongly. As an example, if I were at Amazon I might consider tying “shorter is better” to the leadership principle Invent and Simplify. And since shorter is better and this is already too long, I leave you here.


*This post is 100% human-generated except that I needed a spell-checker to spell logorrhea. Maybe I should’ve used an AI editor, feel free to tell me if you think so!*


*Enjoy this post? You might like my books: *[*The Manager’s Path*](http://amzn.to/2nw1QN5)*, and *[*Platform Engineering: A Guide for Technical, Product, and People Leaders*](https://amzn.to/3MwcgGo), *available on Amazon and Safari Online.*
