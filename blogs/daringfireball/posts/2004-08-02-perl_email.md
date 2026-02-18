---
title: "The Perl Email Project"
date: 2004-08-02
url: https://daringfireball.net/2004/08/perl_email
slug: perl_email
word_count: 319
---


Given that (a) Perl is optimized for text processing and [Unix-y
administrative tasks](http://www.amazon.com/exec/obidos/asin/1565926099/daringfirebal-20); and (b) the [mbox](http://en.wikipedia.org/wiki/Mbox) email storage format
is both plain text and deeply rooted in Unix culture — you’d think
Perl would be a terrific scripting language for mbox parsing.


But I’ve always rather disliked the entire `Mail::` hierarchy of
CPAN modules, several of which provide ways to parse mbox files
(along with other mail storage formats). They reek of
over-engineering — complicated APIs and slow performance. One of
Larry Wall’s guiding precepts for Perl is, “Easy things should be
easy, and hard things should be possible.” The modules in the
`Mail::` hierarchy fail the “easy things should be easy” test.


In response, Simon Cozens and several collaborators have spearheaded
the Perl Email Project, the product of which is the relatively new
`Email::` hierarchy of CPAN modules. These modules are simple, fast,
and easy to use. I replaced `Mail::MboxParser` with `Email::Folder`
in a script I wrote to process mbox files full of T-shirt orders,
and it ran over 10 times faster. Even better, I found the syntax
more intuitive — more, well, *Perlish*.


For example, in my original script using `Mail::MboxParser`, given a
message object `$msg`, to get the body of `$msg` as a string, I
needed to do this:


```
my $body = $msg->body($msg->find_body);
my $text = $body->as_string;

```


Whereas using `Email::Folder` (and `Email::Simple`), I can just
write:


```
my $text = $msg->body;

```


A few weeks ago Cozens wrote an article for Perl.com, “[The
Evolution of Perl Email Handling](http://www.perl.com/lpt/a/2004/06/10/email.html)”, wherein he makes a
compelling case for the new `Email::` modules while providing a good
introduction to their usage. Highly recommended for anyone who uses
Perl to read email files.



| **Previous:** | [Magic 8-Ball Answers Your Questions Regarding RealNetworks’ Harmony](https://daringfireball.net/2004/07/magic_8-ball_harmony) |
| **Next:** | [The Art of the Parlay, Or: How I Learned to Stop Worrying About Platform Licensing and Market Share](https://daringfireball.net/2004/08/parlay) |


PreviousNext