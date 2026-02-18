---
title: "A small website mystery"
date: 2017-05-10
url: https://jvns.ca/blog/2017/05/10/a-small-website-bug-story/
slug: a-small-website-bug-story
word_count: 783
---


Hello! For half of today, my website was broken! I like debugging
stories, so I thought I’d tell this one. Someone [tweeted at me](https://twitter.com/Shoxolat/status/862281387138838528) this morning
saying “hey your website has an issue”. They very kindly sent me a
screenshot:


Yep. That looks like an issue to me! I asked them to run `curl -i http://jvns.ca` and they sent me [the output](https://gist.github.com/jvns/33d5b9d45eaa6a827456daa3d6f278ba/raw/266e8584e127edf67345f1cca550b7118567c33c/gistfile1.txt).


Let’s take a look at the HTTP headers.


```
HTTP/1.1 200 OK
Date: Wed, 10 May 2017 13:12:18 GMT
Transfer-Encoding: chunked
Connection: keep-alive
Set-Cookie: __cfduid=d79dd5269ee9d191c6eb32a5ab5277a391494421938;
expires=Thu, 10-May-18 13:12:18 GMT; path=/; domain=.jvns.ca; HttpOnly
ETag: W/"3715-54e836f53861d-gzip"
Vary: Accept-Encoding
CF-Cache-Status: HIT
Expires: Thu, 11 May 2017 13:12:18 GMT
Cache-Control: public, max-age=86400
X-Content-Type-Options: nosniff
Server: cloudflare-nginx
CF-RAY: 35cd2639b2c36920-CDG

```


### why are these HTTP headers wrong?


There are two things to notice here: first, it says `ETag: W/"3715-54e836f53861d-gzip"`. This is a great clue. I was like “oh, is
it gibberish because it’s gzipped??”


How do you check if a file is gzipped? The easiest way is probably to
try to unzip it and see if it works. In this case the gzipped data was in the same file as the headers
though, so I ran `hexdump -c file.txt`. I looked at the bytes at the
beginning of the binary data and it said `1f 8b`. I [happen to know](https://jvns.ca/blog/2013/10/24/day-16-gzip-plus-poetry-equals-awesome/) that those are the 2 bytes every gzip stream starts with!


So, it was gzipped. That’s fine though, browsers can handle gzipped
data! The second thing to notice is, well, something that isn’t there.
When a site sends gzipped data, it’s meant to send a `Content-Encoding: gzip` header to say “hey, this content is gzipped, unzip it before
displaying it!” So we have our first mystery!


**mystery 1: why is the Content-Encoding: gzip header missing?**


### What happened to the Content-Encoding: gzip header?


I tried running `curl -I http://jvns.nfshost.com` (which is the backend
for my webhost, [https://jvns.ca](https://jvns.ca) uses Cloudflare) to look at the HTTP headers. It was returning a
`Content-Encoding: gzip` header! Here are the headers:


```
HTTP/1.1 200 OK
Date: Thu, 11 May 2017 01:51:56 GMT
Server: Apache
Upgrade: h2c
Connection: Upgrade
Last-Modified: Tue, 02 May 2017 05:01:38 GMT
ETag: "1fcdd-54e836f527c7c"
Accept-Ranges: bytes
Age: 118
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 14327
Content-Type: text/html; charset=UTF-8

```


This is also weird though! You might say – “okay, it says
Content-Encoding: gzip, that’s good”. But normally in order to get
gzipped content, you have to send an `Accept-Encoding: gzip` header to
say “I understand gzip!”. But I wasn’t sending that header with curl, and my site
was returning gzipped content anyway. Weird, right?


So we haven’t solved our mystery, but we’ve found a SECOND mystery:


**mystery 2: why does my site send gzipped content even when I didn’t ask it to??**


### the secret of the surprise gzipped content


I could think of an answer to the second mystery, though! A few years
ago, I felt like I was spending too much money on bandwidth, and I
wanted to save some money. I have a static site, so I gzipped every page
on my site, and set up this Apache configuration:


```
RewriteEngine on 
RewriteCond %{HTTP:Accept-Encoding} gzip 
RewriteCond %{REQUEST_FILENAME}.gz -f 
RewriteRule ^(.*)$ $1.gz [L] 

```


This tells Apache “hey, always send gzipped replies no matter what!!”.
So we’ve solved Mystery 2 – I deleted that `.htaccess` file, and
jvns.nfshost.com started behaving normally again.


Today my web host (nearlyfreespeech, which I like a lot) will
automatically gzip content when asked to, but it didn’t in the past!
([here’s the post announcing it](https://blog.nearlyfreespeech.net/2016/02/19/unlimited_free_bandwidth_some_limitations_apply/))


Also, when I cleared my Cloudflare cache my site started behaving
normally again, which I think means the problem is fixed. Maybe my weird
Apache rule’s aberrant behavior was causing Cloudflare to break somehow? Not clear!


### why did it take me half a day to fix it?


Normally if something is wrong with the Cloudflare version of my site
but the non-CDN version of my site seems ok, I could just turn off
Cloudflare for a bit to see if that fixes it. Hilariously, I turned on
[Strict-Transport-Security](https://jvns.ca/blog/2017/04/30/using-strict-transport-security/)
last week, which means my site only works if it’s served over HTTPS. And
my normal webhost isn’t set up with HTTPS yet, so I can’t just turn off
Cloudflare. That’s ok though, if a few pages on this blog are broken for
a few hours the world won’t end.


### What happened to the Content-Encoding: gzip header though?


I still don’t know where the Content-Encoding: gzip header went! Did
Cloudflare remove it? Did my webhost stop serving it for some reason? I
have no idea! Anyway, my site seems to work again (I think/hope?) and I
thought this was kind of a fun excursion into HTTP headers.
