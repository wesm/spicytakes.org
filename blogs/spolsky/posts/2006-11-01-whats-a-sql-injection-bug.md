---
title: "What’s a SQL Injection Bug?"
date: 2006-11-01
url: https://www.joelonsoftware.com/2006/11/01/whats-a-sql-injection-bug/
word_count: 301
---


I tried to sign up for an online site.


The signup page wanted a secret question and secret answer. For the secret question, I put “what is aunt Vera’s cat’s color”. It complained about the apostrophe in the question. OK, fine. I deleted that apostrophe.


For the secret answer, I put “Aunt Vera doesn’t have a cat.”


And I got this:


1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ‘t have a cat’, ‘male’)’ at line 1


This means that the programmers are in the habit of taking strings that they got from the user (i.e. GET or POST parameters) and concatenating them together with other bits and pieces of SQL to generate SQL statements.


For example, in PHP with PostgreSQL:


`$x = pg_query("select * from accounts where name='" . $_GET["name"] . "'");`


(For non-PHP programmers: “.” is the string concatenation operator).


I’m not surprised that they are in the habit of doing this; a lot of programming books, tutorials, and documentation use examples like this.


Unfortunately it’s a gigantic security hole called SQL injection.


The user, if malicious, can close the string that you opened, finish your select statement, put in a semicolon (the SQL statement separator), and then type *any SQL code they want*, and it will run.


So, for example, if the user supplies this as *name*:


`foo'; delete from accounts --`


… the SQL statement executed will be:


`select * from accounts where name='foo'; delete from accounts --'`


… which will do exactly what it looks like: it will delete the entire table of accounts.


This is an extremely common problem: Michael Sutton did a little research project and found that [11.3% of web applications have SQL injection vulnerabilities](http://portal.spidynamics.com/blogs/msutton/archive/2006/09/26/How-Prevalent-Are-SQL-Injection-Vulnerabilities_3F00_.aspx).
