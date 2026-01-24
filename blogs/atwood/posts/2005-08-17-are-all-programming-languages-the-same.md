---
title: "Are All Programming Languages The Same?"
date: 2005-08-17
url: https://blog.codinghorror.com/are-all-programming-languages-the-same/
slug: are-all-programming-languages-the-same
word_count: 850
---

There’s a chart in [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670) that compares the productivity of working in different languages:


> Programmers working with high-level languages achieve better productivity and quality than those working with lower-level languages. Languages such as C++, Java, Smalltalk, and Visual Basic have been credited with improving productivity, reliability, and comprehensibility by factors of 5 to 15 over low-level languages such assembly and C (Brooks 1987, Jones 1998, Boehm 2000). You save time when you don’t need to have an awards ceremony every time a C statement does what it’s supposed to do. Moreover, higher-level languages are more expressive than lower-level languages. Each line of code says more. The [following table] shows typical ratios of source statements in several high-level languages to the equivalent code in C. A higher ratio means that each line of code in the language listed accomplishes more than does each line of code in C.

kg-card-begin: html


| **Language** | **Level Relative to C** |
| C | 1 |
| C++ | 2.5 |
| Fortran | 2 |
| Java | 2.5 |
| Perl | 6 |
| Python | 6 |
| Smalltalk | 6 |
| MS Visual Basic | 4.5 |


kg-card-end: html

Fair enough. Des Traynor wondered if this table was valid, so he[ performed a simple test](https://web.archive.org/web/20090124205920/http://destraynor.com/serendipity/index.php?/archives/25-All-programming-languages-are-the-same....html): he provides examples of a tiny “read a file and print it to the console” app in Java, Perl, Python, and Ruby. I’ll reprint the smallest version here, which happens to be the Python implementation:

kg-card-begin: html

```

filename = “readAFile.py”
try:
for line in open(filename, ‘r’).readlines(): print line
except: print “Problem with %s” % filename

```

kg-card-end: html

For comparison, here’s the VB.NET 2005 version:

kg-card-begin: html

```

Module Module1
Sub Main()
Dim filename As String = “readAFile.vb”
Try
For Each line As String In System.IO.File.ReadAllLines(filename)
Console.WriteLine(line)
Next
Catch
Console.WriteLine(“Error reading file, or file not found.”)
End Try
End Sub
End Module

```

kg-card-end: html

And the C# 2005 version:

kg-card-begin: html

```

class Module1 {
static void Main(string[] args)	{
string filename = @“readAFile.cs”;
try {
foreach (string line in System.IO.File.ReadAllLines(filename)) {
System.Console.WriteLine(line);
}
}
catch {
System.Console.WriteLine(“File not found or error reading file.”);
}
}
}

```

kg-card-end: html

I had to edit the C# sample quite a bit to get rid of things that would have made the line count ridiculously large. Most notably, I removed the [stupid always-on namespace declaration](https://blog.codinghorror.com/a-modest-namespace-proposal/) (don’t get me started), added the System prefix to avoid the using, and folded leading curlies into the same line.


Anyway. Including the examples provided on Des’ page, that gives us a final line count tally of:

kg-card-begin: html


| **Language** | **Lines of code** |
| Java | 15 |
| C# 2005 | 8 |
| VB.NET 2005 | 8 |
| Ruby | 6 |
| Perl | 5 |
| Python | 4 |


kg-card-end: html

So, even with this trivial little example, there is a wide gap between “scripting” and “non-scripting” languages when it comes to lines of code. There’s plenty of existing research to support the claim that scripting languages offer higher productivity, such as the 2000 IEEE paper [An Empirical Comparison of Seven Programming Languages](http://doi.ieeecomputersociety.org/10.1109/2.876288) (free draft PDF):


> Despite these caveats, directly comparing different programming languages can provide meaningful insights. For example, I conclude from the study that Java’s memory overhead is still huge compared to C or C++, but its runtime efficiency has become quite acceptable. The scripting languages, however, offer reasonable alternatives to C and C++, even for tasks that must handle fair amounts of computation and data. Their relative runtime and memory-consumption overhead will often be acceptable, and they may offer significant advantages with respect to programmer productivity, at least for small programs like the phonecode problem.


That was written in 2000. Five years later, I am wondering if this distinction between “scripting” and “non-scripting” languages is as meaningful in a .NET world. If you examine the code samples above, you’ll notice that **most of the overhead in the “non-scripting” languages comes from the cruft associated with classes, functions, and object orientation**. The main work loop, if considered alone, is almost identical in every language!


So then, if language isn’t the real difference, what is? That very same language comparison paper offers this insight:


> For all program aspects investigated, the performance variability that derives from differences among programmers of the same language – as described by the bad-to-good ratios – is on average **as large or larger than the variability found among the different languages.**


It’s currently all the rage to propose that Ruby is changing [the face of software development](http://www.37signals.com/svn/archives/000592.php). I can definitely respect the passion behind this statement, but the actual data doesn’t support a magic bullet language effect. Given...

1. the abandonment of C++ and C for mainstream programming
2. the huge influence of individual programmer skill
3. the slow but steady adoption of scripting/dynamic language conventions in Java and .NET


... maybe all modern programming languages really *are *the same.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[productivity](https://blog.codinghorror.com/tag/productivity/)
[high-level languages](https://blog.codinghorror.com/tag/high-level-languages/)
[low-level languages](https://blog.codinghorror.com/tag/low-level-languages/)
