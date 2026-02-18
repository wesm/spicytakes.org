---
title: "Snow Leopard Compatibility Tweaks for That Thing I Wrote in January About Writing AppleScripts That Dynamically Target Either Safari or WebKit"
date: 2009-09-14
url: https://daringfireball.net/2009/09/snow_leopard_applescript_perl_safari_webkit
slug: snow_leopard_applescript_perl_safari_webkit
word_count: 568
---


Back in January I posted [this piece](http://daringfireball.net/2009/01/applescripts_targetting_safari_or_webkit) about how to write AppleScripts that dynamically target either Safari or WebKit, depending on which one is your default (or which one is currently the active app).


Two parts of it broke in Snow Leopard. I’ve updated the code in the original entry so that everything now works both in Snow Leopard and in Mac OS X 10.5. But both changes are interesting, so I’ll explain them here.


First is a change in AppleScript. In my original version, I had the following line:


```
if _browser is not "Safari" or "WebKit" then

```


This worked fine in Mac OS X 10.5, but when run in Mac OS X 10.6.1 (and
10.6.0), this line generates an error that the string “WebKit” can’t be
made into a boolean. I fixed it by changing this to:


```
if (_browser is not "Safari") and (_browser is not "WebKit") then

```


[**Update, 16 September 2009:** [Thanks to Michael Tsai](http://mjtsai.com/blog/2009/09/15/perl-and-python-on-snow-leopard/), this is a better way to compose the comparison:


```
if _browser is not in {"Safari", "WebKit"} then

```


Tsai also points out that my original syntax, despite running without error on 10.5 and earlier, did not do what I thought it did. The error produced on 10.6 is in fact correct.]


Second is a change to Perl. In my original post, I used the following AppleScript routine to get the name of the user’s default web browser:


```
on GetDefaultWebBrowser()
    set _scpt to "perl -MMac::InternetConfig -le " & ¬
        "'print +(GetICHelper \"http\")[1]'"
    return do shell script _scpt
end GetDefaultWebBrowser

```


This doesn’t work on Snow Leopard. Long story short, the Mac::Carbon bundle of Perl modules (of which Mac::InternetConfig is one) only work in 32-bit mode, and Perl runs in 64-bit mode by default in Snow Leopard.


The key bit there is “by default”. It ends up that Apple has invoked some serious jiggery-pokery for Perl and Python on Snow Leopard such that they both run in 64-bit mode by default, while still offering full backwards compatibility with 32-bit binaries *and with older versions* of Perl and Python. The new man pages [for Perl](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/perl.1.html) and [Python](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/python.1.html) explain the new system in detail, but the gist is that unlike previous versions of Mac OS X, Snow Leopard ships with *several* versions of Perl and Python:1

- Perl 5.10 (64-bit and 32-bit)
- Perl 5.8.9 (32-bit only)
- Python 2.6 (64-bit and 32-bit)
- Python 2.5 (32-bit only)


The defaults — what gets invoked by `/usr/bin/perl` and `/usr/bin/python` — are Perl 5.10 and Python 2.6, both in 64-bit mode. One way to invoke a different version is by setting an environment variable. In the case of our `GetDefaultWebBrowser()` AppleScript routine, we want to invoke Perl 5.10 in 32-bit mode:


```
on GetDefaultWebBrowser()
    set _scpt to "export VERSIONER_PERL_PREFER_32_BIT=yes; " & ¬
        "perl -MMac::InternetConfig -le " & ¬
        "'print +(GetICHelper \"http\")[1]'"
    return do shell script _scpt
end GetDefaultWebBrowser

```


That’s it. The `VERSIONER_PERL_PREFER_32_BIT` environment variable has no effect on older versions of Mac OS X, so we now have a version of this routine that returns the name of the default web browser on both Mac OS X 10.6 and 10.5.


---

1. The [Python man page](http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/python.1.html) states that Python 3.0 is supported as well, but the system doesn’t ship with it. ↩︎



| **Previous:** | [iTunes and Cocoa](https://daringfireball.net/2009/09/itunes_and_cocoa) |
| **Next:** | [How Should Mac Apps Be Distributed?](https://daringfireball.net/2009/09/how_should_mac_apps_be_distributed) |


PreviousNext