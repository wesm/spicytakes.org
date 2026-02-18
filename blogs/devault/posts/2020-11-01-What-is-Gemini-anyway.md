---
title: "What is this Gemini thing anyway, and why am I excited about it?"
date: 2020-11-01
url: https://drewdevault.com/2020/11/01/What-is-Gemini-anyway.html
slug: What-is-Gemini-anyway
word_count: 1104
---

I’ve been writing about some specific topics in the realm of Gemini on my blog
over the past two months or so, but I still haven’t written a broader
introduction to Gemini, what I’m doing with it, and why you should be excited
about it, too. Let’s do that today!

[Gemini](https://gemini.circumlunar.space/)  is a network protocol for exchanging
hypertext documents — “hypertext” in the general sense of the word, not
with respect to the hypertext markup language (HTML) that web browsers
understand. It’s a simple network protocol which allows clients to request
hypertext documents (in its own document format, gemtext). It is, in some
respects, an evolution of  [Gopher](https://en.wikipedia.org/wiki/Gopher_(protocol)) , but more modernized and streamlined.

Gemini is very simple. The protocol uses TLS to establish an encrypted
connection (using self-signed certificates and
 TOFU  rather than certificate
authorities), and performs a very simple exchange: the client sends the URL it
wants to retrieve, terminated with CRLF.  The server responds with an
informative line, consisting of a numeric status code and some additional
information (such as the document’s mimetype), then writes the document and
closes the connection. Authentication, if desired, is done with client
certificates. User input, if desired, is done with a response code which conveys
a prompt string and a request for user input, followed by a second request with
the user’s response filled into the URL’s query string. And that’s pretty much
it!

```
$ openssl s_client -quiet -crlf   \
    -servername drewdevault.com   \
    -connect drewdevault.com:1965 \
  | awk '{ print "response: " $0 }'
gemini://drewdevault.com
response: 20 text/gemini
response: ```ASCII art of a rocket next to "Drew DeVault" in a stylized font
response:   /\
response:   ||    ________                         ________       ____   ____            .__   __
response:   ||    \______ \_______   ______  _  __ \______ \   ___\   \ /   /____   __ __|  |_/  |_
response:  /||\    |    |  \_  __ \_/ __ \ \/ \/ /  |    |  \_/ __ \   Y   /\__  \ |  |  \  |\   __\
response: /:||:\   |    `   \  | \/\  ___/\     /   |    `   \  ___/\     /  / __ \|  |  /  |_|  |
response: |:||:|  /_______  /__|    \___  >\/\_/   /_______  /\___  >\___/  (____  /____/|____/__|
response: |/||\|        \/            \/                 \/     \/             \/
response:   **
response:   **
response: ```
[...]
```

So why am I excited about it?

My disdain for web browsers is well documented 1 . Web browsers are
 *extraordinarily*  complex, and any attempt to build a new one would be a
Sisyphean task. Successfully completing that implementation, if even possible,
would necessarily produce a Lovecraftian mess: unmaintainable, full of security
vulnerabilities, with gigabytes in RAM use and hours in compile times. And given
that all of the contemporary web browsers that implement a sufficiently useful
subset of web standards are ass and getting assier, what should we do?

The problem is unsolvable. We cannot have the “web” without all of these
problems. But what we can have is something different, like Gemini. Gemini does
not solve all of the web’s problems, but it addresses a subset of its use-cases
better than the web does, and that excites me. I want to discard the parts of
the web that Gemini does better, and explore other solutions for anything that’s
left of the web which is worth keeping (hint: much of it is not).

There are some aspects of Gemini which I approve of immensely:

* It’s dead simple. A client or server implementation can be written from
scratch by a single person in the space of an afternoon or two. A new web
browser could take hundreds of engineers millions of hours to complete.
* It’s not extensible. Gemini is designed to be  *difficult*  to extend without
breaking backwards compatibility, and almost all proposals for expansion on
the mailing list are ultimately shot down. This is a good thing: extensibility
is generally a bad idea. Extensions ultimately lead to more complexity and
Gemini might suffer the same fate as the web if not for its disdain for
extensions.
* It’s opinionated about document formatting. There are no inline links (every
link goes on its own line), no formatting, and no inline images. Gemini
strictly separates the responsibility of content and presentation. Providing
the content is the exclusive role of the server, and providing the
presentation is the exclusive role of the client. There are no stylesheets and
authors have very little say in  *how*  their content is presented. It’s still
possible for authors to express themselves within these constraints —
as with any other constraints — but it allows clients to be simpler and
act more as  *user*  agents than  *vendor*  agents.

Some people argue that what we should have is “the web, but less of it”, i.e. a
“sane” subset of web standards. I don’t agree (for one, I don’t think there  *is* 
a “sane” subset of those standards), but I’ll save that for another blog post.
Gemini is a new medium, and it’s different from the web. Anyone who checking it
out should be prepared for that and open to working within its constraints.
Limitations breed creativity!

For my part, I have been working on a number of Gemini projects. For one, this
blog is now available  [on Gemini](gemini://drewdevault.com) , and I have started
writing some Gemini-exclusive content for it. I’ve also written some software
you’re welcome to use:

[**libgmni**](https://sr.ht/~sircmpwn/gmni) ,
 [**gmni**](https://sr.ht/~sircmpwn/gmni) ,
and  [**gmnlm**](https://sr.ht/~sircmpwn/gmni)  are my suite of Gemini client
software, all written in C11 and only depending on a POSIX-like system and
OpenSSL. libgmni is a general-purpose Gemini client library with  [a simple
interface](https://git.sr.ht/~sircmpwn/gmni/tree/master/include/gmni) . gmni is a
cURL-like  [command line tool](https://drewdevault.com/gmni.1.html)  for
performing Gemini requests. Finally, gmnlm is a line-mode browser with a rich
feature-set. Together these tools weigh just under 4,000 lines of code, of which
about 1,600 are the URL parser from cURL vendored in.

[**gmnisrv**](https://portal.drewdevault.com/gmnisrv.gmi)  is a high-performance
Gemini server, also written in C11 for POSIX systems with OpenSSL. It supports
zero-configuration TLS, CGI scripting, auto-indexing, regex routing and URL
rewrites, and I have a couple more things planned for 1.0. It clocks in at about
6,700 lines, of which the same 1,600 are vendored from cURL, and an additional
2,800 lines are vendored from Fabrice Bellard’s
 [quickjs](https://bellard.org/quickjs/)  regex implementation.

[**kineto**](https://portal.drewdevault.com/kineto.gmi)  is an HTTP-to-Gemini
gateway, implemented as a single Go file (under 500 lines) with the assistance
of ~adnano’s  [go-gemini](https://sr.ht/~adnano/go-gemini/)  library. My Gemini
blog  [is available through this portal](https://portal.drewdevault.com)  if you
would like to browse it.

So dive in and explore! Install gmnisrv on your server and set up a Gemini space
for yourself. Read the feeds from
 [CAPCOM](gemini://gemini.circumlunar.space/capcom/) . Write some software of your
own!

1. [Exhibit A](https://drewdevault.com/2020/08/13/Web-browsers-need-to-stop.html), [Exhibit B](https://drewdevault.com/2020/03/18/Reckless-limitless-scope.html), [Exhibit C](https://cmpwn.com/@sir/104894723861368333) ↩︎
