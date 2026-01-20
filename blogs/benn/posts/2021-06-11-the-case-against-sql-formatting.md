---
title: "The case against SQL formatting"
subtitle: "I went looking for the gospel, and lost my religion."
date: 2021-06-11T15:05:46+00:00
url: https://benn.substack.com/p/the-case-against-sql-formatting
slug: the-case-against-sql-formatting
word_count: 1138
---


![](https://substackcdn.com/image/fetch/$s_!_8ED!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ae6f48c-f09a-43d1-9b14-b93a337a825d_1280x582.jpeg)

*How do you solve a problem like Maria DB SQL formatting?*


I’m a man with a short epitaph. If I were to die tomorrow, the best material I’d leave my eulogizers is three shallow scratches I put on strange corners of the internet: A blog post aboutthe price of weed,1an appeal tomove all the driveways in San Francisco, and a sober argument2againstleading commas in SQL queries. “He cared a lot about SQL formatting,” they might say, before butchering apoetry reading:


> And did you get whatyou wanted from this life, even so?I did.And what did you want?...To make an overzealous case against an aesthetically controversial but semantically meaningless tic in the geographic grammar of a half-century old query language for databases. Obviously.


Given that I am, in fact, not dead—and evidently satisfied with this as my legacy—I’ve continued to prosecute this case, and canonize the gospel of proper SQL formatting for future generations.3To this end, I recently made an effort to document the broader set of rules that I follow when I write queries. Here is, in what will surely be a peaceful take, The Answer:


![](https://substackcdn.com/image/fetch/$s_!FV_n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1b83a0c-fe74-4a33-97b5-d13799838629_1328x576.png)


To anyone who disagrees: I will die on these hills. There should be a gutter six spaces in, because it looks nice. SQL keywords are uppercase; table and column names are lowercase.4TheONclauses are on different lines than the joins. The first clause in a join condition (e.g., theainON a = b) references the table in the join, and the second clause references prior tables. Table aliases should be short, initials if possible. And, as should go without saying, select statements use trailing commas.


After easily recording these rules, my review got more complicated. I needed to come up with commandments for SQL’s more sophisticated maneuvers, like case statements and where clauses with parentheses.


It was then that my faith wavered.


What’s the best way to format these parts of a query? The answer—an answer every analyst should love, if not many priests—is thatit depends.Case statements, for example, solve a number of problems, and, as such, come in all sorts of shapes and sizes. There’s simply no format that works for all of them.


That’s because a query doesn’t work just because a computer can execute it; it needs to make sense to both machines andhumans(because it’s people, who do the reading). Readability includes more than aesthetics (though those do matter). Queries—which, above all, transcribe vague business concepts, like revenue andwin rate, into precise formulae—should also make their logic legible. We get frustrated by SQL’scomputational anachronismsbecause they confuse our ability to follow that logic.5Bad formatting can do the same. Good formatting does the opposite: It actually making querieseasierto understand. Formatting is our medium, andthe medium is the message.6


A well-formatted query highlights its important and complex elements while tucking straightforward ideas into the background. Just as data visualizations should be formatted in ways that draw out the salient differences between datasets, queries should do the same for the logical narratives they tell. And just as these differences in datasets are best surfaced by different graphs, different logical structures are best cued by different formats. As query authors, consistency shouldn’t be our goal, no more than we should make it our goal to consistently use bar charts. Instead, our job is to identify the computational studs in our queries, and make those inescapable.


For example, the case statement below is simple, and the field using it isn’t overly important to the query. Inserting a bunch of line breaks gives that field outsized importance—importance that isn’t warranted. In this example, it’s better to keep the case statement all on one line.


![](https://substackcdn.com/image/fetch/$s_!w_nq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd03f6945-6a7f-4e14-8aaf-168421ecc674_1318x366.png)


This next case statement is a long series of if/then statements. Those pairings are the most important thing for the reader to understand. When each logical couple is on the same line, they’re easy to understand. By contrast, a single-line case statement is hard to read, and a case statement that splits the when/then pairs visually mixes the logically different “if” and “then” clauses, breaking the clear path from one to the other.


![](https://substackcdn.com/image/fetch/$s_!DzNR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F977090ae-4537-4697-8414-ea82f4ff7b7f_1326x554.png)


Compare this approach with the more traditional multi-line format.


![](https://substackcdn.com/image/fetch/$s_!ktF-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F682e675f-7653-48fa-8293-1e032193c952_1328x900.png)


In this third example, the case statements are fairly complex, but each one is similar. Rather than follow either of the formats in the prior example, this query should highlight the single critical difference in each case statement. This is best done by leaving each statement on one line, and adding extra space to align each clause. This makes it easy to see the differencesandthe similarities. Splitting out these case statements onto separate lines hides this pattern, forcing readers to unnecessarily parse and compare each statement individually.


![](https://substackcdn.com/image/fetch/$s_!SteM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6a2eea20-1b67-4901-a92a-9fce80e5da6e_1368x226.jpeg)


The “correctly formatted” version, however, is incomprehensible.


![](https://substackcdn.com/image/fetch/$s_!JumL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F67f04d1e-2d1a-4351-b893-ac0e67108213_1322x1206.png)


Moreover, the ideal format for this query might change if there’s only one case statement. In this instance, the important comparison to highlight is within the case statement rather than across different statements.


![](https://substackcdn.com/image/fetch/$s_!CfOO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0261267-4d51-473c-b0ce-1d60c8520cd9_1482x336.jpeg)


The same reasoning applies to other elements in a query. Complex where clauses often have nested AND and OR logic. The best way to format these queries is to position them according to their order of operations, much as you would draw a complex mathematical expression in LaTeX.


![](https://substackcdn.com/image/fetch/$s_!KKw5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc19a8f61-5287-454d-9a0d-f784d8a398c5_1316x322.png)


This approach visually outlines the logic. Standard formatting blurs it.


![](https://substackcdn.com/image/fetch/$s_!VaH6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F26748509-9ea7-4b17-b060-ba348ef6f054_1314x624.png)


True, these examples don’t follow The Rules, at least not rules that can be programmed into a SQL formatter. But our job as query writers isn’t to be mechanical scribes; it’s to format our work so that it’s easy to interpret. In many cases, convention is a helpful escort. But in other cases, an unconventional format makes a query more readable than the style guide. So be it—ignore the guide.


The alternative is dogma. Adherence to a prescription simply because it’s prescribed is to be conformist prude; it’s to disappear behind a linter; it’s to elevate etiquette overcreativity; it’s to judge our work by how little of ourselves is visible in it. It’s believing that Hemingway’s novels would’ve been better if they’d been edited by Grammarly,7or that Ansel Adams’s photos could’ve been improved by torching them with anX Pro IIfilter. Rules, even the best documented and most hallowed ones, are sometimesbest ignored.

[1](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-1-37307127)

I still get emails about this one, so apologies to whoever inherits my Gmail account and has to deal with the occasional stoner turned political science grad student looking for data to determine the relationship between cannabis prices and voter turnout.

[2](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-2-37307127)

Unhinged diatribe.

[3](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-3-37307127)

The Gospel of Join.

[4](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-4-37307127)

To put this in terms that some databases *cough*Snowflake*cough* might understand, TABLE AND COLUMN NAMES ARE LOWERCASE.

[5](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-5-37307127)

Coming this fall, Mem(ento)SQL, the multi-tenetdatabase: A story where everything is out of order and nothing makes sense.

[6](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-6-37307127)

Counterpoint:I know nothing of this work, and the whole fallacy is wrong.

[7](https://benn.substack.com/p/the-case-against-sql-formatting#footnote-anchor-7-37307127)

Or, ironically, theHemingway App.
