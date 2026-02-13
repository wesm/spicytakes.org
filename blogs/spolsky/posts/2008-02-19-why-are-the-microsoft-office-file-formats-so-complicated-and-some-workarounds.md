---
title: "Why are the Microsoft Office file formats so complicated? (And some workarounds)"
date: 2008-02-19
url: https://www.joelonsoftware.com/2008/02/19/why-are-the-microsoft-office-file-formats-so-complicated-and-some-workarounds/
word_count: 2401
---


Last week, Microsoft published the [binary file formats for Office](http://www.microsoft.com/interop/docs/OfficeBinaryFormats.mspx). These formats appear to be almost completely insane. The Excel 97-2003 file format is a 349 page PDF file. But wait, that’s not all there is to it! This document includes the following interesting comment:


> Each Excel workbook is stored in a compound file.


You see, Excel 97-2003 files are OLE compound documents, which are, essentially, file systems inside a single file. These are sufficiently complicated that you have to read another 9 page spec to figure that out. And these “specs” look more like C data structures than what we traditionally think of as a spec. It’s a whole hierarchical file system.


If you started reading these documents with the hope of spending a weekend writing some spiffy code that imports Word documents into your blog system, or creates Excel-formatted spreadsheets with your personal finance data, the complexity and length of the spec probably cured you of that desire pretty darn quickly. A normal programmer would conclude that Office’s binary file formats:

- are deliberately obfuscated
- are the product of a demented Borg mind
- were created by insanely bad programmers
- and are impossible to read or create correctly.


You’d be wrong on all four counts. With a little bit of digging, I’ll show you how those file formats got so unbelievably complicated, why it doesn’t reflect bad programming on Microsoft’s part, and what you can do to work around it.


The first thing to understand is that the binary file formats were designed with very different design goals than, say, HTML.


**They were designed to be fast on very old computers.** For the early versions of Excel for Windows, 1 MB of RAM was a reasonable amount of memory, and an 80386 at 20 MHz had to be able to run Excel comfortably. There are a lot of optimizations in the file formats that are intended to make opening and saving files much faster:

- These are binary formats, so loading a record is usually a matter of just copying (blitting) a range of bytes from disk to memory, where you end up with a C data structure you can use. There’s no lexing or parsing involved in loading a file. [Lexing and parsing are orders of magnitude slower than blitting](https://www.joelonsoftware.com/articles/fog0000000319.html).
- The file format is contorted, where necessary, to make common operations fast. For example, Excel 95 and 97 have something called “Simple Save” which they use sometimes as a faster variation on the OLE compound document format, which just wasn’t fast enough for mainstream use. Word had something called [Fast Save](http://support.microsoft.com/kb/197978). To save a long document quickly, 14 out of 15 times, only the changes are appended to the end of the file, instead of rewriting the whole document from scratch. On the hard drives of the day, this meant saving a long document took one second instead of thirty. (It also meant that deleted data in a document was still in the file. [This turned out to be not what people wanted](http://www.news.com/8301-10784_3-9780073-7.html).)


**They were designed to use libraries.** If you wanted to write a from-scratch binary importer, you’d have to support things like the Windows Metafile Format (for drawing things) and OLE Compound Storage. If you’re running on Windows, there’s library support for these that makes it trivial… using these features was a shortcut for the Microsoft team. But if you’re writing everything on your own from scratch, you have to do all that work yourself.


Office has extensive support for compound documents, for example, you can embed a spreadsheet in a Word document. A perfect Word file format parser would also have to be able to do something intelligent with the embedded spreadsheet.


**They were not designed with interoperability in mind.** The assumption, and a fairly reasonable one at the time, was that the Word file format only had to be read and written by Word. That means that whenever a programmer on the Word team had to make a decision about how to change the file format, the only thing they cared about was (a) what was fast and (b) what took the fewest lines of code *in the Word code base*. The idea of things like SGML and HTML—interchangeable, standardized file formats—didn’t really take hold until the Internet made it practical to interchange documents in the first place; this was a decade later than the Office binary formats were first invented. There was always an assumption that you could use importers and exporters to exchange documents. In fact Word does have a format designed for easy interchange, called [RTF](http://en.wikipedia.org/wiki/Rich_Text_Format), which has been there almost since the beginning. It’s still 100% supported.


**They have to reflect all the complexity of the applications.** Every checkbox, every formatting option, and every feature in Microsoft Office has to be represented in file formats somewhere. That checkbox in Word’s paragraph menu called “Keep With Next” that causes a paragraph to be moved to the next page if necessary so that it’s on the same page as the paragraph after it? That has to be in the file format. And that means if you want to implement a perfect Word clone than can correctly read Word documents, you have to implement that feature. If you’re creating a competitive word processor that has to load Word documents, it may only take you a minute to write the code to load that bit from the file format, but it might take you weeks to change your page layout algorithm to accommodate it. If you don’t, customers will open their Word files in your clone and all the pages will be messed up.


**They have to reflect the history of the applications. **A lot of the complexities in these file formats reflect features that are old, complicated, unloved, and rarely used. They’re still in the file format for backwards compatibility, and because it doesn’t cost anything for Microsoft to leave the code around. But if you really want to do a thorough and complete job of parsing and writing these file formats, you have to redo all that work that some intern did at Microsoft 15 years ago. The bottom line is that there are **thousands of developer years** of work that went into the current versions of Word and Excel, and if you really want to clone those applications completely, you’re going to have to do thousands of years of work. A file format is just a concise summary of all the features an application supports.


Just for kicks, let’s look at one tiny example in depth. An Excel worksheet is a bunch of BIFF records of different types. I want to look at the very first BIFF record in the spec. It’s a record called **1904**.


The Excel file format specification is remarkably obscure about this. It just says that the 1904 record indicates “if the 1904 date system is used.” Ah. A classic piece of useless specification. If you were a developer working with the Excel file format, and you found this in the file format specification, you might be justified in concluding that Microsoft is hiding something. This piece of information does not give you enough information. You also need some [outside knowledge](http://support.microsoft.com/kb/214330), which I’ll fill you in on now. There are two kinds of Excel worksheets: those where the epoch for dates is 1/1/1900 (with a [leap-year bug](http://support.microsoft.com/kb/214058/) deliberately created for 1-2-3 compatibility that is too boring to describe here), and those where the epoch for dates is 1/1/1904. Excel supports both because the first version of Excel, for the Mac, just used that operating system’s epoch because that was easy, but Excel for Windows had to be able to import 1-2-3 files, which used 1/1/1900 for the epoch. It’s enough to bring you to tears. At no point in history did a programmer ever not do the right thing, but there you have it.


Both 1900 and 1904 file types are commonly found in the wild, usually depending on whether the file originated on Windows or Mac. Converting from one to another silently can cause data integrity errors, so Excel won’t change the file type for you. To parse Excel files you have to handle both. That’s not just a matter of loading this bit from the file. It means you have to rewrite all of your date display and parsing code to handle both epochs. That would take several days to implement, I think.


Indeed, as you work on your Excel clone, you’ll discover all kinds of subtle details about date handling. When does Excel convert numbers to dates? How does the formatting work? Why is 1/31 interpreted as January 31 of this year, while 1/50 is interpreted as January 1st, 1950? All of these subtle bits of behavior cannot be fully documented without writing a document that has the same amount of information as the Excel source code.


And this is only the first of hundreds of BIFF records you have to handle, and one of the simplest. Most of them are complicated enough to reduce a grown programmer to tears.


The only possible conclusion is this. It’s very helpful of Microsoft to release the file formats for Microsoft and Office, but it’s not really going to make it any easier to import or save to the Office file formats. These are insanely complex and rich applications, and you [can’t just implement the most popular 20% and expect 80% of the people to be happy](https://www.joelonsoftware.com/articles/fog0000000020.html). The binary file specification is, at most, going to save you a few minutes reverse engineering a remarkably complex system.


OK, I promised some workarounds. The good news is that for almost all common applications, trying to read or write the Office binary file formats is the wrong decision. There are two major alternatives you should seriously consider: letting Office do the work, or using file formats that are easier to write.


**Let Office do the heavy work for you**. Word and Excel have extremely complete object models, available via COM Automation, which allow you to programmatically do *anything*. In many situations, you are better off reusing the code inside Office rather than trying to reimplement it. Here are a few examples.

1. You have a web-based application that’s needs to output existing Word files in PDF format. Here’s how I would implement that: a few lines of Word VBA code loads a file and saves it as a PDF using the built in PDF exporter in Word 2007. You can call this code directly, even from ASP or ASP.NET code running under IIS. It’ll work. The first time you launch Word it’ll take a few seconds. The second time, Word will be kept in memory by the COM subsystem for a few minutes in case you need it again. It’s fast enough for a reasonable web-based application.
2. Same as above, but your web hosting environment is Linux. Buy one Windows 2003 server, install a fully licensed copy of Word on it, and build a little web service that does the work. Half a day of work with C# and ASP.NET.
3. Same as above, but you need to scale. Throw a load balancer in front of any number of boxes that you built in step 2. No code required.


This kind of approach would work for all kinds of common Office types of applications you might perform on your server. For example:

- Opening an Excel workbook, storing some data in input cells, recalculating, and pulling some results out of output cells
- Using Excel to generate charts in GIF format
- Pulling just about any kind of information out of any kind of Excel worksheet without spending a minute thinking about file formats
- Converting Excel file formats to CSV tabular data (another approach is to use [Excel ODBC drivers](http://support.microsoft.com/kb/178717) to suck data out using SQL queries).
- Editing Word documents
- Filling out Word forms
- Converting files between any of the many file formats supported by Office (there are importers for dozens of word processor and spreadsheet formats)


In all of these cases, there are ways to tell the Office objects that they’re not running interactively, so they shouldn’t bother updating the screen and they shouldn’t prompt for user input. By the way, if you go this route, there are a few gotchas, and it’s not officially supported by Microsoft, so read their [knowledge base article](http://support.microsoft.com/default.aspx?scid=kb;EN-US;257757) before you get started.


**Use a simpler format for writing files**. If you merely have to *produce *Office documents programmatically, there’s almost always a better format than the Office binary formats that you can use which Word and Excel will open happily, without missing a beat.

- If you simply have to produce tabular data for use in Excel, consider CSV.
- If you really need worksheet calculation features that CSV doesn’t support, the [WK1 format](http://www.schnarff.com/file-formats/index.html) (Lotus 1-2-3) is a heck of a lot simpler than Excel, and Excel will open it fine.
- If you really, really have to generate native Excel files, find an extremely old version of Excel… Excel 3.0 is a good choice, before all the compound document stuff, and save a minimum file containing only the exact features you want to use. Use this file to see the exact minimum BIFF records that you have to output and just focus on that part of the spec.
- For Word documents, consider writing HTML. Word will open those fine, too.
- If you really want to generate fancy formatted Word documents, your best bet is to create an RTF document. Everything that Word can do can be expressed in RTF, but it’s a text format, not binary, so you can change things in the RTF document and it’ll still work. You can create a nicely formatted document with placeholders in Word, save as RTF, and then using simple text substitution, replace the placeholders on the fly. Now you have an RTF document that every version of Word will open happily.


Anyway, unless you’re literally trying to create a competitor to Office that can read and write all Office files perfectly, in which case, you’ve got thousands of years of work cut out for you, chances are that reading or writing the Office binary formats is the most labor intensive way to solve whatever problem it is that you’re trying to solve.
