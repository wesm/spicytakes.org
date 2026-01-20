---
title: "Exploring Datasets in Positron"
summary: "Talk at posit::conf(2025)"
date: 2025-09-17T00:00:00
tags: ["talk", "transcript"]
slug: positconf-exploring-datasets-positron
word_count: 3487
source_file: transcripts/2025-09-17-positconf-exploring-datasets-positron.md
content_type: transcript
event: "posit::conf(2025)"
video_url: "https://www.youtube.com/watch?v=R71WCIO6RyY"
---

{{< video https://www.youtube.com/watch?v=R71WCIO6RyY >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I give a deeper dive into the Data Explorer component I've been developing for Positron. I discuss my long interest in visual data exploration tools, going back to starting a visual analytics company called Datapad after five years of working on pandas. The Data Explorer addresses several pain points: the tedium of jumping between coding and inspecting results, scale limitations with large datasets, and the low information density of terminal-centric inspection workflows.

I cover the design principles behind the Data Explorer: enabling ephemeral exploration without disrupting coding flow, being fast and responsive regardless of whether you're in Python, R, or just clicking on a file. We built a custom virtual data grid to achieve snappiness even with unwieldy datasets (50,000 columns, billion rows via DuckDB). The tool provides summary statistics with histograms, filtering and sorting capabilities, and a new convert-to-code feature. I demonstrate live updating when data changes on disk or in memory, and discuss upcoming features like column/row pinning and Ibis expression support.

## Key Quotes

> "The human mind is able to process a lot of information. And so in building the data explorer for Positron, we wanted to pack a lot of visual information to leverage the power of human cognition to be able to recognize outliers, see issues with the dataset that you're trying to fix."

> "We think that human cognition is underrated and we want to help augment your ability to see issues with your data or to find areas that you want to look at more closely so that ultimately you can iterate faster in your data wrangling."

> "We wanted it to enable ephemeral exploration without disrupting your coding flow. Be fast and responsive. It should work just as well whether you're in a Python session, an R session, or just clicking on a CSV or a Parquet file."

> "If your dataset changes, if you manipulate the data frame or you change the data on disk, it should update almost instantaneously. Easy to say, hard to implement in practice."

> "We ultimately came to the conclusion that we needed to build a custom virtual data grid so that we could achieve a level of snappiness even with the most unwieldy datasets."

> "First, the grid, a digital frontier. Shout out to my Tron Legacy fans."

> "We built this partly for ourselves, but mostly for you, and so we want to hear from you how we can make this part of Positron even better than it is."

> "We wanted to build the ideal tool that we always wanted, and we think we've made a lot of progress on this."

## Transcript

**Wes McKinney:** Okay. Very good. Hi. I'm Wes McKinney. I'm a software architect here at Posit. And I'm here to do a little bit of a deeper dive into the Data Explorer, which you've already seen featured in all of my colleagues' talks in this Positron session. So I wanted to talk a little bit about how I got involved in the project, why I'm working on working developing the Data Explorer for Positron, and how we've designed it to have great performance, scalability, as well as integrating into your development workflow as a natural tool to make you more productive.

Most of you know me as the creator of the pandas project, and I've spent a lot of the last 20 years staring at datasets in the console and in other environments. I was really excited when the Jupyter Notebook, used to be called the iPython Notebook, came out in 2011. And for many years, I had a very console and notebook-centric environment for working with datasets and developing the open source libraries that process and manipulate these datasets.

In my book, Python for Data Analysis, it's about teaching people how to use these tools. But one of the first things that I did after five years of working on pandas was that I started a visual analytics company called Datapad to help build visual environments for working with datasets. And so this has been a long time passion for me.

Later, you know, we started the Ibis project to provide portability and adaptability between different backends so that we can build data expressions once and then run them in many different places. And you just saw that featured prominently in Austin's talk.

But when we think about the data viewer component that's within IDEs, often we run into a number of pain points. So one pain point is the tedium of jumping between coding and working with the dataset and inspecting and inspecting the results. And so seeing like the part of the dataset that you need, like the part that you're focused on, maybe you're doing some data cleaning, some data preparation, and you want to see specifically like the part of the dataset that you're trying to fix. We want to make that easier.

We've all seen the scale limitations of large datasets. A data viewer breaking down, it works great when your dataset is small. But when you have suddenly you have a dataset, wild dataset with 50,000 columns and it completely grinds to a halt, the dataset has a billion rows. As long as you have a backend, like DuckDB can handle a billion rows no problem. So we should be able to interact with those types of datasets in our data viewer. So having things become laggy or unresponsive is something we definitely don't want.

Another problem, which is a little more subtle, is the low information density problem. And this is definitely associated with those terminal centric data inspection workflows where you're just not seeing that much about the dataset and the terminal. So the human mind is able to process a lot of information. And so in building the data explorer for Positron, we wanted to pack a lot of visual information to leverage the power of human cognition to be able to recognize outliers, see issues with the dataset that you're trying to fix.

So we think that human cognition is underrated and we want to help augment, you know, your ability to see issues with your data or to find areas that you want to look at more closely so that ultimately you can iterate faster in your data wrangling, whether that's you writing code or working with an AI assistant, Positron assistant or another LLM to write your code.

So we're building all of this in Positron. We had some inspirations from some other tools that we love. Of course, there's the data viewer, which has been a popular and longstanding tool in our studio. There's some other really cool projects that I've admired from afar in real developer as well as the data wrangler for VS code. Of course, there's a ton of other projects that we can learn from.

And so in our design principles for the data explorer, we wanted it to enable ephemeral exploration without disrupting your coding flow. Be fast and responsive. It should work just as well whether you're in a Python session on R session or just clicking on a CSV or a parquet file. It should update in realtime as you work. So if your dataset changes, if you apply it, you manipulate the data frame or you change the data on disk, it should update almost instantaneously. Easy to say, hard to implement in practice.

In pulling this off, we had to do a lot of custom work. So in particular, we spent a lot of time deciding can we do this with off-the-shelf, you know, cobbling together off-the-shelf components and what we ultimately came to the conclusion that we needed to do, you know, build a custom virtual data grid so that we could achieve a level of snappiness even with the most unwieldy datasets. So those really wide datasets or wide and long datasets. We don't want to have any lagging or unresponsiveness.

We've done a lot of optimization work to achieve good performance across the different environments where you're looking at data. We don't want the data explorer to weigh down your computer with a lot of unneeded memory that it's holding. So it's very memory efficient. And we've done a lot of work to enable that live update workflow, which I'll show you in the live demo portion.

We want to make it something you can launch and get at very easily from wherever you are in Positron. So you've already seen that in some of these other talks, but if you just have a data file in your workspace, you can click on it or visit it through the command palette and it will just open. If you have a data frame in the variables pane, there's a button over here that you can click and open the data explorer. But if you're working in the console, we also want you to be able to run, let's say you have an ad hoc Python expression, and that you can use the in Python, you can use the percent view magic or an R, the capital V view function, which you can pipe with a in a dplyr expression, for example, and open a data explorer just to look at the particular Python expression that you're working on.

So you've seen the data explorer. This is what it looks like. So I'll go a little bit through the layers of the data explorer.

First, the grid, a digital frontier. Shout out to my Tron legacy fans. Again, it's a custom built table spreadsheet-like UI. It provides instant scrolling to anywhere in the data set. It provides selection and copy and pasting. And soon in the next major release of Positron, it will support column and row pinning, which I will show you.

The summary pane gives you those at-a-glance statistical data summaries. So when you open the data explorer, you have histograms or for categorical data, you have written strings, you have value counts. You can see the most frequently occurring values in each column. These can be expanded, showing you more detailed summary statistics. Soon there's a feature launching to be able to sort and search within columns. So if you have a data set with hundreds or thousands of columns and there's certain columns that you want to filter down to, there will soon be a filter bar that allows you to find just those columns of interest that you want to see in the data set. I'm keen to eventually have a click-to-drag filter capability within these sparklines, so stay tuned for that, if you're interested in that. We can chat about how it should work on GitHub.

Filtering and sorting, I'll show more in the live demo, but we want to enable you to find the parts of the data set that you're after very quickly. So those filters show up in the filter bar, and you can sort columns in ascending or descending order by clicking on the column dropdown menu from the data explorer. You can sort by multiple columns.

Just recently, Isabel added convert-to-code capabilities, so if there's a particular view that you're looking at, whether it's in Python R or from clicking on a file in the explorer, you can get the exact code that would produce that view and then copy and paste that into your code window, which is super useful.

So it's much more exciting to see a live demo, and I'm going to pray to the demo gods that there will not be too many. I've run into so many bugs in my career with live demos, so I will do my best.

So here we are in Positron. I'll make us a little bigger, and first of all, files in the file browser, if we have a CSV or Parquet file, if we click on a Parquet file, it opens and populates. This uses DuckDB amazingly, which ships with Positron to provide this capability. When you sort from the column dropdown, it, you know, it sorts and updates pretty much instantaneously. You can jump to the middle of a sorted table, and it's essentially instantaneous.

In the summary pane, we have tool tips on these histograms, so for example, suppose you were interested in data that's missing in the departure time table, so if I double click here, I jump right to this departure table, and here I'm going to add a filter, departure time is missing, and so now we see just the missing values in that column, and we can see all of the summary plots here have updated to just show the statistics where there are missing values, and so if you were interested and say, well, maybe there's just one, you know, pesky origin, so it turns out that it's these New York airports where there happens to be a missing departure time, so they're not reporting their data very accurately.

But a cool thing that we can do is this column pinning functionality that I just mentioned is a new feature, so when you have a column with a data set with many columns, sometimes you want to see that column, which is in the middle of the table, and then be able to jump somewhere else in the table, so you can visually compare the data values in that column with another column, which is in some other part of the data set, and the same is true of if there's a wily row that you want to compare with other rows in the data set, we can pin that row to the top of the data explorer and then jump elsewhere in the table, so we hope that you find that useful.

So very quickly, just wanted to show you a little bit of how the live updating functionality works, so here I created a pandas data frame which is populated in the variables pane, I click on view data table to open that there, and then I'm going to split right, collapse the variables pane, and so here it's a small data set, I'll go back to my data file where I'm editing the data frame, and I will quickly add a new column of some random values, and so I run that, I run that line, it adds the new column with those random values, and you can see that each time I run that line, so it's just random data, and you can see that it updates in real time.

And that the same is true for if you just, let's say, clicked on a CSV file, and let's open that CSV file as plain text, I'll move that split right so we can see them side by side, and so if I were to change this value dog to bird, save the file, so it updates immediately in the table.

And so I find it's very useful to have a data explorer open, you can even pop this, any of these tabs out into new windows, and so if you have a large monitor, like I have one of those ultra wide monitors at home, and so it's nice to be able to have the data explorer window out as a separate window alongside my code editor and my console, so that I can be looking at the data set while I'm writing my code and doing all of my data munching.

So we put a lot of work into this, of course, we built this partly for ourselves, but mostly for you, and so we want to hear from you how we can make this part of Positron even better than it is, we have tons of ideas about new capabilities to add to it, but the most important, in addition to using it, one of the best ways you can help us is by providing your feedback, so we're on GitHub, start a GitHub discussion, open a GitHub issue if you run into challenges, but this is, we wanted to build the ideal tool that we always wanted, and we think we've made a lot of progress on this, and we're excited to see where we can take it to be an important part of Positron going forward, so thank you.

**Host:** Thank you so much. We have quite a few questions here, so does the data explorer work with Ibis?

**Wes McKinney:** There is an open pull request to add direct data explorer support for Ibis expression, so if you have an Ibis expression, it will show up in the variables pane, but you cannot currently open it as a, in a data explorer tab, you can execute it and then open it, but as soon as we merge Isabel's pull request, we will have Ibis support and direct Ibis support in the data explorer, which is great.

**Host:** Outstanding, thank you. What are your thoughts about data exploration for other data types, such as multi-dimensional arrays?

**Wes McKinney:** We've discussed adding support in the data explorer for non-tabular data. It would be tricky from a user interface standpoint, because if it doesn't map neatly into the grid, we would need to develop some other type of UI layer that enables you to to drill down into the different, let's say you were looking at a large nested dictionary type object, or like a nested array, like a NumPy array with more than two dimensions, is that type of thing. You can open R matrices in the data explorer, but dimensions more than that, we haven't built support yet, but if you have an idea of how you think that that should work in the data explorer, we would be interested in hearing from you.

**Host:** Great. How well does the data viewer play with the dreaded list column?

**Wes McKinney:** I know that you can see list columns. That's one area that we have not, like if you go on the positron issue tracker, there are issues about having improved UI for for list types, and like looking at complex values. So, for example, if you have a large value that does not fit in a that does not fit in a data cell, so, you know, we it's like, for example, like if we had a value that doesn't fit here, if you hover over it, it will show you a tooltip showing the whole value, but for more complex objects, including list or array types, pullers has a built in list type, it will format the values as it will show the list of values within the cell, but we would like to be able to drill into those cells and get a richer UI display to be able to, like similar to how you can look at a JavaScript object, like a JSON object in the Chrome developer tools pane, if you have ever done that, we would like to expose that type of visual display of complex values within the data explorer.

**Host:** Great. I think we have time for one more quick question. Are there capabilities to explore data from relational databases without having to load the tables into the environment?

**Wes McKinney:** Could you say that again? Sorry, yeah.

**Host:** Are there capabilities to explore data from relational databases without having to load the tables into the environment?

**Wes McKinney:** So, we're planning to develop an integration between the data explorer and the connections pane, so if you're connected to a remote database, a Postgres database or a DuckDB database, that you will be able to, in the future, that you will be able to click on a table and get a data explorer pane. There's some subtleties around, we want to provide control to the user so that it does not execute too much unwanted computation so that you don't get a large bill from Snowflake or from your database provider that you ran tons of queries because you clicked on the wrong table in the connections pane, so probably some of the summary pane plots will be opt-in or click to compute so that we aren't spamming your Snowflake warehouse with too many potentially unwanted queries on a massive table.

I think this will go hand-in-hand with a SQL editing and development experience that we're planning to develop in Positron in the fullness of time, so I think that will all go hand-in-hand, being able to develop and test and run SQL queries directly within Positron to see the outputs of SQL queries within the data explorer and to be able to see your data warehouse as a pane in the connections pane in directly in Positron.

**Host:** Thank you so much.

**Wes McKinney:** Thank you.