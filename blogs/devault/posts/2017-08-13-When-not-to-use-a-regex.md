---
title: "When not to use a regex"
date: 2017-08-13
url: https://drewdevault.com/2017/08/13/When-not-to-use-a-regex.html
slug: When-not-to-use-a-regex
word_count: 329
---

The other day, I saw  [Learn regex the easy
way](https://github.com/zeeshanu/learn-regex) . This is a great resource, but I
felt the need to pen a post explaining that regexes are usually not the right
approach.

Let’s do a little exercise. I googled “URL regex” and here’s the first Stack
Overflow result:

```
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)
```

[source](https://stackoverflow.com/a/3809435/1191610)

This is a bad regex. Here are some valid URLs that this regex fails to match:

* [http://x.org](http://x.org)
* [http://nic.science](http://nic.science)
* http://名がドメイン.com (warning: this is a parked domain)
* [http://example.org/url,with,commas](http://example.org/url,with,commas)
* [https://en.wikipedia.org/wiki/Harry_Potter_(film_series)](https://en.wikipedia.org/wiki/Harry_Potter_(film_series))
* http://127.0.0.1
* http://[::1] (ipv6 loopback)

Here are some invalid URLs the regex is fine with:

* [http://exam..ple.org](http://exam..ple.org)
* [http://--example.org](http://--example.org)

This answer has been revised 9 times on Stack Overflow, and this is the best
they could come up with. Go back and read the regex. Can you tell where each of
these bugs are? How long did it take you? If you received a bug report in your
application because one of these URLs was handled incorrectly, do you understand
this regex well enough to fix it? If your application has a URL regex, go find
it and see how it fares with these tests.

Complicated regexes are opaque, unmaintainable, and often wrong. The correct
approach to validating a URL is as follows:

```
from urllib.parse import urlparse

def is_url_valid(url):
    try:
        urlparse(url)
        return True
    except:
        return False
```

A regex is useful for validating  *simple*  patterns and for  *finding*  patterns in
text. For anything beyond that it’s almost certainly a terrible choice. Say you
want to…

**validate an email address** : try to send an email to it!

**validate password strength requirements** : estimate the complexity with
 [zxcvbn](https://github.com/dropbox/zxcvbn) !

**validate a date** : use your standard library!
 [datetime.datetime.strptime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.strptime)

**validate a credit card number** : run the  [Luhn
algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)  on it!

**validate a social security number** : alright, use a regex. But don’t expect
the number to be assigned to someone until you ask the Social Security
Administration about it!

Get the picture?
