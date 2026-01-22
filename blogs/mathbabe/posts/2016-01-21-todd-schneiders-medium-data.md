---
title: "Todd Schneider’s “medium data”"
date: 2016-01-21
url: https://mathbabe.org/2016/01/21/todd-schneiders-medium-data/
word_count: 458
---


Last night I had the pleasure of going to [a Meetup](http://www.meetup.com/nyhackr/events/227298221/) given by [Todd Schneider](http://toddwschneider.com/), who wrote [this informative and fun blogpost](http://toddwschneider.com/posts/analyzing-1-1-billion-nyc-taxi-and-uber-trips-with-a-vengeance/) about analyzing taxi and Uber data.


You should read his post; among other things it will tell you how long it takes to get to the airport from any NYC neighborhood by the time of day (on weekdays). This corroborates my fear of the dreader post-3pm flight.


His Meetup was also cool, and in particular he posted [a bunch of his code on github](https://github.com/toddwschneider/nyc-taxi-data), and explained what he’d done as well.


For example, the raw data was more than half the size of his personal computer’s storage, so he used an external hard drive to hold the raw data and convert it to a SQL database on his personal computer for later use (he used [PostgreSQL](http://www.postgresql.org/)).


Also, in order to load various types of data into R, (which he uses instead of python but I forgive him because he’s so smart about it), he reduced the granularity of the geocoded events, and worked with them via the database as weights on square blocks of NYC (I think about 10 meters by 10 meters) before turning them into graphics. So if he wanted to map “taxicab pickups”, he first split the goegraphic area into little boxes, then counted how many pickups were in each box, then graphed that result instead. It reduced the number of rows of data by a factor larger than 10.


Todd calls this “medium data” because, after some amount of work, you can do it on a personal computer. I dig it.


Todd also gave a bunch of advice for people to follow if they want to do neat data analysis that gets lots of attention (his taxicab/ Uber post got a million hits from Reddit I believe). It was really useful and good advice, the most important of which was, if you’re not interested in this topic, nobody else will be either.


One interesting piece of analysis Todd showed us, which I can’t seem to find on his blog, was a picture of overall rides in taxis and Ubers, which seemed to indicate that Uber is taking over market share from taxis. That’s not so surprising, but it actually seemed to imply that the overall number of rides hasn’t changed much; it’s been a zero-sum game.


The reason this is interesting is that de Blasio’s contention has been that Uber is increasing traffic. But the above seems to imply that Uber doesn’t increase traffic (if “the number of rides” is a good proxy for traffic); rather, it’s taking business away from medallion cabs. Not a final analysis by any stretch but intriguing.


Finally, [Todd more recently analyzed Citibike rides](http://toddwschneider.com/posts/a-tale-of-twenty-two-million-citi-bikes-analyzing-the-nyc-bike-share-system/), take a look!
