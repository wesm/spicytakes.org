---
title: "Using .htaccess Redirection to Standardize Web Server Addresses"
date: 2006-05-05
url: https://daringfireball.net/2006/05/htaccess_redirection
slug: htaccess_redirection
word_count: 1225
---


Answers to a couple of somewhat frequently-asked questions about the
.htaccess tricks I’m using to standardize the domain names at Daring
Fireball:


## Getting Rid of ‘www’ Prefixes


I’ve always rather disliked the “www” prefix for web servers.
It has become so common that everyone is accustomed to both seeing
and saying it, and so it’s sort of invisible now, but it really is a
goofy convention.1


Long ago, I started using [.htaccess](http://en.wikipedia.org/wiki/Htaccess) redirection to standardize all
Daring Fireball URLs on the prefix-less “daringfireball.net”
address. If you attempt to load “www.daringfireball.net/*anything*”,
you’ll be redirected to “daringfireball.net/*anything*”.


Here’s the applicable portion of my .htaccess file, located in the
root of my web hosting directory:


```
RewriteEngine on
RewriteBase /

RewriteCond %{HTTP_HOST} ^www\.daringfireball\.net$
RewriteRule (.*) http://daringfireball.net/$1 [R=Permanent]

```


The first line turns on Apache’s mod_rewrite module. The second line
sets the “base” URL to the root of the domain.


The RewriteCond line specifies a condition for the subsequent rule
— i.e. the rule on the next line is only applied if the condition
in this line is met. There are two parts to the condition: a test
string, and a regular expression to match against the test string.
The parts are separated by spaces.


The test string, “`%{HTTP_HOST}`”, is a reference to the HTTP_HOST
header that came in with the HTTP request. It’s the name of the
server the request has been sent to. The pattern,
“`^www\.daringfireball\.net$`”, is a precise regular expression that
will successfully match when the HTTP_HOST header is
“www.daringfireball.net”. You could simply write:


```
RewriteCond %{HTTP_HOST} www.daringfireball.net

```


which is less precise, but still matches “www.daringfireball.net”.
But why be lazy? I’m not going to explain regular expression syntax
here, so [look it up](http://regex.info/) if you don’t understand what’s going on in
the precise version.


The RewriteRule line contains the rule that is applied when the
preceding RewriteCond is met. The rule consists of three parts,
again separated by spaces:

- `(.*)` — a regular expression that is applied against the
request string. The request string is everything that comes
after the slash after the domain name. So if you request the URL
“http://daringfireball.net/archives”, the request string that
gets tested against this pattern is “archives”.
This particular pattern, “`(.*)`”, will match anything. It even
successfully matches “nothing” (a.k.a. the empty string), which
means it will successfully match when you request the URL
“http://www.daringfireball.net/”. Wrapping it in parentheses    allows us to refer to it later on, in the replacement string.
- `http://daringfireball.net/$1` — the replacement pattern. When
the regular expression in the first part matches, this pattern
describes how to rewrite the URL. `$1` is a reference to the
text captured by the sub-pattern within the parentheses; if we
had a pattern with more than one set of parentheses, we could
use `$2`, `$3`, etc. to refer to the additional parenthesized
sub-patterns.
Because the pattern in the first part always matches, this
replacement pattern is always applied.
- `[R=Permanent]` — this is a flag that says that this
redirection is permanent. That means the HTTP redirection goes
out with a 301 code, which tells the client that the redirected
URL is the new permanent home for the resource at the original
URL. You could also write this as `[R=301]`, but I prefer the
wordy syntax.
This flag is optional, but if you leave it off, the redirection
will be marked as temporary — i.e. it’ll go out with an HTTP
302 code. If the redirection is permanent, it’s good practice to
mark it so. Intelligent client software will remember this and
go directly to the new URL instead of going through the
redirection on subsquent requests.


So, in summary:

1. We turn on mod_rewrite processing.
2. We use a RewriteCond condition that applies only when the HTTP_HOST
variable matches “www.daringfireball.net”.
3. When that condition is met, we apply a RewriteRule that takes
the entire request *after* the “www.daringfireball.net/” part,
and redirects it to “http://daringfireball.net/”.


## Redirecting From ‘.com’ to ‘.net’


I can’t quite explain why I decided to use “daringfireball.net”
instead of “daringfireball.com” as the canonical domain for Daring
Fireball. Suffice it to say I have some sort of irrational dislike
for “.com”.


But I realized early on that it was a somewhat common mistake for
people to type “daringfireball.com” instead of “.net”, and the last
thing I wanted was for some asshole domain squatter to register
“daringfireball.com”, so I registered the “.com” version too.


But what to do with it? What I want is for any URL in the form
“daringfireball.com/*anything* to redirect to
“daringfireball.net/*anything*”. Sound familiar?


One solution to this problem would be to configure both domain names
to point to the very same web site, much like how “www.example.com”
and “example.com” almost always point to the same web site for any
given domain. I’m not doing this, however, and, uh, to be honest, I
forget why. If I had to guess, I’d say it’s because I had the vague
notion that someday I might want to serve a different web site from
.com than I do from .net. Anyway, the point is that at my web
hosting account, I have “daringfireball.com” configured as an
entirely separate web site than “daringfireball.net”.


I have a simple one-line .htaccess file in the root directory for
“daringfireball.com”:


```
RedirectMatch permanent (.*) http://daringfireball.net$1

```


This pretty much does the same thing as the first example above, the
one that gets rid of “www” prefixes, except that instead of using
mod_rewrite, it uses the RedirectMatch command from Apache’s
mod_alias module.


(There is absolutely no good reason that I couldn’t use mod_rewrite
for this, too. mod_rewrite is much more powerful than mod_alias’s
RedirectMatch command. My excuse is that I wrote this one first, and
at the time, I didn’t know how to use mod_rewrite. I use mod_rewrite
for the “www” truncation because I have a bunch of other, more
complicated redirect rules in my main .htaccess file, and those
rules require mod_rewrite. It’s also worth noting that mod_alias is
available on more web hosts than mod_rewrite is; but personally I’d
never use a web host who didn’t enable mod_rewrite.)


The syntax for RedirectMatch should be self-explanatory after the
previous explanation regarding RewriteRule. The order of the
components is different, however:

- `permanent` — this specifies that the redirection is permanent
and should use an HTTP 301 result code.
- `(.*)` — regular expression to match the request string.
- `http://daringfireball.net$1` — replacement pattern.


The most interesting difference is that with RedirectMatch, the
request string that the regular expression is tested against
contains the leading “/”. As someone who first learned to use
RedirectMatch and then later switched to mod_rewrite, this has
tripped me up dozens of times.


So the replacement pattern when using mod_rewrite was
`http://daringfireball.net/$1`, but the replacement pattern when
using RedirectMatch is `http://daringfireball.net$1`, because with
RedirectMatch, the text referenced by `$1` already starts with a
slash.


## References

- [Apache mod_rewrite Documentation](http://httpd.apache.org/docs/1.3/mod/mod_rewrite.html)
- [Dave Child’s mod_rewrite Cheat Sheet](http://www.ilovejackdaniels.com/cheat-sheets/mod_rewrite-cheat-sheet/)


---

1. I always thought “web.example.com” would have been a better convention than “www.example.com”. People only called it the “World Wide Web” for about a month or so back in 1994 before we all agreed to just call it the “Web”, but yet we’re stuck with the lame “www” prefix for the rest of our lives. ↩︎



| **Previous:** | [More Aperture Dirt](https://daringfireball.net/2006/05/more_aperture_dirt) |
| **Next:** | [Goal](https://daringfireball.net/2006/05/goal) |


PreviousNext