---
title: "In praise of PostgreSQL"
date: 2021-08-05
url: https://drewdevault.com/2021/08/05/In-praise-of-Postgres.html
slug: In-praise-of-Postgres
word_count: 713
---

After writing  [Praise for Alpine Linux](gemini://drewdevault.com/2021/05/06/Praise-for-Alpine-Linux.gmi) , I have decided to continue writing
more articles in praise of good software. Today, I’d like to tell you a bit
about  [PostgreSQL](https://www.postgresql.org) .

Many people don’t understand how old Postgres truly is: the first release 1 
was in July of 1996. It used this logo:

After 25 years of persistence, and a better logo design, Postgres stands today
as one of the most significant pillars of profound achievement in free software,
alongside the likes of Linux and Firefox. PostgreSQL has taken a complex problem
and  *solved*  it to such an effective degree that all of its competitors are
essentially obsolete, perhaps with the exception of SQLite.

For a start, Postgres is simply an incredibly powerful, robust, and reliable
piece of software, providing the best implementation of SQL. 2 
It provides a great deal of insight into its own behavior, and allows
the experienced operator to fine-tune it to achieve optimal performance. It
supports a broad set of SQL features and data types, with which I have always
been able to efficiently store and retrieve my data. SQL is usually the #1
bottleneck in web applications, and Postgres does an excellent job of providing
you with the tools necessary to manage that bottleneck.

Those tools are also exceptionally well-documented. The  [PostgreSQL
documentation](https://www.postgresql.org/docs/current/index.html)  is  *incredibly*  in-depth. It puts the rest of us to shame,
really. Not only do they have comprehensive reference documentation which
exhaustively describes every feature, but also vast amounts of prose which
explains the internal design, architecture, and operation of Postgres, plus
detailed plain-English explanations of how various high-level tasks can be
accomplished, complete with the necessary background to  *understand*  those
tasks. There’s essentially no reason to ever read a blog post or Stack Overflow
answer about how to do something with Postgres — the official docs cover
every aspect of the system in great depth.

The project is maintained by a highly disciplined team of engineers. I have
complete confidence in their abilities to handle matters of performance,
regression testing, and security. They publish meticulously detailed weekly
development updates, as well as thorough release notes that equips you with
sufficient knowledge to confidently run updates on your deployment. Their git
discipline is also legendary — here’s the  [latest commit](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=aa769f80ed80b7adfbdea9a6bc267ba4aeb80fd7)  at the time
of writing:

```
postgres_fdw: Fix issues with generated columns in foreign tables.

postgres_fdw imported generated columns from the remote tables as plain
columns, and caused failures like "ERROR: cannot insert a non-DEFAULT
value into column "foo"" when inserting into the foreign tables, as it
tried to insert values into the generated columns.  To fix, we do the
following under the assumption that generated columns in a postgres_fdw
foreign table are defined so that they represent generated columns in
the underlying remote table:

* Send DEFAULT for the generated columns to the foreign server on insert
  or update, not generated column values computed on the local server.
* Add to postgresImportForeignSchema() an option "import_generated" to
  include column generated expressions in the definitions of foreign
  tables imported from a foreign server.  The option is true by default.

The assumption seems reasonable, because that would make a query of the
postgres_fdw foreign table return values for the generated columns that
are consistent with the generated expression.

While here, fix another issue in postgresImportForeignSchema(): it tried
to include column generated expressions as column default expressions in
the foreign table definitions when the import_default option was enabled.

Per bug #16631 from Daniel Cherniy.  Back-patch to v12 where generated
columns were added.

Discussion: https://postgr.es/m/16631-e929fe9db0ffc7cf%40postgresql.org
```

[They’re all like this](https://git.postgresql.org/gitweb/?p=postgresql.git) .

Ultimately, PostgreSQL is a technically complex program which requires an
experienced and skilled operator to be effective. Learning to use it is a costly
investment, even if it pays handsomely. Though Postgres has occasionally
frustrated or confused me, on the whole my feelings for it are overwhelmingly
positive. It’s an incredibly well-made product and its enormous and
still-growing successes are very well-earned. When I think of projects which
have made the most significant impacts on the free software ecosystem, and on
the world at large, PostgreSQL has a place on that list.

1. The first release of Postgre**SQL**. Its lineage can be traced further back. ↩︎
2. No qualifiers. It’s straight-up the best implementation of SQL. ↩︎
