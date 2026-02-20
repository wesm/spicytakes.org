---
title: "Visualizing Your Commit History"
date: 2010-01-10
url: https://www.kalzumeus.com/2010/01/10/visualizing-your-commit-history/
slug: visualizing-your-commit-history
word_count: 466
---


I was curious today about whether I tend to work consistently or in bits and spurts, so I decided to check by asking my SVN repository.  First I dumped all my commit messages since I started using SVN (back in October 2007, which was over a year after starting my business — I know, *I know*, I was young and stupid once) into a text file.


Then, I parsed the file with a [quick Ruby one-liner](http://www.pastie.org/772391) to pull out how many commits were made in each month.  My commits when I’m working in Rails can range from a single character to a feature worth of code, but I figure over the years the variation probably averages out.


I then dumped them into Excel 2007 (totally worth the price just for the pretty graphs, although if I was doing this dynamically I’d do it differently) and annotated the graph in Paint.NET.


You can probably tell a lot about me from the shape of this graph:

- I tend to work in spurts when I have inspiration.
- I prefer to ship v1.0 of something and iterate like mad rather than spending more time shipping something more ambitious to start with.
- I sometimes get slammed by the day job and am left with no energy for the business.  (See, e.g., summer of 2008.)


What you can’t tell from the shape of the graph is that, happily, code is not everything in the software business.  Here’s another graph which I’ve truncated to fit the same time scale:

I had another thought: why not visualize code bloat how much valuable code I’ve written over the years.  So I checked out a copy of revision 1 into a temporary directory, then used
[another Ruby script](http://www.pastie.org/772412)
to step through each revision and use
*rake stats*
to count how many lines of code were present.
I really don’t recommend doing this at peak time for the server with your SVN repository on it, incidentally, as it is wasteful as heck.  This script took about half an hour to execute on my slice.  Two ways to improve it: number one, use a local copy rather than using svn+ssh to grab the code.  Number two, instead of
*rake stats*
use a purpose-built code counter like
[CLOC](http://www.pastie.org/772443)
, which doesn’t require loading the entire Rails framework to run.  Loading the entire Rails framework 1,334 times will not make your CPU happy.  Of course, smarter than any of these options would have been figuring out what revisions I wanted to look at a priori, and then just looking at those ~20 revisions rather than deep scanning all 1,334 of them.
Then I
[combined](http://www.pastie.org/772443)
the per-revision LOC counts with the SVN log to graph dates against code size.  Tada!
I guess slow and steady wins the race.