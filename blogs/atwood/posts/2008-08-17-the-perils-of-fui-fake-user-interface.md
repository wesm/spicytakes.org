---
title: "The Perils of FUI: Fake User Interface"
date: 2008-08-17
url: https://blog.codinghorror.com/the-perils-of-fui-fake-user-interface/
slug: the-perils-of-fui-fake-user-interface
word_count: 1122
---

As a software developer, tell me if you’ve ever done this:

1. Taken a screenshot of something on the desktop
2. Opened it in a graphics program
3. Gone off to work on something else
4. Upon returning to your computer, attempted to **click on the screenshot as if it was an actual program**.


And let’s not forget the common [goating](https://blog.codinghorror.com/dont-forget-to-lock-your-computer/) technique where you take a screenshot of someone’s desktop, make it the desktop background, then proceed to hide every UI element on the screen. The anguished cries as users desperately double-triple-quadruple click on pixels that *look exactly like real user interfaces* can typically be heard for miles.


I bring this up to generate some sympathy. I get fooled by my own FUI – Fake User Interface – at least once a month. If it can happen to us, it can happen to anyone. Which means FUI can be quite dangerous in the wrong hands. Consider [Ryan Meray's](http://www.ctechsinc.com/) story:


> Okay, so here’s an interesting one. My girlfriend is researching stuff on lilies, so she’s trying to find the website for the Michigan Regional Lily Society.
> The website address is [http://www.mrls.org/](https://web.archive.org/web/20080821032322/http://www.mrls.org/)
> Feel free and browse there directly, there’s nothing wrong with it. But if you don’t remember the URL, your first response is to Google it. We google and get this:
> [http://www.google.com/search?q=Michigan+Regional+Lily+Society](http://www.google.com/search?q=Michigan+Regional+Lily+Society)
> Now, if you’re in Firefox, everything is fine. You click that first result, and you get to their website, and you learn about lilies.
> However, if you are using IE, be aware, you are about to have a Spyware/Virus alert.


Obviously, the poor Michigan Regional Lily Society has fallen prey to website hackers. (Note that it may have been fixed by the time I’m writing this – but I duplicated everything I’m about to show you.)


The first clever point is that **the website appears fine if you navigate there directly**. The malicious JavaScript code inserted into the page checks the referer and does something different if you arrive there via a web search engine. This means the people who own the website, and never arrive there through Google, would be scratching their heads, wondering what all the fuss is about. So the hack survives longer.


But if you do arrive at the MRLS site through a search engine, like [a huge percentage of the world](https://blog.codinghorror.com/if-its-not-in-google-does-your-website-really-exist/) does, you’re redirected to:


`http://scanner.antivir64.com/?aff=1050`


The very first thing this page does is minimize the browser (Firefox 3, in this case) and present us with this JavaScript alert:


![](https://blog.codinghorror.com/content/images/2025/04/image-195.png)


I’m intentionally juxtaposing the browser and the dialog here, but the browser is way off in the very lower right corner of the display and that dialog is smack dab in the middle of the screen. It is not at all clear that the dialog originated from that web page. It’s a primitive technique, but it is surprisingly effective.


I didn’t have the guts to click OK on that dialog; I clicked the close button. The browser then expanded to show this convincing “real time virus scan.”


![](https://blog.codinghorror.com/content/images/2025/04/image-194.png)


The static screenshot does not do it justice; the scrollbar moves, the list of files fly by as they are “scanned,” and the web page rather successfully simulates an ersatz UI somewhere between Windows XP and Windows Vista. Of course, *we* know this Fake User Interface is completely invalid, because it is running in the browser, not on our PC. *You and I* may understand that distinction, but what about your parents? Your wife? Your children? Your less technically savvy friends? **Will they understand this scary, authentic looking virus warning coming from an “encrypted secure site” is all a lie?**


Honestly, whose PC doesn’t “run slower than normal”? Maybe I would want to know if my computer is infected with Viruses, Adware or Spyware. It’s all part of the [culture of fear](https://blog.codinghorror.com/trojans-rootkits-and-the-culture-of-fear/) that security software companies – and let’s be honest, *Windows* security software companies – cultivate so they can rake in millions of dollars per year hawking their software. The difference here, of course, is that **it’s increasingly difficult to tell the good guys from the bad guys**. That’s the downside of fear as a selling point: it cuts equally well in both directions.


Woe betide the poor user who is convinced through the trickery of FUI to install this “antivirus” software. The page does its darndest to **convince you to run its payload executable**. Any click on the page, no matter where, is interpreted as a download request.


![](https://blog.codinghorror.com/content/images/2025/04/image-193.png)


The page also attempts a drive-by download, though those have been auto-blocked for years now.


![](https://blog.codinghorror.com/content/images/2025/04/image-192.png)


It’s tempting to put this down as yet another iteration of [phishing, the forever hack](https://blog.codinghorror.com/phishing-the-forever-hack/). To be fair, this is exactly the sort of thing web browser phishing filters were designed to prevent. This site was already in the Firefox 3 phishing filter – but it was not caught by the Internet Explorer 7 phishing filter, so I reported it.


![](https://blog.codinghorror.com/content/images/2025/04/image-191.png)


I am all for phishing filters as another important line of defense, but like all distributed blacklists, they’re [only so effective](https://blog.codinghorror.com/blacklists-dont-work/).


What I’m more concerned about here is how *well* the user interface was spoofed. The browser FUI was convincing enough to even make me – possibly the world’s most jaded and cynical Windows user – do a bit of a double-take. How do you protect naïve users from cleverly designed FUI exploits like this one? Can you imagine your mother doing a web search on flowers – *flowers, for God’s sake* – clicking on the search results to a totally legitimate website, and **correctly navigating the resulting maze of fake UI, spurious javascript alerts, and download dialogs?**


I know I can’t. As much as I admire distributed phishing blacklist efforts, there’s no way they can possibly keep pace with the rapid setup and teardown of hacked websites. How many compromised websites are out there? How many unsophisticated users surf the internet every day?


As always, we can lay a big part of the blame at Microsoft’s doorstep for not adopting the UNIX policy of [non-administrator accounts for regular users](https://blog.codinghorror.com/the-windows-security-epidemic-dont-run-as-an-administrator/). But then again, if the spoofing is good enough, the FUI extra-convincing, even a Linux or OS X user could be coerced into entering their admin password for a “system security scan.” Or maybe they just wanted to [see the dancing bunnies](https://blog.codinghorror.com/the-dancing-bunnies-problem/).


And then, like Ryan, you’re likely to end up with the same infected computer, and the same distraught spouse. All this for the love of a few lilies.


Short of user education, which is a never ending, continuous uphill battle – **how would you combat a perfectly spoofed FUI presented to a naïve user?**

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[security](https://blog.codinghorror.com/tag/security/)
[fui](https://blog.codinghorror.com/tag/fui/)
[user interface](https://blog.codinghorror.com/tag/user-interface/)
