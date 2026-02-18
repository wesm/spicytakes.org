---
title: "Editing my blog's HTTP headers with Cloudflare workers"
date: 2018-09-03
url: https://jvns.ca/blog/2018/09/03/editing-my-blog-s-http-headers-with-cloudflare-workers/
slug: editing-my-blog-s-http-headers-with-cloudflare-workers
word_count: 1513
---


Hello! For the last 6 months, I’ve had a problem on this blog where every so often a page would show
up like this:


![](https://jvns.ca/images/blog-ugly.jpeg)


Instead of rendering the HTML, it would just display the HTML. Not all the time, just… sometimes.


I’ve gotten a lot of messages from readers with screenshots of this, and it’s no fun! People do not
want to read raw HTML. I would like my pages to render! I finally (I think) have a solution to this,
so I wanted to write up what I did.


### The mystery of the missing Content-Type header


It was clear basically the first time this happened that the reason was that there was a missing
HTTP `Content-Type` header. The `Content-Type` for HTML pages is supposed to be set to
`Content-Type: text/html; charset=UTF-8`. You can see this header with `curl -I`:


```
$ curl -I https://jvns.ca/
HTTP/1.1 200 OK
Date: Mon, 03 Sep 2018 13:59:16 GMT
Content-Type: text/html; charset=UTF-8 <========= this one
Content-Length: 0
Connection: keep-alive
CF-Cache-Status: HIT
Cache-Control: public, max-age=3600
CF-RAY: 4548bc69fc6c3fb9-YUL
Expires: Mon, 03 Sep 2018 14:59:16 GMT
Last-Modified: Sun, 02 Sep 2018 14:21:53 GMT
Strict-Transport-Security: max-age=2592000
Vary: Accept-Encoding
Via: e4s
X-Content-Type-Options: nosniff
Server: cloudflare

```


But sometimes, that Content-Type header would be missing. Weird!!! The most confusing thing about
this was that it happened very infrequently, and usually only on one page at a time, which made it a
lot harder to debug.


I haven’t had too much energy to debug this because while I think debugging weird computer
networking bugs is super fun, what I’ve been doing at work for the last while has been debugging
computer networking bugs and so I’m not that motivated to do it at home too. So that’s why this has
lasted for 6 months :)


### why is the Content-Type header missing?


So, why is the Content-Type header sometimes missing? I actually don’t know! My site is served by
nearlyfreespeech.net and cached by Cloudflare, so it’s something in there somewhere. Either:

- my webhost is not serving a Content-Type header sometimes (which doesn’t make much sense)
- the CDN is deleting the Content-Type header (which makes even less sense)


This isn’t the first time something like this happened – in 2017, the `Content-Encoding: gzip`
header [mysteriously disappeared](https://jvns.ca/blog/2017/05/10/a-small-website-bug-story/) and I
never found out why that was either. But! Even though I don’t know *why* this is happening and I
have no visibility into it, I can still try to fix it!


### things I tried


Before talking about my latest solution that I think will work, here are some things that I tried
that didn’t work:

- clearing my Cloudflare cache lots of times (this would temporarily fix the problem, but it would
just crop up again later)
- upgrading to a new ‘realm’ on my webhost, in the hopes that there was a bad Apache server or
something that I could move away from
- Making sure `<!DOCTYPE html>` was at the beginning of all my HTML in case that helped browsers
figure it out it was HTML (it didn’t)
- Switching away from nearlyfreespeech’s “free beta bandwidth” program
- emailing Cloudflare’s support to see if they knew anything about this
- making a lot of `curl` requests to my webhost directly to see if I could reproduce it (I couldn’t)


None of these things worked. The most annoying thing about this issue is that I couldn’t reliably
reproduce it, so it seemed hard to report to my web host (“hey, i have this problem periodically,
but you can’t observe it, you just have to take my word that it happens, can you do something?”)


The most obvious things to try that I haven’t tried are:

- changing web hosts to S3 or Github Pages or something (changing web hosts is time consuming &
annoying!)
- don’t use a CDN so that bad HTTP responses don’t get cached (for various reasons I want to keep
using a CDN :) )


### what worked: Cloudflare workers


At some point someone at Cloudflare very kindly offered to help me with my weird problem, and
suggested I use a new Cloudflare feature: [cloudflare workers](https://www.cloudflare.com/products/cloudflare-workers).


Basically Cloudflare Workers let you run a custom bit of Javascript on their servers for every HTTP
request that modifies the HTTP response. It costs $5/month to get started. This is useful because I
*know* that I want there always to be a Content-Type header. So if I can write some Javascript that
modifies the response header if there’s no Content-Type header, I can fix this problem!!!


When I woke up this morning a bunch of folks had tweeted at me saying that this problem had cropped
up again. I’d made an attempt at using Cloudflare workers in the past and not quite gotten it to
work, but since I was able to see the problem on my laptop (a very good thing, if I wanted to test a
fix!!), I decided to give it a shot again.


### my Javascript code


And this morning I got the Cloudflare workers working to fix the `Content-Type` header!!! So many
tiny little robots making things better.


Here’s my Javascript code! It basically just checks to see if the `Content-Type` header is missing
and if so, creates a new different Response object which includes a `Content-Type` header. The
reason I didn’t just modify the headers is that it turns out that you can’t modify the headers on a
Response object, so I needed to create a new one.


I also added a `x-julia-test` header for debugging purposes, so that I know that any response with
`x-julia-test` got its `Content-Type` header edited.


```
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

/**
 * @param {Request} request
 */
async function handleRequest(request) {
  const response = await fetch(request)
  const content_type = response.headers.get("Content-Type")
  if (!content_type) {
    var headers = new Headers();
    for (var kv of response.headers.entries()) {
      headers.append(kv[0], kv[1]);
    }
   
    const url = request.url
    console.log("Missing content type for url ", url)
    headers.set("Content-Type", get_content_type(url))
    headers.set("x-julia-test", "edited headers!")
    response.headers = headers
    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: headers})
  }
  return response
}

function get_content_type(url) {
  if (url.endsWith(".svg")) {
    return "image/svg+xml"
  } else if (url.endsWith(".png")) {
    return "image/png"
  } else if (url.endsWith(".jpg")) {
    return "image/jpg"
  } else if (url.endsWith(".css")) {
    return "text/css"
  } else if (url.endsWith(".pdf")) {
    return "application/pdf"
  } else {
    return "text/html; charset=UTF-8"
  }
} 

```


Writing this Javascript was a pretty pleasant experience – they have what looks just like a Chrome
console that you can use to run & preview your code.


### the results: it works!


Right now, Cloudflare’s cached version of [https://jvns.ca/blog/2018/09/01/learning-skills-you-can-practice/](https://jvns.ca/blog/2018/09/01/learning-skills-you-can-practice/) is missing its
Content-Type header (though this will likely have changed by the time this post goes up :)). After
installing the new Content-Type header and my test `x-julia-test` header, here’s what it looks like
when I `curl` the website!


```
$ curl -I https://jvns.ca/blog/2018/09/01/learning-skills-you-can-practice/ 
HTTP/1.1 200 OK
Date: Mon, 03 Sep 2018 14:20:11 GMT
Content-Type: text/html; charset=UTF-8 <==== I added this one!
Connection: keep-alive
Set-Cookie: __cfduid=d837320682d5cd76dc435ad3be07487ae1535984411; expires=Tue, 03-Sep-19 14:20:11 GMT; path=/; domain=.jvns.ca; HttpOnly
CF-Cache-Status: HIT
Cache-Control: public, max-age=3600
cf-ray: 4548db09caf63f95-YUL
etag: W/"46d9-574e4257a46f6"
expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
expires: Mon, 03 Sep 2018 15:20:11 GMT
strict-transport-security: max-age=2592000
vary: Accept-Encoding
via: e2s
x-content-type-options: nosniff
x-julia-test: edited headers! <==== I added this one!
Server: cloudflare

```


And if I load that page in Firefox, I can see that the headers got edited by my Cloudflare worker
(see the `x-julia-test` header at the bottom). Neat!


![](https://jvns.ca/images/firefox-headers.png)


And, most importantly, the website displays properly instead of being a bunch of raw HTML, which was
the point. Amazing!


### logging the HTTP requests & responses


I also tried adding some logging to the request workers by just making a server somewhere else that
logs all POST requests made to it, following the ([instructions here](https://developers.cloudflare.com/workers/writing-workers/debugging-tips/)).


I’m now logging all the requests & responses when the workers see a 200 that’s missing a
Content-Type header. (There are also some 304 responses missing a Content-Type header, but that’s
normal!). It hasn’t turned up anything yet, but maybe something will appear eventually!


### cloudflare workers are neat


I usually don’t talk about paid services on this blog and these workers definitely aren’t free (they
charge $5/month for up to 10 million requests/month). But this was useful to me and I think it’s
really cool to be able to write arbitrary Javascript code that modifies all of my blog’s HTTP
responses!


It’s definitely a hack – running custom javascript on every single HTTP request is an extremely
silly way to fix what is probably some kind of server configuration issue somewhere.  But it helps
me fix my problem until I decide to spend the time to migrate web hosts or whatever, so I’m happy
with that. Paying $60/year is definitely worth it to me to fix the problem & not have to spend the
time to migrate to a different host right now :)


Looking at the CDN landscape in general, Fastly offers a seemingly similar feature called the [Edge SDK](https://www.fastly.com/products/edge-sdk) that lets you write VCL (“varnish configuration
language”). I haven’t used that though.
