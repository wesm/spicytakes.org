---
title: "Universally Annoying Remotes, Revisited"
date: 2005-01-24
url: https://blog.codinghorror.com/universally-annoying-remotes-revisited/
slug: universally-annoying-remotes-revisited
word_count: 588
---

Alex Gorbatchev posted his very favorable [review of the Harmony H659](https://web.archive.org/web/20060420204747/http://blog.dreamprojections.com/archive/2005/01/17/532.aspx) universal remote:


> *This weekend I made one of the best purchases ever and I’m not exaggerating. Up until now I have been in the remote hell. Let me describe my living room setup: TV, DVD, Receiver, PVR and Xbox. That makes a total of five remotes I need to operate to do certain tasks. Most of the time any activity involves at least two remotes. I was seriously getting tired of this.*


Which reminded me – It’s been a month since I [purchased my Harmony H680 remote](https://blog.codinghorror.com/universally-annoying-remotes/). I try to avoid commenting on products until I’ve lived with them long enough to get past the new purchase honeymoon phase, and I think I’m well past that point now.


The short answer is, **yes, it really works**. You want one remote that’s easy to program, easy to use, and controls all your devices? Look no further. I haven’t touched any of the original four remotes in a month!


Although this is the likely the best and easiest to use universal remote on the market, I still have a few quibbles.

1. **Web interface**
You set up the remote through a website, which seems like a good idea at first. However, the more you work with it, the more you realize that plain HTML interfaces are a giant pain in the ass for complex applications like this. Harmony Central is a classic argument for [smart client applications](https://web.archive.org/web/20051028060951/http://msdn.microsoft.com/netframework/programming/winforms/smartclient.aspx). It’s great that they have a huge database of user-submitted devices, but that doesn’t justify suffering through a tedious HTML interface to edit everything, or waiting ~12 seconds to postback through 3 screens to get somewhere. And programming the remote over USB is done by downloading a file from the browser, which executes through an associated handler. It works, but it’s all very hacky and much slower than it needs to be. Square peg, meet round hole. This should be WinForms + HTTP and a supporting website.
2. **Button delays**
The default inter-button and inter-device delays are far too slow, on the order of 200ms. This can be adjusted in the advanced options of the website*. Even with the button delays set to minimum, the remote isn’t responsive enough. On the Tivo remote, I could hit down-down-down and see immediate response, but with the Harmony it’s down (pause) down (pause) down (pause) if I want the commands to be registered.
3. **Command repeat**
Evidently, most remotes repeat individual IR commands multiple times to ensure they’re received. By default, the Harmony repeats IR commands three (!) times. This results in weird side effects – when I press volume up, the receiver steps up the volume 2 to 3 notches, and when I use channel down to navigate through long lists I frequently move down two screens instead of just one. Setting the repeat* value to 1 caused the remote to barely function. And setting it to 2 still results in some repeated IR commands.


None of these things are deal breakers, but they’re annoying. I suggest reading through the [Remote Central Harmony forums](https://web.archive.org/web/20050127050929/http://www.remotecentral.com/cgi-bin/mboard/rc-harmony/list.cgi) for lots of great tips and tricks.


*Good luck finding these advanced settings on the website, by the way. They’re under “troubleshooting” and at least 3 webpages deep on the site, none of which allow you to use the back button. Someone send these guys a clone of [Chris Sells](http://www.sellsbrothers.com) – patron saint of Smart Client applications – stat!

[remote controls](https://blog.codinghorror.com/tag/remote-controls/)
[universal remote](https://blog.codinghorror.com/tag/universal-remote/)
[consumer electronics](https://blog.codinghorror.com/tag/consumer-electronics/)
[software integration](https://blog.codinghorror.com/tag/software-integration/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
