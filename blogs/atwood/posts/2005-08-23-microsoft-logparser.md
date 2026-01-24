---
title: "Microsoft LogParser"
date: 2005-08-23
url: https://blog.codinghorror.com/microsoft-logparser/
slug: microsoft-logparser
word_count: 695
---

Ask yourself this question: **what if everything could be queried with SLQ? **[Microsoft’s LogParser](http://www.microsoft.com/downloads/details.aspx?FamilyID=890cd06b-abf8-4c25-91b2-f8d975cf8c07&displaylang=en) does just that. It lets you slice and dice a variety of log file types using a common SQL-like syntax. It’s an incredibly powerful concept, and the LogParser implementation doesn’t disappoint. This architecture diagram from the LogParser documentation explains it better than I could:


![](https://blog.codinghorror.com/content/images/2025/05/image-130.png)


The excellent [forensic IIS log exploration with LogParser](https://web.archive.org/web/20060412200206/http://securityfocus.com/infocus/1712) article is a good starting point for sample LogParser IIS log queries. Note that I am summarizing just the SQL clauses; I typically output to the console, so the actual, complete command line would be

kg-card-begin: html

```
logparser “(sql clause)” -rtp:-1

```

kg-card-end: html

Top 10 items retrieved:

kg-card-begin: html

```
SELECT TOP 10 cs-uri-stem as Url, COUNT(cs-uri-stem) AS Hits
FROM ex*.log
GROUP BY cs-uri-stem
ORDER BY Hits DESC

```

kg-card-end: html

Top 10 slowest items:

kg-card-begin: html

```
SELECT TOP 10 cs-uri-stem AS Url, MIN(time-taken) as [Min],
AVG(time-taken) AS [Avg], max(time-taken) AS [Max],
count(time-taken) AS Hits
FROM ex*.log
WHERE time-taken < 120000
GROUP BY Url
ORDER BY [Avg] DESC

```

kg-card-end: html

All Unique Urls retrieved:

kg-card-begin: html

```
SELECT DISTINCT TO_LOWERCASE(cs-uri-stem) AS Url, Count(*) AS Hits
FROM ex*.log
WHERE sc-status=200
GROUP BY Url
ORDER BY Url

```

kg-card-end: html

HTTP errors per hour:

kg-card-begin: html

```
SELECT date, QUANTIZE(time, 3600) AS Hour,
sc-status AS Status, COUNT(*) AS Errors
FROM ex*.log
WHERE (sc-status >= 400)
GROUP BY date, hour, sc-status
HAVING (Errors > 25)
ORDER BY Errors DESC

```

kg-card-end: html

HTTP errors ordered by Url and Status:

kg-card-begin: html

```
SELECT cs-uri-stem AS Url, sc-status AS Status, COUNT(*) AS Errors
FROM ex*.log
WHERE (sc-status >= 400)
GROUP BY Url, Status
ORDER BY Errors DESC

```

kg-card-end: html

Win32 error codes by total and page:

kg-card-begin: html

```
SELECT cs-uri-stem AS Url,
WIN32_ERROR_DESCRIPTION(sc-win32-status) AS Error, Count(*) AS Total
FROM ex*.log
WHERE (sc-win32-status > 0)
GROUP BY Url, Error
ORDER BY Total DESC

```

kg-card-end: html

HTTP methods (GET, POST, etc.) used per Url:

kg-card-begin: html

```
SELECT cs-uri-stem AS Url, cs-method AS Method,
Count(*) AS Total
FROM ex*.log
WHERE (sc-status < 400 or sc-status >= 500)
GROUP BY Url, Method
ORDER BY Url, Method

```

kg-card-end: html

Bytes sent from the server:

kg-card-begin: html

```
SELECT cs-uri-stem AS Url, Count(*) AS Hits,
AVG(sc-bytes) AS Avg, Max(sc-bytes) AS Max,
Min(sc-bytes) AS Min, Sum(sc-bytes) AS TotalBytes
FROM ex*.log
GROUP BY cs-uri-stem
HAVING (Hits > 100) ORDER BY [Avg] DESC

```

kg-card-end: html

Bytes sent from the client:

kg-card-begin: html

```
SELECT cs-uri-stem AS Url, Count(*) AS Hits,
AVG(cs-bytes) AS Avg, Max(cs-bytes) AS Max,
Min(cs-bytes) AS Min, Sum(cs-bytes) AS TotalBytes
FROM ex*.log
GROUP BY Url
HAVING (Hits > 100)
ORDER BY [Avg] DESC

```

kg-card-end: html

There’s an [entire book about LogParser](http://www.amazon.com/exec/obidos/ASIN/1932266526/), and Mike Gunderloy even started an [unofficial LogParser fansite](http://www.logparser.com/).


Here are a few other articles I found that touch on different aspects of LogParser:

- [Graphing PING results](https://web.archive.org/web/20051124060823/http://www.adopenstatic.com/cs/blogs/ken/archive/2005/05/30/22.aspx)
- [Generating XML output and Excel 2003 XML pivots](https://web.archive.org/web/20051122020211/http://www.harper.no/valery/PermaLink,guid,b90858aa-16e9-4a7e-a617-f7edce018250.aspx)
- [Auditing the Event Logs](https://web.archive.org/web/20051104002206/http://www.leastprivilege.com/FunWithLogParser.aspx)
- [Querying an RSS Feed](https://web.archive.org/web/20050829143335/http://www.furrygoat.com/2005/01/logparser_22.html)
- [Professor Windows: How LogParser Works](https://web.archive.org/web/20051102150800/http://www.microsoft.com/technet/community/columns/profwin/pw0505.mspx)


Although LogParser is 96.44% awesome, there are a few things that I didn’t like about it:

1. I really, really need a standard deviation function. Min, Max, and Avg are nice but totally inadequate for determining how variable something is.
2. The graphing output is cool – but it’s also a MS Office dependency. If you try to graph something on a machine without Office installed, you’ll get an error.
3. The automatic detection of column types in CSV files isn’t always reliable. This meant I couldn’t graph some numeric values in my PerfMon dumps because LogParser decided they were strings. I couldn’t find any way to force a column to be detected as a certain type, either.


Of course, the idea of SQL being used to query a bunch of stuff isn’t exactly a new one; Microsoft’s WQL (WMI Query Language) is similar but more annoying and less powerful. And you’ll get tons of hits if you logically extend this concept to querying HTML, too. Just try searching Google for [Web Query Language](http://www.google.com/search?q=web+query+language).

[sql](https://blog.codinghorror.com/tag/sql/)
[microsoft logparser](https://blog.codinghorror.com/tag/microsoft-logparser/)
[log analysis](https://blog.codinghorror.com/tag/log-analysis/)
[data query](https://blog.codinghorror.com/tag/data-query/)
[iis log analysis](https://blog.codinghorror.com/tag/iis-log-analysis/)
