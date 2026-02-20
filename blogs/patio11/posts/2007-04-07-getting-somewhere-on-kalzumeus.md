---
title: "Getting Somewhere On Kalzumeus"
date: 2007-04-07
url: https://www.kalzumeus.com/2007/04/07/getting-somewhere-on-kalzumeus/
slug: getting-somewhere-on-kalzumeus
word_count: 627
---


I finally got some time today to sit down and have a coding session.  The program can’t be more than, oh, 5% of the way ready yet, but I’m feeling that I’m starting to get my head around most of the core Rails concepts.  Much more code is actually sticking to the screen and its been a matter of *hours* since I did a rm -rf * on the project directory.


In terms of complexity, my preliminary estimate is that Kalzumeus will require about 15 classes.  This is actually roughly how many there are in Bingo Card Creator.  I have noticed so far that I’m spending much, much less time on nuts&bolts programming than I typically do in Java, and much, much more time on chasing down misnamed variables, typos, and the like.  Partially thats because Eclipse does autocompletion for me in Java so I remember that I called that string nickname instead of nick.  Luckily, the development cycle on Rails is fast enough that I only lose about 15 seconds when that happens — annoying as heck to see the “Ugh, you fail!” error screen, though.


By the way, after spending many hours fighting with a series of IDEs, I eventually went with Netbeans.  My first real work in Java was done in Netbeans, before I switched over to Eclipse a few years ago.  It is a much, much more capable IDE for Rails, so I’m happy to be back.  I’ve supplemented it with a few Direct Access macros to save myself some of Rail’s verbosity, and I hope to publish those later (e.g. typing in ctcs gets *t.column “”, :string* with the cursor positioned right between the quotation marks, ready for you to input a column name).  I do generally like the idea of prioritizing maintenance programmer brainsweat (which Java and Ruby optimize for — java.util.JokeFactory.createNewJoke(camelCasedVerboseIdentifierNamesHelpComprehension) ) over creation programmer finger time (which Perl optimizes for:  $_.=$&).


Kalzumeus is similar to Bingo Card Creator in terms of code complexity, i.e. “not very”.  There will probably be exactly one class which will require anything close to cleverness while coding.  I don’t even think I’ll have to worry about thread safety issues, which is both a relief and a letdown at the same time.  I actually have a perverse affection for concurrency issues.  They’re one of the only places where I’m a halfway decent programmer.


I also have found a way to save myself a few hundred dollars for launch: cut out the UI designer!  oswd.org came through again with a beautiful, configurable design called [Multiflex3 ](http://www.oswd.org/design/preview/id/3626)which has an associated WordPress theme.  I anticipate that after I actually have the application written I can make it look quite presentable in Multiflex in about a day or two, and then add a visually coherent Wordpress blog with another day.  If Kalzumeus takes off then I can always hire myself a designer later to make it look prettier and more unique.


I had a flight of fancy the other day: I will have sufficient savings in August, when my current contract ends, to pay for 6 months of living expenses while subsidized by Bingo Card Creator’s current monthly sales.  If I return to the US at that point, I will get a distribution from the Japanese pension fund, which would extend that to about a year’s worth of expenses.  That would allow me to work full time on the uISV… the downside is that if I failed I would be poor, unemployed, and on the wrong side of the ocean for finding convenient work opportunities.  It was a quite attractive flight of fancy for a few minutes, and it will make a good Plan C or so.  I’m still looking for a more conventional job, though.  For the moment.
