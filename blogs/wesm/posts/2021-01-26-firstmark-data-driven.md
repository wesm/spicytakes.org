---
title: "Fireside Chat with Matt Turck"
summary: "Interview at Data Driven NYC"
date: 2021-01-26T00:00:00
tags: ["interview", "transcript"]
slug: firstmark-data-driven
word_count: 4462
source_file: transcripts/2021-01-26-firstmark-data-driven.md
content_type: transcript
event: "Data Driven NYC"
video_url: "https://www.youtube.com/watch?v=382Ed-0bX2g"
---

{{< video https://www.youtube.com/watch?v=382Ed-0bX2g >}}

*This transcript and summary were AI-generated and may contain errors. [Original post on mattturck.com](https://www.mattturck.com/mckinney)*

## Summary

In this fireside chat with Matt Turck at Data Driven NYC, I discuss the origins and impact of pandas, the motivation behind Apache Arrow, and my transition from Ursa Labs to Ursa Computing.

On pandas: I describe it as a "swiss army knife" for data access, manipulation, analytics, and visualization in Python. I estimate that more than 90% of structured tabular data processing in Python passes through pandas at some point. The project now has over 2,000 contributors, though I haven't been actively involved in development for almost eight years. It has become a model for community-governed open source without a major corporate sponsor.

On why Python became the dominant data language: It wasn't predetermined or inevitable. A small group of open source developers built essential projects - NumPy for array computing, pandas for data manipulation, scikit-learn for machine learning, IPython/Jupyter for the interface, and visualization tools. This "perfect storm" enabled complete workflows. Python also let companies move from research to production quickly, which mattered as startups raced to extract value from smartphone and mobile data.

On Arrow's origins: Around 2015, there was a collective realization that the data ecosystem faced a "grand data interchange and data interoperability crisis." Different groups had built incompatible computing engines, file formats, and data lakes. Hardware was getting faster, but we were bottlenecked by the cost of moving and converting data. I wanted to build bridges from Python to other systems. We got 20-25 people from Cloudera, Hortonworks, Dremio, Twitter and others to agree on building one common solution instead of 14 incompatible standards.

On why ODBC/JDBC are inadequate: I use the analogy of "drinking a thick milkshake through a straw that's too small." These protocols were never designed for bulk data transfer at the gigabyte scale. They're row-oriented, creating a conversion penalty when moving to column-oriented tools like pandas.

On Arrow's value proposition: Arrow is a language-independent, column-oriented data format for both bulk transport and analytics. Data arrives ready for processing without conversion. Snowflake, BigQuery, and Microsoft now support Arrow export. Rather than each vendor building custom pandas connectors, they export to Arrow and we maintain the Arrow-to-pandas bridge.

On the Ursa Labs to Ursa Computing transition: After Arrow started in 2016, I moved to Two Sigma, who recognized its value for their petabytes of data. Companies worldwide wanted to fund Arrow development, so we created Ursa Labs as an industry consortium - hosted by RStudio - where multiple corporations could fund work and have input on priorities without any single company controlling the project. After two years, with only six full-time developers struggling to keep up with bug reports and features, it became clear we needed commercial resources. We spun out Ursa Computing, raised a round led by GV, while maintaining a labs team focused 100% on open source.

On Arrow vs. Databricks/Delta: Arrow is strictly complementary. Spark uses Arrow as an interchange format, especially for Python and R interfaces. Arrow enhances interoperability with Parquet, which is central to the Databricks platform.

On the future of parallel compute: Hardware acceleration is essential - NVIDIA's RAPIDS team uses Arrow as the foundation for GPU analytics, showing significant benchmark improvements with lower power consumption. We need computing engines that scale efficiently at the single-node level, plus quality distributed schedulers like Ray and Dask. Spark's weakness is that it fails to shrink down effectively - using Spark as a pandas alternative via Koalas is often slower than pandas, which isn't impressive.

## Key Quotes

> "Pandas serves sort of as a Swiss Army knife for data access, data manipulation, analytics, and data visualization in Python." — Wes McKinney

> "More than 90% of the data that's coming into structured data processing in the Python ecosystem, tabular data processing, is passing through pandas at some point in its lifetime." — Wes McKinney

> "It certainly wasn't clear - it wasn't predetermined or inevitable that Python was going to become the number one data language that it is today." — Wes McKinney

> "Without scikit-learn, without pandas, without NumPy, it just wouldn't have. I think people would have had to go elsewhere. I don't know what the world would look like, but it would be different." — Wes McKinney

> "The entire data ecosystem was facing this grand data interchange and data interoperability crisis." — Wes McKinney

> "It's kind of like - as a user of these tools, you have this feeling of drinking a thick milkshake through a straw that's too small. You're just trying really hard to extract the data out of the database so that you can do work on it, but you end up bottlenecked on just the transfer." — Wes McKinney

> "Arrow removes the need for that conversion. So aside from transporting bytes over the network, the data is essentially ready for analysis as soon as it gets into your hands." — Wes McKinney

> "It was definitely serendipitous, but it was also a lot of hard labor to be able to get so many people to agree with each other to build one thing, as opposed to 14 different incompatible 'quote unquote' standards." — Wes McKinney

> "One of the things that you find with things like Spark is that they fail to shrink down and effectively do computing at the single-node scale." — Wes McKinney

## Transcript

**Matt Turck:** I'd love to start with pandas actually, which is like your original baby. I think it'd be super interesting for the folks that aren't familiar with pandas to hear about it. So I guess, what is it?

**Wes McKinney:** So pandas serves sort of as a Swiss Army knife for data access, data manipulation, analytics, and data visualization in Python. I often tell people it's one of the primary on-ramps for data into the Python ecosystem. Whether you're reading data out of CSV files or other kinds of data files, or reading data out of databases - it's hard to estimate, but I'd say more than 90% of the data that's coming into structured data processing in the Python ecosystem, tabular data processing, is passing through pandas at some point in its lifetime. And so it's become, after NumPy for array computing in Python, the most widely used Python package for data.

**Matt Turck:** Yeah, I was reading recently - so you have literally millions of users but also like 500 contributors or more than 500... I'm sorry, thousands of contributors, right, for pandas?

**Wes McKinney:** Yeah, I know there have been well over 2,000 contributors at this point. And I haven't been actively involved in the development of the project for almost eight years now, but the project is almost 13 years old. So I worked really actively on it for about five years - a couple years in closed source and then a few years in open source, while also writing my book, which is largely about pandas. But it's really flourished and been a model for a community-governed open source project. Pandas never really had a significant corporate sponsor who was putting in the majority of contributions - it really was a community project almost from the get-go.

**Matt Turck:** Wonderful. And to make this even more approachable to folks that may not spend that much time in the industry - a lot of energy is spent talking about machine learning, AI, and all the things. But ultimately what a lot of data analysis and data scientist people do is they spend a tremendous amount of their time getting the data ready for machine learning and AI. And this is where pandas plays such an important role in accelerating and facilitating that first step, right? Is that correct?

**Wes McKinney:** Yeah. So people use it for not only loading the data into Python but also the data cleaning - what we call data preparation. They use it to do feature engineering, extracting features from data sets, and all of that munging and data work that's needed before you can feed the data into a machine learning model - TensorFlow, scikit-learn, what have you. Because data is largely pretty messy, and so you have to do... people report spending 80% or more of their time doing data cleaning, and they spend comparatively less time actually doing the science part of data science.

**Matt Turck:** And still in an effort to make this educational, do you want to talk about data structures in the context of pandas? In particular, there's a term that comes back a lot, which is DataFrame. Do you want to explain what it is?

**Wes McKinney:** Yeah. So DataFrame is a term that arose originally in the R programming language, which was based on the S and S-Plus programming languages. But a DataFrame basically means a table. And I guess we could call it a table and it would mean the same thing, but the term DataFrame has - at least in popular understanding - become this idea of a style of programming interface for working with tabular data sets that's imperative. So you can write for loops, you can step outside the bounds of what you could do in the SQL query language. It tends to be interactive, very flexible, and enables you to work with data sets from a general purpose programming language like Python. In pandas, DataFrame is the name of the main table object. It's a collection of columns, and so most of the time people are working with either a collection of DataFrames or columns from DataFrames, which are called Series. So when you read a CSV file, it comes into Python as a pandas DataFrame.

**Matt Turck:** And all of this is in the context of the Python world. Especially when you started all of this, it wasn't super clear that Python was going to be the dominant language for data analysis and data science. But it seems to be very much the case now. Why do you think that happened? And do you think that's a permanent state, or could other languages emerge?

**Wes McKinney:** It certainly wasn't clear - it wasn't predetermined or inevitable that Python was going to become the number one data language that it is today. I think a part of that was a relatively small group of very passionate open source developers building the essential projects which enabled the people who are now called data scientists to do complete workflows in Python. We needed the array computing that you have in NumPy, we needed the tabular data manipulation, data cleaning, data loading that you have in pandas, we needed to be able to do machine learning - that came from scikit-learn, which was developed around the same time. We needed a nice user interface, a programming environment - that came from IPython and the Jupyter project. We needed to be able to visualize data. So it was kind of this perfect storm of these different tools coming together and enabling a productive workflow.

I think another thing that was a catalyst for Python was the fact that so many companies were started to get value out of all of the new data that was being generated by smartphones and by mobile browsing. The time to market and the speed at which you could develop systems that created actionable insights on data, production systems that would deliver model predictions and different things - you needed to be able to build those systems and get them to market really quickly. The fact that you could use Python as the language not only of your research and exploratory computing, but then you could also build production systems and put them out there in the cloud - that was very compelling. You could hand somebody a book about Python, they could become productive and start writing useful code within hours or days. So it was really about that rapid prototyping and the research-to-production lifecycle that enabled Python to become what it is today.

But certainly without that perfect storm of open source projects, it just wouldn't have happened. Without scikit-learn, without pandas, without NumPy, it just wouldn't have. I think people would have had to go elsewhere. I don't know what the world would look like, but it would be different.

**Matt Turck:** Your focus for the last few years has been Arrow. When and how did that start?

**Wes McKinney:** I would describe it as this collective realization in the 2015 timeframe that the entire data ecosystem was facing this grand data interchange and data interoperability crisis. That's partly because there were all these different independent groups of people that built different computing engines, data processing systems. There were a lot of different file formats. There was the cloud - people were starting to build the first data lakes in the cloud. And so there was all this angst about how do we move data and transport data between different systems, how do we get access to all these different data formats efficiently.

All that being said, the hardware underneath our feet - disk drives, networking, everything - was getting a lot faster. And so we found ourselves really limited and held back by the speed of getting access to data and the costs associated with moving data around.

I was at Cloudera at the time, and I was interested in this problem. I experienced it from the perspective of pandas and the Python ecosystem - wanting to build bridges from Python into all of these other systems. And so we started... folks from Cloudera, people from the Impala team, from the Kudu team, they'd worked with Julian LeDem at Twitter on Parquet. Julian was now at Dremio. So we kind of very quickly got all these companies together - Cloudera, Hortonworks, Dremio, Twitter folks, and a bunch of others. There were eventually 20 or 25 of us in the room saying, "Hey, this is a really important problem. We need to create a cohesive solution to data interoperability and data interchange that we can all use and that will meet all these diverse needs and make some of the pain go away."

It was definitely serendipitous, but it was also a lot of hard labor to be able to get so many people to agree with each other to build one thing, as opposed to 14 different incompatible "quote unquote" standards.

**Matt Turck:** And to double-click on the problem - is it fair to say on one side you have the world of databases and data warehouses, and that's the world of SQL? And then on the other side you have the world of machine learning and data analysis tools, which is like Spark and NumPy and so on and so forth - and that's Python. Those two worlds did not communicate?

**Wes McKinney:** Yeah, I mean, that's the thing. That was one of the things that was most painful for me - the fact that you had all this really sophisticated, scalable data processing technology that was being created in the big data world or in the analytic database world. And I had come from the data science ecosystem, from Python, and we were off on our own, completely working by ourselves, building everything from scratch. So there was very little cross-pollination between the database, scalable data processing world and the data science world.

For me, one of the primary motivators was to create a technology which could proverbially tie the room together and enable that cross-pollination between database developers and data science developers - that had just never existed because there was nothing productive to collaborate on until that point.

**Matt Turck:** Why is it so hard to extract data from a database? Can't you just use an ODBC/JDBC connector, you get the data out, and you're done?

**Wes McKinney:** We could spend 20 minutes or an hour just talking about this. There's many problems. Part of the problem is that the way that people consume the results of database queries is so diverse. Not everything is a DataFrame library or an analytical tool.

So protocols, interfaces like ODBC and JDBC, were never designed or intended for bulk data transfer - on the order of gigabytes, for example. They are best used for relatively small amounts of data that are the results of database queries. All the work happens in the database, the results are relatively small, and they come into your application through something like ODBC or JDBC.

They're also row-oriented interfaces, which makes them an awkward fit when you need to convert to a column-oriented tool like pandas. And so there's just all this impedance, this conversion penalty, going from things like ODBC into pandas.

It's kind of like - as a user of these tools, you have this feeling of drinking a thick milkshake through a straw that's too small. You're just trying really hard to extract the data out of the database so that you can do work on it, but you end up bottlenecked on just the transfer. Because databases aren't designed for that - they want you to do all of the processing within their walls.

**Matt Turck:** So how does Arrow work, and how does it solve the problem?

**Wes McKinney:** We designed a language-independent, standardized data format that is column-oriented, that can be used for bulk data movement and data transfer, but that is also an efficient data format for doing analytics. So if you get a bunch of Arrow data out of a processing system, out of a database, into memory, you can immediately go to work doing further data processing on it without a need to convert it into some other data format.

Traditionally, data comes into your Python interpreter, into your R interpreter, your process, and you immediately have to convert it into some other format. Arrow removes the need for that conversion. So aside from transporting bytes over the network, the data is essentially ready for analysis as soon as it gets into your hands.

**Matt Turck:** And again, to reiterate for folks - this is a very big deal. And correct me if I'm wrong, Wes - I'm going on a little bit of a limb here - but the world of data keeps talking about Snowflake and the data warehouses, and there's considerable amounts of tweets and articles and all those things, and then also machine learning. But effectively, doing machine learning on top of Snowflake is incredibly hard - not because the machine learning is complicated or not because Snowflake doesn't work, but because the core problem is the movement of data. And it's incredibly complicated and expensive and time-consuming to do this. So Arrow has a very strategic place in the ecosystem in that it precisely enables all these pieces to work together.

So just to reiterate - precisely to this point about data warehouses, what's the status of the integration with Snowflake or BigQuery or others?

**Wes McKinney:** That's been one of the most successful use cases for the project - as a standard medium or data format for bulk interchange with data warehouse systems. So Snowflake supports exporting query results to Arrow format. So does BigQuery. Microsoft has a number of internal projects in their cloud infrastructure for direct-to-Arrow export.

Part of what's motivated the data warehouses to support Arrow is because we built a really efficient bridge between Arrow and pandas. If their goal is to get gigabytes of data out of their data warehouses into the hands of data scientists, rather than building a custom connector that they have to design themselves and build and maintain and optimize, they can go through Arrow. They have one thing to think about. So they get access to all of this ecosystem of tools that now support Arrow after five years of development work.

That makes things much simpler for the data warehouse vendors - they have one thing to support. And we can, on the Python side, deal with "Okay, I know how to optimize getting data into pandas" - so we can maintain that for them, and their developers don't have to solve that problem themselves.

I think in the course of the next few years, pretty much every database system, every data warehouse is going to support Arrow-based import and export in some format. And that's exactly what we want - that's precisely the purpose of the project, to have this common, standardized, efficient interchange format. So it's really just a big, major development that was very difficult to achieve.

**Matt Turck:** Let's talk about Ursa a little bit. You first started this as a non-profit entity with an interesting model, and then as mentioned at the beginning, you either switched or added a commercial entity to this. Do you want to talk about those?

**Wes McKinney:** Yeah. The backstory is - 2016, Arrow started. I moved from Cloudera to Two Sigma. Two Sigma recognized the value of Arrow pretty much immediately, as they have petabytes and petabytes of data. They said, "Make Python work better with all of this big data. We'll let you work on it here."

But then pretty quickly, all around the world, companies began to realize how much of a big deal Arrow was, and they all wanted to fund the development. I had all these companies coming to me saying, "Hey Wes, can you come work here? You can work on Arrow, but we want you to solve our problems."

So initially, Ursa Labs was created as effectively an industry consortium to enable many corporations to fund Arrow development work and have a seat at the table, to have regular syncs with me and my team so we could make sure we were hearing their concerns and prioritizing the important parts of the development roadmap - but we weren't beholden to any single company and any single company's needs.

RStudio was very gracious to provide a home for Ursa Labs and a lot of the - the majority or plurality of - the funding for the work. After a little more than two years of non-profit Ursa Labs work, it became clear to me and to many people that to have more of a commercial engine behind Arrow and the Arrow ecosystem was important for enabling the ecosystem to continue to grow, for us to be able to pour a lot more resources into the open source project.

As of the summer, we were six full-time developers, and even with six full-time people working on the project, our hands were completely full with bug reports and trying to build features and keeping the community growing and healthy. So the writing was on the wall that we needed to think about product development for Arrow and for the data science ecosystem as it relates to Arrow, and to be able to invest more in the maintenance and growth of the Apache Arrow project itself.

**Matt Turck:** And Ursa Computing is going to be the commercial version of this?

**Wes McKinney:** Yeah, so we spun the Ursa Labs team out of RStudio and folded the labs team into a new company, Ursa Computing. We continue to have a labs team which focuses 100% on the open source development, and we're hiring and expanding that labs team. The new company, Ursa Computing, raised a venture round led by GV, and we'll be developing some commercial offerings to accelerate data science use cases - they're all powered by the core computing technology that we're creating in the Arrow project.

**Matt Turck:** Okay, very good. All right, just a couple of questions from the audience, and then we'll switch to Julia and DataKin. Let's see - this is a question from Ragu: How is Arrow leveraged or compared with Databricks' product stack, Delta format, Delta engine?

**Wes McKinney:** It's neither a competitor nor a replacement - it's strictly a complementary technology. Spark supports Arrow as an interchange format. It's used heavily in the interface with Python and R, for example. I'm not up to date on what else Databricks has done to interoperate with Arrow, but I know that they're an active user of Apache Arrow in the Delta Lake Python interface, in Spark core itself, and probably in other parts of Databricks that I'm not aware of. So Arrow essentially enhances interoperability with file formats like Parquet, which are an essential part of the Databricks platform.

**Matt Turck:** And one last question from Joshua Bloom - if we're talking about... Joshua, former speaker at this event... sort of a more broad industry question: After HPC, Hadoop, Spark, Ray - what's the long-term future of parallel compute for data-intensive workflows? What are the key innovations needed? Is it the hardware, is it data center architecture, software platforms, algorithmic? What's your overall take on the future of parallel compute for data-intensive workflows?

**Wes McKinney:** I think that hardware acceleration and leveraging advances in modern hardware is absolutely essential. The folks from NVIDIA have a large team building the RAPIDS project, which is CUDA-based computing against Arrow data. They've been able to basically smash big data, large-scale big data benchmarks on big appliances which are full of NVIDIA GPUs - providing faster performance and lower TCO over alternative solutions that don't leverage that kind of hardware acceleration.

I think it's important that we develop computing engines that very effectively scale up at the single-node scale, and that we build really flexible and high-quality distributed schedulers which enable us to take those efficient single-node computing systems and distribute and scale them on large data sets. You're seeing that trend with projects like Ray and Dask, which provide general-purpose distributed schedulers for single-node computing systems.

But I think one of the things that you find with things like Spark is that they fail to shrink down and effectively do computing at the single-node scale. You can use Spark at the single-node scale as an alternative to pandas through the Koalas interface, but you'll find that for many workloads it's simply slower than pandas - which is not super impressive.

So I think we need to innovate on distributed computing, hardware acceleration, single-node computing... we have a lot of work to do. I think the next decade is going to be really exciting as these pieces begin to come together.

**Matt Turck:** Wonderful. Perfect way to end it. I really appreciate it, Wes. This was wonderful. Congratulations on all the success with all of this, and really appreciate you stopping by Data Driven NYC.

**Wes McKinney:** Thanks Matt. Great to see you as always.

**Matt Turck:** Thanks Wes.