---
title: "Developers Are Users Too"
date: 2005-03-14
url: https://blog.codinghorror.com/developers-are-users-too/
slug: developers-are-users-too
word_count: 729
---

I’m currently whipping up a mini-API for the [BetaBrite](https://blog.codinghorror.com/automated-continuous-integration-and-the-betabrite-led-sign/)-specific subset of the [Alpha Sign Communications Protocol](https://web.archive.org/web/20050404030338/http://www.ams-i.com/Pages/97088061.htm). Naturally, I want it to be easy to use and understandable for other developers – a classic usability problem. How do you approach usability when your audience is other developers?


The answer is, unsurprisingly, **exactly the same way you approach usability for regular users**. Microsoft’s Steven Clarke has [an entire blog](http://blogs.msdn.com/stevencl/) dedicated to this subject, and he’s been conducting regular usability labs on the entire alphabet soup of upcoming Microsoft technologies. There’s a somewhat dense [summary of his results](https://web.archive.org/web/20050512195800/http://www.gotdotnet.com/team/brada/describingandevaluatingapiusabilityatmicrosoft.ppt) (PowerPoint), and it’s all bread-and-butter usability studies. Nothing developer-y about it. Personas, use cases, tasks, and a whole lot of observation. Here are a few representative examples from his blog, which I highly recommend.


On Attributes:


> *I think one factor in this is the low visibility of attributes. For example, one participant in the study this week was stepping through his code in the debugger when he noticed some unexpected behavior at some point during the execution of his code. He was focused on a particular block of code and concentrated his efforts on understanding how that block of code might have caused the behavior he had just observed. The cause for that behavior was due to an attribute that had been applied to the class that defined the method the participant was stepping through. Thus when he was reading his code, the attribute was well out of his focus of attention.*


on ADO.NET:


> *In one usability study I ran on ADO .Net, participants were asked to write code that queries a table and outputs the results to the console. The results were stored in a DataReader. Many participants expected to find some Count property on the DataReader that they could use to loop through the contents of the datareader, indexing each element in each iteration of the loop. However, no such property existed. Participants spent a significant amount of time looking for other similar properties such as Length, NumberOfRows etc. but did not find anything that would help.
> At this point, most participants went to the help docs to find a code sample to help them. As soon as participants found a code sample that showed them that they needed to use an IEnumerator to enumerate through the contents of the DataReader, they understood exactly what they needed to do. Even though the solution was slightly different to the one that participants had originally attempted, they had no difficulties understanding this new approach.*


When it comes to usability, there’s no substitute for observation. It’s absolute bedrock.


One thing that jumped out at me almost immediately was **the importance of good code samples**. Those are the first things I look for in any new environment I’m exposed to, and for better or worse, they set the tone for my experience. But, as Steven describes in a Dr. Dobb’s Journal article, [Measuring API Usability](https://web.archive.org/web/20051031025513/http://www.gotdotnet.com/team/brada/APIUsability.pdf) (PDF), you have to be careful that you’re not papering over bad API design decisions with good code samples:


> *Cognitive dimensions have really helped us get to the root cause of issues that we have observed in the usability labs. For example, in one study, we observed lots of developers spending a large amount of time in the help docs looking for code samples that would show them how to accomplish a given task. The first interpretation of this data was simply **“Fix the help docs!”** However, when we used the cognitive dimensions framework to describe the issues, it became clear that **the reason the developers weren’t successful when they were searching through the help was because what they were looking for simply didn’t exist.** The API they were working with exposed a set of abstractions that were at the wrong level for these particular developers. They expected a particular type of abstraction to be exposed by the API but since it wasn’t, they couldn’t find anything about it in the help docs. As a result, the API team redesigned this API to expose abstractions more in line with what developers were expecting. When we retested the API, it worked much better.*


This is something I’ve touched on before. If you’re answering a lot of questions from other developers about something you’ve written, it’s probably not [because your co-workers suck](https://blog.codinghorror.com/blue-collar-software-development/).

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
