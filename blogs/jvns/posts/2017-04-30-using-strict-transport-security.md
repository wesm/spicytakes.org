---
title: "Using the Strict-Transport-Security header"
date: 2017-04-30
url: https://jvns.ca/blog/2017/04/30/using-strict-transport-security/
slug: using-strict-transport-security
word_count: 1377
---


I just updated my site today to use the `Strict-Transport-Security` (or
“HSTS” as it’s often called) header, and I think it’s an interesting
thing to know about so I thought I’d tell you all about it.


Extra disclaimer for web security posts: I’m not a security
person, you should not take security advice from me, security is
complicated. This is just what I understand so far! I think most of this
is right but if it’s wrong let me know!


### HTTPS is good


The idea behind the Strict-Transport-Security header is that if you
have a HTTPS site (like github.com), you might want your users to *always* use the HTTPS
version of your site.


Until yesterday, my site had a HTTP version and an HTTPS version. So you
could go to [http://jvns.ca](http://jvns.ca) or [https://jvns.ca](https://jvns.ca), depending on what you
wanted! This was fine, because my site is a static HTML site and there’s
no private content on it at all.


But a lot of sites *do* have private content, and should always use
encryption! The standard practice if you always want your site to be
served with HTTPS is:

1. Don’t serve a HTTP version of your site at all. Always redirect HTTP
to HTTPS (run `curl -I http://github.com` to see that they do a
redirect to HTTPS!)
2. Force browsers to *never* visit the HTTP version (not even once!), using the HSTS
header and the “preload list”, which I’ll explain!


As I understand it, there are 2 reasons it isn’t enough to *just* redirect HTTP -> HTTPS is:


**reason 1**: If I go to [http://github.com](http://github.com), by default my browser will send my GitHub
cookies unencrypted, which is bad! Somebody could steal them! So it’s
better if I never visit [http://github.com](http://github.com) at all, even if I type it in
by accident or I click on a malicious link. You can also fix this by
setting the `secure` flag on a cookie, though, which means it’ll never
be sent over HTTP.


**reason 2**: If a sketchy free wifi portal starts serving a fake
“github.com” site, then I don’t want my browser to be tricked. If my
browser refuses to visit any HTTP version of github.com, ever, then I’m
safer. An evil ISP can’t inject ads / malware into my website!


### The Strict-Transport-Security header


Strict-Transport-Security is also knows as “HTTP Strict Transport
Security” or “HSTS”. I’ll use “HSTS” and “Strict-Transport-Security”
interchangeably.


Let’s start with an example of how GitHub uses the
Strict-Transport-Security header and then we’ll talk about what it
does!


First, if I try to go to [http://github.com](http://github.com), I just get a redirect to the
HTTPS version of the site. Here’s what that looks like


```
bork@kiwi~> curl -I http://github.com
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://github.com/
Connection: close

```


Next, when I visit [https://github.com](https://github.com), you can see that they return this
header called `Strict-Transport-Security`


```
bork@kiwi~> curl -I https://github.com
HTTP/1.1 200 OK
Server: GitHub.com
Date: Sun, 30 Apr 2017 17:36:21 GMT
Content-Type: text/html; charset=utf-8
Status: 200 OK
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
(a bunch more stuff removed)

```


So, what does this `Strict-Transport-Security` header mean?
“Strict-Transport-Security” is a way to to tell browsers “hey, never
visit the HTTP version of this site ever”.


So after I visit **https**://github.com one time in my browser, it will
never visit **http**://github.com again. If I write [http://github.com](http://github.com)
it’ll just pretend I wrote `https`.


### The preload list


Okay, so you set the Strict-Transport-Security header! That’s awesome,
but the first time someone tries to go to [http://github.com](http://github.com) they’ll still
visit the insecure version one time.


So browsers do **another** thing called the “preload list”. The idea
here is that Chrome & Firefox will download a list of sites which should
all use HTTPS. If a site is on the list.


If you want to apply to have your site added to the list, you can do it
at [https://hstspreload.org/](https://hstspreload.org/). You can see GitHub’s status at [https://hstspreload.org/?domain=github.com](https://hstspreload.org/?domain=github.com). (they’re on the list!)


### why did I turn it on?


I put an embedded payment form in [this blog post](https://jvns.ca/blog/2017/04/29/new-zine--let-s-learn-tcpdump/)
(from Gumroad).
The payments were definitely made using HTTPS either way (Gumroad
embedded a secure iframe in my site), so you might think it doesn’t
matter if the site is HTTP or HTTPS!


But, if your site has both HTTP and HTTPS content, then users’ browsers
will show a “mixed content warning”.


The reason mixed content is bad is – any HTTP content can be interfered
with! So if I have a HTTP page with a secure payments thing embedded in
it, someone could replace the secure payments thing with an Evil Bad
Payments Thing. That would be no good! If everything on the page is
HTTPS, then we know it’s all for sure from who it says it is.


The other reason that I find compelling is – sometimes ISPs will inject
ads into sites. I don’t want ads injected into my site! I want people to
see my site exactly how I intended them to see it. If my site is always
served with HTTPS, I can be confident nobody has done anything sketchy
to it.


There’s also an argument to be made that [HTTPS can be faster than HTTP](https://www.troyhunt.com/i-wanna-go-fast-https-massive-speed-advantage/)
(for sites that support HTTP/2, which mine does because I use Cloudflare). I don’t actually know
if my site is faster with HTTPS, but that blog post is really
interesting and you should read it.


### HSTS: you can’t go back


I use Cloudflare’s free version, and I turned on HSTS with Cloudflare by
clicking an “Enable HSTS”. Before letting me do it, I had to read the
following warnings:


> If you have HSTS enabled and leave Cloudflare, you need to continue to
> support HTTPS through a new service provider otherwise your site will
> become inaccessible to visitors until you support HTTPS again.


> If you turn off Cloudflare’s HTTPS while HSTS is enabled, and you
> don’t have a valid SSL certificate on your origin server, your website
> will become inaccessible to visitors.


This is kind of scary! Basically browsers will really refuse the visit
the HTTP version of your site after you turn on HSTS. So you’d better
make sure that you can keep having a HTTPS version of your site forever.
This is what the max-age setting is for (I set it to 1 month to start because I
was nervous and that was the lowest setting they’d let me use).
This is why I didn’t turn on HSTS right away when I first made a HTTPS
version for my site.


Luckily, these days anyone can get a free SSL/TLS certificate with [Let’s Encrypt](https://letsencrypt.org/) so even
if I stop using Cloudflare, I can pretty easily get a TLS
certificate for my site and keep providing a secure version.


That said, if you’re gonna turn on HSTS it’s extremely important to make
sure that you’re prepared to keep serving a secure site indefinitely.


### Cloudflare


Technically the fact that my site uses HTTPS doesn’t mean that
everything on the site is from **me** – Cloudflare actually owns the
TLS certificate for my site, and they can (and do!) add stuff to my
website, like a Google analytics code.


I’m okay with this because I trust Cloudflare not to add anything
evil to my site, but I think it’s still useful to keep in mind.


### how can I tell if my site is using the HSTS header properly?


Great question! There’s a site called
[https://observatory.mozilla.org/analyze.html](https://observatory.mozilla.org/analyze.html) that you can use to give
you a report card!


For example:

- github: [https://observatory.mozilla.org/analyze.html?host=github.com](https://observatory.mozilla.org/analyze.html?host=github.com)
- jvns.ca: [https://observatory.mozilla.org/analyze.html?host=jvns.ca](https://observatory.mozilla.org/analyze.html?host=jvns.ca)


You can see that GitHub gets an A+ (yay!) and that I get an F (aw.). I
think this is okay because my site doesn’t set any cookies with
sensitive information, but it kinda makes me feel like I
*should* increase my site’s rating now =).


### that’s all!


There are a lot of security headers to know about. Here’s a partial
list:

- Access-Control-Allow-Origin
- Content-Security-Policy
- Strict-Transport-Security


I think those three are the most important?


and there’s also

- Public-Key-Pins
- X-Content-Type-Options
- X-Frame-Options
- X-XSS-Protection
- … and more!


The [Mozilla Web Security Guidelines](https://wiki.mozilla.org/Security/Guidelines/Web_Security)
looks to me like a good reference if you want to understand what some
specific header does.
