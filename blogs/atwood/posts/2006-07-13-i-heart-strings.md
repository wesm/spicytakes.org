---
title: "I Heart Strings"
date: 2006-07-13
url: https://blog.codinghorror.com/i-heart-strings/
slug: i-heart-strings
word_count: 513
---

[Brad Abrams](http://blogs.msdn.com/BradA/) was a founding member of the .NET common language runtime team way back in 1998. He’s also the co-author of [many essential books on .NET](http://www.amazon.com/exec/obidos/search-handle-url/field-keywords=brad%20abrams), including [both](http://www.amazon.com/exec/obidos/ASIN/0321154894/) [volumes](http://www.amazon.com/exec/obidos/ASIN/0321194454) of the .NET Framework Standard Library Annotated Reference. I was at a presentation Brad gave to the Triangle .NET User’s Group early in 2005. During the Q&A period, an audience member (and a friend of mine) asked Brad this question:


*What’s your favorite class in the .NET 1.1 common language runtime?*


His answer? **String.**


And that’s from a guy who will forget more about the .NET runtime than I will ever know about it. I still have my [.NET class library reference poster](http://www.amazon.com/exec/obidos/ASIN/0321288661), autographed by Brad right next to the String class.


I’ve always felt that **string is the most noble of datatypes**. Computers run on ones and zeros, sure, but people don’t. They use words, sentences, and paragraphs to communicate. People communicate with strings. The meteoric rise of HTTP, HTML, REST, serialization, and other heavily string-oriented, human-readable techniques vindicates – at least in my mind – my lifelong preference for the humble string.


Or, you could argue that we now have so much computing power and bandwidth available that passing friendly strings around in lieu of opaque binary data is actually practical. But don’t be a killjoy.


Guess what my favorite new .NET 2.0 feature is. Go ahead. Guess! Generics? Nope. Partial classes? Nope again. It’s the String.Contains method. And I’m awfully fond of String.IsNullOrEmpty, too.


What I love most about strings is that they have a million and one uses. They’re the swiss army knife of data types. [Regular expressions](https://blog.codinghorror.com/if-you-like-regular-expressions-so-much-why-dont-you-marry-them/), for example, are themselves strings, as is SQL.*

kg-card-begin: html

Regex.IsMatch(s, "<[a-z]|<!|&#|Won[a-z]*s*=|(scripts*:)|expression(")


kg-card-end: html
One of the classic uses for strings, going way [back to the C days](https://web.archive.org/web/20060720131652/http://www.phim.unibe.ch/comp_doc/c_manual/C/FUNCTIONS/format.html), is to specify output formats. Here’s an example of basic string formatting in .NET.
kg-card-begin: html


"Date is " + DateTime.Now.ToString("MM/dd hh:mm:ss");


kg-card-end: html
You can explicitly use the String.Format method to format, well, almost anything, including our date:
kg-card-begin: html


String.Format("Date is {0:MM/dd hh:mm:ss}", DateTime.Now);


kg-card-end: html
As [Karl Seguin](https://web.archive.org/web/20060719100435/http://codebetter.com/blogs/karlseguin/archive/2006/04/10/142602.aspx) points out, String.Format is a superior alternative to naive string concatenation:
kg-card-begin: html


Surely, I can’t be the only one that has a hard time writing and maintaining code like:



d.SelectSingleNode("/graph/data[name=’" + name + "’]");



When I do write code like the above, I almost always forget my closing quote or square bracket! And as things get more complicated, it becomes a flat out nightmare.


The solution is to make heavy use of string.Format. You’ll never EVER see me use plus to concatenate something to a string, and there’s no reason you should either. To write the above code better, try:



d.SelectSingleNode(string.Format("/graph/data[name=’{0}’]", name));



kg-card-end: html
It’s a win-win scenario: you get more power and more protection. For a complete rundown of the zillion possible String.Format specifiers, try these links:SteveX Compiled - [String Formatting in C#](http://blog.stevex.net/index.php/string-formatting-in-csharp/)Kathy Kam - [.NET Format String 101](https://web.archive.org/web/20060719110607/http://blogs.msdn.com/kathykam/archive/2006/03/29/564426.aspx)Kit George - [String Formatting FAQ](https://web.archive.org/web/20060902114437/http://msdn.microsoft.com:80/netframework/programming/bcl/faq/StringFormattingFAQ.aspx)MSDN - Formatting TypesString class, *you complete me*.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[.net](https://blog.codinghorror.com/tag/net/)
[strings](https://blog.codinghorror.com/tag/strings/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
