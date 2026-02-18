---
title: "Google Lucky Search Scripts for ThisService"
date: 2007-04-27
url: https://daringfireball.net/2007/04/google_lucky_thisservice
slug: google_lucky_thisservice
word_count: 528
---


Let’s say you’re writing an email, and you want to insert a link to, say, the IMDB page for *Raiders of the Lost Ark*. Steps:

1. Switch from email client to web browser.
2. Search for “imdb raiders lost ark” in Google search field.
3. Copy the URL for the page on imdb.com from the search results
list. (You can do this from the contextual menu, or you can use
drag-and-drop.)
4. Switch back to email client.
5. Paste. (Or, if you used drag-and-drop in step #3, drop.)


I do this sort of thing every single day. It seems ripe for some sort of automation, especially because I just know that if I do a Google search for “imdb raiders lost ark”, it’s going to be the first hit in the results. (In fact, you can just Google for “imdb raiders”.)


So, I wrote two scripts for [ThisService](http://wafflesoftware.net/thisservice/) for performing Google Lucky searches via the Services menu. In both scripts, the selected text in the current application is used as the terms for a Google search.


The first one I call “Google Lucky (Insert URL)”; with this script, the selected text in the current application is replaced by the URL of the Google Lucky search. The second one I call “Google Lucky (Open)”; with this script, the result of the Google Lucky search is opened in a new window in your default browser — i.e. for when you actually want to visit the page, not just paste its URL.


I wrote these scripts about three weeks ago, and I’ve been using them almost every day since. I assigned the keyboard shortcut Command-Shift-6 to the “Insert URL” version (mnemonic: “^” means “insert”), and Command-Shift-7 to the “Open” version.


So here are the steps I need to insert the URL for the *Raiders* IMDB page in an email now:

1. Type “imdb raiders” wherever I want the URL to go.
2. Select those words.
3. Type Command-Shift-6.


No switching between apps involved — just type what you’re looking for and hit a shortcut. And because they’re services, they work from any app.


## Source Code to ‘Google Lucky (Insert URL)’


```
#!/usr/bin/env perl
use strict;
use warnings;
use URI::Escape qw(uri_escape_utf8);
use open IO  =>  ":utf8",       # UTF8 by default
                 ":std";        # Apply to STDIN/STDOUT/STDERR

my $query = do { local $/; <> };
$query =~ s/^\s+//g;
$query =~ s/\s+$//g;

my $url = "http://www.google.com/search?&q=" 
           . uri_escape_utf8($query, "^A-Za-z0-9") . "&btnI";
my $headers = `curl -iIs -A "Mozilla/5.0" "$url"`;
$headers =~ m/^Location: (\S+)/im;
print $1;

```


## Source Code to ‘Google Lucky (Open)’


```
#!/usr/bin/env perl
use strict;
use warnings;
use URI::Escape qw(uri_escape_utf8);
use open IO  =>  ":utf8",       # UTF8 by default
                 ":std";        # Apply to STDIN/STDOUT/STDERR

my $query = do { local $/; <> };
$query =~ s/^\s+//g;
$query =~ s/\s+$//g;

my $url = "http://www.google.com/search?&q=" 
            . uri_escape_utf8($query) . "&btnI";
system("/usr/bin/open", $url); 

```


For information on how to turn these scripts into system-wide Services menu items, visit the [ThisService](http://wafflesoftware.net/thisservice/) web site. Keyboard shortcuts, if you want them, are specified in ThisService, not in the scripts themselves.



| **Previous:** | [Interview: Dino Dai Zovi](https://daringfireball.net/2007/04/interview_dino_dai_zovi) |
| **Next:** | [The iPhone’s Funny Price](https://daringfireball.net/2007/05/iphones_funny_price) |


PreviousNext