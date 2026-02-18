---
title: "BBEdit CSS Syntax Checker 1.0"
date: 2005-09-06
url: https://daringfireball.net/2005/09/bbedit_css_checker
slug: bbedit_css_checker
word_count: 303
---


If you work on CSS using either of Bare Bones Software’s text editors,
you might be interested in my latest project: [CSS syntax checking
scripts for BBEdit and TextWrangler](http://daringfireball.net/projects/csschecker/). They’re a combination of
Perl and AppleScript that allows you to syntax-check CSS files using
the W3C’s [CSS Validation Service](http://jigsaw.w3.org/css-validator/). Errors and warnings from the
validation service are displayed in a results browser, very similar in
effect to BBEdit’s built-in HTML syntax checker.


These scripts require Mac OS X 10.4 or later, and have been tested
against BBEdit 8.2.3 and TextWrangler 2.1.


I’ve had the idea for this for a couple of years, but I put off
hacking it together because I have a strong aversion to
[screen-scraping](http://www.catb.org/~esr/jargon/html/S/screen-scraping.html). The W3C CSS Validation Service is a wonderful tool,
but, alas, it has no proper API for calling it as a web service.


What these scripts do is take the content of your frontmost
window and pass them to the W3C validator’s regular CGI interface, the
results of which come back as HTML. The Perl component parses this HTML
and reformats any errors and warnings so the AppleScript component can
display the results browser in BBEdit/TextWrangler.


The problems with screen-scraping are obvious: if the W3C changes the
HTML format of the validator’s output, my parser may break. Plus, even
if they don’t change it, parsing the results as they stand is an
inexact science. (Believe it or not, their output isn’t always
well-formed HTML.) A real web-services API for the validator would be
welcome.


That said, it seems to work pretty well.


My thanks to everyone who helped test this, particularly
[Nat Irons](http://bumppo.net/) and [Kevin C. Smith](http://centricle.com/).



| **Previous:** | [Google Is an Advertising Company](https://daringfireball.net/2005/08/google_ad_company) |
| **Next:** | [The iTunes 5 Announcement From the Perspective of an Anthropomorphized Brushed Metal User Interface Theme](https://daringfireball.net/2005/09/anthropomorphized) |


PreviousNext