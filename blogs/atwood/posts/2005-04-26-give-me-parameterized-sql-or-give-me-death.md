---
title: "Give me parameterized SQL, or give me death"
date: 2005-04-26
url: https://blog.codinghorror.com/give-me-parameterized-sql-or-give-me-death/
slug: give-me-parameterized-sql-or-give-me-death
word_count: 287
---

I have fairly strong feelings when it comes to the [stored procedures versus dynamic SQL](https://blog.codinghorror.com/who-needs-stored-procedures-anyways/) argument, but one thing is clear: you should never, ever use concatenated SQL strings in your applications. **Give me parameterized SQL, or give me death.** There are two good reasons you should never do this.


First, consider this naive concatenated SQL:

kg-card-begin: html

```
SELECT email, passwd, login_id, full_name
FROM members
WHERE email = 'x';
```

kg-card-end: html

Code like this **opens your app to SQL injection attacks**, and it’s a huge, gaping vulnerability. Steve Friedl’s [SQL Injection Attacks by Example](http://www.unixwiz.net/techtips/sql-injection.html) provides an excellent visual blow-by-blow of what *can* happen when you write code this naive. Here’s the Reader’s Digest version:

kg-card-begin: html

```
SELECT email, passwd, login_id, full_name
FROM members
WHERE email = 'x' OR full_name LIKE '%Bob%';
```

kg-card-end: html

I know what you’re thinking. No, escaping the strings doesn’t protect you; see Steve’s article.


Second, **parameterized SQL performs better**. A *lot* better. Consider the parameterized version of the above:

kg-card-begin: html

```
SqlConnection conn = new SqlConnection(_connectionString);
conn.Open();
string s = "SELECT email, passwd, login_id, full_name " +
"FROM members WHERE email = @email";
SqlCommand cmd = new SqlCommand(s);
cmd.Parameters.Add("@email", email);
SqlDataReader reader = cmd.ExecuteReader();
```

kg-card-end: html

This code offers the following pure performance benefits:

- Fewer string concatenations
- No need to worry about any kind of manual string escaping
- A more generic query form is presented to db, so it’s likely already hashed and stored as a pre-compiled execution plan
- Smaller strings are sent across the wire


Non-parameterized SQL is [the GoTo statement](https://web.archive.org/web/20060613021431/http://www.acm.org/classics/oct95/) of database programming. Don’t do it, and make sure your coworkers don’t either.

[security](https://blog.codinghorror.com/tag/security/)
[sql injection](https://blog.codinghorror.com/tag/sql-injection/)
[parameterized sql](https://blog.codinghorror.com/tag/parameterized-sql/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[databases](https://blog.codinghorror.com/tag/databases/)
