---
title: "Embracing Languages Inside Languages"
date: 2007-10-30
url: https://blog.codinghorror.com/embracing-languages-inside-languages/
slug: embracing-languages-inside-languages
word_count: 868
---

Martin Fowler loosely defines [a fluent interface](http://www.martinfowler.com/bliki/FluentInterface.html) thusly: “The more the use of the API has that language like flow, the more fluent it is.” If you detect a whiff of skepticism here, you’re right: I’ve never seen this work. [Computer languages aren’t human languages](https://blog.codinghorror.com/computer-languages-arent-human-languages/).


Let’s look at a concrete example [from Joshua Flanagan](http://flimflan.com/blog/ReadableRegularExpressions.aspx). Here’s how we define a regular expression in the standard way:

kg-card-begin: html

```

<divs*class="game"s*id="(?<gameID>d+)-game"(?<content>.*?)
<!--gameStatuss*=s*(?<gameState>d+)-->

```

kg-card-end: html

Here’s how we’d define that same regular expression in Joshua’s fluent interface.

kg-card-begin: html

```

Pattern findGamesPattern = Pattern.With.Literal(@"<div")
.WhiteSpace.Repeat.ZeroOrMore
.Literal(@"class=""game""").WhiteSpace.Repeat.ZeroOrMore.Literal(@"id=""")
.NamedGroup("gameId", Pattern.With.Digit.Repeat.OneOrMore)
.Literal(@"-game""")
.NamedGroup("content", Pattern.With.Anything.Repeat.Lazy.ZeroOrMore)
.Literal(@"<!--gameStatus")
.WhiteSpace.Repeat.ZeroOrMore.Literal("=").WhiteSpace.Repeat.ZeroOrMore
.NamedGroup("gameState", Pattern.With.Digit.Repeat.OneOrMore)
.Literal("-->");

```

kg-card-end: html

So **we’re replacing a nice, succinct one line regular expression with ten lines of objects, methods, and named enumerations.** This is progress?


I’ll grant you that I am probably unusually familiar with regular expressions, even by developer standards. There’s a reason they have a reputation for being dense and inscrutable. I’ve definitely seen some [incredibly bad regular expressions](https://blog.codinghorror.com/regex-use-vs-regex-abuse/) in my day. But in my professional opinion, that regex was a well written one. I had no problem reading it. Adding a ton of hyper-dense object wrappers to that regex makes it *harder* for me to understand what it does.


The new syntax Joshua invented is great, but it’s specific to his implementation. Although it may seem like a good idea to use these kinds of training wheels to “learn” regular expressions, I’d argue that you aren’t learning them at all. And that’s a shame, because regular expression syntax is a mini-language of its own. Once you learn it, you can use it anywhere; it works ([almost](http://www.regular-expressions.info/refext.html)) the same in every environment.


The [Subsonic project](https://web.archive.org/web/20071030235900/http://www.subsonicproject.com/) attempts to do something similar for SQL. Consider this SQL query:

kg-card-begin: html

```

SELECT * from Customers WHERE Country = "USA"
ORDER BY CompanyName

```

kg-card-end: html

Here’s how we would express that same SQL query in SubSonic’s fluent interface:

kg-card-begin: html

```

CustomerCollection c = new CustomerCollection();
c.Where(Customer.Columns.Country, "USA");
c.OrderByAsc(Customer.Columns.CompanyName);
c.Load();

```

kg-card-end: html

I’ve mentioned before that I’m no fan of [object-oriented rendering](https://blog.codinghorror.com/when-object-oriented-rendering-is-too-much-code/) when a simple string will suffice. That’s exactly the reaction I had here; why in the world would I want to use four lines of code instead of one? This seems like a particularly egregious example. **The SQL is harder to write and more difficult to understand when it’s wrapped in all that proprietary SubSonic object noise.** Furthermore, if you don’t learn the underlying SQL – and how databases work – you’re in serious trouble as a software developer.


But I can see the rationale behind these types of database code generation tools:

1. They “solve” [the object-relational mapping problem](https://blog.codinghorror.com/object-relational-mapping-is-the-vietnam-of-computer-science/) for you (and if you believe that, I have a bridge you might be interested in)
2. you get intelligence
3. your database is strongly typed
4. the compiler now “understands” the database, or at least the generated classes that represent the database.


I definitely sympathize with the desire to produce less code, and that’s the whole point of database code generation tools. Personally, I would argue that most of these benefits could be realized with smarter IDEs that actually understood native SQL strings (or regular expressions), rather than relying on a slew of generated code and complicated, proprietary object syntax.


But let’s take a step back and think about what’s *really* happening here. In both cases, **we are embedding one language inside another**. SQL is a language. Regular expressions are a language. Wrapping those languages inside a bunch of mega-verbose fluent interface ObjectJunk – just so we can pretend we’re writing code in our primary language – is a *total cop-out*. Fluent interface object wrappers feel like a nasty hack to me.


Why can’t we embrace the language-inside-a-language paradigm, rather than running and hiding from it? These domain specific languages exist because they are optimized for processing strings and data efficiently. Avoiding them is counterproductive.


Perhaps the ultimate solution is to **redefine the underlying language to incorporate the features of another language**.


Consider how Perl integrates the regular expression language:

kg-card-begin: html

```

while (my $line = <IN>) {
while ( $line =~ /(Romeo|Juliet|Mercutio|Tybalt|Friar w+)/g ) {
my $character = $1;
++$counts{ $character };
}
}

```

kg-card-end: html

Here’s how C# 3.0, with [LINQ](http://en.wikipedia.org/wiki/Language_Integrated_Query), integrates the SQL language:

kg-card-begin: html

```

var c = from Customer in Customers
where Customer.Country == "USA"
orderby Customer.CompanyName
select Customer;

```

kg-card-end: html

Note the conspicuous lack of ObjectJunk. No explosion at the parens and periods factory. No MassivelyLongTextEnumerations to deal with. There’s nothing but code that *looks like exactly what it does*. And that’s a beautiful thing.


**Embrace the idea of languages inside languages**. In The Land of Strings, we speak regular expressions. In The Land of Data, we speak SQL. Oh sure, you can pretend those languages don’t exist, and hide out in the [Kingdom of Nouns](http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html) – but you’re only cheating yourself out of a deeper understanding of how things *really *work in those other places. Fluent interface object wrappers may seem like a helpful convenience, but they’re actually an ugly hack, and a terrible substitute for true language integration.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[fluent interface](https://blog.codinghorror.com/tag/fluent-interface/)
[api](https://blog.codinghorror.com/tag/api/)
