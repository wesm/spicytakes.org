---
title: "Building Rich, High Performance Tools for Practical Data Analysis"
summary: "Video at O'Reilly Webcast"
date: 2013-02-20T00:00:00
tags: ["video", "transcript"]
slug: oreilly-webcast-building-rich-high-performance-tools-for-practica
word_count: 8290
source_file: transcripts/2013-02-20-oreilly-webcast-building-rich-high-performance-tools-for-practica.md
content_type: transcript
event: "O'Reilly Webcast"
video_url: "https://www.youtube.com/watch?v=-q9luEiO_3w"
---

{{< video https://www.youtube.com/watch?v=-q9luEiO_3w >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this Strata Conference talk, I share my approach to building data analysis tools.

## Philosophy

Data preparation represents 80-95% of most analysis workflows. I argue the data science talent shortage can be addressed by making existing practitioners more productive through better tooling. As I put it, "big data is largely about counting things"—much of the infrastructure focuses on reducing enormous datasets into manageable forms.

Building data tools is about human-computer interaction and user interface design, not just algorithms. I advocate for APIs that "fit your brain," citing Uncle Bob Martin's principle that good code "looks like you expect it to." I warn against "parameter soup"—overly general tools with too many configuration options.

## Data Structures

Proper data type systems must handle messy data. Supporting missing values is critical: "most data sets that I encounter have missing values"—often overlooked in academic treatments but essential for real-world work.

Array programming builds on concepts from APL, Fortran, and MATLAB. Arrays enable efficient batch operations and memory-efficient views without copying.

Tables—collections of arrays with metadata—form the primary abstraction. Hierarchical row and column labels can represent multi-dimensional data in tabular format, supporting pivoting and reshaping.

## Split-Apply-Combine

I highlight Hadley Wickham's work on split-apply-combine: split data by grouping keys, apply functions to each group, combine results. The implementation relies on hash tables and sorting—"the two most important things that I utilize on a day-to-day basis."

## Performance

Different implementations of identical algorithms can vary dramatically in speed. Investigating why the J language outperformed other tools revealed that performance often comes from choosing algorithms suited to specific data characteristics, not just optimizing general-purpose implementations.

The demo analyzes USDA nutrient data, showing fluid chaining of operations: grouping, selecting, computing statistics, and plotting.

## Vision

Every programming language should eventually have robust structured data processing capabilities. While syntax differs, fundamental operations share common patterns.

## Key Quotes

> "Working with data and preparing data ends up being 80% to even 95% of the work that's involved in a data analysis workflow."

> "We like to joke in the data community that big data is largely about counting things."

> "Data tools, I like to think about it being the intersection of computer science, which is the algorithms and the underlying data processing code which actually crunches the data and reshapes it and moves it around. But the bigger part of that is how you interact with that code... So it's more about human-computer interaction and user interface design as much as just the underlying algorithms."

> "You know it's a good API if it fits your brain... A sign of good, clean code is if it pretty much looks like you expect it to."

> "There's very general things you're doing with the data set and you might have 12 different knobs that you can turn and that can also be very overwhelming when you're just trying to get some work done."

> "Most data sets that I encounter have missing values."

> "Hashing and sorting, as far as implementing data tools, are two of the most important things that I utilize on a day-to-day basis."

> "The main solution to data science's shortage is to make existing data scientists more productive."

> "I would hope that every language has a core set of structured and semi-structured data processing tools, so that you can be programming in any language and still express operations on the data in a very natural way."

---

## Transcript

The webcast today is sponsored by Accenture. And we'd like to say a very big thank you

to Accenture and let you all know that knowledge is key. But knowledge without insight

isn't much of an advantage. Accenture has more than 257,000 people serving clients

in more than 120 countries. It's a global management consulting, technology services,

and outsourcing company that helps its clients use analytics to turn data into insight,

insight into action, and action into tangible results. That's high performance delivered.

You can learn more about Accenture, how it helps its clients navigate and harness the power

of big data by building big data infrastructures. Folks, today we have Wes McKinney

presenting Building Rich High Performance Tools for Practical Data Analysis.

Wes gave this talk back in the fall at our Strata Conference in New York.

And the talk was so well received and attended that we asked Wes if he could present the event

for you all today. And we're really excited to have him with us.

It is my pleasure to turn the program over to Wes for his presentation. Hello, Wes.

Wes McKinney Hi, Yasmina. Thanks for the introduction,

and thanks everyone for joining us for this webcast. As Yasmina said, I gave this talk

back at the Strata Conference back in October, which already feels like a long time ago.

And I would describe the talk a little, I guess, as more about my philosophy and process

for thinking about building data analysis tools and some of the things that I've learned

along the way in my work in building data tools. So I'll be sharing that with you.

So thankful to Accenture for supporting the webcast.

So the structure of the talk, I'll tell you a little bit about my background

and what I've been working on for the last few years, and how I got involved

with building data tools and the kinds of things that I think about.

I'll talk about some of the motivations for why to, I guess, why are we interested in the philosophy

and what are the various ingredients that go into building data analysis tools,

and what kinds of problems are we trying to solve. And then I'm going to talk specifically

about some of the technical details that go into building data tools,

and I'll show you some examples that come from my book.

So my background is, well, I graduated from MIT back in 2007, and I joined the finance world

and worked for H2O Capital Management for about three years. And while I was there,

I got involved with building data analysis tools for Python,

and started what would later become the pandas Project.

And over the last two or three years, pandas has grown into a very successful project

in large part because I've been putting a lot of development work into it.

Now there's a very robust community around the project, and it's being used very productively

in many areas of the industry. I started out in finance, but pandas is very popular

in essentially anywhere that's working, any industry that's working with data,

and almost anyone who's using Python is using pandas, I find.

I published a book which also came out around the time of Latte Strada.

It's called Python for Data Analysis. And I intended for the book to be

a very accessible introduction to the modern scientific computing stack in Python.

So we do things like NumPy, and IPython, and Matplotlib.

So it's the core scientific tools in Python. And about 60% of the book or more

is really a robust and practical introduction to pandas.

I'm looking at various important topics in data manipulation and data preparation,

and showing you how you can use Python to productively integrate

into your analysis workflow. It's not a treatise on data analysis methods per se,

but more about the kinds of tools in Python that you can start using right away

to incorporate into your analysis.

So I spend a lot of time thinking about data tools.

And I guess working with data and preparing data ends up being 80% to even 95%

of the work that's involved in a data analysis workflow.

So you see various estimates from studies people do on data analysis.

And I'm very interested both in the big data and the small data.

In the case of big data, a lot of the analytics that you're doing

is just taking very, very large data and reducing it to a small or medium size

so that you can reshape, and reshape, and place, and size, and create models.

So a lot of the modeling and really agile data work happens

at what I would call the small and medium data level in typically big data tools.

There is a lot of big data machine learning and big data analytics.

A lot of big data infrastructure is geared around producing enormous data sets

into a manageable form that can be visualized, and placed, and sized, and modeled on.

So we like to joke in the data community that big data is largely about counting things.

I've already said that in a talk, and I always like to use that saying.

So really we're talking about simplifying data wrangling.

So when I say data wrangling, I'm talking about all of the work that you need to do

to take a raw data set which comes in in a CSV file or comes out of a database

or a series of database tables or a series of CSV files,

and all of the work that you need to do to integrate that data together,

to clean up data that's not in the form that you need

or contain data that's unclean or needs some regularization or processing.

So kind of all of the tools along that pipeline I've been focused on,

identifying what are the key features and things that trip up users

and slow down your data analysis process.

So this really ends up coming down to a lot of user interface design.

So data tools, I like to think about it being the intersection of computer science,

which is the algorithms and the underlying data processing code

which actually crunches the data and reshapes it and moves it around.

But the bigger part of that is how you interact with that code

and what are the sequences, what's the sequence of commands that you type into,

type into the terminal or you type into your text editor

to describe the operations that you're doing with the data.

So it's more about human-computer interaction and user interface design

as much as just the underlying algorithms and doing things very fast and efficiently

and in a scalable manner.

So often when you sit down and you're working with a data set,

especially when you're working with an unfamiliar tool set,

thinking about how all of the pieces fit together

and how to efficiently iterate from point A to point B in the analysis process.

So, of course, there are costs to making mistakes in user interface design.

So I like this sort of big data joke that in big data,

if you make a coding error, it can end up costing you a great deal.

I think that's less important in small and medium data

where if you enter the wrong command,

you only have to wait a few seconds to see that it was the wrong command.

But I think the same kinds of design considerations are very important

in big data tools and small data tools.

So very concretely, what that comes down to is API design.

And so there are lots of things to consider in API design.

A couple of things you hear about is that, especially in the Python world,

we like to say that you know it's a good API if it fits your brain.

So that, you know, the function that you write, a function called B, right?

parameters that you pass into them.

It's a sign of, I think Uncle Bob Martin says that,

you know, a sign of good, clean code

is if it pretty much looks like you expect it to.

So I like to, you know, you know that you've designed

a good tool if people don't complain about it

and it sort of seems like common sense

and it fits how you think about the problem.

Of course, there's also risk with API design.

And especially in cases where you might have

a very general tool with many different options

and end up in what I would call a parameter soup

or a parameter health where, you know,

there's very general things you're doing with the data set

and you might have 12 different knobs that you can turn

and that can also be very overwhelming

when you're just trying to get some work done.

So there's another side of it that syntax matters

and there's a cost to, sort of a mental cost

in looking at code and especially code

that other people have written and parsing,

sort of mentally parsing what the code does

and visualizing, especially in the course

of working with data, visualizing the data operation.

And sort of how everything works.

You can definitely recognize sort of bad syntax.

These are kind of two very extreme examples.

Each of these lines is an implementation of quicksort,

so this quicksort algorithm.

This is a bit, you know, cherry picking

and fans of APL languages might complain at me

but the top one is in the J language

and the bottom one is in the K language

which are both modern implementations

of the array programming language APL

from the 80s and 90s, like I said, really 70s in fact.

There's even more, you know, esoteric languages

where you can implement things where the code,

you know, just stops making any sense at all.

You can fill in, you know, the stars are here.

This is a real programming language

but it's largely invented

as a completely esoteric programming language.

So there's definitely a lot of distance, you know,

you can go far off in the extreme

of very esoteric difficult to programming languages

by certain adult programming interfaces.

And, you know, I love this quote from Guido Van Roosa

who is the inventor of Python,

that user interface can handle only so much complexity

or it becomes unusable.

So focusing on building simple tools

versus complex tools, I think is generally

common sense way to do it.

And of course there are, you know,

folks among us who like very complex, precise tools

but there is a place in between.

So in terms of actually implementing data tools

if you were starting on a blank slate

and building yourself a set of practical

data analysis tools, there's the API

and sort of user interface side of things

of how you, the user, you know,

what's the code going to look like

that you'll write to do analysis

with the tool that you've built.

And then there's, you know,

how you actually implement it

and that comes down to representing

the underlying data types,

whether you have, you know,

strings or booleans or dates

or other kinds of data.

Often those, you're working,

one of your primitive types is an array,

so you have a sequence of essentially

multi-dimensional sequence of those data types.

Data structures also fit into that,

especially for writing algorithms

and the algorithms part of things

is how, you know, must be carefully thought about

to make everything fast.

So in terms of arrays, I guess nowadays

a lot of us are programming in R

and Python and MATLAB and we don't think

too much about arrays.

We say, okay, I've got, you know,

a bunch of data in a data frame

or a table-like object.

We don't think too much about

the underlying array representation.

So array programming started back in the 70s and 80s

with Fortran and Fortran and ATL

and the modern languages are,

a lot of us are programming in R

and Python and MATLAB.

Other languages, so these are,

so when I say array, I mean,

all of the elements in the array

have the same type and can be

of arbitrary dimension.

So you could have, you know,

five or six dimensional arrays

if you really wanted to,

but more often than not,

we're working with one or two dimensional arrays.

And you can think about scalar values

as being an array that doesn't have any dimension.

It's zero dimensional.

And arrays are important for expressing

batch operations on data.

So when you take a column in a spreadsheet

or a column in a table,

you'd like to be able to express

batch operations on a set of related data points

and that saves you from having to

to write a lot of loops

and end up with very robust code

that involves iterating over

unnecessarily iterating over the data set.

Arrays are also important when you are

slicing and dicing a very large data set

and that you can,

you can just look at a subset of a table

or a subset of an array as a view.

So proper array data structures

enable you to look at,

if you just want to look at, say,

the first hundred thousand rows in a table,

you can construct a view of an array

and express your data operations on that view

without having to copy any data.

So if you're familiar with,

if you're deeply familiar with R or Python or MATLAB,

there are various places where a lot of data gets copied

and that can be a source of slowness in your application.

Of course, most of you are probably familiar

with the data types they're working with.

There's the low level,

numeric data types and strings and dates and times.

Depending on the language that you're working with,

you can also have arrays of arbitrary objects.

You can have arrays of arrays

or arrays of pairs of dates and strings.

So you can have somewhat arbitrary complexity

and representation of the data.

There are a couple of other data types

that I would add to this list.

So one of them is a categorical variable.

So in R, the namespaces are factored.

For many of your big data types,

you can compute a categorical variable,

which is, I guess,

or another name for it is enumeration.

So if you know that you only have a fixed set

of distinct values that occurs in an array,

you can endow it with special properties

such as ordering

or where you can have a more compact representation

of that data.

And that will help you a lot more on down the road

when you're slicing and dicing or aggregating the data.

You can take advantage of that special structure

that you know that you only have

a fixed set of categories in the data.

You can also compute arbitrary structures of these data.

So things like tuples,

you might have a tuple of an integer

and a string and a date,

and that could be defined as a record

or structured data type.

On top of all of this,

and if you've ever spent a lot of time

implementing data tools,

that in reality,

and I guess in real world data,

I find that most data sets that I encounter

have missing values.

And those might be you are parsing a CSV file

and you come to a row

where there's just no values

for certain entries in a row.

And so you need to be able to encode that

and represent it in the data structure

and have a way to fill missing values,

to drop missing values,

to have a core set of operations

that can take into account the missingness of data.

Of course, there are problems with all of this

data type business that you can end up with.

with, I guess I'd say, stuck-in-type soup,

where among integers and floating-point numbers,

there are different kinds of integers,

different kinds of floating-point numbers.

You can represent complex and real numbers.

There are different kinds of strings.

So things can get very complex very fast

if you aren't careful.

And to make matters worse,

when you're actually implementing the algorithms

underlying these things,

there's many different ways

that you can represent the data at the machine level.

But you don't want the user

to have to think about all of this,

that you don't want to,

the person who's writing code,

you don't want them to have to worry about

whether you have a 16-bit unsigned integer

or a signed 32-bit integer.

It represents the quantity,

and you can do numerical operations on it.

That's really the only thing that matters.

But of course, for someone who's implementing these things,

you do have to think about it

because there's memory use considerations

and performance considerations.

So it is a necessary evil in some cases,

but I think that it should be hidden from the end user

to the extent possible.

So on top of arrays and our basic data types,

in the way I find myself

usually working with data in table form,

so here I've got a drawing of what is

sort of a more generalized table.

So you think of a table as just being a list of arrays,

and each array has a fixed data type.

So we can have, one of the arrays can be an integer,

another can be Boolean, another can be string.

A common simplification is that

the table only contains one-dimensional arrays.

So if you're an R programmer and you use DataFrame,

DataFrame is a table that contains all one-dimensional arrays

but you can, in some other areas,

in some other applications like parametrics,

it's very common to work with panels,

which are tables containing two-dimensional arrays.

You can also think about a panel

as being a three-dimensional array,

all of the data have the same type.

You can add an additional layer of metadata

on top of the table by adding row and column labels.

So in this example, the column labels are just integers,

but we could also have information

about what each row in the table represents.

So here I put a simple two-level index,

which turns this table into what would look like

a pivot table in Excel,

or if you have another tool that builds pivot tables.

So you can have a data structure

which represents arbitrarily many layers of labeling.

So here we just have two levels,

where the first four rows of the A level are the A group,

and the first level of the row labels,

and the second level just has the integers one, two, three,

four.

So here's a sort of a real example from Canvas

of a table that has both hierarchical row labels

and hierarchical column labels.

So if we look at the raw data,

these are some aggregated PIP data,

and you can see that in the columns we have days,

and then we have aggregate statistics,

and in the rows we have the time and smoker variables.

And if you define your data structure

with in this very general way as a sequence of arrays

with arbitrary column and row labels,

then having this more complex data structure,

which represents pretty high-dimensional data here,

we've got four layers of labeling,

you can represent it in a tabular format

that can be very nice to work with.

You could also have represented this data

in more of a traditional flat spreadsheet-like form

that could be loaded into a relational database,

and this is also a valid way of storing this data.

But this pivoted format can also be very nice

to work with depending on your application.

Now, of course, you can have all of these

very complex data structures,

but you need to have very, very simple code

to express operations on them.

So there's a big set of data operations

that you can use on tabular data sets,

and I'll talk about a couple of them.

So this is kind of an exhaustive list.

You can do with tables.

So let's just look at a simple example

of table concatenation.

So on the left side here,

I have a set of stock price data

over a set of date,

and on the right, some stock volume data,

and something that you might want to do

is to join together these two data sets

into a single table,

and still be able to distinguish

the price data from the volume data

and refer to Apple's price or a Johnson & Johnson volume.

And we have the additional complexity

that the row labels of the tables are different.

So we also need to introduce some missing data

into the right table

because it doesn't have any data

on the 13th or 14th of September.

So if you were using the pandas library,

you could express this operation

with the function concat,

and I pass a list of the left and the right tables,

and I'm concatenating along axis one,

which is the column, axis zero is the rows.

And then I have this keys argument here,

which says that I want to add

an additional level in the columns

to be able to refer to the two tables

that are being joined together here.

So we end up with this single table,

which now has column labels consisting of

price and volume as the first level,

and the stock tickers as the second level.

And so now we can refer in a simple way

to any individual data point

by either price and volume, stock ticker, and date.

And in the bottom right corner,

you can see that it's introduced

not a number as missing value,

missing value indicators in the table.

Here's another example of a primitive table operation.

So looking back at this joins table

of this price and volume data,

something I might want to do is to do a reshape operation

where I pivot down the price volume level into the rows.

So now I have one column for each stock,

and then two levels of row labeling.

So if you were using pandas, you could type,

I called this variable result,

and I call result stack zero,

which says take the top level of the columns

and rotate that down into the rows,

and that does compute now.

There's two levels of row labeling on the table.

I see a flashing Q&A tab, but nothing's coming up.

So to actually implement these things

is not entirely straightforward,

but at the end of the day,

it comes down to array operations

and moving data around in an efficient way.

And in a lot of cases,

there's one of the most important sets of algorithms

for processing data has to do with set logic,

and that usually involves the use of hash tables and sets.

And the other class of extremely important algorithms

is sorting, and that, you know,

I would say that those two things,

hashing and sorting, as far as implementing data tools,

are two of the most important things

that I utilize on a day-to-day basis.

Another very important area of data analysis is doing group operations, and there's this

fantastic paper by Hadley Wickham. So, if you don't know Hadley, he's an author of many widely

used R packages, in particular ggplot2 for visualization and the reshape2 and flyer packages.

And I love talking to Hadley because he... So, I developed Candace essentially without

looking at Hadley's libraries. And it's interesting to see how we've developed

some of the same design decisions and also some different design decisions.

And looking at each of those design choices, you can certainly... Decisions that Hadley made,

often I'll say, okay, well, that's a better way of doing things. And then we might disagree over

some other particular design choice that I made in Candace or that he made in flyer.

So, a lot of people are doing group operations by writing SQL. So, I put a simple SQL statement

here where we grouped by three keys and aggregated, computed the means of one column and the standard

deviation of another. And this is a very general class of data operations that goes far beyond

databases. It's just a sort of general way of slicing and dicing tabular data.

So, in Candace land, sort of the way I think about grouping and aggregation is in two different

steps. So, first you have a table grouped by a set of keys. So, the keys could be any number

of things. So, often they'll be just column names in the table that you want to use to group it.

You might have data that falls, that came from outside the table, or maybe it's being derived

from data that's in the table. And so, you could have arbitrary arrays that you use to group the

table. Or you might have some complex logic, which is expressed in a function. And the function can

get applied to each row of the table to determine which group each row belongs to. So, once you

describe how you want to group the table, which in the case of an SQL statement will just be a

list of column names, you want to apply a function to it or a set of functions to the column. And

that might be something as simple as you want to compute the mean of one column and the standard

deviation of another column. But there's more complex operations that you can also do.

And so, we would hope that depending on the form of the function or the form of the

aggregation that we get something useful back that we can work with nicely.

So, this is, I guess, a visual representation of how a group by works. So, you have an array of

data and an array of group indicators or group labels. So, we split the data into pieces and

we apply a function, which in this case, in this case, this picture is just a simple aggregation.

And then we combine that together into a final result table or labeled array.

So, here's a more complex operation where I took a, and you probably can't,

as you know, if you can read the table, it's very small on my screen,

where we group the table by a column. And then instead of aggregating, I want to

take each group of data, sort by the values in a particular column, and then select the highest

two values in the, out of each group. So, if we have the raw table on the left,

I grouped by the size column, and then I select the top two. And then the result that we get

is a table that is now labeled by size. So, in this data set, there were only six

values of size. And then for each size, there are two rows that were retrieved from the table.

So, here's another example where instead of grouping by size, we want to first discretize

into two groups, into zero to three and three to six, and then group by those discrete buckets,

and then select out the top, well, here, four values in this case. So, rather than saying,

okay, I want to group by the size column in the table, I'm going to first discretize the

size column with the pandas cut function. And I say, okay, I want to divide into zero to three

and three to six. And then I'm going to group by my discretized size array, and then apply my top

end function and select the top four values from each group. And in doing so, I get back now a

table that is now has two groups, zero to three and three to six, and four, the top four values

for each of those buckets. So, what's going on inside group by, I don't know if you've ever

thought about this, but the first thing that you have to do is identify which group each row in the

table belongs to. And that typically involves taking a column of data, converting it to a

categorical variable, which enumerates the groups and gives you a nice labeling.

If you have multiple key arrays or multiple key columns, the algorithm is a little more

complicated. You have to form tuples as those values and compute a categorical variable off

of those tuples so that you get all of the unique combinations to the key. And then you can either

apply, you can either aggregate the data by doing a scan of the whole table, but for more complicated

analysis, you may need to sort the data into continuous groups and then go through each

chunk of the table and apply the function to it. So, kind of the gory details of what's going on

inside these data algorithms if you're morbidly curious. And you can get extra performance wins

by saving pre-computed values, but if you pre-compute the categorical variables,

that's a lot of the work that needs to be done in a lot of cases.

So, you get things to be fast and from all number of things, and you have to

make all of these, balance all of these considerations and evaluate depending on

your use case how to make things really fast. Choosing the best algorithm, I guess,

I would say is the most important thing, but there are other kinds of considerations like how your

data is laid out in memory, whether in row-oriented fashion or column-oriented fashion.

If you're using an interpreted language like Python, you also have to worry about

the overhead associated with dynamic typing. So, you have little boxes, you can think of them

as wrapping your underlying data. So, if you're doing a lot of data manipulation of box data,

there might be more overhead associated with boxing and unboxing the data

than actually doing the computation. So, in the case of libraries like pandas, the actual

heavy lifting is being done at a lower level and not in the interpreted language.

So, just to also give you a fun example to show that not all algorithms implementations are

created equal. You can all have several implementations of the same algorithm,

and one might be a lot faster than the other just because of how the code is written. So,

I took a very, very simple function that gets used all over the place to computing.

You have an array and you want to compute the unique values that are found in that array,

and this function is found in basically every data analysis language, and I used the test case of

generating a big set of a million integers that only have 10,000 unique values. It should be

used. So, I ran the unique function in R and in NumPy and in pandas and also in Julia.

I was playing around a lot with Julia back in October

and I was curious about this part of it, part of the thing.

And so everybody's implementing the same algorithm

to compute the unique values

and you can see the performance is quite a bit different.

I also noted that the J array language

is able to do this almost an order of magnitude faster

than other languages.

After I gave this talk, I actually dug down

into the J source code to see what's going on.

It turns out, I was a bit sad

when I found out why it's a lot faster.

And it turns out that there's an even better algorithm

for computing unique values of integer arrays

when the range is small.

So if you look at the values first

and see that the values all fall within,

let's say zero to 10,000,

which I think they did in this case,

then you can use a simpler algorithm

that just does a sweep and count.

It doesn't have to use a count,

sort of a, I don't know what the word would be,

counting sort.

It doesn't require using a full blown hash table.

Okay, so I am going to go to a slightly interactive portion

of the webcast and see if I can share my screen.

So let's try this.

So I'm just gonna run through some quick examples.

And these are, this is a data set that's found

that I used in my book.

It's from the USDA and it's a data set

that contains nutrient information about 6,000 foods.

And I've seen a number of different analogies

and visualization involving this data set

recently on the internet.

So basically the data is in JSON,

so I'm loading in the data.

So if you're interested in web visualization,

you end up having to work in JSON most of the time.

So I'm loading the data into Python

with the JSON load function.

And that gives me a list of what represent

JavaScript objects.

And each object is a, you can see is a Python dictionary

that contains metadata about a single food.

So we have a food name, so we have a caraway cheese,

and then a food group, a food ID,

manufacturer if there is one known.

And for each food there's a nested list of nutrients.

So there's, it might be 40 or 50 different nutrients

for each food.

So the major nutrient groups like protein and fat,

but also down into the individual vitamins and minerals

that are found in the food.

So if you wanted to slice and dice

and do some analysis on this data set,

you have to do, I mean, also considering that it is 6,600

at 6,600 foods in the data set.

So it's pretty big, not big data, but it's median data.

So we need to do a little bit of work

so to wrangle this into shape

and then be able to slice and dice it a little bit.

So if we were just looking,

interested in looking at the nutrients for a single food,

I can just take the nutrients for this caraway cheese.

And that gives me a list of Python dictionaries,

which are just little mappings.

And if I pass those, that list of nutrients

to the pandas data frame constructor,

that gives me a,

that gives me back a data frame, which is a table of data.

And here I call the head function,

which gives me the first 10 rows in the data frame.

So you can see there's the food description,

the food group, the units and the number.

I looked at the value here

is the amount per 100 grams of food.

So if we were just looking at a,

just looking at a single food and we wanted to say,

okay, well, how many nutrients

from each nutrient group are there in the data set?

We could look at the group column from the data frame

and you call the value counts method.

And that returns back a labeled array,

which is the pandas series object.

It shows us that there are 54 amino acids, so 42 vitamins.

And you can see all the other food groups that are there.

We could also group by,

things like group by group.

And then let's say we wanted to compute

the mean value by group.

We could then select the value column

and call the mean method.

And then that gives us back an array

containing the two groups

and then mean values for each group.

So if we wanted to do some more analysis overall,

all the foods need to do a bit more work.

So just walk you through this very quickly.

I'm not hoping to teach you pandas for this demo,

just to kind of illustrate the tools a little bit.

So I write out the metadata that I'm interested

in extracting for each food from the database.

And so I pass the whole database

into the DataFrame constructor with those keys.

And that gives me back a DataFrame

with one row for each food,

and just has the food description group and ID.

So I'm going to rename description to food

and group to F group.

So I have a, I write down a mapping of renamings,

and then I use the rename function

to rename the columns with that mapping.

We get back a new table, which has now

food, food group, instead of description and group,

which is more generic.

So here it's more specific.

And then I'm going to iterate through each food,

take the nutrients for each food,

add a column that is the ID for that food group.

So we'll have the same ID in each row

of that nutrient DataFrame.

And then I'm gonna concatenate together

all of those smaller nutrient tables

to create one big, one big nutrient table.

We look at it, it has about 400,000 rows.

And the number of, if we look at the ID column

and compute the unique values of the ID column,

we can see that we have 2,636 foods.

I also noted that in looking at this data set,

that there are some duplicate entries in it,

which is a pretty common kind of thing,

it turns out in practice.

And so we can call the duplicated method,

which examines all of the rows in the data set.

And when we call duplicated,

it gives us back a Boolean array that we can then sum.

And that shows us that there are 14,000 duplicate entries

in the data set.

So it's a pretty unclean data set.

So what we can do is take this duplicated Boolean array,

put minus in front of it, and say nutrients.

So we're taking nutrients

where the nutrient data is not duplicated.

So I'll call this nutrients.

And so I run that.

Yeah, now we have a little smaller data frame.

We could also just use the drop duplicate convenience method.

So I like to have convenience methods.

You could argue that, well, okay,

writing out nutrients, not duplicated,

is not that complicated.

But I like having a simple method,

especially one that can be tag completed

for doing such a common operation as drop duplicate.

So I see nothing particularly wrong with that.

So I'm also going to rename the description

and group columns in this nutrient data.

And now we can merge together the metadata

about the food and then the nutrients

because we added this ID column.

So now we can merge everything together

with the Canvas merge function.

So we're merging nutrients with nutrient metadata

on the ID columns.

We're gonna do an outer join between the two tables.

So we get back now a single data frame.

has all of the data.

So we can do something like compute a cross tabulation of nutrient group and unit to see

how the cross tabulation is just the count.

So when you see a positive value in this table, it's just the number of observations in that

table that are of that pair.

So it turns out that each nutrient group, with the exception of, well, I guess there's

several that have multiple units, but some of them, like amino acids, is only represented

in grams in the data set, for instance.

So if we look at, I just grabbed the position 30,000 row from the table, you can see what

an individual row in the table looks like.

So we have nutrient, nutrient group, food group, and ID and value of units.

So then we can do, potentially, go crazy from here once you know how to use CANDIS.

So suppose that we want us to group by nutrient and food group.

Let's compute the median value for each group in the data.

These are median nutrient densities by nutrient and food group.

And we could just look at, let's say, zinc, and then order by value and make a bar plot.

So we chain together all of these operations.

You can think about, these might be totally foreign to you, but it's nice to be able to

think about each of the data operations.

Here we group, we select a column, we compute median, we select the zinc values, we order

by value, and then we plot.

So it's nice to be able to chain together these operations in a very natural way.

And then we get a plot, and we can see that the highest concentration of zinc is found

in beef products, and there's almost none to be found down in fats and oils and beverages

category.

So a little bit of a vignette of some data tools that I've been involved with building,

but my general philosophy has been that it tries to minimize friction in writing code,

and the code should be as simple as possible for representing state operations.

So the summary I would say here is that, given that there's a shortage of data sciences that

we're hearing a lot about, the main solution to data science's shortage is to make existing

data sciences more productive.

And when you consider that a lot of the headache involved in data analysis has to do with just

cleaning and manipulating and preparing data, we really should be thinking hard about our

tools.

And whenever you run into a problem where you're spending a lot of time doing some manual

cleanup in Excel, or you're having to call somebody to help you out with your analysis,

you think about how could the tools be better, and if you could have that magical one line

of code that does the thing that you need to do with that data.

It's helpful to kind of write that down and think about it.

And if you can't find an R package or a Python package or something in Canvas that does exactly

what you need, to reach out into the community and talk to people and to share your use cases

and problems that you're encountering with your data.

I think the tools, the tools, today's tools can certainly be a lot better than they are

now.

And I'm very excited to see that in the last four or five years, there's been a lot of

progress to make data preparation, data manipulation, data analysis tools a lot more productive.

So, Hadley Wickham in the R community has done amazing things to make working with data

a lot easier with the vshape2 and flyer packages.

And I've sort of been Hadley's counterpart in the Python community with pandas.

My hope would certainly be that in the future, whenever the future gets here, that in any

programming language, because the programming language that you're using may not totally

be up to use, you may not be able to use R, may not be able to use Python.

But I would hope that every language has a core set of structured and semi-structured

data processing tools, so that you can be programming in any language and still express

operations on the data in a very natural way.

And I think the common structures and the ways that the operations that you need to

do on data, I think there's a lot of commonalities that can be built across all languages and

how the API would look if you're programming in Haskell versus programming in C or Python

or R. I think the code may look a bit different, but the basic idea of what you're doing to

the data is going to be very similar from place to place.

And I'm continuing to work on data tooling, and that's kind of in my area of interest,

and I need to see very smart people doing data analysis and finding themselves limited

by the tool.

I am working on a new project, which I hope to talk about more this spring, so I won't

share too much about it in the webcast, but I'm actively working to build better data

tools and make data analysis more productive for more people.

So, thanks very much for listening in.

I share my thoughts occasionally on these topics on Twitter, and there's a very active

community of data analysts and data scientists on Twitter, so if you're not on Twitter,

I would encourage you to join in on the conversation and to find the thought leaders in our space,

Pete Skomorok and Hilary Mason and Josh Wills and sort of people who are really active in

spreading knowledge and what people are doing in data science these days.

So, thanks everyone for listening, and thanks to Accenture, our sponsor.

I guess, Yaz, maybe I'll let you take it over from here.

And as we close the program, we would like to say a very big thank you to Accenture for

sponsoring today's webcast and let you all know that knowledge is key, but knowledge

without insight isn't much of an advantage.

Accenture has more than 257,000 people serving clients in more than 120 countries.

I'm going to push out a little link to you all here so you can download their PDF.

It's a global management consulting, technology services, and outsourcing company that helps

its clients use analytics to turn data into insight, insight into action, and action into

tangible results.

That's high performance delivered.

You can learn more about how Accenture helps its clients navigate and harness the power

of big data by building big data infrastructures.

And here it comes right there on your site, folks.

All right, there's a PDF that they've made available for you.

So, if you want information, please download that.

You can follow up with them there.

Thank you, Accenture.

Thank you, Wes.

Thank you to you all for attending.

This will conclude our webcast today.

Goodbye, everyone.