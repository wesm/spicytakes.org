---
title: "JavaScript Bookmarklet Builder"
date: 2007-03-19
url: https://daringfireball.net/2007/03/javascript_bookmarklet_builder
slug: javascript_bookmarklet_builder
word_count: 866
---


[**Update 27 January 2014:** I’ve fixed a small bug in the below script. I’m also now hosting a copy of it [on Gist](https://gist.github.com/gruber/8658935).]


So a [bookmarklet](http://en.wikipedia.org/wiki/Bookmarklet) is a little JavaScript script that’s intended to be run from a web browser’s bookmarks bar or menu. The reason they work as “bookmarks” is that the JavaScript source code is crammed into the form of a URL using the “javascript:” scheme.


Developing or modifying bookmarklets can be irritating, to say the least, because of this requirement that the JavaScript code be in the form of a URL.


For example, here’s a simple bit of JavaScript that (1) gets the title of the current web page; (2) shows an alert dialog with the title in all caps with an exclamation mark at the end.


```
var str = document.title;
alert(str.toUpperCase() + "!");

```


Pretty simple. But that same script, in the form of a bookmarklet, looks like this (all on one line):


```
javascript:var%20str%20=%20document.title;
alert(str.toUpperCase()%20+%20%22!%22);

```


In addition to removing line breaks, spaces need to be escaped (`%20`), and it’s a good idea to escape single- and double-quotes, too.1 You also need to escape non-ASCII characters.


So the problem developing bookmarklets is this: You want to write and edit normal JavaScript code, but you need to publish hard-to-read URLs.


My solution: A “Make Bookmarklet” Perl script that I run as a BBEdit filter that (1) takes as input a file containing JavaScript source code; (2) creates a bookmarklet URL from that source code; and then (3) places the bookmarklet code in a comment at the first line of your JavaScript source, but otherwise preserves your original script.


So, for example, given this trivial JavaScript:


```
var str = document.title;
alert(str);

```


My “Make Bookmarklet” script will return:


```
// javascript:var%20str%20=%20document.title;alert(str);
var str = document.title;
alert(str);

```


If you run it again, with a comment on the first line that begins with “`// javascript:`”, it will replace that comment rather than add another one. The idea is that you can keep running the “Make Bookmarklet” script each time you make a change to your JavaScript code.


And, as an added bonus, the bookmarklet URL string is *also* placed on the clipboard, which means you can run the script, and then immediately switch to your browser and paste it into the browser’s bookmarks editor.


## Source Code to ‘Make Bookmarklet’ Script


```
#!/usr/bin/env perl
#
# http://daringfireball.net/2007/03/javascript_bookmarklet_builder

use strict;
use warnings;
use URI::Escape qw(uri_escape_utf8);
use open  IO  => ":utf8",       # UTF8 by default
          ":std";               # Apply to STDIN/STDOUT/STDERR

my $source_code = do { local $/; <> };

# Zap the first line if there's already a bookmarklet comment:
$source_code =~ s{^// ?javascript:.+\n}{};

my $bookmarklet = $source_code;
for ($bookmarklet) {
    s{(^\s*//.+\n)}{}gm;        # Kill commented lines
    s{^\s*/\*.+?\*/\n?}{}gms;   # Kill block comments
    s{\t}{ }gm;                 # Tabs to spaces
    s{[ ]{2,}}{ }gm;            # Space runs to one space
    s{^\s+}{}gm;                # Kill line-leading whitespace
    s{\s+$}{}gm;                # Kill line-ending whitespace
    s{\n}{}gm;                  # Kill newlines
}

# Escape single- and double-quotes, spaces, control chars, unicode:
$bookmarklet = "javascript:" .
    uri_escape_utf8($bookmarklet, qq(%'" \x00-\x1f\x7f-\xff));

print "// $bookmarklet\n" . $source_code;

# Put bookmarklet on clipboard:
my $fh;
open($fh, '|-', '/usr/bin/pbcopy')
    or die "Failed to open pipe to /usr/bin/pbcopy - $!";
print $fh $bookmarklet
    or die "Failed to write to pbcopy pipe - $!";
close($fh)
    or die "Failed to close pipe to pbcopy - $!";

```


## Instructions


Here’s how to use it with [BBEdit](http://barebones.com/support/bbedit/) or [TextWrangler](http://barebones.com/support/textwrangler/). If you use some other editor, there’s probably some easy way to use shell script filters with your editor, too — there’s nothing BBEdit-specific in this script. (It ought to work as a service via [Automator](http://arstechnica.com/apple/2011/03/howto-build-mac-os-x-services-with-automator-and-shell-scripting/) or [ThisService](http://wafflesoftware.net/thisservice/), too, but I haven’t tried that.)

1. Copy the above Perl script and paste it into a new text window.
2. Save it in your *~/Library/Application
Support/BBEdit/Text Filters/* folder.   (Substitute
“TextWrangler” for “BBEdit” if necessary.) I named mine
“Make Bookmarklet”, but you can name it whatever you want.
3. When run in a document window with a range of selected
text, the selection will be passed as input and replaced with
the output. If no text is selected, the entire contents of
the window will be used as input and replaced with the
output. With this script, it’s generally easiest to run it
with no selection.


## Warning and Feedback


This script has worked well for me and many others since I first published it in 2007. But if it eats your source code, Undo is your friend. If you spot anything wrong or wish to suggest improvements, please do let me know, or [fork it on Gist](https://gist.github.com/gruber/8658935).


---

1. It’s unclear to me what characters *must* be escaped in a bookmarklet URL. Some sources suggest that other punctuation characters, such as brackets and semicolons, ought to be escaped, too, but I can see no practical reason to do so. If you want to be really conservative and escape just about everything, change this line:
`uri_escape_utf8($bookmarklet, qq(%'" \x00-\x1f\x7f-\xff));`
to:
`uri_escape_utf8($bookmarklet);`
Personally, I prefer to keep the bookmarklet URL itself as readable as possible. ↩︎



| **Previous:** | [Like a Sponge](https://daringfireball.net/2007/03/like_a_sponge) |
| **Next:** | [LogoMaid Rips Off Dan Cederholm’s SimpleBits Logo, and Then Things Get Weird](https://daringfireball.net/2007/03/logomaid_rip_off) |


PreviousNext