---
title: "Interarchy Interview: Peter N Lewis and Matthew Drayton"
date: 2007-02-01
url: https://daringfireball.net/2007/02/interarchy_interview
slug: interarchy_interview
word_count: 1335
---


It’s not every day that one of the most popular indie Mac apps in history changes hands, but that’s what happened today, when Matthew Drayton and his new company, [Nolobe](http://nolobe.com/), acquired the rights to Interarchy from Peter N Lewis’s [Stairways Software](http://www.stairways.com/main/).


Two years ago I called [Interarchy 7 one of my favorite apps of the year](http://daringfireball.net/2005/02/apps_of_the_year_2004); the [current version](http://nolobe.com/interarchy/) (8.5, released earlier today) remains my file transfer app of choice. At the time the [first version of Anarchie](http://www.stairways.com/press/1993-12-07) was released in 1993, most commercial Mac software was still sold in boxes through retail channels. Peter was a pioneer of the modern web-based business and distribution model for indie Mac developers (including helping to found [Kagi](http://kagi.com/), the popular software payment processor).


---


**Gruber:**
  As the [PR announcing this deal says](http://www.stairways.com/press/2007-02-01), this more or less amounts
  to an employee buyout of the product. I take it we can presume this
  is an amicable agreement?


**Lewis:**
  The agreement is entirely amicable, we see it as a great way to
  ensure Interarchy’s future.


**Gruber:**
  Peter, when did you start writing the first version of Anarchie?


**Lewis:**
  I started writing Anarchie in 1993 as an archie client (archie was
  a very primitive search engine for finding files available on
  public FTP archives) coupled together with an FTP file downloading
  engine to allow the user to perform a search and then directly
  download the file.


At the time I was working full time for supporting a small
  University department with 20 Macs, and writing Mac Internet
  applications after hours (I even had to pay them for the computer
  usage!).


**Gruber:**
  Why give it up now?


**Lewis:**
  I’ve enjoyed working on Interarchy, but I have been doing it for a
  dozen years now, and it is time to try something else.  The
  problem with having a successful program like Interarchy is it
  essentially stops you from working on anything else that doesn’t
  succeed as well as it does.


Matthew has been an excellent employee, and I have had a great
  time working with him, but this gives him a chance to go out on
  his own, which is something he would have needed to do sooner or
  later anyway.


As for what that next thing might be, I have no specific plans at
  the moment.  Our third child is due any day now, so that will keep
  me busy for a while and then I’ll see what I might like to do
  next. Perhaps a revision of [Keyboard Maestro](http://www.keyboardmaestro.com/) or a Mac OS X version
  of [Greebles](http://www.infam.ch/greebles/), or perhaps something entirely different.


**Gruber:**
  Good to know that Stairways Software will continue.


A decade ago, you really had a slew of small utilities under
  active development. Most of the individual networking utilities
  were folded together under the Interarchy umbrella, but things
  like Obi Wan simply faded away.


I’m not asking you for specific ideas on what you might do, but
  do you have a general sense of whether it’d be one big new
  thing, or a handful of smaller projects?


**Lewis:**
  Actually, I still use ObiWan (now called Wanobi) and ThufirCalc,
  but many of our early programs served to bring Unix Internet
  facilities to the Mac, but many of those facilities have since
  faded away and our programs with them.


Currently I doubt I’ll write a new big program, at least not in
  the short term.  I’d like to write a game, but they generally take
  a large group of people these days.  I might build a few web sites
  to try something a bit different.


**Gruber:**
  Matthew, when did you start working for Stairways on Interarchy?


**Drayton:**
  I started working for Stairways at the beginning of 2001; 19th of
  March to be precise.  I’d just finished my Computer Science degree
  and desperately wanted to write Mac software.  Stairways was the
  only Australian company I knew of that developed Mac software so I
  sent them an email.  A couple of days later I had a job.


**Gruber:**
  Pretty cool. Are you doing Nolobe on your own?


**Drayton:**
  I’ve enlisted the help of my brother David.  We have wanted to work
  together for a long time and now we have the opportunity to do so.


David’s current situation is not dissimilar to mine back in 2001. 
  He has just finished a Computer Science degree and wants to write
  Mac software.


**Gruber:**
  Interarchy is pretty unique, architecturally. My understanding
  is that it’s still written mostly (or completely) in Pascal. Is
  that right?


**Drayton:**
  Yes.  There are a few C and Objective-C files but the rest is Pascal.


**Gruber:**
  There certainly aren’t many modern Mac apps left that are
  written primarily in Pascal. For one thing, support for Pascal isn’t
  provided by default in Xcode. How much work is it just to maintain a
  working tool chain?


**Lewis:**
  It is actually not too bad.  There are a group of us who
  maintain the Pascal “Universal Interfaces” which are just
  translations from the C headers.  There are GNU Pascal people who
  work at maintaining GNU Pascal, so we don’t have to worry about
  that, although early on we worked with them to minimize the
  inter-operability problems when converting from CodeWarrior Pascal.


Now that it is all set up, it works very nicely.  We work in BBEdit
  and hit a key to cause a make or compile, which builds the program,
  potentially including all the documentation, widgets, actions,
  command line tools, disk images, etc.  BBEdit supports [ctags](http://ctags.sourceforge.net/), so
  there is good syntax coloring and quick navigation.  It also
  supports subversion, so we can use all of those facilities.
  Debugging is a bit limited, but we use lots of assertions which
  detect most errors at their source, cutting down debugging time
  enormously.


**Gruber:**
  I can see two sides to taking over the reins of an app as
  long-standing and popular as Interarchy. On the one hand, it gives
  you the opportunity to start your own company with an enormous
  existing customer base.


But on the other hand, existing customers have, shall we say, strong
  feelings about how Interarchy should look and work. How much do you
  feel bound to Interarchy’s tradition?


**Drayton:**
  I have been working on Interarchy for a long time; nearly
  six years.  I like to think that I have played a big part in
  creating this tradition.  It is something that I am very proud of
  and hope to continue with Nolobe.


**Gruber:**
  One of the things I like best about Interarchy is that it works so
  much like the Finder, e.g. its list views offer hierarchy
  disclosure triangles. And in other ways — and I mean this as a
  deep compliment — it works like the Finder *used* to, getting
  certain things right that the OS X Finder never has. For example,
  when I open a folder into its own window in Interarchy, the window
  opens in the same size and location as the last time I opened that
  folder.


Have either of you ever considered working on a Finder alternative?
  Something that leverages the UI architecture of Interarchy but for
  local file browsing — more or less a competitor to Path Finder?


**Lewis:**
  Not really, no.  Going head to head with Apple on what
  amounts to a straight user interface does not strike me as a good
  idea.  Who knows when Apple might decide it is time for a major
  change in direction for the Finder, so after a lot of work it would
  be very easy to be left behind in the dust if Apple ever got
  serious.  It would not surprise me to see a big change in the Finder
  experience for 10.5.


**Gruber:**
  Well, congratulations. I’m sure this has been an exciting
  day for both of you.


Matthew, if you accept as many of my feature requests as
  Peter did, I’m sure Nolobe is going to do just fine.


**Lewis:**
  Thanks John!


**Drayton:**
  Thank you.



| **Previous:** | [Sometimes I Wonder Whether Rob Enderle Is Just Pulling Our Legs](https://daringfireball.net/2007/01/enderle_leg_pulling) |
| **Next:** | [Lies, Damned Lies, and Bill Gates](https://daringfireball.net/2007/02/lies_damned_lies_and_bill_gates) |


PreviousNext