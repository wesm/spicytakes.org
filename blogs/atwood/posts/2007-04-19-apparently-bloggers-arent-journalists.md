---
title: "Apparently Bloggers Aren’t Journalists"
date: 2007-04-19
url: https://blog.codinghorror.com/apparently-bloggers-arent-journalists/
slug: apparently-bloggers-arent-journalists
word_count: 979
---

I ran across this blog entry while researching Microsoft’s new [Silverlight](http://www.microsoft.com/silverlight/) Flash competitor. It makes some disturbing complaints about the limitations of Silverlight, in bold all-caps to boot:


> This is where I threw my hands up in disgust. What in the holy name of Scooby-Doo are those people thinking?!?! After poring through the [Silverlight] API, I thought “I must be mistaken. Surely this is a mistake.” But then I asked a colleague and he confirmed it for me. Let me skip a couple lines and highlight this so you all can see it clearly.
> **WPF/E (Silverlight) HAS NO SUPPORT FOR BINDING TO MODELS, BINDING TO DATA, OR EVEN CONNECTING TO NETWORK RESOURCES TO OBTAIN DATA.**
> So, I will summarize Microsoft’s efforts to date around Silverlight. They have created a declarative programming model that uses XAML as an instantiation language for rich 2D (not 3D) content and animations, as well as extended JavaScript to support this model. Using this model, you can create embedded mini-apps that have access to rich animations, graphics, audio, and video objects. However, these mini applications cannot communicate with the outside world, they cannot consume web services, and they cannot bind UI elements to data. In addition, this model doesn’t even have support for things that should be considered a stock part of any library such as buttons, checkboxes, list boxes, list views, grids, etc.


Those are serious problems indeed. I found this blog entry because it’s referenced by another blog entry on [the limitations of Silverlight](https://web.archive.org/web/20070501204004/http://vistasmalltalk.wordpress.com/2007/04/18/thoughts-on-microsofts-silverlight/#comment-5636  ):


> But what are the capabilities of Silverlight itself? I came across this blog entry of someone who has downloaded the SDK, read the documentation, and looked at the code. Microsoft seems to be waiting for the Orcas release cycle before adding data binding, controls, and .Net runtime support to Silverlight - and Orcas could be delayed until 2008.


But before I clicked through to *that* blog entry, I started by reading this blog post on [the limitations of Silverlight](https://blog.codinghorror.com/lets-talk-about-the-american-dream/):


> Although I just found this post about it which points out that [Silverlight] has a lot of pretty major shortcomings.


The idea that Microsoft’s new Flash-alike **can’t even download data via HTTP** seemed impossibly wrong to me. Couldn’t be. Can’t be. Like any large company, Microsoft certainly makes their share of dumb mistakes. But an epic mistake like that stretches the bounds of credibility even for Microsoft.


In short, I didn’t believe it. So I downloaded the Silverlight SDK to take a look for myself. Guess what I found in the Silverlight SDK documentation, not five minutes after downloading it?


> The **Downloader** object is a special-purpose WPF/E object that provides the ability to download content, such as XAML content, JavaScript content, or media assets, such as images. By using the **Downloader** object you do not have to provide all application content when the WPF/E control is instantiated. Rather, you can download content on demand in response to application needs. The **Downloader** object provides functionality for initiating the data transfer, monitoring the progress of the data transfer, and retrieving the downloaded content.
> The properties and methods of the Downloader object are modeled after the XMLHttpRequest (XHR) set of APIs. [XMLHttpRequest](http://msdn2.microsoft.com/en-us/library/ms535874.aspx) provides JavaScript and other web browser scripting languages the ability to transfer and manipulate XML data to and from a web server using HTTP.


I’m not out to defend Silverlight here.


It’s clear that blogger A posted *completely erroneous information*; I’m not sure how he could have missed the obviously named and prominently featured Downloader object in the SDK. It really calls into question whether or not he actually used the SDK at all. But let’s assume, for the moment, that he did, and it was a simple oversight on his part. The strident tone of his post makes me think otherwise, but let’s give him the benefit of the doubt.


The real problem is that this erroneous information was echoed by blogger B, and then echoed *again* by blogger C. **At no point did anyone stop to actually verify the claims of blogger A, even in the most rudimentary, basic of ways.** All they had to do was download the SDK and look for themselves to confirm that his complaints were true. I’m talking five minutes, maximum.


But they didn’t.


Instead, they blindly parroted blogger A, assumed that all of his claims were valid, and perpetuated his mistake across the internet.


Let’s compare that behavior with the [Society of Professional Journalists Code of Ethics](http://www.spj.org/ethicscode.asp), which includes the following guidelines:

- Test the accuracy of information from all sources and exercise care to avoid inadvertent error. Deliberate distortion is never permissible.
- Diligently seek out subjects of news stories to give them the opportunity to respond to allegations of wrongdoing.
- Identify sources whenever feasible. The public is entitled to as much information as possible on sources’ reliability.


I realize that it’s unrealistic to hold every blogger on planet Earth to the same standards as [professionally trained journalists](http://en.wikipedia.org/wiki/Journalism_ethics_and_standards#Standards_and_reputation). Bloggers, after all, aren’t professionals.


But I do believe blog readers have a right to expect that amateur bloggers will:

1. Do their homework before writing.
2. Do some basic investigation of other bloggers’ claims *before* linking to their posts or quoting them.


None of these bloggers did any of the above. Don’t let their mistakes delude you into thinking this is typical or acceptable behavior. It isn’t. We may not be professional journalists – but we are still accountable for the words we write. It pains me that I even have to say this in 2007, but don’t assume everything you read on the internet is true. **Check the facts *yourself*.** Putting in that extra bit of effort won’t transform you into a journalist, but I can *guarantee* it’ll make you a better blogger.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[microsoft silverlight](https://blog.codinghorror.com/tag/microsoft-silverlight/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[xaml](https://blog.codinghorror.com/tag/xaml/)
[declarative programming](https://blog.codinghorror.com/tag/declarative-programming/)
