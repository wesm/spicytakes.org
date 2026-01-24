---
title: "Are Web Interfaces “Good Enough?”"
date: 2007-03-14
url: https://blog.codinghorror.com/are-web-interfaces-good-enough/
slug: are-web-interfaces-good-enough
word_count: 1173
---

[Torrent](http://www.utorrent.com/), my favorite BitTorrent client, now offers a web UI. See if you can spot the differences between the Web UI and the Windows UI:


![Torrent web UI](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0120a86d8640970b-pi.png)


![Torrent Windows UI](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0120a86d8653970b-pi.png)


After spending about a year interacting with Torrent exclusively through Remote Desktop, I was pleasantly surprised to discover how good the web UI is. It aggressively exploits the latest Ajax techniques to replicate most of the rich GUI functionality of Torrent in a browser. But the web UI is still a pale shadow of the full-blown Windows UI. There are small but important details missing throughout, and part of the pleasure of using Torrent was luxuriating in its intense attention to detail, its wealth of well-designed data readouts. Using the web UI is like drinking watered-down beer. It doesn’t satisfy.


**But *does it matter?*** Despite my nitpicking, I can do everything I need to do remotely through the web UI.


I do sometimes miss the fit and finish of the complete Windows UI. But if the only way to achieve full fidelity is to log in to the machine as a user via Remote Desktop, it’s hardly worth the effort. Remote GUI technology has never caught on, either in Windows ([RDP](http://en.wikipedia.org/wiki/Terminal_Services)), in UNIX ([X11](http://en.wikipedia.org/wiki/X_Window_System)), or even on the Mac ([ARD](http://en.wikipedia.org/wiki/Apple_Remote_Desktop)). This approach has always felt like overkill, and it doesn’t seem workable based on the historical evidence.


But maybe “good enough,” via the eccentric and often unreliable combination of DHTML, JavaScript, and HTML, is all we need. That’s [what Joel Spolsky thinks](http://www.joelonsoftware.com/articles/APIWar.html), anyway:


> So the Web user interface is about 80% there, and even without new web browsers we can probably get 95% there. This is Good Enough for most people and it’s certainly good enough for developers, who have voted to develop almost every significant new application as a web application.
> I’m actually a little bit sad about this, myself. To me the Web is great but Web-based applications with their sucky, high-latency, inconsistent user interfaces are a huge step backwards in daily usability. I love my rich client applications and would go nuts if I had to use web versions of the applications I use daily: Visual Studio, CityDesk, Outlook, Corel PhotoPaint, QuickBooks. But that’s what developers are going to give us. Nobody (by which, again, I mean “fewer than 10,000,000 people”) wants to develop for the Windows API any more. Venture Capitalists won’t invest in Windows applications because they’re so afraid of competition from Microsoft. And most users don’t seem to care about crappy Web UIs as much as I do.
> None of this bodes well for Microsoft and the profits it enjoyed thanks to its API power. The new API is HTML, and the new winners in the application development marketplace will be the people who can make HTML sing.


Bruce Eckel read the same tea leaves as Joel Spolsky, and concludes that the future of rich web applications lies [not in HTML, but in Flash](https://web.archive.org/web/20070314000133/http://www.artima.com/weblogs/viewpost.jsp?thread=193593):


> JavaScript has been around since, effectively, the beginning of the Web, but the browser wars made JavaScript inconsistent and thus painful to use. A key part of Ajax is that someone has gone to the trouble of figuring out cross-platform JavaScript issues so you can ignore the often radical inconsistencies between different browsers.
> There are two problems with this approach. The first is that JavaScript is limited in what it can do. Although Ajax is an excellent hack that gets the last bit of mileage from JavaScript, it is nonetheless a hack, and the end is in sight. The second problem is that you are relying on Ajax libraries to handle cross-browser issues. If you want to write your own code, you must become an expert on those issues, and at that point much of the leverage of Ajax goes away. Ajax improves the experience a lot, but it has limits and I suspect we’ve already seen most of the tricks that Ajax is going to offer.
> There’s a very impressive Flash web app called Gliffy that imitates Visio (this was created with OpenLaszlo, which I’ll mention later). No one could even think of creating something like that with Ajax, although someone did an imitation of the much simpler Microsoft Paint using HTML, CSS and JavaScript. Very impressive, but you get the sense that this is close to the limit of what those technologies can do, whereas Flash would just be getting started. Plus the Paint clone is a bit slow and clunky and the UI is inconsistent across browsers.
> While amazing things have been accomplished within the confines of JavaScript with technologies like Ajax, JSON, GWT etc., these are nonetheless confines. We bump up against their limits every day, and those limits are not going away.


I think Eckel is too quick to dismiss the utility of browser-based JavaScript applications. Yes, they’re painful to create and debug, but they exploit the path of least resistance. And if I have learned anything in my entire life, it is this: *never bet against the path of least resistance.* You will lose. Every time. What Eckel neglects to consider is this:

- The typical user only touches a fraction of the functionality in most applications. Switching to an online spreadsheet like EditGrid or WikiCalc is hardly a catastrophic loss when you only used 1 percent of Excel’s functionality to begin with.
- Online applications may be awkward, but they do one key thing that local applications can never do: embed snippets of live content in a web page. [Instacalc](http://instacalc.com/) may never be Excel, but so what? It’s a completely different use case. Instacalc is ideal for embedding bite-sized, interactive nuggets of calculation next to a paragraph of text on a web page. It’s the YouTube of spreadsheets.
- Eckel sees a world of JavaScript and DHTML that’s inappropriate for large applications. I see a world of large applications that are inappropriate for most users. It’s high time we scaled down and scaled back. If anything, this is a *beneficial* side-effect of the limitations inherent to the platform.


Like Joel, I think the future of many – but not all – applications is in the browser. Web apps are good enough today for most tasks, and they’re getting better every year. **The web browser is the giant black hole of the computing universe, and like it or not, your application is caught in its immense gravitational pull along with the rest of us.**


As useful and as clever as Torrent’s web UI is, I’m still deeply disappointed. I’m disappointed that, with all the technology at our disposal, we can’t come up with some way to deliver a full-fidelity user interface over the wire for an application as nifty as Torrent. I’ll belatedly agree that web interfaces are “good enough” – but after all these years of progress, why should we have to *settle* for something that’s merely “good enough?” There has to be a[ better way](https://web.archive.org/web/20070318030210/http://msdn2.microsoft.com/en-us/architecture/bb288452.aspx) out there somewhere.

[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[ajax](https://blog.codinghorror.com/tag/ajax/)
[remote access](https://blog.codinghorror.com/tag/remote-access/)
[software interfaces](https://blog.codinghorror.com/tag/software-interfaces/)
