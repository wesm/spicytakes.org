---
title: "Don't Compare Averages"
description: "In business meetings, it's common to compare groups of numbers by   comparing their averages. But doing so often hides important information in   the distribution of the numbers in those groups. There"
date: 2020-09-24T00:00:00
tags: ["data analytics", "metrics"]
url: https://martinfowler.com/articles/dont-compare-averages.html
slug: dont-compare-averages
word_count: 2272
---


Imagine you're an executive, and you're asked to
    decide which of your sales leaders to give a big award/promotion/bonus to.
    Your company is a tooth-and-claw capitalist company that only considers
    revenue to be important, so the key element in your decision is who has got
    the most revenue growth this year. (Given it's 2020, maybe we sell
    masks.)


Here's the all-important numbers.



| name | average revenue increase (%) |
| alice | 5.0 |
| bob | 7.9 |
| clara | 5.0 |



And a colorful graph


![](dont-compare-averages/average-bars.png)


Based on this, the decision looks easy. Bob, at just under 8%, has a
    notably better revenue increase than his rivals who languish at 5%.


But lets dig deeper, and look at the individual accounts for each of our
    salespeeps.



| name | account revenue increases (%) |
| alice | -1.0 | 2.0 | 1.0 | -3.0 | -1.0 | 10.0 | 13.0 | 8.0 | 11.0 | 10.0 |
| bob | -0.5 | -2.5 | -6.0 | -1.5 | -2.0 | -1.8 | -2.3 | 80.0 |  |  |
| clara | 3.0 | 7.0 | 4.5 | 5.5 | 4.8 | 5.0 | 5.2 | 4.0 | 6.0 | 5.0 |



This account-level data tells a different story. Bob's high performance
    is due to one account yielding a huge 80% revenue increase. All his other
    accounts shrank. With Bob's performance based on just one account,
    is he really the best salespeep for the bonus?


Bob's tale is a classic example of one the biggest problems with
    comparing any group of data points by looking at the average. The usual
    average, technically the mean, is very prone to one outlier swinging the
    whole value. Remember the average net worth of a hundred homeless people is
    $1B once Bill Gates enters the room.


The detailed account data reveals another difference. Although Alice and
    Clara both have the same average, their account data tells two very
    different stories. Alice is either very successful (~10%) or mediocre (~2%), while Clara
    is consistently mildly successful (~5%). Just looking at the average hides this
    important difference.


By this point, anyone who's studied statistics or data visualization is
    rolling their eyes at me being Captain Obvious. But this knowledge isn't
    getting transmitted to folks in the corporate world. I see bar charts
    comparing averages all the time in business presentations. So I decided to
    write this article, to show a range of visualizations that you can use to
    explore this kind of information, gaining insights that the average alone
    cannot provide. In doing this I hope I can persuade some people to stop only
    using averages, and to question averages when they see others doing that.
    After all there's no point eagerly collecting the data you need to be a
    data-driven enterprise unless you know how to examine that data
    properly.


## A strip chart shows all the individual numbers


So the rule is don't compare averages when you don't know what the
      actual distribution of the data looks like. How can you get a good picture
      of the data?


I'll start with the case above, when we don't have very many
      data points. Often the best way to go for this is a strip chart, which
      will show every data point in the different populations.


![](dont-compare-averages/sales-strip.png)


With this chart we can now clearly see the lone high point for Bob,
      that most of his results are similar to Alice's worst results, and that Clara
      is far more consistent. This tells us far more than the earlier bar chart,
      but isn't really any harder to interpret.


You may then ask, how to plot this nice strip chart? Most people who
      want to plot some quick graphs use Excel, or some other spreadsheet. I
      don't know how easy it is to plot a strip chart in the average
      spreadsheet, as I'm not much of a spreadsheet user. Based on what I see in
      management presentations, it may be impossible, as I hardly ever see one.
      For my plotting I use R, which a frighteningly powerful statistics
      package, used by people who are familiar with phrases like âKendall rank
      correlation coefficientâ and âMann-Whitney U testâ. Despite this fearsome
      armory, however, it's pretty easy to dabble with the R system for simple
      data manipulation and graph plotting. It's developed by academics as
      open-source software, so you can download and use it without worrying about
      license costs and procurement bureaucracy. Unusually for the open-source
      world, it has excellent documentation and tutorials to learn how to use
      it. (If you're a Pythonista, there's also a fine range of Python libraries
      to do all these things, although I've not delved much into that
      territory.) If you're curious about R, I have a
      summary in the appendix of how I've learned what I know about it.


If you're interested in how I generate the various charts I show
      here, I've included a âshow-codeâ disclosure after each chart which shows
      the commands to plot the chart. The sales dataframes
      used have two columns: name, and d_revenue.


What if we have a larger number of data points to consider? Imagine our
      trio are now rather more important, each handling a couple of hundred
      accounts. Their distributions still, however show the same basic characteristics, and we
      can see that from a new strip chart.


![](dont-compare-averages/sales-strip-large.png)


One problem with the strip chart, however, is that we can't see the
      average. So we can't tell whether Bob's high values are enough to
      compensate for this general lower points. I can deal with this by plotting
      the mean point on the graph, in this case as a black diamond.


![](dont-compare-averages/sales-strip-mean-large.png)


So in this case Bob's mean is a bit less than the other two.


This shows that, even though I often disparage those who use means to
      compare groups, I don't think means are useless. My disdain is for those
      who *only* use means, or use them without examining the overall
      distribution. Some kind of average is often a useful element of a
      comparison, but more often than not, the median is actually the better
      central point to use since it holds up better to big outliers like Bob's.
      Whenever you see an âaverageâ, you should always consider which is better:
      median or mean?


Often the reason median is such an under-used function is because our tooling
      doesn't encourage us to use it. SQL, the dominant database query
      language,  comes with a built-in AVG function
      that computes the mean. If you want the median, however, you're usually
      doomed to googling some rather ugly algorithms, unless your database has
      the ability to load extension functions. 1 If
      some day I become supreme leader, I will decree that no platform can have
      a mean function unless they also supply a median.


1: 
      I've made good use of SQLite's 
      [extension-functions](https://sqlite.org/contrib) contributed file,
      which has a bunch of useful functions,
      including median.


## Using histograms to see the shape of a distribution


While using a strip chart is a good way to get an immediate sense of
      what the data looks like, other charts can help us compare them in
      different ways. One thing I notice is that many people want to use The One
      Chart to show a particular set of data. But every kind of chart
      illuminates different features of a dataset, and it's wise to use several
      to get a sense of what the data may be telling us. Certainly this is true
      when I'm exploring data, trying to get a sense of what it's telling me.
      But even when it comes to communicating data, I'll use several charts so
      my readers can see different aspects of what the data is saying.


The histogram is a classic way of looking at a distribution. Here are
      histograms for the large dataset.


![](dont-compare-averages/sales-hist-large.png)


Histograms work really well at showing the shape of a single
      distribution. So it's easy to see that Alice's deals clump into two
      distinct blocks, while Clara's have a single block. Those shapes are
      somewhat easy to see from the strip chart too, but the histogram clarifies
      the shape.


A histogram shows only one group, but here I've shown several together
      to do the comparison. R has a special feature for this, which it refers to
      as faceted plots. These kind of âsmall multiplesâ (a term coined by
      Edward Tufte) can be very handy for comparisons. Fortunately R makes them
      easy to plot.


Another way to visualize the shapes of the distributions is a density
      plot, which I think of as a smooth curve of a histogram.


![](dont-compare-averages/sales-dense-mult-large.png)


The density scale on the y axis isn't very meaningful to
      me, so I tend to remove that scale from the plot - after all the key
      element of these are shapes of the distributions. In addition, since the
      density plot is easy to render as a line, I can plot all of them on a
      single graph.


![](dont-compare-averages/sales-dense-single-large.png)


Histograms and density plots are more effective when there are more
      data points, they aren't so helpful when there's only a handful (as with
      the first example). A bar chart of counts is useful when there are only a few
      values, such as the 5-star ratings on review sites. A few years ago Amazon
      added such a chart for its reviews, which show the distribution in
      addition to the average score.


## Boxplots work well with many comparisons


Histograms and density plots are a good way to compare different
      shapes of distributions, but once I get beyond a handful of graphs then
      they become difficult to compare. It's also useful to get a sense of
      commonly defined ranges and positions within the distribution. This is
      where the boxplot comes in handy.


![](dont-compare-averages/sales-box-large.png)


The box plot focuses our attention on the middle range of the data, so
      that half the data points are within the box. Looking at the graph we can
      see more than half of Bob's accounts shrank and that his upper quartile is
      below Clara's lower quartile. We also see his cluster of hot accounts at
      the upper end of the graph.


![](dont-compare-averages/box-plot.png)


The box plot works nicely with a couple of dozen items to compare,
      providing a good summary of what the underlying data looks like. Here's an
      example of this. I moved to London in 1983 and moved to Boston a decade
      later. Being British, I naturally think about how the weather compares in
      the two cities. So here is a chart showing comparing their daily high
      temperatures each month since 1983.


![](dont-compare-averages/bos-lon.png)


This is an impressive chart, since it summarizes over 27,000 data
      points. I can see how the median temperatures are warmer in London during
      the winter, but cooler in the summer. But I can also see how the
      variations in each month compare. I can see that over a quarter of the
      time, Boston doesn't get over freezing in January. Boston's upper quartile
      is barely over London's lower quartile, clearly indicating how much colder
      it is in my new home. But I can also see there are occasions when Boston
      can be warmer in January than London ever is during that winter month.


The box plot does have a weakness, however, in that we can't see the
      exact shape of the data, just the commonly defined aggregate points. This
      may be an issue when comparing Alice and Clara, since we don't see the
      double-peak in Alice's distribution in the way that we do with histogram
      and density chart.


There are a couple of ways around this. One is that I can easily
      combine the box plot with the strip chart.


![](dont-compare-averages/sales-box-strip-large.png)


This allows me to show both the underlying data, and the important
      aggregate values. In this plot I also included the black diamond that I
      used before to show the position of the mean. This is a good way to
      highlight cases like Bob where the mean and median are quite different.


Another approach is the violin plot, which draws a density plot into
      the sides of the boxes.


![](dont-compare-averages/sales-violin-large.png)


This has the advantage of showing the shape of the distribution
      clearly, so the double peak of Alice's performance stands right out. As
      with density plots, they only become effective with a larger number of
      points. For the sales example, I think I'd rather see the points in the
      box, but the trade-off changes if we have 27,000 temperature measurements.


![](dont-compare-averages/bos-lon-violin.png)


Here we can see that the violins do a great job of showing the shapes
      of the data for each month. But overall I find the box chart of this data
      more useful. It's often easier to compare by using significant signposts
      in the data, such as the medians and quartiles. This is another case where
      multiple plots play a role, at least while exploring the data. The box
      plot is usually the most useful, but it's worth at least a glance at a
      violin plot, just to see if reveals some quirky shape.


## Summing Up

- Don't use just an average to compare groups unless you understand
        the underlying distribution.
- If someone shows you data with just an average ask: âwhat does the
        distribution look like?â
- If you're exploring how groups compare, use several different plots
        to explore their shape and how best to compare them.
- If asked for an âaverageâ, check whether a mean or median is better.
- When presenting differences between groups, consider at least the
        charts I've shown here, don't be afraid to use more than one, and pick
        those that best illustrate the important features.
- above all: **plot the distribution!**


---
