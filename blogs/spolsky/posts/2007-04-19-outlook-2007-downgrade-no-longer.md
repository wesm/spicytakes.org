---
title: "Outlook 2007: downgrade no longer"
date: 2007-04-19
url: https://www.joelonsoftware.com/2007/04/19/outlook-2007-downgrade-no-longer/
word_count: 341
---


Search used to be *horrible *in Outlook. It was so bad that for all intents and purposes, you couldn’t search your old email. Instead, you were encouraged to carefully sort it out into a hierarchy of folders (shudder).


A bunch of third party fixes appeared. My favorite was called Lookout. It provided blazingly fast full text search. Searches took less than a second and really found things. It was built on [DotLucene](http://incubator.apache.org/lucene.net/) (now called Lucene.Net) an excellent open source search engine.


Microsoft did the only thing that made sense: they bought Lookout (the company) and took the product off the market.


People complained.


Microsoft finally put Lookout back up for download, but they sure weren’t happy about it. When Outlook 2007 runs, it checks to see if Lookout was running and disabled it if it was.


Theoretically, Outlook 2007 has search built in, although it’s not really built-in: it’s built on top of [Windows Desktop Search](http://www.microsoft.com/windows/desktopsearch/default.mspx), which comes with Vista and is available as a free download for XP.


The trouble is, Windows Desktop Search is just not that fast. When I “upgraded” from Outlook XP to Outlook 2007, the only new “feature” I noticed was that full text searches started taking about 30 seconds. About 100 times longer than they did with Lookout. And I couldn’t install Lookout: of all the Outlook add-ins in existence, Outlook specifically refused to run Lookout.


The only possible explanation is that someone on the Outlook team is getting paid a bonus for convincing people to switch to [Gmail](http://gmail.google.com/).


The story has a happy ending. Last week Microsoft released a [patch](http://www.microsoft.com/downloads/details.aspx?familyid=C262BCFD-1E09-49B6-9003-C4C47539DF66&displaylang=en) for Outlook 2007 which fixed the problem for me (I have a lot of big PST files, which, I’m told, is why search was so slow for me). Now I can search old email quickly enough that I don’t forget what I was searching for by the time the results come up. It’s not quite as fast as Lookout used to be, but it’s a big improvement and makes Outlook less of a downgrade.
