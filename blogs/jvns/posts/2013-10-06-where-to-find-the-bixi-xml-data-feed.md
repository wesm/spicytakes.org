---
title: "Where to find bike sharing systems' data feeds"
date: 2013-10-06
url: https://jvns.ca/blog/2013/10/06/where-to-find-the-bixi-xml-data-feed/
slug: where-to-find-the-bixi-xml-data-feed
word_count: 188
---


Bike sharing systems by [Bixi](http://publicbikesystem.com) publish
information about how many bikes and docks are available at each station
about every minute, as XML or JSON.


People sometimes ask me where the feed is for this data, as it’s not
always advertised on their website. Here are the feeds for all the
systems so far:


XML feeds:

- Toronto - [http://toronto.bixi.com/data/bikeStations.xml](http://toronto.bixi.com/data/bikeStations.xml)
- Montreal - [http://montreal.bixi.com/data/bikeStations.xml](http://montreal.bixi.com/data/bikeStations.xml)
- Ottawa - [http://capital.bixi.com/data/bikeStations.xml](http://capital.bixi.com/data/bikeStations.xml)
- Washington D.C. Capital Bike Share - [http://www.capitalbikeshare.com/data/stations/bikeStations.xml](http://www.capitalbikeshare.com/data/stations/bikeStations.xml)
- Minneapolis Nice Ride - [http://secure.niceridemn.org/data2/bikeStations.xml](http://secure.niceridemn.org/data2/bikeStations.xml)
- Boston Hubway - [http://thehubway.com/data/stations/bikeStations.xml](http://thehubway.com/data/stations/bikeStations.xml)
- London Barclay’s Cycle Hire - [http://www.tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml](http://www.tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml)


JSON feeds:

- New York Citi Bike - [http://citibikenyc.com/stations/json](http://citibikenyc.com/stations/json)
- Melbourne Bike Share-  [http://www.melbournebikeshare.com.au/stationmap/data](http://www.melbournebikeshare.com.au/stationmap/data)
- Bay Area Bike Share - [http://bayareabikeshare.com/stations/json](http://bayareabikeshare.com/stations/json)
- Chicago Divvy Bikes - [http://divvybikes.com/stations/json](http://divvybikes.com/stations/json)
- Chattanooga - [http://www.bikechattanooga.com/stations/json](http://www.bikechattanooga.com/stations/json)
- Columbus CoGo Bike Share - [http://cogobikeshare.com/stations/json](http://cogobikeshare.com/stations/json)
- Aspen WE-cycle - [https://www.we-cycle.org/pbsc/stations.php](https://www.we-cycle.org/pbsc/stations.php)


Other:


Washington State University’s [Green Bike](http://www.greenbike.wsu.edu/) system
has an unfortunate situation where the availability data is embedded in
the source of their homepage (near the end).


I’ve found that there are some irregularities in the feed format, and
sometimes it changes without notice. It may have stabilized now though.


Happy hacking!
