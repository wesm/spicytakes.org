---
title: "Migrate from Oracle to Microsoft (Views) â Part III"
date: 2016-09-24
url: https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-iii/
slug: migrate-from-oracle-to-microsoft-views-part-iii
word_count: 592
---

![Migrate from Oracle to Microsoft (Views) â Part III](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-iii/images/microsoft-sql-server-vs-oracle.jpg)

Contents

Continued from [Migrate from Oracle to Microsoft (Views) â Part II](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-ii/) here part III withÂ the main focus on very interesting topic testing 😉.


## Testing


When I implemented all about 20 views from Oracle to SQL Server, I had to test the performance and not least important, the content of the views if their still contain the same. And how do you do that the easiest way?


### Measure performance


For measuring the performance you simply select alls Views with a SELECT COUNT(*) on both databases. Don’t forget to clear the cache before each run.

To generate all the COUNT-Statements I created a little script, just to make life easier right ;-):



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
` | `--Generate Queries - Performance Test...
SELECT  v.TABLE_NAME,
		--stuff(c.list,1,1,'') as cols,
		'PRINT ''' + v.Table_name + '''    ' +
		'SELECT '''+v.Table_name+''' as Tbl_name, NULL as cnt UNION ALL ' +
		'SELECT '''+v.Table_name+''' as Tbl_name, count(*) as cnt FROM [dbo].['+v.Table_name +'] '--WHERE 1=2 '
		+ CHAR(13)+CHAR(10)

  FROM INFORMATION_SCHEMA.VIEWS v
  --where v.TABLE_NAME LIKE '%What you like%'
 ORDER BY v.TABLE_NAME


--To the generated output you just add below in front and you're ready to go:
SET STATISTICS TIME ON

PRINT 'My_View'    SELECT 'My_View' as Tbl_name, NULL as cnt UNION ALL SELECT 'My_View' as Tbl_name, count(*) as cnt FROM [dbo].[My_View]
...
` |



### Compare content

1. First you create a database linked server on your SQL Server database. If you don’t know how to do this, please read the following [How-to](https://blogs.msdn.microsoft.com/dbrowne/2013/10/02/creating-a-linked-server-for-oracle-in-64bit-sql-server/).
2. If you have only a few comparison you easily create EXCEPT-SELECT-Query and compare your Oracle Views over the database link (linked-Server) to your Microsoft Views.



| ` 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
` | `--Generate Queries - MINUS-Query...
SELECT  v.TABLE_NAME,
		--stuff(c.list,1,1,'') as cols,
		'SELECT '''+v.Table_name+''' as Tbl_name, NULL as cnt, ' + stuff(c_null.list,1,1,'') +
		' UNION ALL ' +
		'SELECT '''+v.Table_name+''' as Tbl_name, count(*) as cnt, '+ stuff(c_null.list,1,1,'') +  ' FROM [LinkedServerName]..[SchemaName].['+v.Table_name +'] ' + --' WHERE 1=2 '+
		' EXCEPT ' +
		'SELECT '''+v.Table_name+''' as Tbl_name, count(*) as cnt, '+ stuff(c_null.list,1,1,'') + ' FROM [dbo].['+v.Table_name +'] ' + --' WHERE 1=2 ' +
		' UNION ALL ' +
		'SELECT '''+v.Table_name+''' as Tbl_name, null as cnt, '+ stuff(c.list,1,1,'') + ' FROM OPENQUERY(LinkedServerName,''SELECT * FROM SchemaName.'+v.Table_name +''') ' + --' WHERE 1=2 '+
		'EXCEPT ' +
		'SELECT '''+v.Table_name+''' as Tbl_name, null as cnt, '+ stuff(c.list,1,1,'') + ' FROM [dbo].['+v.Table_name +'] ' + --' WHERE 1=2 '
		+ CHAR(13)+CHAR(10)
		, stuff(c.list,1,1,'') as cols
  FROM INFORMATION_SCHEMA.VIEWS v cross apply
	   (
		SELECT
          --',CAST(['+cast(c.COLUMN_NAME as varchar)+'] AS VARCHAR(3000)) AS ' +cast(c.COLUMN_NAME as varchar)+' ' as [text()]
          ',['+cast(c.COLUMN_NAME as varchar)+'] ' as [text()]
          FROM INFORMATION_SCHEMA.COLUMNS c
         WHERE c.DATA_TYPE != 'ntext'
           AND c.TABLE_NAME = v.table_name
--         GROUP BY c.TABLE_NAME
         ORDER BY ORDINAL_POSITION
           FOR XML PATH('')
       ) as c(list)
       CROSS APPLY
	   (
		SELECT
          ',NULL AS ['+cast(c.COLUMN_NAME as varchar)+']' as [text()]
          FROM INFORMATION_SCHEMA.COLUMNS c
         WHERE c.DATA_TYPE != 'ntext'
           AND c.TABLE_NAME = v.table_name-
--         GROUP BY c.TABLE_NAME
         ORDER BY ORDINAL_POSITION
           FOR XML PATH('')
       ) as c_null(list)
       --WHERE v.TABLE_NAME LIKE '%blabla%'

 ORDER BY v.TABLE_NAME
` |



Have fun, let me know if you have questions or comment to add notes or annotations.

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-iii/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Microsoft](https://www.ssp.sh/tags/microsoft/)
[MSSQL](https://www.ssp.sh/tags/mssql/)
[ORA-SQL](https://www.ssp.sh/tags/ora-sql/)
[Oracle](https://www.ssp.sh/tags/oracle/)
