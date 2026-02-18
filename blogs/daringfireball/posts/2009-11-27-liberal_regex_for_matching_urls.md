---
title: "A Liberal, Accurate Regex Pattern for Matching URLs"
date: 2009-11-27
url: https://daringfireball.net/2009/11/liberal_regex_for_matching_urls
slug: liberal_regex_for_matching_urls
word_count: 357
---


[**Update, 27 July 2010:** This article has been superseded by [this one](http://daringfireball.net/2010/07/improved_regex_for_matching_urls), which presents a superior solution to the same problem.]


A common programming problem: identify the URLs in an arbitrary string of text, where by “arbitrary” let’s agree we mean something unstructured such as an email message or a tweet. I offer a solution, in the form of the following regex pattern:


```
\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))

```


This pattern should work in most modern regex implementations. I can vouch for it working in Perl, Ruby, and with the PCRE regex library (which in turn means it works in PHP and BBEdit, both of which use PCRE).


This pattern attempts to be practical. It makes no attempt to parse URLs according to any official specification. It isn’t limited to predefined URL protocols. It should be clever about things like parentheses and trailing punctuation. For example, it will correctly match the URL in the following example lines:


```
http://foo.com/blah_blah
http://foo.com/blah_blah/
(Something like http://foo.com/blah_blah)
http://foo.com/blah_blah_(wikipedia)
(Something like http://foo.com/blah_blah_(wikipedia))
http://foo.com/blah_blah.
http://foo.com/blah_blah/.
<http://foo.com/blah_blah>
<http://foo.com/blah_blah/>
http://foo.com/blah_blah,
http://www.example.com/wpstyle/?p=364.
http://✪df.ws/123
rdar://1234
rdar:/1234
http://userid:[email protected]:8080
http://[email protected]
http://[email protected]:8080
http://userid:[email protected]
http://example.com:8080 x-yojimbo-item://6303E4C1-xxxx-45A6-AB9D-3A908F59AE0E
message://%[email protected]%3e
http://➡.ws/䨹
www.➡.ws/䨹
<tag>http://example.com</tag>
Just a www.example.com link.

```


It attempts to be particularly clever with regard to parentheses, which, in my experience, only ever seem to occur in the wild in Wikipedia URLs, and which many URL matching patterns seem to botch. The pattern looks for a single pair of balanced parentheses within the URL, which is how it correctly omits the trailing parenthesis in the following line:


```
(Something like http://foo.com/blah_blah)

```


The pattern is also liberal about Unicode glyphs within the URL, which allows it, among other things, to match IDN domain names, such as the ✪df.ws domain I registered for the custom URL shortener I use for the [Daring Fireball Twitter feed](http://twitter.com/daringfireball).


Suggestions and improvements are welcome, including just sending me example input where the current pattern fails.


**Update, 28 Nov 2009**: [Alan Storm has a great follow-up piece.](http://daringfireball.net/linked/2009/11/28/storm-regex)



| **Previous:** | [iPhone Web Apps as an Alternative to the App Store](https://daringfireball.net/2009/11/iphone_web_apps_alternative) |
| **Next:** | [Who Do You Believe, Randall Stross or Your Own Lying Eyes?](https://daringfireball.net/2009/12/stross_lying_eyes) |


PreviousNext