---
title: "Bleg For Perl Help"
date: 2006-10-19
url: https://www.kalzumeus.com/2006/10/19/bleg-for-perl-help/
slug: bleg-for-perl-help
word_count: 173
---


I am not an accomplished Perl hacker and something has been frustrating me at work for the last several weeks.  If you know of an easy way to solve this, I will be forever in your debt:


We are using Perl to run a HTTP server (HTTP::Daemon, incidentally, works like a charm) to receive information from a rich client application.  The client has to upload text files via HTTP post.  Everything is A-OK on the client’s side of things, but I have no clue how to go about extracting the uploaded text file from the HTTP request on the server side of things.  My experiments have been a bunch of failures, I can’t seem to find any CPAN Module which will do this cleanly, and there are other deliverables up in the air which are getting held up by the server being only 98% complete (that last pesky 2% is critical to testing the client application, sadly).  Does anyone have any suggestions?  Perl’s documentation is, well…  up to its usual standard of lucidity.
