---
title: "Whidbey ships with Visual SourceSafe"
date: 2004-09-11
url: https://blog.codinghorror.com/whidbey-ships-with-visual-sourcesafe/
slug: whidbey-ships-with-visual-sourcesafe
word_count: 672
---

At this week’s [Triangle .NET Users Group](http://www.trinug.org), Microsoft’s Doug Neumann gave a presentation on Visual Studio 2005 Team System, which looks great. What wasn’t so great, however, was the related news that Doug delivered: **Whidbey will ship with a “new” version of crusty old Visual SourceSafe**.


There will be some new features, as outlined in Korby Parnell’s blog:

- **Remote Access**. The new version of VSS will support remote access through firewalls via https. This is similar to an Outlook 2003 feature that enables people to access mail outside the firewall, without RAS. Remote access makes working from a remote location much easier. This includes remote teams (for example, with offshore development) as well as simpler scenarios like telecommuting or doing development work while traveling.
- **Improved Performance**. The new version of Visual SourceSafe will include improved performance and scalability for large projects and will make common operations faster and asynchronous, so you can start working more quickly on large projects and be productive while source control transfers are taking place.
- **Other Features**. SourceSafe Whidbey will include improved merging UI, support for Unicode file content viewing and merging, re-vamped source control for web service and web site projects, and a “check out local version” feature.


But this is still incredibly depressing news to me. Where do I begin?


Let’s get this out of the way first: [**Visual SourceSafe sucks**](http://www.highprogrammer.com/alan/windev/sourcesafe.html). I’m sorry, but it has to be said. It’s a ten year old application, and boy does it ever show. This isn’t an app that needs some incremental improvements, it’s an app that needs to be taken out behind the woodshed and put out of its misery. It is acceptable for rudimentary “better than nothing” source control, but not much more. We can’t even use branching on our projects at work because VSS has such terrible support for it!


**Why isn’t Microsoft shipping a “lite” version of Team System in the Whidbey box?** Why keep VSS on life support? This seems like a profoundly bad decision to me for a number of reasons:

- **It fragments the development userbase**. Some people have the default VSS, some people have Team System. The two systems are completely different and totally incompatible. I also suspect VSS will enjoy much wider usage because it will be “in the box”.
- **VSS will continue to be a second-class citizen.** Of course all the hot new features will be on the hot new platform, Team System. That’s where all the cool developers work. You don’t put your “A” development team on the crappy ten year old codebase.
- **It creates a development caste system.** The more I learn about TS, the more I think it seems destined for the nebulous and ultra-expensive “enterprise” software ghetto. I wonder how many people are going to actually benefit from it? How about a nice, modern version of source control for the common folk, without all that enterprise marketing crap (and the corresponding sticker shock).
- **Source control is a bread and butter function of development**. It’s irritating that Microsoft would treat such an essential part of development as something they can plug with a stopgap measure. this isn’t the first misstep Microsoft has made in this area – the Visual Studio 2005 Express products [**don’t even support source control!**](http://michaelteper.com/archive/2004/07/15/188.aspx)


Wouldn’t it be easier for Microsoft to have **one source control product to support**, rather than two? I don’t care if we get the “lite” version of Team System in the box; we probably won’t have time to make use of 80 percent of the whiz-bang features of the full Team System anyway.


But no. Instead, we’re stuck with a band-aided version of the geriatric Visual SourceSafe. I have zero confidence that the many problems of VSS will be addressed with this gussied-up point release. That means we’ll get the same marginal source control out of the box with VS.NET 2005 that we got with VS.NET 2003. How is this progress?

[microsoft visual studio](https://blog.codinghorror.com/tag/microsoft-visual-studio/)
[visual sourcesafe](https://blog.codinghorror.com/tag/visual-sourcesafe/)
[team system](https://blog.codinghorror.com/tag/team-system/)
[remote access](https://blog.codinghorror.com/tag/remote-access/)
[improved performance](https://blog.codinghorror.com/tag/improved-performance/)
