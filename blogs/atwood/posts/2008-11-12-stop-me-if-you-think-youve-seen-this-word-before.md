---
title: "Stop Me If You Think You’ve Seen This Word Before"
date: 2008-11-12
url: https://blog.codinghorror.com/stop-me-if-you-think-youve-seen-this-word-before/
slug: stop-me-if-you-think-youve-seen-this-word-before
word_count: 2297
---

If you’ve ever searched for anything, you’ve probably run into [stop words](http://en.wikipedia.org/wiki/Stop_words). **Stop words are words so common they are typically ignored for search purposes**. That is, if you type in a stop word as one of your search terms, the search engine will ignore that word (if it can). If you attempt to search using *nothing* but stop words, the search engine will throw up its hands and tell you to try again.


Seems straightforward enough. But there can be issues with stop words. Imagine, for example, you wanted to search for information on [this band.](http://www.amazon.com/dp/B0000025Z4)


![](https://blog.codinghorror.com/content/images/2025/04/image-227.png)


“The” is one of the most common words in the English language, so a [naïve search for “The The”](http://www.google.com/search?q=the+the) rarely ends well.


Let’s consider some typical English stopword lists.

kg-card-begin: html


| **SQL Server stop words** | **Oracle stop words** |
| 1beforetheseonhim2beingtheyonlyhimself3betweenthisorhis4boththoseotherhow5butthroughourif6bytooutin7cametoooverinto8canunderreis9comeupsaidit0couldusesameitsaboutdidveryseejustafterdowantshouldlikealldoeswassincemakealsoeachwaysomanyanelsewesomemeandforwellstillmightanotherfromweresuchmoreanygetwhattakemostaregotwhenthanmuchashaswherethatmustathadwhichthemybehewhiletheirnever$havewhothemnobecauseherwillthennowbeenherewiththereofwouldyouyour  a b c d e f g h i j k l m n o p q r s t u v w x y z | 1 | before | these | on | him | 2 | being | they | only | himself | 3 | between | this | or | his | 4 | both | those | other | how | 5 | but | through | our | if | 6 | by | to | out | in | 7 | came | too | over | into | 8 | can | under | re | is | 9 | come | up | said | it | 0 | could | use | same | its | about | did | very | see | just | after | do | want | should | like | all | does | was | since | make | also | each | way | so | many | an | else | we | some | me | and | for | well | still | might | another | from | were | such | more | any | get | what | take | most | are | got | when | than | much | as | has | where | that | must | at | had | which | the | my | be | he | while | their | never | $ | have | who | them | no | because | her | will | then | now | been | here | with | there | of | would | you | your |  |  | a b c d e f g h i j k l m n o p q r s t u v w x y z | aheoutupbemoretheirathadonewillfromitthanandisonlywhencorpnotshealsoinsayswasbymstoaboutherover becausemostthere hasorwith itsthatare ofwhichcould someaninc wecanmz afterhiss beenmrthey haveotherwould lasttheas onwhofor suchanyinto werecono allifso butmrsthis | a | he | out | up | be | more | their | at | had | one | will | from | it | than | and | is | only | when | corp | not | she | also | in | says | was | by | ms | to | about | her | over |  | because | most | there |  | has | or | with |  | its | that | are |  | of | which | could |  | some | an | inc |  | we | can | mz |  | after | his | s |  | been | mr | they |  | have | other | would |  | last | the | as |  | on | who | for |  | such | any | into |  | were | co | no |  | all | if | so |  | but | mrs | this |  |
| 1 | before | these | on | him |
| 2 | being | they | only | himself |
| 3 | between | this | or | his |
| 4 | both | those | other | how |
| 5 | but | through | our | if |
| 6 | by | to | out | in |
| 7 | came | too | over | into |
| 8 | can | under | re | is |
| 9 | come | up | said | it |
| 0 | could | use | same | its |
| about | did | very | see | just |
| after | do | want | should | like |
| all | does | was | since | make |
| also | each | way | so | many |
| an | else | we | some | me |
| and | for | well | still | might |
| another | from | were | such | more |
| any | get | what | take | most |
| are | got | when | than | much |
| as | has | where | that | must |
| at | had | which | the | my |
| be | he | while | their | never |
| $ | have | who | them | no |
| because | her | will | then | now |
| been | here | with | there | of |
| would | you | your |  |  |
| a b c d e f g h i j k l m n o p q r s t u v w x y z |
| a | he | out | up |
| be | more | their | at |
| had | one | will | from |
| it | than | and | is |
| only | when | corp | not |
| she | also | in | says |
| was | by | ms | to |
| about | her | over |  |
| because | most | there |  |
| has | or | with |  |
| its | that | are |  |
| of | which | could |  |
| some | an | inc |  |
| we | can | mz |  |
| after | his | s |  |
| been | mr | they |  |
| have | other | would |  |
| last | the | as |  |
| on | who | for |  |
| such | any | into |  |
| were | co | no |  |
| all | if | so |  |
| but | mrs | this |  |


kg-card-end: html

You’d think a pure count of frequency, how often the word occurs, would be enough to make a common group of words “stop words,” but apparently not everyone agrees. The default SQL Server stop word list is much larger than the Oracle stop word list. What makes **“many”** a stop word to Microsoft, but not to Oracle? Who knows. And I’m not even going to show the MySQL full [text search stop word list](http://dev.mysql.com/doc/refman/5.0/en/fulltext-stopwords.html) here, because it’s *enormous*, easily double the size of the SQL Server stop word list.


These are just the default stop word lists; that doesn’t mean you’re stuck with them. You can edit the stop word list for any of these databases. Depending on what you’re searching, you might decide to have different stop words entirely, or maybe no stop words at all.


Way back in 2004, I ran a little experiment with Google – over a period of a week, **I searched for an entire dictionary of ~110k individual English words and recorded how many hits Google returned for each**.


Yes, this is probably a massive violation of the Google terms of service, but I tried to keep it polite and low impact – I used Gzip compressed HTTP requests, specified only 10 search results should be returned per query (as all I needed was the count of hits), and I added a healthy delay between queries so I wasn’t querying too rapidly. I’m not sure this kind of experiment would fly against today’s Google, but it worked in 2004. At any rate, I **ended up with a MySQL database of 110,000 English words and their frequency in Google as of late summer 2004**. Here are the top results:

kg-card-begin: html


| the522,000,000of515,000,000and508,000,000to507,000,000in479,000,000for468,000,000internet429,000,000on401,000,000home370,000,000is368,000,000by366,000,000all352,000,000this341,000,000with338,000,000services329,000,000about319,000,000or317,000,000at316,000,000 | the | 522,000,000 | of | 515,000,000 | and | 508,000,000 | to | 507,000,000 | in | 479,000,000 | for | 468,000,000 | internet | 429,000,000 | on | 401,000,000 | home | 370,000,000 | is | 368,000,000 | by | 366,000,000 | all | 352,000,000 | this | 341,000,000 | with | 338,000,000 | services | 329,000,000 | about | 319,000,000 | or | 317,000,000 | at | 316,000,000 | email311,000,000from308,000,000are306,000,000website302,000,000us301,000,000site283,000,000sites279,000,000you276,000,000information276,000,000contact274,000,000more271,000,000an271,000,000search269,000,000new269,000,000that267,000,000your262,000,000it261,000,000be258,000,000 | email | 311,000,000 | from | 308,000,000 | are | 306,000,000 | website | 302,000,000 | us | 301,000,000 | site | 283,000,000 | sites | 279,000,000 | you | 276,000,000 | information | 276,000,000 | contact | 274,000,000 | more | 271,000,000 | an | 271,000,000 | search | 269,000,000 | new | 269,000,000 | that | 267,000,000 | your | 262,000,000 | it | 261,000,000 | be | 258,000,000 | prices258,000,000as255,000,000page246,000,000hotels240,000,000products234,000,000other222,000,000have219,000,000web219,000,000copyright218,000,000download218,000,000not214,000,000can209,000,000reviews209,000,000our206,000,000use205,000,000women200,000,000 | prices | 258,000,000 | as | 255,000,000 | page | 246,000,000 | hotels | 240,000,000 | products | 234,000,000 | other | 222,000,000 | have | 219,000,000 | web | 219,000,000 | copyright | 218,000,000 | download | 218,000,000 | not | 214,000,000 | can | 209,000,000 | reviews | 209,000,000 | our | 206,000,000 | use | 205,000,000 | women | 200,000,000 |
| the | 522,000,000 |
| of | 515,000,000 |
| and | 508,000,000 |
| to | 507,000,000 |
| in | 479,000,000 |
| for | 468,000,000 |
| internet | 429,000,000 |
| on | 401,000,000 |
| home | 370,000,000 |
| is | 368,000,000 |
| by | 366,000,000 |
| all | 352,000,000 |
| this | 341,000,000 |
| with | 338,000,000 |
| services | 329,000,000 |
| about | 319,000,000 |
| or | 317,000,000 |
| at | 316,000,000 |
| email | 311,000,000 |
| from | 308,000,000 |
| are | 306,000,000 |
| website | 302,000,000 |
| us | 301,000,000 |
| site | 283,000,000 |
| sites | 279,000,000 |
| you | 276,000,000 |
| information | 276,000,000 |
| contact | 274,000,000 |
| more | 271,000,000 |
| an | 271,000,000 |
| search | 269,000,000 |
| new | 269,000,000 |
| that | 267,000,000 |
| your | 262,000,000 |
| it | 261,000,000 |
| be | 258,000,000 |
| prices | 258,000,000 |
| as | 255,000,000 |
| page | 246,000,000 |
| hotels | 240,000,000 |
| products | 234,000,000 |
| other | 222,000,000 |
| have | 219,000,000 |
| web | 219,000,000 |
| copyright | 218,000,000 |
| download | 218,000,000 |
| not | 214,000,000 |
| can | 209,000,000 |
| reviews | 209,000,000 |
| our | 206,000,000 |
| use | 205,000,000 |
| women | 200,000,000 |


kg-card-end: html

Again, a very different list than what we saw from SQL Server or Oracle. I’m not sure why the results are so strikingly different. Also, the web (or at least Google’s index of the web) is much bigger now than it was in 2004; [a search for “the”](http://www.google.com/search?q=the) returns 13.4 *billion* results – that’s 25 times larger than my 2004 result of 522 million.


On Stack Overflow, **we warn users via an AJAX callback when they enter a title composed entirely of stop words**. It’s hard to imagine a good title consisting solely of stopwords, but maybe that’s just because our technology stack isn’t sufficiently advanced yet.


Google doesn’t seem to use stop words any more, as you can see from [this search ](http://www.google.com/search?q=to+be+or+not+to+be)for “to be or not to be.”


![](https://blog.codinghorror.com/content/images/2025/04/image-226.png)


**Indeed, I wonder if classic search stop words are relevant in modern computing**; perhaps they’re a relic of early 90’s computing that we haven’t quite left behind yet. We have server farms and computers perfectly capable of handling the extremely large result sets from querying common English words. A Google patent filed in 2004 and granted in 2008 seems to argue against [the use of stop words](http://www.seobythesea.com/?p=1109).


> Sometimes words and phrases that might be considered stopwords or stop-phrases may actually be meaningful or important. For example, the word “the” in the phrase “the matrix” could be considered a stopword, but someone searching for the term may be looking for information about the movie “The Matrix” instead of trying to find information about mathematical information contained in a table of rows and columns (a matrix).
> A search for “show me the money” might be looking for a movie where the phrase was an important line, repeated a few times in the movie. Or a search for “show me the way” might be a request to find songs using that phrase as a title from Peter Frampton or from the band Styx.
> A Google patent granted this week explores how a search engine might look at queries that contain stopwords or stop-phrases, and determine whether or not the stopword or stop-phrase is meaningful enough to include in search results shown to a searcher.


Apparently, at least to Google, stop word warnings are a thing of the past.

[stop words](https://blog.codinghorror.com/tag/stop-words/)
[search engine optimization](https://blog.codinghorror.com/tag/search-engine-optimization/)
[search algorithms](https://blog.codinghorror.com/tag/search-algorithms/)
[information retrieval](https://blog.codinghorror.com/tag/information-retrieval/)
[stopwords](https://blog.codinghorror.com/tag/stopwords/)
[search terms](https://blog.codinghorror.com/tag/search-terms/)
