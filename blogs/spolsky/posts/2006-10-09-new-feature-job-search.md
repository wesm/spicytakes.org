---
title: "New Feature: Job Search"
date: 2006-10-09
url: https://www.joelonsoftware.com/2006/10/09/new-feature-job-search/
word_count: 337
---


When we opened the [job listings](http://jobs.joelonsoftware.com) section I had originally imagined people would just read through the entire list to see if there were any interesting jobs.


In the first month, though, we got about 420 listings; there are 174 live right now: too many to scan. So we added a new search feature:


The best part is that once you set up a search, you can subscribe to it using RSS. I imagine this will be especially interesting if you’re looking for a job outside of Silicon Valley or New York. Right now 50% of the job listings are for jobs within 100 miles of either New York, NY or Palo Alto, CA, but if you’re from, say, Atlanta, and you want to stay there, but would love to hear about new opportunities, run the search and subscribe to the RSS feed and you’ll automatically find out when new jobs are posted in your area.


Intern Noah, shown at right wearing the official Fog Creek intern uniform while singing the Fog Creek anthem, coded the UI for this, but Stanford wanted him back for classes, so I finished implementing the search feature myself over the last two weeks. I got the ZIP Code database from [zipcodeworld.com](http://www.zipcodeworld.com/) and the Canadian postal code data from [zipcodedownload.com](http://www.zipcodedownload.com/) (inexplicably missing H0H 0H0, the Postal code for Santa Claus at the North Pole, but that might be because they couldn’t decide what to put in the longitude column). I got the formula for great circle distances using Ed Williams’ [Aviation Formulary](http://williams.best.vwh.net/avform.htm) and double-checked the results using the incredibly cool [Great Circle Mapper](http://gc.kls2.com/). Of course, when you’re looking for points that are within 20 miles of a given longitude and latitude, it’s not that big a deal to pretend the Earth is flat and just use the Pythagorean Theorem, but of course, then you have to convert degrees to miles and suddenly it’s just as hard to do it the wrong way as it would be to do it the right way.
