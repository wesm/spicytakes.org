---
title: "Migrate from Oracle to Microsoft (Views) – Part I"
date: 2016-09-24
url: https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-i/
slug: migrate-from-oracle-to-microsoft-views-part-i
word_count: 1456
---

![Migrate from Oracle to Microsoft (Views) – Part I](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-i/images/microsoft-sql-server-vs-oracle.jpg)

Contents

Sometimes you have to migrate from an Oracle database to a Microsoft SQL Server. I’m not going into the reason that could be behind. I had different projects where I had to achieve this goal. The issues that I faced is what I would like to share with you.


## Different functions


When it comes to rewrite code from Ora-SQL to MS-SQL, in my case it were Oracle Views that had to be transfered to Microsoft Views, then the first thing you figure out is, that there’s not the same built in functions on both sides. For example the well know `TO_NUMBER()` or `TO_CHAR()` in Oracle dosen’t exist in Microsoft. So what you do?

Below you see a list of the common functions compared between the two technologies:



| Description | Oracle | MS SQL Server |
|  |  |  |
| Smallest integer >= n | CEIL | CEILING |
| Modulus | MOD | % |
| Truncate number | TRUNC |  |
| Max or min number or string in list | GREATEST,
LEAST |  |
| Translate NULL to n | NVL | ISNULL |
| Return NULL if two values are equal | DECODE | NULLIF |
| String concatenation | CONCAT(str1,str2) | str1 + str2 |
| Convert ASCII to char | CHR | CHAR |
| Capitalize first letters of words | INITCAP |  |
| Find string in string | INSTR | CHARINDEX |
| Find pattern in string | INSTR | PATINDEX |
| String length | LENGTH | DATALENGTH |
| Pad string with blanks | LPAD,
RPAD |  |
| Trim leading or trailing chars other than blanks | LTRIM(str,chars),
RTRIM(str,chars) |  |
| Replace chars in string | REPLACE | STUFF |
| Convert number to string | TO_CHAR | STR, CAST |
| Convert string to number | TO_NUMBER | CAST |
| Get substring from string | SUBSTR | SUBSTRING |
| Char for char translation in string | TRANSLATE |  |
| Date addition | ADD_MONTH or + | DATEADD |
| Date subtraction | MONTHS_BETWEEN or - | DATEDIFF |
| Last day of month | LAST_DAY |  |
| Time zone conversion | NEW_TIME |  |
| Next specified weekday after date | NEXT_DAY |  |
| Convert date to string | TO_CHAR | DATENAME, CONVERT |
| Convert string to date | TO_DATE | CAST |
| Convert date to number | TO_NUMBER(TO_CHAR(d)) | DATEPART |
| Date round | ROUND | CONVERT |
| Date truncate | TRUNC | CONVERT |
| Current date | SYSDATE | GETDATE |
| Convert hex to binary | HEXTORAW | CAST |
| Convert binary to hex | RAWTOHEX | CONVERT |
| If statement in an expression | DECODE | CASE … WHEN
or COALESCE |
| User’s login id number or name | UID, USER | SUSER_ID, SUSER_NAME |
| User’s database id number or name | UID, USER | USER_ID, USR_NAME |
| Current user | USER | USER |



Source: [dba-oracle.com](http://www.dba-oracle.com/oracle_news/2005_12_16_sql_syntax_differences.htm)


## Examples


### TO_CHAR replaced by CONVERT


**Oracle**:



| `1
2
` | `-- Convert the current date to YYYY-MM-DD format
SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD') FROM dual;
` |



**SQL Server**:



| `1
2
` | `--Convert the current date to YYYY-MM-DD format
SELECT CONVERT(VARCHAR(10), GETDATE(), 120);
` |



### TO_NUMBER replaced by CONVERT(float,..), CAST()


As you can see in the list above, you can use `CAST`, also `CONVERT` is possible. But attention, it sounds like a very easy translation, but you have to be careful, for instance when it comes to decimals. Because the built-in `TO_NUMBER()` function rounds at the 16th decimal place and if you use `CONVERT`, the behavior is a bit different.


I used `CONVERT(numeric,..)` for my needs, but as you can see below, the rounding of decimals is not the same:



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
` | `--TO_NUMBER rounds at the 16th decimal place
select to_number('555.555999999999996699999999999999') from dual
--> 555.5559999999999967

--Float rounds it already at the 3rd precision
select CONVERT(float, '555.555999999999996699999999999999')
--> 555.556

--numeric instead shows it as a integer
select CONVERT(numeric, 555.555999999999996699999999999999)
--> 556
` |



Combined with Modulo (mod / %) you have to keep this in mind:



| `1
2
3
4
5
6
7
8
` | `SELECT (CONVERT(numeric,88.62673565)  % 6)
	,(CONVERT(decimal,88.62673565)  % 6)
	,(CONVERT(money,88.62673565)  % 6)
	,(CONVERT(INT,88.62673565)  % 6)
	, (CAST(88.62673565 AS numeric)  % 6)
	, (88.62673565  % 6)

-->	5	5	4.6267	4	5	4.62673565
` |



See more oracle built-in function conversion to SQL-Server in the attachment below.


Continue reading about performance in my part II [Migrate from Oracle to Microsoft (Views) – Part II](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-ii/).


## Attachment



| `  1
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
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
` | `-- =============================================================================================
-- Author:		Simon Späti
-- Create date: 16.09.2015
------------------------------------------------------------------------------------------------
-- Description:	Gibt den String als Varchar zurück. Achtung Oracle TO_CHAR unterstützt noch
-- Formatierungen, welche diese nicht unterstützt. Dieese werden aber im Umfang der
-- *Oracle-und MS-SQL Scripte Migration nicht verwendet
-- =============================================================================================
CREATE FUNCTION [dbo].[TO_CHAR] (@str VARCHAR(8000))
  RETURNS VARCHAR(8000)
  AS
  BEGIN
	RETURN CONVERT(varchar, @str);
  END

GO

-- =============================================================================================
-- Author:		Simon Späti
-- Create date: 16.09.2015
------------------------------------------------------------------------------------------------
-- Description:	Gibt den String als Zahl zurück. Achtung bei Kommastellen!
-- =============================================================================================
CREATE FUNCTION [dbo].[TO_NUMBER] (@str VARCHAR(4000))
  RETURNS numeric
  AS
  BEGIN
	RETURN CONVERT(numeric,@str);
  END
GO

-- =============================================================================================
-- Author:		Simon Späti
-- Create date: 16.09.2015
------------------------------------------------------------------------------------------------
-- Description:	Gibt den Modulo Wert zweier Zahlen aus. Achtung bei Kommastellen!
-- =============================================================================================
CREATE FUNCTION [dbo].[MOD] (@numb numeric, @mod int)
  RETURNS numeric
  AS
  BEGIN
	RETURN @numb % @mod;
  END

GO

-- =============================================================================================
-- Author:		Simon Späti
-- Create date: 16.09.2015
------------------------------------------------------------------------------------------------
-- Description:	Gibt die Position eines Substrings in einem String zurück, dabei wird im String
-- ab der angegebenen Startposition (@start) nach dem durch den Parameter @occurrence (Zahl > 0)
-- angegebenen Auftreten vom Substring ab der Startposition gesucht. Die Startposition wird durch
-- den Parameter @start (Zahl <> 0) ermittelt, indem es bei einer positiven Zahl ab dem String-
-- Anfang nach rechts und bei einer negativen Zahl ab dem String-Ende nach links bis zu dieser
-- Zahl gezählt wird.
--                        @str____________ @substr @start @occurrence
-- Beispiele: dbo.instr ('BO_PKZ_05.10.10','.'    ,-1    ,1          ) = 13
--		      dbo.instr ('1-345-7-9'      ,'-'    ,-5    ,1          ) = 2
--			  dbo.instr	('abcdabcd'		  ,'abc'  ,-1	 ,2			 ) = 1
-- =============================================================================================
CREATE FUNCTION [dbo].[INSTR] (@str VARCHAR(8000), @substr VARCHAR(255), @start INT, @occurrence INT)
  RETURNS INT WITH SCHEMABINDING --New WITH SCHEMABINDING
  AS
  BEGIN
	DECLARE @count INT = @occurrence,
			@found INT = 0,
			@pos INT = 0;
	IF @start = 0
		RETURN -1;
	IF @start > 0
		SET @pos = @start;
	ELSE
		SET @pos = - @start;
	WHILE @count > 0
	BEGIN
		IF @start > 0
			SET @found = CHARINDEX(@substr, @str, @pos);
		ELSE
			SET @found = CHARINDEX(REVERSE(@substr), REVERSE(@str), @pos);
		IF @found > 0
		BEGIN
			SET @pos = @found + 1;
		END
		SET @count = @count - 1;
	END --WHILE @count > 0
	IF @start < 0 AND @found > 0
			SET @found = LEN (@Str)- @found + 1 -LEN (@substr)+1;
	RETURN @found;
  END
GO

-- =============================================================================================
-- Author:		Simon Späti
-- Create date: 16.09.2015
------------------------------------------------------------------------------------------------
-- Description:	Gibt den Substring eines Strings zurück, der an der mit dem angegebenen Position
-- ("start") startet und die angegebene Länge ("length") hat oder per Default bis zum Ende des
-- Strings. Bei negativen Argumenten @start oder @length wird der leere String zurückgegeben ohne
-- einen Fehler hervorzurufen.
-- =============================================================================================
CREATE FUNCTION [dbo].[SUBSTR] (@str VARCHAR(8000), @start INT, @length INT=0)
  RETURNS VARCHAR(255) WITH SCHEMABINDING --New WITH SCHEMABINDING
  AS
  BEGIN
	DECLARE @result VARCHAR(255) = '',
			@length_1 INT = 0;
	IF @length = 0
		set @length_1 = LEN(@str)-- default
	ELSE
		set @length_1 = @length
	IF @length_1 > 0
	BEGIN
		IF @start >= 0
			set @result = SUBSTRING(@str, @start, @length_1)
		ELSE
			set @result = SUBSTRING (@str, LEN(@str)+ @start + 1 ,@length_1)
	END
	RETURN @result
  END

GO
` |


[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-i/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Microsoft](https://www.ssp.sh/tags/microsoft/)
[MSSQL](https://www.ssp.sh/tags/mssql/)
[ORA-SQL](https://www.ssp.sh/tags/ora-sql/)
[Oracle](https://www.ssp.sh/tags/oracle/)
