---
title: "This Site May Harm Your Computer"
date: 2007-05-10
url: https://blog.codinghorror.com/this-site-may-harm-your-computer/
slug: this-site-may-harm-your-computer
word_count: 709
---

[The Ghost In The Browser](http://www.usenix.org/events/hotbots07/tech/full_papers/provos/provos.pdf): Analysis of Web-based Malware (pdf) describes **how Google is leveraging their overwhelming search dominance to combat browser malware installations**. In [a blog entry last summer](http://www.mattcutts.com/blog/siteadvisor-study/), Matt Cutts said:


> Given how much I hate web pages that install malicious software or abuse browser security holes, I’d like it if we did even more to protect our users.


Apparently, they’ve [done even more to protect users](http://www.mattcutts.com/blog/how-google-handles-malware-a-historical-overview/) since then. Here’s a Google search result tagged with the ominous warning “This site may harm your computer:”


![Search results page with an entry tagged 'this site may harm your computer'](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b0120a86d7e77970b-pi.png)


Clicking “[This site may harm your computer](http://www.google.com/support/bin/answer.py?answer=45449&topic=360&hl=en&sa=X&oi=malwarewarninglink&resnum=1&ct=help)” leads to a Google support page. Attempting to click through to the actual website results in an interstitial warning, offering no way to click through:


![Warning - vsiting this site may harm your computer!](https://blog.codinghorror.com/content/images/uploads/2007/05/6a0120a85dcdae970b0120a86d7e88970b-pi.png)


I think this is a fairly effective method of warning away most rational users from a clearly evil website. Of course, users who desire whatever media, software, or pornography the site is hawking can still type the URL in their address bar. Users will find a way to see [the dancing bunnies](https://blog.codinghorror.com/the-dancing-bunnies-problem/) if they really, *really* want to, no matter how many warnings and barriers you blast in front of them.


If you want to see what’s behind that URL, fair warning: in addition to being outright dangerous for a machine that’s not patched to the gills, it’s NSFW in a big way. A little investigation showed that it’s doing the following:

- Attempts to use the remote data services ActiveX control.
- Shows a spoof HTML page with the text “windows media player cannot play video file; Click here to download missing Video ActiveX object.” The download runs setup.exe.
- Runs Javascript with exploit sniffing code.


If you accept that Google wields the immense power of being [the de-facto start page](https://blog.codinghorror.com/if-its-not-in-google-does-your-website-really-exist/) for the internet, then maybe this kind of policing effort comes with the territory. **To do nothing – to let these purely evil sites show up in Google results with no warning whatsoever – would be irresponsible.** Although a person might be performing questionable searches to get this page in their results, it’s irrelevant. Despite the individual ethics of the person using that one computer, a compromised computer will be used for attacks and spam against everyone.


Still, I’m a little curious. Why does Google deploy the ultimate weapon of search delisting on sites using black-hat SEO techniques to game search rankings, while known evil malware sites get stern warning interstitials instead? I brought up the Google result by doing a direct search on the domain name. The very same search **produces no results on live.com or ask.com**. Clearly that site has been delisted by everyone except Google. The domain still has a PageRank of four. I applaud the effort, but what value does keeping a site like that in your search index have for users?


Even if your web site is *not* evil, it’s possible for others to inject malicious code into your page if you’re not careful. The [Google whitepaper](http://www.usenix.org/events/hotbots07/tech/full_papers/provos/provos.pdf) provides three external vectors that can turn a good web page to the dark side:

- Compromised webservers can insert malicious code into all HTML pages served
- Pages which allow user-contributed HTML, where the HTML hasn’t been properly sanitized
- The use of questionable advertising content, or compromised ad servers


It’s scary how many ways this can happen. I strongly urge you to read the whitepaper to get all the gory details.


Google’s paper says **one in ten webpages contains malicious code**. The most direct way to address malware delivered via web pages is to increase the security of the operating system and the browser, so “drive-by downloads” cannot happen without the user’s explicit consent. But a problem as large as malware should be attacked on multiple fronts. Search engines are in a unique position to help index and identify malicious webpages, and prevent them from being accessible in search results. It’s encouraging to read about Google’s architecture for automatically identifying malicious URLs. I don’t think it’s fair to call this Google policing the web; it’s just good, ethical business to **filter out the evil**.

[security](https://blog.codinghorror.com/tag/security/)
[malware](https://blog.codinghorror.com/tag/malware/)
[browser security](https://blog.codinghorror.com/tag/browser-security/)
[google](https://blog.codinghorror.com/tag/google/)
[web-based threats](https://blog.codinghorror.com/tag/web-based-threats/)
