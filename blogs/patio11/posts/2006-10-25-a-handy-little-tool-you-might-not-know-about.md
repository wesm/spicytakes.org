---
title: "A Handy Little Tool You Might Not Know About"
date: 2006-10-25
url: https://www.kalzumeus.com/2006/10/26/a-handy-little-tool-you-might-not-know-about/
slug: a-handy-little-tool-you-might-not-know-about
word_count: 546
---


I never touched Unix in my life before going to college, but it was the development environment of choice for most of the upper-level coursework at school (lower level was Windows + Emacs… not a combination I would recommend given the excellent Java IDEs which exist right now, incidentally), and so I’ve gotten very used to having my good friends ls, grep, wc, and gawk available on my machine.  I use [Cygwin ](http://www.cygwin.com)to have them available on my Windows box, because while Linux is a lovely operating system in many ways I rather enjoy having iTunes and games available.


Anyhow, I had a task yesterday: I have a local copy of my website.  All of the pages have a very similar structure because the navigational elements are embedded in static HTML.  However, this didn’t use an official templating feature because NVU doesn’t support any, which means updating the navigational elements means updating approximately twenty pages by hand.  There was one particular snippet of HTML that I wanted to change to another, globally.


Normally, I would do this in a gawk script (you can do just about anything in a gawk script), but it gets a little messy:


> BEGIN {
> startTag = “<a href=\”guarantee.htm\”>Money-back Guarantee”
> replacementTag = “<a href=\”guarantee.htm\”><img src=\”images/money-back-guarantee.htm\” alt=\”Money-back Guarantee\” \>”
> }
> ($0 !~ startTag { print $0}
> ($0 ~ startTag) {
> gsub(startTag, replacementTag, $0);
> print $0;
> }


Anyhow, that is the way to do it in gawk.  Define your regular expression to search for, print out every line that doesn’t match it and do some surgery on the ones that do.  Note that you’ll have to run this on every file in your web directory, with the easiest way probably being a bash script, and output the results.  However, if you output to the file directly it will generally end up empty for reasons that I have never bothered really understanding, so you probably want to have another quick shell script to output it to a temp file and then copy over the original.  Something like, oh,


> for file in *.htm do
>   gawk -f myscript $file > temp.htm
>   mv temp.htm $file
> done


But that is two scripts, and two scripts is too complicated!  Enter sed, a handy little stream processing utility.  Sed is perfect when you just need to do a quick substitution for a regular express:


sed -e “/myregularexpression/myreplacement/”


There, you’re done.  Or in my case, you have to finangle the regular expression into a string, which involves quite a bit of escape characters, but it still only took about 30 seconds.  This saves about half of your typing time versus doing it in gawk, and you can’t accidentally bork the matching logic (something which is easy to do in gawk — forget the ! before the ~, or execute the (string ~ regex) block before the (string !~ regex) block, and you’re screwed.


Of course, you could always write it in Perl.  That would probably take a single line and look like your cat had just tap danced across your keyboard.  But if you want a simple, intuitive way to do fairly powerful data processing, you’ll see sed is your man…  err, I mean, you should see man sed.
