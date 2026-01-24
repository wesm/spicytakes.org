---
title: "A Visual Explanation of SQL Joins"
date: 2007-10-11
url: https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/
slug: a-visual-explanation-of-sql-joins
word_count: 632
---

I thought Ligaya Turmelle’s [post on SQL joins](https://web.archive.org/web/20071031012053/http://www.khankennels.com/blog/index.php/archives/2007/04/20/getting-joins/) was a great primer for novice developers. Since SQL joins *appear* to be set-based, the use of [Venn diagrams](https://en.wikipedia.org/wiki/Venn_diagram) to explain them seems, at first blush, to be a natural fit. However, like the commenters to her post, I found that the Venn diagrams didn’t quite match the [SQL join syntax](https://en.wikipedia.org/wiki/Join_(SQL)) reality in my testing.


I love the concept, though, so let’s see if we can make it work. Assume we have the following two tables. **Table A** is on the left, and **Table B** is on the right. We’ll populate them with four records each; note that only two of the records are matches, the ones in red.

kg-card-begin: html

```
id name       id  name
-- ----       --  ----
1  Pirate     1   Rutabaga
2  Monkey     2   Pirate
3  Ninja      3   Darth Vader
4  Spaghetti  4   Ninja
```

kg-card-end: html

Let’s join these tables by the name field in a few different ways and see if we can get a conceptual match to those nifty Venn diagrams.

kg-card-begin: html

```
SELECT * FROM TableA
INNER JOIN TableB
ON TableA.name = TableB.name

id  name       id   name
--  ----       --   ----
1   Pirate     2    Pirate
3   Ninja      4    Ninja
```

kg-card-end: html

**Inner join** produces only the set of records that match in both Table A and Table B.


![](https://blog.codinghorror.com/content/images/2025/03/6a0120a85dcdae970b012877702708970c-pi.png)

kg-card-begin: html

```
SELECT * FROM TableA
FULL OUTER JOIN TableB
ON TableA.name = TableB.name

id    name       id    name
--    ----       --    ----
1     Pirate     2     Pirate
2     Monkey     null  null
3     Ninja      4     Ninja
4     Spaghetti  null  null
null  null       1     Rutabaga
null  null       3     Darth Vader

```

kg-card-end: html

**Full outer join** produces the set of all records in Table A and Table B, with matching records from both sides where available. If there is no match, the missing side will contain null.


![](https://blog.codinghorror.com/content/images/2025/03/image-8.png)

kg-card-begin: html

```
SELECT * FROM TableA
LEFT OUTER JOIN TableB
ON TableA.name = TableB.name

id  name       id    name
--  ----       --    ----
1   Pirate     2     Pirate
2   Monkey     null  null
3   Ninja      4     Ninja
4   Spaghetti  null  null

```

kg-card-end: html

**Left outer join** produces a complete set of records from Table A, with the matching records (where available) in Table B. If there is no match, the right side will contain null.


![](https://blog.codinghorror.com/content/images/2025/03/image-9.png)

kg-card-begin: html

```
SELECT * FROM TableA
LEFT OUTER JOIN TableB
ON TableA.name = TableB.name
WHERE TableB.id IS null

id  name       id     name
--  ----       --     ----
2   Monkey     null   null
4   Spaghetti  null   null

```

kg-card-end: html

To produce the set of records only in Table A, but not in Table B, we perform the same left outer join, then **exclude the records we don’t want from the right side via a where clause**.


![](https://blog.codinghorror.com/content/images/2025/03/image-10.png)

kg-card-begin: html

```

SELECT * FROM TableA
FULL OUTER JOIN TableB
ON TableA.name = TableB.name
WHERE TableA.id IS null
OR TableB.id IS null

id    name       id    name
--    ----       --    ----
2     Monkey     null  null
4     Spaghetti  null  null
null  null       1     Rutabaga
null  null       3     Darth Vader

```

kg-card-end: html

To produce the set of records unique to Table A and Table B, we perform the same full outer join, then **exclude the records we don’t want from both sides via a where clause**.


![](https://blog.codinghorror.com/content/images/2025/03/image-11.png)


There’s also a cartesian product or **cross join**, which as far as I can tell, can’t be expressed as a Venn diagram:

kg-card-begin: html

```
SELECT * FROM TableA
CROSS JOIN TableB

```

kg-card-end: html

This joins “everything to everything,” resulting in 4 x 4 = 16 rows, far more than we had in the original sets. If you do the math, you can see why this is a *very* dangerous join to run against large tables.

[sql](https://blog.codinghorror.com/tag/sql/)
[joins](https://blog.codinghorror.com/tag/joins/)
[database](https://blog.codinghorror.com/tag/database/)
[venn diagrams](https://blog.codinghorror.com/tag/venn-diagrams/)
[syntax](https://blog.codinghorror.com/tag/syntax/)
