---
title: "Guest post: Clustering and predicting NYC taxi activity"
date: 2014-10-27
url: https://mathbabe.org/2014/10/27/guest-post-nyc-taxi-wait-times/
word_count: 614
---


*This is a guest post by [Deepak Subburam](https://www.linkedin.com/pub/deepak-subburam/8/270/b3a), a data scientist who works at [Tessellate](http://tessell8.com/).*


![Screenshot](https://i0.wp.com/www.tessell8.com/blog/static/taxishot3.jpg)


from NYCTaxi.info


Greetings fellow Mathbabers! At Cathy’s invitation, I am writing here about [NYCTaxi.info](http://NYCTaxi.info), a public service web app [my co-founder and I](http://www.tessell8.com) have developed. It overlays on a Google map around you estimated taxi activity, as expected number of passenger pickups and dropoffs this current hour. We modeled these estimates from the recently released 2013 NYC [taxi trips dataset](http://chriswhong.com/open-data/foil_nyc_taxi/) comprising 173 million trips, the same dataset that Cathy’s [post last week](https://mathbabe.org/2014/10/17/de-anonymizing-what-used-to-be-anonymous-nyc-taxicabs/) on deanonymization referenced. Our work will not help you stalk your favorite NYC celebrity, but guide your search for a taxi and maybe save some commute time. My writeup below shall take you through the four broad stages our work proceeded through: **data extraction and cleaning **, **clustering**, **modeling**, and **visualization**.


We **extract** three columns from the data: the longitude and latitude GPS coordinates of the passenger pickup or dropoff location, and the timestamp. We make no distinction between pickups and dropoffs, since both of these events imply an available taxicab at that location. The data was generally **clean**, with a very small fraction of a percent of coordinates looking bad, e.g. in the middle of the Hudson River. These coordinate errors get screened out by the clustering step that follows.


We **cluster** the pickup and dropoff locations into areas of high density, i.e. where many pickups and dropoffs happen, to determine where on the map it is worth making and displaying estimates of taxi activity. We rolled our own algorithm, a variation on heatmap generation, after finding existing clustering algorithms such as K-means unsuitable—we are seeking centroids of areas of high density rather than cluster membership per se. See figure below which shows the cluster centers as identified by our algorithm on a square-mile patch of Manhattan. The axes represent the longitude and latitude of the area; the small blue crosses a random sample of pickups and dropoffs; and the red numbers the identified cluster centers, in descending order of activity.


![](https://i0.wp.com/www.tessell8.com/blog/static/square21.png)


Taxi activity clusters


We then **model** taxi activity at each cluster. We discretize time into hourly intervals—for each cluster, we sum all pickups and dropoffs that occur each hour in 2013. So our datapoints now are triples of the form [<cluster>, <hour>, <activity>], with <hour> being some hour in 2013 and <activity> being the number of pickups and dropoffs that occurred in hour <hour> in cluster <cluster>. We then regress each <activity> against neighboring clusters’ and neighboring times’ <activity> values. This regression serves to smooth estimates across time and space, smoothing out effects of special events or weather in the prior year that don’t repeat this year. It required some tricky choices on arranging and aligning the various data elements; not technically difficult or maybe even interesting, but nevertheless likely better part of an hour at a whiteboard to explain. In other words, typical data science. We then extrapolate these predictions to 2014, by mapping each hour in 2014 to the most similar hour in 2013. So we now have a prediction at each cluster location, for each hour in 2014, the number of passenger pickups and dropoffs.


We **display** these predictions by overlaying them on a Google maps at the corresponding cluster locations. We round <activity> to values like 20, 30 to avoid giving users number dyslexia. We color the labels based on these values, using the black body radiation color temperatures for the color scale, as that is [one of two color scales](https://en.wikipedia.org/wiki/Heat_map#Color_schemes) where the ordering of change is perceptually intuitive.


If you live in New York, we hope you find NYCTaxi.info useful. Regardless, we look forward to receiving any comments.
