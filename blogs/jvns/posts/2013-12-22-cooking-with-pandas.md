---
title: "A pandas cookbook"
date: 2013-12-22
url: https://jvns.ca/blog/2013/12/22/cooking-with-pandas/
slug: cooking-with-pandas
word_count: 256
---


A few people have told me recently that they find the slides for my
talks really helpful for getting started with
[pandas](http://pandas.pydata.org), a Python library for manipulating
data. But then they get out of date, and it’s tough to support slides
for a talk that I gave a year ago.


So I was procrastinating packing to leave New York yesterday, and I
started writing up some examples, with explanations! A lot of them are
taken from talks I’ve given, but I also want to give some new
examples, like

- how to deal with timestamps
- what is a pivot table and why would you ever want one?
- how to deal with “big” data


I’ve put it in a GitHub repository called
[pandas-cookbook](https://github.com/jvns/pandas-cookbook). It’s along
the same lines as the pandas talks I’ve given – take a real dataset
or three, play around with it, and learn how to use pandas along the
way.


Here’s the current table of contents, as of right now. These links
will probably break as I update it.

- [Chapter 1: Reading from a CSV](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%201%20-%20Reading%20from%20a%20CSV.ipynb)
- [Chapter 2: Selecting data & finding the most common complaint type](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%202%20-%20Selecting%20data%20&%20finding%20the%20most%20common%20complaint%20type.ipynb)
- [Chapter 3: Which borough has the most noise complaints? (or, more selecting data)](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%203%20-%20Which%20borough%20has%20the%20most%20noise%20complaints%3F%20%28or%2C%20more%20selecting%20data%29.ipynb)
- [Chapter 4: Find out on which weekday people bike the most with groupby and aggregate](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%204%20-%20Find%20out%20on%20which%20weekday%20people%20bike%20the%20most%20with%20groupby%20and%20aggregate.ipynb)
- [Chapter 5: Combining dataframes and scraping Canadian weather data](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%205%20-%20Combining%20dataframes%20and%20scraping%20Canadian%20weather%20data.ipynb)
- [Chapter 6: String operations! Which month was the snowiest?](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%206%20-%20String%20operations%21%20Which%20month%20was%20the%20snowiest%3F.ipynb)
- [Chapter 7: Cleaning up messy data](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%207%20-%20Cleaning%20up%20messy%20data.ipynb)
- [Chapter 8: Parsing Unix timestamps](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%208%20-%20How%20to%20deal%20with%20timestamps.ipynb)
